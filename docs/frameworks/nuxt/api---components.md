# Nuxt - API - Components


## Client Only

# <ClientOnly>

> Render components only in client-side with the <ClientOnly> component.

The `<ClientOnly>` component is used for purposely rendering a component only on client side.

<note>

The content of the default slot will be tree-shaken out of the server build. (This does mean that any CSS used by components within it may not be inlined when rendering the initial HTML.)

</note>

## Props

- `placeholderTag` | `fallbackTag`: specify a tag to be rendered server-side.
- `placeholder` | `fallback`: specify a content to be rendered server-side.

```vue
<template>
  <div>
    <Sidebar />
    <!-- The <Comment> component will only be rendered on client-side -->
    <ClientOnly
      fallback-tag="span"
      fallback="Loading comments..."
    >
      <Comment />
    </ClientOnly>
  </div>
</template>
```

## Slots

- `#fallback`: specify a content to be rendered on the server and displayed until `<ClientOnly>` is mounted in the browser.

```vue [app/pages/example.vue]
<template>
  <div>
    <Sidebar />
    <!-- This renders the "span" element on the server side -->
    <ClientOnly fallback-tag="span">
      <!-- this component will only be rendered on client side -->
      <Comments />
      <template #fallback>
        <!-- this will be rendered on server side -->
        <p>Loading comments...</p>
      </template>
    </ClientOnly>
  </div>
</template>
```

## Examples

### Accessing HTML Elements

Components inside `<ClientOnly>` are rendered only after being mounted. To access the rendered elements in the DOM, you can watch a template ref:

```vue [app/pages/example.vue]
<script setup lang="ts">
const nuxtWelcomeRef = useTemplateRef('nuxtWelcomeRef')

// The watch will be triggered when the component is available
watch(nuxtWelcomeRef, () => {
  console.log('<NuxtWelcome /> mounted')
}, { once: true })
</script>

<template>
  <ClientOnly>
    <NuxtWelcome ref="nuxtWelcomeRef" />
  </ClientOnly>
</template>
```

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/client-only.ts)

## Nuxt Page

# <NuxtPage>

> The <NuxtPage> component is required to display pages located in the pages/ directory.

`<NuxtPage>` is a built-in component that comes with Nuxt. It lets you display top-level or nested pages located in the [`app/pages/`](/docs/4.x/directory-structure/app/pages) directory.

<note>

