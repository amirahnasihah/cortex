# Nuxt - API - Utils


## Define Page Meta

# definePageMeta

> Define metadata for your page components.

`definePageMeta` is a compiler macro that you can use to set metadata for your **page** components located in the [`app/pages/`](/docs/4.x/directory-structure/app/pages) directory (unless [set otherwise](/docs/4.x/api/nuxt-config#pages)). This way you can set custom metadata for each static or dynamic route of your Nuxt application.

```vue [app/pages/some-page.vue]
<script setup lang="ts">
definePageMeta({
  layout: 'default',
})
</script>
```

<read-more to="/docs/4.x/directory-structure/app/pages#page-metadata">



</read-more>

## Type

```ts [Signature]
export function definePageMeta (meta: PageMeta): void

interface PageMeta {
  validate?: ((route: RouteLocationNormalized) => boolean | Promise<boolean> | Partial<NuxtError> | Promise<Partial<NuxtError>>)
  redirect?: RouteRecordRedirectOption
  name?: string
  path?: string
  props?: RouteRecordRaw['props']
  alias?: string | string[]
  groups?: string[]
  pageTransition?: boolean | TransitionProps
  layoutTransition?: boolean | TransitionProps
  viewTransition?: ViewTransitionPageOptions['enabled'] | ViewTransitionPageOptions
  key?: false | string | ((route: RouteLocationNormalizedLoaded) => string)
  keepalive?: boolean | KeepAliveProps
  layout?: false | LayoutKey | Ref<LayoutKey> | ComputedRef<LayoutKey> | { name?: LayoutKey | false, props?: Record<string, unknown> /* or the selected layout's props */ }
  middleware?: MiddlewareKey | NavigationGuard | Array<MiddlewareKey | NavigationGuard>
  scrollToTop?: boolean | ((to: RouteLocationNormalizedLoaded, from: RouteLocationNormalizedLoaded) => boolean)
  [key: string]: unknown
}
```

## Parameters

### `meta`

- **Type**: `PageMeta`<br />

An object accepting the following page metadata:<br />

**name**
  - **Type**: `string`<br />
  
  You may define a name for this page's route. By default, name is generated based on path inside the [`app/pages/` directory](/docs/4.x/directory-structure/app/pages).<br />

**path**
  - **Type**: `string`<br />
  
  You may define a [custom regular expression](/docs/4.x/api/utils/define-page-meta#using-a-custom-regular-expression) if you have a more complex pattern than can be expressed with the file name.<br />

**props**
  - **Type**: [`RouteRecordRaw['props']`](https://router.vuejs.org/guide/essentials/passing-props)<br />
  
  Allows accessing the route `params` as props passed to the page component.<br />

**alias**
  - **Type**: `string | string[]`<br />
  
  Aliases for the record. Allows defining extra paths that will behave like a copy of the record. Allows having paths shorthands like `/users/:id` and `/u/:id`. All `alias` and `path` values must share the same params.<br />

**groups**
  - **Type**: `string[]`<br />
  
  Route groups the page belongs to, based on the folder structure. Automatically populated for pages within [route groups](/docs/4.x/guide/directory-structure/app/pages#route-groups).<br />

**keepalive**
  - **Type**: `boolean` | [`KeepAliveProps`](https://vuejs.org/api/built-in-components#keepalive)<br />
  
  Set to `true` when you want to preserve page state across route changes or use the [`KeepAliveProps`](https://vuejs.org/api/built-in-components#keepalive) for a fine-grained control.<br />

**key**
  - **Type**: `false` | `string` | `((route: RouteLocationNormalizedLoaded) => string)`<br />
  
  Set `key` value when you need more control over when the `<NuxtPage>` component is re-rendered.<br />

**layout**
  - **Type**: `false` | `LayoutKey` | `Ref<LayoutKey>` | `ComputedRef<LayoutKey>` | `{ name?: LayoutKey | false; props?: Record<string, unknown> /* or the selected layout's props */ }`<br />
  
  Set a static or dynamic name of the layout for each route. This can be set to `false` in case the default layout needs to be disabled.<br />
  
  You can also pass an object with `name` and `props` to pass typed props to your layout component. When your layout defines props with `defineProps`, they will be fully typed in `definePageMeta`.<br />

**layoutTransition**
  - **Type**: `boolean` | [`TransitionProps`](https://vuejs.org/api/built-in-components#transition)<br />
  
  Set name of the transition to apply for current layout. You can also set this value to `false` to disable the layout transition.<br />

**middleware**
  - **Type**: `MiddlewareKey` | [`NavigationGuard`](https://router.vuejs.org/api/interfaces/navigationguard) | `Array<MiddlewareKey | NavigationGuard>`<br />
  
  Define anonymous or named middleware directly within `definePageMeta`. Learn more about [route middleware](/docs/4.x/directory-structure/app/middleware).<br />

**pageTransition**
  - **Type**: `boolean` | [`TransitionProps`](https://vuejs.org/api/built-in-components#transition)<br />
  
  Set name of the transition to apply for current page. You can also set this value to `false` to disable the page transition.<br />

**viewTransition**
  - **Type**: `boolean | 'always' | ViewTransitionPageOptions`<br />
  
  **Experimental feature, only available when enabled in your nuxt.config file**<br />
  
  
  Enable/disable View Transitions for the current page.
  If set to true, Nuxt will not apply the transition if the users browser matches `prefers-reduced-motion: reduce` (recommended). If set to `always`, Nuxt will always apply the transition.<br />
  
  You can also pass a `ViewTransitionPageOptions` object to configure [view transition types](/docs/4.x/getting-started/transitions#view-transition-types):
    - `enabled`: `boolean | 'always'` - enable/disable the transition
    - `types`: `string[] | (to, from) => string[]` - types applied to any transition involving this page
    - `toTypes`: `string[] | (to, from) => string[]` - types applied only when navigating **to** this page
    - `fromTypes`: `string[] | (to, from) => string[]` - types applied only when navigating **from** this page<br />

**redirect**
  - **Type**: [`RouteRecordRedirectOption`](https://router.vuejs.org/guide/essentials/redirect-and-alias)<br />
  
  Where to redirect if the route is directly matched. The redirection happens before any navigation guard and triggers a new navigation with the new target location.<br />

**validate**
  - **Type**: `(route: RouteLocationNormalized) => boolean | Promise<boolean> | Partial<NuxtError> | Promise<Partial<NuxtError>>`<br />
  
  Validate whether a given route can validly be rendered with this page. Return true if it is valid, or false if not. If another match can't be found, this will mean a 404. You can also directly return an object with `status`/`statusText` to respond immediately with an error (other matches will not be checked).<br />

**scrollToTop**
  - **Type**: `boolean | (to: RouteLocationNormalized, from: RouteLocationNormalized) => boolean`<br />
  
  Tell Nuxt to scroll to the top before rendering the page or not. Navigation is independent from rendering, so scroll behavior is always triggered even when the page doesn't re-render (e.g. when using a fixed [`key`](/docs/4.x/api/utils/define-page-meta#key)). Set `scrollToTop: false` to disable scrolling in such cases. If you want to overwrite the default scroll behavior of Nuxt, you can do so in `~/router.options.ts` (see [custom routing](/docs/4.x/guide/recipes/custom-routing#using-routeroptions)) for more info.<br />

**[key: string]**
  - **Type**: `any`<br />
  
  Apart from the above properties, you can also set **custom** metadata. You may wish to do so in a type-safe way by [augmenting the type of the `meta` object](/docs/4.x/directory-structure/app/pages/#typing-custom-metadata).

## Examples

### Basic Usage

The example below demonstrates:

- how `key` can be a function that returns a value;
- how `keepalive` property makes sure that the `<modal>` component is not cached when switching between multiple components;
- adding `pageType` as a custom property:

```vue [app/pages/some-page.vue]
<script setup lang="ts">
definePageMeta({
  key: route => route.fullPath,

  keepalive: {
    exclude: ['modal'],
  },

  pageType: 'Checkout',
})
</script>
```

### Defining Middleware

The example below shows how the middleware can be defined using a `function` directly within the `definePageMeta` or set as a `string` that matches the middleware file name located in the `app/middleware/` directory:

```vue [app/pages/some-page.vue]
<script setup lang="ts">
definePageMeta({
  // define middleware as a function
  middleware: [
    function (to, from) {
      const auth = useState('auth')

      if (!auth.value.authenticated) {
        return navigateTo('/login')
      }

      if (to.path !== '/checkout') {
        return navigateTo('/checkout')
      }
    },
  ],

  // ... or a string
  middleware: 'auth',

  // ... or multiple strings
  middleware: ['auth', 'another-named-middleware'],
})
</script>
```

### Using a Custom Regular Expression

A custom regular expression is a good way to resolve conflicts between overlapping routes, for instance:

The two routes "/test-category" and "/1234-post" match both `[postId]-[postSlug].vue` and `[categorySlug].vue` page routes.

To make sure that we are only matching digits (`\d+`) for `postId` in the `[postId]-[postSlug]` route, we can add the following to the `[postId]-[postSlug].vue` page template:

```vue [app/pages/[postId]-[postSlug].vue]
<script setup lang="ts">
definePageMeta({
  path: '/:postId(\\d+)-:postSlug',
})
</script>
```

For more examples see [Vue Router's Matching Syntax](https://router.vuejs.org/guide/essentials/route-matching-syntax).

### Defining Layout

You can define the layout that matches the layout's file name located (by default) in the [`app/layouts/` directory](/docs/4.x/directory-structure/app/layouts). You can also disable the layout by setting the `layout` to `false`:

```vue [app/pages/some-page.vue]
<script setup lang="ts">
definePageMeta({
  // set custom layout
  layout: 'admin',

  // ... or disable a default layout
  layout: false,
})
</script>
```

### Passing Props to a Layout

You can pass props to a layout by using the object syntax for `layout`. If your layout defines props with `defineProps`, the props will be fully typed.

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

Layout props set via `definePageMeta` are fully typed based on the layout's `defineProps`. You'll get autocomplete and type-checking in your editor.

</tip>

<read-more to="/docs/4.x/directory-structure/app/layouts#passing-props-to-layouts">



</read-more>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/pages/runtime/composables.ts)

## Navigate To

# navigateTo

> navigateTo is a helper function that programmatically navigates users.

## Usage

`navigateTo` is available on both server side and client side. It can be used within the [Nuxt context](/docs/4.x/guide/going-further/nuxt-app#the-nuxt-context), or directly, to perform page navigation.

<warning>

Make sure to always use `await` or `return` on result of `navigateTo` when calling it.

</warning>

<note>

`navigateTo` cannot be used within Nitro routes. To perform a server-side redirect in Nitro routes, use [`sendRedirect`](https://h3.dev/utils/response#redirectlocation-status-statustext) instead.

</note>

### Within a Vue Component

```vue
<script setup lang="ts">
// passing 'to' as a string
await navigateTo('/search')

// ... or as a route object
await navigateTo({ path: '/search' })

// ... or as a route object with query parameters
await navigateTo({
  path: '/search',
  query: {
    page: 1,
    sort: 'asc',
  },
})
</script>
```

### Within Route Middleware

```ts
export default defineNuxtRouteMiddleware((to, from) => {
  if (to.path !== '/search') {
    // setting the redirect code to '301 Moved Permanently'
    return navigateTo('/search', { redirectCode: 301 })
  }
})
```

When using `navigateTo` within route middleware, you must **return its result** to ensure the middleware execution flow works correctly.

For example, the following implementation **will not work as expected**:

```ts
export default defineNuxtRouteMiddleware((to, from) => {
  if (to.path !== '/search') {
    // ❌ This will not work as expected
    navigateTo('/search', { redirectCode: 301 })
    return
  }
})
```

In this case, `navigateTo` will be executed but not returned, which may lead to unexpected behavior.

<read-more to="/docs/4.x/directory-structure/app/middleware">



</read-more>

### Navigating to an External URL

The `external` parameter in `navigateTo` influences how navigating to URLs is handled:

- **Without external: true**:
  - Internal URLs navigate as expected.
  - External URLs throw an error.
- **With external: true**:
  - Internal URLs navigate with a full-page reload.
  - External URLs navigate as expected.

#### Example

```vue
<script setup lang="ts">
// will throw an error;
// navigating to an external URL is not allowed by default
await navigateTo('https://nuxt.com')

// will redirect successfully with the 'external' parameter set to 'true'
await navigateTo('https://nuxt.com', {
  external: true,
})
</script>
```

### Opening a Page in a New Tab

```vue
<script setup lang="ts">
// will open 'https://nuxt.com' in a new tab
await navigateTo('https://nuxt.com', {
  open: {
    target: '_blank',
    windowFeatures: {
      width: 500,
      height: 500,
    },
  },
})
</script>
```

## Type

```ts [Signature]
export function navigateTo (
  to: RouteLocationRaw | undefined | null,
  options?: NavigateToOptions,
): Promise<void | NavigationFailure | false> | false | void | RouteLocationRaw

interface NavigateToOptions {
  replace?: boolean
  redirectCode?: number
  external?: boolean
  open?: OpenOptions
}

type OpenOptions = {
  target: string
  windowFeatures?: OpenWindowFeatures
}

type OpenWindowFeatures = {
  popup?: boolean
  noopener?: boolean
  noreferrer?: boolean
} & XOR<{ width?: number }, { innerWidth?: number }>
  & XOR<{ height?: number }, { innerHeight?: number }>
  & XOR<{ left?: number }, { screenX?: number }>
  & XOR<{ top?: number }, { screenY?: number }>
```

## Parameters

### `to`

**Type**: [`RouteLocationRaw`](https://router.vuejs.org/api/interfaces/routelocationoptions) | `undefined` | `null`

**Default**: `'/'`

`to` can be a plain string or a route object to redirect to. When passed as `undefined` or `null`, it will default to `'/'`.

#### Example

```ts
// Passing the URL directly will redirect to the '/blog' page
await navigateTo('/blog')

// Using the route object, will redirect to the route with the name 'blog'
await navigateTo({ name: 'blog' })

// Redirects to the 'product' route while passing a parameter (id = 1) using the route object.
await navigateTo({ name: 'product', params: { id: 1 } })
```

### `options` (optional)

**Type**: `NavigateToOptions`

An object accepting the following properties:

- `replace`
  - **Type**: `boolean`
  - **Default**: `false`
  - By default, `navigateTo` pushes the given route into the Vue Router's instance on the client side.<br />
  
  This behavior can be changed by setting `replace` to `true`, to indicate that given route should be replaced.
- `redirectCode`
  - **Type**: `number`
  - **Default**: `302`
  - `navigateTo` redirects to the given path and sets the redirect code to [`302 Found`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/302) by default when the redirection takes place on the server side.<br />
  
  This default behavior can be modified by providing different `redirectCode`. Commonly, [`301 Moved Permanently`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/301) can be used for permanent redirections.
- `external`
  - **Type**: `boolean`
  - **Default**: `false`
  - Allows navigating to an external URL when set to `true`. Otherwise, `navigateTo` will throw an error, as external navigation is not allowed by default.
- `open`
  - **Type**: `OpenOptions`
  - Allows navigating to the URL using the [open()](https://developer.mozilla.org/en-US/docs/Web/API/Window/open) method of the window. This option is only applicable on the client side and will be ignored on the server side.<br />
  
  An object accepting the following properties:
  - `target`
    - **Type**: `string`
    - **Default**: `'_blank'`
    - A string, without whitespace, specifying the name of the browsing context the resource is being loaded into.
  - `windowFeatures`
    - **Type**: `OpenWindowFeatures`
    - An object accepting the following properties:<table>
    <thead>
      <tr>
        <th>
          Property
        </th>
        
        <th>
          Type
        </th>
        
        <th>
          Description
        </th>
      </tr>
    </thead>
    
    <tbody>
      <tr>
        <td>
          <code>
            popup
          </code>
        </td>
        
        <td>
          <code>
            boolean
          </code>
        </td>
        
        <td>
          Requests a minimal popup window instead of a new tab, with UI features decided by the browser.
        </td>
      </tr>
      
      <tr>
        <td>
          <code>
            width
          </code>
          
           or <code>
            innerWidth
          </code>
        </td>
        
        <td>
          <code>
            number
          </code>
        </td>
        
        <td>
          Specifies the content area's width (minimum 100 pixels), including scrollbars.
        </td>
      </tr>
      
      <tr>
        <td>
          <code>
            height
          </code>
          
           or <code>
            innerHeight
          </code>
        </td>
        
        <td>
          <code>
            number
          </code>
        </td>
        
        <td>
          Specifies the content area's height (minimum 100 pixels), including scrollbars.
        </td>
      </tr>
      
      <tr>
        <td>
          <code>
            left
          </code>
          
           or <code>
            screenX
          </code>
        </td>
        
        <td>
          <code>
            number
          </code>
        </td>
        
        <td>
          Sets the horizontal position of the new window relative to the left edge of the screen.
        </td>
      </tr>
      
      <tr>
        <td>
          <code>
            top
          </code>
          
           or <code>
            screenY
          </code>
        </td>
        
        <td>
          <code>
            number
          </code>
        </td>
        
        <td>
          Sets the vertical position of the new window relative to the top edge of the screen.
        </td>
      </tr>
      
      <tr>
        <td>
          <code>
            noopener
          </code>
        </td>
        
        <td>
          <code>
            boolean
          </code>
        </td>
        
        <td>
          Prevents the new window from accessing the originating window via <code>
            window.opener
          </code>
          
          .
        </td>
      </tr>
      
      <tr>
        <td>
          <code>
            noreferrer
          </code>
        </td>
        
        <td>
          <code>
            boolean
          </code>
        </td>
        
        <td>
          Prevents the Referer header from being sent and implicitly enables <code>
            noopener
          </code>
          
          .
        </td>
      </tr>
    </tbody>
    </table>
    
    <br />
    
    Refer to the [documentation](https://developer.mozilla.org/en-US/docs/Web/API/Window/open#windowfeatures) for more detailed information on the **windowFeatures** properties.

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts)

## Abort Navigation

# abortNavigation

> abortNavigation is a helper function that prevents navigation from taking place and throws an error if one is set as a parameter.

<warning>

`abortNavigation` is only usable inside a [route middleware handler](/docs/4.x/directory-structure/app/middleware).

</warning>

## Type

```ts [Signature]
export function abortNavigation (err?: Error | string): false
```

## Parameters

### `err`

- **Type**: [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) | `string`<br />

Optional error to be thrown by `abortNavigation`.

## Examples

The example below shows how you can use `abortNavigation` in a route middleware to prevent unauthorized route access:

```ts [app/middleware/auth.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  const user = useState('user')

  if (!user.value.isAuthorized) {
    return abortNavigation()
  }

  if (to.path !== '/edit-post') {
    return navigateTo('/edit-post')
  }
})
```

### `err` as a String

You can pass the error as a string:

```ts [app/middleware/auth.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  const user = useState('user')

  if (!user.value.isAuthorized) {
    return abortNavigation('Insufficient permissions.')
  }
})
```

### `err` as an Error Object

You can pass the error as an [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) object, e.g. caught by the `catch`-block:

```ts [app/middleware/auth.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  try {
    /* code that might throw an error */
  } catch (err) {
    return abortNavigation(err)
  }
})
```

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts)

## Add Route Middleware

# addRouteMiddleware

> addRouteMiddleware() is a helper function to dynamically add middleware in your application.

<note>

Route middleware are navigation guards stored in the [`app/middleware/`](/docs/4.x/directory-structure/app/middleware) directory of your Nuxt application (unless [set otherwise](/docs/4.x/api/nuxt-config#middleware)).

</note>

## Type

```ts
function addRouteMiddleware (name: string, middleware: RouteMiddleware, options?: AddRouteMiddlewareOptions): void
function addRouteMiddleware (middleware: RouteMiddleware): void

interface AddRouteMiddlewareOptions {
  global?: boolean
}
```

## Parameters

### `name`

- **Type:** `string` | `RouteMiddleware`

Can be either a string or a function of type `RouteMiddleware`. Function takes the next route `to` as the first argument and the current route `from` as the second argument, both of which are Vue route objects.

Learn more about available properties of [route objects](/docs/4.x/api/composables/use-route).

### `middleware`

- **Type:** `RouteMiddleware`

The second argument is a function of type `RouteMiddleware`. Same as above, it provides `to` and `from` route objects. It becomes optional if the first argument in `addRouteMiddleware()` is already passed as a function.

### `options`

- **Type:** `AddRouteMiddlewareOptions`

An optional `options` argument lets you set the value of `global` to `true` to indicate whether the router middleware is global or not (set to `false` by default).

## Examples

### Named Route Middleware

Named route middleware is defined by providing a string as the first argument and a function as the second:

```ts [app/plugins/my-plugin.ts]
export default defineNuxtPlugin(() => {
  addRouteMiddleware('named-middleware', () => {
    console.log('named middleware added in Nuxt plugin')
  })
})
```

When defined in a plugin, it overrides any existing middleware of the same name located in the `app/middleware/` directory.

### Global Route Middleware

Global route middleware can be defined in two ways:

- Pass a function directly as the first argument without a name. It will automatically be treated as global middleware and applied on every route change.```ts [app/plugins/my-plugin.ts]
export default defineNuxtPlugin(() => {
  addRouteMiddleware((to, from) => {
    console.log('anonymous global middleware that runs on every route change')
  })
})
```
- Set an optional, third argument `{ global: true }` to indicate whether the route middleware is global.```ts [app/plugins/my-plugin.ts]
export default defineNuxtPlugin(() => {
  addRouteMiddleware('global-middleware', (to, from) => {
    console.log('global middleware that runs on every route change')
  },
  { global: true },
  )
})
```

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts)

## Define Nuxt Route Middleware

# defineNuxtRouteMiddleware

> Create named route middleware using defineNuxtRouteMiddleware helper function.

Route middleware are stored in the [`app/middleware/`](/docs/4.x/directory-structure/app/middleware) of your Nuxt application (unless [set otherwise](/docs/4.x/api/nuxt-config#middleware)).

## Type

```ts [Signature]
export function defineNuxtRouteMiddleware (middleware: RouteMiddleware): RouteMiddleware

interface RouteMiddleware {
  (to: RouteLocationNormalized, from: RouteLocationNormalized): ReturnType<NavigationGuard>
}
```

## Parameters

### `middleware`

- **Type**: `RouteMiddleware`

A function that takes two Vue Router's route location objects as parameters: the next route `to` as the first, and the current route `from` as the second.

Learn more about available properties of `RouteLocationNormalized` in the **Vue Router docs**.

## Examples

### Showing Error Page

You can use route middleware to throw errors and show helpful error messages:

```ts [app/middleware/error.ts]
export default defineNuxtRouteMiddleware((to) => {
  if (to.params.id === '1') {
    throw createError({ status: 404, statusText: 'Page Not Found' })
  }
})
```

The above route middleware will redirect a user to the custom error page defined in the `~/error.vue` file, and expose the error message and code passed from the middleware.

### Redirection

Use [`useState`](/docs/4.x/api/composables/use-state) in combination with `navigateTo` helper function inside the route middleware to redirect users to different routes based on their authentication status:

```ts [app/middleware/auth.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  const auth = useState('auth')

  if (!auth.value.isAuthenticated) {
    return navigateTo('/login')
  }

  if (to.path !== '/dashboard') {
    return navigateTo('/dashboard')
  }
})
```

Both [navigateTo](/docs/4.x/api/utils/navigate-to) and [abortNavigation](/docs/4.x/api/utils/abort-navigation) are globally available helper functions that you can use inside `defineNuxtRouteMiddleware`.

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts)

## Define Route Rules

# defineRouteRules

> Define route rules for hybrid rendering at the page level.

<read-more icon="i-lucide-star" to="/docs/4.x/guide/going-further/experimental-features#inlinerouterules">

This feature is experimental and in order to use it you must enable the `experimental.inlineRouteRules` option in your `nuxt.config`.

</read-more>

## Usage

```vue [app/pages/index.vue]
<script setup lang="ts">
defineRouteRules({
  prerender: true,
})
</script>

<template>
  <h1>Hello world!</h1>
</template>
```

Will be translated to:

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  routeRules: {
    '/': { prerender: true },
  },
})
```

<note>

When running [`nuxt build`](/docs/4.x/api/commands/build), the home page will be pre-rendered in `.output/public/index.html` and statically served.

</note>

## Notes

- A rule defined in `~/pages/foo/bar.vue` will be applied to `/foo/bar` requests.
- A rule in `~/pages/foo/[id].vue` will be applied to `/foo/**` requests.

For more control, such as if you are using a custom `path` or `alias` set in the page's [`definePageMeta`](/docs/4.x/api/utils/define-page-meta), you should set `routeRules` directly within your `nuxt.config`.

<read-more icon="i-lucide-medal" to="/docs/4.x/guide/concepts/rendering#hybrid-rendering">

Read more about the `routeRules`.

</read-more>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/pages/runtime/composables.ts)

## Set Response Status

# setResponseStatus

> setResponseStatus sets the status (and optionally the statusText) of the response.

Nuxt provides composables and utilities for first-class server-side-rendering support.

`setResponseStatus` sets the status (and optionally the statusText) of the response.

<important>

`setResponseStatus` can only be called in the [Nuxt context](/docs/4.x/guide/going-further/nuxt-app#the-nuxt-context).

</important>

```ts
const event = useRequestEvent()

// event will be undefined in the browser
if (event) {
  // Set the status code to 404 for a custom 404 page
  setResponseStatus(event, 404)

  // Set the status message as well
  setResponseStatus(event, 404, 'Page Not Found')
}
```

<note>

In the browser, `setResponseStatus` will have no effect.

</note>

<read-more to="/docs/4.x/getting-started/error-handling">



</read-more>

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts)

## Set Page Layout

# setPageLayout

> setPageLayout allows you to dynamically change the layout of a page.

<important>

`setPageLayout` allows you to dynamically change the layout of a page. It relies on access to the Nuxt context and therefore can only be called within the [Nuxt context](/docs/4.x/guide/going-further/nuxt-app#the-nuxt-context).

</important>

```ts [app/middleware/custom-layout.ts]
export default defineNuxtRouteMiddleware((to) => {
  // Set the layout on the route you are navigating _to_
  setPageLayout('other')
})
```

## Passing Props to Layouts

You can pass props to the layout by providing an object as the second argument:

```ts [app/middleware/admin-layout.ts]
export default defineNuxtRouteMiddleware((to) => {
  setPageLayout('admin', {
    sidebar: true,
    title: 'Dashboard',
  })
})
```

The layout can then receive these props:

```vue [app/layouts/admin.vue]
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

<note>

If you choose to set the layout dynamically on the server side, you *must* do so before the layout is rendered by Vue (that is, within a plugin or route middleware) to avoid a hydration mismatch.

</note>

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts)

## Show Error

# showError

> Nuxt provides a quick and simple way to show a full screen error page if needed.

Within the [Nuxt context](/docs/4.x/guide/going-further/nuxt-app#the-nuxt-context) you can use `showError` to show an error.

**Parameters:**

- `error`: `string | Error | Partial<{ cause, data, message, name, stack, status, statusText }>`

```ts
showError('😱 Oh no, an error has been thrown.')
showError({
  status: 404,
  statusText: 'Page Not Found',
})
```

The error is set in the state using [`useError()`](/docs/4.x/api/composables/use-error) to create a reactive and SSR-friendly shared error state across components.

<tip>

`showError` calls the `app:error` hook.

</tip>

<read-more to="/docs/4.x/getting-started/error-handling">



</read-more>

<style>

html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/error.ts)

## Clear Error

# clearError

> The clearError composable clears all handled errors.

Within your pages, components, and plugins, you can use `clearError` to clear all errors and redirect the user.

**Parameters:**

- `options?: { redirect?: string }`

You can provide an optional path to redirect to (for example, if you want to navigate to a 'safe' page).

```ts
// Without redirect
clearError()

// With redirect
clearError({ redirect: '/homepage' })
```

Errors are set in state using [`useError()`](/docs/4.x/api/composables/use-error). The `clearError` composable will reset this state and calls the `app:error:cleared` hook with the provided options.

<read-more to="/docs/4.x/getting-started/error-handling">



</read-more>

<style>

html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/error.ts)

## Create Error

# createError

> Create an error object with additional metadata.

You can use this function to create an error object with additional metadata. It is usable in both the Vue and Nitro portions of your app, and is meant to be thrown.

## Parameters

- `err`: `string | { cause, data, message, name, stack, status, statusText, fatal }`

You can pass either a string or an object to the `createError` function. If you pass a string, it will be used as the error `message`, and the `status` will default to `500`. If you pass an object, you can set multiple properties of the error, such as `status`, `message`, and other error properties.

## In Vue App

If you throw an error created with `createError`:

- on server-side, it will trigger a full-screen error page which you can clear with `clearError`.
- on client-side, it will throw a non-fatal error for you to handle. If you need to trigger a full-screen error page, then you can do this by setting `fatal: true`.

### Example

```vue [app/pages/movies/[slug].vue]
<script setup lang="ts">
const route = useRoute()
const { data } = await useFetch(`/api/movies/${route.params.slug}`)
if (!data.value) {
  throw createError({ status: 404, statusText: 'Page Not Found' })
}
</script>
```

## In API Routes

Use `createError` to trigger error handling in server API routes.

### Example

```ts [server/api/error.ts]
export default eventHandler(() => {
  throw createError({
    status: 404,
    statusText: 'Page Not Found',
  })
})
```

In API routes, using `createError` by passing an object with a short `statusText` is recommended because it can be accessed on the client side. Otherwise, a `message` passed to `createError` on an API route will not propagate to the client. Alternatively, you can use the `data` property to pass data back to the client. In any case, always consider avoiding to put dynamic user input to the message to avoid potential security issues.

<read-more to="/docs/4.x/getting-started/error-handling">



</read-more>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/error.ts)

## Call Once

# callOnce

> Run a given function or block of code once during SSR or CSR.

<important>

This utility is available since [Nuxt v3.9](/blog/v3-9).

</important>

## Purpose

The `callOnce` function is designed to execute a given function or block of code only once during:

- server-side rendering but not hydration
- client-side navigation

This is useful for code that should be executed only once, such as logging an event or setting up a global state.

## Usage

The default mode of `callOnce` is to run code only once. For example, if the code runs on the server it won't run again on the client. It also won't run again if you `callOnce` more than once on the client, for example by navigating back to this page.

```vue [app/app.vue]
<script setup lang="ts">
const websiteConfig = useState('config')

await callOnce(async () => {
  console.log('This will only be logged once')
  websiteConfig.value = await $fetch('https://my-cms.com/api/website-config')
})
</script>
```

It is also possible to run on every navigation while still avoiding the initial server/client double load. For this, it is possible to use the `navigation` mode:

```vue [app/app.vue]
<script setup lang="ts">
const websiteConfig = useState('config')

await callOnce(async () => {
  console.log('This will only be logged once and then on every client side navigation')
  websiteConfig.value = await $fetch('https://my-cms.com/api/website-config')
}, { mode: 'navigation' })
</script>
```

<important>

`navigation` mode is available since [Nuxt v3.15](/blog/v3-15).

</important>

<tip to="/docs/4.x/getting-started/state-management#usage-with-pinia">

`callOnce` is useful in combination with the [Pinia module](/modules/pinia) to call store actions.

</tip>

<read-more to="/docs/4.x/getting-started/state-management">



</read-more>

<warning>

Note that `callOnce` doesn't return anything. You should use [`useAsyncData`](/docs/4.x/api/composables/use-async-data) or [`useFetch`](/docs/4.x/api/composables/use-fetch) if you want to do data fetching during SSR.

</warning>

<note>

`callOnce` is a composable meant to be called directly in a setup function, plugin, or route middleware, because it needs to add data to the Nuxt payload to avoid re-calling the function on the client when the page hydrates.

</note>

## Type

```ts [Signature]
export function callOnce (key?: string, fn?: (() => any | Promise<any>), options?: CallOnceOptions): Promise<void>
export function callOnce (fn?: (() => any | Promise<any>), options?: CallOnceOptions): Promise<void>

type CallOnceOptions = {
  /**
   * Execution mode for the callOnce function
   * @default 'render'
   */
  mode?: 'navigation' | 'render'
}
```

## Parameters

- `key`: A unique key ensuring that the code is run once. If you do not provide a key, then a key that is unique to the file and line number of the instance of `callOnce` will be generated for you.
- `fn`: The function to run once. It can be asynchronous.
- `options`: Setup the mode, either to re-execute on navigation (`navigation`) or just once for the lifetime of the app (`render`). Defaults to `render`.

  - `render`: Executes once during initial render (either SSR or CSR) - Default mode
  - `navigation`: Executes once during initial render and once per subsequent client-side navigation

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .s0grJ, html code.shiki .s0grJ{--shiki-light:#9C3EDA;--shiki-light-font-style:italic;--shiki-default:#9C3EDA;--shiki-default-font-style:italic;--shiki-dark:#C792EA;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/once.ts)

## Refresh Nuxt Data

# refreshNuxtData

> Refresh all or specific asyncData instances in Nuxt

`refreshNuxtData` is used to refetch all or specific `asyncData` instances, including those from [`useAsyncData`](/docs/4.x/api/composables/use-async-data), [`useLazyAsyncData`](/docs/4.x/api/composables/use-lazy-async-data), [`useFetch`](/docs/4.x/api/composables/use-fetch), and [`useLazyFetch`](/docs/4.x/api/composables/use-lazy-fetch).

<note>

If your component is cached by `<KeepAlive>` and enters a deactivated state, the `asyncData` inside the component will still be refetched until the component is unmounted.

</note>

## Type

```ts [Signature]
export function refreshNuxtData (keys?: string | string[])
```

## Parameters

- `keys`: A single string or an array of strings as `keys` that are used to fetch the data. This parameter is **optional**. All [`useAsyncData`](/docs/4.x/api/composables/use-async-data) and [`useFetch`](/docs/4.x/api/composables/use-fetch) keys are re-fetched when no `keys` are explicitly specified.

## Return Values

`refreshNuxtData` returns a promise, resolving when all or specific `asyncData` instances have been refreshed.

## Examples

### Refresh All Data

This example below refreshes all data being fetched using `useAsyncData` and `useFetch` in Nuxt application.

```vue [app/pages/some-page.vue]
<script setup lang="ts">
const refreshing = ref(false)

async function refreshAll () {
  refreshing.value = true
  try {
    await refreshNuxtData()
  } finally {
    refreshing.value = false
  }
}
</script>

<template>
  <div>
    <button
      :disabled="refreshing"
      @click="refreshAll"
    >
      Refetch All Data
    </button>
  </div>
</template>
```

### Refresh Specific Data

This example below refreshes only data where the key matches to `count` and `user`.

```vue [app/pages/some-page.vue]
<script setup lang="ts">
const refreshing = ref(false)

async function refresh () {
  refreshing.value = true
  try {
    // you could also pass an array of keys to refresh multiple data
    await refreshNuxtData(['count', 'user'])
  } finally {
    refreshing.value = false
  }
}
</script>

<template>
  <div v-if="refreshing">
    Loading
  </div>
  <button @click="refresh">
    Refresh
  </button>
</template>
```

<note>

If you have access to the `asyncData` instance, it is recommended to use its `refresh` or `execute` method as the preferred way to refetch the data.

</note>

<read-more to="/docs/4.x/getting-started/data-fetching">



</read-more>

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/asyncData.ts)

## Clear Nuxt Data

# clearNuxtData

> Delete cached data, error status and pending promises of useAsyncData and useFetch.

<note>

This method is useful if you want to invalidate the data fetching for another page.

</note>

## Type

```ts [Signature]
export function clearNuxtData (keys?: string | string[] | ((key: string) => boolean)): void
```

## Parameters

- `keys`: One or an array of keys that are used in [`useAsyncData`](/docs/4.x/api/composables/use-async-data) to delete their cached data. If no keys are provided, **all data** will be invalidated.

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/asyncData.ts)

## Clear Nuxt State

# clearNuxtState

> Delete the cached state of useState.

<note>

This method is useful if you want to invalidate the state of `useState`. You can also reset the state to its initial value by passing `{ reset: true }` as the second parameter.

</note>

## Type

```ts [Signature]
export function clearNuxtState (keys?: string | string[] | ((key: string) => boolean), opts?: ClearNuxtStateOptions): void
```

## Parameters

- `keys`: One or an array of keys that are used in [`useState`](/docs/4.x/api/composables/use-state) to delete their cached state. If no keys are provided, **all state** will be invalidated.
- `opts`: An options object to configure the clear behavior.

  - `reset`: When set to `true`, resets the state to the initial value provided by the `init` function of [`useState`](/docs/4.x/api/composables/use-state) instead of setting it to `undefined`. When not specified, defaults to the value of `experimental.defaults.useState.resetOnClear` in your Nuxt config (which is `true` with `compatibilityVersion: 5`).

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/state.ts)

## Refresh Cookie

# refreshCookie

> Refresh useCookie values manually when a cookie has changed

<important>

This utility is available since [Nuxt v3.10](/blog/v3-10).

</important>

## Purpose

The `refreshCookie` function is designed to refresh cookie value returned by `useCookie`.

This is useful for updating the `useCookie` ref when we know the new cookie value has been set in the browser.

## Usage

```vue [app/app.vue]
<script setup lang="ts">
const tokenCookie = useCookie('token')

const login = async (username, password) => {
  const token = await $fetch('/api/token', { /** ... */ }) // Sets `token` cookie on response
  refreshCookie('token')
}

const loggedIn = computed(() => !!tokenCookie.value)
</script>
```

<note to="/docs/4.x/guide/going-further/experimental-features#cookiestore">

Since [Nuxt v3.12.0](https://github.com/nuxt/nuxt/releases/tag/v3.12.0), the experimental `cookieStore` option is enabled by default. It automatically refreshes the `useCookie` value when cookies change in the browser.

</note>

## Type

```ts [Signature]
export function refreshCookie (name: string): void
```

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/cookie.ts)

## Reload Nuxt App

# reloadNuxtApp

> reloadNuxtApp will perform a hard reload of the page.

<note>

`reloadNuxtApp` will perform a hard reload of your app, re-requesting a page and its dependencies from the server.

</note>

By default, it will also save the current `state` of your app (that is, any state you could access with `useState`).

<read-more icon="i-lucide-star" to="/docs/4.x/guide/going-further/experimental-features#restorestate">

You can enable experimental restoration of this state by enabling the `experimental.restoreState` option in your `nuxt.config` file.

</read-more>

## Type

```ts [Signature]
export function reloadNuxtApp (options?: ReloadNuxtAppOptions)

interface ReloadNuxtAppOptions {
  ttl?: number
  force?: boolean
  path?: string
  persistState?: boolean
}
```

### `options` (optional)

**Type**: `ReloadNuxtAppOptions`

An object accepting the following properties:

- `path` (optional)<br />

**Type**: `string`<br />

**Default**: `window.location.pathname`<br />

The path to reload (defaulting to the current path). If this is different from the current window location it
will trigger a navigation and add an entry in the browser history.
- `ttl` (optional)<br />

**Type**: `number`<br />

**Default**: `10000`<br />

The number of milliseconds in which to ignore future reload requests. If called again within this time period,
`reloadNuxtApp` will not reload your app to avoid reload loops.
- `force` (optional)<br />

**Type**: `boolean`<br />

**Default**: `false`<br />

This option allows bypassing reload loop protection entirely, forcing a reload even if one has occurred within
the previously specified TTL.
- `persistState` (optional)<br />

**Type**: `boolean`<br />

**Default**: `false`<br />

Whether to dump the current Nuxt state to sessionStorage (as `nuxt:reload:state`). By default this will have no
effect on reload unless `experimental.restoreState` is also set, or unless you handle restoring the state yourself.

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/chunk.ts)

## On Nuxt Ready

# onNuxtReady

> The onNuxtReady composable allows running a callback after your app has finished initializing.

<important>

`onNuxtReady` only runs on the client-side. <br />


It is ideal for running code that should not block the initial rendering of your app.

</important>

```ts [app/plugins/ready.client.ts]
export default defineNuxtPlugin(() => {
  onNuxtReady(async () => {
    const myAnalyticsLibrary = await import('my-big-analytics-library')
    // do something with myAnalyticsLibrary
  })
})
```

It is 'safe' to run even after your app has initialized. In this case, then the code will be registered to run in the next idle callback.

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ready.ts)

## On Before Route Leave

# onBeforeRouteLeave

> The onBeforeRouteLeave composable allows registering a route guard within a component.

<read-more icon="i-simple-icons-vuedotjs" target="_blank" title="Vue Router Docs" to="https://router.vuejs.org/api/functions/onbeforerouteleave">



</read-more>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts)

## On Before Route Update

# onBeforeRouteUpdate

> The onBeforeRouteUpdate composable allows registering a route guard within a component.

<read-more icon="i-simple-icons-vuedotjs" target="_blank" title="Vue Router Docs" to="https://router.vuejs.org/api/functions/onbeforerouteupdate">



</read-more>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts)

## Prefetch Components

# prefetchComponents

> Nuxt provides utilities to give you control over prefetching components.

Prefetching component downloads the code in the background, this is based on the assumption that the component will likely be used for rendering, enabling the component to load instantly if and when the user requests it. The component is downloaded and cached for anticipated future use without the user making an explicit request for it.

Use `prefetchComponents` to manually prefetch individual components that have been registered globally in your Nuxt app. By default Nuxt registers these as async components. You must use the Pascal-cased version of the component name.

```ts
await prefetchComponents('MyGlobalComponent')

await prefetchComponents(['MyGlobalComponent1', 'MyGlobalComponent2'])
```

<note>

Current implementation behaves exactly the same as [`preloadComponents`](/docs/4.x/api/utils/preload-components) by preloading components instead of just prefetching we are working to improve this behavior.

</note>

<note>

On server, `prefetchComponents` will have no effect.

</note>

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/preload.ts)

## Preload Components

# preloadComponents

> Nuxt provides utilities to give you control over preloading components.

Preloading components loads components that your page will need very soon, which you want to start loading early in rendering lifecycle. This ensures they are available earlier and are less likely to block the page's render, improving performance.

Use `preloadComponents` to manually preload individual components that have been registered globally in your Nuxt app. By default Nuxt registers these as async components. You must use the Pascal-cased version of the component name.

```ts
await preloadComponents('MyGlobalComponent')

await preloadComponents(['MyGlobalComponent1', 'MyGlobalComponent2'])
```

<note>

On server, `preloadComponents` will have no effect.

</note>

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/preload.ts)

## Preload Route Components

# preloadRouteComponents

> preloadRouteComponents allows you to manually preload individual pages in your Nuxt app.

Preloading routes loads the components of a given route that the user might navigate to in future. This ensures that the components are available earlier and less likely to block the navigation, improving performance.

<tip icon="i-lucide-rocket">

Nuxt already automatically preloads the necessary routes if you're using the `NuxtLink` component.

</tip>

<read-more to="/docs/4.x/api/components/nuxt-link">



</read-more>

## Example

Preload a route when using `navigateTo`.

```ts
// we don't await this async function, to avoid blocking rendering
// this component's setup function
preloadRouteComponents('/dashboard')

const submit = async () => {
  const results = await $fetch('/api/authentication')

  if (results.token) {
    await navigateTo('/dashboard')
  }
}
```

<read-more to="/docs/4.x/api/utils/navigate-to">



</read-more>

<note>

On server, `preloadRouteComponents` will have no effect.

</note>

<style>

html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/preload.ts)

## Prerender Routes

# prerenderRoutes

> prerenderRoutes hints to Nitro to prerender an additional route.

When prerendering, you can hint to Nitro to prerender additional paths, even if their URLs do not show up in the HTML of the generated page.

<important>

`prerenderRoutes` can only be called within the [Nuxt context](/docs/4.x/guide/going-further/nuxt-app#the-nuxt-context).

</important>

<note>

`prerenderRoutes` has to be executed during prerendering. If the `prerenderRoutes` is used in dynamic pages/routes which are not prerendered, then it will not be executed.

</note>

```ts
const route = useRoute()

prerenderRoutes('/')
prerenderRoutes(['/', '/about'])
```

<note>

In the browser, or if called outside prerendering, `prerenderRoutes` will have no effect.

</note>

You can even prerender API routes which is particularly useful for full statically generated sites (SSG) because you can then `$fetch` data as if you have an available server!

```ts
prerenderRoutes('/api/content/article/name-of-article')

// Somewhere later in App
const articleContent = await $fetch('/api/content/article/name-of-article', {
  responseType: 'json',
})
```

<warning>

Prerendered API routes in production may not return the expected response headers, depending on the provider you deploy to. For example, a JSON response might be served with an `application/octet-stream` content type.
Always manually set `responseType` when fetching prerendered API routes.

</warning>

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts)

## Define Nuxt Component

# defineNuxtComponent

> defineNuxtComponent() is a helper function for defining type safe components with Options API.

<note>

`defineNuxtComponent()` is a helper function for defining type safe Vue components using options API similar to [`defineComponent()`](https://vuejs.org/api/general#definecomponent). `defineNuxtComponent()` wrapper also adds support for `asyncData` and `head` component options.

</note>

<note>

Using `<script setup lang="ts">` is the recommended way of declaring Vue components in Nuxt.

</note>

<read-more to="/docs/getting-started/data-fetching">



</read-more>

## `asyncData()`

If you choose not to use `setup()` in your app, you can use the `asyncData()` method within your component definition:

```vue [app/pages/index.vue]
<script lang="ts">
export default defineNuxtComponent({
  asyncData () {
    return {
      data: {
        greetings: 'hello world!',
      },
    }
  },
})
</script>
```

## `head()`

If you choose not to use `setup()` in your app, you can use the `head()` method within your component definition:

```vue [app/pages/index.vue]
<script lang="ts">
export default defineNuxtComponent({
  head (nuxtApp) {
    return {
      title: 'My site',
    }
  },
})
</script>
```

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/component.ts)

## Define Nuxt Plugin

# defineNuxtPlugin

> defineNuxtPlugin() is a helper function for creating Nuxt plugins.

`defineNuxtPlugin` is a helper function for creating Nuxt plugins with enhanced functionality and type safety. This utility normalizes different plugin formats into a consistent structure that works seamlessly within Nuxt's plugin system.

```ts [plugins/hello.ts]twoslash
export default defineNuxtPlugin((nuxtApp) => {
  // Doing something with nuxtApp
})
```

<read-more to="/docs/4.x/directory-structure/app/plugins#creating-plugins">



</read-more>

## Type

```ts [Signature]
export function defineNuxtPlugin<T extends Record<string, unknown>> (plugin: Plugin<T> | ObjectPlugin<T>): Plugin<T> & ObjectPlugin<T>

type Plugin<T> = (nuxt: NuxtApp) => Promise<void> | Promise<{ provide?: T }> | void | { provide?: T }

interface ObjectPlugin<T> {
  name?: string
  enforce?: 'pre' | 'default' | 'post'
  dependsOn?: string[]
  order?: number
  parallel?: boolean
  setup?: Plugin<T>
  hooks?: Partial<RuntimeNuxtHooks>
  env?: {
    islands?: boolean
  }
}
```

## Parameters

**plugin**: A plugin can be defined in two ways:

1. **Function Plugin**: A function that receives the [`NuxtApp`](/docs/4.x/guide/going-further/internals#the-nuxtapp-interface) instance and can return a promise with a potential object with a [`provide`](/docs/4.x/directory-structure/app/plugins#providing-helpers) property if you want to provide a helper on [`NuxtApp`](/docs/4.x/guide/going-further/internals#the-nuxtapp-interface) instance.
2. **Object Plugin**: An object that can include various properties to configure the plugin's behavior, such as `name`, `enforce`, `dependsOn`, `order`, `parallel`, `setup`, `hooks`, and `env`.

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        name
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Optional name for the plugin, useful for debugging and dependency management.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        enforce
      </code>
    </td>
    
    <td>
      <code>
        'pre'
      </code>
      
       | <code>
        'default'
      </code>
      
       | <code>
        'post'
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Controls when the plugin runs relative to other plugins.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        dependsOn
      </code>
    </td>
    
    <td>
      <code>
        string[]
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Array of plugin names this plugin depends on. Ensures proper execution order.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        order
      </code>
    </td>
    
    <td>
      <code>
        number
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      This allows more granular control over plugin order and should only be used by advanced users. <strong>
        It overrides the value of <code>
          enforce
        </code>
        
         and is used to sort plugins.
      </strong>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        parallel
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Whether to execute the plugin in parallel with other parallel plugins.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setup
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          Plugin
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          T
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      The main plugin function, equivalent to a function plugin.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        hooks
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          Partial
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          RuntimeNuxtHooks
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Nuxt app runtime hooks to register directly.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        env
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          {
        </span>
        
        <span class="sZSNi">
          islands
        </span>
        
        <span class="sDfIl">
          ?:
        </span>
        
        <span class="sZSNi">
          boolean
        </span>
        
        <span class="sDfIl">
          }
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Set this value to <code>
        false
      </code>
      
       if you don't want the plugin to run when rendering server-only or island components.
    </td>
  </tr>
</tbody>
</table>

<video-accordion title="Watch a video from Alexander Lichter about the Object Syntax for Nuxt plugins" video-id="2aXZyXB1QGQ">



</video-accordion>

## Examples

### Basic Usage

The example below demonstrates a simple plugin that adds global functionality:

```ts [plugins/hello.ts]twoslash
export default defineNuxtPlugin((nuxtApp) => {
  // Add a global method
  return {
    provide: {
      hello: (name: string) => `Hello ${name}!`,
    },
  }
})
```

### Object Syntax Plugin

The example below shows the object syntax with advanced configuration:

```ts [plugins/advanced.ts]twoslash
export default defineNuxtPlugin({
  name: 'my-plugin',
  enforce: 'pre',
  async setup (nuxtApp) {
    // Plugin setup logic
    const data = await $fetch('/api/config')

    return {
      provide: {
        config: data,
      },
    }
  },
  hooks: {
    'app:created' () {
      console.log('App created!')
    },
  },
})
```

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/nuxt.ts)

## Update App Config

# updateAppConfig

> Update the App Config at runtime.

<note>

Updates the [`app.config`](/docs/4.x/directory-structure/app/app-config) using deep assignment. Existing (nested) properties will be preserved.

</note>

## Usage

```js
import { updateAppConfig, useAppConfig } from '#imports'

const appConfig = useAppConfig() // { foo: 'bar' }

const newAppConfig = { foo: 'baz' }
updateAppConfig(newAppConfig)

console.log(appConfig) // { foo: 'baz' }
```

<read-more to="/docs/4.x/directory-structure/app/app-config">



</read-more>

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/config.ts)

## Dollarfetch

# $fetch

> Nuxt uses ofetch to expose globally the $fetch helper for making HTTP requests.

Nuxt uses [ofetch](https://github.com/unjs/ofetch) to expose globally the `$fetch` helper for making HTTP requests within your Vue app or API routes.

<tip icon="i-lucide-rocket">

During server-side rendering, calling `$fetch` to fetch your internal [API routes](/docs/4.x/directory-structure/server) will directly call the relevant function (emulating the request), **saving an additional API call**.

</tip>

<note color="blue" icon="i-lucide-info">

Using `$fetch` in components without wrapping it with [`useAsyncData`](/docs/4.x/api/composables/use-async-data) causes fetching the data twice: initially on the server, then again on the client-side during hydration, because `$fetch` does not transfer state from the server to the client. Thus, the fetch will be executed on both sides because the client has to get the data again.

</note>

## Usage

We recommend using [`useFetch`](/docs/4.x/api/composables/use-fetch) or [`useAsyncData`](/docs/4.x/api/composables/use-async-data) + `$fetch` to prevent double data fetching when fetching the component data.

```vue [app/app.vue]
<script setup lang="ts">
// During SSR data is fetched twice, once on the server and once on the client.
const dataTwice = await $fetch('/api/item')

// During SSR data is fetched only on the server side and transferred to the client.
const { data } = await useAsyncData('item', () => $fetch('/api/item'))

// You can also useFetch as shortcut of useAsyncData + $fetch
const { data } = await useFetch('/api/item')
</script>
```

<read-more to="/docs/4.x/getting-started/data-fetching">



</read-more>

You can use `$fetch` in any methods that are executed only on client-side.

```vue [app/pages/contact.vue]
<script setup lang="ts">
async function contactForm () {
  await $fetch('/api/contact', {
    method: 'POST',
    body: { hello: 'world' },
  })
}
</script>

<template>
  <button @click="contactForm">
    Contact
  </button>
</template>
```

<tip>

`$fetch` is the preferred way to make HTTP calls in Nuxt instead of [@nuxt/http](https://github.com/nuxt/http) and [@nuxtjs/axios](https://github.com/nuxt-community/axios-module) that are made for Nuxt 2.

</tip>

<note>

If you use `$fetch` to call an (external) HTTPS URL with a self-signed certificate in development, you will need to set `NODE_TLS_REJECT_UNAUTHORIZED=0` in your environment.

</note>

### Passing Headers and Cookies

When we call `$fetch` in the browser, user headers like `cookie` will be directly sent to the API.

However, during Server-Side Rendering, due to security risks such as **Server-Side Request Forgery (SSRF)** or **Authentication Misuse**, the `$fetch` wouldn't include the user's browser cookies, nor pass on cookies from the fetch response.

<code-group>

```vue [app/pages/index.vue]
<script setup lang="ts">
// This will NOT forward headers or cookies during SSR
const { data } = await useAsyncData(() => $fetch('/api/cookies'))
</script>
```

```ts [server/api/cookies.ts]
export default defineEventHandler((event) => {
  const foo = getCookie(event, 'foo')
  // ... Do something with the cookie
})
```

</code-group>

If you need to forward headers and cookies on the server, you must manually pass them:

```vue [app/pages/index.vue]
<script setup lang="ts">
// This will forward the user's headers and cookies to `/api/cookies`
const requestFetch = useRequestFetch()
const { data } = await useAsyncData(() => requestFetch('/api/cookies'))
</script>
```

However, when calling `useFetch` with a relative URL on the server, Nuxt will use [`useRequestFetch`](/docs/4.x/api/composables/use-request-fetch) to proxy headers and cookies (with the exception of headers not meant to be forwarded, like `host`).

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/entry.ts)

## Define Lazy Hydration Component

# defineLazyHydrationComponent

> Define a lazy hydration component with a specific strategy.

`defineLazyHydrationComponent` is a compiler macro that helps you create a component with a specific lazy hydration strategy. Lazy hydration defers hydration until components become visible or until the browser has completed more critical tasks. This can significantly reduce the initial performance cost, especially for non-essential components.

## Usage

### Visibility Strategy

Hydrates the component when it becomes visible in the viewport.

```vue
<script setup lang="ts">
const LazyHydrationMyComponent = defineLazyHydrationComponent(
  'visible',
  () => import('./components/MyComponent.vue'),
)
</script>

<template>
  <div>
    <!--
      Hydration will be triggered when
      the element(s) is 100px away from entering the viewport.
    -->
    <LazyHydrationMyComponent :hydrate-on-visible="{ rootMargin: '100px' }" />
  </div>
</template>
```

The `hydrateOnVisible` prop is optional. You can pass an object to customize the behavior of the `IntersectionObserver` under the hood.

<read-more title="IntersectionObserver options" to="https://developer.mozilla.org/en-US/docs/Web/API/IntersectionObserver/IntersectionObserver">

Read more about the options for `hydrate-on-visible`.

</read-more>

<note>

Under the hood, this uses Vue's built-in [`hydrateOnVisible` strategy](https://vuejs.org/guide/components/async#hydrate-on-visible).

</note>

### Idle Strategy

Hydrates the component when the browser is idle. This is suitable if you need the component to load as soon as possible, but not block the critical rendering path.

```vue
<script setup lang="ts">
const LazyHydrationMyComponent = defineLazyHydrationComponent(
  'idle',
  () => import('./components/MyComponent.vue'),
)
</script>

<template>
  <div>
    <!-- Hydration will be triggered when the browser is idle or after 2000ms. -->
    <LazyHydrationMyComponent :hydrate-on-idle="2000" />
  </div>
</template>
```

The `hydrateOnIdle` prop is optional. You can pass a positive number to specify the maximum timeout.

Idle strategy is for components that can be hydrated when the browser is idle.

<note>

Under the hood, this uses Vue's built-in [`hydrateOnIdle` strategy](https://vuejs.org/guide/components/async#hydrate-on-idle).

</note>

### Interaction Strategy

Hydrates the component after a specified interaction (e.g., click, mouseover).

```vue
<script setup lang="ts">
const LazyHydrationMyComponent = defineLazyHydrationComponent(
  'interaction',
  () => import('./components/MyComponent.vue'),
)
</script>

<template>
  <div>
    <!--
      Hydration will be triggered when
      the element(s) is hovered over by the pointer.
    -->
    <LazyHydrationMyComponent hydrate-on-interaction="mouseover" />
  </div>
</template>
```

The `hydrateOnInteraction` prop is optional. If you do not pass an event or a list of events, it defaults to hydrating on `pointerenter`, `click`, and `focus`.

<note>

Under the hood, this uses Vue's built-in [`hydrateOnInteraction` strategy](https://vuejs.org/guide/components/async#hydrate-on-interaction).

</note>

### Media Query Strategy

Hydrates the component when the window matches a media query.

```vue
<script setup lang="ts">
const LazyHydrationMyComponent = defineLazyHydrationComponent(
  'mediaQuery',
  () => import('./components/MyComponent.vue'),
)
</script>

<template>
  <div>
    <!--
      Hydration will be triggered when
      the window width is greater than or equal to 768px.
    -->
    <LazyHydrationMyComponent hydrate-on-media-query="(min-width: 768px)" />
  </div>
</template>
```

<note>

Under the hood, this uses Vue's built-in [`hydrateOnMediaQuery` strategy](https://vuejs.org/guide/components/async#hydrate-on-media-query).

</note>

### Time Strategy

Hydrates the component after a specified delay (in milliseconds).

```vue
<script setup lang="ts">
const LazyHydrationMyComponent = defineLazyHydrationComponent(
  'time',
  () => import('./components/MyComponent.vue'),
)
</script>

<template>
  <div>
    <!-- Hydration is triggered after 1000ms. -->
    <LazyHydrationMyComponent :hydrate-after="1000" />
  </div>
</template>
```

Time strategy is for components that can wait a specific amount of time.

### If Strategy

Hydrates the component based on a boolean condition.

```vue
<script setup lang="ts">
const LazyHydrationMyComponent = defineLazyHydrationComponent(
  'if',
  () => import('./components/MyComponent.vue'),
)

const isReady = ref(false)

function myFunction () {
  // Trigger custom hydration strategy...
  isReady.value = true
}
</script>

<template>
  <div>
    <!-- Hydration is triggered when isReady becomes true. -->
    <LazyHydrationMyComponent :hydrate-when="isReady" />
  </div>
</template>
```

If strategy is best for components that might not always need to be hydrated.

### Never Hydrate

Never hydrates the component.

```vue
<script setup lang="ts">
const LazyHydrationMyComponent = defineLazyHydrationComponent(
  'never',
  () => import('./components/MyComponent.vue'),
)
</script>

<template>
  <div>
    <!-- This component will never be hydrated by Vue. -->
    <LazyHydrationMyComponent />
  </div>
</template>
```

### Listening to Hydration Events

All delayed hydration components emit a `@hydrated` event when they are hydrated.

```vue
<script setup lang="ts">
const LazyHydrationMyComponent = defineLazyHydrationComponent(
  'visible',
  () => import('./components/MyComponent.vue'),
)

function onHydrate () {
  console.log('Component has been hydrated!')
}
</script>

<template>
  <div>
    <LazyHydrationMyComponent
      :hydrate-on-visible="{ rootMargin: '100px' }"
      @hydrated="onHydrated"
    />
  </div>
</template>
```

## Parameters

<warning>

To ensure that the compiler correctly recognizes this macro, avoid using external variables. The following approach will prevent the macro from being properly recognized:

```vue
<script setup lang="ts">
const strategy = 'visible'
const source = () => import('./components/MyComponent.vue')
const LazyHydrationMyComponent = defineLazyHydrationComponent(strategy, source)
</script>
```

</warning>

### `strategy`

- **Type**: `'visible' | 'idle' | 'interaction' | 'mediaQuery' | 'if' | 'time' | 'never'`
- **Required**: `true`

<table>
<thead>
  <tr>
    <th>
      Strategy
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        visible
      </code>
    </td>
    
    <td>
      Hydrates when the component becomes visible in the viewport.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        idle
      </code>
    </td>
    
    <td>
      Hydrates when the browser is idle or after a delay.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        interaction
      </code>
    </td>
    
    <td>
      Hydrates upon user interaction (e.g., click, hover).
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        mediaQuery
      </code>
    </td>
    
    <td>
      Hydrates when the specified media query condition is met.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        if
      </code>
    </td>
    
    <td>
      Hydrates when a specified boolean condition is met.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        time
      </code>
    </td>
    
    <td>
      Hydrates after a specified time delay.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        never
      </code>
    </td>
    
    <td>
      Prevents Vue from hydrating the component.
    </td>
  </tr>
</tbody>
</table>

### `source`

- **Type**: `() => Promise<Component>`
- **Required**: `true`

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/components/plugins/lazy-hydration-macro-transform.ts)