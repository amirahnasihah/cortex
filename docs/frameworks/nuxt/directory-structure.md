# Nuxt - Directory Structure


## Directory Structure

# Nuxt Directory Structure

> Learn about the directory structure of a Nuxt application and how to use it.

Nuxt applications have a specific directory structure that is used to organize the code. This structure is designed to be easy to understand and to be used in a consistent way.

## Root Directory

The root directory of a Nuxt application is the directory that contains the `nuxt.config.ts` file. This file is used to configure the Nuxt application.

## App Directory

The `app/` directory is the main directory of the Nuxt application. It contains the following subdirectories:

- [`assets/`](/docs/4.x/directory-structure/app/assets): website's assets that the build tool (Vite or webpack) will process
- [`components/`](/docs/4.x/directory-structure/app/components): Vue components of the application
- [`composables/`](/docs/4.x/directory-structure/app/composables): add your Vue composables
- [`layouts/`](/docs/4.x/directory-structure/app/layouts): Vue components that wrap around your pages and avoid re-rendering between pages
- [`middleware/`](/docs/4.x/directory-structure/app/middleware): run code before navigating to a particular route
- [`pages/`](/docs/4.x/directory-structure/app/pages): file-based routing to create routes within your web application
- [`plugins/`](/docs/4.x/directory-structure/app/plugins): use Vue plugins and more at the creation of your Nuxt application
- [`utils/`](/docs/4.x/directory-structure/app/utils): add functions throughout your application that can be used in your components, composables, and pages.

This directory also includes specific files:

- [`app.config.ts`](/docs/4.x/directory-structure/app/app-config): a reactive configuration within your application
- [`app.vue`](/docs/4.x/directory-structure/app/app): the root component of your Nuxt application
- [`error.vue`](/docs/4.x/directory-structure/app/error): the error page of your Nuxt application

## Public Directory

The [`public/`](/docs/4.x/directory-structure/public) directory is the directory that contains the public files of the Nuxt application. Files contained within this directory are served at the root and are not modified by the build process.

This is suitable for files that have to keep their names (e.g. `robots.txt`) *or* likely won't change (e.g. `favicon.ico`).

## Server Directory

The [`server/`](/docs/4.x/directory-structure/server) directory is the directory that contains the server-side code of the Nuxt application. It contains the following subdirectories:

