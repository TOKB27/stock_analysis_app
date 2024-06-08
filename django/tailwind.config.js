/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js",
    "./django/**/*.html", // Djangoテンプレートがある場所を指定
    "./django/**/templates/**/*.html", // 各アプリケーションのテンプレートフォルダを指定
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
