# Nuxt — Deployment

## Build

```bash
nuxt build
```

Produces `.output/` directory — deployable anywhere.

## Preview

```bash
nuxt preview
# Opens http://localhost:3000 with production build
```

## Static Generation

```bash
nuxt generate
```

Pre-renders every route to HTML files.

## Output Structure

`.output/` contains everything — minified, tree-shaken, Node.js polyfills only.

## Platform Guides

### Node.js / Deno

```bash
node .output/server/index.mjs
```

### Vercel

```bash
npx nuxi@latest module add vercel
```

Or auto-detected via `vercel.json`.

### Netlify

```bash
npx nuxi@latest module add netlify
```

### Cloudflare Workers

```bash
npx nuxi@latest module add cloudflare
```

### AWS Amplify

Deploy the `.output/` directory.

### DigitalOcean App Platform

Point to `.output/server/index.mjs`.

### Docker

```dockerfile
FROM node:22-alpine
WORKDIR /app
COPY .output/ .output/
CMD ["node", ".output/server/index.mjs"]
```

### Static Hosting (GitHub Pages, etc.)

```bash
nuxt generate
```

Upload `.output/public/`.

## Environment Variables

```bash
NUXT_API_SECRET=secret node .output/server/index.mjs
```

Or `.env` file in production.

## Runtime Config in Production

```ts
export default defineNuxtConfig({
  runtimeConfig: {
    apiSecret: process.env.NUXT_API_SECRET,
  },
})
```

## Route Rules for Deployment

```ts
export default defineNuxtConfig({
  routeRules: {
    '/': { prerender: true },
    '/blog/**': { isr: 3600 },
    '/api/**': { cors: true },
  },
})
```