- [`api/`](/docs/4.x/directory-structure/server#server-routes): contains the API routes of the application.
- [`routes/`](/docs/4.x/directory-structure/server#server-routes): contains the server routes of the application (e.g. dynamic `/sitemap.xml`).
- [`middleware/`](/docs/4.x/directory-structure/server#server-middleware): run code before a server route is processed
- [`plugins/`](/docs/4.x/directory-structure/server#server-plugins): use plugins and more at the creation of the Nuxt server
- [`utils/`](/docs/4.x/directory-structure/server#server-utilities): add functions throughout your application that can be used in your server  code.

## Shared Directory

The [`shared/`](/docs/4.x/directory-structure/shared) directory is the directory that contains the shared code of the Nuxt application and Nuxt server. This code can be used in both the Vue app and the Nitro server.

## Content Directory

The [`content/`](/docs/4.x/directory-structure/content) directory is enabled by the [Nuxt Content](https://content.nuxt.com) module. It is used to create a file-based CMS for your application using Markdown files.

## Modules Directory

The [`modules/`](/docs/4.x/directory-structure/modules) directory is the directory that contains the local modules of the Nuxt application. Modules are used to extend the functionality of the Nuxt application.

## Layers Directory

The [`layers/`](/docs/4.x/directory-structure/layers) directory allows you to organize and share reusable code, components, composables, and configurations. Layers within this directory are automatically registered in your project.

## Nuxt Files

- [`nuxt.config.ts`](/docs/4.x/directory-structure/nuxt-config) file is the main configuration file for the Nuxt application.
- [`.nuxtrc`](/docs/4.x/directory-structure/nuxtrc) file is another syntax for configuring the Nuxt application (useful for global configurations).
- [`.nuxtignore`](/docs/4.x/directory-structure/nuxtignore) file is used to ignore files in the root directory during the build phase.

## Nuxt Config

# nuxt.config.ts

> Nuxt can be easily configured with a single nuxt.config file.

The `nuxt.config` file extension can either be `.js`, `.ts` or `.mjs`.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  // My Nuxt config
})
```

<tip>

`defineNuxtConfig` helper is globally available without import.

</tip>

You can explicitly import `defineNuxtConfig` from `nuxt/config` if you prefer:

```ts [nuxt.config.ts]twoslash
import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  // My Nuxt config
})
```

<read-more to="/docs/4.x/api/configuration/nuxt-config">

Discover all the available options in the **Nuxt configuration** documentation.

</read-more>

To ensure your configuration is up to date, Nuxt will make a full restart when detecting changes in the main configuration file, the [`.env`](/docs/4.x/directory-structure/env), [`.nuxtignore`](/docs/4.x/directory-structure/nuxtignore) and [`.nuxtrc`](/docs/4.x/directory-structure/nuxtrc) dotfiles.

## App

# app.vue
 Copy page The app.vue file is the main component of your Nuxt application. If you have a `app/pages/` directory, the `app.vue` file is optional. Nuxt will automatically include a default `app.vue`, but you can still add your own to customize the structure and content as needed.
## Usage

### Minimal Usage
 With Nuxt, the `app/pages/` directory is optional. If it is not present, Nuxt will not include the vue-router dependency. This is useful when building a landing page or an application that does not require routing.
 app/app.vue ` < template >
 < h1 > Hello World! </ h1 >
 </ template >
 ` Read and edit a live example in Docs > 4 X > Examples > Hello World .
### Usage with Pages
 When you have a `app/pages/` directory, you need to use the `<NuxtPage>` component to display the current page:
 app/app.vue ` < template >
 < NuxtPage />
 </ template >
 ` You can also define the common structure of your application directly in `app.vue`. This is useful when you want to include global elements such as a header or footer:
 app/app.vue ` < template >
 < header >
 Header content
 </ header >
 < NuxtPage />
 < footer >
 Footer content
 </ footer >
 </ template >
 ` Remember that `app.vue` acts as the main component of your Nuxt application. Anything you add to it (JS and CSS) will be global and included in every page. Learn more about how to structure your pages using the `app/pages/` directory.
### Usage with Layouts
 When your application requires different layouts for different pages, you can use the `app/layouts/` directory with the `<NuxtLayout>` component. This allows you to define multiple layouts and apply them per page.
 app/app.vue ` < template >
 < NuxtLayout >
 < NuxtPage />
 </ NuxtLayout >
 </ template >
 ` Learn more about how to structure your layouts using the `app/layouts/` directory. Was this helpful? 🤩 🙂 ☹️ 😰 Report an issue or Edit this page on GitHub utils
Use the utils/ directory to auto-import your utility functions throughout your application.
 app.config.ts
Expose reactive configuration within your application with the App Config file.
 Nuxt on Discord Nuxt on Bluesky Nuxt on X Nuxt on GitHub Menu On this page

## Pages

# pages

> Nuxt provides file-based routing to create routes within your web application.

<note>

To reduce your application's bundle size, this directory is **optional**, meaning that [`vue-router`](https://router.vuejs.org) won't be included if you only use [`app.vue`](/docs/4.x/directory-structure/app/app). To force the pages system, set `pages: true` in `nuxt.config` or have a [`router.options.ts`](/docs/4.x/guide/recipes/custom-routing#using-routeroptions).

</note>

## Usage

Pages are Vue components and can have any [valid extension](/docs/4.x/api/nuxt-config#extensions) that Nuxt supports (by default `.vue`, `.js`, `.jsx`, `.mjs`, `.ts` or `.tsx`).

Nuxt will automatically create a route for every page in your `~/pages/` directory.

<code-group>

```vue [app/pages/index.vue]
<template>
  <h1>Index page</h1>
</template>
```

```ts [pages/index.ts]twoslash
// https://vuejs.org/guide/extras/render-function.html
export default defineComponent({
  render () {
    return h('h1', 'Index page')
  },
})
```

```tsx [pages/index.tsx]twoslash
// https://nuxt.com/docs/4.x/examples/advanced/jsx
// https://vuejs.org/guide/extras/render-function.html#jsx-tsx
export default defineComponent({
  render () {
    return <h1>Index page</h1>
  },
})
```

</code-group>

The `app/pages/index.vue` file will be mapped to the `/` route of your application.

If you are using [`app.vue`](/docs/4.x/directory-structure/app/app), make sure to use the [`<NuxtPage/>`](/docs/4.x/api/components/nuxt-page) component to display the current page:

```vue [app/app.vue]
<template>
  <div>
    <!-- Markup shared across all pages, ex: NavBar -->
    <NuxtPage />
  </div>
</template>
```

Pages **must have a single root element** to allow [route transitions](/docs/4.x/getting-started/transitions) between pages. HTML comments are considered elements as well.

This means that when the route is server-rendered, or statically generated, you will be able to see its contents correctly, but when you navigate towards that route during client-side navigation the transition between routes will fail and you'll see that the route will not be rendered.

Here are some examples to illustrate what a page with a single root element looks like:

<code-group>

```vue [app/pages/working.vue]
<template>
  <div>
    <!-- This page correctly has only one single root element -->
    Page content
  </div>
</template>
```

```vue [app/pages/bad-1.vue]
<template>
  <!-- This page will not render when route changes during client side navigation, because of this comment -->
  <div>Page content</div>
</template>
```

```vue [app/pages/bad-2.vue]
<template>
  <div>This page</div>
  <div>Has more than one root element</div>
  <div>And will not render when route changes during client side navigation</div>
</template>
```

</code-group>

## Dynamic Routes

If you place anything within square brackets, it will be turned into a [dynamic route](https://router.vuejs.org/guide/essentials/dynamic-matching) parameter. You can mix and match multiple parameters and even non-dynamic text within a file name or directory.

If you want a parameter to be *optional*, you must enclose it in double square brackets - for example, `~/pages/[[slug]]/index.vue` or `~/pages/[[slug]].vue` will match both `/` and `/test`.

```bash [Directory Structure]
-| pages/
---| index.vue
---| users-[group]/
-----| [id].vue
```

Given the example above, you can access group/id within your component via the `$route` object:

```vue [app/pages/users-[group]/[id].vue]
<template>
  <p>{{ $route.params.group }} - {{ $route.params.id }}</p>
</template>
```

Navigating to `/users-admins/123` would render:

```html
<p>admins - 123</p>
```

If you want to access the route using Composition API, there is a global [`useRoute`](/docs/4.x/api/composables/use-route) function that will allow you to access the route just like `this.$route` in the Options API.

```vuetwoslash
<script setup lang="ts">
const route = useRoute()

if (route.params.group === 'admins' && !route.params.id) {
  console.log('Warning! Make sure user is authenticated!')
}
</script>
```

<note>

Named parent routes will take priority over nested dynamic routes. For the `/foo/hello` route, `~/pages/foo.vue` will take priority over `~/pages/foo/[slug].vue`. <br />

 Use `~/pages/foo/index.vue` and `~/pages/foo/[slug].vue` to match `/foo` and `/foo/hello` with different pages,.

</note>

<video-accordion platform="vimeo" title="Watch a video from Vue School on dynamic routes" video-id="754465699">



</video-accordion>

## Catch-all Route

If you need a catch-all route, you create it by using a file named like `[...slug].vue`. This will match *all* routes under that path.

```vue [app/pages/[...slug].vue]
<template>
  <p>{{ $route.params.slug }}</p>
</template>
```

Navigating to `/hello/world` would render:

```html
<p>["hello", "world"]</p>
```

## Nested Routes

It is possible to display [nested routes](https://router.vuejs.org/guide/essentials/nested-routes) with `<NuxtPage>`.

Example:

```bash [Directory Structure]
-| pages/
---| parent/
-----| child.vue
---| parent.vue
```

This file tree will generate these routes:

```js
[
  {
    path: '/parent',
    component: '~/pages/parent.vue',
    name: 'parent',
    children: [
      {
        path: 'child',
        component: '~/pages/parent/child.vue',
        name: 'parent-child',
      },
    ],
  },
]
```

To display the `child.vue` component, you have to insert the `<NuxtPage>` component inside `app/pages/parent.vue`:

```vue [pages/parent.vue]
<template>
  <div>
    <h1>I am the parent view</h1>
    <NuxtPage :foobar="123" />
  </div>
</template>
```

```vue [pages/parent/child.vue]
<script setup lang="ts">
const props = defineProps({
  foobar: String,
})

console.log(props.foobar)
</script>
```

### Child Route Keys

If you want more control over when the `<NuxtPage>` component is re-rendered (for example, for transitions), you can either pass a string or function via the `pageKey` prop, or you can define a `key` value via `definePageMeta`:

```vue [pages/parent.vue]
<template>
  <div>
    <h1>I am the parent view</h1>
    <NuxtPage :page-key="route => route.fullPath" />
  </div>
</template>
```

Or alternatively:

```vue [pages/parent/child.vue]twoslash
<script setup lang="ts">
definePageMeta({
  key: route => route.fullPath,
})
</script>
```

<link-example to="/docs/4.x/examples/routing/pages">



</link-example>

## Named Views

A single route can render into multiple `<NuxtPage>` outlets in a parent component by giving each outlet a `name` and providing a sibling page file for each name.

Use the `name@view.vue` filename convention to declare a named view alongside the default route file:

```bash [Directory Structure]
-| pages/
---| parent/
-----| child.vue
-----| child@sidebar.vue
---| parent.vue
```

Then render each outlet by name from the parent:

```vue [pages/parent.vue]
<template>
  <div>
    <NuxtPage />
    <aside>
      <NuxtPage name="sidebar" />
    </aside>
  </div>
</template>
```

When the user navigates to `/parent/child`, `child.vue` renders into the default `<NuxtPage />` and `child@sidebar.vue` renders into `<NuxtPage name="sidebar" />`. Outlets without a matching named view are left empty.

<note>

`definePageMeta` is read from the default route file only. Meta declared inside a `name@view.vue` sibling has no effect on the route.

</note>

<read-more to="https://router.vuejs.org/guide/essentials/named-views.html" target="_blank" title="Named Views">



</read-more>

## Route Groups

In some cases, you may want to group a set of routes together in a way which doesn't affect file-based routing. For this purpose, you can put files in a folder which is wrapped in parentheses - `(` and `)`.

For example:

```bash [Directory structure]
-| pages/
---| index.vue
---| (marketing)/
-----| about.vue
-----| contact.vue
```

This will produce `/`, `/about` and `/contact` pages in your app. The `marketing` group is ignored for purposes of your URL structure.

### Accessing Route Groups

Route groups are automatically available in the route metadata as `route.meta.groups`.
This allows you to access the group information in your components for conditional logic, styling, or other purposes.

```vue [pages/(marketing)/about.vue]
<script setup lang="ts">
const route = useRoute()

console.log(route.meta.groups) // Output: ['marketing']
</script>

<template>
  <div>
    <p v-if="route.meta.groups?.includes('marketing')">
      This is a marketing page
    </p>
  </div>
</template>
```

## Page Metadata

You might want to define metadata for each route in your app. You can do this using the `definePageMeta` macro, which will work both in `<script>` and in `<script setup>`:

```vuetwoslash
<script setup lang="ts">
definePageMeta({
  title: 'My home page',
})
</script>
```

This data can then be accessed throughout the rest of your app from the `route.meta` object.

```vuetwoslash
<script setup lang="ts">
const route = useRoute()

console.log(route.meta.title) // My home page
</script>
```

If you are using nested routes, the page metadata from all these routes will be merged into a single object. For more on route meta, see the [vue-router docs](https://router.vuejs.org/guide/advanced/meta).

Much like `defineEmits` or `defineProps` (see [Vue docs](https://vuejs.org/api/sfc-script-setup#defineprops-defineemits)), `definePageMeta` is a **compiler macro**. It will be compiled away so you cannot reference it within your component. Instead, the metadata passed to it will be hoisted out of the component.
Therefore, the page meta object cannot reference the component. However, it can reference imported bindings, as well as locally defined **pure functions**.

<warning>

Make sure not to reference any reactive data or functions that cause side effects. This can lead to unexpected behavior.

</warning>

```vue
<script setup lang="ts">
import { someData } from '~/utils/example'

function validateIdParam (route) {
  return route.params.id && !Number.isNaN(Number(route.params.id))
}

const title = ref('')

definePageMeta({
  validate: validateIdParam,
  someData,
  title, // do not do this, the ref will be hoisted out of the component
})
</script>
```

### Special Metadata

Of course, you are welcome to define metadata for your own use throughout your app. But some metadata defined with `definePageMeta` has a particular purpose:

#### `alias`

You can define page aliases. They allow you to access the same page from different paths. It can be either a string or an array of strings as defined [in the vue-router documentation](https://router.vuejs.org/guide/essentials/redirect-and-alias#Alias).

#### `keepalive`

Nuxt will automatically wrap your page in [the Vue `<KeepAlive>` component](https://vuejs.org/guide/built-ins/keep-alive#keepalive) if you set `keepalive: true` in your `definePageMeta`. This might be useful to do, for example, in a parent route that has dynamic child routes, if you want to preserve page state across route changes.

When your goal is to preserve state for parent routes use this syntax: `<NuxtPage keepalive />`. You can also set props to be passed to `<KeepAlive>` (see [a full list](https://vuejs.org/api/built-in-components#keepalive)).

You can set a default value for this property [in your `nuxt.config`](/docs/4.x/api/nuxt-config#keepalive).

#### `key`

[See above](/docs/4.x/directory-structure/app/pages#child-route-keys).

#### `layout`

You can define the layout used to render the route. This can be either false (to disable any layout), a string or a ref/computed, if you want to make it reactive in some way. [More about layouts](/docs/4.x/directory-structure/app/layouts).

#### `layoutTransition` and `pageTransition`

You can define transition properties for the `<transition>` component that wraps your pages and layouts, or pass `false` to disable the `<transition>` wrapper for that route. You can see [a list of options that can be passed](https://vuejs.org/api/built-in-components#transition) or read [more about how transitions work](https://vuejs.org/guide/built-ins/transition#transition).

You can set default values for these properties [in your `nuxt.config`](/docs/4.x/api/nuxt-config#layouttransition).

#### `middleware`

You can define middleware to apply before loading this page. It will be merged with all the other middleware used in any matching parent/child routes. It can be a string, a function (an anonymous/inlined middleware function following [the global before guard pattern](https://router.vuejs.org/guide/advanced/navigation-guards#Global-Before-Guards)), or an array of strings/functions. [More about named middleware](/docs/4.x/directory-structure/app/middleware).

#### `name`

You may define a name for this page's route.

#### `path`

You may define a path matcher, if you have a more complex pattern than can be expressed with the file name. See [the `vue-router` docs](https://router.vuejs.org/guide/essentials/route-matching-syntax#Custom-regex-in-params) for more information.

#### `props`

Allows accessing the route `params` as props passed to the page component. See [the `vue-router` docs](https://router.vuejs.org/guide/essentials/passing-props) for more information.

### Typing Custom Metadata

If you add custom metadata for your pages, you may wish to do so in a type-safe way. It is possible to augment the type of the object accepted by `definePageMeta`:

```ts [index.d.ts]
declare module '#app' {
  interface PageMeta {
    pageType?: string
  }
}

// It is always important to ensure you import/export something when augmenting a type
export {}
```

## Navigation

To navigate between pages of your app, you should use the [`<NuxtLink>`](/docs/4.x/api/components/nuxt-link) component.

This component is included with Nuxt and therefore you don't have to import it as you do with other components.

A simple link to the `index.vue` page in your `app/pages` folder:

```vue
<template>
  <NuxtLink to="/">Home page</NuxtLink>
</template>
```

<read-more to="/docs/4.x/api/components/nuxt-link">

Learn more about `<NuxtLink>` usage.

</read-more>

## Programmatic Navigation

Nuxt allows programmatic navigation through the `navigateTo()` utility method. Using this utility method, you will be able to programmatically navigate the user in your app. This is great for taking input from the user and navigating them dynamically throughout your application. In this example, we have a simple method called `navigate()` that gets called when the user submits a search form.

<note>

Make sure to always `await` on `navigateTo` or chain its result by returning from functions.

</note>

```vuetwoslash
<script setup lang="ts">
const name = ref('')
const type = ref(1)

function navigate () {
  return navigateTo({
    path: '/search',
    query: {
      name: name.value,
      type: type.value,
    },
  })
}
</script>
```

## Client-Only Pages

You can define a page as [client only](/docs/4.x/directory-structure/app/components#client-components) by giving it a `.client.vue` suffix. None of the content of this page will be rendered on the server.

## Server-Only Pages

You can define a page as [server only](/docs/4.x/directory-structure/app/components#server-components) by giving it a `.server.vue` suffix. While you will be able to navigate to the page using client-side navigation, controlled by `vue-router`, it will be rendered with a server component automatically, meaning the code required to render the page will not be in your client-side bundle.

<warning>

Server-only pages must have a single root element. (HTML comments are considered elements as well.)

</warning>

## Custom Routing

As your app gets bigger and more complex, your routing might require more flexibility. For this reason, Nuxt directly exposes the router, routes and router options for customization in different ways.

<read-more to="/docs/4.x/guide/recipes/custom-routing">



</read-more>

## Multiple Pages Directories

By default, all your pages should be in one `app/pages` directory at the root of your project.

However, you can use [Nuxt Layers](/docs/4.x/getting-started/layers) to create groupings of your app's pages:

```bash [Directory Structure]
-| some-app/
---| nuxt.config.ts
---| pages/
-----| app-page.vue
-| nuxt.config.ts
```

```ts [some-app/nuxt.config.ts]twoslash
// some-app/nuxt.config.ts
export default defineNuxtConfig({
})
```

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  extends: ['./some-app'],
})
```

<read-more to="/docs/4.x/guide/going-further/layers">



</read-more>

## Components

# components

> The components/ directory is where you put all your Vue components.

Nuxt automatically imports any components in this directory (along with components that are registered by any modules you may be using).

```bash [Directory Structure]
-| components/
---| AppHeader.vue
---| AppFooter.vue
```

```html [app/app.vue]
<template>
  <div>
    <AppHeader />
    <NuxtPage />
    <AppFooter />
  </div>
</template>
```

## Component Names

If you have a component in nested directories such as:

```bash [Directory Structure]
-| components/
---| base/
-----| foo/
-------| Button.vue
```

... then the component's name will be based on its own path directory and filename, with duplicate segments being removed. Therefore, the component's name will be:

```html
<BaseFooButton />
```

<note>

For clarity, we recommend that the component's filename matches its name. So, in the example above, you could rename `Button.vue` to be `BaseFooButton.vue`.

</note>

If you want to auto-import components based only on its name, not path, then you need to set `pathPrefix` option to `false` using extended form of the configuration object:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  components: [
    {
      path: '~/components',
      pathPrefix: false, // [!code ++]
    },
  ],
})
```

This registers the components using the same strategy as used in Nuxt 2. For example, `~/components/Some/MyComponent.vue` will be usable as `<MyComponent>` and not `<SomeMyComponent>`.

## Dynamic Components

If you want to use the Vue `<component :is="someComputedComponent">` syntax, you need to use the `resolveComponent` helper provided by Vue or import the component directly from `#components` and pass it into `is` prop.

For example:

```vue [app/pages/index.vue]
<script setup lang="ts">
import { SomeComponent } from '#components'

const MyButton = resolveComponent('MyButton')
</script>

<template>
  <component :is="clickable ? MyButton : 'div'" />
  <component :is="SomeComponent" />
</template>
```

<important>

If you are using `resolveComponent` to handle dynamic components, make sure not to insert anything but the name of the component, which must be a literal string and not be or contain a variable. The string is statically analyzed at the compilation step.

</important>

<video-accordion title="Watch Daniel Roe's short video about resolveComponent()" video-id="4kq8E5IUM2U">



</video-accordion>

Alternatively, though not recommended, you can register all your components globally, which will create async chunks for all your components and make them available throughout your application.

```diff
export default defineNuxtConfig({
    components: {
+     global: true,
+     dirs: ['~/components']
    },
  })
```

You can also selectively register some components globally by placing them in a `~/components/global` directory, or by using a `.global.vue` suffix in the filename. As noted above, each global component is rendered in a separate chunk, so be careful not to overuse this feature.

<note>

The `global` option can also be set per component directory.

</note>

## Dynamic Imports

To dynamically import a component (also known as lazy-loading a component) all you need to do is add the `Lazy` prefix to the component's name. This is particularly useful if the component is not always needed.

By using the `Lazy` prefix you can delay loading the component code until the right moment, which can be helpful for optimizing your JavaScript bundle size.

```vue [app/pages/index.vue]
<script setup lang="ts">
const show = ref(false)
</script>

<template>
  <div>
    <h1>Mountains</h1>
    <LazyMountainsList v-if="show" />
    <button
      v-if="!show"
      @click="show = true"
    >
      Show List
    </button>
  </div>
</template>
```

