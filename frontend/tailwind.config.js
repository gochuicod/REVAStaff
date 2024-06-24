/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontSize: {
        'dh1': '2.5vw',
        'th1': '4vw',
        'mh1': '8vw',
        'dspan': '0.8vw',
        'tspan': '1.3vw',
        'mspan': '3vw',
      },
    },
  },
  plugins: [],
}