# Nuxt - Guide - Concepts


## Rendering

# Rendering Modes

> Learn about the different rendering modes available in Nuxt.

Nuxt supports different rendering modes, [universal rendering](/docs/4.x/guide/concepts/rendering#universal-rendering), [client-side rendering](/docs/4.x/guide/concepts/rendering#client-side-rendering) but also offers [hybrid-rendering](/docs/4.x/guide/concepts/rendering#hybrid-rendering) and the possibility to render your application on [CDN Edge Servers](/docs/4.x/guide/concepts/rendering#edge-side-rendering).

Both the browser and server can interpret JavaScript code to turn Vue.js components into HTML elements. This step is called **rendering**. Nuxt supports both **universal** and **client-side** rendering. The two approaches have benefits and downsides that we will cover.

By default, Nuxt uses **universal rendering** to provide better user experience, performance and to optimize search engine indexing, but you can switch rendering modes in [one line of configuration](/docs/4.x/api/nuxt-config#ssr).

## Universal Rendering

This step is similar to traditional **server-side rendering** performed by PHP or Ruby applications. When the browser requests a URL with universal rendering enabled, Nuxt runs the JavaScript (Vue.js) code in a server environment and returns a fully rendered HTML page to the browser. Nuxt may also return a fully rendered HTML page from a cache if the page was generated in advance. Users immediately get the entirety of the initial content of the application, contrary to client-side rendering.

Once the HTML document has been downloaded, the browser interprets this and Vue.js takes control of the document. The same JavaScript code that once ran on the server runs on the client (browser) **again** in the background now enabling interactivity (hence **Universal rendering**) by binding its listeners to the HTML. This is called **Hydration**. When hydration is complete, the page can enjoy benefits such as dynamic interfaces and page transitions.

Universal rendering allows a Nuxt application to provide quick page load times while preserving the benefits of client-side rendering. Furthermore, as the content is already present in the HTML document, crawlers can index it without overhead.

![Users can access the static content when the HTML document is loaded. Hydration then allows page's interactivity](/assets/docs/concepts/rendering/ssr.svg)

**What's server-rendered and what's client-rendered?**

It is normal to ask which parts of a Vue file runs on the server and/or the client in universal rendering mode.

```vue [app/app.vue]
<script setup lang="ts">
const counter = ref(0) // executes in server and client environments

const handleClick = () => {
  counter.value++ // executes only in a client environment
}
</script>

<template>
  <div>
    <p>Count: {{ counter }}</p>
    <button @click="handleClick">
      Increment
    </button>
  </div>
</template>
```

On the initial request, the `counter` ref is initialized in the server since it is rendered inside the `<p>` tag. The contents of `handleClick` is never executed here. During hydration in the browser, the `counter` ref is re-initialized. The `handleClick` finally binds itself to the button; Therefore it is reasonable to deduce that the body of `handleClick` will always run in a browser environment.

[Middlewares](/docs/4.x/directory-structure/app/middleware) and [pages](/docs/4.x/directory-structure/app/pages) run in the server and on the client during hydration. [Plugins](/docs/4.x/directory-structure/app/plugins) can be rendered on the server or client or both. [Components](/docs/4.x/directory-structure/app/components) can be forced to run on the client only as well. [Composables](/docs/4.x/directory-structure/app/composables) and [utilities](/docs/4.x/directory-structure/app/utils) are rendered based on the context of their usage.

**Benefits of server-side rendering:**

- **Performance**: Users can get immediate access to the page's content because browsers can display static content much faster than JavaScript-generated content. At the same time, Nuxt preserves the interactivity of a web application during the hydration process.
- **Search Engine Optimization**: Universal rendering delivers the entire HTML content of the page to the browser as a classic server application. Web crawlers can directly index the page's content, which makes Universal rendering a great choice for any content that you want to index quickly.

**Downsides of server-side rendering:**

- **Development constraints:** Server and browser environments don't provide the same APIs, and it can be tricky to write code that can run on both sides seamlessly. Fortunately, Nuxt provides guidelines and specific variables to help you determine where a piece of code is executed.
- **Cost:** A server needs to be running in order to render pages on the fly. This adds a monthly cost like any traditional server. However, the server calls are highly reduced thanks to universal rendering with the browser taking over on client-side navigation. A cost reduction is possible by leveraging [edge-side-rendering](/docs/4.x/guide/concepts/rendering#edge-side-rendering).

Universal rendering is very versatile and can fit almost any use case, and is especially appropriate for any content-oriented websites: **blogs, marketing websites, portfolios, e-commerce sites, and marketplaces.**

<tip>

For more examples about writing Vue code without hydration mismatch, see [the Vue docs](https://vuejs.org/guide/scaling-up/ssr#hydration-mismatch).

</tip>

<important>

When importing a library that relies on browser APIs and has side effects, make sure the component importing it is only called client-side. Bundlers do not treeshake imports of modules containing side effects.

</important>

## Client-Side Rendering

Out of the box, a traditional Vue.js application is rendered in the browser (or **client**). Then, Vue.js generates HTML elements after the browser downloads and parses all the JavaScript code containing the instructions to create the current interface.

![Users have to wait for the browser to download, parse and execute the JavaScript before seeing the page's content](/assets/docs/concepts/rendering/csr.svg)

**Benefits of client-side rendering:**

- **Development speed**: When working entirely on the client-side, we don't have to worry about the server compatibility of the code, for example, by using browser-only APIs like the `window` object.
- **Cheaper:** Running a server adds a cost of infrastructure as you would need to run on a platform that supports JavaScript. We can host client-only applications on any static server with HTML, CSS, and JavaScript files.
- **Offline:** Because code entirely runs in the browser, it can nicely keep working while the internet is unavailable.

**Downsides of client-side rendering:**

- **Performance**: The user has to wait for the browser to download, parse and run JavaScript files. Depending on the network for the download part and the user's device for the parsing and execution, this can take some time and impact the user's experience.
- **Search Engine Optimization**: Indexing and updating the content delivered via client-side rendering takes more time than with a server-rendered HTML document. This is related to the performance drawback we discussed, as search engine crawlers won't wait for the interface to be fully rendered on their first try to index the page. Your content will take more time to show and update in search results pages with pure client-side rendering.

Client-side rendering is a good choice for heavily interactive **web applications** that don't need indexing or whose users visit frequently. It can leverage browser caching to skip the download phase on subsequent visits, such as **SaaS, back-office applications, or online games**.

You can enable client-side only rendering with Nuxt in your `nuxt.config.ts`:

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  ssr: false,
})
```

<note>

If you do use `ssr: false`, you should also place an HTML file in `~/spa-loading-template.html` with some HTML you would like to use to render a loading screen that will be rendered until your app is hydrated.

<read-more title="SPA Loading Template" to="/docs/4.x/api/configuration/nuxt-config#spaloadingtemplate">



</read-more>
</note>

<video-accordion title="Watch a video from Alexander Lichter about Building a plain SPA with Nuxt" video-id="7Lr0QTP1Ro8">



</video-accordion>

### Deploying a Static Client-Rendered App

If you deploy your app to [static hosting](/docs/4.x/getting-started/deployment#static-hosting) with the `nuxt generate` or `nuxt build --prerender` commands, then by default, Nuxt will render every page as a separate static HTML file.

<warning>

If you prerender your app with the `nuxt generate` or `nuxt build --prerender` commands, then you will not be able to use any server endpoints as no server will be included in your output folder. If you need server functionality, use `nuxt build` instead.

</warning>

If you are using purely client-side rendering, then this might be unnecessary. You might only need a single `index.html` file, plus `200.html` and `404.html` fallbacks, which you can tell your static web host to serve up for all requests.

In order to achieve this we can change how the routes are prerendered. Just add this to [your hooks](/docs/4.x/api/advanced/hooks#nuxt-hooks-build-time) in your `nuxt.config.ts`:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  hooks: {
    'prerender:routes' ({ routes }) {
      routes.clear() // Do not generate any routes (except the defaults)
    },
  },
})
```

This will produce three files:

- `index.html`
- `200.html`
- `404.html`

The `200.html` file is intended for static hosts that need a success-status fallback for client-side routing. The `404.html` file is intended for static hosts that serve a not-found page while preserving a 404 status. Which file you should use depends on your hosting provider's fallback or rewrite settings.

#### Skipping Client Fallback Generation

When prerendering a client-rendered app, Nuxt will generate `index.html`, `200.html` and `404.html` files by default. However, if you need to prevent any (or all) of these files from being generated in your build, you can use the `'prerender:generate'` hook from [Nitro](/docs/4.x/getting-started/prerendering#prerendergenerate-nitro-hook).

```ts [nuxt.config.ts]twoslash
// @errors: 2353 7006
export default defineNuxtConfig({
  ssr: false,
  nitro: {
    hooks: {
      'prerender:generate' (route) {
        const routesToSkip = ['/index.html', '/200.html', '/404.html']
        if (routesToSkip.includes(route.route)) {
          route.skip = true
        }
      },
    },
  },
})
```

## Hybrid Rendering

Hybrid rendering allows different caching rules per route using **Route Rules** and decides how the server should respond to a new request on a given URL.

Previously every route/page of a Nuxt application and server must use the same rendering mode, universal or client-side. In various cases, some pages could be generated at build time, while others should be client-side rendered. For example, think of a content website with an admin section. Every content page should be primarily static and generated once, but the admin section requires registration and behaves more like a dynamic application.

Nuxt includes route rules and hybrid rendering support. Using route rules you can define rules for a group of nuxt routes, change rendering mode or assign a cache strategy based on route!

Nuxt server will automatically register corresponding middleware and wrap routes with cache handlers using [Nitro caching layer](https://nitro.build/guide/cache).

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  routeRules: {
    // Homepage pre-rendered at build time
    '/': { prerender: true },
    // Products page generated on demand, revalidates in background, cached until API response changes
    '/products': { swr: true },
    // Product pages generated on demand, revalidates in background, cached for 1 hour (3600 seconds)
    '/products/**': { swr: 3600 },
    // Blog posts page generated on demand, revalidates in background, cached on CDN for 1 hour (3600 seconds)
    '/blog': { isr: 3600 },
    // Blog post page generated on demand once until next deployment, cached on CDN
    '/blog/**': { isr: true },
    // Admin dashboard renders only on client-side
    '/admin/**': { ssr: false },
    // Add cors headers on API routes
    '/api/**': { cors: true },
    // Redirects legacy urls
    '/old-page': { redirect: '/new-page' },
  },
})
```

### Route Rules

The different properties you can use are the following:

- `redirect: string` - Define server-side redirects.
- `ssr: boolean` - Disables server-side rendering of the HTML for sections of your app and make them render only in the browser with `ssr: false`
- `cors: boolean` - Automatically adds cors headers with `cors: true` - you can customize the output by overriding with `headers`
- `headers: object` - Add specific headers to sections of your site - for example, your assets
- `swr: number | boolean` - Add cache headers to the server response and cache it on the server or reverse proxy for a configurable TTL (time to live). The `node-server` preset of Nitro is able to cache the full response. When the TTL expired, the cached response will be sent while the page will be regenerated in the background. If true is used, a `stale-while-revalidate` header is added without a MaxAge.
- `isr: number | boolean` - The behavior is the same as `swr` except that we are able to add the response to the CDN cache on platforms that support this (currently Netlify or Vercel). If `true` is used, the content persists until the next deploy inside the CDN.
- `prerender: boolean` - Prerenders routes at build time and includes them in your build as static assets
- `noScripts: boolean` - Disables rendering of Nuxt scripts and JS resource hints for sections of your site.
- `appMiddleware: string | string[] | Record<string, boolean>` - Allows you to define middleware that should or should not run for page paths within the Vue app part of your application (that is, not your Nitro routes)

<note>

Routes using `isr` or `swr` also generate `_payload.json` files alongside HTML. Client-side navigation loads these cached payloads instead of re-fetching data. Configure dynamic routes like `pages/[...slug].vue` with glob patterns: `'/**': { isr: true }`.

</note>

Whenever possible, route rules will be automatically applied to the deployment platform's native rules for optimal performances (Netlify and Vercel are currently supported).

<important>

Note that Hybrid Rendering is not available when using [`nuxt generate`](/docs/4.x/api/commands/generate).

</important>

**Examples:**

<card-group>
<card :ui="{"icon":{"base":"text-black dark:text-white"}}" icon="i-simple-icons-github" target="_blank" title="Nuxt Vercel ISR" to="https://github.com/danielroe/nuxt-vercel-isr">

Example of a Nuxt application with hybrid rendering deployed on Vercel.

</card>
</card-group>

## Edge-Side Rendering

Edge-Side Rendering (ESR) is a powerful feature introduced in Nuxt that allows the rendering of your Nuxt application closer to your users via edge servers of a Content Delivery Network (CDN). By leveraging ESR, you can ensure improved performance and reduced latency, thereby providing an enhanced user experience.

With ESR, the rendering process is pushed to the 'edge' of the network - the CDN's edge servers. Note that ESR is more a deployment target than an actual rendering mode.

When a request for a page is made, instead of going all the way to the original server, it's intercepted by the nearest edge server. This server generates the HTML for the page and sends it back to the user. This process minimizes the physical distance the data has to travel, **reducing latency and loading the page faster**.

Edge-side rendering is possible thanks to [Nitro](https://nitro.build/), the [server engine](/docs/4.x/guide/concepts/server-engine) that powers Nuxt. It offers cross-platform support for Node.js, Deno, Cloudflare Workers, and more.

The current platforms where you can leverage ESR are:

- [Cloudflare Pages](https://pages.cloudflare.com) with zero configuration using the git integration and the `nuxt build` command
- [Vercel Cloud](https://vercel.com/home) using the `nuxt build` command and `NITRO_PRESET=vercel-edge` environment variable
- [Netlify Edge Functions](https://www.netlify.com/platform/#netlify-edge-functions) using the `nuxt build` command and `NITRO_PRESET=netlify-edge` environment variable

Note that **Hybrid Rendering** can be used when using Edge-Side Rendering with route rules.

## Vuejs Development

# Vue.js Development

> Nuxt uses Vue.js and adds features such as component auto-imports, file-based routing and composables for an SSR-friendly usage.

Nuxt integrates Vue 3, the new major release of Vue that enables new patterns for Nuxt users.

<note>

While an in-depth knowledge of Vue is not required to use Nuxt, we recommend that you read the documentation and go through some of the examples on [vuejs.org](https://vuejs.org).

</note>

Nuxt has always used Vue as a frontend framework.

We chose to build Nuxt on top of Vue for these reasons:

- The reactivity model of Vue, where a change in data automatically triggers a change in the interface.
- The component-based templating, while keeping HTML as the common language of the web, enables intuitive patterns to keep your interface consistent, yet powerful.
- From small projects to large web applications, Vue keeps performing well at scale to ensure that your application keeps delivering value to your users.

## Vue with Nuxt

### Single File Components

[Vue’s single-file components](https://vuejs.org/guide/scaling-up/sfc) (SFC or `*.vue` files) encapsulate the markup (`<template>`), logic (`<script>`) and styling (`<style>`) of a Vue component. Nuxt provides a zero-config experience for SFCs with [Hot Module Replacement](https://vite.dev/guide/features#hot-module-replacement) that offers a seamless developer experience.

### Auto-imports

Every Vue component created in the [`app/components/`](/docs/4.x/directory-structure/app/components) directory of a Nuxt project will be available in your project without having to import it. If a component is not used anywhere, your production’s code will not include it.

<read-more to="/docs/4.x/guide/concepts/auto-imports">



</read-more>

### Vue Router

Most applications need multiple pages and a way to navigate between them. This is called **routing**. Nuxt uses an [`app/pages/`](/docs/4.x/directory-structure/app/pages) directory and naming conventions to directly create routes mapped to your files using the official [Vue Router library](https://router.vuejs.org).

<read-more to="/docs/4.x/getting-started/routing">



</read-more>

<link-example to="/docs/4.x/examples/features/auto-imports">



</link-example>

## Differences with Nuxt 2 / Vue 2

Nuxt 3+ is based on Vue 3. The new major Vue version introduces several changes that Nuxt takes advantage of:

- Better performance
- Composition API
- TypeScript support

### Faster Rendering

The Vue Virtual DOM (VDOM) has been rewritten from the ground up and allows for better rendering performance. On top of that, when working with compiled Single-File Components, the Vue compiler can further optimize them at build time by separating static and dynamic markup.

This results in faster first rendering (component creation) and updates, and less memory usage. In Nuxt 3, it enables faster server-side rendering as well.

### Smaller Bundle

With Vue 3 and Nuxt 3, a focus has been put on bundle size reduction. With version 3, most of Vue’s functionality, including template directives and built-in components, is tree-shakable. Your production bundle will not include them if you don’t use them.

This way, a minimal Vue 3 application can be reduced to 12 kb gzipped.

### Composition API

The only way to provide data and logic to components in Vue 2 was through the Options API, which allows you to return data and methods to a template with pre-defined properties like `data` and `methods`:

```vuetwoslash
<script>
export default {
  data () {
    return {
      count: 0,
    }
  },
  methods: {
    increment () {
      this.count++
    },
  },
}
</script>
```

The [Composition API](https://vuejs.org/guide/extras/composition-api-faq) introduced in Vue 3 is not a replacement of the Options API, but it enables better logic reuse throughout an application, and is a more natural way to group code by concern in complex components.

Used with the `setup` keyword in the `<script>` definition, here is the above component rewritten with Composition API and Nuxt 3’s auto-imported Reactivity APIs:

```vue [components/Counter.vue]twoslash
<script setup lang="ts">
const count = ref(0)
const increment = () => count.value++
</script>
```

The goal of Nuxt is to provide a great developer experience around the Composition API.

- Use auto-imported [Reactivity functions](https://vuejs.org/api/reactivity-core) from Vue and Nuxt [built-in composables](/docs/4.x/api/composables/use-async-data).
- Write your own auto-imported reusable functions in the [`app/composables/` directory](/docs/4.x/directory-structure/app/composables).

### TypeScript Support

Both Vue 3 and Nuxt 3+ are written in TypeScript. A fully typed codebase prevents mistakes and documents APIs usage. This doesn’t mean that you have to write your application in TypeScript to take advantage of it. With Nuxt 3, you can opt-in by renaming your file from `.js` to `.ts` , or add `<script setup lang="ts">` in a component.

<read-more to="/docs/4.x/guide/concepts/typescript">

Read the details about TypeScript in Nuxt

</read-more>

## Nuxt Lifecycle

# Nuxt Lifecycle

> Understanding the lifecycle of Nuxt applications can help you gain deeper insights into how the framework operates, especially for both server-side and client-side rendering.

The goal of this chapter is to provide a high-level overview of the different parts of the framework, their execution order, and how they work together.

## Server lifecycle

On the server, the following steps are executed for every initial request to your application:

<steps>

### Server plugins <badge className="align-middle" color="info">once</badge>

Nuxt is powered by [Nitro](https://nitro.build/), a modern server engine.

When Nitro starts, it initializes and executes the plugins under the [`/server/plugins`](/docs/4.x/directory-structure/server#server-plugins) directory. These plugins can:

- Capture and handle application-wide errors.
- Register hooks that execute when Nitro shuts down.
- Register hooks for request lifecycle events, such as modifying responses.

<callout icon="i-lucide-lightbulb">

Nitro plugins are executed only once when the server starts. In a serverless environment, the server boots on each incoming request, and so do the Nitro plugins. However, they are not awaited.

</callout>

<read-more to="/docs/4.x/directory-structure/server#server-plugins">



</read-more>

### Server middleware

After initializing the Nitro server, middleware under `server/middleware/` is executed for every request. Middleware can be used for tasks such as authentication, logging, or request transformation.

<warning>

Returning a value from middleware will terminate the request and send the returned value as the response. This behavior should generally be avoided to ensure proper request handling!

</warning>

<read-more to="/docs/4.x/directory-structure/server#server-middleware">



</read-more>

### App plugins

The Vue and Nuxt instances are created first. Afterward, Nuxt executes its app plugins. This includes:

- Built-in plugins, such as Vue Router and `unhead`.
- Custom plugins located in the `app/plugins/` directory, including those without a suffix (e.g., `myPlugin.ts`) and those with the `.server` suffix (e.g., `myServerPlugin.server.ts`).

Plugins execute in a specific order and may have dependencies on one another. For more details, including execution order and parallelism, refer to the [Plugins documentation](/docs/4.x/directory-structure/app/plugins).

<callout icon="i-lucide-lightbulb">

After this step, Nuxt calls the [`app:created`](/docs/4.x/api/advanced/hooks#app-hooks-runtime) hook, which can be used to execute additional logic.

</callout>

<read-more to="/docs/4.x/directory-structure/app/plugins">



</read-more>

### Route validation

After initializing plugins and before executing middleware, Nuxt calls the `validate` method if it is defined in the `definePageMeta` function. The `validate` method, which can be synchronous or asynchronous, is often used to validate dynamic route parameters.

- The `validate` function should return `true` if the parameters are valid.
- If validation fails, it should return `false` or an object containing a `status` and/or `statusText` to terminate the request.

For more information, see the [Route Validation documentation](/docs/4.x/getting-started/routing#route-validation).

<read-more to="/docs/4.x/getting-started/routing#route-validation">



</read-more>

### App middleware

Middleware allows you to run code before navigating to a particular route. It is often used for tasks such as authentication, redirection, or logging.

In Nuxt, there are three types of middleware:

- **Global route middleware**
- **Named route middleware**
- **Anonymous (or inline) route middleware**

Nuxt executes all global middleware on the initial page load (both on server and client) and then again before any client-side navigation. Named and anonymous middleware are executed only on the routes specified in the middleware property of the page(route) meta defined in the corresponding page components.

For details about each type and examples, see the [Middleware documentation](/docs/4.x/directory-structure/app/middleware).

Any redirection on the server will result in a `Location:` header being sent to the browser; the browser then makes a fresh request to this new location. All application state will be reset when this happens, unless persisted in a cookie.

<read-more to="/docs/4.x/directory-structure/app/middleware">



</read-more>

### Page and components

Nuxt renders the page and its components and fetches any required data with `useFetch` and `useAsyncData` during this step. Since there are no dynamic updates and no DOM operations occur on the server, Vue lifecycle hooks such as `onBeforeMount`, `onMounted`, and subsequent hooks are **NOT** executed during SSR.

By default, Vue pauses dependency tracking during SSR for better performance.

<callout icon="i-lucide-lightbulb">

There is no reactivity on the server side because Vue SSR renders the app top-down as static HTML, making it impossible to go back and modify content that has already been rendered.

</callout>

<important>

You should avoid code that produces side effects that need cleanup in root scope of `<script setup>`. An example of such side effects is setting up timers with `setInterval`. In client-side only code we may setup a timer and then tear it down in `onBeforeUnmount` or `onUnmounted`. However, because the unmount hooks will never be called during SSR, the timers will stay around forever. To avoid this, move your side-effect code into `onMounted` instead.

</important>

<tip icon="i-lucide-video" target="_blank" to="https://youtu.be/dZSNW07sO-A">

Watch a video from Daniel Roe explaining Server Rendering and Global State.

</tip>

### HTML Output

After all required data is fetched and the components are rendered, Nuxt combines the rendered components with settings from `unhead` to generate a complete HTML document. This HTML, along with the associated data, is then sent back to the client to complete the SSR process.

<callout icon="i-lucide-lightbulb">

After rendering the Vue application to HTML, Nuxt calls the [`app:rendered`](/docs/4.x/api/advanced/hooks#app-hooks-runtime) hook.

</callout>

<callout icon="i-lucide-lightbulb">

Before finalizing and sending the HTML, Nitro will call the [`render:html`](/docs/4.x/api/advanced/hooks#nitro-app-hooks-runtime-server-side) hook. This hook allows you to manipulate the generated HTML, such as injecting additional scripts or modifying meta tags.

</callout>
</steps>

## Client lifecycle

This part of the lifecycle is fully executed in the browser, no matter which Nuxt mode you've chosen.

<steps>

### App plugins

This step is similar to the server-side execution and includes both built-in and custom plugins.

Custom plugins in the `app/plugins/` directory, such as those without a suffix (e.g., `myPlugin.ts`) and with the `.client` suffix (e.g., `myClientPlugin.client.ts`), are executed on the client side.

<callout icon="i-lucide-lightbulb">

After this step, Nuxt calls the [`app:created`](/docs/4.x/api/advanced/hooks#app-hooks-runtime) hook, which can be used to execute additional logic.

</callout>

<read-more to="/docs/4.x/directory-structure/app/plugins">



</read-more>

### Route validation

This step is the same as the server-side execution and includes the `validate` method if defined in the `definePageMeta` function.

### App middleware

Nuxt middleware runs on both the server and the client. If you want certain code to run in specific environments, consider splitting it by using `import.meta.client` for the client and `import.meta.server` for the server.

<read-more to="/docs/4.x/directory-structure/app/middleware#when-middleware-runs">



</read-more>

### Mount Vue app and hydrate

Calling `app.mount('#__nuxt')` mounts the Vue application to the DOM. If the application uses SSR or SSG mode, Vue performs a hydration step to make the client-side application interactive. During hydration, Vue recreates the application (excluding [Server Components](/docs/4.x/directory-structure/app/components#server-components)), matches each component to its corresponding DOM nodes, and attaches DOM event listeners.

To ensure proper hydration, it's important to maintain consistency between the data on the server and the client. For API requests, it is recommended to use `useAsyncData`, `useFetch`, or other SSR-friendly composables. These methods ensure that the data fetched on the server side is reused during hydration, avoiding repeated requests. Any new requests should only be triggered after hydration, preventing hydration errors.

<callout icon="i-lucide-lightbulb">

Before mounting the Vue application, Nuxt calls the [`app:beforeMount`](/docs/4.x/api/advanced/hooks#app-hooks-runtime) hook.

</callout>

<callout icon="i-lucide-lightbulb">

After mounting the Vue application, Nuxt calls the [`app:mounted`](/docs/4.x/api/advanced/hooks#app-hooks-runtime) hook.

</callout>

### Vue lifecycle

Unlike on the server, the browser executes the full [Vue lifecycle](https://vuejs.org/guide/essentials/lifecycle).

</steps>

## Auto Imports

# Auto-imports

> Nuxt auto-imports components, composables, helper functions and Vue APIs.

Nuxt auto-imports components, composables and [Vue.js APIs](https://vuejs.org/api/) to use across your application without explicitly importing them.

```vue [app/app.vue]twoslash
<script setup lang="ts">
const count = ref(1) // ref is auto-imported
</script>
```

Thanks to its opinionated directory structure, Nuxt can auto-import your [`app/components/`](/docs/4.x/directory-structure/app/components), [`app/composables/`](/docs/4.x/directory-structure/app/composables) and [`app/utils/`](/docs/4.x/directory-structure/app/utils).

Contrary to a classic global declaration, Nuxt preserves typings, IDEs completions and hints, and **only includes what is used in your production code**.

<note>

In the docs, every function that is not explicitly imported is auto-imported by Nuxt and can be used as-is in your code. You can find a reference for auto-imported components, composables and utilities in the [API section](/docs/4.x/api).

</note>

<note>

In the [`server`](/docs/4.x/directory-structure/server) directory, Nuxt auto-imports exported functions and variables from `server/utils/`.

</note>

<note>

You can also auto-import functions exported from custom folders or third-party packages by configuring the [`imports`](/docs/4.x/api/nuxt-config#imports) section of your `nuxt.config` file.

</note>

## Built-in Auto-imports

Nuxt auto-imports functions and composables to perform [data fetching](/docs/4.x/getting-started/data-fetching), get access to the [app context](/docs/4.x/api/composables/use-nuxt-app) and [runtime config](/docs/4.x/guide/going-further/runtime-config), manage [state](/docs/4.x/getting-started/state-management) or define components and plugins.

```vuetwoslash
<script setup lang="ts">
/* useFetch() is auto-imported */
const { data, refresh, status } = await useFetch('/api/hello')
</script>
```

Vue exposes Reactivity APIs like `ref` or `computed`, as well as lifecycle hooks and helpers that are auto-imported by Nuxt.

```vuetwoslash
<script setup lang="ts">
/* ref() and computed() are auto-imported */
const count = ref(1)
const double = computed(() => count.value * 2)
</script>
```

### Vue and Nuxt Composables

When you are using the built-in Composition API composables provided by Vue and Nuxt, be aware that many of them rely on being called in the right *context*.

During a component lifecycle, Vue tracks the temporary instance of the current component (and similarly, Nuxt tracks a temporary instance of `nuxtApp`) via a global variable, and then unsets it in the same tick. This is essential when server rendering, both to avoid cross-request state pollution (leaking a shared reference between two users) and to avoid leakage between different components.

That means that (with very few exceptions) you cannot use them outside a Nuxt plugin, Nuxt route middleware or Vue setup function. On top of that, you must use them synchronously - that is, you cannot use `await` before calling a composable, except within `<script setup>` blocks, within the setup function of a component declared with `defineNuxtComponent`, in `defineNuxtPlugin` or in `defineNuxtRouteMiddleware`, where we perform a transform to keep the synchronous context even after the `await`.

If you get an error message like `Nuxt instance is unavailable` then it probably means you are calling a Nuxt composable in the wrong place in the Vue or Nuxt lifecycle.

<video-accordion title="Watch a video from Alexander Lichter about avoiding the 'Nuxt instance is unavailable' error" video-id="ofuKRZLtOdY">



</video-accordion>

<tip>

When using a composable that requires the Nuxt context inside a non-SFC component, you need to wrap your component with `defineNuxtComponent` instead of `defineComponent`

</tip>

<read-more to="/docs/4.x/guide/going-further/experimental-features#asynccontext" icon="i-lucide-star">

Checkout the `asyncContext` experimental feature to use Nuxt composables in async functions.

</read-more>

<read-more to="https://github.com/nuxt/nuxt/issues/14269#issuecomment-1397352832" target="_blank">

See the full explanation in this GitHub comment.

</read-more>

**Example of breaking code:**

```ts [composables/example.ts]twoslash
// trying to access runtime config outside a composable
const config = useRuntimeConfig()

export const useMyComposable = () => {
  // accessing runtime config here
}
```

**Example of working code:**

```ts [composables/example.ts]twoslash
export const useMyComposable = () => {
  // Because your composable is called in the right place in the lifecycle,
  // useRuntimeConfig will work here
  const config = useRuntimeConfig()

  // ...
}
```

## Directory-based Auto-imports

Nuxt directly auto-imports files created in defined directories:

- `app/components/` for [Vue components](/docs/4.x/directory-structure/app/components).
- `app/composables/` for [Vue composables](/docs/4.x/directory-structure/app/composables).
- `app/utils/` for helper functions and other utilities.

<link-example to="/docs/4.x/examples/features/auto-imports">



</link-example>

<warning>

**Auto-imported ref and computed won't be unwrapped in a component <template>.** <br />


This is due to how Vue works with refs that aren't top-level to the template. You can read more about it [in the Vue documentation](https://vuejs.org/guide/essentials/reactivity-fundamentals#caveat-when-unwrapping-in-templates).

</warning>

### Explicit Imports

Nuxt exposes every auto-import with the `#imports` alias that can be used to make the import explicit if needed:

```vue
<script setup lang="ts">
import { computed, ref } from '#imports'

const count = ref(1)
const double = computed(() => count.value * 2)
</script>
```

### Disabling Auto-imports

If you want to disable auto-importing composables and utilities, you can set `imports.autoImport` to `false` in the `nuxt.config` file.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  imports: {
    autoImport: false,
  },
})
```

This will disable auto-imports completely but it's still possible to use [explicit imports](/docs/4.x/guide/concepts/auto-imports#explicit-imports) from `#imports`.

### Partially Disabling Auto-imports

If you want framework-specific functions like `ref` to remain auto-imported but wish to disable auto-imports for your own code (e.g., custom composables), you can set the `imports.scan` option to `false` in your `nuxt.config.ts` file:

```ts
export default defineNuxtConfig({
  imports: {
    scan: false,
  },
})
```

With this configuration:

- Framework functions like `ref`, `computed`, or `watch` will still work without needing manual imports.
- Custom code, such as composables, will need to be manually imported in your files.

<warning>

**Caution:** This setup has certain limitations:

- If you structure your project with layers, you will need to explicitly import the composables from each layer, rather than relying on auto-imports.
- This breaks the layer system’s override feature. If you use `imports.scan: false`, ensure you understand this side-effect and adjust your architecture accordingly.

</warning>

## Auto-imported Components

Nuxt also automatically imports components from your `~/components` directory, although this is configured separately from auto-importing composables and utility functions.

<read-more to="/docs/4.x/directory-structure/app/components">



</read-more>

To disable auto-importing components from your own `~/components` directory, you can set `components.dirs` to an empty array (though note that this will not affect components added by modules).

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  components: {
    dirs: [],
  },
})
```

## Auto-import from Third-Party Packages

Nuxt also allows auto-importing from third-party packages.

<tip>

If you are using the Nuxt module for that package, it is likely that the module has already configured auto-imports for that package.

</tip>

For example, you could enable the auto-import of the `useI18n` composable from the `vue-i18n` package like this:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  imports: {
    presets: [
      {
        from: 'vue-i18n',
        imports: ['useI18n'],
      },
    ],
  },
})
```