## Delayed (or Lazy) Hydration

Lazy components are great for controlling the chunk sizes in your app, but they don't always enhance runtime performance, as they still load eagerly unless conditionally rendered. In real-world applications, some pages may include a lot of content and a lot of components, and most of the time not all of them need to be interactive as soon as the page is loaded. Having them all load eagerly can negatively impact performance.

In order to optimize your app, you may want to delay the hydration of some components until they're visible, or until the browser is done with more important tasks.

Nuxt supports this using lazy (or delayed) hydration, allowing you to control when components become interactive.

### Hydration Strategies

Nuxt provides a range of built-in hydration strategies. Only one strategy can be used per lazy component.

<note>

Any prop change on a lazily hydrated component will trigger hydration immediately. (e.g., changing a prop on a component with `hydrate-never` will cause it to hydrate)

</note>

<warning>

Currently Nuxt's built-in lazy hydration only works in single-file components (SFCs), and requires you to define the prop in the template (rather than spreading an object of props via `v-bind`). It also does not work with direct imports from `#components`.

</warning>

#### `hydrate-on-visible`

Hydrates the component when it becomes visible in the viewport.

```vue [app/pages/index.vue]
<template>
  <div>
    <LazyMyComponent hydrate-on-visible />
  </div>
</template>
```

<read-more to="https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/IntersectionObserver" title="IntersectionObserver options">

Read more about the options for `hydrate-on-visible`.

</read-more>

<note>

Under the hood, this uses Vue's built-in [`hydrateOnVisible` strategy](https://vuejs.org/guide/components/async#hydrate-on-visible).

</note>

#### `hydrate-on-idle`

Hydrates the component when the browser is idle. This is suitable if you need the component to load as soon as possible, but not block the critical rendering path.

You can also pass a number which serves as a max timeout.

```vue [app/pages/index.vue]
<template>
  <div>
    <LazyMyComponent hydrate-on-idle />
  </div>
</template>
```

<note>

Under the hood, this uses Vue's built-in [`hydrateOnIdle` strategy](https://vuejs.org/guide/components/async#hydrate-on-idle).

</note>

#### `hydrate-on-interaction`

Hydrates the component after a specified interaction (e.g., click, mouseover).

```vue [app/pages/index.vue]
<template>
  <div>
    <LazyMyComponent hydrate-on-interaction="mouseover" />
  </div>
</template>
```

If you do not pass an event or list of events, it defaults to hydrating on `pointerenter`, `click` and `focus`.

<note>

Under the hood, this uses Vue's built-in [`hydrateOnInteraction` strategy](https://vuejs.org/guide/components/async#hydrate-on-interaction).

</note>

#### `hydrate-on-media-query`

Hydrates the component when the window matches a media query.

```vue [app/pages/index.vue]
<template>
  <div>
    <LazyMyComponent hydrate-on-media-query="(max-width: 768px)" />
  </div>
</template>
```

<note>

Under the hood, this uses Vue's built-in [`hydrateOnMediaQuery` strategy](https://vuejs.org/guide/components/async#hydrate-on-media-query).

</note>

#### `hydrate-after`

Hydrates the component after a specified delay (in milliseconds).

```vue [app/pages/index.vue]
<template>
  <div>
    <LazyMyComponent :hydrate-after="2000" />
  </div>
</template>
```

#### `hydrate-when`

Hydrates the component based on a boolean condition.

```vue [app/pages/index.vue]
<template>
  <div>
    <LazyMyComponent :hydrate-when="isReady" />
  </div>
</template>

<script setup lang="ts">
const isReady = ref(false)
function myFunction () {
  // trigger custom hydration strategy...
  isReady.value = true
}
</script>
```

#### `hydrate-never`

Never hydrates the component.

```vue [app/pages/index.vue]
<template>
  <div>
    <LazyMyComponent hydrate-never />
  </div>
</template>
```

### Listening to Hydration Events

All delayed hydration components emit a `@hydrated` event when they are hydrated.

```vue [app/pages/index.vue]
<template>
  <div>
    <LazyMyComponent
      hydrate-on-visible
      @hydrated="onHydrate"
    />
  </div>
</template>

<script setup lang="ts">
function onHydrate () {
  console.log('Component has been hydrated!')
}
</script>
```

### Caveats and Best Practices

Delayed hydration can offer performance benefits, but it's essential to use it correctly:

1. **Prioritize In-Viewport Content:** Avoid delayed hydration for critical, above-the-fold content. It's best suited for content that isn't immediately needed.
2. **Conditional Rendering:** When using `v-if="false"` on a lazy component, you might not need delayed hydration. You can just use a normal lazy component.
3. **Shared State:** Be mindful of shared state (`v-model`) across multiple components. Updating the model in one component can trigger hydration in all components bound to that model.
4. **Use Each Strategy's Intended Use Case:** Each strategy is optimized for a specific purpose.
  - `hydrate-when` is best for components that might not always need to be hydrated.
  - `hydrate-after` is for components that can wait a specific amount of time.
  - `hydrate-on-idle` is for components that can be hydrated when the browser is idle.
5. **Avoid hydrate-never on interactive components:** If a component requires user interaction, it should not be set to never hydrate.

## Direct Imports

You can also explicitly import components from `#components` if you want or need to bypass Nuxt's auto-importing functionality.

```vue [app/pages/index.vue]
<script setup lang="ts">
import { LazyMountainsList, NuxtLink } from '#components'

const show = ref(false)
</script>

<template>
  <div>
    <h1>Mountains</h1>
    <LazyMountainsList v-if="show" />
    <button
      v-if="!show"
      @click="show = true"
    >
      Show List
    </button>
    <NuxtLink to="/">Home</NuxtLink>
  </div>
</template>
```

## Custom Directories

By default, only the `~/components` directory is scanned. If you want to add other directories, or change how the components are scanned within a subfolder of this directory, you can add additional directories to the configuration:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  components: [
    // ~/calendar-module/components/event/Update.vue => <EventUpdate />
    { path: '~/calendar-module/components' },

    // ~/user-module/components/account/UserDeleteDialog.vue => <UserDeleteDialog />
    { path: '~/user-module/components', pathPrefix: false },

    // ~/components/special-components/Btn.vue => <SpecialBtn />
    { path: '~/components/special-components', prefix: 'Special' },

    // It's important that this comes last if you have overrides you wish to apply
    // to sub-directories of `~/components`.
    //
    // ~/components/Btn.vue => <Btn />
    // ~/components/base/Btn.vue => <BaseBtn />
    '~/components',
  ],
})
```

<note>

Any nested directories need to be added first as they are scanned in order.

</note>

## npm Packages

If you want to auto-import components from an npm package, you can use [`addComponent`](/docs/4.x/api/kit/components#addcomponent) in a [local module](/docs/4.x/directory-structure/modules) to register them.

<code-group>

```ts [~/modules/register-component.ts]twoslash
import { addComponent, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    // import { MyComponent as MyAutoImportedComponent } from 'my-npm-package'
    addComponent({
      name: 'MyAutoImportedComponent',
      export: 'MyComponent',
      filePath: 'my-npm-package',
    })
  },
})
```

```vue [app/app.vue]
<template>
  <div>
    <!--  the component uses the name we specified and is auto-imported  -->
    <MyAutoImportedComponent />
  </div>
</template>
```

</code-group>

## Component Extensions

By default, any file with an extension specified in the [extensions key of `nuxt.config.ts`](/docs/4.x/api/nuxt-config#extensions) is treated as a component.
If you need to restrict the file extensions that should be registered as components, you can use the extended form of the components directory declaration and its `extensions` key:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  components: [
    {
      path: '~/components',
      extensions: ['.vue'], // [!code ++]
    },
  ],
})
```

## Client Components

If a component is meant to be rendered only client-side, you can add the `.client` suffix to your component.

```bash [Directory Structure]
| components/
--| Comments.client.vue
```

```vue [app/pages/example.vue]
<template>
  <div>
    <!-- this component will only be rendered on client side -->
    <Comments />
  </div>
</template>
```

<note>

This feature only works with Nuxt auto-imports and `#components` imports. Explicitly importing these components from their real paths does not convert them into client-only components.

</note>

<important>

`.client` components are rendered only after being mounted. To access the rendered template using `onMounted()`, add `await nextTick()` in the callback of the `onMounted()` hook.

</important>

<read-more to="/docs/4.x/api/components/client-only">

You can also achieve a similar result with the `<ClientOnly>` component.

</read-more>

## Server Components

Server components allow server-rendering individual components within your client-side apps. It's possible to use server components within Nuxt, even if you are generating a static site. That makes it possible to build complex sites that mix dynamic components, server-rendered HTML and even static chunks of markup.

Server components can either be used on their own or paired with a [client component](/docs/4.x/directory-structure/app/components#paired-with-a-client-component).

<video-accordion title="Watch Learn Vue video about Nuxt Server Components" video-id="u1yyXe86xJM">



</video-accordion>

<tip icon="i-lucide-newspaper" target="_blank" to="https://roe.dev/blog/nuxt-server-components">

Read Daniel Roe's guide to Nuxt Server Components.

</tip>

### Standalone server components

Standalone server components will always be rendered on the server, also known as Islands components.

When their props update, this will result in a network request that will update the rendered HTML in-place.

Server components are currently experimental and in order to use them, you need to enable the 'component islands' feature in your nuxt.config:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  experimental: {
    componentIslands: true,
  },
})
```

Now you can register server-only components with the `.server` suffix and use them anywhere in your application automatically.

```bash [Directory Structure]
-| components/
---| HighlightedMarkdown.server.vue
```

```vue [app/pages/example.vue]
<template>
  <div>
    <!--
      this will automatically be rendered on the server, meaning your markdown parsing + highlighting
      libraries are not included in your client bundle.
     -->
    <HighlightedMarkdown markdown="# Headline" />
  </div>
</template>
```

Server-only components use [`<NuxtIsland>`](/docs/4.x/api/components/nuxt-island) under the hood, meaning that `lazy` prop and `#fallback` slot are both passed down to it.

<warning>

Server components (and islands) must have a single root element. (HTML comments are considered elements as well.)

</warning>

<warning>

Props are passed to server components via URL query parameters, and are therefore limited by the possible length of a URL, so be careful not to pass enormous amounts of data to server components via props.

</warning>

<warning>

Be careful when nesting islands within other islands as each island adds some extra overhead.

</warning>

<warning>

Most features for server-only components and island components, such as slots and client components, are only available for single file components.

</warning>

#### Client components within server components

<note>

This feature needs `experimental.componentIslands.selectiveClient` within your configuration to be true.

</note>

You can partially hydrate a component by setting a `nuxt-client` attribute on the component you wish to be loaded client-side.

```vue [app/components/ServerWithClient.vue]
<template>
  <div>
    <HighlightedMarkdown markdown="# Headline" />
    <!-- Counter will be loaded and hydrated client-side -->
    <Counter
      nuxt-client
      :count="5"
    />
  </div>
</template>
```

<note>

This only works within a server component. Slots for client components are working only with `experimental.componentIsland.selectiveClient` set to `'deep'` and since they are rendered server-side, they are not interactive once client-side.

</note>

#### Server Component Context

