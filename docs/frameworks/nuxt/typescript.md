# Nuxt — TypeScript

## Zero-Config TypeScript

Nuxt auto-generates types and `tsconfig.json`. Just use `.ts` for `nuxt.config.ts`.

## Auto-Generated Types

`.nuxt/` directory contains generated types:

- `tsconfig.app.json` — App code
- `tsconfig.server.json` — Server code
- `tsconfig.node.json` — Build-time code
- `tsconfig.shared.json` — Shared code

## Extending Types

```ts
// app/types/my-types.ts
interface User {
  id: number
  name: string
}

declare module '#app' {
  interface NuxtApp {
    $myHelper: (msg: string) => string
  }
}
```

## Typed Composables

```ts
// Custom typed composable
export function useUser(userId: string) {
  return useAsyncData(`user-${userId}`, () =>
    $fetch<User>(`/api/users/${userId}`)
  )
}
```

## Typed Route Params

```vue
<script setup>
const route = useRoute()
// route.params.id is typed based on file name [id].vue
</script>
```

## Type Checking

```bash
npx nuxt typecheck
```

## TypeScript Config Options

```ts
export default defineNuxtConfig({
  typescript: {
    tsConfig: {
      compilerOptions: {
        noUncheckedIndexedAccess: true, // default in v4
      },
    },
  },
})
```

## Nuxt 4 TypeScript Splitting

Separate configs for different contexts:

- `.nuxt/tsconfig.app.json` — Vue components, composables
- `.nuxt/tsconfig.server.json` — Nitro/server code
- `.nuxt/tsconfig.node.json` — Build-time (modules, config)
- `.nuxt/tsconfig.shared.json` — Shared types/utils

Opt into project references:

```json
{
  "references": [
    { "path": "./.nuxt/tsconfig.app.json" },
    { "path": "./.nuxt/tsconfig.server.json" },
    { "path": "./.nuxt/tsconfig.shared.json" },
    { "path": "./.nuxt/tsconfig.node.json" }
  ]
}
```

Update typecheck script:

```json
{
  "scripts": {
    "typecheck": "nuxt prepare && vue-tsc -b --noEmit"
  }
}
```