`<NuxtPage>` is a wrapper around [`<RouterView>`](https://router.vuejs.org/api/interfaces/routerviewprops) from Vue Router. It should be used instead of `<RouterView>` because the former takes additional care of internal states. Otherwise, `useRoute()` may return incorrect paths.

</note>

`<NuxtPage>` includes the following components:

```vue
<template>
  <RouterView v-slot="{ Component }">
    <!-- Optional, when using transitions -->
    <Transition>
      <!-- Optional, when using keep-alive -->
      <KeepAlive>
        <Suspense>
          <component :is="Component" />
        </Suspense>
      </KeepAlive>
    </Transition>
  </RouterView>
</template>
```

By default, Nuxt does not enable `<Transition>` and `<KeepAlive>`. You can enable them in the nuxt.config file or by setting the `transition` and `keepalive` properties on `<NuxtPage>`. If you want to define a specific page, you can set it in `definePageMeta` in the page component.

<warning>

If you enable `<Transition>` in your page component, ensure that the page has a single root element.

</warning>

Since `<NuxtPage>` uses `<Suspense>` under the hood, the component lifecycle behavior during page changes differs from that of a typical Vue application.

In a typical Vue application, a new page component is mounted **only after** the previous one has been fully unmounted. However, in Nuxt, due to how Vue `<Suspense>` is implemented, the new page component is mounted **before** the previous one is unmounted.

## Props

- `name`: tells `<RouterView>` to render the component with the corresponding name in the matched route record's components option. See [Named Views](/docs/4.x/directory-structure/app/pages#named-views) for the `name@view.vue` filename convention.

  - type: `string`
- `route`: route location that has all of its components resolved.

  - type: `RouteLocationNormalized`
- `pageKey`: control when the `NuxtPage` component is re-rendered.

  - type: `string` or `function`
- `transition`: define global transitions for all pages rendered with the `NuxtPage` component.

  - type: `boolean` or [`TransitionProps`](https://vuejs.org/api/built-in-components#transition)
- `keepalive`: control state preservation of pages rendered with the `NuxtPage` component.

  - type: `boolean` or [`KeepAliveProps`](https://vuejs.org/api/built-in-components#keepalive)

<tip>

Nuxt automatically resolves the `name` and `route` by scanning and rendering all Vue component files found in the `/pages` directory.

</tip>

## Example

For example, if you pass a key that never changes, the `<NuxtPage>` component will be rendered only once - when it is first mounted.

```vue [app/app.vue]
<template>
  <NuxtPage page-key="static" />
</template>
```

You can also use a dynamic key based on the current route:

```html
<NuxtPage :page-key="route => route.fullPath" />
```

<warning>

Don't use `$route` object here as it can cause problems with how `<NuxtPage>` renders pages with `<Suspense>`.

</warning>

Alternatively, `pageKey` can be passed as a `key` value via [`definePageMeta`](/docs/4.x/api/utils/define-page-meta) from the `<script>` section of your Vue component in the `/pages` directory.

```vue [app/pages/my-page.vue]
<script setup lang="ts">
definePageMeta({
  key: route => route.fullPath,
})
</script>
```

<link-example to="/docs/4.x/examples/routing/pages">



</link-example>

## Page's Ref

To get the `ref` of a page component, access it through `ref.value.pageRef`

```vue [app/app.vue]
<script setup lang="ts">
const page = ref()

function logFoo () {
  page.value.pageRef.foo()
}
</script>

<template>
  <NuxtPage ref="page" />
</template>
```

```vue [my-page.vue]
<script setup lang="ts">
const foo = () => {
  console.log('foo method called')
}

defineExpose({
  foo,
})
</script>
```

## Custom Props

`<NuxtPage>` also accepts custom props that you may need to pass further down the hierarchy.

For example, in the below example, the value of `foobar` will be passed to the `NuxtPage` component and then to the page components.

```vue [app/app.vue]
<template>
  <NuxtPage :foobar="123" />
</template>
```

We can access the `foobar` prop in the page component:

```vue [app/pages/page.vue]
<script setup lang="ts">
const props = defineProps<{ foobar: number }>()

console.log(props.foobar) // Outputs: 123
```

If you have not defined the prop with `defineProps`, any props passed down to `NuxtPage` can still be accessed directly from the page `attrs`:

```vue [app/pages/page.vue]
<script setup lang="ts">
const attrs = useAttrs()
console.log(attrs.foobar) // Outputs: 123
</script>
```

<read-more to="/docs/4.x/directory-structure/app/pages">



</read-more>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/pages/runtime/page.ts)

## Nuxt Layout

# <NuxtLayout>

> Nuxt provides the <NuxtLayout> component to show layouts on pages and error pages.

You can use `<NuxtLayout />` component to activate the `default` layout on `app.vue` or `error.vue`.

```vue [app/app.vue]
<template>
  <NuxtLayout>
    some page content
  </NuxtLayout>
</template>
```

<read-more to="/docs/4.x/directory-structure/app/layouts">



</read-more>

## Props

- `name`: Specify a layout name to be rendered, can be a string, reactive reference or a computed property. It **must** match the name of the corresponding layout file in the [`app/layouts/`](/docs/4.x/directory-structure/app/layouts) directory, or `false` to disable the layout.

  - **type**: `string | false`
  - **default**: `default`

```vue [app/pages/index.vue]
<script setup lang="ts">
// layouts/custom.vue
const layout = 'custom'
</script>

<template>
  <NuxtLayout :name="layout">
    <NuxtPage />
  </NuxtLayout>
</template>
```

<note>

Please note the layout name is normalized to kebab-case, so if your layout file is named `errorLayout.vue`, it will become `error-layout` when passed as a `name` property to `<NuxtLayout />`.

</note>

```vue [error.vue]
<template>
  <NuxtLayout name="error-layout">
    <NuxtPage />
  </NuxtLayout>
</template>
```

<read-more to="/docs/4.x/directory-structure/app/layouts">

Read more about dynamic layouts.

</read-more>

- `fallback`: If an invalid layout is passed to the `name` prop, no layout will be rendered. Specify a `fallback` layout to be rendered in this scenario. It **must** match the name of the corresponding layout file in the [`app/layouts/`](/docs/4.x/directory-structure/app/layouts) directory.

  - **type**: `string`
  - **default**: `null`

## Additional Props

`NuxtLayout` also accepts any additional props that you may need to pass to the layout. These custom props are then made accessible as attributes.

```vue [app/pages/some-page.vue]
<template>
  <div>
    <NuxtLayout
      name="custom"
      title="I am a custom layout"
    >
      <!-- ... -->
    </NuxtLayout>
  </div>
</template>
```

In the above example, the value of `title` will be available using `$attrs.title` in the template or `useAttrs().title` in `<script setup>` at custom.vue.

```vue [app/layouts/custom.vue]
<script setup lang="ts">
const layoutCustomProps = useAttrs()

console.log(layoutCustomProps.title) // I am a custom layout
</script>
```

## Layout Props from Page Meta

When using [`definePageMeta`](/docs/4.x/api/utils/define-page-meta) with the object syntax for `layout`, props are automatically passed to the layout component. The layout can receive them with `defineProps`:

```vue [app/pages/dashboard.vue]
<script setup lang="ts">
definePageMeta({
  layout: {
    name: 'admin',
    props: {
      sidebar: true,
    },
  },
})
</script>
```

```vue [app/layouts/admin.vue]
<script setup lang="ts">
const props = defineProps<{
  sidebar?: boolean
}>()
</script>
```

<read-more to="/docs/4.x/directory-structure/app/layouts#passing-props-to-layouts">

Read more about passing props to layouts.

</read-more>

## Transitions

`<NuxtLayout />` renders incoming content via `<slot />`, which is then wrapped around Vue’s `<Transition />` component to activate layout transition. For this to work as expected, it is recommended that `<NuxtLayout />` is **not** the root element of the page component.

<code-group>

```vue [app/pages/index.vue]
<template>
  <div>
    <NuxtLayout name="custom">
      <template #header>
        Some header template content.
      </template>
    </NuxtLayout>
  </div>
</template>
```

```vue [app/layouts/custom.vue]
<template>
  <div>
    <!-- named slot -->
    <slot name="header" />
    <slot />
  </div>
</template>
```

</code-group>

<read-more to="/docs/4.x/getting-started/transitions">



</read-more>

## Layout's Ref

To get the ref of a layout component, access it through `ref.value.layoutRef`.

<code-group>

```vue [app/app.vue]
<script setup lang="ts">
const layout = ref()

function logFoo () {
  layout.value.layoutRef.foo()
}
</script>

<template>
  <NuxtLayout ref="layout">
    default layout
  </NuxtLayout>
</template>
```

```vue [app/layouts/default.vue]
<script setup lang="ts">
const foo = () => console.log('foo')
defineExpose({
  foo,
})
</script>

<template>
  <div>
    default layout
    <slot />
  </div>
</template>
```

</code-group>

<read-more to="/docs/4.x/directory-structure/app/layouts">



</read-more>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/nuxt-layout.ts)

## Nuxt Link

# <NuxtLink>

> Nuxt provides <NuxtLink> component to handle any kind of links within your application.

<note>

`<NuxtLink>` is a drop-in replacement for both Vue Router's `<RouterLink>` component and HTML's `<a>` tag. It intelligently determines whether the link is *internal* or *external* and renders it accordingly with available optimizations (prefetching, default attributes, etc.)

</note>

## Internal Routing

In this example, we use `<NuxtLink>` component to link to another page of the application.

<code-group>

```vue [app/pages/index.vue]
<template>
  <NuxtLink to="/about">About page</NuxtLink>
</template>
```

```html [(Renders as) index.html]
<!-- (Vue Router & Smart Prefetching) -->
<a href="/about">About page</a>
```

</code-group>

### Passing Params to Dynamic Routes

In this example, we pass the `id` param to link to the route `~/pages/posts/[id].vue`.

<code-group>

```vue [app/pages/index.vue]
<template>
  <NuxtLink :to="{ name: 'posts-id', params: { id: 123 } }">
    Post 123
  </NuxtLink>
</template>
```

```html [(Renders as) index.html]
<a href="/posts/123">Post 123</a>
```

</code-group>

<tip>

Check out the Pages panel in Nuxt DevTools to see the route name and the params it might take.

</tip>

<tip>

When you pass an object into the `to` prop, `<NuxtLink>` will inherit Vue Router’s handling of query parameters. Keys and values will be automatically encoded, so you don’t need to call `encodeURI` or `encodeURIComponent` manually.

</tip>

### Handling Static File and Cross-App Links

By default, `<NuxtLink>` uses Vue Router's client side navigation for relative route. When linking to static files in the `/public` directory or to another application hosted on the same domain, it might result in unexpected 404 errors because they are not part of the client routes. In such cases, you can use the `external` prop with `<NuxtLink>` to bypass Vue Router's internal routing mechanism.

The `external` prop explicitly indicates that the link is external. `<NuxtLink>` will render the link as a standard HTML `<a>` tag. This ensures the link behaves correctly, bypassing Vue Router’s logic and directly pointing to the resource.

#### Linking to Static Files

For static files in the `/public` directory, such as PDFs or images, use the `external` prop to ensure the link resolves correctly.

```vue [app/pages/index.vue]
<template>
  <NuxtLink
    to="/example-report.pdf"
    external
  >
    Download Report
  </NuxtLink>
</template>
```

#### Linking to a Cross-App URL

When pointing to a different application on the same domain, using the `external` prop ensures the correct behavior.

```vue [app/pages/index.vue]
<template>
  <NuxtLink
    to="/another-app"
    external
  >
    Go to Another App
  </NuxtLink>
</template>
```

Using the `external` prop or relying on automatic handling ensures proper navigation, avoids unexpected routing issues, and improves compatibility with static resources or cross-application scenarios.

## External Routing

In this example, we use `<NuxtLink>` component to link to a website.

```vue [app/app.vue]
<template>
  <NuxtLink to="https://nuxtjs.org">
    Nuxt website
  </NuxtLink>
  <!-- <a href="https://nuxtjs.org" rel="noopener noreferrer">...</a> -->
</template>
```

## `rel` and `noRel` Attributes

A `rel` attribute of `noopener noreferrer` is applied by default to links with a `target` attribute or to absolute links (e.g., links starting with `http://`, `https://`, or `//`).

- `noopener` solves a [security bug](https://mathiasbynens.github.io/rel-noopener/) in older browsers.
- `noreferrer` improves privacy for your users by not sending the `Referer` header to the linked site.

These defaults have no negative impact on SEO and are considered [best practice](https://developer.chrome.com/docs/lighthouse/best-practices/external-anchors-use-rel-noopener).

When you need to overwrite this behavior you can use the `rel` or `noRel` props.

```vue [app/app.vue]
<template>
  <NuxtLink to="https://twitter.com/nuxt_js">
    Nuxt Twitter
  </NuxtLink>
  <!-- <a href="https://twitter.com/nuxt_js" rel="noopener noreferrer">...</a> -->

  <NuxtLink
    to="https://discord.nuxtjs.org"
    rel="noopener"
  >
    Nuxt Discord
  </NuxtLink>
  <!-- <a href="https://discord.nuxtjs.org" rel="noopener">...</a> -->

  <NuxtLink
    to="/about"
    target="_blank"
  >About page</NuxtLink>
  <!-- <a href="/about" target="_blank" rel="noopener noreferrer">...</a> -->
</template>
```

A `noRel` prop can be used to prevent the default `rel` attribute from being added to the absolute links.

```vue [app/app.vue]
<template>
  <NuxtLink
    to="https://github.com/nuxt"
    no-rel
  >
    Nuxt GitHub
  </NuxtLink>
  <!-- <a href="https://github.com/nuxt">...</a> -->
</template>
```

<note>

`noRel` and `rel` cannot be used together. `rel` will be ignored.

</note>

## Prefetch Links

Nuxt automatically includes smart prefetching. That means it detects when a link is visible (by default), either in the viewport or when scrolling and prefetches the JavaScript for those pages so that they are ready when the user clicks the link. Nuxt only loads the resources when the browser isn't busy and skips prefetching if your connection is offline or if you only have 2g connection.

```vue [app/pages/index.vue]
<NuxtLink to="/about" no-prefetch>
About page not pre-fetched
</NuxtLink>

<NuxtLink to="/about" :prefetch="false">
About page not pre-fetched
</NuxtLink>
```

### Custom Prefetch Triggers

We now support custom prefetch triggers for `<NuxtLink>` after `v3.13.0`. You can use the `prefetchOn` prop to control when to prefetch links.

```vue
<template>
  <NuxtLink prefetch-on="visibility">
    This will prefetch when it becomes visible (default)
  </NuxtLink>

  <NuxtLink prefetch-on="interaction">
    This will prefetch when hovered or when it gains focus
  </NuxtLink>
</template>
```

- `visibility`: Prefetches when the link becomes visible in the viewport. Monitors the element's intersection with the viewport using the [Intersection Observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API). Prefetching is triggered when the element is scrolled into view.
- `interaction`: Prefetches when the link is hovered or focused. This approach listens for `pointerenter` and `focus` events, proactively prefetching resources when the user indicates intent to interact.

You can also use an object to configure `prefetchOn`:

```vue
<template>
  <NuxtLink :prefetch-on="{ interaction: true }">
    This will prefetch when hovered or when it gains focus
  </NuxtLink>
</template>
```

That you probably don't want both enabled!

```vue
<template>
  <NuxtLink :prefetch-on="{ visibility: true, interaction: true }">
    This will prefetch when hovered/focus - or when it becomes visible
  </NuxtLink>
</template>
```

This configuration will observe when the element enters the viewport and also listen for `pointerenter` and `focus` events. This may result in unnecessary resource usage or redundant prefetching, as both triggers can prefetch the same resource under different conditions.

### Enable Cross-origin Prefetch

To enable cross-origin prefetching, you can set the `crossOriginPrefetch` option in your `nuxt.config`. This will enable cross-origin prefetching using the [Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API).

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  experimental: {
    crossOriginPrefetch: true,
  },
})
```

### Disable prefetch globally

It's also possible to enable/disable prefetching all links globally for your app.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  experimental: {
    defaults: {
      nuxtLink: {
        prefetch: false,
      },
    },
  },
})
```

## Props

### RouterLink

When not using `external`, `<NuxtLink>` supports all Vue Router's [`RouterLink` props](https://router.vuejs.org/api/interfaces/routerlinkprops)

- `to`: Any URL or a [route location object](https://router.vuejs.org/api/type-aliases/routelocation) from Vue Router
- `custom`: Whether `<NuxtLink>` should wrap its content in an `<a>` element. It allows taking full control of how a link is rendered and how navigation works when it is clicked. Works the same as [Vue Router's `custom` prop](https://router.vuejs.org/api/interfaces/routerlinkprops#custom-)
- `exactActiveClass`: A class to apply on exact active links. Works the same as [Vue Router's `exactActiveClass` prop](https://router.vuejs.org/api/interfaces/routerlinkprops#exactActiveClass-) on internal links. Defaults to Vue Router's default (`"router-link-exact-active"`)
- `activeClass`: A class to apply on active links. Works the same as [Vue Router's `activeClass` prop](https://router.vuejs.org/api/interfaces/routerlinkprops#activeClass-) on internal links. Defaults to Vue Router's default (`"router-link-active"`)
- `replace`: Works the same as [Vue Router's `replace` prop](https://router.vuejs.org/api/interfaces/routelocationoptions#replace-) on internal links
- `ariaCurrentValue`: An `aria-current` attribute value to apply on exact active links. Works the same as [Vue Router's `ariaCurrentValue` prop](https://router.vuejs.org/api/interfaces/routerlinkprops#ariaCurrentValue-) on internal links

### NuxtLink

- `href`: An alias for `to`. If used with `to`, `href` will be ignored
- `noRel`: If set to `true`, no `rel` attribute will be added to the external link
- `external`: Forces the link to be rendered as an `<a>` tag instead of a Vue Router `RouterLink`.
- `prefetch`: When enabled will prefetch middleware, layouts and payloads (when using [payloadExtraction](/docs/4.x/guide/going-further/experimental-features#payloadextraction)) of links in the viewport. Used by the experimental [crossOriginPrefetch](/docs/4.x/guide/going-further/experimental-features#crossoriginprefetch) config.
- `prefetchOn`: Allows custom control of when to prefetch links. Possible options are `interaction` and `visibility` (default). You can also pass an object for full control, for example: `{ interaction: true, visibility: true }`. This prop is only used when `prefetch` is enabled (default) and `noPrefetch` is not set.
- `noPrefetch`: Disables prefetching.
- `prefetchedClass`: A class to apply to links that have been prefetched.

### Anchor

- `target`: A `target` attribute value to apply on the link
- `rel`: A `rel` attribute value to apply on the link. Defaults to `"noopener noreferrer"` for external links.

<tip>

Defaults can be overwritten, see [overwriting defaults](/docs/4.x/api/components/nuxt-link#overwriting-defaults) if you want to change them.

</tip>

## Overwriting Defaults

### In Nuxt Config

You can overwrite some `<NuxtLink>` defaults in your [`nuxt.config`](/docs/4.x/guide/going-further/experimental-features#defaults)

<important>

These options will likely be moved elsewhere in the future, such as into `app.config` or into the `app/` directory.

</important>

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  experimental: {
    defaults: {
      nuxtLink: {
        // default values
        componentName: 'NuxtLink',
        externalRelAttribute: 'noopener noreferrer',
        activeClass: 'router-link-active',
        exactActiveClass: 'router-link-exact-active',
        prefetchedClass: undefined, // can be any valid string class name
        trailingSlash: undefined, // can be 'append' or 'remove'
        prefetch: true,
        prefetchOn: { visibility: true },
      },
    },
  },
})
```

### Custom Link Component

You can overwrite `<NuxtLink>` defaults by creating your own link component using `defineNuxtLink`.

```ts [app/components/MyNuxtLink.ts]
export default defineNuxtLink({
  componentName: 'MyNuxtLink',
  /* see signature below for more */
})
```

You can then use `<MyNuxtLink />` component as usual with your new defaults.

### `defineNuxtLink` Signature

```ts
interface NuxtLinkOptions {
  componentName?: string
  externalRelAttribute?: string
  activeClass?: string
  exactActiveClass?: string
  trailingSlash?: 'append' | 'remove'
  prefetch?: boolean
  prefetchedClass?: string
  prefetchOn?: Partial<{
    visibility: boolean
    interaction: boolean
  }>
}
function defineNuxtLink (options: NuxtLinkOptions): Component {}
```

- `componentName`: A name for the component. Default is `NuxtLink`.
- `externalRelAttribute`: A default `rel` attribute value applied on external links. Defaults to `"noopener noreferrer"`. Set it to `""` to disable
- `activeClass`: A default class to apply on active links. Works the same as [Vue Router's `linkActiveClass` option](https://router.vuejs.org/api/interfaces/routeroptions#linkActiveClass-). Defaults to Vue Router's default (`"router-link-active"`)
- `exactActiveClass`: A default class to apply on exact active links. Works the same as [Vue Router's `linkExactActiveClass` option](https://router.vuejs.org/api/interfaces/routeroptions#linkExactActiveClass-). Defaults to Vue Router's default (`"router-link-exact-active"`)
- `trailingSlash`: An option to either add or remove trailing slashes in the `href`. If unset or not matching the valid values `append` or `remove`, it will be ignored.
- `prefetch`: Whether or not to prefetch links by default.
- `prefetchOn`: Granular control of which prefetch strategies to apply by default.
- `prefetchedClass`: A default class to apply to links that have been prefetched.

<link-example to="/docs/4.x/examples/routing/pages">



</link-example>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/nuxt-link.ts)

## Nuxt Loading Indicator

# <NuxtLoadingIndicator>

> Display a progress bar between page navigations.

## Usage

Add `<NuxtLoadingIndicator/>` in your [`app.vue`](/docs/4.x/directory-structure/app/app) or [`app/layouts/`](/docs/4.x/directory-structure/app/layouts).

```vue [app/app.vue]
<template>
  <NuxtLoadingIndicator />
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
```

<link-example to="/docs/4.x/examples/routing/pages">



</link-example>

## Slots

You can pass custom HTML or components through the loading indicator's default slot.

## Props

- `color`: The color of the loading bar. It can be set to `false` to turn off explicit color styling.
- `errorColor`: The color of the loading bar when `error` is set to `true`.
- `height`: Height of the loading bar, in pixels (default `3`).
- `duration`: Duration of the loading bar, in milliseconds (default `2000`).
- `throttle`: Throttle the appearing and hiding, in milliseconds (default `200`).
- `estimatedProgress`: By default Nuxt will back off as it approaches 100%. You can provide a custom function to customize the progress estimation, which is a function that receives the duration of the loading bar (above) and the elapsed time. It should return a value between 0 and 100.

<note>

This component is optional. <br />


To achieve full customization, you can implement your own one based on [its source code](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/nuxt-loading-indicator.ts).

</note>

<note>

You can hook into the underlying indicator instance using [the `useLoadingIndicator` composable](/docs/4.x/api/composables/use-loading-indicator), which will allow you to trigger start/finish events yourself.

</note>

<tip>

The loading indicator's speed gradually decreases after reaching a specific point controlled by `estimatedProgress`. This adjustment provides a more accurate reflection of longer page loading times and prevents the indicator from prematurely showing 100% completion.

</tip>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/nuxt-loading-indicator.ts)

## Nuxt Error Boundary

# <NuxtErrorBoundary>

> The <NuxtErrorBoundary> component handles client-side errors happening in its default slot.

<tip>

The `<NuxtErrorBoundary>` uses Vue's [`onErrorCaptured`](https://vuejs.org/api/composition-api-lifecycle#onerrorcaptured) hook under the hood.

</tip>

## Events

- `@error`: Event emitted when the default slot of the component throws an error.```vue
<template>
  <NuxtErrorBoundary @error="logSomeError">
    <!-- ... -->
  </NuxtErrorBoundary>
</template>
```

## Slots

- `#error`: Specify a fallback content to display in case of error.```vue
<template>
  <NuxtErrorBoundary>
    <!-- ... -->
    <template #error="{ error, clearError }">
      <p>An error occurred: {{ error }}</p>

      <button @click="clearError">
        Clear error
      </button>
    </template>
  </NuxtErrorBoundary>
</template>
```

<read-more to="/docs/4.x/getting-started/error-handling">



</read-more>

## Examples

### Accessing `error` and `clearError` in script

You can access `error` and `clearError` properties within the component's script as below:

```vue
<template>
  <NuxtErrorBoundary ref="errorBoundary">
    <!-- ... -->
  </NuxtErrorBoundary>
</template>

<script setup lang="ts">
const errorBoundary = useTemplateRef('errorBoundary')

// errorBoundary.value?.error
// errorBoundary.value?.clearError()
</script>
```

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/nuxt-error-boundary.vue)

## Nuxt Img

# <NuxtImg>

> Nuxt provides a <NuxtImg> component to handle automatic image optimization.

`<NuxtImg>` is a drop-in replacement for the native `<img>` tag.

- Uses built-in provider to optimize local and remote images
- Converts `src` to provider-optimized URLs
- Automatically resizes images based on `width` and `height`
- Generates responsive sizes when providing `sizes` option
- Supports native lazy loading as well as other `<img>` attributes

## Setup

In order to use `<NuxtImg>` you should install and enable the Nuxt Image module:

```bash [Terminal]
npx nuxt module add image
```

## Usage

`<NuxtImg>` outputs a native `img` tag directly (without any wrapper around it). Use it like you would use the `<img>` tag:

```html
<NuxtImg src="/nuxt-icon.png" />
```

Will result in:

```html
<img src="/nuxt-icon.png" />
```

<read-more target="_blank" to="https://image.nuxt.com/usage/nuxt-img">

Read more about the `<NuxtImg>` component.

</read-more>

<style>

html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}

</style>

---

- [Source](https://github.com/nuxt/image/blob/main/src/runtime/components/NuxtImg.vue)

## Nuxt Picture

# <NuxtPicture>

> Nuxt provides a <NuxtPicture> component to handle automatic image optimization.

`<NuxtPicture>` is a drop-in replacement for the native `<picture>` tag.

Usage of `<NuxtPicture>` is almost identical to [`<NuxtImg>`](/docs/4.x/api/components/nuxt-img) but it also allows serving modern formats like `webp` when possible.

Learn more about the [`<picture>` tag on MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture).

## Setup

In order to use `<NuxtPicture>` you should install and enable the Nuxt Image module:

```bash [Terminal]
npx nuxt module add image
```

<read-more target="_blank" to="https://image.nuxt.com/usage/nuxt-picture">

Read more about the `<NuxtPicture>` component.

</read-more>

<style>

html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/image/blob/main/src/runtime/components/NuxtPicture.vue)

## Nuxt Welcome

# <NuxtWelcome>

> The <NuxtWelcome> component greets users in new projects made from the starter template.

It includes links to the Nuxt documentation, source code, and social media accounts.

```vue [app/app.vue]
<template>
  <NuxtWelcome />
</template>
```

<read-more target="_blank" to="https://templates.ui.nuxtjs.org/templates/welcome">

Preview the `<NuxtWelcome />` component.

</read-more>

<tip>

This component is part of [`@nuxt/ui-templates`](https://github.com/nuxt/nuxt/tree/main/packages/ui-templates) package.

</tip>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/ui-templates/templates/welcome/index.html)

## Nuxt Island

# <NuxtIsland>

> Nuxt provides the <NuxtIsland> component to render a non-interactive component without any client JS.

When rendering an island component, the content of the island component is static, thus no JS is downloaded client-side.

Changing the island component props triggers a refetch of the island component to re-render it again.

<note>

Global styles of your application are sent with the response.

</note>

<tip>

Server only components use `<NuxtIsland>` under the hood

</tip>

## Props

- `name` : Name of the component to render.

  - **type**: `string`
  - **required**
- `lazy`: Make the component non-blocking.

  - **type**: `boolean`
  - **default**: `false`
- `props`: Props to send to the component to render.

  - **type**: `Record<string, any>`
- `source`: Remote source to call the island to render.

  - **type**: `string`
- **dangerouslyLoadClientComponents**: Required to load client components from a remote source.

  - **type**: `boolean`
  - **default**: `false`

<note>

Remote islands need `experimental.componentIslands` to be `'local+remote'` in your `nuxt.config`.

</note>

<warning icon="i-ph-warning-duotone">

Using the `source` prop to render content from a remote server is inherently dangerous. When you specify a remote `source`, you are fully trusting that server to provide safe HTML content that will be rendered directly in your application.

This is similar to using `v-html` with external content - the remote server can inject any HTML, including potentially malicious content. **Only use source with servers you fully trust and control.**

The `dangerouslyLoadClientComponents` prop controls an additional layer of risk: whether to also download and execute client components from the remote source. Even with `dangerouslyLoadClientComponents` disabled (the default), you are still trusting the remote server's HTML output.

</warning>

<note>

Component props and context are sent as GET query parameters to enable caching. Query parameters may be visible in server access logs, CDN caches, and HTTP `Referer` headers.

</note>

<note>

By default, component islands are scanned from the `~/components/islands/` directory. So the `~/components/islands/MyIsland.vue` component could be rendered with `<NuxtIsland name="MyIsland" />`.

</note>

## Slots

Slots can be passed to an island component if declared.

Every slot is interactive since the parent component is the one providing it.

Some slots are reserved to `NuxtIsland` for special cases.

- `#fallback`: Specify the content to be rendered before the island loads (if the component is lazy) or if `NuxtIsland` fails to fetch the component.

## Ref

- `refresh()`
  - **type**: `() => Promise<void>`
  - **description**: force refetch the server component by refetching it.

## Events

- `error`
  - **parameters**:
  
    - **error**:
    
      - **type**: `unknown`
  - **description**: emitted when `NuxtIsland` fails to fetch the new island.

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/nuxt-island.ts)

## Nuxt Route Announcer

# <NuxtRouteAnnouncer>

> The <NuxtRouteAnnouncer> component adds a hidden element with the page title to announce route changes to assistive technologies.

<important>

This component is available in Nuxt v3.12+.

</important>

## Usage

Add `<NuxtRouteAnnouncer/>` in your [`app.vue`](/docs/4.x/directory-structure/app/app) or [`app/layouts/`](/docs/4.x/directory-structure/app/layouts) to enhance accessibility by informing assistive technologies about page title changes. This ensures that navigational changes are announced to users relying on screen readers.

```vue [app/app.vue]
<template>
  <NuxtRouteAnnouncer />
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
```

## Slots

You can pass custom HTML or components through the route announcer's default slot.

```vue
<template>
  <NuxtRouteAnnouncer>
    <template #default="{ message }">
      <p>{{ message }} was loaded.</p>
    </template>
  </NuxtRouteAnnouncer>
</template>
```

## Props

- `atomic`: Controls if screen readers only announce changes or the entire content. Set to true for full content readouts on updates, false for changes only. (default `false`)
- `politeness`: Sets the urgency for screen reader announcements: `off` (disable the announcement), `polite` (waits for silence), or `assertive` (interrupts immediately). (default `polite`)

<callout>

This component is optional. <br />


To achieve full customization, you can implement your own one based on [its source code](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/nuxt-route-announcer.ts).

</callout>

<callout>

You can hook into the underlying announcer instance using [the `useRouteAnnouncer` composable](/docs/4.x/api/composables/use-route-announcer), which allows you to set a custom announcement message.

</callout>

<callout>

For announcing in-page content changes (form validation, toast notifications, loading states, etc.), use the [`<NuxtAnnouncer>`](/docs/4.x/api/components/nuxt-announcer) component with the [`useAnnouncer`](/docs/4.x/api/composables/use-announcer) composable instead.

</callout>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/nuxt-route-announcer.ts)

## Nuxt Time

# <NuxtTime>

> The <NuxtTime> component displays time in a locale-friendly format with server-client consistency.

<important>

This component is available in Nuxt v3.17+.

</important>

The `<NuxtTime>` component lets you display dates and times in a locale-friendly format with proper `<time>` HTML semantics. It ensures consistent rendering between server and client without hydration mismatches.

## Usage

You can use the `<NuxtTime>` component anywhere in your app:

```vue
<template>
  <NuxtTime :datetime="Date.now()" />
</template>
```

## Props

### `datetime`

- Type: `Date | number | string`
- Required: `true`

The date and time value to display. You can provide:

- A `Date` object
- A timestamp (number)
- An ISO-formatted date string

```vue
<template>
  <NuxtTime :datetime="Date.now()" />
  <NuxtTime :datetime="new Date()" />
  <NuxtTime datetime="2023-06-15T09:30:00.000Z" />
</template>
```

### `locale`

- Type: `string`
- Required: `false`
- Default: Uses the browser or server's default locale

The [BCP 47 language tag](https://datatracker.ietf.org/doc/html/rfc5646) for formatting (e.g., 'en-US', 'fr-FR', 'ja-JP'):

```vue
<template>
  <NuxtTime
    :datetime="Date.now()"
    locale="fr-FR"
  />
</template>
```

### Formatting Props

The component accepts any property from the [Intl.DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat) options:

```vue
<template>
  <NuxtTime
    :datetime="Date.now()"
    year="numeric"
    month="long"
    day="numeric"
    hour="2-digit"
    minute="2-digit"
  />
</template>
```

This would output something like: "April 22, 2025, 08:30 AM"

### `relative`

- Type: `boolean`
- Required: `false`
- Default: `false`

Enables relative time formatting using the Intl.RelativeTimeFormat API:

```vue
<template>
  <!-- Shows something like "5 minutes ago" -->
  <NuxtTime
    :datetime="Date.now() - 5 * 60 * 1000"
    relative
  />
</template>
```

### Relative Time Formatting Props

When `relative` is set to `true`, the component also accepts properties from [Intl.RelativeTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/RelativeTimeFormat):

<warning>

Due to `style` being a reserved prop, `relativeStyle` prop is used instead.

</warning>

```vue
<template>
  <NuxtTime
    :datetime="Date.now() - 3 * 24 * 60 * 60 * 1000"
    relative
    numeric="auto"
    relative-style="long"
  />
</template>
```

This would output something like: "3 days ago" or "last Friday" depending on the `numeric` setting.

## Examples

### Basic Usage

```vue
<template>
  <NuxtTime :datetime="Date.now()" />
</template>
```

### Custom Formatting

```vue
<template>
  <NuxtTime
    :datetime="Date.now()"
    weekday="long"
    year="numeric"
    month="short"
    day="numeric"
    hour="numeric"
    minute="numeric"
    second="numeric"
    time-zone-name="short"
  />
</template>
```

### Relative Time

```vue
<template>
  <div>
    <p>
      <NuxtTime
        :datetime="Date.now() - 30 * 1000"
        relative
      />
      <!-- 30 seconds ago -->
    </p>
    <p>
      <NuxtTime
        :datetime="Date.now() - 45 * 60 * 1000"
        relative
      />
      <!-- 45 minutes ago -->
    </p>
    <p>
      <NuxtTime
        :datetime="Date.now() + 2 * 24 * 60 * 60 * 1000"
        relative
      />
      <!-- in 2 days -->
    </p>
  </div>
</template>
```

### With Custom Locale

```vue
<template>
  <div>
    <NuxtTime
      :datetime="Date.now()"
      locale="en-US"
      weekday="long"
    />
    <NuxtTime
      :datetime="Date.now()"
      locale="fr-FR"
      weekday="long"
    />
    <NuxtTime
      :datetime="Date.now()"
      locale="ja-JP"
      weekday="long"
    />
  </div>
</template>
```

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/nuxt-time.vue)

## Nuxt Announcer

# <NuxtAnnouncer>

> The <NuxtAnnouncer> component adds a hidden element to announce dynamic content changes to assistive technologies.

<important>

This component is available in Nuxt v4.4.2+.

</important>

## Usage

Add `<NuxtAnnouncer/>` in your [`app.vue`](/docs/4.x/directory-structure/app/app) or [`app/layouts/`](/docs/4.x/directory-structure/app/layouts) to enable announcing dynamic content changes to screen readers. This is useful for form validation, toast notifications, loading states, and other in-page updates.

```vue [app/app.vue]
<template>
  <NuxtAnnouncer />
  <NuxtRouteAnnouncer />
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
```

Then use the [`useAnnouncer`](/docs/4.x/api/composables/use-announcer) composable anywhere in your app to announce messages:

```vue [app/pages/contact.vue]
<script setup lang="ts">
const { polite, assertive } = useAnnouncer()

async function submitForm () {
  try {
    await $fetch('/api/contact', { method: 'POST', body: formData })
    polite('Message sent successfully')
  } catch (error) {
    assertive('Error: Failed to send message')
  }
}
</script>
```

## Slots

You can pass custom HTML or components through the announcer's default slot.

```vue
<template>
  <NuxtAnnouncer>
    <template #default="{ message }">
      <p>{{ message }}</p>
    </template>
  </NuxtAnnouncer>
</template>
```

## Props

- `atomic`: Controls if screen readers announce only changes or the entire content. Set to true for full content readouts on updates, false for changes only. (default `true`)
- `politeness`: Sets the default urgency for screen reader announcements: `off` (disable the announcement), `polite` (waits for silence), or `assertive` (interrupts immediately). (default `polite`)

## Differences from `<NuxtRouteAnnouncer>`

<table>
<thead>
  <tr>
    <th>
      Aspect
    </th>
    
    <th>
      <code>
        <NuxtRouteAnnouncer>
      </code>
    </th>
    
    <th>
      <code>
        <NuxtAnnouncer>
      </code>
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <strong>
        Purpose
      </strong>
    </td>
    
    <td>
      Announces route/page changes
    </td>
    
    <td>
      Announces any dynamic content
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Trigger
      </strong>
    </td>
    
    <td>
      Automatic on navigation
    </td>
    
    <td>
      Manual via <code>
        polite()
      </code>
      
      /<code>
        assertive()
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        Message source
      </strong>
    </td>
    
    <td>
      Page <code>
        <title>
      </code>
    </td>
    
    <td>
      Developer-provided
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>
        atomic default
      </strong>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
  </tr>
</tbody>
</table>

<callout>

This component is optional. <br />


To achieve full customization, you can implement your own one based on [its source code](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/nuxt-announcer.ts).

</callout>

<callout>

You can hook into the underlying announcer instance using [the `useAnnouncer` composable](/docs/4.x/api/composables/use-announcer), which allows you to set custom announcement messages.

</callout>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/nuxt-announcer.ts)

## Nuxt Client Fallback

# <NuxtClientFallback>

> Nuxt provides the <NuxtClientFallback> component to render its content on the client if any of its children trigger an error in SSR

Nuxt provides the `<NuxtClientFallback>` component to render its content on the client if any of its children trigger an error in SSR.

<note to="/docs/4.x/guide/going-further/experimental-features#clientfallback">

This component is experimental and in order to use it you must enable the `experimental.clientFallback` option in your `nuxt.config`.

</note>

```vue [app/pages/example.vue]
<template>
  <div>
    <Sidebar />
    <!-- this component will be rendered on client-side -->
    <NuxtClientFallback fallback-tag="span">
      <Comments />
      <BrokeInSSR />
    </NuxtClientFallback>
  </div>
</template>
```

## Events

- `@ssr-error`: Event emitted when a child triggers an error in SSR. Note that this will only be triggered on the server.```vue
<template>
  <NuxtClientFallback @ssr-error="logSomeError">
    <!-- ... -->
  </NuxtClientFallback>
</template>
```

## Props

- `placeholderTag` | `fallbackTag`: Specify a fallback tag to be rendered if the slot fails to render on the server.

  - **type**: `string`
  - **default**: `div`
- `placeholder` | `fallback`: Specify fallback content to be rendered if the slot fails to render.

  - **type**: `string`
- `keepFallback`: Keep the fallback content if it failed to render server-side.

  - **type**: `boolean`
  - **default**: `false`

<warning icon="i-ph-warning-duotone">

The `placeholder` and `fallback` props render content as raw HTML. Do not pass untrusted user input to these props as it may lead to XSS vulnerabilities. Use the `#fallback` or `#placeholder` slots instead for dynamic content that needs proper escaping.

</warning>

```vue
<template>
  <!-- render <span>Hello world</span> server-side if the default slot fails to render -->
  <NuxtClientFallback
    fallback-tag="span"
    fallback="Hello world"
  >
    <BrokeInSSR />
  </NuxtClientFallback>
</template>
```

## Slots

- `#fallback`: specify content to be displayed server-side if the slot fails to render.

```vue
<template>
  <NuxtClientFallback>
    <!-- ... -->
    <template #fallback>
      <!-- this will be rendered on server side if the default slot fails to render in ssr -->
      <p>Hello world</p>
    </template>
  </NuxtClientFallback>
</template>
```

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}

</style>

---

- [Source (client)](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/client-fallback.client.ts)
- [Source (server)](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/client-fallback.server.ts)

## Dev Only

# <DevOnly>

> Render components only during development with the <DevOnly> component.

Nuxt provides the `<DevOnly>` component to render a component only during development.

The content will not be included in production builds.

```vue [app/pages/example.vue]
<template>
  <div>
    <Sidebar />
    <DevOnly>
      <!-- this component will only be rendered during development -->
      <LazyDebugBar />

      <!-- if you ever require to have a replacement during production -->
      <!-- be sure to test these using `nuxt preview` -->
      <template #fallback>
        <div><!-- empty div for flex.justify-between --></div>
      </template>
    </DevOnly>
  </div>
</template>
```

## Slots

- `#fallback`: if you ever require to have a replacement during production.

```vue
<template>
  <div>
    <Sidebar />
    <DevOnly>
      <!-- this component will only be rendered during development -->
      <LazyDebugBar />
      <!-- be sure to test these using `nuxt preview` -->
      <template #fallback>
        <div><!-- empty div for flex.justify-between --></div>
      </template>
    </DevOnly>
  </div>
</template>
```

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/components/dev-only.ts)

## Teleports

# <Teleport>

> The <Teleport> component teleports a component to a different location in the DOM.

<warning>

The `to` target of [`<Teleport>`](https://vuejs.org/guide/built-ins/teleport) expects a CSS selector string or an actual DOM node. Nuxt currently has SSR support for teleports to `#teleports` only, with client-side support for other targets using a `<ClientOnly>` wrapper.

</warning>

## Body Teleport

```vue
<template>
  <button @click="open = true">
    Open Modal
  </button>
  <Teleport to="#teleports">
    <div
      v-if="open"
      class="modal"
    >
      <p>Hello from the modal!</p>
      <button @click="open = false">
        Close
      </button>
    </div>
  </Teleport>
</template>
```

## Client-side Teleport

```vue
<template>
  <ClientOnly>
    <Teleport to="#some-selector">
      <!-- content -->
    </Teleport>
  </ClientOnly>
</template>
```

<link-example to="/docs/4.x/examples/advanced/teleport">



</link-example>