When rendering a server-only or island component, `<NuxtIsland>` makes a fetch request which comes back with a `NuxtIslandResponse`. (This is an internal request if rendered on the server, or a request that you can see in the network tab if it's rendering on client-side navigation.)

This means:

- A new Vue app will be created server-side to create the `NuxtIslandResponse`.
- A new 'island context' will be created while rendering the component.
- You can't access the 'island context' from the rest of your app and you can't access the context of the rest of your app from the island component. In other words, the server component or island is *isolated* from the rest of your app.
- Your plugins will run again when rendering the island, unless they have `env: { islands: false }` set (which you can do in an object-syntax plugin).

<important>

Route middleware does not run when rendering island components. Middleware is a routing concept that applies to pages, not components, and is not designed to control component rendering.

</important>

<important>

`useRoute()` and other `vue-router` composables do not track the current page route inside a server (island) component. The island is rendered in its own isolated Vue app keyed only on its props (and any explicit context), which is what keeps islands cacheable independently of the page they are rendered on. Inside an island, `useRoute()` will reflect the island's own request, not the page the user is on.

If an island needs information about the current route, pass it in explicitly — either as props from the parent component, or via the `context` prop on `<NuxtIsland>` (read inside the island from `nuxtApp.ssrContext.islandContext`).

</important>

Within an island component, you can access its island context through `nuxtApp.ssrContext.islandContext`. Note that while island components are still marked as experimental, the format of this context may change.

<note>

Slots can be interactive and are wrapped within a `<div>` with `display: contents;`

</note>

### Paired with a Client component

In this case, the `.server` + `.client` components are two 'halves' of a component and can be used in advanced use cases for separate implementations of a component on server and client side.

```bash [Directory Structure]
-| components/
---| Comments.client.vue
---| Comments.server.vue
```

```vue [app/pages/example.vue]
<template>
  <div>
    <!-- this component will render Comments.server on the server then Comments.client once mounted in the browser -->
    <Comments />
  </div>
</template>
```

## Built-In Nuxt Components

There are a number of components that Nuxt provides, including `<ClientOnly>` and `<DevOnly>`. You can read more about them in the API documentation.

<read-more to="/docs/4.x/api">



</read-more>

## Library Authors

Making Vue component libraries with automatic tree-shaking and component registration is super easy. ✨

You can use the [`addComponentsDir`](/docs/4.x/api/kit/components#addcomponentsdir) method provided from the `@nuxt/kit` to register your components directory in your Nuxt module.

Imagine a directory structure like this:

```bash [Directory Structure]
-| node_modules/
---| awesome-ui/
-----| components/
-------| Alert.vue
-------| Button.vue
-----| nuxt.ts
-| pages/
---| index.vue
-| nuxt.config.ts
```

Then in `awesome-ui/nuxt.ts` you can use the `addComponentsDir` hook:

```tstwoslash
import { addComponentsDir, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    const resolver = createResolver(import.meta.url)

    // Add ./components dir to the list
    addComponentsDir({
      path: resolver.resolve('./components'),
      prefix: 'awesome',
    })
  },
})
```

That's it! Now in your project, you can import your UI library as a Nuxt module in your `nuxt.config` file:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  modules: ['awesome-ui/nuxt'],
})
```

... and directly use the module components (prefixed with `awesome-`) in our `app/pages/index.vue`:

```vue
<template>
  <div>
    My <AwesomeButton>UI button</AwesomeButton>!
    <awesome-alert>Here's an alert!</awesome-alert>
  </div>
</template>
```

It will automatically import the components only if used and also support HMR when updating your components in `node_modules/awesome-ui/components/`.

<link-example to="/docs/4.x/examples/features/auto-imports">



</link-example>

## Composables

# composables

> Use the composables/ directory to auto-import your Vue composables into your application.

## Usage

**Method 1:** Using named export

```ts [app/composables/useFoo.ts]
export const useFoo = () => {
  return useState('foo', () => 'bar')
}
```

**Method 2:** Using default export

```ts [app/composables/use-foo.ts or composables/useFoo.ts]
// It will be available as useFoo() (camelCase of file name without extension)
export default function () {
  return useState('foo', () => 'bar')
}
```

**Usage:** You can now use auto imported composable in `.js`, `.ts` and `.vue` files

```vue [app/app.vue]
<script setup lang="ts">
const foo = useFoo()
</script>

<template>
  <div>
    {{ foo }}
  </div>
</template>
```

<note>

The `app/composables/` directory in Nuxt does not provide any additional reactivity capabilities to your code. Instead, any reactivity within composables is achieved using Vue's Composition API mechanisms, such as ref and reactive. Note that reactive code is also not limited to the boundaries of the `app/composables/` directory. You are free to employ reactivity features wherever they're needed in your application.

</note>

<read-more to="/docs/4.x/guide/concepts/auto-imports">



</read-more>

<link-example to="/docs/4.x/examples/features/auto-imports">



</link-example>

## Types

Under the hood, Nuxt auto generates the file `.nuxt/imports.d.ts` to declare the types.

Be aware that you have to run [`nuxt prepare`](/docs/4.x/api/commands/prepare), [`nuxt dev`](/docs/4.x/api/commands/dev) or [`nuxt build`](/docs/4.x/api/commands/build) in order to let Nuxt generate the types.

<note>

If you create a composable without having the dev server running, TypeScript will throw an error, such as `Cannot find name 'useBar'.`

</note>

## Examples

### Nested Composables

You can use a composable within another composable using auto imports:

```ts [app/composables/test.ts]
export const useFoo = () => {
  const nuxtApp = useNuxtApp()
  const bar = useBar()
}
```

### Access plugin injections

You can access [plugin injections](/docs/4.x/directory-structure/app/plugins#providing-helpers) from composables:

```ts [app/composables/test.ts]
export const useHello = () => {
  const nuxtApp = useNuxtApp()
  return nuxtApp.$hello
}
```

## How Files Are Scanned

Nuxt only scans files at the top level of the [`app/composables/` directory](/docs/4.x/directory-structure/app/composables), e.g.:

```bash [Directory Structure]
-| composables/
---| index.ts     // scanned
---| useFoo.ts    // scanned
---| nested/
-----| utils.ts   // not scanned
```

Only `app/composables/index.ts` and `app/composables/useFoo.ts` would be searched for imports.

To get auto imports working for nested modules, you could either re-export them (recommended) or configure the scanner to include nested directories:

**Example:** Re-export the composables you need from the `app/composables/index.ts` file:

```ts [app/composables/index.ts]
// Enables auto import for this export
export { utils } from './nested/utils.ts'
```

**Example:** Scan nested directories inside the `app/composables/` folder:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  imports: {
    dirs: [
      // Scan top-level composables
      '~/composables',
      // ... or scan composables nested one level deep with a specific name and file extension
      '~/composables/*/index.{ts,js,mjs,mts}',
      // ... or scan all composables within given directory
      '~/composables/**',
    ],
  },
})
```

## Layouts

# layouts

> Nuxt provides a layouts framework to extract common UI patterns into reusable layouts.

<tip icon="i-lucide-rocket">

For best performance, components placed in this directory will be automatically loaded via asynchronous import when used.

</tip>

## Enable Layouts

Layouts are enabled by adding [`<NuxtLayout>`](/docs/4.x/api/components/nuxt-layout) to your [`app.vue`](/docs/4.x/directory-structure/app/app):

```vue [app/app.vue]
<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
```

To use a layout:

- Set a `layout` property in your page with [definePageMeta](/docs/4.x/api/utils/define-page-meta).
- Set the `name` prop of `<NuxtLayout>`.
- Set the `appLayout` property in route rules.

<note>

The layout name is normalized to kebab-case, so `someLayout` becomes `some-layout`.

</note>

<note>

If no layout is specified, `app/layouts/default.vue` will be used.

</note>

<important>

If you only have a single layout in your application, we recommend using [`app.vue`](/docs/4.x/directory-structure/app/app) instead.

</important>

<important>

Unlike other components, your layouts must have a single root element to allow Nuxt to apply transitions between layout changes - and this root element cannot be a `<slot />`.

</important>

## Default Layout

Add a `~/layouts/default.vue`:

```vue [app/layouts/default.vue]
<template>
  <div>
    <p>Some default layout content shared across all pages</p>
    <slot />
  </div>
</template>
```

In a layout file, the content of the page will be displayed in the `<slot />` component.

## Named Layout

```bash [Directory Structure]
-| layouts/
---| default.vue
---| custom.vue
```

Then you can use the `custom` layout in your page:

```vue [pages/about.vue]twoslash
<script setup lang="ts">
declare module 'nuxt/app' {
  interface NuxtLayouts {
    'custom': unknown
  }
}
// ---cut---
definePageMeta({
  layout: 'custom',
})
</script>
```

<read-more to="/docs/4.x/directory-structure/app/pages#page-metadata">

Learn more about `definePageMeta`.

</read-more>

You can directly override the default layout for all pages using the `name` property of [`<NuxtLayout>`](/docs/4.x/api/components/nuxt-layout):

```vue [app/app.vue]
<script setup lang="ts">
// You might choose this based on an API call or logged-in status
const layout = 'custom'
</script>

<template>
  <NuxtLayout :name="layout">
    <NuxtPage />
  </NuxtLayout>
</template>
```

If you have a layout in nested directories, the layout's name will be based on its own path directory and filename, with duplicate segments being removed.

<table>
<thead>
  <tr>
    <th>
      File
    </th>
    
    <th>
      Layout Name
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        ~/layouts/desktop/default.vue
      </code>
    </td>
    
    <td>
      <code>
        desktop-default
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ~/layouts/desktop-base/base.vue
      </code>
    </td>
    
    <td>
      <code>
        desktop-base
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ~/layouts/desktop/index.vue
      </code>
    </td>
    
    <td>
      <code>
        desktop
      </code>
    </td>
  </tr>
</tbody>
</table>

For clarity, we recommend that the layout's filename matches its name:

<table>
<thead>
  <tr>
    <th>
      File
    </th>
    
    <th>
      Layout Name
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        ~/layouts/desktop/DesktopDefault.vue
      </code>
    </td>
    
    <td>
      <code>
        desktop-default
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ~/layouts/desktop-base/DesktopBase.vue
      </code>
    </td>
    
    <td>
      <code>
        desktop-base
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ~/layouts/desktop/Desktop.vue
      </code>
    </td>
    
    <td>
      <code>
        desktop
      </code>
    </td>
  </tr>
</tbody>
</table>

<link-example to="/docs/4.x/examples/features/layouts">



</link-example>

## Changing the Layout Dynamically

You can also use the [`setPageLayout`](/docs/4.x/api/utils/set-page-layout) helper to change the layout dynamically:

```vue [app/pages/index.vue]twoslash
<script setup lang="ts">
declare module 'nuxt/app' {
  interface NuxtLayouts {
    'custom': unknown
  }
}
// ---cut---
function enableCustomLayout () {
  setPageLayout('custom')
}
definePageMeta({
  layout: false,
})
</script>

<template>
  <div>
    <button @click="enableCustomLayout">
      Update layout
    </button>
  </div>
</template>
```

You can also set layouts for specific routes using the `appLayout` property in route rules:

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  routeRules: {
    // Set layout for specific route
    '/admin': { appLayout: 'admin' },
    // Set layout for multiple routes
    '/dashboard/**': { appLayout: 'dashboard' },
    // Disable layout for a route
    '/landing': { appLayout: false },
  },
})
```

<tip>

This is useful when you want to manage layouts centrally in your configuration rather than in each page file, or when you need to apply layouts to routes that don't have corresponding page components (such as catchall pages which might match many paths).

</tip>

<link-example to="/docs/4.x/examples/features/layouts">



</link-example>

## Passing Props to Layouts <badge className="align-middle" color="primary">+4.4</badge>

You can pass props to layouts in several ways.

### Via `definePageMeta`

Use the object syntax for the `layout` property to pass props directly from your page:

<code-group>

```vue [app/pages/dashboard.vue]
<script setup lang="ts">
definePageMeta({
  layout: {
    name: 'panel',
    props: {
      sidebar: true,
      title: 'Dashboard',
    },
  },
})
</script>
```

```vue [app/layouts/panel.vue]
<script setup lang="ts">
const props = defineProps<{
  sidebar?: boolean
  title?: string
}>()
</script>

<template>
  <div>
    <aside v-if="sidebar">
      Sidebar
    </aside>
    <main>
      <h1>{{ title }}</h1>
      <slot />
    </main>
  </div>
</template>
```

</code-group>

<tip>

Props are fully typed based on your layout's `defineProps`. You'll get autocomplete and type-checking in your editor.

</tip>

### Via `setPageLayout`

You can also pass props when changing the layout dynamically with [`setPageLayout`](/docs/4.x/api/utils/set-page-layout):

```ts
setPageLayout('panel', { sidebar: true, title: 'Dashboard' })
```

## Overriding a Layout on a Per-page Basis

If you are using pages, you can take full control by setting `layout: false` and then using the `<NuxtLayout>` component within the page.

<code-group>

```vue [app/pages/index.vue]
<script setup lang="ts">
definePageMeta({
  layout: false,
})
</script>

<template>
  <div>
    <NuxtLayout name="custom">
      <template #header>
        Some header template content.
      </template>

      The rest of the page
    </NuxtLayout>
  </div>
</template>
```

```vue [app/layouts/custom.vue]
<template>
  <div>
    <header>
      <slot name="header">
        Default header content
      </slot>
    </header>
    <main>
      <slot />
    </main>
  </div>
