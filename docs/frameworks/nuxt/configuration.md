# Nuxt — Configuration

## nuxt.config.ts

Single source of truth for all config. `defineNuxtConfig` is globally available (no import).

```ts
export default defineNuxtConfig({
  // Your config
})
```

## Environment Overrides

```ts
export default defineNuxtConfig({
  $production: { routeRules: { '/**': { isr: true } } },
  $development: { /* ... */ },
  $env: { staging: { /* ... */ } },
})
```

Run with: `nuxt build --envName staging`

## runtimeConfig (Environment Variables)

Exposes values to the app. Private keys server-only; `public` keys also on client.

```ts
export default defineNuxtConfig({
  runtimeConfig: {
    apiSecret: '123',           // server-only
    public: {
      apiBase: '/api',          // also on client
    },
  },
})
```

Override with env vars: `NUXT_API_SECRET=token`

Access in components:

```vue
<script setup>
const runtimeConfig = useRuntimeConfig()
</script>
```

## app.config (Build-Time Config)

Public variables determined at build time. Cannot be overridden by env vars.

```ts
// app/app.config.ts
export default defineAppConfig({
  title: 'Hello Nuxt',
  theme: { dark: true, colors: { primary: '#ff0000' } },
})
```

Access: `const appConfig = useAppConfig()`

## runtimeConfig vs app.config

| Feature | runtimeConfig | app.config |
|---------|--------------|------------|
| Client-side | Hydrated | Bundled |
| Env vars | Yes | No |
| Reactive | Yes | Yes |
| Types support | Partial | Yes |
| Per-request config | No | Yes |
| HMR | No | Yes |
| Non-primitive types | No | Yes |

## External Config Files

Nuxt uses `nuxt.config.ts` as single source. These are configured inside it:

| Tool | Config Key |
|------|-----------|
| Nitro | `nitro` |
| PostCSS | `postcss` |
| Vite | `vite` |
| webpack | `webpack` |

Other configs still standalone: `tsconfig.json`, `eslint.config.js`, `prettier.config.js`, `tailwind.config.js`

## Vue Configuration (Vite)

```ts
export default defineNuxtConfig({
  vite: {
    vue: { customElement: true },
    vueJsx: { mergeProps: true },
  },
})
```

## Experimental Vue Features

```ts
export default defineNuxtConfig({
  vue: {
    propsDestructure: true,
  },
})
```
