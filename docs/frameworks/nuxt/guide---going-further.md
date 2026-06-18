# Nuxt - Guide - Going Further


## Runtime Config

# Runtime Config

> Nuxt provides a runtime config API to expose configuration and secrets within your application.

## Exposing

To expose config and environment variables to the rest of your app, you will need to define runtime configuration in your [`nuxt.config`](/docs/4.x/directory-structure/nuxt-config) file, using the [`runtimeConfig`](/docs/4.x/api/nuxt-config#runtimeconfig) option.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  runtimeConfig: {
    // The private keys which are only available within server-side
    apiSecret: '123',
    // Keys within public, will be also exposed to the client-side
    public: {
      apiBase: '/api',
    },
  },
})
```

When adding `apiBase` to the `runtimeConfig.public`, Nuxt adds it to each page payload. We can universally access `apiBase` in both server and browser.

```ts
const runtimeConfig = useRuntimeConfig()

console.log(runtimeConfig.apiSecret)
console.log(runtimeConfig.public.apiBase)
```

<tip>

Public runtime config is accessible in Vue templates with `$config.public`.

</tip>

### Serialization

Your runtime config will be serialized before being passed to Nitro. This means that anything that cannot be serialized and then deserialized (such as functions, Sets, Maps, and so on), should not be set in your `nuxt.config`.

Instead of passing non-serializable objects or functions into your application from your `nuxt.config`, you can place this code in a Nuxt or Nitro plugin or middleware.

### Environment Variables

The most common way to provide configuration is by using environment variables.

<note>

The Nuxt CLI has built-in support for reading your `.env` file in development, build and generate. But when you run your built server, **your .env file will not be read**.

<read-more to="/docs/4.x/directory-structure/env">



</read-more>
</note>

Runtime config values are **automatically replaced by matching environment variables at runtime**.

There are two key requirements:

1. Your desired variables must be defined in your `nuxt.config`. This ensures that arbitrary environment variables are not exposed to your application code.
2. Only a specially-named environment variable can override a runtime config property. That is, an uppercase environment variable starting with `NUXT_` which uses `_` to separate keys and case changes.

<warning>

Setting the default of `runtimeConfig` values to *differently named environment variables* (for example setting `myVar` to `process.env.OTHER_VARIABLE`) will only work during build-time and will break on runtime.
It is advised to use environment variables that match the structure of your `runtimeConfig` object.

</warning>

<tip icon="i-lucide-video" target="_blank" to="https://youtu.be/_FYV5WfiWvs">

Watch a video from Alexander Lichter showcasing the top mistake developers make using runtimeConfig.

</tip>

#### Example

```ini [.env]
NUXT_API_SECRET=api_secret_token
NUXT_PUBLIC_API_BASE=https://nuxtjs.org
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  runtimeConfig: {
    apiSecret: '', // can be overridden by NUXT_API_SECRET environment variable
    public: {
      apiBase: '', // can be overridden by NUXT_PUBLIC_API_BASE environment variable
    },
  },
})
```

## Reading

### Vue App

Within the Vue part of your Nuxt app, you will need to call [`useRuntimeConfig()`](/docs/4.x/api/composables/use-runtime-config) to access the runtime config.

<important>

The behavior is different between the client-side and server-side:

- On client-side, only keys in `runtimeConfig.public` and `runtimeConfig.app` (which is used by Nuxt internally) are available, and the object is both writable and reactive.
- On server-side, the entire runtime config is available, but it is read-only to avoid context sharing.

</important>

```vue [app/pages/index.vue]
<script setup lang="ts">
const config = useRuntimeConfig()

console.log('Runtime config:', config)
if (import.meta.server) {
  console.log('API secret:', config.apiSecret)
}
</script>

<template>
  <div>
    <div>Check developer console!</div>
  </div>
</template>
```

<caution>

**Security note:** Be careful not to expose runtime config keys to the client-side by either rendering them or passing them to `useState`.

</caution>

### Plugins

If you want to use the runtime config within any (custom) plugin, you can use [`useRuntimeConfig()`](/docs/4.x/api/composables/use-runtime-config) inside of your `defineNuxtPlugin` function.

```ts [app/plugins/config.ts]
export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig()

  console.log('API base URL:', config.public.apiBase)
})
```

### Server Routes

You can access runtime config within the server routes as well using `useRuntimeConfig`.

```ts [server/api/test.ts]
export default defineEventHandler(async (event) => {
  const { apiSecret } = useRuntimeConfig(event)
  const result = await $fetch('https://my.api.com/test', {
    headers: {
      Authorization: `Bearer ${apiSecret}`,
    },
  })
  return result
})
```

<note>

Giving the `event` as argument to `useRuntimeConfig` is optional, but it is recommended to pass it to get the runtime config overwritten by [environment variables](/docs/4.x/guide/going-further/runtime-config#environment-variables) at runtime for server routes.

</note>

## Typing Runtime Config

Nuxt tries to automatically generate a typescript interface from provided runtime config using [unjs/untyped](https://github.com/unjs/untyped).

But it is also possible to type your runtime config manually:

```ts [index.d.ts]
declare module 'nuxt/schema' {
  interface RuntimeConfig {
    apiSecret: string
  }
  interface PublicRuntimeConfig {
    apiBase: string
  }
}
// It is always important to ensure you import/export something when augmenting a type
export {}
```

<note>

`nuxt/schema` is provided as a convenience for end-users to access the version of the schema used by Nuxt in their project. Module authors should instead augment `@nuxt/schema`.

</note>

## Hooks

# Lifecycle Hooks

> Nuxt provides a powerful hooking system to expand almost every aspect using hooks.

<tip>

The hooking system is powered by [unjs/hookable](https://github.com/unjs/hookable).

</tip>

## Nuxt Hooks (Build Time)

These hooks are available for [Nuxt modules](/docs/4.x/guide/modules) and build context.

### Within `nuxt.config.ts`

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  hooks: {
    close: () => { },
  },
})
```

### Within Nuxt Modules

```js
import { defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options, nuxt) {
    nuxt.hook('close', async () => { })
  },
})
```

<read-more to="/docs/4.x/api/advanced/hooks#nuxt-hooks-build-time">

Explore all available Nuxt hooks.

</read-more>

## App Hooks (Runtime)

App hooks can be mainly used by [Nuxt Plugins](/docs/4.x/directory-structure/app/plugins) to hook into rendering lifecycle but could also be used in Vue composables.

```ts [app/plugins/test.ts]
export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.hook('page:start', () => {
    /* your code goes here */
  })
})
```

<read-more to="/docs/4.x/api/advanced/hooks#app-hooks-runtime">

Explore all available App hooks.

</read-more>

## Server Hooks (Runtime)

