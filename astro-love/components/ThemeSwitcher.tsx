"use client";

import { useTheme } from "./ThemeProvider";
import { THEMES, type ThemeKey } from "@/lib/theme";

export default function ThemeSwitcher() {
  const { theme, setTheme } = useTheme();
  return (
    <label className="inline-flex items-center gap-2 text-[11px] uppercase tracking-[0.16em] text-haze">
      <span aria-hidden className="text-gold">{theme === "dawn" ? "☀" : "☾"}</span>
      <span className="sr-only">Theme</span>
      <select
        aria-label="Choose a theme"
        className="field px-3 py-1.5 text-[11px] uppercase tracking-[0.12em] cursor-pointer"
        value={theme}
        onChange={(e) => setTheme(e.target.value as ThemeKey)}
      >
        {THEMES.map((t) => (
          <option key={t.key} value={t.key}>
            {t.label} — {t.hint}
          </option>
        ))}
      </select>
    </label>
  );
}
