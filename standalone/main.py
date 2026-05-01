"""
main.py — FastAPI service exposing the standalone auditor.

Three endpoints:
    POST /audit          — kick off an audit (async, returns audit_id)
    GET  /audit/{id}     — fetch status + result (poll until completed)
    GET  /healthz        — service health check

Plus convenience routes:
    GET /audit/{id}.json — raw JSON
    GET /audit/{id}.md   — Markdown report
    GET /audit/{id}.pdf  — PDF summary
    GET /audit/{id}.html — preview-friendly HTML render

USAGE
    pip install fastapi uvicorn anthropic python-dotenv
    export ANTHROPIC_API_KEY="sk-ant-..."
    uvicorn main:app --host 0.0.0.0 --port 8000

ENVIRONMENT VARIABLES
    ANTHROPIC_API_KEY  — required for audit narrative generation
    AUDIT_OUTPUT_DIR   — where to write audit artifacts (default: ./audits/)
    PORT               — port to bind (default: 8000)
"""

from __future__ import annotations

import os
import sys
import threading
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Optional

# Load .env if present (graceful fallback if python-dotenv not installed)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse, PlainTextResponse
from pydantic import BaseModel, HttpUrl

from audit_pipeline import run_audit


# ----------------------------------------------------------------------
# CONFIG
# ----------------------------------------------------------------------

OUTPUT_DIR = Path(os.getenv('AUDIT_OUTPUT_DIR', './audits/')).expanduser().resolve()
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# In-memory job tracker (sufficient for single-instance v1).
# For multi-instance scale, swap for Redis or DB.
JOBS: Dict[str, Dict] = {}
JOBS_LOCK = threading.Lock()


# ----------------------------------------------------------------------
# REQUEST / RESPONSE MODELS
# ----------------------------------------------------------------------

class AuditRequest(BaseModel):
    url: HttpUrl


class AuditResponse(BaseModel):
    audit_id: str
    status: str  # 'queued' | 'running' | 'completed' | 'error'
    message: str
    poll_url: str


class AuditStatusResponse(BaseModel):
    audit_id: str
    status: str
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    duration_seconds: Optional[float] = None
    error: Optional[str] = None
    result_summary: Optional[dict] = None
    artifacts: Optional[dict] = None


# ----------------------------------------------------------------------
# FASTAPI APP
# ----------------------------------------------------------------------

app = FastAPI(
    title='AEO/SEO/GEO Auditor',
    description='Standalone deterministic website audit service. '
                'Powered by 12,764-entry Sieve brain + Anthropic Sonnet 4.6.',
    version='4.0',
)


@app.get('/')
def root():
    return {
        'service': 'aeo-seo-auditor',
        'version': '4.0',
        'endpoints': {
            'POST /audit': 'Submit a URL for audit',
            'GET /audit/{id}': 'Fetch status + result',
            'GET /audit/{id}.{json,md,pdf}': 'Fetch specific artifact',
            'GET /healthz': 'Health check',
        },
        'docs': '/docs',
    }


@app.get('/healthz')
def healthz():
    """Liveness/readiness check. Verifies brain snapshots load."""
    try:
        sys.path.insert(0, str(THIS_DIR.parent / 'auditor-ruleset-export'))
        from ranker import BrainIndex
        brain = BrainIndex.from_export_dir(
            str(THIS_DIR.parent / 'auditor-ruleset-export')
        )
        stats = brain.stats()
        api_key_set = bool(os.getenv('ANTHROPIC_API_KEY'))
        return {
            'status': 'ok',
            'brain_loaded': True,
            'brain_stats': stats,
            'anthropic_key_set': api_key_set,
            'output_dir': str(OUTPUT_DIR),
        }
    except Exception as e:
        return JSONResponse(
            status_code=503,
            content={
                'status': 'degraded',
                'error': f'{type(e).__name__}: {e}',
            },
        )


@app.post('/audit', response_model=AuditResponse)
async def submit_audit(req: AuditRequest, background_tasks: BackgroundTasks):
    """Submit a URL for audit. Returns audit_id immediately; audit runs async.

    Poll GET /audit/{id} for status. Typical completion: 60-120 seconds.
    """
    audit_id = str(uuid.uuid4())
    url_str = str(req.url)

    with JOBS_LOCK:
        JOBS[audit_id] = {
            'audit_id': audit_id,
            'status': 'queued',
            'url': url_str,
            'started_at': None,
            'completed_at': None,
            'result': None,
            'error': None,
        }

    background_tasks.add_task(_run_audit_background, audit_id, url_str)

    return AuditResponse(
        audit_id=audit_id,
        status='queued',
        message='Audit queued. Poll the audit endpoint for status.',
        poll_url=f'/audit/{audit_id}',
    )


