"use client";

import { SIGNS, BODIES, ELEMENT_COLOR } from "@/lib/astro/zodiac";
import { polar, wedge, declump } from "@/lib/astro/wheel";
import type { ChartFacts } from "@/lib/astro/types";
import type { SynastryResult } from "@/lib/astro/synastry";

const SIZE = 600;
const C = SIZE / 2;
const R = {
  signOuter: 288,
  signInner: 250,
  signGlyph: 269,
  bGlyph: 224,
  bDot: 248,
  aGlyph: 176,
  aDot: 152,
  aspect: 150,
};
const GLYPH_FONT =
  '"Noto Sans Symbols2","Segoe UI Symbol","Apple Symbols","DejaVu Sans",serif';
const A_COLOR = "#f4e0b0"; // gold
const B_COLOR = "#c9b6f2"; // lilac
const ASPECT_COLOR: Record<string, string> = {
  harmonious: "#74b2c4",
  tension: "#dd8fa6",
  blending: "#e8c887",
};

export default function SynastryWheel({
  chartA,
  chartB,
  syn,
}: {
  chartA: ChartFacts;
  chartB: ChartFacts;
  syn: SynastryResult;
}) {
  const orient = chartA.asc?.lon ?? 0;

  const aPlaced = declump(chartA.planets.map((p) => ({ item: p, lon: p.lon })), orient, 11);
  const bPlaced = declump(chartB.planets.map((p) => ({ item: p, lon: p.lon })), orient, 11);
  const topAspects = syn.aspects.slice(0, 20);
  const maxPts = topAspects[0]?.points ?? 1;

  return (
    <svg viewBox={`0 0 ${SIZE} ${SIZE}`} className="wheel-rise w-full h-full" role="img" aria-label="Synastry bi-wheel">
      <defs>
        <radialGradient id="syndisc" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="#1a1538" />
          <stop offset="60%" stopColor="#100d28" />
          <stop offset="100%" stopColor="#0a0820" />
        </radialGradient>
        <radialGradient id="syncore" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="rgba(232,200,135,0.28)" />
          <stop offset="100%" stopColor="rgba(232,200,135,0)" />
        </radialGradient>
        <filter id="synglow" x="-50%" y="-50%" width="200%" height="200%">
          <feGaussianBlur stdDeviation="2.2" result="b" />
          <feMerge>
            <feMergeNode in="b" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>

      <circle cx={C} cy={C} r={R.signOuter} fill="url(#syndisc)" />
      <circle cx={C} cy={C} r={R.signOuter} fill="none" stroke="rgba(232,200,135,0.45)" strokeWidth={1.5} />
      <circle cx={C} cy={C} r={R.signInner} fill="none" stroke="rgba(232,200,135,0.25)" strokeWidth={1} />
      <circle cx={C} cy={C} r={R.bGlyph - 24} fill="none" stroke="rgba(201,182,242,0.16)" strokeWidth={1} />
      <circle cx={C} cy={C} r={R.aspect} fill="none" stroke="rgba(244,224,176,0.14)" strokeWidth={1} />

      {/* sign band */}
      {SIGNS.map((s, i) => {
        const start = i * 30;
        const g = polar(C, C, R.signGlyph, start + 15, orient);
        const divIn = polar(C, C, R.signInner, start, orient);
        const div = polar(C, C, R.signOuter, start, orient);
        return (
          <g key={s.key}>
            <path d={wedge(C, C, R.signInner, R.signOuter, start, start + 30, orient)} fill={i % 2 === 0 ? "rgba(232,200,135,0.05)" : "rgba(120,86,200,0.06)"} />
            <line x1={divIn.x} y1={divIn.y} x2={div.x} y2={div.y} stroke="rgba(232,200,135,0.22)" strokeWidth={1} />
            <text x={g.x} y={g.y} fontSize={22} fill={ELEMENT_COLOR[s.element]} fontFamily={GLYPH_FONT} textAnchor="middle" dominantBaseline="central" opacity={0.95}>
              {s.glyph}
            </text>
          </g>
        );
      })}

      {/* inter-chart aspect web (top contacts) */}
      {topAspects.map((a, idx) => {
        const A = polar(C, C, R.aspect, a.aLon, orient);
        const B = polar(C, C, R.aspect, a.bLon, orient);
        const strength = 0.25 + 0.55 * (a.points / maxPts);
        return (
          <line
            key={idx}
            className="aspect-line"
            x1={A.x}
            y1={A.y}
            x2={B.x}
            y2={B.y}
            stroke={ASPECT_COLOR[a.valence]}
            strokeWidth={a.points > maxPts * 0.5 ? 1.6 : 1}
            opacity={strength}
            style={{ animationDelay: `${0.5 + idx * 0.05}s` }}
          />
        );
      })}

      {/* Person B (outer ring) */}
      {renderPlanets(bPlaced, orient, R.bGlyph, R.bDot, B_COLOR, "b")}
      {/* Person A (inner ring) */}
      {renderPlanets(aPlaced, orient, R.aGlyph, R.aDot, A_COLOR, "a")}

      {/* core */}
      <circle cx={C} cy={C} r={58} fill="url(#syncore)" />
      <text x={C} y={C - 8} fontSize={34} fill="#f4e0b0" textAnchor="middle" dominantBaseline="central" fontFamily='"Cormorant Garamond",Georgia,serif' fontWeight={600}>
        {syn.score}
      </text>
      <text x={C} y={C + 18} fontSize={10} fill="rgba(167,159,196,0.9)" textAnchor="middle" dominantBaseline="central" letterSpacing="0.18em">
        / 100
      </text>
    </svg>
  );
}

function renderPlanets(
  placed: ReturnType<typeof declump>,
  orient: number,
  rGlyph: number,
  rDot: number,
  color: string,
  who: string,
) {
  return placed.map((pg, idx) => {
    const p = pg.item as { body: string; degInSign: number; retrograde: boolean; id: string };
    const meta = BODIES.find((b) => b.key === p.body)!;
    const glyphPt = polar(C, C, rGlyph, pg.plotLon, orient);
    const truePt = polar(C, C, rDot, (pg as { trueLon: number }).trueLon, orient);
    return (
      <g key={`${who}.${p.id}`} className="planet-pop" style={{ animationDelay: `${0.9 + idx * 0.06}s` }}>
        <line x1={truePt.x} y1={truePt.y} x2={glyphPt.x} y2={glyphPt.y} stroke={color} strokeOpacity={0.35} strokeWidth={0.7} />
        <circle cx={truePt.x} cy={truePt.y} r={1.6} fill={color} />
        <text x={glyphPt.x} y={glyphPt.y} fontSize={19} fill={color} fontFamily={GLYPH_FONT} textAnchor="middle" dominantBaseline="central" filter="url(#synglow)">
          {meta.glyph}
        </text>
      </g>
    );
  });
}
