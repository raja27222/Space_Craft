import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/lib/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        luxury: {
          ivory: "#F6F3ED",
          gold: "#C6A46A",
          goldLight: "#DFCA9B",
          goldDark: "#9F7E46",
          charcoal: "#20201E",
          charcoalDark: "#151514",
          charcoalLight: "#2D2D2A",
          beige: "#E8E0D4",
          bronze: "#92744F",
          pureWhite: "#FFFFFF",
        },
      },
      fontFamily: {
        serif: ["var(--font-cormorant)", "Cormorant Garamond", "Playfair Display", "serif"],
        sans: ["var(--font-inter)", "Inter", "Manrope", "sans-serif"],
        arabic: ["var(--font-arabic)", "IBM Plex Sans Arabic", "Cairo", "sans-serif"],
      },
      boxShadow: {
        luxury: "0 10px 30px -10px rgba(198, 164, 106, 0.15)",
        luxuryHover: "0 20px 40px -15px rgba(198, 164, 106, 0.25)",
        deep: "0 25px 50px -12px rgba(32, 32, 30, 0.35)",
      },
      animation: {
        'fade-in': 'fadeIn 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards',
        'fade-up': 'fadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards',
        'pulse-subtle': 'pulseSubtle 3s infinite ease-in-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        fadeUp: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        pulseSubtle: {
          '0%, 100%': { transform: 'scale(1)', opacity: '1' },
          '50%': { transform: 'scale(1.03)', opacity: '0.9' },
        },
      },
    },
  },
  plugins: [],
};
export default config;
