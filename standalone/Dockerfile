# Dockerfile for the standalone audit service.
# Used by Railway, Fly.io, Cloud Run, or any Docker-compatible host.

FROM python:3.11-slim

# System deps: curl for the audit scripts, chromium for PDF rendering
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    bash \
    chromium \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# Tell the auditor where Chrome lives (overrides the default macOS path)
ENV CHROME_PATH=/usr/bin/chromium

WORKDIR /app

# Copy requirements first for layer caching
COPY standalone/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the auditor — everything the scripts and pipeline need
COPY auditor-ruleset-export /app/auditor-ruleset-export
COPY skill-unified /app/skill-unified
COPY standalone /app/standalone

# Make scripts executable
RUN chmod +x /app/skill-unified/scripts/*.sh /app/skill-unified/scripts/*.py 2>/dev/null || true

# Audit output dir (mountable as a volume in production)
RUN mkdir -p /app/audits
ENV AUDIT_OUTPUT_DIR=/app/audits

# Railway sets PORT automatically; default to 8000 locally
ENV PORT=8000
EXPOSE 8000

WORKDIR /app/standalone

# Run the FastAPI app via uvicorn
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
