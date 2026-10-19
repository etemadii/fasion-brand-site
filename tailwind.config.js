/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        cream: "#F7F2E9",
        cream2: "#FBF8F2",
        surface: "#FFFDF8",
        ink: "#26221F",
        inkSoft: "#584F47",
        muted: "#8C8177",
        wine: "#6E1D2B",
        wineDeep: "#4E121C",
      },
      fontFamily: {
        vazir: ["Vazirmatn", "Segoe UI", "Tahoma", "sans-serif"],
      },
    },
  },
  plugins: [],
};
