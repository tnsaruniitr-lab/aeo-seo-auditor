#!/usr/bin/env bash
# run_local_batch.sh — Run the deterministic auditor core locally over a batch
# of domains. REQUIRES OPEN NETWORK EGRESS (curl must reach the targets).
#
# This produces the deterministic ground-truth core for each domain
# (Bot's Eye View + 9 checks + robots + sitemap + schema completeness). The
# agent then layers WebSearch company/competitor/GEO context on top and writes
# the full SKILL.md 3-layer report per domain.
#
# USAGE
#   bash scripts-v2/run_local_batch.sh                 # built-in 10-domain list
#   bash scripts-v2/run_local_batch.sh a.com b.com     # custom list
#
# OUTPUT (per domain, under audit-reports/raw/):
#   <slug>.det.json   — combined deterministic JSON (for the agent to quote)
#   <slug>.det.txt    — human-readable summary (for quick eyeballing)
#
# REQUIREMENTS: curl, python3 (3.8+), bash. Open egress to the target hosts.

set -uo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ORCH="${REPO_DIR}/skill/scripts/run_deterministic.sh"
OUT_DIR="${REPO_DIR}/audit-reports/raw"
mkdir -p "$OUT_DIR"

DEFAULT_DOMAINS=(
  mmedien.net
  medical-marketing.berlin
  prodoc.design
  klinika.de
  seosupport.de
  onehundred.digital
  missionviral.de
  excognito.de
  wir-branden.de
  onlinemarketingagenturde.de
)

if [ "$#" -gt 0 ]; then DOMAINS=("$@"); else DOMAINS=("${DEFAULT_DOMAINS[@]}"); fi

slug() { echo "$1" | sed -E 's#^https?://##; s#/.*$##; s#\.#-#g'; }

# Fast preflight: confirm egress is actually open before burning time.
probe="$(curl -sS -o /dev/null -w '%{http_code}' --max-time 8 "https://${DOMAINS[0]}/" 2>/dev/null)"
deny="$(curl -sS -D - -o /dev/null --max-time 8 "https://${DOMAINS[0]}/" 2>/dev/null | grep -i 'x-deny-reason' | tr -d '\r')"
if [ -n "$deny" ]; then
  echo "ABORT: egress appears blocked (${deny}). This needs an open-network environment." >&2
  echo "       Reconfigure the environment's network policy, then re-run." >&2
  exit 2
fi
echo "Egress preflight OK (HTTP $probe from ${DOMAINS[0]}). Running ${#DOMAINS[@]} domains."
echo "=========================================================================="

for d in "${DOMAINS[@]}"; do
  s="$(slug "$d")"
  url="https://${d}/"
  echo "→ ${d}"
  bash "$ORCH" "$url"        > "${OUT_DIR}/${s}.det.json" 2>/dev/null
  bash "$ORCH" "$url" human  > "${OUT_DIR}/${s}.det.txt"  2>/dev/null
  cls="$(python3 -c "import json,sys;print(json.load(open('${OUT_DIR}/${s}.det.json')).get('bots_eye_view',{}).get('classification','?'))" 2>/dev/null || echo '?')"
  echo "   classification=${cls}  → audit-reports/raw/${s}.det.{json,txt}"
done

echo "=========================================================================="
echo "Deterministic cores written to audit-reports/raw/."
echo "Next: the agent reads each .det.json, runs WebSearch context, and writes"
echo "the full SKILL.md report to audit-reports/<slug>-audit-1-<date>.md."
