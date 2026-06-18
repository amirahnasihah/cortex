# Nuxt — Assets & Styling

## Asset Directories

### public/

Static assets served at root. No processing.

```
public/
  img/
    logo.png     → /img/logo.png
  robots.txt     → /robots.txt
```

### app/assets/

Processed by build tool (Vite/webpack).

```
app/assets/
  css/
    main.css
  images/
    hero.png
```

Reference with `~/assets/`:

```vue
<template>
  <img src="~/assets/images/hero.png" alt="Hero">
</template>
```

**Note:** Files in `app/assets/` are NOT served at `/assets/`. Use `public/` for static URLs.

---

## Styling

### CSS in Components

```vue
<style>
h1 { color: red; }
</style>

<style scoped>
.example { color: blue; }
</style>
```

### Global CSS

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  css: ['~/assets/css/main.css'],
})
```

### CSS Modules

```vue
<template>
  <p :class="$style.red">Red text</p>
</template>

<style module>
.red { color: red; }
</style>
```

### Dynamic Styles with v-bind

```vue
<script setup>
const color = ref('red')
</script>

<style>
.text { color: v-bind(color); }
</style>
```

---

## Preprocessors

Install:

```bash
npm install -D sass less stylus
```

Use in components:

```vue
<style lang="scss">
@use "~/assets/scss/main.scss";
</style>
```

Or globally:

```ts
export default defineNuxtConfig({
  css: ['~/assets/scss/main.scss'],
})
```

### Inject Variables

```ts
export default defineNuxtConfig({
  vite: {
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@use "~/assets/_colors.scss" as *;',
        },
      },
    },
  },
})
```

---

## PostCSS

Configured in `nuxt.config.ts`:

```ts
export default defineNuxtConfig({
  postcss: {
    plugins: {
      'postcss-nested': {},
      'postcss-custom-media': {},
    },
  },
})
```

Built-in plugins: `postcss-import`, `postcss-url`, `autoprefixer`, `cssnano`.

---

## External Stylesheets

```ts
export default defineNuxtConfig({
  app: {
    head: {
      link: [{ rel: 'stylesheet', href: 'https://cdn.example.com/style.css' }],
    },
  },
})
```

Or dynamically:

```ts
useHead({
  link: [{ rel: 'stylesheet', href: 'https://cdn.example.com/style.css' }],
})
```

---

## Tailwind CSS

```bash
npx nuxi@latest module add tailwindcss
```

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss'],
})
```

## UnoCSS

```bash
npx nuxi@latest module add unocss
```

---

## Nuxt UI (with Tailwind)

```bash
pnpm add @nuxt/ui tailwindcss
```

```ts
export default defineNuxtConfig({ modules: ['@nuxt/ui'] })
```

```css
@import "tailwindcss";
@import "@nuxt/ui";
```

---

## Transitions

```vue
<NuxtPage :transition="{ name: 'page', mode: 'out-in' }" />
```

```css
.page-enter-active,
.page-leave-active {
  transition: all 0.3s;
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1rem);
}
```