def _run_audit_background(audit_id: str, url: str):
    """Background runner — invoked via FastAPI background_tasks."""
    with JOBS_LOCK:
        JOBS[audit_id]['status'] = 'running'
        JOBS[audit_id]['started_at'] = datetime.now(timezone.utc).isoformat()

    try:
        result = run_audit(url, output_dir=str(OUTPUT_DIR))
        with JOBS_LOCK:
            JOBS[audit_id]['status'] = 'completed'
            JOBS[audit_id]['completed_at'] = datetime.now(timezone.utc).isoformat()
            JOBS[audit_id]['result'] = result
    except Exception as e:
        with JOBS_LOCK:
            JOBS[audit_id]['status'] = 'error'
            JOBS[audit_id]['error'] = f'{type(e).__name__}: {e}'
            JOBS[audit_id]['completed_at'] = datetime.now(timezone.utc).isoformat()


@app.get('/audit/{audit_id}', response_model=AuditStatusResponse)
def get_audit(audit_id: str):
    """Fetch audit status + summary. Poll until status == 'completed'."""
    with JOBS_LOCK:
        job = JOBS.get(audit_id)
    if not job:
        raise HTTPException(status_code=404, detail='audit not found')

    response = {
        'audit_id': audit_id,
        'status': job['status'],
        'started_at': job.get('started_at'),
        'completed_at': job.get('completed_at'),
    }

    if job['status'] == 'error':
        response['error'] = job.get('error')
        return response

    if job['status'] == 'completed' and job.get('result'):
        result = job['result']
        response['duration_seconds'] = result.get('duration_seconds')

        # Compact summary — full data via .json artifact
        response['result_summary'] = {
            'url': result.get('url'),
            'domain': result.get('domain'),
            'page_type': result.get('classification', {}).get('page_type'),
            'industry': result.get('classification', {}).get('industry'),
            'overall_score': result.get('scoring', {}).get('overall_score'),
            'overall_grade': result.get('scoring', {}).get('overall_grade'),
            'section_scores': result.get('scoring', {}).get('section_scores'),
            'findings_count': len(result.get('findings', [])),
            'executive_diagnosis': result.get('narrative', {}).get('executive_diagnosis'),
        }

        response['artifacts'] = {
            'json': f'/audit/{audit_id}.json',
            'markdown': f'/audit/{audit_id}.md',
            'pdf': f'/audit/{audit_id}.pdf',
        }

    return response


@app.get('/audit/{audit_id}.json')
def get_audit_json(audit_id: str):
    """Full audit JSON."""
    with JOBS_LOCK:
        job = JOBS.get(audit_id)
    if not job or job['status'] != 'completed':
        raise HTTPException(status_code=404, detail='audit not ready or not found')
    json_path = job['result'].get('json_path')
    if not json_path or not Path(json_path).exists():
        raise HTTPException(status_code=404, detail='json artifact not found')
    return FileResponse(json_path, media_type='application/json',
                         filename=f'{audit_id}.json')


@app.get('/audit/{audit_id}.md')
def get_audit_markdown(audit_id: str):
    """Markdown audit report."""
    with JOBS_LOCK:
        job = JOBS.get(audit_id)
    if not job or job['status'] != 'completed':
        raise HTTPException(status_code=404, detail='audit not ready')
    md_path = job['result'].get('md_path')
    if not md_path or not Path(md_path).exists():
        raise HTTPException(status_code=404, detail='markdown artifact not found')
    return FileResponse(md_path, media_type='text/markdown',
                         filename=f'{audit_id}.md')


@app.get('/audit/{audit_id}.pdf')
def get_audit_pdf(audit_id: str):
    """1-page PDF summary."""
    with JOBS_LOCK:
        job = JOBS.get(audit_id)
    if not job or job['status'] != 'completed':
        raise HTTPException(status_code=404, detail='audit not ready')
    pdf_path = job['result'].get('pdf_path')
    if not pdf_path or not Path(pdf_path).exists():
        raise HTTPException(
            status_code=404,
            detail='PDF not available (Chrome may not be installed on this host)'
        )
    return FileResponse(pdf_path, media_type='application/pdf',
                         filename=f'{audit_id}.pdf')


@app.get('/audits')
def list_audits():
    """List all audits in this service instance (in-memory only, lost on restart)."""
    with JOBS_LOCK:
        return {
            'count': len(JOBS),
            'audits': [
                {
                    'audit_id': a['audit_id'],
                    'url': a['url'],
                    'status': a['status'],
                    'started_at': a.get('started_at'),
                    'completed_at': a.get('completed_at'),
                }
                for a in JOBS.values()
            ],
        }


if __name__ == '__main__':
    import uvicorn
    port = int(os.getenv('PORT', 8000))
    uvicorn.run(app, host='0.0.0.0', port=port)
