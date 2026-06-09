#!/usr/bin/env python3
"""persist_bundle.py — Push Claude-generated audits into Supabase so they show
up at audits.growthmonk.ai/{domain}.

WHY THIS EXISTS
  Claude (in the locked-down web session) produces byte-accurate audits from
  pasted page bytes, but cannot reach Supabase from that session (egress
  blocked). This runner takes the audit JSON Claude writes and persists it via
  the SAME persist_audit() the deployed service uses — so the only credential
  you need is the Supabase service key (NOT the Anthropic API key, NOT the
  deployed audit pipeline).

USAGE (on any machine with internet + the repo)
  export SUPABASE_URL="https://<project>.supabase.co"
  export SUPABASE_SERVICE_KEY="<service_role key>"
  python3 scripts-v2/persist_bundle.py audit-reports/json/*.audit.json

Each input file is one audit_data dict shaped for tools.persist_audit():
  {url, domain, scoring:{overall_score,...}, section_scores, findings:[...], ...}
"""
import os, sys, json, glob, pathlib

# Make standalone/ importable so we reuse the exact production persist logic.
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "standalone"))

try:
    from tools import persist_audit  # noqa: E402
except Exception as e:  # pragma: no cover
    sys.exit(f"could not import persist_audit from standalone/tools.py: {e}")


def main(argv):
    if not argv:
        sys.exit("usage: persist_bundle.py <audit.json> [more.json ...]")
    if not (os.getenv("SUPABASE_URL") and os.getenv("SUPABASE_SERVICE_KEY")):
        sys.exit("set SUPABASE_URL and SUPABASE_SERVICE_KEY first")

    paths = []
    for a in argv:
        paths.extend(sorted(glob.glob(a)) or [a])

    ok = 0
    for p in paths:
        try:
            data = json.load(open(p))
        except Exception as e:
            print(f"  SKIP {p}: bad json ({e})"); continue
        res = persist_audit(data)
        status = "ok" if res.get("supabase_row_id") else "FAILED"
        print(f"  {status:7} {data.get('domain', p)} "
              f"row={res.get('supabase_row_id')} "
              f"findings={res.get('findings_persisted')} "
              f"{res.get('error') or ''}")
        ok += 1 if res.get("supabase_row_id") else 0
    print(f"persisted {ok}/{len(paths)} audits")


if __name__ == "__main__":
    main(sys.argv[1:])
