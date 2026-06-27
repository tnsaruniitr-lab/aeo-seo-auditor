"use client";

import { SIGNS, BODIES, ELEMENT_COLOR, norm360 } from "@/lib/astro/zodiac";
import { polar, wedge, declump } from "@/lib/astro/wheel";
import type { ChartFacts, PlacedBody } from "@/lib/astro/types";

const SIZE = 600;
const C = SIZE / 2;

const R = {
  signOuter: 288,
  signInner: 246,
  signGlyph: 267,
  houseNum: 224,
  planet: 196,
  leaderDot: 242,
  aspect: 150,
  center: 64,
};

const GLYPH_FONT =
  '"Noto Sans Symbols2","Segoe UI Symbol","Apple Symbols","DejaVu Sans",serif';

const ASPECT_COLOR: Record<string, string> = {
  harmonious: "#74b2c4",
  tension: "#dd8fa6",
  blending: "#e8c887",
};

export default function ChartWheel({ chart }: { chart: ChartFacts }) {
  const orient = chart.asc?.lon ?? 0;
  const hasTime = chart.asc !== null;

  const placed = declump(
    chart.planets.map((p) => ({ item: p, lon: p.lon })),
    orient,
    9,
  );

  return (
    <svg
      viewBox={`0 0 ${SIZE} ${SIZE}`}
      className="wheel-rise w-full h-full"
      role="img"
      aria-label="Natal chart wheel"
    >
      <defs>
        <radialGradient id="disc" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="#1a1538" />
          <stop offset="60%" stopColor="#100d28" />
          <stop offset="100%" stopColor="#0a0820" />
        </radialGradient>
        <radialGradient id="core" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="rgba(232,200,135,0.30)" />
          <stop offset="100%" stopColor="rgba(232,200,135,0)" />
        </radialGradient>
        <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
          <feGaussianBlur stdDeviation="2.4" result="b" />
          <feMerge>
            <feMergeNode in="b" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>

      {/* base discs */}
      <circle cx={C} cy={C} r={R.signOuter} fill="url(#disc)" />
      <circle cx={C} cy={C} r={R.signOuter} fill="none" stroke="rgba(232,200,135,0.45)" strokeWidth={1.5} />
      <circle cx={C} cy={C} r={R.signInner} fill="none" stroke="rgba(232,200,135,0.28)" strokeWidth={1} />
      <circle cx={C} cy={C} r={R.aspect} fill="none" stroke="rgba(232,200,135,0.12)" strokeWidth={1} />

      {/* sign band: 12 wedges, glyphs, dividers */}
      {SIGNS.map((s, i) => {
        const start = i * 30;
        const mid = start + 15;
        const div = polar(C, C, R.signOuter, start, orient);
        const divIn = polar(C, C, R.signInner, start, orient);
        const g = polar(C, C, R.signGlyph, mid, orient);
        return (
          <g key={s.key}>
            <path
              d={wedge(C, C, R.signInner, R.signOuter, start, start + 30, orient)}
              fill={i % 2 === 0 ? "rgba(232,200,135,0.05)" : "rgba(120,86,200,0.06)"}
            />
            <line x1={divIn.x} y1={divIn.y} x2={div.x} y2={div.y} stroke="rgba(232,200,135,0.25)" strokeWidth={1} />
            <text
              x={g.x}
              y={g.y}
              fontSize={24}
              fill={ELEMENT_COLOR[s.element]}
              fontFamily={GLYPH_FONT}
              textAnchor="middle"
              dominantBaseline="central"
              opacity={0.95}
            >
              {s.glyph}
            </text>
          </g>
        );
      })}

      {/* degree ticks */}
      {Array.from({ length: 360 }, (_, deg) => {
        const major = deg % 10 === 0;
        const medium = deg % 5 === 0;
        if (!medium) return null;
        const len = major ? 10 : 5;
        const a = polar(C, C, R.signInner, deg, orient);
        const b = polar(C, C, R.signInner - len, deg, orient);
        return (
          <line
            key={deg}
            x1={a.x}
            y1={a.y}
            x2={b.x}
            y2={b.y}
            stroke="rgba(232,200,135,0.22)"
            strokeWidth={major ? 1 : 0.6}
          />
        );
      })}

      {/* house numbers (whole-sign: one per 30° sign starting at the Asc sign) */}
      {hasTime &&
        chart.houseCusps!.map((cusp, i) => {
          const mid = norm360(cusp + 15);
          const p = polar(C, C, R.houseNum, mid, orient);
          const angular = i === 0 || i === 3 || i === 6 || i === 9;
          return (
            <text
              key={i}
              x={p.x}
              y={p.y}
              fontSize={11}
              fill={angular ? "rgba(244,224,176,0.8)" : "rgba(167,159,196,0.55)"}
              textAnchor="middle"
              dominantBaseline="central"
              fontFamily='"Inter",sans-serif'
            >
              {i + 1}
            </text>
          );
        })}

      {/* aspect lines */}
      {chart.aspects.map((asp, idx) => {
        const pa = chart.planets.find((p) => p.id === asp.a)!;
        const pb = chart.planets.find((p) => p.id === asp.b)!;
        const A = polar(C, C, R.aspect, pa.lon, orient);
        const B = polar(C, C, R.aspect, pb.lon, orient);
        return (
          <line
            key={idx}
            className="aspect-line"
            x1={A.x}
            y1={A.y}
            x2={B.x}
            y2={B.y}
            stroke={ASPECT_COLOR[asp.valence]}
            strokeWidth={asp.aspect === "conjunction" ? 1.4 : 1}
            opacity={0.5}
            style={{ animationDelay: `${0.5 + idx * 0.04}s` }}
          />
        );
      })}

      {/* axes: Ascendant–Descendant & MC–IC */}
      {hasTime && <Axes chart={chart} orient={orient} />}

      {/* center core */}
      <circle cx={C} cy={C} r={R.center} fill="url(#core)" />
      <circle cx={C} cy={C} r={6} fill="#f4e0b0" filter="url(#glow)" />
      <FourStar cx={C} cy={C} r={16} />

      {/* planets */}
      {placed.map((pg, idx) => {
        const p = pg.item as PlacedBody;
        const meta = BODIES.find((b) => b.key === p.body)!;
        const glyphPt = polar(C, C, R.planet, pg.plotLon, orient);
        const truePt = polar(C, C, R.leaderDot, p.lon, orient);
        const labelPt = polar(C, C, R.planet - 24, pg.plotLon, orient);
        return (
          <g key={p.id} className="planet-pop" style={{ animationDelay: `${0.9 + idx * 0.07}s` }}>
            {/* leader from true degree to glyph */}
            <line x1={truePt.x} y1={truePt.y} x2={glyphPt.x} y2={glyphPt.y} stroke="rgba(232,200,135,0.3)" strokeWidth={0.7} />
            <circle cx={truePt.x} cy={truePt.y} r={1.7} fill="#e8c887" />
            <text
              x={glyphPt.x}
              y={glyphPt.y}
              fontSize={22}
              fill="#f4e0b0"
              fontFamily={GLYPH_FONT}
              textAnchor="middle"
              dominantBaseline="central"
              filter="url(#glow)"
            >
              {meta.glyph}
            </text>
            <text
              x={labelPt.x}
              y={labelPt.y}
              fontSize={9.5}
              fill="rgba(239,233,246,0.75)"
              textAnchor="middle"
              dominantBaseline="central"
              fontFamily='"Inter",sans-serif'
            >
              {Math.floor(p.degInSign)}°{p.retrograde ? " ℞" : ""}
            </text>
          </g>
        );
      })}
    </svg>
  );
}

