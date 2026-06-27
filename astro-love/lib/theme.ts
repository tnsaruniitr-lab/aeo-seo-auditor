// Theme system: two aesthetics, switchable at runtime.
//  - "night": Cosmic Night (deep, dark, starlit) — the SaaS-leaning default.
//  - "dawn":  Rose Aurora (soft, warm, ambient, love-suited).
//
// UI surfaces re-theme via CSS variables (see globals.css). The SVG chart
// wheels can't read CSS vars from presentation attributes reliably, so they
// use this resolved palette object instead.

export type ThemeKey = "night" | "dawn";

export const THEMES: { key: ThemeKey; label: string; hint: string }[] = [
  { key: "night", label: "Cosmic Night", hint: "deep & starlit" },
  { key: "dawn", label: "Rose Aurora", hint: "soft & romantic" },
];

export interface WheelPalette {
  discFrom: string;
  discMid: string;
  discTo: string;
  ring: string;
  ringSoft: string;
  ringFaint: string;
  tick: string;
  wedgeA: string;
  wedgeB: string;
  element: { fire: string; earth: string; air: string; water: string };
  planet: string;
  planetLabel: string;
  leader: string;
  leaderDot: string;
  core: string;
  coreStar: string;
  coreDot: string;
  axis: string;
  axisSoft: string;
  aspect: { harmonious: string; tension: string; blending: string };
  houseNum: string;
  houseNumAngular: string;
  personA: string;
  personB: string;
  sub: {
    emotional: string;
    attraction: string;
    affection: string;
    communication: string;
    commitment: string;
  };
  gauge: { from: string; mid: string; to: string };
}

const NIGHT: WheelPalette = {
  discFrom: "#1a1538",
  discMid: "#100d28",
  discTo: "#0a0820",
  ring: "rgba(232,200,135,0.45)",
  ringSoft: "rgba(232,200,135,0.25)",
  ringFaint: "rgba(232,200,135,0.12)",
  tick: "rgba(232,200,135,0.22)",
  wedgeA: "rgba(232,200,135,0.05)",
  wedgeB: "rgba(120,86,200,0.06)",
  element: { fire: "#E0794B", earth: "#9DB07A", air: "#D8C36B", water: "#6FA8C7" },
  planet: "#f4e0b0",
  planetLabel: "rgba(239,233,246,0.75)",
  leader: "rgba(232,200,135,0.30)",
  leaderDot: "#e8c887",
  core: "rgba(232,200,135,0.30)",
  coreStar: "rgba(232,200,135,0.35)",
  coreDot: "#f4e0b0",
  axis: "rgba(232,200,135,0.6)",
  axisSoft: "rgba(232,200,135,0.45)",
  aspect: { harmonious: "#74b2c4", tension: "#dd8fa6", blending: "#e8c887" },
  houseNum: "rgba(167,159,196,0.55)",
  houseNumAngular: "rgba(244,224,176,0.8)",
  personA: "#f4e0b0",
  personB: "#c9b6f2",
  sub: {
    emotional: "#6fa8c7",
    attraction: "#dd8fa6",
    affection: "#e0a96b",
    communication: "#d8c36b",
    commitment: "#9db07a",
  },
  gauge: { from: "#f4e0b0", mid: "#e8c887", to: "#dd8fa6" },
};

const DAWN: WheelPalette = {
  // soft rose-parchment disc that lifts gently off the cream background
  discFrom: "#fdeef0",
  discMid: "#f8e2e6",
  discTo: "#f1d6dd",
  ring: "rgba(150,70,80,0.45)",
  ringSoft: "rgba(150,70,80,0.28)",
  ringFaint: "rgba(150,70,80,0.14)",
  tick: "rgba(150,70,80,0.28)",
  wedgeA: "rgba(189,111,111,0.07)",
  wedgeB: "rgba(154,130,196,0.08)",
  // deepened element hues for legibility on a light disc
  element: { fire: "#c75a3a", earth: "#6f8a4e", air: "#b1923a", water: "#3f7e93" },
  planet: "#7a3b46",
  planetLabel: "rgba(74,46,58,0.72)",
  leader: "rgba(150,70,80,0.4)",
  leaderDot: "#b56b73",
  core: "rgba(207,126,126,0.32)",
  coreStar: "rgba(189,111,111,0.4)",
  coreDot: "#c97e7e",
  axis: "rgba(150,70,80,0.55)",
  axisSoft: "rgba(150,70,80,0.4)",
  aspect: { harmonious: "#4f8693", tension: "#c4546f", blending: "#b97e74" },
  houseNum: "rgba(150,116,130,0.7)",
  houseNumAngular: "rgba(122,59,70,0.85)",
  personA: "#b56b73",
  personB: "#8a70b8",
  sub: {
    emotional: "#4f8693",
    attraction: "#c4546f",
    affection: "#c47e52",
    communication: "#a98a35",
    commitment: "#6f8a4e",
  },
  gauge: { from: "#e8a597", mid: "#cf7e7e", to: "#b56b73" },
};

export const PALETTES: Record<ThemeKey, WheelPalette> = { night: NIGHT, dawn: DAWN };