</template>
```

</code-group>

<important>

If you use `<NuxtLayout>` within your pages, make sure it is not the root element (or [disable layout/page transitions](/docs/4.x/getting-started/transitions#disable-transitions)).

</important>

## Middleware

# middleware

> Nuxt provides middleware to run code before navigating to a particular route.

Nuxt provides a customizable **route middleware** framework you can use throughout your application, ideal for extracting code that you want to run before navigating to a particular route.

There are three kinds of route middleware:

1. Anonymous (or inline) route middleware are defined directly within the page.
2. Named route middleware, placed in the `app/middleware/` and automatically loaded via asynchronous import when used on a page.
3. Global route middleware, placed in the `app/middleware/` with a `.global` suffix and is run on every route change.

The first two kinds of route middleware can be defined in [`definePageMeta`](/docs/4.x/api/utils/define-page-meta).

<note>

Name of middleware are normalized to kebab-case: `myMiddleware` becomes `my-middleware`.

</note>

<note>

Route middleware run within the Vue part of your Nuxt app. Despite the similar name, they are completely different from [server middleware](/docs/4.x/directory-structure/server#server-middleware), which are run in the Nitro server part of your app.

</note>

<video-accordion platform="vimeo" title="Watch a video from Vue School on all 3 kinds of middleware" video-id="761471577">



</video-accordion>

## Usage

Route middleware are navigation guards that receive the current route and the next route as arguments.

```ts [middleware/my-middleware.ts]twoslash
export default defineNuxtRouteMiddleware((to, from) => {
  if (to.params.id === '1') {
    return abortNavigation()
  }
  // In a real app you would probably not redirect every route to `/`
  // however it is important to check `to.path` before redirecting or you
  // might get an infinite redirect loop
  if (to.path !== '/') {
    return navigateTo('/')
  }
})
```

Nuxt provides two globally available helpers that can be returned directly from the middleware.

1. [`navigateTo`](/docs/4.x/api/utils/navigate-to) - Redirects to the given route
2. [`abortNavigation`](/docs/4.x/api/utils/abort-navigation) - Aborts the navigation, with an optional error message.

Unlike [navigation guards](https://router.vuejs.org/guide/advanced/navigation-guards#Global-Before-Guards) from `vue-router`, a third `next()` argument is not passed, and **redirect or route cancellation is handled by returning a value from the middleware**.

Possible return values are:

- nothing (a simple `return` or no return at all) - does not block navigation and will move to the next middleware function, if any, or complete the route navigation
- `return navigateTo('/')` - redirects to the given path and will set the redirect code to [`302` Found](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/302) if the redirect happens on the server side
- `return navigateTo('/', { redirectCode: 301 })` - redirects to the given path and will set the redirect code to [`301` Moved Permanently](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/301) if the redirect happens on the server side
- `return abortNavigation()` - stops the current navigation
- `return abortNavigation(error)` - rejects the current navigation with an error

<read-more to="/docs/4.x/api/utils/navigate-to">



</read-more>

<read-more to="/docs/4.x/api/utils/abort-navigation">



</read-more>

<important>

We recommend using the helper functions above for performing redirects or stopping navigation. Other possible return values described in [the vue-router docs](https://router.vuejs.org/guide/advanced/navigation-guards#Global-Before-Guards) may work but there may be breaking changes in future.

</important>

## Middleware Order

Middleware runs in the following order:

1. Global Middleware
2. Page defined middleware order (if there are multiple middleware declared with the array syntax)

For example, assuming you have the following middleware and component:

```bash [app/middleware/ directory]
-| middleware/
---| analytics.global.ts
---| setup.global.ts
---| auth.ts
```

```vue [pages/profile.vue]twoslash
<script setup lang="ts">
definePageMeta({
  middleware: [
    function (to, from) {
      // Custom inline middleware
    },
    'auth',
  ],
})
</script>
```

You can expect the middleware to be run in the following order:

1. `analytics.global.ts`
2. `setup.global.ts`
3. Custom inline middleware
4. `auth.ts`

### Ordering Global Middleware

By default, global middleware is executed alphabetically based on the filename.

However, there may be times you want to define a specific order. For example, in the last scenario, `setup.global.ts` may need to run before `analytics.global.ts`. In that case, we recommend prefixing global middleware with 'alphabetical' numbering.

```bash [Directory structure]
-| middleware/
---| 01.setup.global.ts
---| 02.analytics.global.ts
---| auth.ts
```

<note>

In case you're new to 'alphabetical' numbering, remember that filenames are sorted as strings, not as numeric values. For example, `10.new.global.ts` would come before `2.new.global.ts`. This is why the example prefixes single digit numbers with `0`.

</note>

## When Middleware Runs

If your site is server-rendered or generated, middleware for the initial page will be executed both when the page is rendered and then again on the client. This might be needed if your middleware needs a browser environment, such as if you have a generated site, aggressively cache responses, or want to read a value from local storage.

However, if you want to avoid this behaviour you can do so:

```ts [middleware/example.ts]twoslash
export default defineNuxtRouteMiddleware((to) => {
  // skip middleware on server
  if (import.meta.server) {
    return
  }
  // skip middleware on client side entirely
  if (import.meta.client) {
    return
  }
  // or only skip middleware on initial client load
  const nuxtApp = useNuxtApp()
  if (import.meta.client && nuxtApp.isHydrating && nuxtApp.payload.serverRendered) {
    return
  }
})
```

This is true even if you throw an error in your middleware on the server, and an error page is rendered. The middleware will still run again in the browser.

<note>

Rendering an error page is an entirely separate page load, meaning any registered middleware will run again. You can use [`useError`](/docs/4.x/getting-started/error-handling#useerror) in middleware to check if an error is being handled.

</note>

## Accessing Route in Middleware

Always use the `to` and `from` parameters in your middleware to access the next and previous routes. Avoid using the [`useRoute()`](/docs/4.x/api/composables/use-route) composable in this context altogether.
There is **no concept of a "current route" in middleware**, as middleware can abort a navigation or redirect to a different route. The `useRoute()` composable will always be inaccurate in this context.

<warning>

Sometimes, you might call a composable that uses `useRoute()` internally, which can trigger this warning even if there is no direct call in your middleware.
This leads to the **same issue as above**, so you should structure your functions to accept the route as an argument instead when they are used in middleware.

</warning>

<code-group>

```ts [middleware/access-route.ts]twoslash
// @errors: 2304
export default defineNuxtRouteMiddleware((to) => {
  // passing the route to the function to avoid calling `useRoute()` in middleware
  doSomethingWithRoute(to)

  // ❌ this will output a warning and is NOT recommended
  callsRouteInternally()
})
```

```ts [utils/handle-route.ts]twoslash
// providing the route as an argument so that it can be used in middleware correctly
export function doSomethingWithRoute (route = useRoute()) {
  // ...
}
```

```ts [utils/dont-do-this.ts]twoslash
// ❌ this function is not suitable for use in middleware
export function callsRouteInternally () {
  const route = useRoute()
  // ...
}
```

</code-group>

## Adding Middleware Dynamically

It is possible to add global or named route middleware manually using the [`addRouteMiddleware()`](/docs/4.x/api/utils/add-route-middleware) helper function, such as from within a plugin.

```tstwoslash
export default defineNuxtPlugin(() => {
  addRouteMiddleware('global-test', () => {
    console.log('this global middleware was added in a plugin and will be run on every route change')
  }, { global: true })

  addRouteMiddleware('named-test', () => {
    console.log('this named middleware was added in a plugin and would override any existing middleware of the same name')
  })
})
```

## Example

```bash [Directory Structure]
-| middleware/
---| auth.ts
```

In your page file, you can reference this route middleware:

```vuetwoslash
<script setup lang="ts">
definePageMeta({
  middleware: ['auth'],
  // or middleware: 'auth'
})
</script>
```

Now, before navigation to that page can complete, the `auth` route middleware will be run.

<link-example to="/docs/4.x/examples/routing/middleware">



</link-example>

## Setting Middleware at Build Time

Instead of using `definePageMeta` on each page, you can add named route middleware within the `pages:extend` hook.

```ts [nuxt.config.ts]twoslash
import type { NuxtPage } from 'nuxt/schema'

export default defineNuxtConfig({
  hooks: {
    'pages:extend' (pages) {
      function setMiddleware (pages: NuxtPage[]) {
        for (const page of pages) {
          if (/* some condition */ Math.random() > 0.5) {
            page.meta ||= {}
            // Note that this will override any middleware set in `definePageMeta` in the page
            page.meta.middleware = ['named']
          }
          if (page.children) {
            setMiddleware(page.children)
          }
        }
      }
      setMiddleware(pages)
    },
  },
})
```

## Plugins

# plugins

> Nuxt has a plugins system to use Vue plugins and more at the creation of your Vue application.

Nuxt automatically reads the files in the `app/plugins/` directory and loads them at the creation of the Vue application.

<note>

All plugins inside are auto-registered, you don't need to add them to your `nuxt.config` separately.

</note>

<note>

You can use `.server` or `.client` suffix in the file name to load a plugin only on the server or client side.

</note>

## Registered Plugins

Only files at the top level of the directory (or index files within any subdirectories) will be auto-registered as plugins.

```bash [Directory structure]
-| plugins/
---| foo.ts      // scanned
---| bar/
-----| baz.ts    // not scanned
-----| foz.vue   // not scanned
-----| index.ts  // currently scanned but deprecated
```

Only `foo.ts` and `bar/index.ts` would be registered.

To add plugins in subdirectories, you can use the [`app/plugins`](/docs/4.x/api/nuxt-config#plugins-1) option in `nuxt.config.ts`:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  plugins: [
    '~/plugins/bar/baz',
    '~/plugins/bar/foz',
  ],
})
```

## Creating Plugins

The only argument passed to a plugin is [`nuxtApp`](/docs/4.x/api/composables/use-nuxt-app).

```ts [plugins/hello.ts]twoslash
export default defineNuxtPlugin((nuxtApp) => {
  // Doing something with nuxtApp
})
```

### Object Syntax Plugins

It is also possible to define a plugin using an object syntax, for more advanced use cases. For example:

```ts [plugins/hello.ts]twoslash
export default defineNuxtPlugin({
  name: 'my-plugin',
  enforce: 'pre', // or 'post'
  async setup (nuxtApp) {
    // this is the equivalent of a normal functional plugin
  },
  hooks: {
    // You can directly register Nuxt app runtime hooks here
    'app:created' () {
      const nuxtApp = useNuxtApp()
      // do something in the hook
    },
  },
  env: {
    // Set this value to `false` if you don't want the plugin to run when rendering server-only or island components.
    islands: true,
  },
})
```

<video-accordion title="Watch a video from Alexander Lichter about the Object Syntax for Nuxt plugins" video-id="2aXZyXB1QGQ">



</video-accordion>

<note>

If you are using the object-syntax, the properties are statically analyzed to produce a more optimized build. So you should not define them at runtime. <br />


For example, setting `enforce: import.meta.server ? 'pre' : 'post'` would defeat any future optimization Nuxt is able to do for your plugins.
Nuxt does statically pre-load any hook listeners when using object-syntax, allowing you to define hooks without needing to worry about order of plugin registration.

</note>

## Registration Order

You can control the order in which plugins are registered by prefixing with 'alphabetical' numbering to the file names.

```bash [Directory structure]
plugins/
 | - 01.myPlugin.ts
 | - 02.myOtherPlugin.ts
```

In this example, `02.myOtherPlugin.ts` will be able to access anything that was injected by `01.myPlugin.ts`.

This is useful in situations where you have a plugin that depends on another plugin.

<note>

In case you're new to 'alphabetical' numbering, remember that filenames are sorted as strings, not as numeric values. For example, `10.myPlugin.ts` would come before `2.myOtherPlugin.ts`. This is why the example prefixes single digit numbers with `0`.

</note>

## Loading Strategy

### Parallel Plugins

By default, Nuxt loads plugins sequentially. You can define a plugin as `parallel` so Nuxt won't wait until the end of the plugin's execution before loading the next plugin.

```ts [plugins/my-plugin.ts]twoslash
export default defineNuxtPlugin({
  name: 'my-plugin',
  parallel: true,
  async setup (nuxtApp) {
    // the next plugin will be executed immediately
  },
})
```

### Plugins With Dependencies

If a plugin needs to wait for another plugin before it runs, you can add the plugin's name to the `dependsOn` array.

```ts [plugins/depending-on-my-plugin.ts]twoslash
export default defineNuxtPlugin({
  name: 'depends-on-my-plugin',
  dependsOn: ['my-plugin'],
  async setup (nuxtApp) {
    // this plugin will wait for the end of `my-plugin`'s execution before it runs
  },
})
```

## Using Composables

You can use [composables](/docs/4.x/directory-structure/app/composables) as well as [utils](/docs/4.x/directory-structure/app/utils) within Nuxt plugins:

```ts [app/plugins/hello.ts]
export default defineNuxtPlugin((nuxtApp) => {
  const foo = useFoo()
})
```

