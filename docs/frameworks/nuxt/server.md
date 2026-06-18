# Nuxt — Server (Nitro)

## API Routes

Auto-registered from `server/api/`:

```ts
// server/api/hello.get.ts
export default defineEventHandler(() => ({ hello: 'world' }))

// server/api/users/[id].get.ts
export default defineEventHandler((event) => {
  const id = getRouterParam(event, 'id')
  return { user: { id } }
})
```

### HTTP Methods

`.get.ts`, `.post.ts`, `.put.ts`, `.patch.ts`, `.delete.ts`

## Route Parameters

```ts
// server/api/users/[id].get.ts
export default defineEventHandler((event) => {
  const id = getRouterParam(event, 'id')
  return { id }
})
```

## Request Body

```ts
export default defineEventHandler(async (event) => {
  const body = await readBody(event)
  return { received: body }
})
```

## Query Parameters

```ts
export default defineEventHandler((event) => {
  const query = getQuery(event)
  return { page: query.page }
})
```

## Server Middleware

`server/middleware/` — runs on every request before route handlers:

```ts
// server/middleware/log.ts
export default defineEventHandler((event) => {
  console.log(`${event.method} ${event.path}`)
})
```

## Server Plugins

`server/plugins/` — hook into Nitro lifecycle:

```ts
// server/plugins/my-plugin.ts
export default defineNitroPlugin((nitroApp) => {
  nitroApp.hooks.hook('request', (event) => { /* ... */ })
  nitroApp.hooks.hook('render:html', (html, { event }) => {
    html.head.push('<meta name="custom" content="value">')
  })
})
```

## Server Utils

`server/utils/` — auto-imported in server context.

## Runtime Config in Server

```ts
export default defineEventHandler((event) => {
  const config = useRuntimeConfig()
  return { secret: config.apiSecret }
})
```

## Error Handling

```ts
import { createError } from 'h3'

export default defineEventHandler(() => {
  throw createError({ statusCode: 401, message: 'Unauthorized' })
})
```

## CORS

```ts
export default defineNuxtConfig({
  nitro: {
    routeRules: {
      '/api/**': { cors: true },
    },
  },
})
```

Or per-handler:

```ts
export default defineEventHandler((event) => {
  setResponseHeader(event, 'Access-Control-Allow-Origin', '*')
})
```
