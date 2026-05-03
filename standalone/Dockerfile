# Dockerfile for the standalone audit service.
# Used by Railway, Fly.io, Cloud Run, or any Docker-compatible host.

FROM python:3.11-slim

# System deps:
#   curl + bash for the deterministic audit scripts
#   chromium + fonts-liberation for PDF rendering
#   Playwright system deps (libnss3, libxkbcommon, etc.) for render_page_js
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    bash \
    chromium \
    fonts-liberation \
    libnss3 \
    libnspr4 \
    libxkbcommon0 \
    libdrm2 \
    libgbm1 \
    libasound2 \
    libatspi2.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libpango-1.0-0 \
    libcairo2 \
    libcups2 \
    libxshmfence1 \
    && rm -rf /var/lib/apt/lists/*

# Tell the auditor where Chrome lives (overrides the default macOS path)
ENV CHROME_PATH=/usr/bin/chromium

WORKDIR /app

# Copy requirements first for layer caching
COPY standalone/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Install Playwright Chromium browser (uses the same binary family as system chromium,
# but Playwright manages its own copy for API stability).
RUN python -m playwright install chromium && \
    python -m playwright install-deps chromium 2>/dev/null || true

# Copy the rest of the auditor — everything the scripts and pipeline need
COPY auditor-ruleset-export /app/auditor-ruleset-export
COPY skill-unified /app/skill-unified
COPY standalone /app/standalone

# Make scripts executable
RUN chmod +x /app/skill-unified/scripts/*.sh /app/skill-unified/scripts/*.py 2>/dev/null || true

# Audit output dir (mountable as a volume in production)
RUN mkdir -p /app/audits
ENV AUDIT_OUTPUT_DIR=/app/audits

# Default audit mode: "agent" (full parity) or "deterministic" (legacy fast path)
ENV AUDIT_MODE=agent

# Railway sets PORT automatically; default to 8000 locally
ENV PORT=8000
EXPOSE 8000

WORKDIR /app/standalone

# Run the FastAPI app via uvicorn
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