However, keep in mind there are some limitations and differences:

<important>

**If a composable depends on another plugin registered later, it might not work.** <br />



Plugins are called in order sequentially and before everything else. You might use a composable that depends on another plugin which has not been called yet.

</important>

<important>

**If a composable depends on the Vue.js lifecycle, it won't work.** <br />



Normally, Vue.js composables are bound to the current component instance while plugins are only bound to [`nuxtApp`](/docs/4.x/api/composables/use-nuxt-app) instance.

</important>

## Providing Helpers

If you would like to provide a helper on the [`NuxtApp`](/docs/4.x/api/composables/use-nuxt-app) instance, return it from the plugin under a `provide` key.

<code-group>

```ts [plugins/hello.ts]twoslash
export default defineNuxtPlugin(() => {
  return {
    provide: {
      hello: (msg: string) => `Hello ${msg}!`,
    },
  }
})
```

```ts [plugins/hello-object-syntax.ts]twoslash
export default defineNuxtPlugin({
  name: 'hello',
  setup () {
    return {
      provide: {
        hello: (msg: string) => `Hello ${msg}!`,
      },
    }
  },
})
```

</code-group>

You can then use the helper in your components:

```vue [app/components/Hello.vue]
<script setup lang="ts">
// alternatively, you can also use it here
const { $hello } = useNuxtApp()
</script>

<template>
  <div>
    {{ $hello('world') }}
  </div>
</template>
```

<important>

Note that we highly recommend using [`composables`](/docs/4.x/directory-structure/app/composables) instead of providing helpers to avoid polluting the global namespace and keep your main bundle entry small.

</important>

<warning>

**If your plugin provides a ref or computed, it will not be unwrapped in a component <template>.** <br />


This is due to how Vue works with refs that aren't top-level to the template. You can read more about it [in the Vue documentation](https://vuejs.org/guide/essentials/reactivity-fundamentals#caveat-when-unwrapping-in-templates).

</warning>

## Typing Plugins

If you return your helpers from the plugin, they will be typed automatically; you'll find them typed for the return of `useNuxtApp()` and within your templates.

<note>

If you need to use a provided helper *within* another plugin, you can call [`useNuxtApp()`](/docs/4.x/api/composables/use-nuxt-app) to get the typed version. But in general, this should be avoided unless you are certain of the plugins' order.

</note>

For advanced use-cases, you can declare the type of injected properties like this:

```ts [index.d.ts]
declare module '#app' {
  interface NuxtApp {
    $hello (msg: string): string
  }
}

declare module 'vue' {
  interface ComponentCustomProperties {
    $hello (msg: string): string
  }
}

export {}
```

## Vue Plugins

