/** @type {import('next').NextConfig} */

// Static export so the app can be hosted on GitHub Pages (no server needed —
// the astrology engine runs in the browser). basePath is set for project
// Pages (https://<user>.github.io/<repo>/) via NEXT_PUBLIC_BASE_PATH.
const basePath = process.env.NEXT_PUBLIC_BASE_PATH || "";

const nextConfig = {
  reactStrictMode: true,
  output: "export",
  trailingSlash: true,
  basePath,
  assetPrefix: basePath || undefined,
  images: { unoptimized: true },
};

export default nextConfig;
