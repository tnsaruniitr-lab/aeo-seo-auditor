#!/usr/bin/env bash
# capture_for_paste.sh — Capture everything the auditor needs for a 100%-legit
# audit, into ONE pasteable text blob. Run this on any machine with normal
# internet (your laptop), then paste the entire output back into the Claude
# session. Claude serves the captured bytes on localhost and runs the real
# deterministic auditor against them — byte-accurate, no API key, no deployed
# service.
#
# USAGE
#   bash scripts-v2/capture_for_paste.sh https://www.mmedien.net/ > mmedien.bundle.txt
#   # then paste the contents of mmedien.bundle.txt back to Claude
#
# Captures: page HTML (default UA), response headers, TTFB/size/redirect timing,
# robots.txt, sitemap.xml, and per-bot-UA byte counts + a 404 probe (for the
# cloaking / SPA-shell checks). Pure curl — no dependencies.

set -uo pipefail
URL="${1:?usage: capture_for_paste.sh <url>}"
case "$URL" in http://*|https://*) ;; *) URL="https://$URL";; esac
ORIGIN="$(echo "$URL" | sed -E 's#(https?://[^/]+).*#\1#')"
UA_BROWSER='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'

emit() { printf '\n===== %s =====\n' "$1"; }

echo "########## AUDIT CAPTURE BUNDLE v1 ##########"
echo "URL: $URL"
echo "ORIGIN: $ORIGIN"
echo "CAPTURED_AT: $(date -u +%Y-%m-%dT%H:%M:%SZ)"

emit "PAGE_HTML (default browser UA)"
curl -sS -A "$UA_BROWSER" -L --max-redirs 5 --max-time 20 "$URL"

emit "RESPONSE_HEADERS"
curl -sS -A "$UA_BROWSER" -D - -o /dev/null -L --max-redirs 5 --max-time 20 "$URL"

emit "TIMING (5 TTFB samples)"
for i in 1 2 3 4 5; do
  curl -sS -A "$UA_BROWSER" -o /dev/null \
    -w "sample$i ttfb=%{time_starttransfer}s total=%{time_total}s code=%{http_code} size=%{size_download} redirects=%{num_redirects}\n" \
    -L --max-redirs 5 --max-time 20 "$URL"
done

emit "ROBOTS_TXT"
curl -sS --max-time 12 "$ORIGIN/robots.txt"

emit "SITEMAP_XML (/sitemap.xml)"
curl -sS --max-time 12 "$ORIGIN/sitemap.xml"

emit "SITEMAP_INDEX (/sitemap_index.xml)"
curl -sS --max-time 12 "$ORIGIN/sitemap_index.xml"

emit "PER_BOT_UA_SIZES (cloaking / SPA-shell signal)"
for ua in \
  "default::$UA_BROWSER" \
  "googlebot::Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" \
  "gptbot::Mozilla/5.0 (compatible; GPTBot/1.0; +https://openai.com/gptbot)" \
  "perplexitybot::Mozilla/5.0 (compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)" \
  "claudebot::Mozilla/5.0 (compatible; ClaudeBot/1.0; +claudebot@anthropic.com)"; do
  name="${ua%%::*}"; agent="${ua#*::}"
  curl -sS -A "$agent" -o /dev/null \
    -w "$name code=%{http_code} size=%{size_download}\n" --max-time 15 "$URL"
done
# 404 probe — same origin, nonexistent path (detects SPA shells)
curl -sS -A "$UA_BROWSER" -o /dev/null \
  -w "probe_404 code=%{http_code} size=%{size_download}\n" --max-time 15 \
  "$ORIGIN/__nonexistent_$(date +%s)__"

echo ""
echo "########## END BUNDLE ##########"
