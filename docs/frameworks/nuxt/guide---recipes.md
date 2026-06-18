# Nuxt - Guide - Recipes


## Custom Routing

# Custom Routing

> In Nuxt, your routing is defined by the structure of your files inside the pages directory. However, since it uses vue-router under the hood, Nuxt offers you several ways to add custom routes in your project.

## Adding custom routes

In Nuxt, your routing is defined by the structure of your files inside the [app/pages directory](/docs/4.x/directory-structure/app/pages). However, since it uses [vue-router](https://router.vuejs.org) under the hood, Nuxt offers you several ways to add custom routes in your project.

### Router Config

Using [router options](/docs/4.x/guide/recipes/custom-routing#router-options), you can optionally override or extend your routes using a function that accepts the scanned routes and returns customized routes.

If it returns `null` or `undefined`, Nuxt will fall back to the default routes (useful to modify input array).

```ts [router.options.ts]
import type { RouterConfig } from '@nuxt/schema'

export default {
  // https://router.vuejs.org/api/interfaces/routeroptions#routes
  routes: _routes => [
    {
      name: 'home',
      path: '/',
      component: () => import('~/pages/home.vue'),
    },
  ],
} satisfies RouterConfig
```

<note>

Nuxt will not augment any new routes you return from the `routes` function with metadata defined in `definePageMeta` of the component you provide. If you want that to happen, you should use the `pages:extend` hook which is [called at build-time](/docs/4.x/api/advanced/hooks#nuxt-hooks-build-time).

</note>

### Pages Hook

You can add, change or remove pages from the scanned routes with the `pages:extend` nuxt hook.

For example, to prevent creating routes for any `.ts` files:

```ts [nuxt.config.ts]
import type { NuxtPage } from '@nuxt/schema'

export default defineNuxtConfig({
  hooks: {
    'pages:extend' (pages) {
      // add a route
      pages.push({
        name: 'profile',
        path: '/profile',
        file: '~/extra-pages/profile.vue',
      })

      // remove routes
      function removePagesMatching (pattern: RegExp, pages: NuxtPage[] = []) {
        const pagesToRemove: NuxtPage[] = []
        for (const page of pages) {
          if (page.file && pattern.test(page.file)) {
            pagesToRemove.push(page)
          } else {
            removePagesMatching(pattern, page.children)
          }
        }
        for (const page of pagesToRemove) {
          pages.splice(pages.indexOf(page), 1)
        }
      }
      removePagesMatching(/\.ts$/, pages)
    },
  },
})
```

### Nuxt Module

If you plan to add a whole set of pages related with a specific functionality, you might want to use a [Nuxt module](/modules).

The [Nuxt kit](/docs/4.x/guide/going-further/kit) provides a few ways [to add routes](/docs/4.x/api/kit/pages):

- [`extendPages`](/docs/4.x/api/kit/pages#extendpages) (callback: pages => void)
- [`extendRouteRules`](/docs/4.x/api/kit/pages#extendrouterules) (route: string, rule: NitroRouteConfig, options: ExtendRouteRulesOptions)

## Router Options

On top of customizing options for [`vue-router`](https://router.vuejs.org/api/interfaces/routeroptions), Nuxt offers [additional options](/docs/4.x/api/nuxt-config#router) to customize the router.

### Using `router.options`

This is the recommended way to specify [router options](/docs/4.x/api/nuxt-config#router).

```ts [app/router.options.ts]
import type { RouterConfig } from '@nuxt/schema'

export default {
} satisfies RouterConfig
```

It is possible to add more router options files by adding files within the `pages:routerOptions` hook. Later items in the array override earlier ones.

<callout>

Adding a router options file in this hook will switch on page-based routing, unless `optional` is set, in which case it will only apply when page-based routing is already enabled.

</callout>

```ts [nuxt.config.ts]
import { createResolver } from '@nuxt/kit'

export default defineNuxtConfig({
  hooks: {
    'pages:routerOptions' ({ files }) {
      const resolver = createResolver(import.meta.url)
      // add a route
      files.push({
        path: resolver.resolve('./runtime/router-options'),
        optional: true,
      })
    },
  },
})
```

### Using `nuxt.config`

**Note:** Only JSON serializable [options](/docs/4.x/api/nuxt-config#router) are configurable:

- `linkActiveClass`
- `linkExactActiveClass`
- `end`
- `sensitive`
- `strict`
- `hashMode`
- `scrollBehaviorType`

```ts [nuxt.config]
export default defineNuxtConfig({
  router: {
    options: {},
  },
})
```

### Hash Mode (SPA)

You can enable hash history in SPA mode using the `hashMode` [config](/docs/4.x/api/nuxt-config#router). In this mode, router uses a hash character (#) before the actual URL that is internally passed. When enabled, the **URL is never sent to the server** and **SSR is not supported**.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  ssr: false,
  router: {
    options: {
      hashMode: true,
    },
  },
})
```

### Scroll Behavior for hash links

You can optionally customize the scroll behavior for hash links. When you set the [config](/docs/4.x/api/nuxt-config#router) to be `smooth` and you load a page with a hash link (e.g. `https://example.com/blog/my-article#comments`), you will see that the browser smoothly scrolls to this anchor.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  router: {
    options: {
      scrollBehaviorType: 'smooth',
    },
  },
})
```

#### Custom History (advanced)

You can optionally override history mode using a function that accepts the base URL and returns the history mode. If it returns `null` or `undefined`, Nuxt will fallback to the default history.

```ts [router.options.ts]
import type { RouterConfig } from '@nuxt/schema'
import { createMemoryHistory } from 'vue-router'

export default {
  // https://router.vuejs.org/api/interfaces/routeroptions
  history: base => import.meta.client ? createMemoryHistory(base) : null, /* default */
} satisfies RouterConfig
```

## Vite Plugin

# Using Vite Plugins in Nuxt

> Learn how to integrate Vite plugins into your Nuxt project.

While Nuxt modules offer extensive functionality, sometimes a specific Vite plugin might meet your needs more directly.

First, we need to install the Vite plugin, for our example, we'll use `@rollup/plugin-yaml`:

<code-group sync="pm">

```bash [npm]
npm install @rollup/plugin-yaml
```

```bash [yarn]
yarn add @rollup/plugin-yaml
```

```bash [pnpm]
pnpm add @rollup/plugin-yaml
```

```bash [bun]
bun add @rollup/plugin-yaml
```

```bash [deno]
deno add npm:@rollup/plugin-yaml
```

</code-group>

Next, we need to import and add it to our [`nuxt.config.ts`](/docs/4.x/directory-structure/nuxt-config) file:

```ts [nuxt.config.ts]
import yaml from '@rollup/plugin-yaml'

export default defineNuxtConfig({
  vite: {
    plugins: [
      yaml(),
    ],
  },
})
```

Now we installed and configured our Vite plugin, we can start using YAML files directly in our project.

For example, we can have a `config.yaml` that stores configuration data and import this data in our Nuxt components:

<code-group>

```yaml [data/hello.yaml]
greeting: "Hello, Nuxt with Vite!"
```

```vue [app/components/Hello.vue]
<script setup>
import config from '~/data/hello.yaml'
</script>

<template>
  <h1>{{ config.greeting }}</h1>
</template>
```

</code-group>

## Using Vite Plugins in Nuxt Modules

If you're developing a Nuxt module and need to add Vite plugins, you should use the [`addVitePlugin`](/docs/4.x/api/kit/builder#addviteplugin) utility:

```ts [modules/my-module.ts]
import { addVitePlugin, defineNuxtModule } from '@nuxt/kit'
import yaml from '@rollup/plugin-yaml'

export default defineNuxtModule({
  setup () {
    addVitePlugin(yaml())
  },
})
```

For environment-specific plugins in Nuxt 5+, use the `applyToEnvironment()` method:

```ts [modules/my-module.ts]
import { addVitePlugin, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    addVitePlugin(() => ({
      name: 'my-client-plugin',
      applyToEnvironment (environment) {
        return environment.name === 'client'
      },
      // Plugin configuration
    }))
  },
})
```

<important>

If you're writing code that needs to access resolved Vite configuration, you should use the `config` and `configResolved` hooks *within* your Vite plugin, rather than using Nuxt's `vite:extend`, `vite:extendConfig` and `vite:configResolved`.

</important>

<read-more to="/docs/4.x/api/kit/builder#addviteplugin">

Read more about `addVitePlugin` in the Nuxt Kit documentation.

</read-more>

## Custom Usefetch

# Custom useFetch in Nuxt

> How to create a custom fetcher for calling your external API in Nuxt.

When working with Nuxt, you might be making the frontend and fetching an external API, and you might want to set some default options for fetching from your API.

The [`$fetch`](/docs/4.x/api/utils/dollarfetch) utility function (used by the [`useFetch`](/docs/4.x/api/composables/use-fetch) composable) is intentionally not globally configurable. This is important so that fetching behavior throughout your application remains consistent, and other integrations (like modules) can rely on the behavior of core utilities like `$fetch`.

However, Nuxt provides a way to create a custom fetcher for your API (or multiple fetchers if you have multiple APIs to call).

## Recipe: API Client with Auth

Let's say you have an external API at `https://api.nuxt.com` that requires JWT authentication via [nuxt-auth-utils](https://github.com/atinux/nuxt-auth-utils), and you want to redirect to `/login` on `401` responses.

```ts [app/composables/useAPI.ts]
export const useAPI = createUseFetch({
  baseURL: 'https://api.nuxt.com',
  onRequest ({ options }) {
    const { session } = useUserSession()
    if (session.value?.token) {
      options.headers.set('Authorization', `Bearer ${session.value.token}`)
    }
  },
  async onResponseError ({ response }) {
    if (response.status === 401) {
      await navigateTo('/login')
    }
  },
})
```

Now every call to `useAPI` automatically includes the auth header and handles 401 redirects:

```vue [app/pages/dashboard.vue]
<script setup lang="ts">
const { data: profile } = await useAPI('/me')
const { data: orders } = await useAPI('/orders')
</script>
```

<read-more to="/docs/4.x/api/composables/create-use-fetch">



</read-more>

## Recipe: Custom `$fetch` Instance

If you need lower-level control, you can create a custom `$fetch` instance with a [Nuxt plugin](/docs/4.x/directory-structure/app/plugins) and either use it with `useAsyncData` directly or pass it to `createUseFetch`.

<note>

`$fetch` is a configured instance of [ofetch](https://github.com/unjs/ofetch) which supports adding the base URL of your Nuxt server as well as direct function calls during SSR (avoiding HTTP roundtrips).

</note>

```ts [app/plugins/api.ts]
export default defineNuxtPlugin((nuxtApp) => {
  const { session } = useUserSession()

  const api = $fetch.create({
    baseURL: 'https://api.nuxt.com',
    onRequest ({ request, options, error }) {
      if (session.value?.token) {
        options.headers.set('Authorization', `Bearer ${session.value?.token}`)
      }
    },
    async onResponseError ({ response }) {
      if (response.status === 401) {
        await nuxtApp.runWithContext(() => navigateTo('/login'))
      }
    },
  })

  return {
    provide: {
      api,
    },
  }
})
```

You can then use the custom `$fetch` instance directly:

```vue [app/app.vue]
<script setup>
const { $api } = useNuxtApp()
const { data: modules } = await useAsyncData('modules', () => $api('/modules'))
</script>
```

<callout>

Wrapping with [`useAsyncData`](/docs/4.x/api/composables/use-async-data) **avoids double data fetching when doing server-side rendering** (server & client on hydration).

</callout>

<link-example to="/docs/4.x/examples/advanced/use-custom-fetch-composable">



</link-example>

<video-accordion title="Watch a video about custom $fetch and Repository Pattern in Nuxt" video-id="jXH8Tr-exhI">



</video-accordion>

## Sessions And Authentication

# Sessions and Authentication

> Authentication is an extremely common requirement in web apps. This recipe will show you how to implement basic user registration and authentication in your Nuxt app.

## Introduction

In this recipe we'll be setting up authentication in a full-stack Nuxt app using [Nuxt Auth Utils](https://github.com/Atinux/nuxt-auth-utils) which provides convenient utilities for managing client-side and server-side session data.

The module uses secured & sealed cookies to store session data, so you don't need to setup a database to store session data.

## Install nuxt-auth-utils

Install the `nuxt-auth-utils` module using the `nuxt` CLI.

```bash [Terminal]
npx nuxt module add auth-utils
```

<callout>

This command will install `nuxt-auth-utils` as dependency and push it in the `modules` section of our `nuxt.config.ts`

</callout>

## Cookie Encryption Key

As `nuxt-auth-utils` uses sealed cookies to store session data, session cookies are encrypted using a secret key from the `NUXT_SESSION_PASSWORD` environment variable.

<note>

If not set, this environment variable will be added to your `.env` automatically when running in development mode.

</note>

```ini [.env]
NUXT_SESSION_PASSWORD=a-random-password-with-at-least-32-characters
```

<important>

You'll need to add this environment variable to your production environment before deploying.

</important>

## Login API Route

For this recipe, we'll create a simple API route to sign-in a user based on static data.

Let's create a `/api/login` API route that will accept a POST request with the email and password in the request body.

```ts [server/api/login.post.ts]
import { z } from 'zod'

const bodySchema = z.object({
  email: z.email(),
  password: z.string().min(8),
})

export default defineEventHandler(async (event) => {
  const { email, password } = await readValidatedBody(event, bodySchema.parse)

  if (email === 'admin@admin.com' && password === 'iamtheadmin') {
    // set the user session in the cookie
    // this server util is auto-imported by the auth-utils module
    await setUserSession(event, {
      user: {
        name: 'John Doe',
      },
    })
    return {}
  }
  throw createError({
    status: 401,
    message: 'Bad credentials',
  })
})
```

<callout>

Make sure to install the `zod` dependency in your project (`npm i zod`).

</callout>

<tip to="https://github.com/atinux/nuxt-auth-utils#server-utils">

Read more about the `setUserSession` server helper exposed by `nuxt-auth-utils`.

</tip>

## Login Page

The module exposes a Vue composable to know if a user is authenticated in our application:

```vue
<script setup>
const { loggedIn, session, user, clear, fetch } = useUserSession()
</script>
```

Let's create a login page with a form to submit the login data to our `/api/login` route.

```vue [app/pages/login.vue]
<script setup lang="ts">
const { loggedIn, user, fetch: refreshSession } = useUserSession()
const credentials = reactive({
  email: '',
  password: '',
})
async function login () {
  try {
    await $fetch('/api/login', {
      method: 'POST',
      body: credentials,
    })

    // Refresh the session on client-side and redirect to the home page
    await refreshSession()
    await navigateTo('/')
  } catch {
    alert('Bad credentials')
  }
}
</script>

<template>
  <form @submit.prevent="login">
    <input
      v-model="credentials.email"
      type="email"
      placeholder="Email"
    >
    <input
      v-model="credentials.password"
      type="password"
      placeholder="Password"
    >
    <button type="submit">
      Login
    </button>
  </form>
</template>
```

## Protect API Routes

Protecting server routes is key to making sure your data is safe. Client-side middleware is helpful for the user, but without server-side protection your data can still be accessed. It is critical to protect any routes with sensitive data, we should return a 401 error if the user is not logged in on those.

The `auth-utils` module provides the `requireUserSession` utility function to help make sure that users are logged in and have an active session.

Let's create an example of a `/api/user/stats` route that only authenticated users can access.

```ts [server/api/user/stats.get.ts]
export default defineEventHandler(async (event) => {
  // make sure the user is logged in
  // This will throw a 401 error if the request doesn't come from a valid user session
  const { user } = await requireUserSession(event)

  // TODO: Fetch some stats based on the user

  return {}
})
```

## Protect App Routes

Our data is safe with the server-side route in place, but without doing anything else, unauthenticated users would probably get some odd data when trying to access the `/users` page. We should create a [client-side middleware](https://nuxt.com/docs/4.x/directory-structure/app/middleware) to protect the route on the client side and redirect users to the login page.

`nuxt-auth-utils` provides a convenient `useUserSession` composable which we'll use to check if the user is logged in, and redirect them if they are not.

We'll create a middleware in the `/middleware` directory. Unlike on the server, client-side middleware is not automatically applied to all endpoints, and we'll need to specify where we want it applied.

```typescript [app/middleware/authenticated.ts]
export default defineNuxtRouteMiddleware(() => {
  const { loggedIn } = useUserSession()

  // redirect the user to the login screen if they're not authenticated
  if (!loggedIn.value) {
    return navigateTo('/login')
  }
})
```

## Home Page

Now that we have our app middleware to protect our routes, we can use it on our home page that display our authenticated user information. If the user is not authenticated, they will be redirected to the login page.

We'll use [`definePageMeta`](/docs/4.x/api/utils/define-page-meta) to apply the middleware to the route that we want to protect.

```vue [app/pages/index.vue]
<script setup lang="ts">
definePageMeta({
  middleware: ['authenticated'],
})

const { user, clear: clearSession } = useUserSession()

async function logout () {
  await clearSession()
  await navigateTo('/login')
}
</script>

<template>
  <div>
    <h1>Welcome {{ user.name }}</h1>
    <button @click="logout">
      Logout
    </button>
  </div>
</template>
```

We also added a logout button to clear the session and redirect the user to the login page.

## Conclusion

We've successfully set up a very basic user authentication and session management in our Nuxt app. We've also protected sensitive routes on the server and client side to ensure that only authenticated users can access them.

As next steps, you can:

- Add authentication using the [20+ supported OAuth providers](https://github.com/atinux/nuxt-auth-utils?tab=readme-ov-file#supported-oauth-providers)
- Add a database to store users, see [Nitro SQL Database](https://nitro.build/guide/database) or [NuxtHub SQL Database](https://hub.nuxt.com/docs/database)
- Let user signup with email & password using [password hashing](https://github.com/atinux/nuxt-auth-utils?tab=readme-ov-file#password-hashing)
- Add support for [WebAuthn / Passkeys](https://github.com/atinux/nuxt-auth-utils?tab=readme-ov-file#webauthn-passkey)

Checkout the open source [atidone repository](https://github.com/atinux/atidone) for a full example of a Nuxt app with OAuth authentication, database and CRUD operations.