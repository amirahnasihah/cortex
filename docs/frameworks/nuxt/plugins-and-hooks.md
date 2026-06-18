# Nuxt — Plugins & Hooks

## Plugins

`app/plugins/` — auto-registered at app creation.

```ts
// app/plugins/my-plugin.ts
export default defineNuxtPlugin((nuxtApp) => {
  // Client-side only
  if (import.meta.client) {
    console.log('Client plugin')
  }
  // Server-side only
  if (import.meta.server) {
    console.log('Server plugin')
  }
})
```

### Plugin with inject

```ts
export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig()
  return {
    provide: {
      hello: (msg) => `Hello ${msg}! (secret: ${config.apiSecret})`,
    },
  }
})
```

Use in components:

```vue
<script setup>
const { $hello } = useNuxtApp()
</script>

<template>
  <p>{{ $hello('world') }}</p>
</template>
```

### Conditional Plugins

```ts
// Only run on client
export default defineNuxtPlugin(() => { /* ... */ }, { parallel: true })

// Only on specific routes
export default defineNuxtPlugin(() => { /* ... */ })
```

## Nuxt Hooks

### Build Hooks

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  hooks: {
    'build:manifest': (manifest) => { /* ... */ },
    'pages:extend': (pages) => { /* ... */ },
    'app:resolve': (app) => { /* ... */ },
  },
})
```

### Runtime Hooks

```ts
// In plugins or middleware
const nuxtApp = useNuxtApp()
nuxtApp.callHook('my:hook', data)
nuxtApp.hooks.hook('my:hook', (data) => { /* ... */ })
```

### Common Hooks

| Hook | When |
|------|------|
| `app:created` | App instance created |
| `app:mounted` | App mounted on DOM |
| `page:transition:finish` | Page transition complete |
| `page:start` | Page component starts |
| `page:finish` | Page component rendered |
| `render:html` | HTML being rendered (server) |
| `render:response` | Response being sent |

## Nitro Hooks (Server)

```ts
// server/plugins/my-plugin.ts
export default defineNitroPlugin((nitroApp) => {
  nitroApp.hooks.hook('request', (event) => { /* ... */ })
  nitroApp.hooks.hook('render:html', (html, { event }) => {
    html.head.push('<meta name="x-custom" content="value">')
  })
})
```
