import type { Config } from 'tailwindcss'

export default {
  content: [
    './app/components/**/*.{js,vue,ts}',
    './app/layouts/**/*.vue',
    './app/pages/**/*.vue',
    './app/plugins/**/*.{js,ts}',
    './app/app.vue',
  ],
  theme: {
    extend: {
      colors: {
        // TODO: Add project colors from design spec
        // Example:
        // primary: '#DE0017',
        // secondary: '#333333',
      },
      fontFamily: {
        // TODO: Add project fonts from design spec
        // Example:
        // sans: ['Noto Sans JP', 'sans-serif'],
      },
    },
  },
  plugins: [],
} satisfies Config