If you want to use Vue plugins, like [vue-gtag](https://github.com/MatteoGabriele/vue-gtag) to add Google Analytics tags, you can use a Nuxt plugin to do so.

First, install the Vue plugin dependency:

<code-group sync="pm">

```bash [npm]
npm install --save-dev vue-gtag-next
```

```bash [yarn]
yarn add --dev vue-gtag-next
```

```bash [pnpm]
pnpm add -D vue-gtag-next
```

```bash [bun]
bun add -D vue-gtag-next
```

```bash [deno]
deno add -D npm:vue-gtag-next
```

</code-group>

Then create a plugin file:

```ts [app/plugins/vue-gtag.client.ts]
import VueGtag, { trackRouter } from 'vue-gtag-next'

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.use(VueGtag, {
    property: {
      id: 'GA_MEASUREMENT_ID',
    },
  })
  trackRouter(useRouter())
})
```

## Vue Directives

Similarly, you can register a custom Vue directive in a plugin.

```ts [plugins/my-directive.ts]twoslash
export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.directive('focus', {
    mounted (el) {
      el.focus()
    },
    getSSRProps (binding, vnode) {
      // you can provide SSR-specific props here
      return {}
    },
  })
})
```

<warning>

If you register a Vue directive, you *must* register it on both client and server side unless you are only using it when rendering one side. If the directive only makes sense from a client side, you can always move it to `~/plugins/my-directive.client.ts` and provide a 'stub' directive for the server in `~/plugins/my-directive.server.ts`.

</warning>

<read-more icon="i-simple-icons-vuedotjs" target="_blank" title="Custom Directives on Vue Docs" to="https://vuejs.org/guide/reusability/custom-directives.html">



</read-more>

## Utils

# utils

> Use the utils/ directory to auto-import your utility functions throughout your application.

The main purpose of the [`app/utils/` directory](/docs/4.x/directory-structure/app/utils) is to allow a semantic distinction between your Vue composables and other auto-imported utility functions.

## Usage

**Method 1:** Using named export

```ts [utils/index.ts]twoslash
export const { format: formatNumber } = Intl.NumberFormat('en-GB', {
  notation: 'compact',
  maximumFractionDigits: 1,
})
```

**Method 2:** Using default export

```ts [utils/random-entry.ts or utils/randomEntry.ts]twoslash
// It will be available as randomEntry() (camelCase of file name without extension)
export default function (arr: Array<any>) {
  return arr[Math.floor(Math.random() * arr.length)]
}
```

You can now use auto imported utility functions in `.js`, `.ts` and `.vue` files

```vue [app/app.vue]
<template>
  <p>{{ formatNumber(1234) }}</p>
</template>
```

<read-more to="/docs/4.x/guide/concepts/auto-imports">



</read-more>

<link-example to="/docs/4.x/examples/features/auto-imports">



</link-example>

<tip>

The way `app/utils/` auto-imports work and are scanned is identical to the [`app/composables/`](/docs/4.x/directory-structure/app/composables) directory.

</tip>

<important>

These utils are only available within the Vue part of your app. <br />


Only `server/utils` are auto-imported in the [`server/`](/docs/4.x/directory-structure/server#server-utilities) directory.

</important>

## Assets

# assets

> The assets/ directory is used to add all the website's assets that the build tool will process.

The directory usually contains the following types of files:

- Stylesheets (CSS, SASS, etc.)
- Fonts
- Images that won't be served from the [`public/`](/docs/4.x/directory-structure/public) directory.

If you want to serve assets from the server, we recommend taking a look at the [`public/`](/docs/4.x/directory-structure/public) directory.

<read-more to="/docs/4.x/getting-started/assets">



</read-more>

## App Config

# app.config.ts

> Expose reactive configuration within your application with the App Config file.

Nuxt provides an `app/app.config.ts` config file to expose reactive configuration within your application with the ability to update it at runtime within lifecycle or using a nuxt plugin and editing it with HMR (hot-module-replacement).

You can easily provide runtime app configuration using `app.config.ts` file. It can have either of `.ts`, `.js`, or `.mjs` extensions.

```ts [app/app.config.ts]twoslash
export default defineAppConfig({
  foo: 'bar',
})
```

<caution>

Do not put any secret values inside `app.config` file. It is exposed to the user client bundle.

</caution>

<note>

When configuring a custom [`srcDir`](/docs/4.x/api/nuxt-config#srcdir), make sure to place the `app.config` file at the root of the new `srcDir` path.

</note>

## Usage

To expose config and environment variables to the rest of your app, you will need to define configuration in `app.config` file.

```ts [app/app.config.ts]twoslash
export default defineAppConfig({
  theme: {
    primaryColor: '#ababab',
  },
})
```

We can now universally access `theme` both when server-rendering the page and in the browser using [`useAppConfig`](/docs/4.x/api/composables/use-app-config) composable.

```vue [app/pages/index.vue]
<script setup lang="ts">
const appConfig = useAppConfig()

console.log(appConfig.theme)
</script>
```

The [`updateAppConfig`](/docs/4.x/api/utils/update-app-config) utility can be used to update the `app.config` at runtime.

```vue [app/pages/index.vue]
<script setup>
const appConfig = useAppConfig() // { foo: 'bar' }

const newAppConfig = { foo: 'baz' }

updateAppConfig(newAppConfig)

console.log(appConfig) // { foo: 'baz' }
</script>
```

<read-more to="/docs/4.x/api/utils/update-app-config">

Read more about the `updateAppConfig` utility.

</read-more>

## Typing App Config

Nuxt tries to automatically generate a TypeScript interface from provided app config so you won't have to type it yourself.

However, there are some cases where you might want to type it yourself. There are two possible things you might want to type.

### App Config Input

`AppConfigInput` might be used by module authors who are declaring what valid *input* options are when setting app config. This will not affect the type of `useAppConfig()`.

```ts [index.d.ts]
declare module 'nuxt/schema' {
  interface AppConfigInput {
    /** Theme configuration */
    theme?: {
      /** Primary app color */
      primaryColor?: string
    }
  }
}

// It is always important to ensure you import/export something when augmenting a type
export {}
```

### App Config Output

If you want to type the result of calling [`useAppConfig()`](/docs/4.x/api/composables/use-app-config), then you will want to extend `AppConfig`.

<warning>

Be careful when typing `AppConfig` as you will overwrite the types Nuxt infers from your actually defined app config.

</warning>

```ts [index.d.ts]
declare module 'nuxt/schema' {
  interface AppConfig {
    // This will entirely replace the existing inferred `theme` property
    theme: {
      // You might want to type this value to add more specific types than Nuxt can infer,
      // such as string literal types
      primaryColor?: 'red' | 'blue'
    }
  }
}

// It is always important to ensure you import/export something when augmenting a type
export {}
```

## Merging Strategy

Nuxt uses a custom merging strategy for the `AppConfig` within [the layers](/docs/4.x/getting-started/layers) of your application.

This strategy is implemented using a [Function Merger](https://github.com/unjs/defu#function-merger), which allows defining a custom merging strategy for every key in `app.config` that has an array as value.

<note>

The function merger can only be used in the extended layers and not the main `app.config` in project.

</note>

Here's an example of how you can use:

<code-group>

```ts [layer/app/app.config.ts]twoslash
export default defineAppConfig({
  // Default array value
  array: ['hello'],
})
```

```ts [app/app.config.ts]twoslash
export default defineAppConfig({
  // Overwrite default array value by using a merger function
  array: () => ['bonjour'],
})
```

</code-group>

## Known Limitations

As of Nuxt v3.3, the `app.config.ts` file is shared with Nitro, which results in the following limitations:

1. You cannot import Vue components directly in `app.config.ts`.
2. Some auto-imports are not available in the Nitro context.

These limitations occur because Nitro processes the app config without full Vue component support.

While it's possible to use Vite plugins in the Nitro config as a workaround, this approach is not recommended:

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    vite: {
      plugins: [vue()],
    },
  },
})
```

<warning>

Using this workaround may lead to unexpected behavior and bugs. The Vue plugin is one of many that are not available in the Nitro context.

</warning>

Related issues:

- [Issue #19858](https://github.com/nuxt/nuxt/issues/19858)
- [Issue #19854](https://github.com/nuxt/nuxt/issues/19854)

<note>

Nitro v3 will resolve these limitations by removing support for the app config.
You can track the progress in [this pull request](https://github.com/nitrojs/nitro/pull/2521).

</note>

## Error

# error.vue

> The error.vue file is the error page in your Nuxt application.

During the lifespan of your application, some errors may appear unexpectedly at runtime. In such case, we can use the `error.vue` file to override the default error files and display the error nicely.

```vue [error.vue]
<script setup lang="ts">
import type { NuxtError } from '#app'

const props = defineProps<{ error: NuxtError }>()
</script>

<template>
  <div>
    <h1>{{ error.status }}</h1>
    <NuxtLink to="/">Go back home</NuxtLink>
  </div>
</template>
```

<note>

Although it is called an 'error page' it's not a route and shouldn't be placed in your `~/pages` directory. For the same reason, you shouldn't use `definePageMeta` within this page. That being said, you can still use layouts in the error file, by utilizing the [`NuxtLayout`](/docs/4.x/api/components/nuxt-layout) component and specifying the name of the layout.

</note>

The error page has a single prop - `error` which contains an error for you to handle.

The `error` object provides the following fields:

```ts
interface NuxtError {
  status: number
  fatal: boolean
  unhandled: boolean
  statusText?: string
  data?: unknown
  cause?: unknown
  // legacy/deprecated equivalent of `status`
  statusCode: number
  // legacy/deprecated equivalent of `statusText`
  statusMessage?: string
}
```

If you have an error with custom fields they will be lost; you should assign them to `data` instead:

```ts
throw createError({
  status: 404,
  statusText: 'Page Not Found',
  data: {
    myCustomField: true,
  },
})
```

## Server

# server

> The server/ directory is used to register API and server handlers to your application.

Nuxt automatically scans files inside these directories to register API and server handlers with Hot Module Replacement (HMR) support.

```bash [Directory structure]
-| server/
---| api/
-----| hello.ts      # /api/hello
---| routes/
-----| bonjour.ts    # /bonjour
---| middleware/
-----| log.ts        # log all requests
```

Each file should export a default function defined with `defineEventHandler()` or `eventHandler()` (alias).

The handler can directly return JSON data, a `Promise`, or use `event.node.res.end()` to send a response.

```ts [server/api/hello.ts]twoslash
export default defineEventHandler((event) => {
  return {
    hello: 'world',
  }
})
```

You can now universally call this API in your pages and components:

```vue [app/pages/index.vue]
<script setup lang="ts">
const { data } = await useFetch('/api/hello')
</script>

<template>
  <pre>{{ data }}</pre>
</template>
```

## Server Routes

Files inside the `~~/server/api` are automatically prefixed with `/api` in their route.

<video-accordion platform="vimeo" title="Watch a video from Vue School on API routes" video-id="761468863">



</video-accordion>

To add server routes without `/api` prefix, put them into `~~/server/routes` directory.

**Example:**

```ts [server/routes/hello.ts]
export default defineEventHandler(() => 'Hello World!')
```

Given the example above, the `/hello` route will be accessible at [http://localhost:3000/hello](http://localhost:3000/hello).

<note>

Note that currently server routes do not support the full functionality of dynamic routes as [pages](/docs/4.x/directory-structure/app/pages#dynamic-routes) do.

</note>

## Server Middleware

Nuxt will automatically read in any file in the `~~/server/middleware` to create server middleware for your project.

Middleware handlers will run on every request before any other server route to add or check headers, log requests, or extend the event's request object.

<note>

Middleware handlers should not return anything (nor close or respond to the request) and only inspect or extend the request context or throw an error.

</note>

**Examples:**

```ts [server/middleware/log.ts]
export default defineEventHandler((event) => {
  console.log('New request: ' + getRequestURL(event))
})
```

```ts [server/middleware/auth.ts]
export default defineEventHandler((event) => {
  event.context.auth = { user: 123 }
})
```

## Server Plugins

Nuxt will automatically read any files in the `~~/server/plugins` directory and register them as Nitro plugins. This allows extending Nitro's runtime behavior and hooking into lifecycle events.

**Example:**

```ts [server/plugins/nitroPlugin.ts]
export default defineNitroPlugin((nitroApp) => {
  console.log('Nitro plugin', nitroApp)
})
```

<read-more to="https://nitro.build/guide/plugins" target="_blank" title="Nitro Plugins">



</read-more>

## Server Utilities

Server routes are powered by [h3js/h3](https://github.com/h3js/h3) which comes with a handy set of helpers.

<read-more to="https://www.jsdocs.io/package/h3#package-index-functions" target="_blank" title="Available H3 Request Helpers">



</read-more>

You can add more helpers yourself inside the `~~/server/utils` directory.

For example, you can define a custom handler utility that wraps the original handler and performs additional operations before returning the final response.

**Example:**

```ts [server/utils/handler.ts]
export const defineWrappedResponseHandler = <T extends EventHandlerRequest, D> (
  handler: EventHandler<T, D>,
): EventHandler<T, D> =>
  defineEventHandler<T>(async (event) => {
    try {
      // do something before the route handler
      const response = await handler(event)
      // do something after the route handler
      return { response }
    } catch (err) {
      // Error handling
      return { err }
    }
  })
```

```ts [server/api/hello.get.ts]
export default defineWrappedResponseHandler(event => 'hello world')
```

## Server Alias

You can use the `#server` alias to import files from anywhere within the `server/` directory, regardless of the importing file's location.

```ts [server/api/users/[id]/profile.ts]
// Instead of relative paths like this:
// import { formatUser } from '../../../utils/formatUser'

// Use the #server alias:
import { formatUser } from '#server/utils/formatUser'
```

This alias ensures consistent imports across your server code, especially useful in deeply nested route handlers.

<note>

The `#server` alias can only be used within the `server/` directory. Importing from `#server` in client code will result in an error.

</note>

## Server Types

Auto-imports and other types are different for the `server/` directory, as it is running in a different context from the `app/` directory.

By default, Nuxt 4 generates a [`tsconfig.json`](/docs/4.x/directory-structure/tsconfig) which includes a project reference covering the `server/` folder which ensures accurate typings.

## Recipes

### Route Parameters

Server routes can use dynamic parameters within brackets in the file name like `/api/hello/[name].ts` and be accessed via `event.context.params`.

```ts [server/api/hello/[name].ts]
export default defineEventHandler((event) => {
  const name = getRouterParam(event, 'name')

  return `Hello, ${name}!`
})
```

<tip to="https://h3.dev/examples/validate-data#validate-params">

Alternatively, use `getValidatedRouterParams` with a schema validator such as Zod for runtime and type safety.

</tip>

You can now universally call this API on `/api/hello/nuxt` and get `Hello, nuxt!`.

### Matching HTTP Method

Handle file names can be suffixed with `.get`, `.post`, `.put`, `.delete`, ... to match request's [HTTP Method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods).

```ts [server/api/test.get.ts]
export default defineEventHandler(() => 'Test get handler')
```

```ts [server/api/test.post.ts]
export default defineEventHandler(() => 'Test post handler')
```

Given the example above, fetching `/test` with:

- **GET** method: Returns `Test get handler`
- **POST** method: Returns `Test post handler`
- Any other method: Returns 405 error

You can also use `index.[method].ts` inside a directory for structuring your code differently, this is useful to create API namespaces.

<code-group>

```ts [server/api/foo/index.get.ts]
export default defineEventHandler((event) => {
  // handle GET requests for the `api/foo` endpoint
})
```

```ts [server/api/foo/index.post.ts]
export default defineEventHandler((event) => {
  // handle POST requests for the `api/foo` endpoint
})
```

```ts [server/api/foo/bar.get.ts]
export default defineEventHandler((event) => {
  // handle GET requests for the `api/foo/bar` endpoint
})
```

</code-group>

### Catch-all Route

Catch-all routes are helpful for fallback route handling.

For example, creating a file named `~~/server/api/foo/[...].ts` will register a catch-all route for all requests that do not match any route handler, such as `/api/foo/bar/baz`.

```ts [server/api/foo/[...].ts]
export default defineEventHandler((event) => {
  // event.context.path to get the route path: '/api/foo/bar/baz'
  // event.context.params._ to get the route segment: 'bar/baz'
  return `Default foo handler`
})
```

You can set a name for the catch-all route by using `~~/server/api/foo/[...slug].ts` and access it via `event.context.params.slug`.

```ts [server/api/foo/[...slug].ts]
export default defineEventHandler((event) => {
  // event.context.params.slug to get the route segment: 'bar/baz'
  return `Default foo handler`
})
```

### Body Handling

```ts [server/api/submit.post.ts]
export default defineEventHandler(async (event) => {
  const body = await readBody(event)
  return { body }
})
```

<tip to="https://unjs.io/blog/2023-08-15-h3-towards-the-edge-of-the-web/#runtime-type-safe-request-utils">

Alternatively, use `readValidatedBody` with a schema validator such as Zod for runtime and type safety.

</tip>

You can now universally call this API using:

```vue [app/app.vue]
<script setup lang="ts">
async function submit () {
  const { body } = await $fetch('/api/submit', {
    method: 'post',
    body: { test: 123 },
  })
}
</script>
```

<note>

We are using `submit.post.ts` in the filename only to match requests with `POST` method that can accept the request body. When using `readBody` within a GET request, `readBody` will throw a `405 Method Not Allowed` HTTP error.

</note>

### Query Parameters

Sample query `/api/query?foo=bar&baz=qux`

```ts [server/api/query.get.ts]
export default defineEventHandler((event) => {
  const query = getQuery(event)

  return { a: query.foo, b: query.baz }
})
```

<tip to="https://unjs.io/blog/2023-08-15-h3-towards-the-edge-of-the-web#runtime-type-safe-request-utils">

Alternatively, use `getValidatedQuery` with a schema validator such as Zod for runtime and type safety.

</tip>

### Error Handling

If no errors are thrown, a status code of `200 OK` will be returned.

Any uncaught errors will return a `500 Internal Server Error` HTTP Error.

To return other error codes, throw an exception with [`createError`](/docs/4.x/api/utils/create-error):

```ts [server/api/validation/[id].ts]
export default defineEventHandler((event) => {
  const id = Number.parseInt(event.context.params.id) as number

  if (!Number.isInteger(id)) {
    throw createError({
      status: 400,
      statusText: 'ID should be an integer',
    })
  }
  return 'All good'
})
```

### Status Codes

To return other status codes, use the [`setResponseStatus`](/docs/4.x/api/utils/set-response-status) utility.

For example, to return `202 Accepted`

```ts [server/api/validation/[id].ts]
export default defineEventHandler((event) => {
  setResponseStatus(event, 202)
})
```

### Runtime Config

<code-group>

```ts [server/api/foo.ts]
export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig(event)

  const repo = await $fetch('https://api.github.com/repos/nuxt/nuxt', {
    headers: {
      Authorization: `token ${config.githubToken}`,
    },
  })

  return repo
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  runtimeConfig: {
    githubToken: '',
  },
})
```

```ini [.env]
NUXT_GITHUB_TOKEN='<my-super-token>'
```

</code-group>

<note>

Giving the `event` as argument to `useRuntimeConfig` is optional, but it is recommended to pass it to get the runtime config overwritten by [environment variables](/docs/4.x/guide/going-further/runtime-config#environment-variables) at runtime for server routes.

</note>

### Request Cookies

```ts [server/api/cookies.ts]
export default defineEventHandler((event) => {
  const cookies = parseCookies(event)

  return { cookies }
})
```

### Forwarding Context & Headers

By default, neither the headers from the incoming request nor the request context are forwarded when
making fetch requests in server routes. You can use `event.$fetch` to forward the request context and headers when making fetch requests in server routes.

```ts [server/api/forward.ts]
export default defineEventHandler((event) => {
  return event.$fetch('/api/forwarded')
})
```

<note>

Headers that are **not meant to be forwarded** will **not be included** in the request. These headers include, for example:
`transfer-encoding`, `connection`, `keep-alive`, `upgrade`, `expect`, `host`, `accept`

</note>

### Awaiting Promises After Response

When handling server requests, you might need to perform asynchronous tasks that shouldn't block the response to the client (for example, caching and logging). You can use `event.waitUntil` to await a promise in the background without delaying the response.

The `event.waitUntil` method accepts a promise that will be awaited before the handler terminates, ensuring the task is completed even if the server would otherwise terminate the handler right after the response is sent. This integrates with runtime providers to leverage their native capabilities for handling asynchronous operations after the response is sent.

```ts [server/api/background-task.ts]
const timeConsumingBackgroundTask = async () => {
  await new Promise(resolve => setTimeout(resolve, 1000))
}

export default eventHandler((event) => {
  // schedule a background task without blocking the response
  event.waitUntil(timeConsumingBackgroundTask())

  // immediately send the response to the client
  return 'done'
})
```

## Advanced Usage

### Nitro Config

You can use `nitro` key in `nuxt.config` to directly set [Nitro configuration](https://nitro.build/config).

<warning>

This is an advanced option. Custom config can affect production deployments, as the configuration interface might change over time when Nitro is upgraded in semver-minor versions of Nuxt.

</warning>

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  // https://nitro.build/config
  nitro: {},
})
```

<read-more to="/docs/4.x/guide/concepts/server-engine">



</read-more>

### Nested Router

```ts [server/api/hello/[...slug].ts]
import { createRouter, defineEventHandler, useBase } from 'h3'

const router = createRouter()

router.get('/test', defineEventHandler(() => 'Hello World'))

export default useBase('/api/hello', router.handler)
```

### Sending Streams

<tip>

This is an experimental feature and is available in all environments.

</tip>

```ts [server/api/foo.get.ts]
import fs from 'node:fs'
import { sendStream } from 'h3'

export default defineEventHandler((event) => {
  return sendStream(event, fs.createReadStream('/path/to/file'))
})
```

### Sending Redirect

```ts [server/api/foo.get.ts]
export default defineEventHandler(async (event) => {
  await sendRedirect(event, '/path/redirect/to', 302)
})
```

### Legacy Handler or Middleware

```ts [server/api/legacy.ts]
export default fromNodeMiddleware((req, res) => {
  res.end('Legacy handler')
})
```

<important>

Legacy support is possible using [h3js/h3](https://github.com/h3js/h3), but it is advised to avoid legacy handlers as much as you can.

</important>

```ts [server/middleware/legacy.ts]
export default fromNodeMiddleware((req, res, next) => {
  console.log('Legacy middleware')
  next()
})
```

<warning>

Never combine `next()` callback with a legacy middleware that is `async` or returns a `Promise`.

</warning>

### Server Storage

Nitro provides a cross-platform [storage layer](https://nitro.build/guide/storage). In order to configure additional storage mount points, you can use `nitro.storage`, or [server plugins](/docs/4.x/directory-structure/server#server-plugins).

**Example of adding a Redis storage:**

Using `nitro.storage`:

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  nitro: {
    storage: {
      redis: {
        driver: 'redis',
        /* redis connector options */
        port: 6379, // Redis port
        host: '127.0.0.1', // Redis host
        username: '', // needs Redis >= 6
        password: '',
        db: 0, // Defaults to 0
        tls: {}, // tls/ssl
      },
    },
  },
})
```

Then in your API handler:

```ts [server/api/storage/test.ts]
export default defineEventHandler(async (event) => {
  // List all keys with
  const keys = await useStorage('redis').getKeys()

  // Set a key with
  await useStorage('redis').setItem('foo', 'bar')

  // Remove a key with
  await useStorage('redis').removeItem('foo')

  return {}
})
```

<read-more to="https://nitro.build/guide/storage" target="_blank">

Read more about Nitro Storage Layer.

</read-more>

Alternatively, you can create a storage mount point using a server plugin and runtime config:

<code-group>

```ts [server/plugins/storage.ts]
import redisDriver from 'unstorage/drivers/redis'

export default defineNitroPlugin(() => {
  const storage = useStorage()

  // Dynamically pass in credentials from runtime configuration, or other sources
  const driver = redisDriver({
    base: 'redis',
    host: useRuntimeConfig().redis.host,
    port: useRuntimeConfig().redis.port,
    /* other redis connector options */
  })

  // Mount driver
  storage.mount('redis', driver)
})
```

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  runtimeConfig: {
    redis: { // Default values
      host: '',
      port: 0,
      /* other redis connector options */
    },
  },
})
```

</code-group>

## Content

# content

> Use the content/ directory to create a file-based CMS for your application.

[Nuxt Content](https://content.nuxt.com) reads the `content/` directory in your project and parses `.md`, `.yml`, `.csv` and `.json` files to create a file-based CMS for your application.

- Render your content with built-in components.
- Query your content with a MongoDB-like API.
- Use your Vue components in Markdown files with the MDC syntax.
- Automatically generate your navigation.

<read-more target="_blank" to="https://content.nuxt.com">

Learn more in **Nuxt Content** documentation.

</read-more>

## Enable Nuxt Content

Install the `@nuxt/content` module in your project as well as adding it to your `nuxt.config.ts` with one command:

```bash [Terminal]
npx nuxt module add content
```

## Create Content

Place your markdown files inside the `content/` directory:

```md [content/index.md]
# Hello Content
```

The module automatically loads and parses them.

## Render Content

To render content pages, add a [catch-all route](/docs/4.x/directory-structure/app/pages/#catch-all-route) using the [`<ContentRenderer>`](https://content.nuxt.com/docs/components/content-renderer) component:

```vue [app/pages/[...slug].vue]
<script lang="ts" setup>
const route = useRoute()
const { data: page } = await useAsyncData(route.path, () => {
  return queryCollection('content').path(route.path).first()
})
</script>

