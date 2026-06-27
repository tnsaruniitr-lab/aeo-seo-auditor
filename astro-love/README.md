# Astro-Love

A Russian-native, **synastry-first** Web PWA that answers love questions from real astrological **math** (computed planetary positions + a transparent, weighted aspect score) with warm, grounded AI readings in **Russian, Ukrainian, and English**.

The differentiator: not vague sun-signs and not a black-box score — every compatibility number traces back to named aspects ("Venus trine Mars, +6.8 pts"), and the AI layer interprets *only* the pre-computed chart facts (it writes the words, never the numbers).

## Status — Milestone 1 built ✅ (natal engine + UX)

A working **Next.js (App Router) PWA** with the deterministic natal-chart engine and a hand-crafted chart UI. You enter birth date / time / place and get a real, validated natal chart: planet positions, Ascendant, Midheaven, whole-sign houses, and an animated SVG chart wheel.

### Run it
```bash
cd astro-love
npm install
npm run validate:engine   # numerically validates the astronomy (closed-form + almanac checks)
npm run dev               # http://localhost:3000
```

### What's implemented
- **Engine (`lib/astro`, `lib/geo`)** — deterministic, reproducible:
  - geocoding via a curated city DB (CIS + world) and **historical-DST-correct** UTC resolution (Luxon + IANA tz);
  - geocentric **ecliptic-of-date** planet longitudes via the MIT `astronomy-engine` (with the heliocentric / J2000-precession traps handled — see `ephemeris.ts`);
  - **Ascendant / Midheaven** spherical-trig formulas and **whole-sign houses**;
  - retrograde detection, natal aspect detection with luminary-adjusted orbs;
  - emits the versioned `chart-facts` JSON (the engine ↔ AI/UI contract from `SPEC.md` §6.7);
  - graceful degradation when birth time is unknown.
- **UX (`app`, `components`)** — a cosmic, gold-on-indigo design: birth-data form, "big three" (Sun / Moon / Rising), a bespoke **SVG natal wheel** (element-colored sign glyphs, planet glyphs + degrees + retrograde, valence-colored aspect lines, AC–DC / MC–IC axes, declumped planets with leader lines), and a planet table. Server-rendered with a sample chart on first load; recomputes via `/api/chart`.
- **Validation (`scripts/validate-engine.ts`)** — closed-form checks (Asc/MC reference values, whole-sign houses, 0/360 wraparound) plus almanac sanity (Sun sign/degree). The reference chart (Moscow, 14 May 1990) reproduces the real 1988–91 Saturn/Uranus/Neptune-in-Capricorn stack and a mid-May-1990 Mercury retrograde — and correctly resolves Moscow to **UTC+4** (summer time then), not today's UTC+3.

### Not yet (next milestones, per `SPEC.md` §12)
M2 synastry scoring · M3 the Claude AI reading layer · M4 i18n (ru/uk/en) · M5 monetization + legal.

## The spec
**[`SPEC.md`](./SPEC.md)** — the full technical + product specification (engine math, synastry rubric, AI grounding, i18n, GDPR/privacy/Russia, monetization, roadmap, open decisions §13). Points tagged **⚠️ VERIFY** are the known accuracy traps; the M1 engine handles the engine-side ones.
