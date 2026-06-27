import { NextResponse } from "next/server";
import { computeChart } from "@/lib/astro/chart";
import { findCity } from "@/lib/geo/cities";
import type { ChartInput } from "@/lib/astro/types";

export const runtime = "nodejs";

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const city = findCity(body.cityId);
    if (!city) {
      return NextResponse.json({ error: "Unknown city" }, { status: 400 });
    }
    const input: ChartInput = {
      name: typeof body.name === "string" ? body.name.slice(0, 60) : undefined,
      place: city.name,
      year: Number(body.year),
      month: Number(body.month),
      day: Number(body.day),
      hour: Number(body.hour) || 0,
      minute: Number(body.minute) || 0,
      timeKnown: Boolean(body.timeKnown),
      lat: city.lat,
      lon: city.lon,
      tz: city.tz,
    };

    // Basic validation
    if (
      !Number.isFinite(input.year) || input.year < 1900 || input.year > 2100 ||
      input.month < 1 || input.month > 12 ||
      input.day < 1 || input.day > 31
    ) {
      return NextResponse.json({ error: "Invalid date" }, { status: 400 });
    }

    return NextResponse.json(computeChart(input));
  } catch {
    return NextResponse.json({ error: "Bad request" }, { status: 400 });
  }
}