<template>
  <div>
    <header><!-- ... --></header>

    <ContentRenderer
      v-if="page"
      :value="page"
    />

    <footer><!-- ... --></footer>
  </div>
</template>
```

## Documentation

<tip icon="i-lucide-book">

Head over to [https://content.nuxt.com](https://content.nuxt.com) to learn more about the Content module features, such as how to build queries and use Vue components in your Markdown files with the MDC syntax.

</tip>

## Layers

# layers

> Use the layers/ directory to organize and auto-register local layers within your application.

The `layers/` directory allows you to organize and share reusable code, components, composables, and configurations across your Nuxt application. Any layers within your project in the `layers/` directory will be automatically registered.

<note>

The `layers/` directory auto-registration is available in Nuxt v3.12.0+.

</note>

<tip icon="i-lucide-lightbulb">

Layers are ideal for organizing large codebases with **Domain-Driven Design (DDD)**, creating reusable **UI libraries** or **themes**, sharing **configuration presets** across projects, and separating concerns like **admin panels** or **feature modules**.

</tip>

## Structure

Each subdirectory within `layers/` is treated as a separate layer. A layer can contain the same structure as a standard Nuxt application.

<important>

Every layer **must have** a `nuxt.config.ts` file to be recognized as a valid layer, even if it's empty.

</important>

```bash [Directory structure]
-| layers/
---| base/
-----| nuxt.config.ts
-----| app/
-------| components/
---------| BaseButton.vue
-------| composables/
---------| useBase.ts
-----| server/
-------| api/
---------| hello.ts
---| admin/
-----| nuxt.config.ts
-----| app/
-------| pages/
---------| admin.vue
-------| layouts/
---------| admin.vue
```

## Automatic Aliases

Named layer aliases to the `srcDir` of each layer are automatically created. You can access a layer using the `#layers/[name]` alias:

```ts
// Access the base layer
import something from '#layers/base/path/to/file'

// Access the admin layer
import { useAdmin } from '#layers/admin/composables/useAdmin'
```

<note>

Named layer aliases were introduced in Nuxt v3.16.0.

</note>

## Layer Content

Each layer can include:

- [`nuxt.config.ts`](/docs/4.x/directory-structure/nuxt-config) - Layer-specific configuration that will be merged with the main config
- [`app.config.ts`](/docs/4.x/directory-structure/app/app-config) - Reactive application configuration
- [`app/components/`](/docs/4.x/directory-structure/app/components) - Vue components (auto-imported)
- [`app/composables/`](/docs/4.x/directory-structure/app/composables) - Vue composables (auto-imported)
- [`app/utils/`](/docs/4.x/directory-structure/app/utils) - Utility functions (auto-imported)
- [`app/pages/`](/docs/4.x/directory-structure/app/pages) - Application pages
- [`app/layouts/`](/docs/4.x/directory-structure/app/layouts) - Application layouts
- [`app/middleware/`](/docs/4.x/directory-structure/app/middleware) - Route middleware
- [`app/plugins/`](/docs/4.x/directory-structure/app/plugins) - Nuxt plugins
- [`server/`](/docs/4.x/directory-structure/server) - Server routes, middleware, and utilities
- [`shared/`](/docs/4.x/directory-structure/shared) - Shared code between app and server

## Priority Order

When multiple layers define the same resource (component, composable, page, etc.), the layer with **higher priority wins**. Layers are sorted alphabetically, with later letters having higher priority (Z > A).

To control the order, prefix directories with numbers: `1.base/`, `2.features/`, `3.admin/`.

<read-more to="/docs/4.x/getting-started/layers#layer-priority">



</read-more>

<video-accordion title="Watch a video from Learn Vue about Nuxt Layers" video-id="lnFCM7c9f7I">



</video-accordion>

## Modules

# modules

> Use the modules/ directory to automatically register local modules within your application.

It is a good place to place any local modules you develop while building your application.

The auto-registered files patterns are:

- `modules/*/index.ts`
- `modules/*.ts`

You don't need to add those local modules to your [`nuxt.config.ts`](/docs/4.x/directory-structure/nuxt-config) separately.

<code-group>

```ts [modules/hello/index.ts]twoslash
// `nuxt/kit` is a helper subpath import you can use when defining local modules
// that means you do not need to add `@nuxt/kit` to your project's dependencies
import { addComponentsDir, addServerHandler, createResolver, defineNuxtModule } from 'nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'hello',
  },
  setup () {
    const resolver = createResolver(import.meta.url)

    // Add an API route
    addServerHandler({
      route: '/api/hello',
      handler: resolver.resolve('./runtime/api-route'),
    })

    // Add components
    addComponentsDir({
      path: resolver.resolve('./runtime/app/components'),
      pathPrefix: true, // Prefix your exports to avoid conflicts with user code or other modules
    })
  },
})
```

```ts [modules/hello/runtime/api-route.ts]twoslash
export default defineEventHandler(() => {
  return { hello: 'world' }
})
```

</code-group>

When starting Nuxt, the `hello` module will be registered and the `/api/hello` route will be available.

<note>

Note that all components, pages, composables and other files that would be normally placed in your `app/` directory need to be in `modules/your-module/runtime/app/`. This ensures they can be type-checked properly.

</note>

Modules are executed in the following sequence:

- First, the modules defined in [`nuxt.config.ts`](/docs/4.x/api/nuxt-config#modules-1) are loaded.
- Then, modules found in the `modules/` directory are executed, and they load in alphabetical order.

You can change the order of local module by adding a number to the front of each directory name:

```bash [Directory structure]
modules/
  1.first-module/
    index.ts
  2.second-module.ts
```

<read-more to="/docs/4.x/guide/modules">



</read-more>

<tip icon="i-lucide-video" target="_blank" to="https://vueschool.io/lessons/creating-your-first-module-from-scratch?friend=nuxt">

Watch Vue School video about Nuxt private modules.

</tip>

## Public

# public

> The public/ directory is used to serve your website's static assets.

Files contained within the `public/` directory are served at the root and are not modified by the build process. This is suitable for files that have to keep their names (e.g. `robots.txt`) *or* likely won't change (e.g. `favicon.ico`).

```bash [Directory structure]
-| public/
---| favicon.ico
---| og-image.png
---| robots.txt
```

```vue [app/app.vue]
<script setup lang="ts">
useSeoMeta({
  ogImage: '/og-image.png',
})
</script>
```

<tip target="_blank" to="https://v2.nuxt.com/docs/directory-structure/static/">

This is known as the <span>

`static/`

</span>

 directory in Nuxt 2.

</tip>

## Shared

# shared

> Use the shared/ directory to share functionality between the Vue app and the Nitro server.

The `shared/` directory allows you to share code that can be used in both the Vue app and the Nitro server.

<note>

The `shared/` directory is available in Nuxt v3.14+.

</note>

<important>

Code in the `shared/` directory cannot import any Vue or Nitro code.

</important>

<video-accordion title="Watch a video from Vue School on sharing utils and types between app and server" video-id="nnAR-MO3q5M">



</video-accordion>

## Usage

**Method 1:** Named export

```ts [shared/utils/capitalize.ts]twoslash
export const capitalize = (input: string) => {
  return input[0] ? input[0].toUpperCase() + input.slice(1) : ''
}
```

**Method 2:** Default export

```ts [shared/utils/capitalize.ts]twoslash
export default function (input: string) {
  return input[0] ? input[0].toUpperCase() + input.slice(1) : ''
}
```

You can now use [auto-imported](/docs/4.x/directory-structure/shared) utilities in your Nuxt app and `server/` directory.

```vue [app/app.vue]
<script setup lang="ts">
const hello = capitalize('hello')
</script>

<template>
  <div>
    {{ hello }}
  </div>
</template>
```

```ts [server/api/hello.get.ts]
export default defineEventHandler((event) => {
  return {
    hello: capitalize('hello'),
  }
})
```

## How Files Are Scanned

Only files in the `shared/utils/` and `shared/types/` directories will be auto-imported. Files nested within subdirectories of these directories will not be auto-imported unless you add these directories to `imports.dirs` and `nitro.imports.dirs`.

<tip>

The way `shared/utils` and `shared/types` auto-imports work and are scanned is identical to the [`app/composables/`](/docs/4.x/directory-structure/app/composables) and [`app/utils/`](/docs/4.x/directory-structure/app/utils) directories.

</tip>

<read-more to="/docs/4.x/directory-structure/app/composables#how-files-are-scanned">



</read-more>

```bash [Directory Structure]
-| shared/
---| capitalize.ts        # Not auto-imported
---| formatters
-----| lower.ts           # Not auto-imported
---| utils/
-----| lower.ts           # Auto-imported
-----| formatters
-------| upper.ts         # Not auto-imported
---| types/
-----| bar.ts             # Auto-imported
```

Any other files you create in the `shared/` folder must be manually imported using the `#shared` alias (automatically configured by Nuxt):

```ts
// For files directly in the shared directory
import capitalize from '#shared/capitalize'

// For files in nested directories
import lower from '#shared/formatters/lower'

// For files nested in a folder within utils
import upper from '#shared/utils/formatters/upper'
```

This alias ensures consistent imports across your application, regardless of the importing file's location.

<read-more to="/docs/4.x/guide/concepts/auto-imports">



</read-more>