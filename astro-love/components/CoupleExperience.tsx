"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import BirthFields, { type BirthFormValues } from "./BirthFields";
import SynastryWheel from "./SynastryWheel";
import { BODIES } from "@/lib/astro/zodiac";
import type { ChartFacts } from "@/lib/astro/types";
import type { SynastryResult, SynAspect } from "@/lib/astro/synastry";

const GLYPH_FONT =
  '"Noto Sans Symbols2","Segoe UI Symbol","Apple Symbols","DejaVu Sans",serif';

export interface CoupleResult {
  a: ChartFacts;
  b: ChartFacts;
  syn: SynastryResult;
}

const ASPECT_GLYPH: Record<string, string> = {
  conjunction: "☌", sextile: "⚹", square: "□", trine: "△", quincunx: "⚻", opposition: "☍",
};
const VALENCE_COLOR: Record<string, string> = {
  harmonious: "#74b2c4", tension: "#dd8fa6", blending: "#e8c887",
};

export default function CoupleExperience({
  initialA,
  initialB,
  initialResult,
}: {
  initialA: BirthFormValues;
  initialB: BirthFormValues;
  initialResult: CoupleResult;
}) {
  const [a, setA] = useState(initialA);
  const [b, setB] = useState(initialB);
  const [result, setResult] = useState<CoupleResult>(initialResult);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function calculate() {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch("/api/synastry", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ a, b }),
      });
      if (!res.ok) throw new Error((await res.json()).error ?? "Failed");
      setResult(await res.json());
    } catch (e) {
      setError(e instanceof Error ? e.message : "Something went wrong");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="relative mx-auto max-w-6xl px-4 sm:px-6 py-10 sm:py-14">
      <nav className="flex justify-center mb-8">
        <Link href="/" className="text-xs uppercase tracking-[0.2em] text-haze hover:text-gold transition-colors">
          ← Single natal chart
        </Link>
      </nav>

      <header className="text-center">
        <div className="inline-flex items-center gap-2 text-[11px] uppercase tracking-[0.32em] text-gold/80">
          <span>✦</span> Astro-Love · Compatibility <span>✦</span>
        </div>
        <h1 className="font-display text-4xl sm:text-6xl leading-tight mt-3">
          <span className="gold-text">Two charts,</span>{" "}
          <span className="text-cream italic">one connection.</span>
        </h1>
        <p className="text-haze mt-4 max-w-xl mx-auto">
          Real synastry: we measure the angles between your planets and theirs, and
          score them by what actually drives love. Every point is explained below —{" "}
          <span className="text-cream/80">прозрачная математика.</span>
        </p>
      </header>

      {/* Two birth panels */}
      <div className="grid md:grid-cols-2 gap-5 mt-10">
        <Panel label="Person A" accent="#f4e0b0">
          <BirthFields value={a} onChange={setA} namePlaceholder="e.g. Anna" />
        </Panel>
        <Panel label="Person B" accent="#c9b6f2">
          <BirthFields value={b} onChange={setB} namePlaceholder="e.g. Dmitri" />
        </Panel>
      </div>
      <div className="flex flex-col items-center mt-5">
        <button onClick={calculate} disabled={loading} className="btn-gold px-10 py-3">
          {loading ? "Reading the stars…" : "Calculate compatibility"}
        </button>
        {error && <p className="mt-3 text-sm text-rose/90">{error}</p>}
      </div>

      <Result result={result} />

      <footer className="mt-14 text-center text-xs text-haze/60 space-y-1">
        <p>For entertainment &amp; self-reflection. Not a substitute for professional advice.</p>
        <p className="text-haze/40">Astro-Love · Milestone 2 — synastry scoring · tropical zodiac, whole-sign houses</p>
      </footer>
    </main>
  );
}

function Panel({ label, accent, children }: { label: string; accent: string; children: React.ReactNode }) {
  return (
    <div className="glass p-6">
      <div className="flex items-center gap-2 mb-4">
        <span className="inline-block w-2.5 h-2.5 rounded-full" style={{ background: accent }} />
        <h2 className="font-display text-xl text-cream">{label}</h2>
      </div>
      {children}
    </div>
  );
}

