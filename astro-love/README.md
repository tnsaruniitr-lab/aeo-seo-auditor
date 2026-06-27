# Astro-Love

A Russian-native, **synastry-first** Web PWA that answers love questions from real astrological **math** (computed planetary positions + a transparent, weighted aspect score) with warm, grounded AI readings in **Russian, Ukrainian, and English**.

The differentiator: not vague sun-signs and not a black-box score — every compatibility number traces back to named aspects ("Venus trine Mars, +6.8 pts"), and the AI layer interprets *only* the pre-computed chart facts (it writes the words, never the numbers).

## What's here

- **[`SPEC.md`](./SPEC.md)** — the full technical + product specification for v1 (MVP):
  - the deterministic astrology engine (ephemeris via the MIT-licensed `astronomy-engine`, Ascendant/MC/house formulas, the synastry scoring rubric, composite/Davison math, the `chart-facts` JSON contract);
  - the Claude AI interpretation layer (grounding contract, structured output, snippet library, cost control);
  - localization (ru/uk/en, glossary, cultural notes);
  - data model, GDPR/privacy, Russia 242-FZ, payments, monetization;
  - roadmap and the open decisions that need product input (§13).

## Status

Spec draft for review — no application code yet. Build milestones are in `SPEC.md` §12.

Points tagged **⚠️ VERIFY** in the spec are known accuracy traps to confirm during implementation (e.g. `astronomy-engine`'s of-date vs J2000 longitudes, east-positive observer longitude, the 0/360 midpoint wraparound, and historical-DST timezone resolution).