These hooks are available for [server plugins](/docs/4.x/directory-structure/server#server-plugins) to hook into Nitro's runtime behavior.

```ts [~~/server/plugins/test.ts]
export default defineNitroPlugin((nitroApp) => {
  nitroApp.hooks.hook('render:html', (html, { event }) => {
    console.log('render:html', html)
    html.bodyAppend.push('<hr>Appended by custom plugin')
  })

  nitroApp.hooks.hook('render:response', (response, { event }) => {
    console.log('render:response', response)
  })
})
```

<read-more to="/docs/4.x/api/advanced/hooks#nitro-app-hooks-runtime-server-side">

Learn more about available Nitro lifecycle hooks.

</read-more>

## Adding Custom Hooks

You can define your own custom hooks support by extending Nuxt's hook interfaces.

```ts
import type { HookResult } from '@nuxt/schema'

declare module '#app' {
  interface RuntimeNuxtHooks {
    'your-nuxt-runtime-hook': () => HookResult
  }
  interface NuxtHooks {
    'your-nuxt-hook': () => HookResult
  }
}

declare module 'nitropack/types' {
  interface NitroRuntimeHooks {
    'your-nitro-hook': () => void
  }
}
```

## Kit

# Nuxt Kit

> @nuxt/kit provides features for module authors.

Nuxt Kit provides composable utilities to make interacting with [Nuxt Hooks](/docs/4.x/api/advanced/hooks), the [Nuxt Interface](/docs/4.x/guide/going-further/internals#the-nuxt-interface) and developing [Nuxt modules](/docs/4.x/guide/modules) super easy.

<read-more to="/docs/4.x/api/kit">

Discover all Nuxt Kit utilities.

</read-more>

## Usage

### Install Dependency

You can install the latest Nuxt Kit by adding it to the `dependencies` section of your `package.json`. However, please consider always explicitly installing the `@nuxt/kit` package even if it is already installed by Nuxt.

<note>

`@nuxt/kit` and `@nuxt/schema` are key dependencies for Nuxt. If you are installing it separately, make sure that the versions of `@nuxt/kit` and `@nuxt/schema` are equal to or greater than your `nuxt` version to avoid any unexpected behavior.

</note>

```json [package.json]
{
  "dependencies": {
    "@nuxt/kit": "npm:@nuxt/kit-nightly@latest"
  }
}
```

### Import Kit Utilities

```ts [test.mjs]
import { useNuxt } from '@nuxt/kit'
```

<read-more to="/docs/4.x/api/kit">



</read-more>

<note>

Nuxt Kit utilities are only available for modules and not meant to be imported in runtime (components, Vue composables, pages, plugins, or server routes).

</note>

Nuxt Kit is an [esm-only package](/docs/4.x/guide/concepts/esm) meaning that you **cannot** `require('@nuxt/kit')`. As a workaround, use dynamic import in the CommonJS context:

```ts [test.cjs]
// This does NOT work!
// const kit = require('@nuxt/kit')
async function main () {
  const kit = await import('@nuxt/kit')
}
main()
```

## Nuxt App

# NuxtApp

> In Nuxt, you can access runtime app context within composables, components and plugins.

In Nuxt, you can access runtime app context within composables, components and plugins.

<read-more to="https://v2.nuxt.com/docs/internals-glossary/context/#the-context" target="_blank">

In Nuxt 2, this was referred to as **Nuxt context**.

</read-more>

## Nuxt App Interface

<read-more to="/docs/4.x/guide/going-further/internals#the-nuxtapp-interface">

Jump over the `NuxtApp` interface documentation.

</read-more>

## The Nuxt Context

Many composables and utilities, both built-in and user-made, may require access to the Nuxt instance. This doesn't exist everywhere on your application, because a fresh instance is created on every request.

Currently, the Nuxt context is only accessible in [plugins](/docs/4.x/directory-structure/app/plugins), [Nuxt hooks](/docs/4.x/guide/going-further/hooks), [Nuxt middleware](/docs/4.x/directory-structure/app/middleware) (if wrapped in `defineNuxtRouteMiddleware`), and [setup functions](https://vuejs.org/api/composition-api-setup) (in pages and components).

If a composable is called without access to the context, you may get an error stating that 'A composable that requires access to the Nuxt instance was called outside of a plugin, Nuxt hook, Nuxt middleware, or Vue setup function.' In that case, you can also explicitly call functions within this context by using [`nuxtApp.runWithContext`](/docs/4.x/api/composables/use-nuxt-app#runwithcontext).

## Accessing NuxtApp

Within composables, plugins and components you can access `nuxtApp` with [`useNuxtApp()`](/docs/4.x/api/composables/use-nuxt-app):

```ts [app/composables/useMyComposable.ts]
export function useMyComposable () {
  const nuxtApp = useNuxtApp()
  // access runtime nuxt app instance
}
```

If your composable does not always need `nuxtApp` or you simply want to check if it is present or not, since [`useNuxtApp`](/docs/4.x/api/composables/use-nuxt-app) throws an exception, you can use [`tryUseNuxtApp`](/docs/4.x/api/composables/use-nuxt-app#tryusenuxtapp) instead.

Plugins also receive `nuxtApp` as the first argument for convenience.

<read-more to="/docs/4.x/directory-structure/app/plugins">



</read-more>

## Providing Helpers

You can provide helpers to be usable across all composables and application. This usually happens within a Nuxt plugin.

```ts
const nuxtApp = useNuxtApp()
nuxtApp.provide('hello', name => `Hello ${name}!`)

console.log(nuxtApp.$hello('name')) // Prints "Hello name!"
```

<read-more to="/docs/4.x/directory-structure/app/plugins#providing-helpers">

It is possible to inject helpers by returning an object with a `provide` key in plugins.

</read-more>

<read-more to="https://v2.nuxt.com/docs/directory-structure/plugins/#inject-in-root--context" target="_blank">

In Nuxt 2 plugins, this was referred to as **inject function**.

</read-more>

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/nuxt.ts)

## Layers

# Authoring Nuxt Layers

> Nuxt provides a powerful system that allows you to extend the default files, configs, and much more.

Nuxt layers are a powerful feature that you can use to share and reuse partial Nuxt applications within a monorepo, or from a git repository or npm package. The layers structure is almost identical to a standard Nuxt application, which makes them easy to author and maintain.

<read-more to="/docs/4.x/getting-started/layers">



</read-more>

A minimal Nuxt layer directory should contain a [`nuxt.config.ts`](/docs/4.x/directory-structure/nuxt-config) file to indicate it is a layer.

```ts [base/nuxt.config.ts]
export default defineNuxtConfig({})
```

Additionally, certain other files in the layer directory will be auto-scanned and used by Nuxt for the project extending this layer.

- [`app/components/*`](/docs/4.x/directory-structure/app/components)   - Extend the default components
- [`app/composables/*`](/docs/4.x/directory-structure/app/composables)  - Extend the default composables
- [`app/layouts/*`](/docs/4.x/directory-structure/app/layouts)  - Extend the default layouts
- [`app/middleware/*`](/docs/4.x/directory-structure/app/middleware)  - Extend the default middleware
- [`app/pages/*`](/docs/4.x/directory-structure/app/pages)        - Extend the default pages
- [`app/plugins/*`](/docs/4.x/directory-structure/app/plugins)        - Extend the default plugins
- [`app/utils/*`](/docs/4.x/directory-structure/app/utils)   - Extend the default utils
- [`app/app.config.ts`](/docs/4.x/directory-structure/app/app-config)  - Extend the default app config
- [`server/*`](/docs/4.x/directory-structure/server)       - Extend the default server endpoints & middleware
- [`nuxt.config.ts`](/docs/4.x/directory-structure/nuxt-config)- Extend the default nuxt config

## Basic Example

<code-tree :expand-all="true" default-value="nuxt.config.ts">

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  extends: [
    './base',
  ],
})
```

```vue [app/app.vue]
<template>
  <BaseComponent />
</template>
```

```ts [base/nuxt.config.ts]
export default defineNuxtConfig({
  // Extending from base nuxt.config.ts!
  app: {
    head: {
      title: 'Extending Configs is Fun!',
      meta: [
        { name: 'description', content: 'I am using the extends feature in Nuxt!' },
      ],
    },
  },
})
```

```vue [base/app/components/BaseComponent.vue]
<template>
  <h1>Extending Components is Fun!</h1>
</template>
```

</code-tree>

## Layer Priority

When extending from multiple layers, it's important to understand the override order. Layers with **higher priority** override layers with lower priority when they define the same files or components.

The priority order from highest to lowest is:

1. **Your project files** - always have the highest priority
2. **Auto-scanned layers** from `~~/layers` directory - sorted alphabetically (Z has higher priority than A)
3. **Layers in extends** config - first entry has higher priority than second

### When to Use Each

- **extends** - Use for external dependencies (npm packages, remote repositories) or layers outside your project directory
- **~~/layers directory** - Use for local layers that are part of your project

<tip>

If you need to control the order of auto-scanned layers, you can prefix them with numbers: `~/layers/1.z-layer`, `~/layers/2.a-layer`. This way `2.a-layer` will have higher priority than `1.z-layer`.

</tip>

### Example

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  extends: [
    // Local layer outside the project
    '../base',
    // NPM package
    '@my-themes/awesome',
    // Remote repository
    'github:my-themes/awesome#v1',
  ],
})
```

If you also have `~~/layers/custom`, the priority order is:

- Your project files (highest)
- `~~/layers/custom`
- `../base`
- `@my-themes/awesome`
- `github:my-themes/awesome#v1` (lowest)

This means your project files will override any layer, and `~~/layers/custom` will override anything in `extends`.

## Starter Template

To get started you can initialize a layer with the [nuxt/starter/layer template](https://github.com/nuxt/starter/tree/layer). This will create a basic structure you can build upon. Execute this command within the terminal to get started:

```bash [Terminal]
npm create nuxt -- --template layer nuxt-layer
```

Follow up on the README instructions for the next steps.

## Publishing Layers

You can publish and share layers by either using a remote source or an npm package.

### Git Repository

You can use a git repository to share your Nuxt layer. Some examples:

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  extends: [
    // GitHub Remote Source
    'github:username/repoName',
    // GitHub Remote Source within /base directory
    'github:username/repoName/base',
    // GitHub Remote Source from dev branch
    'github:username/repoName#dev',
    // GitHub Remote Source from v1.0.0 tag
    'github:username/repoName#v1.0.0',
    // GitLab Remote Source example
    'gitlab:username/repoName',
    // Bitbucket Remote Source example
    'bitbucket:username/repoName',
  ],
})
```

<tip>

If you want to extend a private remote source, you need to add the environment variable `GIGET_AUTH=<token>` to provide a token.

</tip>

<tip>

If you want to extend a remote source from a self-hosted GitHub or GitLab instance, you need to supply its URL with the `GIGET_GITHUB_URL=<url>` or `GIGET_GITLAB_URL=<url>` environment variable - or directly configure it with [the `auth` option](https://github.com/unjs/c12#extending-config-layer-from-remote-sources) in your `nuxt.config`.

</tip>

<warning>

Bear in mind that if you are extending a remote source as a layer, you will not be able to access its dependencies outside of Nuxt. For example, if the remote layer depends on an eslint plugin, this will not be usable in your eslint config. That is because these dependencies will be located in a special location (`node_modules/.c12/layer_name/node_modules/`) that is not accessible to your package manager.

</warning>

<note>

When using git remote sources, if a layer has npm dependencies and you wish to install them, you can do so by specifying `install: true` in your layer options.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  extends: [
    ['github:username/repoName', { install: true }],
  ],
})
```

</note>

### npm Package

You can publish Nuxt layers as an npm package that contains the files and dependencies you want to extend. This allows you to share your config with others, use it in multiple projects or use it privately.

To extend from an npm package, you need to make sure that the module is published to npm and installed in the user's project as a devDependency. Then you can use the module name to extend the current nuxt config:

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  extends: [
    // Node Module with scope
    '@scope/moduleName',
    // or just the module name
    'moduleName',
  ],
})
```

To publish a layer directory as an npm package, you want to make sure that the `package.json` has the correct properties filled out. This will make sure that the files are included when the package is published.

```json [package.json]
{
  "name": "my-theme",
  "version": "1.0.0",
  "type": "module",
  "main": "./nuxt.config.ts",
  "dependencies": {},
  "devDependencies": {
    "nuxt": "^3.0.0"
  }
}
```

<important>

Make sure any dependency imported in the layer is **explicitly added** to the `dependencies`. The `nuxt` dependency, and anything only used for testing the layer before publishing, should remain in the `devDependencies` field.

</important>

Now you can proceed to publish the module to npm, either publicly or privately.

<important>

When publishing the layer as a private npm package, you need to make sure you log in, to authenticate with npm to download the node module.

</important>

## Tips

### Named Layer Aliases

Auto-scanned layers (from your `~~/layers` directory) automatically create aliases. For example, you can access your `~~/layers/test` layer via `#layers/test`.

