# Nuxt - Examples


## Hello World

# Hello World

> A minimal Nuxt application only requires the `app.vue` and `nuxt.config.js` files.

<read-more to="/docs/getting-started/introduction">



</read-more>

<sandbox branch="main" dir="examples/hello-world" file="app.vue" repo="nuxt/examples">



</sandbox>

## Auto Imports

# Auto Imports

> This example demonstrates the auto-imports feature in Nuxt.

Example of the auto-imports feature in Nuxt with:

- Vue components in the `components/` directory are auto-imported and can be used directly in your templates.
- Vue composables in the `composables/` directory are auto-imported and can be used directly in your templates and JS/TS files.
- JS/TS variables and functions in the `utils/` directory are auto-imported and can be used directly in your templates and JS/TS files.

<read-more to="/docs/guide/directory-structure/components">



</read-more>

<read-more to="/docs/guide/directory-structure/composables">



</read-more>

<read-more to="/docs/guide/directory-structure/utils">



</read-more>

<sandbox branch="main" dir="examples/features/auto-imports" file="app.vue" repo="nuxt/examples">



</sandbox>

## Data Fetching

# Data Fetching

> This example demonstrates data fetching with Nuxt using built-in composables and API routes.

<read-more to="/docs/getting-started/data-fetching">



</read-more>

<read-more to="/docs/guide/directory-structure/server">



</read-more>

<sandbox branch="main" dir="examples/features/data-fetching" file="app.vue" repo="nuxt/examples">



</sandbox>

## State Management

# State Management

> This example shows how to use the `useState` composable to create a reactive and SSR-friendly shared state across components.

<read-more to="/docs/getting-started/state-management">



</read-more>

<read-more to="/docs/api/composables/use-state">



</read-more>

<sandbox branch="main" dir="examples/features/state-management" file="app.vue" repo="nuxt/examples">



</sandbox>

## Meta Tags

# Meta Tags

> This example shows how to use the Nuxt helpers and composables for SEO and meta management.

<read-more to="/docs/getting-started/seo-meta">



</read-more>

<sandbox branch="main" dir="examples/features/meta-tags/" file="app.vue" repo="nuxt/examples">



</sandbox>

## Layouts

# Layouts

> This example shows how to define default and custom layouts.

<read-more to="/docs/getting-started/views#layouts">



</read-more>

<read-more to="/docs/guide/directory-structure/layouts">



</read-more>

<sandbox branch="main" dir="examples/features/layouts" file="pages/index.vue" repo="nuxt/examples">



</sandbox>

## Pages

# Pages

> This example shows how to use the pages/ directory to create application routes.

<read-more to="/docs/guide/directory-structure/pages">



</read-more>

<sandbox branch="main" dir="examples/routing/pages" file="app.vue" repo="nuxt/examples">



</sandbox>

## Middleware

# Middleware

> This example shows how to add route middleware with the middleware/ directory or with a plugin, and how to use them globally or per page.

<read-more to="/docs/guide/directory-structure/middleware">



</read-more>

<sandbox branch="main" dir="examples/routing/middleware" file="app.vue" repo="nuxt/examples">



</sandbox>

## Universal Router

# Universal Router

> This example demonstrates Nuxt universal routing utilities without depending on `pages/` and `vue-router`.

<sandbox branch="main" dir="examples/routing/universal-router" file="app.vue" repo="nuxt/examples">



</sandbox>

## Config Extends

# Layers

> This example shows how to use the extends key in `nuxt.config.ts`.

This example shows how to use the `extends` key in `nuxt.config.ts` to use the `base/` directory as a base Nuxt application, and use its components, composables or config and override them if necessary.

<read-more to="/docs/getting-started/layers">



</read-more>

<sandbox branch="main" dir="examples/advanced/config-extends" file="nuxt.config.ts" repo="nuxt/examples">



</sandbox>

## Error Handling

# Error Handling

> This example shows how to handle errors in different contexts: pages, plugins, components and middleware.

<read-more to="/docs/getting-started/error-handling">



</read-more>

<sandbox branch="main" dir="examples/advanced/error-handling" file="app.vue" repo="nuxt/examples">



</sandbox>

## Testing

# Testing

> This example shows how to test your Nuxt application.

<read-more to="/docs/getting-started/testing">



</read-more>

<sandbox branch="main" dir="examples/advanced/testing" file="app.vue" repo="nuxt/examples">



</sandbox>

## Use Cookie

# useCookie

> This example shows how to use the useCookie API to persist small amounts of data that both client and server can use.

<read-more to="/docs/api/composables/use-cookie">



</read-more>

<sandbox branch="main" dir="examples/advanced/use-cookie" file="app.vue" repo="nuxt/examples">



</sandbox>

## Jsx

# JSX / TSX

> This example shows how to use JSX syntax with typescript in Nuxt pages and components.

<read-more icon="i-simple-icons-vuedotjs" target="_blank" to="https://vuejs.org/guide/extras/render-function.html#jsx-tsx">



</read-more>

<sandbox branch="main" dir="examples/advanced/jsx" file="app.vue" repo="nuxt/examples">



</sandbox>

## Locale

# Locale

> This example shows how to define a locale composable to handle the application's locale, both server and client side.

<callout icon="i-ph-info-duotone">

You can right-click to "View Page Source" and see that Nuxt renders the correct date in SSR based on the visitor's locale.

</callout>

<sandbox branch="main" dir="examples/advanced/locale" file="app.vue" repo="nuxt/examples">



</sandbox>

## Teleport

# Teleport

> This example shows how to use the <Teleport> with client-side and server-side rendering.

Vue 3 provides the [`<Teleport>` component](https://vuejs.org/guide/built-ins/teleport.html) which allows content to be rendered elsewhere in the DOM, outside of the Vue application.

This example shows how to use the `<Teleport>` with client-side and server-side rendering.

<read-more to="/docs/api/components/teleports">



</read-more>

<sandbox branch="main" dir="examples/advanced/teleport" file="app.vue" repo="nuxt/examples">



</sandbox>