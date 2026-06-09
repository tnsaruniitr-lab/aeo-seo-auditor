#!/usr/bin/env bash
# capture_all_for_paste.sh — Capture the audit bundle for the full batch (or a
# custom list) into per-domain files AND a combined blob. Run on a networked
# machine, then paste bundles back to Claude in small waves (2-3 at a time).
#
#   bash scripts-v2/capture_all_for_paste.sh            # built-in 10
#   bash scripts-v2/capture_all_for_paste.sh a.com b.com
#
# Writes: ./captures/<slug>.bundle.txt  (paste these), one per domain.
set -uo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT="./captures"; mkdir -p "$OUT"
DEFAULT=(mmedien.net medical-marketing.berlin prodoc.design klinika.de seosupport.de \
         onehundred.digital missionviral.de excognito.de wir-branden.de onlinemarketingagenturde.de)
if [ "$#" -gt 0 ]; then DOMAINS=("$@"); else DOMAINS=("${DEFAULT[@]}"); fi
for d in "${DOMAINS[@]}"; do
  s="$(echo "$d" | sed -E 's#^https?://##; s#/.*$##; s#\.#-#g')"
  echo "capturing $d -> $OUT/$s.bundle.txt"
  bash "$DIR/capture_for_paste.sh" "https://$d/" > "$OUT/$s.bundle.txt" 2>/dev/null
done
echo "Done. Paste files from $OUT/ in waves of 2-3."