function Result({ result }: { result: CoupleResult }) {
  const { a, b, syn } = result;
  return (
    <section className="mt-10 space-y-6">
      {/* Score hero */}
      <div className="glass p-6 sm:p-8 text-center fade-up">
        <div className="text-sm text-haze tracking-wide">
          <span style={{ color: "#f4e0b0" }}>{syn.names.a}</span>
          <span className="mx-2 text-gold">✦</span>
          <span style={{ color: "#c9b6f2" }}>{syn.names.b}</span>
        </div>
        <div className="flex flex-col items-center mt-3">
          <ScoreGauge score={syn.score} />
          <h2 className="font-display text-3xl text-goldbright mt-3">{syn.band.label}</h2>
          <p className="text-haze max-w-md mx-auto mt-2 text-sm leading-relaxed">{syn.band.blurb}</p>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-5 gap-3 mt-7 max-w-3xl mx-auto">
          <SubBar label="Emotional" value={syn.subscores.emotional} color="#6fa8c7" />
          <SubBar label="Attraction" value={syn.subscores.attraction} color="#dd8fa6" />
          <SubBar label="Affection" value={syn.subscores.affection} color="#e0a96b" />
          <SubBar label="Communication" value={syn.subscores.communication} color="#d8c36b" />
          <SubBar label="Commitment" value={syn.subscores.commitment} color="#9db07a" />
        </div>
      </div>

      <div className="grid lg:grid-cols-5 gap-6">
        {/* Bi-wheel */}
        <div className="lg:col-span-3 glass p-5 sm:p-6 fade-up">
          <div className="aspect-square max-w-[560px] mx-auto">
            <SynastryWheel chartA={a} chartB={b} syn={syn} />
          </div>
          <div className="flex flex-wrap items-center justify-center gap-x-5 gap-y-1.5 mt-3 text-[11px] text-haze">
            <Legend c="#f4e0b0" t={`${syn.names.a} (inner)`} dot />
            <Legend c="#c9b6f2" t={`${syn.names.b} (outer)`} dot />
            <Legend c="#74b2c4" t="harmonious" />
            <Legend c="#dd8fa6" t="challenging" />
            <Legend c="#e8c887" t="conjunction" />
          </div>
        </div>

        {/* Why this score */}
        <div className="lg:col-span-2 glass p-5 sm:p-6 fade-up">
          <h3 className="font-display text-xl text-cream">Why this score</h3>
          <p className="text-xs text-haze mt-1 mb-4">
            The {syn.aspects.length} contacts below add up to the result — strongest first.
          </p>
          <ul className="space-y-2.5 max-h-[460px] overflow-y-auto pr-1">
            {syn.aspects.slice(0, 14).map((asp, i) => (
              <AspectRow key={i} asp={asp} />
            ))}
          </ul>

          {syn.overlays.length > 0 && (
            <div className="mt-5">
              <h4 className="text-xs uppercase tracking-[0.16em] text-haze/80 mb-2">House overlays</h4>
              <ul className="space-y-1.5 text-sm text-cream/85">
                {syn.overlays.slice(0, 5).map((o, i) => (
                  <li key={i} className="flex gap-2">
                    <span className="text-gold">+{o.bonus}</span>
                    <span>{o.sentence}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </div>

      {syn.warnings.length > 0 && (
        <div className="text-xs text-gold/75 bg-gold/5 border border-gold/15 rounded-xl px-4 py-3">
          {syn.warnings.map((w, i) => (
            <p key={i}>✦ {w}</p>
          ))}
        </div>
      )}
    </section>
  );
}

function AspectRow({ asp }: { asp: SynAspect }) {
  const aMeta = BODIES.find((x) => x.key === asp.aBody);
  const bMeta = BODIES.find((x) => x.key === asp.bBody);
  return (
    <li className="flex items-start gap-3 rounded-xl bg-white/[0.02] border border-white/5 px-3 py-2.5">
      <span className="mt-0.5 inline-flex items-center gap-1 shrink-0" style={{ fontFamily: GLYPH_FONT }}>
        <span style={{ color: "#f4e0b0" }}>{aMeta?.glyph ?? "↑"}</span>
        <span style={{ color: VALENCE_COLOR[asp.valence], fontSize: "0.85em" }}>{ASPECT_GLYPH[asp.aspect]}</span>
        <span style={{ color: "#c9b6f2" }}>{bMeta?.glyph ?? "↑"}</span>
      </span>
      <span className="text-[13px] text-cream/85 leading-snug flex-1">{asp.sentence}</span>
      <span className="text-xs tabular-nums shrink-0" style={{ color: VALENCE_COLOR[asp.valence] }}>+{asp.points.toFixed(1)}</span>
    </li>
  );
}

function SubBar({ label, value, color }: { label: string; value: number; color: string }) {
  const [w, setW] = useState(0);
  useEffect(() => {
    const t = setTimeout(() => setW(value), 200);
    return () => clearTimeout(t);
  }, [value]);
  return (
    <div className="text-left">
      <div className="flex justify-between items-baseline mb-1">
        <span className="text-[10px] uppercase tracking-wider text-haze/80">{label}</span>
        <span className="text-sm tabular-nums" style={{ color }}>{value}</span>
      </div>
      <div className="h-1.5 rounded-full bg-white/10 overflow-hidden">
        <div className="h-full rounded-full transition-[width] duration-1000 ease-out" style={{ width: `${w}%`, background: color }} />
      </div>
    </div>
  );
}

function Legend({ c, t, dot }: { c: string; t: string; dot?: boolean }) {
  return (
    <span className="inline-flex items-center gap-1.5">
      <span className={dot ? "inline-block w-2.5 h-2.5 rounded-full" : "inline-block w-4 h-[2px] rounded"} style={{ background: c }} />
      {t}
    </span>
  );
}

function ScoreGauge({ score }: { score: number }) {
  const r = 76;
  const circ = 2 * Math.PI * r;
  const [offset, setOffset] = useState(circ);
  useEffect(() => {
    const t = setTimeout(() => setOffset(circ * (1 - score / 100)), 150);
    return () => clearTimeout(t);
  }, [score, circ]);
  return (
    <div className="relative" style={{ width: 180, height: 180 }}>
      <svg viewBox="0 0 180 180" className="w-full h-full -rotate-90">
        <defs>
          <linearGradient id="gauge" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stopColor="#f4e0b0" />
            <stop offset="55%" stopColor="#e8c887" />
            <stop offset="100%" stopColor="#dd8fa6" />
          </linearGradient>
        </defs>
        <circle cx="90" cy="90" r={r} fill="none" stroke="rgba(255,255,255,0.08)" strokeWidth="10" />
        <circle
          cx="90" cy="90" r={r} fill="none" stroke="url(#gauge)" strokeWidth="10" strokeLinecap="round"
          strokeDasharray={circ} strokeDashoffset={offset}
          style={{ transition: "stroke-dashoffset 1.4s cubic-bezier(0.16,1,0.3,1)" }}
        />
      </svg>
      <div className="absolute inset-0 flex flex-col items-center justify-center">
        <span className="font-display text-5xl text-goldbright leading-none">{score}</span>
        <span className="text-[10px] uppercase tracking-[0.22em] text-haze mt-1">/ 100</span>
      </div>
    </div>
  );
}
