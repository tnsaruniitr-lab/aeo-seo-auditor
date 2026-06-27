import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        ink: "#070612",
        cosmos: "#0c0a1d",
        panel: "#15122b",
        gold: "#e8c887",
        goldbright: "#f4e0b0",
        rose: "#dd8fa6",
        teal: "#74b2c4",
        lilac: "#b9a7e6",
        haze: "#a79fc4",
        cream: "#efe9f6",
      },
      fontFamily: {
        display: ['"Cormorant Garamond"', "Georgia", '"Times New Roman"', "serif"],
        body: ['"Inter"', "system-ui", "-apple-system", "Segoe UI", "Roboto", "sans-serif"],
      },
    },
  },
  plugins: [],
};

export default config;