If you want to create named layer aliases for other layers, you can specify a name in the configuration of the layer.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  $meta: {
    name: 'example',
  },
})
```

This will produce an alias of `#layers/example` which points to your layer.

### Relative Paths and Aliases

When importing using global aliases (such as `~/` and `@/`) in a layer components and composables, note that these aliases are resolved relative to the user's project paths. As a workaround, you can **use relative paths** to import them, or use named layer aliases.

Also when using relative paths in `nuxt.config` file of a layer, (with exception of nested `extends`) they are resolved relative to user's project instead of the layer. As a workaround, use full resolved paths in `nuxt.config`:

```ts [nuxt.config.ts]
import { fileURLToPath } from 'node:url'
import { dirname, join } from 'node:path'

const currentDir = dirname(fileURLToPath(import.meta.url))

export default defineNuxtConfig({
  css: [
    join(currentDir, './app/assets/main.css'),
  ],
})
```

## Disabling Modules from Layers

When extending a layer, you might want to disable certain modules that it includes. You can do this by setting the module's config key to `false` in your Nuxt config.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  extends: ['./base-layer'],
  // Disable modules from the layer by setting their config key to false
  image: false, // Disables @nuxt/image
  pinia: false, // Disables @pinia/nuxt
})
```

<note>

The config key is defined by each module. Common examples include `image` for `@nuxt/image`, `pinia` for `@pinia/nuxt`, and `content` for `@nuxt/content`. Check the module's documentation for its specific config key.

</note>

This is useful when:

- A layer includes modules you don't need in your project
- You want to use a different implementation than what the layer provides
- You need to disable analytics or other modules in specific environments

<tip>

You can also use this approach to disable modules in your own project - not just those from layers. Setting a module's config key to `false` will prevent its setup function from running while still generating types for the module.

</tip>

## Multi-Layer Support for Nuxt Modules

You can use the [`getLayerDirectories`](/docs/4.x/api/kit/layers#getlayerdirectories) utility from Nuxt Kit to support custom multi-layer handling for your modules.

```ts [modules/my-module.ts]
import { defineNuxtModule, getLayerDirectories } from 'nuxt/kit'

export default defineNuxtModule({
  setup (_options, nuxt) {
    const layerDirs = getLayerDirectories()

    for (const [index, layer] of layerDirs.entries()) {
      console.log(`Layer ${index}:`)
      console.log(`  Root: ${layer.root}`)
      console.log(`  App: ${layer.app}`)
      console.log(`  Server: ${layer.server}`)
      console.log(`  Pages: ${layer.appPages}`)
      // ... other directories
    }
  },
})
```

**Notes:**

- Earlier items in the array have higher priority and override later ones
- The user's project is the first item in the array

## Going Deeper

Configuration loading and extends support is handled by [unjs/c12](https://github.com/unjs/c12), merged using [unjs/defu](https://github.com/unjs/defu) and remote git sources are supported using [unjs/giget](https://github.com/unjs/giget). Check the docs and source code to learn more.

<read-more to="https://github.com/nuxt/nuxt/issues/13367" icon="i-simple-icons-github" target="_blank">

Checkout our ongoing development to bring more improvements for layers support on GitHub.

</read-more>

## Experimental Features

# Experimental Features

> Enable Nuxt experimental features to unlock new possibilities.

Nuxt includes experimental features that you can enable in your configuration file.

Internally, Nuxt uses `@nuxt/schema` to define these experimental features. You can refer to the [API documentation](/docs/4.x/guide/going-further/experimental-features) or the [source code](https://github.com/nuxt/nuxt/blob/main/packages/schema/src/config/experimental.ts) for more information.

<note>

Note that these features are experimental and could be removed or modified in the future.

</note>

## alwaysRunFetchOnKeyChange

Whether to run `useFetch` when the key changes, even if it is set to `immediate: false` and it has not been triggered yet.

`useFetch` and `useAsyncData` will always run when the key changes if `immediate: true` or if it has been already triggered.

This flag is disabled by default, but you can enable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    alwaysRunFetchOnKeyChange: true,
  },
})
```

## appManifest

Use app manifests to respect route rules on client-side.

This flag is enabled by default, but you can disable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    appManifest: false,
  },
})
```

## asyncContext

Enable native async context to be accessible for nested composables in Nuxt and in Nitro. This opens the possibility to use composables inside async composables and reduce the chance to get the `Nuxt instance is unavailable` error.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    asyncContext: true,
  },
})
```

<read-more to="https://github.com/nuxt/nuxt/pull/20918" icon="i-simple-icons-github" target="_blank">

See full explanation on the GitHub pull-request.

</read-more>

## asyncEntry

