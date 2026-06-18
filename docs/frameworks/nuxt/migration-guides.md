# Nuxt — Migration Guides

## Nuxt 3 → Nuxt 4

### New Directory Structure

- `srcDir` defaults to `app/`
- Move `assets/`, `components/`, `composables/`, `layouts/`, `middleware/`, `pages/`, `plugins/`, `utils/` into `app/`
- Keep `server/`, `public/`, `layers/`, `modules/`, `content/` at root

### Data Fetching Changes

- Same key = shared refs across components
- `data` is now `shallowRef` (use `deep: true` for deep reactivity)
- `getCachedData` receives context with `ctx.cause`
- `pending` only `true` when status is pending

### Normalized Component Names

Component names now match auto-import pattern (`SomeFolderMyComponent` not just `MyComponent`).

### Unhead v2

- Removed: `vmid`, `hid`, `children`, `body` props
- Import from `#imports` instead of `@unhead/vue`

### TypeScript Changes

- `noUncheckedIndexedAccess: true` by default
- Separate tsconfig files for app/server/node/shared

### Other Breaking Changes

- Absolute `builder:watch` paths
- `window.__NUXT__` removed (use `useNuxtApp().payload`)
- Shallow data reactivity
- `clearNuxtState` resets to defaults
- Module loading order corrected (layers first)

### Codemods

```bash
npx codemod@0.18.7 nuxt/4/migration-recipe
```

## Nuxt 4 → Nuxt 5 (Preview)

Enable with:

```ts
export default defineNuxtConfig({
  future: { compatibilityVersion: 5 },
})
```

### New Features

- **Vite Environment API** — better build config per environment
- **Normalized page names** — match route names
- **Non-async `callHook`** — 20-40x faster (no Promise overhead)
- **Comment node placeholders** — `<ClientOnly>` uses `<!--placeholder-->` instead of `<div>`
- **clearNuxtState resets to defaults**

### Vite Environment API Migration

```ts
// Before
extendViteConfig((config) => { /* ... */ }, { server: false })

// After
addVitePlugin(() => ({
  name: 'my-plugin',
  configEnvironment(name, config) {
    if (name === 'client') { /* ... */ }
  },
  applyToEnvironment(env) { return env.name === 'client' },
}))
```

### Non-Async callHook

```diff
- nuxtApp.callHook('my:hook', data).then(() => { ... })
+ await nuxtApp.callHook('my:hook', data)
```

## Nuxt 2 → Nuxt 3 (Legacy)

See [Nuxt 3 migration docs](https://nuxt.com/docs/4.x/migration/overview).
