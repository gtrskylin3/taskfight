/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js,ts,jsx,tsx}",
    "./public/**/*.{html,js,ts,jsx,tsx}",
    "./*.{html,js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        background: '#000000',
        foreground: '#f0f0f0',
        card: '#0a0a0a',
        'card-foreground': '#f0f0f0',
        popover: '#0a0a0a',
        'popover-foreground': '#f0f0f0',
        primary: {
          DEFAULT: '#6366f1',
          foreground: '#ffffff',
        },
        secondary: {
          DEFAULT: '#333333',
          foreground: '#ffffff',
        },
        muted: {
          DEFAULT: '#1a1a1a',
          foreground: '#9ca3af',
        },
        accent: {
          DEFAULT: '#6366f1',
          foreground: '#ffffff',
        },
        destructive: {
          DEFAULT: '#ef4444',
          foreground: '#ffffff',
        },
        border: '#262626',
        input: '#262626',
        ring: '#6366f1',
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
    },
  },
  plugins: [],
}