#!/usr/bin/env bash
# bots_eye_view.sh — Deterministic bot visibility check
#
# Usage: bash bots_eye_view.sh <URL>
# Output: JSON to stdout with everything AI crawlers see about the page.
#
# This is the single most important crawlability diagnostic. It answers:
#   1. What do GPTBot / PerplexityBot / ClaudeBot / Googlebot actually receive?
#   2. Does the server serve the same empty shell for every URL? (SPA-no-SSR detector)
#   3. Is the site cloaking (different content per user-agent)?
#   4. Is the content JS-rendered or actually in the raw HTML?
#
# Designed to produce identical output across runs when the underlying page is unchanged.

set -euo pipefail

if [ "${1:-}" = "" ]; then
  echo '{"error":"missing URL argument","usage":"bash bots_eye_view.sh https://example.com/path"}'
  exit 1
fi

URL="$1"
TMPDIR="${TMPDIR:-/tmp}"
RUNID="$(date +%s)_$$"
PREFIX="${TMPDIR}/bev_${RUNID}"

# Parse URL for origin + a guaranteed-404 path on the same origin
ORIGIN=$(printf '%s' "$URL" | sed -E 's|(https?://[^/]+).*|\1|')
NONEXISTENT_PATH="/nonexistent-probe-$(date +%s)-$$"
NONEXISTENT_URL="${ORIGIN}${NONEXISTENT_PATH}"

# Four UA probes + one 404 probe
# UAs cover: default, Googlebot, GPTBot, PerplexityBot, ClaudeBot
fetch() {
  local ua="$1"; local out="$2"; local url="$3"
  curl -sS --max-time 20 \
    -o "$out" \
    -w "%{http_code} %{size_download} %{time_starttransfer}\n" \
    -H "User-Agent: $ua" \
    -H "Cache-Control: no-cache" \
    "$url" 2>/dev/null || echo "0 0 0"
}

# Run all probes
DEFAULT_UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
GBOT_UA="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
GPT_UA="Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.0; +https://openai.com/gptbot)"
PERP_UA="Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)"
CLAUDE_UA="Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; ClaudeBot/1.0; +claudebot@anthropic.com)"

DEFAULT_RESULT=$(fetch "$DEFAULT_UA" "${PREFIX}_default.html" "$URL")
GBOT_RESULT=$(fetch "$GBOT_UA" "${PREFIX}_gbot.html" "$URL")
GPT_RESULT=$(fetch "$GPT_UA" "${PREFIX}_gpt.html" "$URL")
PERP_RESULT=$(fetch "$PERP_UA" "${PREFIX}_perp.html" "$URL")
CLAUDE_RESULT=$(fetch "$CLAUDE_UA" "${PREFIX}_claude.html" "$URL")
NE_RESULT=$(fetch "$DEFAULT_UA" "${PREFIX}_404.html" "$NONEXISTENT_URL")

# Delegate all parsing + classification to Python for consistency
python3 "$(dirname "$0")/_bev_analyze.py" \
  "$URL" "$NONEXISTENT_URL" \
  "${PREFIX}_default.html" "$DEFAULT_RESULT" \
  "${PREFIX}_gbot.html" "$GBOT_RESULT" \
  "${PREFIX}_gpt.html" "$GPT_RESULT" \
  "${PREFIX}_perp.html" "$PERP_RESULT" \
  "${PREFIX}_claude.html" "$CLAUDE_RESULT" \
  "${PREFIX}_404.html" "$NE_RESULT"

# Clean up temp files
rm -f "${PREFIX}_default.html" "${PREFIX}_gbot.html" "${PREFIX}_gpt.html" \
      "${PREFIX}_perp.html" "${PREFIX}_claude.html" "${PREFIX}_404.html"