function Axes({ chart, orient }: { chart: ChartFacts; orient: number }) {
  const asc = chart.asc!.lon;
  const mc = chart.mc!.lon;
  const ascP = polar(C, C, R.signInner, asc, orient);
  const descP = polar(C, C, R.signInner, asc + 180, orient);
  const mcP = polar(C, C, R.signInner, mc, orient);
  const icP = polar(C, C, R.signInner, mc + 180, orient);
  const lblAC = polar(C, C, R.signOuter + 14, asc, orient);
  const lblDC = polar(C, C, R.signOuter + 14, asc + 180, orient);
  const lblMC = polar(C, C, R.signOuter + 14, mc, orient);
  const lblIC = polar(C, C, R.signOuter + 14, mc + 180, orient);
  const label = (p: { x: number; y: number }, t: string) => (
    <text x={p.x} y={p.y} fontSize={12} fill="#f4e0b0" textAnchor="middle" dominantBaseline="central" fontFamily='"Inter",sans-serif' fontWeight={600} letterSpacing="0.05em">
      {t}
    </text>
  );
  return (
    <g>
      <line x1={ascP.x} y1={ascP.y} x2={descP.x} y2={descP.y} stroke="rgba(232,200,135,0.6)" strokeWidth={1.4} />
      <line x1={mcP.x} y1={mcP.y} x2={icP.x} y2={icP.y} stroke="rgba(232,200,135,0.45)" strokeWidth={1.1} strokeDasharray="4 4" />
      {label(lblAC, "AC")}
      {label(lblDC, "DC")}
      {label(lblMC, "MC")}
      {label(lblIC, "IC")}
    </g>
  );
}

function FourStar({ cx, cy, r }: { cx: number; cy: number; r: number }) {
  const pts = [
    `${cx},${cy - r}`,
    `${cx + r * 0.18},${cy - r * 0.18}`,
    `${cx + r},${cy}`,
    `${cx + r * 0.18},${cy + r * 0.18}`,
    `${cx},${cy + r}`,
    `${cx - r * 0.18},${cy + r * 0.18}`,
    `${cx - r},${cy}`,
    `${cx - r * 0.18},${cy - r * 0.18}`,
  ].join(" ");
  return <polygon points={pts} fill="rgba(232,200,135,0.35)" />;
}
