import { NextResponse } from "next/server";
import { computeChart } from "@/lib/astro/chart";
import { computeSynastry } from "@/lib/astro/synastry";
import { findCity } from "@/lib/geo/cities";
import type { ChartInput } from "@/lib/astro/types";

export const runtime = "nodejs";

function toInput(raw: unknown): ChartInput | null {
  const b = raw as Record<string, unknown>;
  const city = findCity(String(b?.cityId));
  if (!city) return null;
  const year = Number(b.year);
  const month = Number(b.month);
  const day = Number(b.day);
  if (!Number.isFinite(year) || year < 1900 || year > 2100 || month < 1 || month > 12 || day < 1 || day > 31) return null;
  return {
    name: typeof b.name === "string" && b.name.trim() ? b.name.slice(0, 40) : undefined,
    place: city.name,
    year, month, day,
    hour: Number(b.hour) || 0,
    minute: Number(b.minute) || 0,
    timeKnown: Boolean(b.timeKnown),
    lat: city.lat,
    lon: city.lon,
    tz: city.tz,
  };
}

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const inA = toInput(body?.a);
    const inB = toInput(body?.b);
    if (!inA || !inB) return NextResponse.json({ error: "Invalid birth data" }, { status: 400 });

    const chartA = computeChart(inA);
    const chartB = computeChart(inB);
    const syn = computeSynastry(chartA, chartB, inA.name ?? "Person A", inB.name ?? "Person B");
    return NextResponse.json({ a: chartA, b: chartB, syn });
  } catch {
    return NextResponse.json({ error: "Bad request" }, { status: 400 });
  }
}