Enables generation of an async entry point for the Vue bundle, aiding module federation support.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    asyncEntry: true,
  },
})
```

## externalVue

Externalizes `vue`, `@vue/*` and `vue-router` when building.

This flag is enabled by default, but you can disable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    externalVue: false,
  },
})
```

<warning>

This feature will likely be removed in a near future.

</warning>

## extractAsyncDataHandlers

Extracts handler functions from `useAsyncData` and `useLazyAsyncData` calls into separate chunks for improved code splitting and caching efficiency.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    extractAsyncDataHandlers: true,
  },
})
```

This feature transforms inline handler functions into dynamically imported chunks:

```vue
<!-- Before -->
<script setup>
const { data } = await useAsyncData('user', async () => {
  return await $fetch('/api/user')
})
</script>
```

```vue
<!-- After transformation -->
<script setup>
const { data } = await useAsyncData('user', () =>
  import('/generated-chunk.js').then(r => r.default()),
)
</script>
```

The benefit of this transformation is that we can split out data fetching logic — while still allowing the code to be loaded if required.

<important>

This feature is only recommended for **static builds** with payload extraction, and where data does not need to be re-fetched at runtime.

</important>

## emitRouteChunkError

Emits `app:chunkError` hook when there is an error loading vite/webpack chunks. Default behavior is to perform a reload of the new route on navigation to a new route when a chunk fails to load.

By default, Nuxt will also perform a reload of the new route when a chunk fails to load when navigating to a new route (`automatic`).

Setting `automatic-immediate` will lead Nuxt to perform a reload of the current route right when a chunk fails to load (instead of waiting for navigation). This is useful for chunk errors that are not triggered by navigation, e.g., when your Nuxt app fails to load a [lazy component](/docs/4.x/directory-structure/app/components#dynamic-imports). A potential downside of this behavior is undesired reloads, e.g., when your app does not need the chunk that caused the error.

You can disable automatic handling by setting this to `false`, or handle chunk errors manually by setting it to `manual`.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    emitRouteChunkError: 'automatic', // or 'automatic-immediate', 'manual' or false
  },
})
```

## enforceModuleCompatibility

Whether Nuxt should throw an error (and fail to load) if a Nuxt module is incompatible.

This feature is disabled by default.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    enforceModuleCompatibility: true,
  },
})
```

## restoreState

Allows Nuxt app state to be restored from `sessionStorage` when reloading the page after a chunk error or manual [`reloadNuxtApp()`](/docs/4.x/api/utils/reload-nuxt-app) call.

To avoid hydration errors, it will be applied only after the Vue app has been mounted, meaning there may be a flicker on initial load.

<important>

Consider carefully before enabling this as it can cause unexpected behavior,
and consider providing explicit keys to [`useState`](/docs/4.x/api/composables/use-state) as auto-generated keys may not match across builds.

</important>

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    restoreState: true,
  },
})
```

## inlineRouteRules

Define route rules at the page level using [`defineRouteRules`](/docs/4.x/api/utils/define-route-rules).

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    inlineRouteRules: true,
  },
})
```

Matching route rules will be created, based on the page's `path`.

<read-more to="/docs/4.x/api/utils/define-route-rules" icon="i-lucide-square-function">

Read more in `defineRouteRules` utility.

</read-more>

<read-more to="/docs/4.x/guide/concepts/rendering#hybrid-rendering" icon="i-lucide-medal">



</read-more>

## renderJsonPayloads

Allows rendering of JSON payloads with support for revivifying complex types.

This flag is enabled by default, but you can disable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    renderJsonPayloads: false,
  },
})
```

## noVueServer

Disables Vue server renderer endpoint within Nitro.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    noVueServer: true,
  },
})
```

## parseErrorData

Whether to parse `error.data` when rendering a server error page.

This flag is enabled by default, but you can disable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    parseErrorData: false,
  },
})
```

## payloadExtraction

Controls how payload data is delivered for prerendered and cached (ISR/SWR) pages.

- `'client'` - Payload is inlined in HTML for the initial server render, and extracted to `_payload.json` files for client-side navigation. This avoids a separate network request on initial load while still enabling efficient client-side navigation.
- `true` - Payload is extracted to a separate `_payload.json` file for both the initial server render and client-side navigation.
- `false` - Payload extraction is disabled entirely. Payload is always inlined in HTML and no `_payload.json` files are generated.

The default is `true`, or `'client'` when `compatibilityVersion: 5` is set.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    // Inline payload in HTML, extract for client-side navigation only
    payloadExtraction: 'client',
  },
})
```

Payload extraction also works for routes using ISR (Incremental Static Regeneration) or SWR (Stale-While-Revalidate) caching strategies. This allows CDNs to cache payload files alongside HTML, improving client-side navigation performance for cached routes.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    payloadExtraction: 'client',
  },
  routeRules: {
    // Payload files will be generated for these cached routes
    '/products/**': { isr: 3600 },
    '/blog/**': { swr: true },
  },
})
```

## clientNodePlaceholder

Uses comment nodes (`<!--placeholder-->`) instead of `<div>` elements as placeholders for client-only components during server-side rendering.

When enabled, `.client.vue` components and `createClientOnly()` wrappers render an HTML comment on the server instead of an empty `<div>`. This fixes a Vue hydration issue where scoped styles may not be applied when the placeholder `<div>` and the actual component root share the same tag name.

<warning>

Enabling this means attributes (`class`, `style`, etc.) passed to `.client.vue` components will not appear in the SSR HTML. If you need styled placeholders to prevent layout shift, use `<ClientOnly>` with a `#fallback` slot instead.

</warning>

This flag is enabled when `future.compatibilityVersion` is set to `5` or higher, but you can also enable it explicitly:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    clientNodePlaceholder: true,
  },
})
```

## clientFallback

Enables the experimental [`<NuxtClientFallback>`](/docs/4.x/api/components/nuxt-client-fallback) component for rendering content on the client if there's an error in SSR.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    clientFallback: true,
  },
})
```

## crossOriginPrefetch

Enables cross-origin prefetch using the Speculation Rules API.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    crossOriginPrefetch: true,
  },
})
```

<read-more to="https://wicg.github.io/nav-speculation/prefetch.html" icon="i-simple-icons-w3c" target="_blank">

Read more about the **Speculation Rules API**.

</read-more>

## viewTransition

Enables View Transition API integration with client-side router.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    viewTransition: true,
  },
})
```

You can also pass an object to configure [view transition types](/docs/4.x/getting-started/transitions#view-transition-types), which allow different CSS animations based on the type of navigation:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    viewTransition: {
      enabled: true,
      types: ['slide'],
    },
  },
})
```

<link-example target="_blank" to="https://stackblitz.com/edit/nuxt-view-transitions?file=app.vue">



</link-example>

<read-more to="https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API" icon="i-simple-icons-mdnwebdocs" target="_blank">

Read more about the **View Transition API**.

</read-more>

<read-more to="https://developer.chrome.com/blog/view-transitions-update-io24" icon="i-simple-icons-google" target="_blank">

Read more about the **View Transition API**.

</read-more>

## writeEarlyHints

Enables writing of early hints when using node server.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    writeEarlyHints: true,
  },
})
```

## componentIslands

Enables experimental component islands support with [`<NuxtIsland>`](/docs/4.x/api/components/nuxt-island) and `.island.vue` files.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    componentIslands: true, // false or 'local+remote'
  },
})
```

<read-more to="/docs/4.x/directory-structure/app/components#server-components">



</read-more>

<read-more to="https://github.com/nuxt/nuxt/issues/19772" icon="i-simple-icons-github" target="_blank">

You can follow the server components roadmap on GitHub.

</read-more>

## localLayerAliases

Resolve `~`, `~~`, `@` and `@@` aliases located within layers with respect to their layer source and root directories.

This flag is enabled by default, but you can disable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    localLayerAliases: false,
  },
})
```

## typedPages

Enable the new experimental typed router.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    typedPages: true,
  },
})
```

Out of the box, this will enable typed usage of [`navigateTo`](/docs/4.x/api/utils/navigate-to), [`<NuxtLink>`](/docs/4.x/api/components/nuxt-link), [`router.push()`](/docs/4.x/api/composables/use-router) and more.

You can even get typed params within a page by using `const route = useRoute('route-name')`.

<video-accordion title="Watch a video from Daniel Roe explaining type-safe routing in Nuxt" video-id="SXk-L19gTZk">



</video-accordion>

## watcher

Set an alternative watcher that will be used as the watching service for Nuxt.

Nuxt uses `chokidar-granular` by default, which will ignore top-level directories
(like `node_modules` and `.git`) that are excluded from watching.

You can set this instead to `parcel` to use `@parcel/watcher`, which may improve
performance in large projects or on Windows platforms.

You can also set this to `chokidar` to watch all files in your source directory.

Set to `'builder'` to reuse the active builder's own file watcher (for example,
Vite's `server.watcher`) instead of starting a second one. This reduces the
number of file watchers active in dev mode and becomes the default when
`future.compatibilityVersion` is `5`. If the active builder does not implement
its own watcher (currently webpack and rspack), Nuxt logs a warning and falls
back to its default selection.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    watcher: 'chokidar-granular', // 'chokidar', 'parcel' or 'builder' are also options
  },
})
```

## sharedPrerenderData

Nuxt automatically shares payload *data* between pages that are prerendered. This can result in a significant performance improvement when prerendering sites that use `useAsyncData` or `useFetch` and fetch the same data in different pages.

You can disable this feature if needed.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    sharedPrerenderData: false,
  },
})
```

<video-accordion title="Watch a video from Alexander Lichter about the experimental sharedPrerenderData" video-id="1jUupYHVvrU">



</video-accordion>

It is particularly important when enabling this feature to make sure that any unique key of your data
is always resolvable to the same data. For example, if you are using `useAsyncData` to fetch
data related to a particular page, you should provide a key that uniquely matches that data. (`useFetch`
should do this automatically for you.)

```ts
// This would be unsafe in a dynamic page (e.g. `[slug].vue`) because the route slug makes a difference
// to the data fetched, but Nuxt can't know that because it's not reflected in the key.
const route = useRoute()
const { data } = await useAsyncData(async (_nuxtApp, { signal }) => {
  return await $fetch(`/api/my-page/${route.params.slug}`, { signal })
})
// Instead, you should use a key that uniquely identifies the data fetched.
const { data } = await useAsyncData(route.params.slug, async (_nuxtApp, { signal }) => {
  return await $fetch(`/api/my-page/${route.params.slug}`, { signal })
})
```

## clientNodeCompat

With this feature, Nuxt will automatically polyfill Node.js imports in the client build using [`unenv`](https://github.com/unjs/unenv).

<note>

To make globals like `Buffer` work in the browser, you need to manually inject them.

```ts
import { Buffer } from 'node:buffer'

globalThis.Buffer ||= Buffer
```

</note>

## scanPageMeta

Nuxt exposing some route metadata defined in `definePageMeta` at build-time to modules (specifically `alias`, `name`, `path`, `redirect`, `props` and `middleware`).

This only works with static or strings/arrays rather than variables or conditional assignment. See [original issue](https://github.com/nuxt/nuxt/issues/24770) for more information and context.

By default page metadata is only scanned after all routes have been registered in `pages:extend`. Then another hook, `pages:resolved` will be called.

You can disable this feature if it causes issues in your project.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    scanPageMeta: false,
  },
})
```

## cookieStore

Enables CookieStore support to listen for cookie updates (if supported by the browser) and refresh `useCookie` ref values.

This flag is enabled by default, but you can disable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    cookieStore: false,
  },
})
```

<read-more to="https://developer.mozilla.org/en-US/docs/Web/API/CookieStore" icon="i-simple-icons-mdnwebdocs" target="_blank">

Read more about the **CookieStore**.

</read-more>

## buildCache

Caches Nuxt build artifacts based on a hash of the configuration and source files.

This only works for source files within `srcDir` and `serverDir` for the Vue/Nitro parts of your app.

This flag is disabled by default, but you can enable it:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    buildCache: true,
  },
})
```

When enabled, changes to the following files will trigger a full rebuild:

```bash [Directory structure]
.nuxtrc
.npmrc
package.json
package-lock.json
yarn.lock
pnpm-lock.yaml
tsconfig.json
bun.lock
bun.lockb
```

In addition, any changes to files within `srcDir` will trigger a rebuild of the Vue client/server bundle. Nitro will always be rebuilt (though work is in progress to allow Nitro to announce its cacheable artifacts and their hashes).

<note>

A maximum of 10 cache tarballs are kept.

</note>

## checkOutdatedBuildInterval

Set the time interval (in ms) to check for new builds. Disabled when `experimental.appManifest` is `false`.

Set to `false` to disable.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    checkOutdatedBuildInterval: 3600000, // 1 hour, or false to disable
  },
})
```

## extraPageMetaExtractionKeys

The `definePageMeta()` macro is a useful way to collect build-time meta about pages. Nuxt itself provides a set list of supported keys which is used to power some of the internal features such as redirects, page aliases and custom paths.

This option allows passing additional keys to extract from the page metadata when using `scanPageMeta`.

```vue
<script lang="ts" setup>
definePageMeta({
  foo: 'bar',
})
</script>
```

```ts
export default defineNuxtConfig({
  experimental: {
    extraPageMetaExtractionKeys: ['foo'],
  },
  hooks: {
    'pages:resolved' (ctx) {
      // ✅ foo is available
    },
  },
})
```

This allows modules to access additional metadata from the page metadata in the build context. If you are using this within a module, it's recommended also to [augment the `NuxtPage` types with your keys](/docs/4.x/directory-structure/app/pages#typing-custom-metadata).

## navigationRepaint

Wait for a single animation frame before navigation, which gives an opportunity for the browser to repaint, acknowledging user interaction.

It can reduce INP when navigating on prerendered routes.

This flag is enabled by default, but you can disable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    navigationRepaint: false,
  },
})
```

## normalizeComponentNames

Nuxt updates auto-generated Vue component names to match the full component name you would use to auto-import the component.

If you encounter issues, you can disable this feature.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    normalizeComponentNames: false,
  },
})
```

By default, if you haven't set it manually, Vue will assign a component name that matches
the filename of the component.

```bash [Directory structure]
├─ components/
├─── SomeFolder/
├───── MyComponent.vue
```

In this case, the component name would be `MyComponent`, as far as Vue is concerned. If you wanted to use `<KeepAlive>` with it, or identify it in the Vue DevTools, you would need to use this component.

But in order to auto-import it, you would need to use `SomeFolderMyComponent`.

By setting `experimental.normalizeComponentNames`, these two values match, and Vue will generate a component name that matches the Nuxt pattern for component naming.

## normalizePageNames

Ensure that page component names match their route names. This sets the `__name` property on page components so that Vue's `<KeepAlive>` can correctly identify them by name.

By default, Vue assigns component names based on the filename. For example, `pages/foo/index.vue` and `pages/bar/index.vue` would both have the component name `index`. This makes name-based `<KeepAlive>` filtering unreliable because multiple pages share the same name.

With `normalizePageNames` enabled, page components are named after their route (e.g. `foo` and `bar`), so you can use `<KeepAlive>` with `include`/`exclude` without manually adding `defineOptions({ name: '...' })` to each page.

This flag is enabled when `future.compatibilityVersion` is set to `5` or higher, but you can disable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    normalizePageNames: false,
  },
})
```

```vue [app.vue]
<template>
  <NuxtPage :keepalive="{ include: ['foo'] }" />
</template>
```

## spaLoadingTemplateLocation

When rendering a client-only page (with `ssr: false`), we optionally render a loading screen (from `~/spa-loading-template.html`).

It can be set to `within`, which will render it like this:

```html
<div id="__nuxt">
  <!-- spa loading template -->
</div>
```

Alternatively, you can render the template alongside the Nuxt app root by setting it to `body`:

```html
<div id="__nuxt"></div>
<!-- spa loading template -->
```

This avoids a white flash when hydrating a client-only page.

## browserDevtoolsTiming

Enables performance markers for Nuxt hooks in browser devtools. This adds performance markers that you can track in the Performance tab of Chromium-based browsers, which is useful for debugging and optimizing performance.

This is enabled by default in development mode. If you need to disable this feature, it is possible to do so:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    browserDevtoolsTiming: false,
  },
})
```

<read-more to="https://github.com/nuxt/nuxt/pull/29922" icon="i-simple-icons-github" target="_blank" color="gray">

See PR #29922 for implementation details.

</read-more>

<read-more to="https://developer.chrome.com/docs/devtools/performance/extension#tracks" icon="i-simple-icons-googlechrome" target="_blank" color="gray">

Learn more about Chrome DevTools Performance API.

</read-more>

## debugModuleMutation

Records mutations to `nuxt.options` in module context, helping to debug configuration changes made by modules during the Nuxt initialization phase.

This is enabled by default when `debug` mode is enabled. If you need to disable this feature, it is possible to do so:

To enable it explicitly:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    debugModuleMutation: true,
  },
})
```

<read-more to="https://github.com/nuxt/nuxt/pull/30555" icon="i-simple-icons-github" target="_blank" color="gray">

See PR #30555 for implementation details.

</read-more>

## lazyHydration

This enables hydration strategies for `<Lazy>` components, which improves performance by deferring hydration of components until they're needed.

Lazy hydration is enabled by default, but you can disable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    lazyHydration: false,
  },
})
```

<read-more to="/docs/4.x/directory-structure/app/components#delayed-or-lazy-hydration" icon="i-simple-icons-github" color="gray">

Read more about lazy hydration.

</read-more>

## templateImportResolution

Disable resolving imports into Nuxt templates from the path of the module that added the template.

By default, Nuxt attempts to resolve imports in templates relative to the module that added them. Setting this to `false` disables this behavior, which may be useful if you're experiencing resolution conflicts in certain environments.

This flag is enabled by default, but you can disable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    templateImportResolution: false,
  },
})
```

<read-more to="https://github.com/nuxt/nuxt/pull/31175" icon="i-simple-icons-github" target="_blank" color="gray">

See PR #31175 for implementation details.

</read-more>

## templateRouteInjection

By default the route object returned by the auto-imported `useRoute()` composable is kept in sync with the current page in view in `<NuxtPage>`. This is not true for `vue-router`'s exported `useRoute` or for the default `$route` object available in your Vue templates.

By enabling this option a mixin will be injected to keep the `$route` template object in sync with Nuxt's managed `useRoute()`.

This flag is enabled by default, but you can disable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    templateRouteInjection: false,
  },
})
```

## decorators

This option enables decorator syntax across your entire Nuxt/Nitro app.

When using the Vite builder (default), decorators are lowered via [Babel](https://babeljs.io/) using [`@babel/plugin-proposal-decorators`](https://babeljs.io/docs/babel-plugin-proposal-decorators). When using the webpack or rspack builders, decorators are lowered via [esbuild](https://github.com/evanw/esbuild/releases/tag/v0.21.3).

For a long time, TypeScript has had support for decorators via `compilerOptions.experimentalDecorators`. This implementation predated the TC39 standardization process. Now, decorators are a [Stage 3 Proposal](https://github.com/tc39/proposal-decorators), and supported without special configuration in TS 5.0+ (see [https://github.com/microsoft/TypeScript/pull/52582](https://github.com/microsoft/TypeScript/pull/52582) and [https://devblogs.microsoft.com/typescript/announcing-typescript-5-0-beta/#decorators](https://devblogs.microsoft.com/typescript/announcing-typescript-5-0-beta/#decorators)).

Enabling `experimental.decorators` enables support for the TC39 proposal, **NOT** for TypeScript's previous `compilerOptions.experimentalDecorators` implementation.

<warning>

Note that there may be changes before this finally lands in the JS standard.

</warning>

### Usage

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    decorators: true,
  },
})
```

When using the Vite builder or the Nitro server build, you will need to install additional Babel packages as dev dependencies:

<code-group>

```bash [npm]
npm install -D @babel/plugin-proposal-decorators @babel/plugin-syntax-jsx
```

```bash [pnpm]
pnpm add -D @babel/plugin-proposal-decorators @babel/plugin-syntax-jsx
```

```bash [yarn]
yarn add -D @babel/plugin-proposal-decorators @babel/plugin-syntax-jsx
```

</code-group>

<tip>

Nuxt will prompt you to install these automatically if they are not already present.

</tip>

```ts [app/app.vue]
function something (_method: () => unknown) {
  return () => 'decorated'
}

class SomeClass {
  @something
  public someMethod () {
    return 'initial'
  }
}

const value = new SomeClass().someMethod()
// this will return 'decorated'
```

## defaults

This allows specifying the default options for core Nuxt components and composables.

These options will likely be moved elsewhere in the future, such as into `app.config` or into the `app/` directory.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    defaults: {
      nuxtLink: {
        componentName: 'NuxtLink',
        prefetch: true,
        prefetchOn: {
          visibility: true,
        },
      },
      useAsyncData: {
        deep: true,
      },
      useState: {
        resetOnClear: true,
      },
    },
  },
})
```

The `useState.resetOnClear` option controls whether [`clearNuxtState`](/docs/4.x/api/utils/clear-nuxt-state) resets state to its initial value (provided by the `init` function of [`useState`](/docs/4.x/api/composables/use-state)) instead of setting it to `undefined`. This defaults to `true` with `compatibilityVersion: 5`.

## purgeCachedData

Whether to clean up Nuxt static and asyncData caches on route navigation.

Nuxt will automatically purge cached data from `useAsyncData` and `nuxtApp.static.data`. This helps prevent memory leaks and ensures fresh data is loaded when needed, but it is possible to disable it.

This flag is enabled by default, but you can disable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    purgeCachedData: false,
  },
})
```

<read-more to="https://github.com/nuxt/nuxt/pull/31379" icon="i-simple-icons-github" target="_blank" color="gray">

See PR #31379 for implementation details.

</read-more>

## prefetchPreloadTags

When a `<NuxtLink>` is prefetched and the destination route has [payload extraction](#payloadextraction) enabled (the default for prerendered and cached routes), forward any `<link rel="preload">` hints that the destination set via [`useHead`](/docs/4.x/api/composables/use-head) (or via modules like [`@nuxt/image`](https://image.nuxt.com)'s `<NuxtImg preload>`) into the current document.

The forwarded links are downgraded from `rel="preload"` to `rel="prefetch"` so they don't compete with the current page's critical resources. Only user-defined head tags are forwarded; build-time JS/CSS chunk preloads are already handled separately by the prefetch pipeline.

This flag is off by default because, combined with `prefetchOn: 'visibility'` (the `<NuxtLink>` default), it could trigger a lot of cross-route prefetches at once. Enable it once you are confident the destination preloads are worth forwarding for the links your users typically encounter.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    prefetchPreloadTags: true,
  },
})
```

<read-more to="https://github.com/nuxt/nuxt/issues/34953" icon="i-simple-icons-github" target="_blank" color="gray">

See issue #34953 for motivation.

</read-more>

## granularCachedData

Whether to call and use the result from `getCachedData` when refreshing data for `useAsyncData` and `useFetch` (whether by `watch`, `refreshNuxtData()`, or a manual `refresh()` call.

This flag is enabled by default, but you can disable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    granularCachedData: false,
  },
})
```

<read-more to="https://github.com/nuxt/nuxt/pull/31373" icon="i-simple-icons-github" target="_blank" color="gray">

See PR #31373 for implementation details.

</read-more>

## headNext

Use head optimisations:

- Add the capo.js head plugin in order to render tags in of the head in a more performant way.
- Uses the hash hydration plugin to reduce initial hydration

This flag is enabled by default, but you can disable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    headNext: false,
  },
})
```

## pendingWhenIdle

For `useAsyncData` and `useFetch`, whether `pending` should be `true` when data has not yet started to be fetched.

This flag is disabled by default, but you can enable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    pendingWhenIdle: true,
  },
})
```

## entryImportMap

By default, Nuxt improves chunk stability by using an import map to resolve the entry chunk of the bundle.

This injects an import map at the top of your `<head>` tag:

```html
<script type="importmap">{"imports":{"#entry":"/_nuxt/DC5HVSK5.js"}}</script>
```

Within the script chunks emitted by Vite, imports will be from `#entry`. This means that changes to the entry will not invalidate chunks which are otherwise unchanged.

<note>

Nuxt smartly disables this feature if you have configured `vite.build.target` to include a browser that doesn't support import maps, or if you have configured `vite.build.rollupOptions.output.entryFileNames` to a value that does not include `[hash]`.

</note>

If you need to disable this feature you can do so:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    entryImportMap: false,
  },
  // or, better, simply tell vite your desired target
  // which nuxt will respect
  vite: {
    build: {
      target: 'safari13',
    },
  },
})
```

## typescriptPlugin

Enable enhanced TypeScript developer experience with the `@dxup/nuxt` module.

This experimental plugin provides improved TypeScript integration and development tooling for better DX when working with TypeScript in Nuxt applications.

This flag is disabled by default, but you can enable this feature:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    typescriptPlugin: true,
  },
})
```

<important>

To use this feature, you need to:

- Have `typescript` installed as a dependency
- Configure VS Code to use your workspace TypeScript version (see [VS Code documentation](https://code.visualstudio.com/docs/typescript/typescript-compiling#_using-the-workspace-version-of-typescript))

</important>

<read-more to="https://github.com/KazariEX/dxup" icon="i-simple-icons-github" target="_blank">

Learn more about **@dxup/nuxt**.

</read-more>

## viteEnvironmentApi

Enable Vite 6's new [Environment API](https://vite.dev/guide/api-environment) for improved build configuration and plugin architecture.

When you set `future.compatibilityVersion` to `5`, this feature is enabled by default. You can also enable it explicitly for testing:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    viteEnvironmentApi: true,
  },
})
```

The Vite Environment API provides better consistency between development and production builds, more granular control over environment-specific configuration, and improved performance.

<important>

Enabling this feature changes how Vite plugins are registered and configured. See the [Vite Environment API migration guide](/docs/4.x/getting-started/upgrade#migration-to-vite-environment-api) for details on updating your plugins.

</important>

<read-more to="https://vite.dev/guide/api-environment" target="_blank">

Learn more about Vite's Environment API.

</read-more>

## ssrStreaming

Enables SSR streaming to dramatically improve Time to First Byte (TTFB). When enabled, the server sends the HTML shell (including `<head>`, styles, preload hints, and entry scripts) immediately, then streams the rendered body content progressively using Vue's `renderToWebStream`.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    ssrStreaming: true,
  },
})
```

Streaming is automatically disabled for bot and crawler user agents (such as Googlebot, Bingbot, etc.) to ensure search engines receive fully-rendered HTML for SEO safety. The default pattern matches indexing crawlers only; Lighthouse and other audit tools deliberately fall outside it so synthetic measurements reflect the same streamed response real users get. You can customize the bot detection regex:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    ssrStreaming: {
      botRegex: /googlebot|bingbot|my-internal-crawler/i,
    },
  },
})
```

You can also control streaming per-route using `routeRules`:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    ssrStreaming: true,
  },
  routeRules: {
    '/no-stream/**': { streaming: false },
  },
})
```

<warning>

**Automatic fallback to non-streamed rendering.** Streaming commits the response status and headers as soon as the shell is flushed, which is incompatible with features that need to mutate the response after render. Requests matching any of the following are not streamed; they use the buffered renderer, or short-circuit to a redirect or error response:

- `routeRules` setting `noScripts`, `cache`, `isr`, `swr`, `redirect`, or `streaming: false` for the route
- `ssr: false` routes (already SPA-rendered)
- Bot/crawler user agents (controlled via `botRegex`)
- Prerendered routes (`nuxi generate`)
- Server-side `navigateTo()` redirects from plugins, middleware, or page setup
- Fatal errors thrown during initial render (before the shell flushes)

</warning>

<warning>

**Response status and headers must be set before the shell is flushed.** Streaming commits the HTTP status and headers with the first byte, so anything that mutates the response after that point cannot reach the client. This is inherent to streaming, not a Nuxt-specific bug.

The boundary is the shell flush:

- **Reaches the client**: mutations from Nuxt and Nitro plugins, which run to completion before rendering begins.
- **Dropped**: `setResponseStatus()`, `useResponseHeader()`, `useCookie()` writes and h3 `setHeader()`/`appendResponseHeader()` calls made during component rendering (including after an `await` in route middleware or `<script setup>`), since that work happens after the shell is already on the wire.

To keep a response mutation, move it into a plugin, or opt the route out of streaming:

- `routeRules: { '/path': { streaming: false } }`: static, per route.
- the `render:route` hook with `ctx.prefersStream = false`: runtime, per request (e.g. for routes that conditionally set a 404).

In development the streaming handler logs a warning naming the dropped mutations and the route, so these never fail silently.

</warning>

<note>

If an error occurs during streaming after the HTTP status is already committed, `payload.error` is set and the closing tags are still emitted as a well-formed document so the client picks up the error during hydration and renders the error page. Errors thrown before the shell flushes fall through to the buffered error renderer with the correct status code.

</note>

<note>

**Route styles are streamed, JS hints are entry-only.** The shell is flushed before the route renders, so its `<head>` carries entry-chunk styles and hints only. Once render registers the page and layout modules, their CSS is streamed straight after the shell (inlined as `<style>` when `inlineStyles` is enabled, otherwise as stylesheet links), so page, layout, and top-level async-component styles arrive before the body paints (nested async components are a FOUC caveat, covered below). Route-specific JS chunks are not preloaded from the shell; the browser discovers them after parsing the entry script. Streaming improves TTFB on every route; LCP gains are largest on routes whose JS overlaps the entry chunk.

</note>

<note>

**Component islands are compatible with streaming.** Island slot content and selective-client (`nuxt-client`) components are normally stitched into the HTML in a post-render pass, which is impossible once the body has streamed past the island anchors. Instead, the renderer emits each island teleport as an inert `<template>` at the end of the document and relocates it into place with an inline script that runs before hydration. This is transparent to app code. The exception is apps built with `features.noScripts` and island components, which fall back to the buffered renderer since the relocation script cannot run.

</note>

### Module hooks

Modules participate in the streaming response via the existing `render:html` hook (now with a `streaming: true` flag on the second argument) plus a per-request decision hook and two streaming-only hooks:

- **render:route** fires once per request before rendering begins, for every render (streaming enabled or not). Read `ctx.canStream` to see whether streaming is possible for the route, and set `ctx.prefersStream = false` to force buffered rendering for this request, e.g. based on a cookie, auth state, or A/B bucket. The renderer streams only when `canStream && prefersStream`. This is the runtime escape hatch for the static `routeRules` / `botRegex` config.
- **render:html** fires once, before the shell flushes, with `streaming: true` on its second argument. Mutations to `htmlAttrs`, `head`, `bodyAttrs`, and `bodyPrepend` reach the wire. Mutations to `body`/`bodyAppend` are dropped, since the body is about to stream (a dev-mode warning is emitted). Modules that only mutate head fields (CSP injection, OG tags, analytics meta) work in streaming with no code changes.
- **render:html:chunk** fires for each chunk produced by the renderer before it is enqueued. Mutate `ctx.chunk: Uint8Array` to transform bytes (e.g. nonce injection); read `ctx.index` to identify the first chunk vs. subsequent ones.
- **render:html:close** fires after the body stream completes, before closing tags. Mutate `ctx.bodyAppend: string[]` to inject final markup (end-of-body analytics tags, server-rendered debug widgets, etc.).

```ts
// modules/streaming-csp/src/runtime/server-plugin.ts
import { defineNitroPlugin } from '#imports'

export default defineNitroPlugin((nitro) => {
  nitro.hooks.hook('render:html', (ctx, { event }) => {
    const nonce = event.context.cspNonce
    if (!nonce) { return }
    // Works for both streaming (pre-shell) and buffered (post-render) paths.
    for (let i = 0; i < ctx.head.length; i++) {
      ctx.head[i] = ctx.head[i].replace(/<script(?![^>]*\snonce=)/g, `<script nonce="${nonce}"`)
    }
  })
})
```

<note>

**CSP nonce.** The streaming renderer emits several inline scripts and styles that bypass unhead: the bootstrap queue, the IIFE, suspense head pushes, island-teleport relocation, and route `<style>` blocks. If a `nonce` is present on the rendered head scripts, the renderer reuses it on all of them automatically, so a strict `script-src`/`style-src 'nonce-…'` policy does not block streaming. A module only needs to put the nonce on the head scripts (as above); the `render:html:chunk` hook remains available for stamping scripts that components render into the body.

</note>

<warning>

**Dev-mode FOUC for SFC styles:** in development, Vite serves SFC `<style>` blocks as JavaScript modules that inject styles client-side after the module evaluates, with no corresponding `<link>` in the shell. With streaming, the browser starts painting the streamed DOM before those style-injection modules run, so SFC-defined styles flash unstyled briefly.

Workaround: put paint-critical styles in a global CSS file registered via `css: ['~/assets/main.css']`. Global CSS files are emitted as `<link rel="stylesheet">` in the shell `<head>` and apply before body content streams. SFC `<style>` blocks remain fine for component-scoped styling that doesn't gate the initial paint.

Production builds extract all styles to real CSS files (or inline via `features.inlineStyles`), so this only affects `nuxt dev`. Validate streaming visuals against `nuxt build && nuxt preview`.

</warning>

<warning>

**Production FOUC for nested async components:** the renderer inlines route CSS in a chunk sent straight after the shell. It can only inline the styles for components whose modules are already registered at that point: the page, the layout, and any async component placed directly inside a `<Suspense>` boundary (Vue instantiates those eagerly when render begins).

An async component that is rendered *inside another async component* is instantiated only once its parent resolves, after the first chunk has streamed. Its SFC `<style>` misses the post-shell styles chunk and is emitted in the closing HTML instead, behind the component's own DOM. The browser paints that component unstyled until the final chunk arrives.

Avoid it by keeping paint-critical styling out of deeply nested async components:

- Put styles that gate the initial paint in a global CSS file (`css: ['~/assets/main.css']`); these reach the shell `<head>`.
- Style with utility classes (Tailwind, UnoCSS): utility CSS lives in the entry stylesheet, not per-component `<style>` blocks.
- Keep async components that own paint-critical `<style>` directly under a `<Suspense>` boundary rather than nested behind another async parent.
- Or opt the route out of streaming with `routeRules: { '/path': { streaming: false } }`.

Non-paint-critical scoped styles on nested async components are fine: the brief flash only matters for above-the-fold content.

</warning>

## Features

# Features

> Enable or disable optional Nuxt features to unlock new possibilities.

Some features of Nuxt are available on an opt-in basis, or can be disabled based on your needs.

## `features`

### devLogs

Stream server logs to the client as you are developing. These logs can be handled in the `dev:ssr-logs` hook.

By default, this is enabled in development (when test mode is not active).

If set to `silent`, the logs will not be printed to the browser console.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  features: {
    devLogs: true,
  },
})
```

### inlineStyles

Inlines styles when rendering HTML. This is currently available only when using Vite.

You can also pass a function that receives the path of a Vue component and returns a boolean indicating whether to inline the styles for that component.

It defaults to `(id) => id.includes('.vue')`.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  features: {
    inlineStyles: false, // or a function to determine inlining
  },
})
```

### noScripts

Turn off rendering of Nuxt scripts and JavaScript resource hints. Can also be configured granularly within `routeRules`.

You can also disable scripts more granularly within `routeRules`.

If set to 'production' or `true`, JavaScript will be disabled in production mode only. If set to 'all', JavaScript will be disabled in both development and production modes.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  features: {
    noScripts: true, // or 'production' | 'all' | false
  },
})
```

## `future`

There is also a `future` namespace for early opting-in to new features that will become default in a future (possibly major) version of the framework.

### compatibilityVersion

This enables early access to Nuxt features or flags.

Setting `compatibilityVersion` to `5` changes defaults throughout your Nuxt configuration to opt in to Nuxt v5 behaviour, including enabling the [Vite Environment API](/docs/4.x/guide/going-further/experimental-features#viteenvironmentapi).

```ts
export default defineNuxtConfig({
  future: {
    compatibilityVersion: 5,
  },
})
```

<read-more to="/docs/4.x/getting-started/upgrade#testing-nuxt-5">

Learn more about testing Nuxt 5.

</read-more>

### multiApp

This enables early access to the experimental multi-app support. You can follow the [tracker issue #21635](https://github.com/nuxt/nuxt/issues/21635) to see the progress of multi-app support in Nuxt.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  future: {
    multiApp: true,
  },
})
```

### typescriptBundlerResolution

This enables 'Bundler' module resolution mode for TypeScript, which is the recommended setting for frameworks like Nuxt and [Vite](https://vite.dev/guide/performance#reduce-resolve-operations).

It improves type support when using modern libraries with `exports`.

See [the original TypeScript pull request](https://github.com/microsoft/TypeScript/pull/51669).

You can set it to false to use the legacy 'Node' mode, which is the default for TypeScript.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  future: {
    typescriptBundlerResolution: false,
  },
})
```

## Internals

# How Nuxt Works?

> Nuxt is a minimal but highly customizable framework to build web applications.

This guide helps you better understand Nuxt internals to develop new solutions and module integrations on top of Nuxt.

## The Nuxt Interface

When you start Nuxt in development mode with [`nuxt dev`](/docs/4.x/api/commands/dev) or building a production application with [`nuxt build`](/docs/4.x/api/commands/build),
a common context will be created, referred to as `nuxt` internally. It holds normalized options merged with `nuxt.config` file,
some internal state, and a powerful [hooking system](/docs/4.x/api/advanced/hooks) powered by [unjs/hookable](https://github.com/unjs/hookable)
allowing different components to communicate with each other. You can think of it as **Builder Core**.

This context is globally available to be used with [Nuxt Kit](/docs/4.x/guide/going-further/kit) composables.
Therefore only one instance of Nuxt is allowed to run per process.

To extend the Nuxt interface and hook into different stages of the build process, we can use [Nuxt modules](/docs/4.x/guide/modules).

For more details, check out [the source code](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/core/nuxt.ts).

## The NuxtApp Interface

When rendering a page in the browser or on the server, a shared context will be created, referred to as `nuxtApp`.
This context keeps vue instance, runtime hooks, and internal states like ssrContext and payload for hydration.
You can think of it as **Runtime Core**.

This context can be accessed using [`useNuxtApp()`](/docs/4.x/api/composables/use-nuxt-app) composable within Nuxt plugins and `<script setup>` and vue composables.
Global usage is possible for the browser but not on the server, to avoid sharing context between users.

Since [`useNuxtApp`](/docs/4.x/api/composables/use-nuxt-app) throws an exception if context is currently unavailable, if your composable does not always require `nuxtApp`, you can use [`tryUseNuxtApp`](/docs/4.x/api/composables/use-nuxt-app#tryusenuxtapp) instead, which will return `null` instead of throwing an exception.

To extend the `nuxtApp` interface and hook into different stages or access contexts, we can use [Nuxt Plugins](/docs/4.x/directory-structure/app/plugins).

Check [Nuxt App](/docs/4.x/api/composables/use-nuxt-app) for more information about this interface.

`nuxtApp` has the following properties:

```ts
interface NuxtApp {
  vueApp // the global Vue application: https://vuejs.org/api/application.html#application-api

  versions // an object containing Nuxt and Vue versions

  // These let you call and add runtime NuxtApp hooks
  // https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/nuxt.ts#L18
  hooks
  hook
  callHook

  // Only accessible on server-side
  ssrContext: {
    url
    req
    res
    runtimeConfig
    noSSR
  }

  // This will be stringified and passed from server to client
  payload: {
    serverRendered: true
    data: {}
    state: {}
  }

  provide: (name: string, value: any) => void
}
```

For more details, check out [the source code](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/nuxt.ts).

## Runtime Context vs. Build Context

Nuxt builds and bundles project using Node.js but also has a runtime side.

While both areas can be extended, that runtime context is isolated from build-time. Therefore, they are not supposed to share state, code, or context other than runtime configuration!

`nuxt.config` and [Nuxt modules](/docs/4.x/guide/modules) can be used to extend the build context, and [Nuxt Plugins](/docs/4.x/directory-structure/app/plugins) can be used to extend runtime.

When building an application for production, `nuxt build` will generate a standalone build in the `.output` directory, independent of `nuxt.config` and [Nuxt modules](/docs/4.x/guide/modules).

## Debugging

# Debugging

> In Nuxt, you can get started with debugging your application directly in the browser as well as in your IDE.

## Sourcemaps

Sourcemaps are enabled for your server build by default, and for the client build in dev mode, but you can enable them more specifically in your configuration.

```ts
export default defineNuxtConfig({
  // or sourcemap: true
  sourcemap: {
    server: true,
    client: true,
  },
})
```

## Debugging with Node Inspector

You can use [Node inspector](https://nodejs.org/en/learn/getting-started/debugging) to debug Nuxt server-side.

```bash
nuxt dev --inspect
```

This will start Nuxt in `dev` mode with debugger active. If everything is working correctly a Node.js icon will appear on your Chrome DevTools and you can attach to the debugger.

<important>

Note that the Node.js and Chrome processes need to be run on the same platform. This doesn't work inside of Docker.

</important>

## Debugging in Your IDE

It is possible to debug your Nuxt app in your IDE while you are developing it.

### Example VS Code Debug Configuration

You may need to update the config below with a path to your web browser. For more information, visit the [VS Code documentation about debug configuration](https://code.visualstudio.com/docs/debugtest/debugging#_launch-configurations).

```json5
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  "version": "0.2.0",
  "configurations": [
    {
      "type": "chrome",
      "request": "launch",
      "name": "client: chrome",
      "url": "http://localhost:3000",
      // this should point to your Nuxt `srcDir`, which is `app` by default
      "webRoot": "${workspaceFolder}/app"
    },
    {
      "type": "node",
      "request": "launch",
      "name": "server: nuxt",
      "outputCapture": "std",
      "program": "${workspaceFolder}/node_modules/nuxt/bin/nuxt.mjs",
      "args": [
        "dev"
      ],
    }
  ],
  "compounds": [
    {
      "name": "fullstack: nuxt",
      "configurations": [
        "server: nuxt",
        "client: chrome"
      ]
    }
  ]
}
```

If you prefer your usual browser extensions, add this to the *chrome* configuration above:

```json5
"userDataDir": false,
```

### Example JetBrains IDEs Debug Configuration

You can also debug your Nuxt app in JetBrains IDEs such as IntelliJ IDEA, WebStorm, or PhpStorm.

1. Create a new file in your project root directory and name it `nuxt.run.xml`.
2. Open the `nuxt.run.xml` file and paste the following debug configuration:

```html
<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="client: chrome" type="JavascriptDebugType" uri="http://localhost:3000" useFirstLineBreakpoints="true">
    <method v="2" />
  </configuration>

  <configuration default="false" name="server: nuxt" type="NodeJSConfigurationType" application-parameters="dev" path-to-js-file="$PROJECT_DIR$/node_modules/nuxt/bin/nuxt.mjs" working-dir="$PROJECT_DIR$">
    <method v="2" />
  </configuration>

  <configuration default="false" name="fullstack: nuxt" type="CompoundRunConfigurationType">
    <toRun name="client: chrome" type="JavascriptDebugType" />
    <toRun name="server: nuxt" type="NodeJSConfigurationType" />
    <method v="2" />
  </configuration>
</component>
```

### Other IDEs

If you have another IDE and would like to contribute sample configuration, feel free to [open a PR](https://github.com/nuxt/nuxt/edit/main/docs/2.guide/3.going-further/9.debugging.md)!

## Events

# Creating Custom Events

> Nuxt provides a powerful event system powered by hookable.

Using events is a great way to decouple your application and allow for more flexible and modular communication between different parts of your code. Events can have multiple listeners that do not depend on each other. For example, you may wish to send an email to your user each time an order has shipped. Instead of coupling your order processing code to your email code, you can emit an event which a listener can receive and use to dispatch an email.

The Nuxt event system is powered by [unjs/hookable](https://github.com/unjs/hookable), which is the same library that powers the Nuxt hooks system.

## Creating Events and Listeners

You can create your own custom events using the `hook` method:

```ts
const nuxtApp = useNuxtApp()

nuxtApp.hook('app:user:registered', (payload) => {
  console.log('A new user has registered!', payload)
})
```

To emit an event and notify any listeners, use `callHook`:

```ts
const nuxtApp = useNuxtApp()

await nuxtApp.callHook('app:user:registered', {
  id: 1,
  name: 'John Doe',
})
```

You can also use the payload object to enable two-way communication between the emitter and listeners. Since the payload is passed by reference, a listener can modify it to send data back to the emitter.

```ts
const nuxtApp = useNuxtApp()

nuxtApp.hook('app:user:registered', (payload) => {
  payload.message = 'Welcome to our app!'
})

const payload = {
  id: 1,
  name: 'John Doe',
}

await nuxtApp.callHook('app:user:registered', {
  id: 1,
  name: 'John Doe',
})

// payload.message will be 'Welcome to our app!'
```

<tip>

You can inspect all events using the **Nuxt DevTools** Hooks panel.

</tip>

<read-more to="/docs/4.x/guide/going-further/hooks">

Learn more about Nuxt's built-in hooks and how to extend them

</read-more>