<video-accordion title="Watch a video from Alexander Lichter on how to easily set up custom auto imports" video-id="FT2LQJ2NvVI">



</video-accordion>

## Server Engine

# Server Engine

> Nuxt is powered by a new server engine: Nitro.

While building Nuxt, we created a new server engine: [Nitro](https://nitro.build/).

It is shipped with many features:

- Cross-platform support for Node.js, browsers, service workers and more.
- Serverless support out-of-the-box.
- API routes support.
- Automatic code-splitting and async-loaded chunks.
- Hybrid mode for static + serverless sites.
- Development server with hot module reloading.

## API Layer

Server [API endpoints](/docs/4.x/directory-structure/server#server-routes) and [Middleware](/docs/4.x/directory-structure/server#server-middleware) are added by Nitro that internally uses [h3](https://github.com/h3js/h3).

Key features include:

- Handlers can directly return objects/arrays for an automatically-handled JSON response
- Handlers can return promises, which will be awaited (`res.end()` and `next()` are also supported)
- Helper functions for body parsing, cookie handling, redirects, headers and more

Check out [the h3 docs](https://github.com/h3js/h3) for more information.

<read-more to="/docs/4.x/directory-structure/server#server-routes">

Learn more about the API layer in the `server/` directory.

</read-more>

## Direct API Calls

Nitro allows 'direct' calling of routes via the globally-available [`$fetch`](/docs/4.x/api/utils/dollarfetch) helper. This will make an API call to the server if run on the browser, but will directly call the relevant function if run on the server, **saving an additional API call**.

[`$fetch`](/docs/4.x/api/utils/dollarfetch) API is using [ofetch](https://github.com/unjs/ofetch), with key features including:

- Automatic parsing of JSON responses (with access to raw response if needed)
- Request body and params are automatically handled, with correct `Content-Type` headers

For more information on `$fetch` features, check out [ofetch](https://github.com/unjs/ofetch).

## Typed API Routes

When using API routes (or middleware), Nitro will generate typings for these routes as long as you are returning a value instead of using `res.end()` to send a response.

You can access these types when using [`$fetch()`](/docs/4.x/api/utils/dollarfetch) or [`useFetch()`](/docs/4.x/api/composables/use-fetch).

## Standalone Server

Nitro produces a standalone server dist that is independent of `node_modules`.

The server in Nuxt 2 is not standalone and requires part of Nuxt core to be involved by running `nuxt start` (with the [`nuxt-start`](https://www.npmjs.com/package/nuxt-start) or [`nuxt`](https://www.npmjs.com/package/nuxt) distributions) or custom programmatic usage, which is fragile and prone to breakage and not suitable for serverless and service worker environments.

Nuxt generates this dist when running `nuxt build` into a [`.output`](/docs/4.x/directory-structure/output) directory.

The output contains runtime code to run your Nuxt server in any environment (including experimental browser service workers!) and serve your static files, making it a true hybrid framework for the JAMstack. In addition, Nuxt implements a native storage layer, supporting multi-source drivers and local assets.

<read-more to="https://github.com/nitrojs/nitro" icon="i-simple-icons-github" target="_blank">

Read more about Nitro engine on GitHub.

</read-more>

## Modules

# Modules

> Nuxt provides a module system to extend the framework core and simplify integrations.

## Exploring Nuxt Modules

When developing production-grade applications with Nuxt you might find that the framework's core functionality is not enough. Nuxt can be extended with configuration options and plugins, but maintaining these customizations across multiple projects can be tedious, repetitive and time-consuming. On the other hand, supporting every project's needs out of the box would make Nuxt very complex and hard to use.

This is one of the reasons why Nuxt provides a module system that makes it possible to extend the core. Nuxt modules are async functions that sequentially run when starting Nuxt in development mode using [`nuxt dev`](/docs/4.x/api/commands/dev) or building a project for production with [`nuxt build`](/docs/4.x/api/commands/build). They can override templates, configure webpack loaders, add CSS libraries, and perform many other useful tasks.

Best of all, Nuxt modules can be distributed in npm packages. This makes it possible for them to be reused across projects and shared with the community, helping create an ecosystem of high-quality add-ons.

<read-more to="/modules">

Explore Nuxt Modules

</read-more>

## Add Nuxt Modules

Once you have installed the modules you can add them to your [`nuxt.config.ts`](/docs/4.x/directory-structure/nuxt-config) file under the `modules` property. Module developers usually provide additional steps and details for usage.

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  modules: [
    // Using package name (recommended usage)
    '@nuxtjs/example',

    // Load a local module
    './modules/example',

    // Add module with inline-options
    ['./modules/example', { token: '123' }],

    // Inline module definition
    async (inlineOptions, nuxt) => { },
  ],
})
```

<warning>

Nuxt modules are now build-time-only, and the `buildModules` property used in Nuxt 2 is deprecated in favor of `modules`.

</warning>

## Disabling Modules

You can disable a module by setting its config key to `false` in your Nuxt config. This is particularly useful when you want to disable modules inherited from layers.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  // Disable `@nuxt/image` module
  image: false,
})
```

<read-more to="/docs/4.x/guide/going-further/layers#disabling-modules-from-layers">



</read-more>

## Create a Nuxt Module

Everyone has the opportunity to develop modules and we cannot wait to see what you will build.

<read-more to="/docs/4.x/guide/modules" title="Module Author Guide">



</read-more>

## Esm

# ES Modules

> Nuxt uses native ES modules.

This guide helps explain what ES Modules are and how to make a Nuxt app (or upstream library) compatible with ESM.

## Background

### CommonJS Modules

CommonJS (CJS) is a format introduced by Node.js that allows sharing functionality between isolated JavaScript modules ([read more](https://nodejs.org/api/modules.html)).
You might be already familiar with this syntax:

```js
const a = require('./a')

module.exports.a = a
```

Bundlers like webpack and Rollup support this syntax and allow you to use modules written in CommonJS in the browser.

### ESM Syntax

Most of the time, when people talk about ESM vs. CJS, they are talking about a different syntax for writing [modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules).

```js
import a from './a'

export { a }
```

Before ECMAScript Modules (ESM) became a standard (it took more than 10 years!), tooling like
[webpack](https://webpack.js.org/guides/ecma-script-modules/) and even languages like TypeScript started supporting so-called **ESM syntax**.
However, there are some key differences with actual spec; here's [a helpful explainer](https://hacks.mozilla.org/2018/03/es-modules-a-cartoon-deep-dive/).

### What is 'Native' ESM?

You may have been writing your app using ESM syntax for a long time. After all, it's natively supported by the browser, and in Nuxt 2 we compiled all the code you wrote to the appropriate format (CJS for server, ESM for browser).

When adding modules to your package, things were a little different. A sample library might expose both CJS and ESM versions, and let us pick which one we wanted:

```json
{
  "name": "sample-library",
  "main": "dist/sample-library.cjs.js",
  "module": "dist/sample-library.esm.js"
}
```

So in Nuxt 2, the bundler (webpack) would pull in the CJS file ('main') for the server build and use the ESM file ('module') for the client build.

<note>

The `module` field is a convention used by bundlers like webpack and Rollup, but is not recognized by Node.js itself. Node.js only uses the [`exports`](https://nodejs.org/api/packages.html#exports) and [`main`](https://nodejs.org/api/packages.html#main) fields for module resolution.

</note>

However, in recent Node.js LTS releases, it is now possible to [use native ESM module](https://nodejs.org/api/esm.html) within Node.js. That means that Node.js itself can process JavaScript using ESM syntax, although it doesn't do it by default. The two most common ways to enable ESM syntax are:

- set `"type": "module"` within your `package.json` and keep using `.js` extension
- use the `.mjs` file extensions (recommended)

This is what we do for Nuxt Nitro; we output a `.output/server/index.mjs` file. That tells Node.js to treat this file as a native ES module.

### What Are Valid Imports in a Node.js Context?

When you `import` a module rather than `require` it, Node.js resolves it differently. For example, when you import `sample-library`, Node.js will look for the `exports` entry in that library's `package.json`, or fall back to the `main` entry if `exports` is not defined.

This is also true of dynamic imports, like `const b = await import('sample-library')`.

Node supports the following kinds of imports (see [docs](https://nodejs.org/api/packages.html#determining-module-system)):

1. files ending in `.mjs` - these are expected to use ESM syntax
2. files ending in `.cjs` - these are expected to use CJS syntax
3. files ending in `.js` - these are expected to use CJS syntax unless their `package.json` has `"type": "module"`

### What Kinds of Problems Can There Be?

For a long time module authors have been producing ESM-syntax builds but using conventions like `.esm.js` or `.es.js`, which they have added to the `module` field in their `package.json`. This hasn't been a problem until now because they have only been used by bundlers like webpack, which don't especially care about the file extension.

However, if you try to import a package with an `.esm.js` file in a Node.js ESM context, it won't work, and you'll get an error like:

```bash [Terminal]
(node:22145) Warning: To load an ES module, set "type": "module" in the package.json or use the .mjs extension.
/path/to/index.js:1

export default {}
^^^^^^

SyntaxError: Unexpected token 'export'
    at wrapSafe (internal/modules/cjs/loader.js:1001:16)
    at Module._compile (internal/modules/cjs/loader.js:1049:27)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:1114:10)
    ....
    at async Object.loadESM (internal/process/esm_loader.js:68:5)
```

You might also get this error if you have a named import from an ESM-syntax build that Node.js thinks is CJS:

```bash [Terminal]
file:///path/to/index.mjs:5
import { named } from 'sample-library'
         ^^^^^
SyntaxError: Named export 'named' not found. The requested module 'sample-library' is a CommonJS module, which may not support all module.exports as named exports.

CommonJS modules can always be imported via the default export, for example using:

import pkg from 'sample-library';
const { named } = pkg;

    at ModuleJob._instantiate (internal/modules/esm/module_job.js:120:21)
    at async ModuleJob.run (internal/modules/esm/module_job.js:165:5)
    at async Loader.import (internal/modules/esm/loader.js:177:24)
    at async Object.loadESM (internal/process/esm_loader.js:68:5)
```

## Troubleshooting ESM Issues

If you encounter these errors, the issue is almost certainly with the upstream library. They need to [fix their library](/docs/4.x/guide/concepts/esm#library-author-guide) to support being imported by Node.

### Transpiling Libraries

In the meantime, you can tell Nuxt not to try to import these libraries by adding them to `build.transpile`:

```tstwoslash
export default defineNuxtConfig({
  build: {
    transpile: ['sample-library'],
  },
})
```

You may find that you *also* need to add other packages that are being imported by these libraries.

### Aliasing Libraries

In some cases, you may also need to manually alias the library to the CJS version, for example:

```tstwoslash
export default defineNuxtConfig({
  alias: {
    'sample-library': 'sample-library/dist/sample-library.cjs.js',
  },
})
```

### Default Exports

A dependency with CommonJS format, can use `module.exports` or `exports` to provide a default export:

```js [node_modules/cjs-pkg/index.js]
module.exports = { test: 123 }
// or
exports.test = 123
```

This normally works well if we `require` such dependency:

```js [test.cjs]
const pkg = require('cjs-pkg')

console.log(pkg) // { test: 123 }
```

[Node.js in native ESM mode](https://nodejs.org/api/esm.html#interoperability-with-commonjs), [typescript with `esModuleInterop` enabled](https://www.typescriptlang.org/tsconfig/#esModuleInterop) and bundlers such as webpack, provide a compatibility mechanism so that we can default import such library.
This mechanism is often referred to as "interop require default":

```js
import pkg from 'cjs-pkg'

console.log(pkg) // { test: 123 }
```

However, because of the complexities of syntax detection and different bundle formats, there is always a chance that the interop default fails and we end up with something like this:

```js
import pkg from 'cjs-pkg'

console.log(pkg) // { default: { test: 123 } }
```

Also when using dynamic import syntax (in both CJS and ESM files), we always have this situation:

```js
import('cjs-pkg').then(console.log) // [Module: null prototype] { default: { test: '123' } }
```

In this case, we need to manually interop the default export:

```js
// Static import
import { default as pkg } from 'cjs-pkg'

// Dynamic import
import('cjs-pkg').then(m => m.default || m).then(console.log)
```

For handling more complex situations and more safety, we recommend and internally use [mlly](https://github.com/unjs/mlly) in Nuxt that can preserve named exports.

```js
import { interopDefault } from 'mlly'

// Assuming the shape is { default: { foo: 'bar' }, baz: 'qux' }
import myModule from 'my-module'

console.log(interopDefault(myModule)) // { foo: 'bar', baz: 'qux' }
```

## Library Author Guide

The good news is that it's relatively simple to fix issues of ESM compatibility. There are two main options:

1. **You can rename your ESM files to end with .mjs.**<br />

*This is the recommended and simplest approach.* You may have to sort out issues with your library's dependencies and possibly with your build system, but in most cases, this should fix the problem for you. It's also recommended to rename your CJS files to end with `.cjs`, for the greatest explicitness.
2. **You can opt to make your entire library ESM-only**.<br />

This would mean setting `"type": "module"` in your `package.json` and ensuring that your built library uses ESM syntax. However, you may face issues with your dependencies - and this approach means your library can *only* be consumed in an ESM context.

### Migration

The initial step from CJS to ESM is updating any usage of `require` to use `import` instead:

<code-group>

```ts [Before]
module.exports = function () { /* ... */ }

exports.hello = 'world'
```

```ts [After]
export default function () { /* ... */ }

export const hello = 'world'
```

</code-group>

<code-group>

```js [Before]
const myLib = require('my-lib')
```

```js [After]
import myLib from 'my-lib'
// or
const dynamicMyLib = await import('my-lib').then(lib => lib.default || lib)
```

</code-group>

In ESM Modules, unlike CJS, `require`, `require.resolve`, `__filename` and `__dirname` globals are not available
and should be replaced with `import()` and `import.meta.filename`.

<code-group>

```js [Before]
const { join } = require('node:path')

const newDir = join(__dirname, 'new-dir')
```

```js [After]
import { fileURLToPath } from 'node:url'

const newDir = fileURLToPath(new URL('./new-dir', import.meta.url))
```

</code-group>

<code-group>

```js [Before]
const someFile = require.resolve('./lib/foo.js')
```

```js [After]
import { resolvePath } from 'mlly'

const someFile = await resolvePath('my-lib', { url: import.meta.url })
```

</code-group>

### Best Practices

- Prefer named exports rather than default export. This helps reduce CJS conflicts. (see [Default exports](/docs/4.x/guide/concepts/esm#default-exports) section)
- Avoid depending on Node.js built-ins and CommonJS or Node.js-only dependencies as much as possible to make your library usable in Browsers and Edge Workers without needing Nitro polyfills.
- Use new `exports` field with conditional exports. ([read more](https://nodejs.org/api/packages.html#conditional-exports)).

```json
{
  "exports": {
    ".": {
      "import": "./dist/mymodule.mjs"
    }
  }
}
```

## Typescript

# TypeScript

> Nuxt is fully typed and provides helpful shortcuts to ensure you have access to accurate type information when you are coding.

## Type-checking

By default, Nuxt doesn't check types when you run [`nuxt dev`](/docs/4.x/api/commands/dev) or [`nuxt build`](/docs/4.x/api/commands/build), for performance reasons.

To enable type-checking at build or development time, install `vue-tsc` and `typescript` as development dependency:

<code-group sync="pm">

```bash [npm]
npm install --save-dev vue-tsc typescript
```

```bash [yarn]
yarn add --dev vue-tsc typescript
```

```bash [pnpm]
pnpm add -D vue-tsc typescript
```

```bash [bun]
bun add -D vue-tsc typescript
```

```bash [deno]
deno add -D npm:vue-tsc npm:typescript
```

</code-group>

Then, run [`nuxt typecheck`](/docs/4.x/api/commands/typecheck) command to check your types:

```bash [Terminal]
npx nuxt typecheck
```

To enable type-checking at build or development time, you can also use the [`typescript.typeCheck`](/docs/4.x/api/nuxt-config#typecheck) option in your `nuxt.config` file:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  typescript: {
    typeCheck: true,
  },
})
```

## Auto-generated Types

Nuxt projects rely on auto-generated types to work properly. These types are stored in the [`.nuxt`](/docs/4.x/directory-structure/nuxt) directory and are generated when you run the dev server or build your application. You can also generate these files manually by running `nuxt prepare`.

The generated `tsconfig.json` files inside the [`.nuxt`](/docs/4.x/directory-structure/nuxt) directory include **recommended basic TypeScript configuration** for your project, references to [auto-imports](/docs/4.x/guide/concepts/auto-imports), [API route types](/docs/4.x/guide/concepts/server-engine#typed-api-routes), path aliases like `#imports`, `~/file`, or `#build/file`, and more.

<warning>

Nuxt relies on this configuration, and [Nuxt modules](/docs/4.x/guide/modules) can extend it as well. For this reason, it is not recommended to modify your `tsconfig.json` file directly, as doing so could overwrite important settings. Instead, extend it via `nuxt.config.ts`. [Learn more about extending the configuration here](/docs/4.x/directory-structure/tsconfig).

</warning>

<tip icon="i-lucide-video" target="_blank" to="https://youtu.be/umLI7SlPygY">

Watch a video from Daniel Roe explaining built-in Nuxt aliases.

</tip>

## Project References

Nuxt uses [TypeScript project references](https://www.typescriptlang.org/docs/handbook/project-references.html) to improve type-checking performance and provide better IDE support. This feature allows TypeScript to break up your codebase into smaller, more manageable pieces.

### How Nuxt Uses Project References

When you run `nuxt dev`, `nuxt build` or `nuxt prepare`, Nuxt will generate multiple `tsconfig.json` files for different parts of your application.

- **.nuxt/tsconfig.app.json** - Configuration for your application code within the `app/` directory
- **.nuxt/tsconfig.node.json** - Configuration for your `nuxt.config.ts` and files outside the other contexts
- **.nuxt/tsconfig.server.json** - Configuration for server-side code (when applicable)
- **.nuxt/tsconfig.shared.json** - For code shared between app and server contexts (like types and non-environment specific utilities)

Each of these files is configured to reference the appropriate dependencies and provide optimal type-checking for their specific context.

<note>

For backward compatibility, Nuxt still generates `.nuxt/tsconfig.json`. However, we recommend using [TypeScript project references](/docs/4.x/directory-structure/tsconfig) with the new configuration files (`.nuxt/tsconfig.app.json`, `.nuxt/tsconfig.server.json`, etc.) for better type safety and performance. This legacy file will be removed in a future version of Nuxt.

</note>

### Benefits of Project References

- **Faster builds**: TypeScript can skip rebuilding unchanged projects
- **Better IDE performance**: Your IDE can provide faster IntelliSense and error checking
- **Isolated compilation**: Errors in one part of your application don't prevent compilation of other parts
- **Clearer dependency management**: Each project explicitly declares its dependencies

### Augmenting Types with Project References

Since the project is divided into **multiple type contexts**, it's important to **augment types within the correct context** to ensure they're properly recognized. TypeScript will not recognize augmentations placed outside these directories unless they are explicitly included in the appropriate context.

For example, if you want to augment types for the `app` context, the augmentation file should be placed in the `app/` directory.

Similarly:

- For the `server` context, place the augmentation file in the `server/` directory.
- For types that are **shared between the app and server**, place the file in the `shared/` directory.

<read-more to="/docs/4.x/guide/modules/recipes-advanced#extend-typescript-config">

Read more about augmenting specific type contexts from **files outside those contexts** in the Module Author Guide.

</read-more>

## Strict Checks

TypeScript comes with certain checks to give you more safety and analysis of your program.

[Strict checks](https://www.typescriptlang.org/docs/handbook/migrating-from-javascript.html#getting-stricter-checks) are enabled by default in Nuxt when the [`typescript.typeCheck`](/docs/4.x/guide/concepts/typescript#type-checking) option is enabled to give you greater type safety.

If you are currently converting your codebase to TypeScript, you may want to temporarily disable strict checks by setting `strict` to `false` in your `nuxt.config`:

```ts [nuxt.config.ts]twoslash
export default defineNuxtConfig({
  typescript: {
    strict: false,
  },
})
```

## Code Style

# Code Style

> Nuxt supports ESLint out of the box

## ESLint

The recommended approach for Nuxt is to enable ESLint support using the [`@nuxt/eslint`](https://eslint.nuxt.com/packages/module) module, that will setup project-aware ESLint configuration for you.

<callout icon="i-lucide-lightbulb">

The module is designed for the [new ESLint flat config format](https://eslint.org/docs/latest/use/configure/configuration-files) which is the [default format since ESLint v9](https://eslint.org/blog/2024/04/eslint-v9.0.0-released/). If you are using the legacy `.eslintrc` config, you will need to [configure manually with `@nuxt/eslint-config`](https://eslint.nuxt.com/packages/config#customizing-the-config). We highly recommend you to migrate over the flat config to be future-proof.

</callout>

## Quick Setup

```bash
npx nuxt module add eslint
```

Start your Nuxt app, a `eslint.config.mjs` file will be generated under your project root. You can customize it as needed.

You can learn more about the module and customizations in [Nuxt ESLint's documentation](https://eslint.nuxt.com/packages/module).