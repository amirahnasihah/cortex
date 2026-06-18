# Nuxt — Views & Layouts

## app.vue

Entry point — renders for every route.

```vue
<template>
  <div>
    <NuxtPage />
  </div>
</template>
```

If you have layouts, wrap with `<NuxtLayout>`:

```vue
<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
```

## Components

Place in `app/components/` — auto-imported everywhere.

```
components/
  AppHeader.vue
  AppFooter.vue
  ui/
    BaseButton.vue
```

Use without imports:

```vue
<template>
  <AppHeader />
  <AppFooter />
</template>
```

### Nested Components

```
components/
  AppHeader.vue           → <AppHeader>
  ui/
    BaseButton.vue        → <UiBaseButton>
```

### Lazy Components

```vue
<ClientOnly>
  <LazyHeavyComponent />
</ClientOnly>
```

## Pages

Files in `app/pages/` = routes. Each page is a Vue component.

```vue
<!-- app/pages/index.vue -->
<template>
  <div>
    <h1>Home</h1>
  </div>
</template>
```

## Layouts

Wrappers around pages with shared UI (header, footer, sidebar).

`app/layouts/default.vue`:

```vue
<template>
  <div>
    <AppHeader />
    <slot />
    <AppFooter />
  </div>
</template>
```

### Custom Layouts

```vue
<!-- app/layouts/dashboard.vue -->
<template>
  <div class="dashboard">
    <Sidebar />
    <main><slot /></main>
  </div>
</template>
```

Assign to a page:

```vue
<script setup>
definePageMeta({ layout: 'dashboard' })
</script>
```

### Dynamic Layouts

```vue
<script setup>
const route = useRoute()
const layout = computed(() => route.meta.layout || 'default')
</script>

<template>
  <NuxtLayout :name="layout">
    <NuxtPage />
  </NuxtLayout>
</template>
```

## error.vue

Custom error page:

```vue
<!-- app/error.vue -->
<script setup>
defineProps({ error: Object })
</script>

<template>
  <div>
    <h2>{{ error.statusCode }}</h2>
    <p>{{ error.message }}</p>
    <button @click="clearError">Go home</button>
  </div>
</template>
```

## `<ClientOnly>`

Render only on client side:

```vue
<ClientOnly>
  <BrowserOnlyComponent />
  <template #fallback>
    <div>Loading...</div>
  </template>
</ClientOnly>
```

## `<DevOnly>`

Render only in development:

```vue
<DevOnly>
  <DevTools />
</DevOnly>
```

## `<NuxtLoadingIndicator>`

Progress bar between page navigations:

```vue
<NuxtLoadingIndicator />
```

## `<NuxtErrorBoundary>`

Catch client-side errors:

```vue
<NuxtErrorBoundary @error="handleError">
  <MyComponent />
  <template #error="{ error }">
    <p>Something went wrong: {{ error }}</p>
  </template>
</NuxtErrorBoundary>
```

## `<NuxtPage>`

Required in `app.vue` (or layout) to render pages:

```vue
<NuxtPage />
<!-- with transition -->
<NuxtPage :transition="{ name: 'page', mode: 'out-in' }" />
```
