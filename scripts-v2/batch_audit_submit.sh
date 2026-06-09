#!/usr/bin/env bash
# batch_audit_submit.sh — Submit a batch of URLs to the deployed aeo-seo-auditor
# service (audits.growthmonk.ai) and poll each to completion.
#
# WHY THIS EXISTS
#   The deployed service fetches target sites via Anthropic's *server-side* web
#   tools (open internet) — so it can audit any public site, unlike a restricted
#   CI/sandbox whose egress is locked down. Run this from any machine (or the
#   Railway shell) that can reach the service.
#
# USAGE
#   export AUDIT_API_KEY="<the AUDIT_API_KEY you set in Railway>"
#   export BASE_URL="https://audits.growthmonk.ai"      # optional; this is the default
#   bash scripts-v2/batch_audit_submit.sh               # audits the built-in list
#   bash scripts-v2/batch_audit_submit.sh a.com b.com   # or pass your own domains
#
# REQUIREMENTS: curl, python3 (stdlib only). No jq needed.
#
# OUTPUT: per-domain auditId, live status, and the public shareable report URL
#   https://audits.growthmonk.ai/<domain>

set -uo pipefail

BASE_URL="${BASE_URL:-https://audits.growthmonk.ai}"
API_KEY="${AUDIT_API_KEY:-}"
POLL_INTERVAL="${POLL_INTERVAL:-10}"     # seconds between status polls
POLL_TIMEOUT="${POLL_TIMEOUT:-300}"      # max seconds to wait per audit

# Default batch — override by passing domains as args.
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

if [ "$#" -gt 0 ]; then
  DOMAINS=("$@")
else
  DOMAINS=("${DEFAULT_DOMAINS[@]}")
fi

if [ -z "$API_KEY" ]; then
  echo "WARNING: AUDIT_API_KEY is not set. If the service has API_KEY_ENABLED," \
       "requests will be rejected with 401. Export AUDIT_API_KEY first." >&2
fi

auth_header=()
[ -n "$API_KEY" ] && auth_header=(-H "X-API-Key: ${API_KEY}")

# Extract a JSON string field without jq.
json_field() { python3 -c "import sys,json;d=json.load(sys.stdin);print(d.get('$1',''))" 2>/dev/null; }

normalize() { case "$1" in http://*|https://*) echo "$1";; *) echo "https://$1";; esac; }
slug()      { echo "$1" | sed -E 's#^https?://##; s#/.*$##'; }

echo "=========================================================================="
echo " Batch audit → ${BASE_URL}"
echo " ${#DOMAINS[@]} domains | poll every ${POLL_INTERVAL}s | timeout ${POLL_TIMEOUT}s each"
echo "=========================================================================="

declare -A AUDIT_IDS
declare -A FINAL_STATUS

# ---- Phase 1: submit all (idempotent start; fires them server-side) ----
for d in "${DOMAINS[@]}"; do
  url="$(normalize "$d")"
  resp="$(curl -sS -X POST "${BASE_URL}/api/audit/start" \
            "${auth_header[@]}" \
            -H 'Content-Type: application/json' \
            -d "{\"url\":\"${url}\"}" --max-time 30 2>/dev/null)"
  aid="$(echo "$resp" | json_field auditId)"
  reused="$(echo "$resp" | json_field reused)"
  if [ -n "$aid" ]; then
    AUDIT_IDS["$d"]="$aid"
    printf '  submitted  %-30s → %s %s\n' "$d" "$aid" \
      "$([ "$reused" = "True" ] && echo '(reused)')"
  else
    FINAL_STATUS["$d"]="SUBMIT_FAILED: ${resp:0:120}"
    printf '  FAILED     %-30s → %s\n' "$d" "${resp:0:120}"
  fi
done

# ---- Phase 2: poll each to a terminal state ----
echo "--------------------------------------------------------------------------"
echo " Polling for completion…"
for d in "${DOMAINS[@]}"; do
  aid="${AUDIT_IDS[$d]:-}"
  [ -z "$aid" ] && continue
  elapsed=0
  while : ; do
    st="$(curl -sS "${BASE_URL}/api/audit/${aid}/status" "${auth_header[@]}" \
            --max-time 30 2>/dev/null | json_field status)"
    case "$st" in
      complete|completed|done|failed|error)
        FINAL_STATUS["$d"]="$st"; printf '  %-30s %s\n' "$d" "$st"; break;;
      "")
        FINAL_STATUS["$d"]="no_status"; printf '  %-30s no_status\n' "$d"; break;;
    esac
    if [ "$elapsed" -ge "$POLL_TIMEOUT" ]; then
      FINAL_STATUS["$d"]="TIMEOUT (still ${st})"; printf '  %-30s TIMEOUT (%s)\n' "$d" "$st"; break
    fi
    sleep "$POLL_INTERVAL"; elapsed=$((elapsed + POLL_INTERVAL))
  done
done

# ---- Phase 3: report hosted links ----
echo "=========================================================================="
echo " RESULTS"
echo "=========================================================================="
for d in "${DOMAINS[@]}"; do
  s="${FINAL_STATUS[$d]:-unknown}"
  printf '  %-30s %-22s %s/%s\n' "$d" "$s" "$BASE_URL" "$(slug "$d")"
done
echo "--------------------------------------------------------------------------"
echo " Public report pages: ${BASE_URL}/<domain>   (e.g. ${BASE_URL}/$(slug "${DOMAINS[0]}"))"
echo " Full JSON:           ${BASE_URL}/api/by-domain/<domain>"
