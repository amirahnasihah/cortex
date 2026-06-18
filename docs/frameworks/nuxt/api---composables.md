# Nuxt - API - Composables


## Use Async Data

# useAsyncData

> useAsyncData provides access to data that resolves asynchronously in an SSR-friendly composable.

Within your pages, components, and plugins you can use useAsyncData to get access to data that resolves asynchronously.

<note>

[`useAsyncData`](/docs/4.x/api/composables/use-async-data) is a composable meant to be called directly in the [Nuxt context](/docs/4.x/guide/going-further/nuxt-app#the-nuxt-context). It returns reactive composables and handles adding responses to the Nuxt payload so they can be passed from server to client **without re-fetching the data on client side** when the page hydrates.

</note>

## Usage

```vue [app/pages/index.vue]
<script setup lang="ts">
const { data, status, pending, error, refresh, clear } = await useAsyncData(
  'mountains',
  (_nuxtApp, { signal }) => $fetch('https://api.nuxtjs.dev/mountains', { signal }),
)
</script>
```

<tip to="/docs/4.x/guide/recipes/custom-usefetch#custom-usefetch-with-createusefetch">

Need a custom `useAsyncData` with pre-defined defaults? Use `createUseAsyncData` to create a fully typed custom composable. See the [custom useFetch recipe](/docs/4.x/guide/recipes/custom-usefetch) for details.

</tip>

<note>

`data`, `status`, `pending` and `error` are Vue refs and they should be accessed with `.value` when used within the `<script setup>`, while `refresh`/`execute` and `clear` are plain functions.

</note>

### Watch Params

The built-in `watch` option allows automatically rerunning the fetcher function when any changes are detected.

```vue [app/pages/index.vue]
<script setup lang="ts">
const page = ref(1)
const { data: posts } = await useAsyncData(
  'posts',
  (_nuxtApp, { signal }) => $fetch('https://fakeApi.com/posts', {
    params: {
      page: page.value,
    },
    signal,
  }), {
    watch: [page],
  },
)
</script>
```

### Reactive Keys

You can use a computed ref, plain ref or a getter function as the key, allowing for dynamic data fetching that automatically updates when the key changes:

```vue [app/pages/[id].vue]
<script setup lang="ts">
const route = useRoute()
const userId = computed(() => `user-${route.params.id}`)

// When the route changes and userId updates, the data will be automatically refetched
const { data: user } = useAsyncData(
  userId,
  () => fetchUserById(route.params.id),
)
</script>
```

### Make your `handler` abortable

You can make your `handler` function abortable by using the `signal` provided in the second argument. This is useful for cancelling requests when they are no longer needed, such as when a user navigates away from a page. `$fetch` natively supports abort signals.

```ts
const { data, error } = await useAsyncData(
  'users',
  (_nuxtApp, { signal }) => $fetch('/api/users', { signal }),
)

refresh() // will actually cancel the $fetch request (if dedupe: cancel)
refresh() // will actually cancel the $fetch request (if dedupe: cancel)
refresh()

clear() // will cancel the latest pending handler
```

You can also pass an `AbortSignal` to the `refresh`/`execute` function to cancel individual requests manually.

```ts
const { refresh } = await useAsyncData(
  'users',
  (_nuxtApp, { signal }) => $fetch('/api/users', { signal }),
)
let abortController: AbortController | undefined

function handleUserAction () {
  abortController = new AbortController()
  refresh({ signal: abortController.signal })
}

function handleCancel () {
  abortController?.abort() // aborts the ongoing refresh request
}
```

If your `handler` function does not support abort signals, you can implement your own abort logic using the `signal` provided.

```ts
const { data, error } = await useAsyncData(
  'users',
  (_nuxtApp, { signal }) => {
    return new Promise((resolve, reject) => {
      signal?.addEventListener('abort', () => {
        reject(new Error('Request aborted'))
      })
      return Promise.resolve(callback.call(this, yourHandler)).then(resolve, reject)
    })
  },
)
```

The handler signal will be aborted when:

- A new request is made with `dedupe: 'cancel'`
- The `clear` function is called
- The `options.timeout` duration is exceeded

<warning>

[`useAsyncData`](/docs/4.x/api/composables/use-async-data) is a reserved function name transformed by the compiler, so you should not name your own function [`useAsyncData`](/docs/4.x/api/composables/use-async-data).

</warning>

<read-more to="/docs/4.x/getting-started/data-fetching#useasyncdata">



</read-more>

## Params

- `key`: a unique key to ensure that data fetching can be properly de-duplicated across requests. If you do not provide a key, then a key that is unique to the file name and line number of the instance of `useAsyncData` will be generated for you.
- `handler`: an asynchronous function that must return a truthy value (for example, it should not be `undefined` or `null`) or the request may be duplicated on the client side.
<warning>

The `handler` function should be **side-effect free** to ensure predictable behavior during SSR and CSR hydration. If you need to trigger side effects, use the [`callOnce`](/docs/4.x/api/utils/call-once) utility to do so.

</warning>
- `options`:

  - `server`: whether to fetch the data on the server (defaults to `true`)
  - `lazy`: whether to resolve the async function after loading the route, instead of blocking client-side navigation (defaults to `false`)
  - `immediate`: when set to `false`, will prevent the request from firing immediately. (defaults to `true`)
  - `default`: a factory function to set the default value of the `data`, before the async function resolves - useful with the `lazy: true` or `immediate: false` option
  - `transform`: a function that can be used to alter `handler` function result after resolving
  - `getCachedData`: Provide a function which returns cached data. An `undefined` return value will trigger a fetch. By default, this is:
  ```ts
  const getDefaultCachedData = (key, nuxtApp, ctx) => nuxtApp.isHydrating
    ? nuxtApp.payload.data[key]
    : nuxtApp.static.data[key]
  ```
  
  
  Which only caches data when `experimental.payloadExtraction` of `nuxt.config` is enabled.
  - `pick`: only pick specified keys in this array from the `handler` function result
  - `watch`: watch reactive sources to auto-refresh
  - `deep`: return data in a deep ref object. It is `false` by default to return data in a shallow ref object, which can improve performance if your data does not need to be deeply reactive.
  - `dedupe`: avoid fetching same key more than once at a time (defaults to `cancel`). Possible options:
  
    - `cancel` - cancels existing requests when a new one is made
    - `defer` - does not make new requests at all if there is a pending request
  - `timeout` - a number in milliseconds to wait before timing out the request (defaults to `undefined`, which means no timeout)

<note>

Under the hood, `lazy: false` uses `<Suspense>` to block the loading of the route before the data has been fetched. Consider using `lazy: true` and implementing a loading state instead for a snappier user experience.

</note>

<read-more to="/docs/4.x/api/composables/use-lazy-async-data">

You can use `useLazyAsyncData` to have the same behavior as `lazy: true` with `useAsyncData`.

</read-more>

<video-accordion title="Watch a video from Alexander Lichter about client-side caching with getCachedData" video-id="aQPR0xn-MMk">



</video-accordion>

### Shared State and Option Consistency

When using the same key for multiple `useAsyncData` calls, they will share the same `data`, `error`, `status` and `pending` refs. This ensures consistency across components but requires option consistency.

The following options **must be consistent** across all calls with the same key:

- `handler` function
- `deep` option
- `transform` function
- `pick` array
- `getCachedData` function
- `default` value

The following options **can differ** without triggering warnings:

- `server`
- `lazy`
- `immediate`
- `dedupe`
- `watch`

```ts
// ❌ This will trigger a development warning
const { data: users1 } = useAsyncData('users', (_nuxtApp, { signal }) => $fetch('/api/users', { signal }), { deep: false })
const { data: users2 } = useAsyncData('users', (_nuxtApp, { signal }) => $fetch('/api/users', { signal }), { deep: true })

// ✅ This is allowed
const { data: users1 } = useAsyncData('users', (_nuxtApp, { signal }) => $fetch('/api/users', { signal }), { immediate: true })
const { data: users2 } = useAsyncData('users', (_nuxtApp, { signal }) => $fetch('/api/users', { signal }), { immediate: false })
```

<tip>

Keyed state created using `useAsyncData` can be retrieved across your Nuxt application using [`useNuxtData`](/docs/4.x/api/composables/use-nuxt-data).

</tip>

## Return Values

- `data`: the result of the asynchronous function that is passed in.
- `refresh`/`execute`: a function that can be used to refresh the data returned by the `handler` function.
- `error`: an error object if the data fetching failed.
- `status`: a string indicating the status of the data request:

  - `idle`: when the request has not started, such as:
  
    - when `execute` has not yet been called and `{ immediate: false }` is set
    - when rendering HTML on the server and `{ server: false }` is set
  - `pending`: the request is in progress
  - `success`: the request has completed successfully
  - `error`: the request has failed
- `pending`: a `Ref<boolean>` that is `true` while the request is in progress (that is, while `status.value === 'pending'`).
- `clear`: a function that can be used to set `data` to `undefined` (or the value of `options.default()` if provided), set `error` to `undefined`, set `status` to `idle`, and mark any currently pending requests as cancelled.

By default, Nuxt waits until a `refresh` is finished before it can be executed again.

<note>

If you have not fetched data on the server (for example, with `server: false`), then the data *will not* be fetched until hydration completes. This means even if you await [`useAsyncData`](/docs/4.x/api/composables/use-async-data) on the client side, `data` will remain `undefined` within `<script setup>`.

</note>

## Type

```ts [Signature]
export type AsyncDataHandler<ResT> = (nuxtApp: NuxtApp, options: { signal: AbortSignal }) => Promise<ResT>

export function useAsyncData<DataT, DataE> (
  handler: AsyncDataHandler<DataT>,
  options?: AsyncDataOptions<DataT>,
): AsyncData<DataT, DataE>
export function useAsyncData<DataT, DataE> (
  key: MaybeRefOrGetter<string>,
  handler: AsyncDataHandler<DataT>,
  options?: AsyncDataOptions<DataT>,
): Promise<AsyncData<DataT, DataE>>

type AsyncDataOptions<DataT> = {
  server?: boolean
  lazy?: boolean
  immediate?: boolean
  deep?: boolean
  dedupe?: 'cancel' | 'defer'
  default?: () => DataT | Ref<DataT> | null
  transform?: (input: DataT) => DataT | Promise<DataT>
  pick?: string[]
  watch?: MultiWatchSources
  getCachedData?: (key: string, nuxtApp: NuxtApp, ctx: AsyncDataRequestContext) => DataT | undefined
  timeout?: number
}

type AsyncDataRequestContext = {
  /** The reason for this data request */
  cause: 'initial' | 'refresh:manual' | 'refresh:hook' | 'watch'
}

type AsyncData<DataT, ErrorT> = {
  data: Ref<DataT | undefined>
  refresh: (opts?: AsyncDataExecuteOptions) => Promise<void>
  execute: (opts?: AsyncDataExecuteOptions) => Promise<void>
  clear: () => void
  error: Ref<ErrorT | undefined>
  status: Ref<AsyncDataRequestStatus>
  pending: Ref<boolean>
}

interface AsyncDataExecuteOptions {
  dedupe?: 'cancel' | 'defer'
  timeout?: number
  signal?: AbortSignal
}

type AsyncDataRequestStatus = 'idle' | 'pending' | 'success' | 'error'
```

<read-more to="/docs/4.x/getting-started/data-fetching">



</read-more>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/asyncData.ts)

## Use Fetch

# useFetch

> Fetch data from an API endpoint with an SSR-friendly composable.

This composable provides a convenient wrapper around [`useAsyncData`](/docs/4.x/api/composables/use-async-data) and [`$fetch`](/docs/4.x/api/utils/dollarfetch).
It automatically generates a key based on URL and fetch options, provides type hints for request url based on server routes, and infers API response type.

<note>

`useFetch` is a composable meant to be called directly in a setup function, plugin, or route middleware. It returns reactive composables and handles adding responses to the Nuxt payload so they can be passed from server to client without re-fetching the data on client side when the page hydrates.

</note>

## Usage

```vue [app/pages/modules.vue]
<script setup lang="ts">
const { data, status, error, refresh, clear } = await useFetch('/api/modules', {
  pick: ['title'],
})
</script>
```

<tip to="/docs/4.x/guide/recipes/custom-usefetch#custom-usefetch-with-createusefetch">

Need a custom `useFetch` with pre-defined defaults (like `baseURL` or auth headers)? Use `createUseFetch` to create a fully typed custom composable.

</tip>

<note>

`data`, `status`, and `error` are Vue refs, and they should be accessed with `.value` when used within the `<script setup>`, while `refresh`/`execute` and `clear` are plain functions.

</note>

Using the `query` option, you can add search parameters to your query. This option is extended from [unjs/ofetch](https://github.com/unjs/ofetch) and is using [unjs/ufo](https://github.com/unjs/ufo) to create the URL. Objects are automatically stringified.

```ts
const param1 = ref('value1')
const { data, status, error, refresh } = await useFetch('/api/modules', {
  query: { param1, param2: 'value2' },
})
```

The above example results in `https://api.nuxt.com/modules?param1=value1&param2=value2`.

You can also use [interceptors](https://github.com/unjs/ofetch#%EF%B8%8F-interceptors):

```ts
const { data, status, error, refresh, clear } = await useFetch('/api/auth/login', {
  onRequest ({ request, options }) {
    // Set the request headers
    // note that this relies on ofetch >= 1.4.0 - you may need to refresh your lockfile
    options.headers.set('Authorization', '...')
  },
  onRequestError ({ request, options, error }) {
    // Handle the request errors
  },
  onResponse ({ request, response, options }) {
    // Process the response data
    localStorage.setItem('token', response._data.token)
  },
  onResponseError ({ request, response, options }) {
    // Handle the response errors
  },
})
```

### Reactive Keys and Shared State

You can use a computed ref or a plain ref as the URL, allowing for dynamic data fetching that automatically updates when the URL changes:

```vue [app/pages/[id].vue]
<script setup lang="ts">
const route = useRoute()
const id = computed(() => route.params.id)

// When the route changes and id updates, the data will be automatically refetched
const { data: post } = await useFetch(() => `/api/posts/${id.value}`)
</script>
```

When using `useFetch` with the same URL and options in multiple components, they will share the same `data`, `error` and `status` refs. This ensures consistency across components.

<tip>

Keyed state created using `useFetch` can be retrieved across your Nuxt application using [`useNuxtData`](/docs/4.x/api/composables/use-nuxt-data).

</tip>

<warning>

`useFetch` is a reserved function name transformed by the compiler, so you should not name your own function `useFetch`. To create a custom variant with pre-defined options, use [`createUseFetch`](/docs/4.x/guide/recipes/custom-usefetch#custom-usefetch-with-createusefetch) instead.

</warning>

<warning>

If you encounter the `data` variable destructured from a `useFetch` returns a string and not a JSON parsed object then make sure your component doesn't include an import statement like `import { useFetch } from '@vueuse/core`.

</warning>

<video-accordion title="Watch the video from Alexander Lichter to avoid using useFetch the wrong way" video-id="njsGVmcWviY">



</video-accordion>

<read-more to="/docs/4.x/getting-started/data-fetching">



</read-more>

### Reactive Fetch Options

Fetch options can be provided as reactive, supporting `computed`, `ref` and [computed getters](https://vuejs.org/guide/essentials/computed). When a reactive fetch option is updated it will trigger a refetch using the updated resolved reactive value.

```ts
const searchQuery = ref('initial')
const { data } = await useFetch('/api/search', {
  query: { q: searchQuery },
})
// triggers a refetch: /api/search?q=new%20search
searchQuery.value = 'new search'
```

If needed, you can opt out of this behavior using `watch: false`:

```ts
const searchQuery = ref('initial')
const { data } = await useFetch('/api/search', {
  query: { q: searchQuery },
  watch: false,
})
// does not trigger a refetch
searchQuery.value = 'new search'
```

## Type

```ts [Signature]
export function useFetch<DataT, ErrorT> (
  url: string | Request | Ref<string | Request> | (() => string | Request),
  options?: UseFetchOptions<DataT>,
): Promise<AsyncData<DataT, ErrorT>>

type UseFetchOptions<DataT> = {
  key?: MaybeRefOrGetter<string>
  method?: MaybeRefOrGetter<string>
  query?: MaybeRefOrGetter<SearchParams>
  params?: MaybeRefOrGetter<SearchParams>
  body?: MaybeRefOrGetter<RequestInit['body'] | Record<string, any>>
  headers?: MaybeRefOrGetter<Record<string, string> | [key: string, value: string][] | Headers>
  baseURL?: MaybeRefOrGetter<string>
  cache?: false | 'default' | 'force-cache' | 'no-cache' | 'no-store' | 'only-if-cached' | 'reload'
  server?: boolean
  lazy?: boolean
  immediate?: boolean
  getCachedData?: (key: string, nuxtApp: NuxtApp, ctx: AsyncDataRequestContext) => DataT | undefined
  deep?: boolean
  dedupe?: 'cancel' | 'defer'
  timeout?: number
  default?: () => DataT
  transform?: (input: DataT) => DataT | Promise<DataT>
  pick?: string[]
  $fetch?: typeof globalThis.$fetch
  watch?: MultiWatchSources | false
}

type AsyncDataRequestContext = {
  /** The reason for this data request */
  cause: 'initial' | 'refresh:manual' | 'refresh:hook' | 'watch'
}

type AsyncData<DataT, ErrorT> = {
  data: Ref<DataT | undefined>
  pending: Ref<boolean>
  refresh: (opts?: AsyncDataExecuteOptions) => Promise<void>
  execute: (opts?: AsyncDataExecuteOptions) => Promise<void>
  clear: () => void
  error: Ref<ErrorT | undefined>
  status: Ref<AsyncDataRequestStatus>
}

interface AsyncDataExecuteOptions {
  dedupe?: 'cancel' | 'defer'
  timeout?: number
  signal?: AbortSignal
}

type AsyncDataRequestStatus = 'idle' | 'pending' | 'success' | 'error'
```

## Parameters

- `URL` (`string | Request | Ref<string | Request> | () => string | Request`): The URL or request to fetch. Can be a string, a Request object, a Vue ref, or a function returning a string/Request. Supports reactivity for dynamic endpoints.
- `options` (object): Configuration for the fetch request. Extends [unjs/ofetch](https://github.com/unjs/ofetch) options and [`AsyncDataOptions`](/docs/4.x/api/composables/use-async-data#params). All options can be a static value, a `ref`, or a computed value.

<table>
<thead>
  <tr>
    <th>
      Option
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Default
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
        key
      </code>
    </td>
    
    <td>
      <code>
        MaybeRefOrGetter<string>
      </code>
    </td>
    
    <td>
      auto-gen
    </td>
    
    <td>
      Unique key for de-duplication. If not provided, generated from URL and options.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        method
      </code>
    </td>
    
    <td>
      <code>
        MaybeRefOrGetter<string>
      </code>
    </td>
    
    <td>
      <code>
        'GET'
      </code>
    </td>
    
    <td>
      HTTP request method.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        query
      </code>
    </td>
    
    <td>
      <code>
        MaybeRefOrGetter<SearchParams>
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Query/search params to append to the URL. Alias: <code>
        params
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        params
      </code>
    </td>
    
    <td>
      <code>
        MaybeRefOrGetter<SearchParams>
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Alias for <code>
        query
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        body
      </code>
    </td>
    
    <td>
      <code>
        MaybeRefOrGetter<RequestInit['body'] | Record<string, any>>
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Request body. Objects are automatically stringified.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        headers
      </code>
    </td>
    
    <td>
      <code>
        MaybeRefOrGetter<Record<string, string> | [key, value][] | Headers>
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Request headers.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        baseURL
      </code>
    </td>
    
    <td>
      <code>
        MaybeRefOrGetter<string>
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Base URL for the request.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        cache
      </code>
    </td>
    
    <td>
      <code>
        false | string
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Cache control. Boolean disables cache, or use Fetch API values: <code>
        default
      </code>
      
      , <code>
        no-store
      </code>
      
      , etc.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        server
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Whether to fetch on the server.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        lazy
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
      If true, resolves after route loads (does not block navigation).
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        immediate
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      If false, prevents request from firing immediately.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        default
      </code>
    </td>
    
    <td>
      <code>
        () => DataT
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Factory for default value of <code>
        data
      </code>
      
       before async resolves.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        timeout
      </code>
    </td>
    
    <td>
      <code>
        number
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      A number in milliseconds to wait before timing out the request (defaults to <code>
        undefined
      </code>
      
      , which means no timeout)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        transform
      </code>
    </td>
    
    <td>
      <code>
        (input: DataT) => DataT | Promise<DataT>
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Function to transform the result after resolving.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        getCachedData
      </code>
    </td>
    
    <td>
      <code>
        (key, nuxtApp, ctx) => DataT | undefined
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Function to return cached data. See below for default.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        pick
      </code>
    </td>
    
    <td>
      <code>
        string[]
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Only pick specified keys from the result.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        watch
      </code>
    </td>
    
    <td>
      <code>
        MultiWatchSources | false
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Array of reactive sources to watch and auto-refresh. <code>
        false
      </code>
      
       disables watching.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        deep
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
      Return data in a deep ref object.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        dedupe
      </code>
    </td>
    
    <td>
      <code>
        'cancel' | 'defer'
      </code>
    </td>
    
    <td>
      <code>
        'cancel'
      </code>
    </td>
    
    <td>
      Avoid fetching same key more than once at a time.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        $fetch
      </code>
    </td>
    
    <td>
      <code>
        typeof globalThis.$fetch
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Custom $fetch implementation. See <a href="/docs/4.x/guide/recipes/custom-usefetch">
        Custom useFetch in Nuxt
      </a>
    </td>
  </tr>
</tbody>
</table>

<note>

All fetch options can be given a `computed` or `ref` value. These will be watched and new requests made automatically with any new values if they are updated.

</note>

**getCachedData default:**

```ts
const getDefaultCachedData = (key, nuxtApp, ctx) => nuxtApp.isHydrating
  ? nuxtApp.payload.data[key]
  : nuxtApp.static.data[key]
```

This only caches data when `experimental.payloadExtraction` in `nuxt.config` is enabled.

## Return Values

<table>
<thead>
  <tr>
    <th>
      Name
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
        data
      </code>
    </td>
    
    <td>
      <code>
        Ref<DataT | undefined>
      </code>
    </td>
    
    <td>
      The result of the asynchronous fetch.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        refresh
      </code>
    </td>
    
    <td>
      <code>
        (opts?: AsyncDataExecuteOptions) => Promise<void>
      </code>
    </td>
    
    <td>
      Function to manually refresh the data. By default, Nuxt waits until a <code>
        refresh
      </code>
      
       is finished before it can be executed again.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        execute
      </code>
    </td>
    
    <td>
      <code>
        (opts?: AsyncDataExecuteOptions) => Promise<void>
      </code>
    </td>
    
    <td>
      Alias for <code>
        refresh
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        error
      </code>
    </td>
    
    <td>
      <code>
        Ref<ErrorT | undefined>
      </code>
    </td>
    
    <td>
      Error object if the data fetching failed.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        status
      </code>
    </td>
    
    <td>
      <code>
        Ref<'idle' | 'pending' | 'success' | 'error'>
      </code>
    </td>
    
    <td>
      Status of the data request. See below for possible values.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        pending
      </code>
    </td>
    
    <td>
      <code>
        Ref<boolean>
      </code>
    </td>
    
    <td>
      Boolean flag indicating whether the current request is in progress.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        clear
      </code>
    </td>
    
    <td>
      <code>
        () => void
      </code>
    </td>
    
    <td>
      Resets <code>
        data
      </code>
      
       to <code>
        undefined
      </code>
      
       (or the value of <code>
        options.default()
      </code>
      
       if provided), <code>
        error
      </code>
      
       to <code>
        undefined
      </code>
      
      , set <code>
        status
      </code>
      
       to <code>
        idle
      </code>
      
      , and cancels any pending requests.
    </td>
  </tr>
</tbody>
</table>

### Status values

- `idle`: Request has not started (e.g. `{ immediate: false }` or `{ server: false }` on server render)
- `pending`: Request is in progress
- `success`: Request completed successfully
- `error`: Request failed

<note>

If you have not fetched data on the server (for example, with `server: false`), then the data *will not* be fetched until hydration completes. This means even if you await `useFetch` on client-side, `data` will remain undefined within `<script setup>`.

</note>

### Examples

<link-example to="/docs/4.x/examples/advanced/use-custom-fetch-composable">



</link-example>

<link-example to="/docs/4.x/examples/features/data-fetching">



</link-example>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/fetch.ts)

## Use Lazy Async Data

# useLazyAsyncData

> This wrapper around useAsyncData triggers navigation immediately.

`useLazyAsyncData` provides a wrapper around [`useAsyncData`](/docs/4.x/api/composables/use-async-data) that triggers navigation before the handler is resolved by setting the `lazy` option to `true`.

<note>

By default, [`useAsyncData`](/docs/4.x/api/composables/use-async-data) blocks navigation until its async handler is resolved. `useLazyAsyncData` allows navigation to occur immediately while data fetching continues in the background.

</note>

## Usage

```vue [app/pages/index.vue]
<script setup lang="ts">
const { status, data: posts } = await useLazyAsyncData('posts', () => $fetch('/api/posts'))
</script>

<template>
  <div>
    <div v-if="status === 'pending'">
      Loading...
    </div>
    <div v-else-if="status === 'error'">
      Error loading posts
    </div>
    <div v-else>
      {{ posts }}
    </div>
  </div>
</template>
```

When using `useLazyAsyncData`, navigation will occur before fetching is complete. This means you must handle `pending` and `error` states directly within your component's template.

<warning>

`useLazyAsyncData` is a reserved function name transformed by the compiler, so you should not name your own function `useLazyAsyncData`.

</warning>

## Type

```ts [Signature]
export function useLazyAsyncData<DataT, ErrorT> (
  handler: (ctx?: NuxtApp) => Promise<DataT>,
  options?: AsyncDataOptions<DataT>,
): AsyncData<DataT, ErrorT>

export function useLazyAsyncData<DataT, ErrorT> (
  key: string,
  handler: (ctx?: NuxtApp) => Promise<DataT>,
  options?: AsyncDataOptions<DataT>,
): AsyncData<DataT, ErrorT>
```

`useLazyAsyncData` has the same signature as [`useAsyncData`](/docs/4.x/api/composables/use-async-data).

## Parameters

`useLazyAsyncData` accepts the same parameters as [`useAsyncData`](/docs/4.x/api/composables/use-async-data), with the `lazy` option automatically set to `true`.

<read-more to="/docs/4.x/api/composables/use-async-data#parameters">



</read-more>

## Return Values

`useLazyAsyncData` returns the same values as [`useAsyncData`](/docs/4.x/api/composables/use-async-data).

<read-more to="/docs/4.x/api/composables/use-async-data#return-values">



</read-more>

## Example

```vue [app/pages/index.vue]
<script setup lang="ts">
/* Navigation will occur before fetching is complete.
  Handle 'pending' and 'error' states directly within your component's template
*/
const { status, data: count } = await useLazyAsyncData('count', () => $fetch('/api/count'))

watch(count, (newCount) => {
  // Because count might start out null, you won't have access
  // to its contents immediately, but you can watch it.
})
</script>

<template>
  <div>
    {{ status === 'pending' ? 'Loading' : count }}
  </div>
</template>
```

<read-more to="/docs/4.x/getting-started/data-fetching">



</read-more>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/asyncData.ts)

## Use Lazy Fetch

# useLazyFetch

> This wrapper around useFetch triggers navigation immediately.

`useLazyFetch` provides a wrapper around [`useFetch`](/docs/4.x/api/composables/use-fetch) that triggers navigation before the handler is resolved by setting the `lazy` option to `true`.

## Usage

By default, [`useFetch`](/docs/4.x/api/composables/use-fetch) blocks navigation until its async handler is resolved. `useLazyFetch` allows navigation to proceed immediately, with data being fetched in the background.

```vue [app/pages/index.vue]
<script setup lang="ts">
const { status, data: posts } = await useLazyFetch('/api/posts')
</script>

<template>
  <div v-if="status === 'pending'">
    Loading ...
  </div>
  <div v-else>
    <div v-for="post in posts">
      <!-- do something -->
    </div>
  </div>
</template>
```

<note>

`useLazyFetch` has the same signature as [`useFetch`](/docs/4.x/api/composables/use-fetch).

</note>

<warning>

Awaiting `useLazyFetch` only ensures the call is initialized. On client-side navigation, data may not be immediately available, and you must handle the `pending` state in your component's template.

</warning>

<warning>

`useLazyFetch` is a reserved function name transformed by the compiler, so you should not name your own function `useLazyFetch`.

</warning>

## Type

```ts [Signature]
export function useLazyFetch<DataT, ErrorT> (
  url: string | Request | Ref<string | Request> | (() => string | Request),
  options?: UseFetchOptions<DataT>,
): Promise<AsyncData<DataT, ErrorT>>
```

<note>

`useLazyFetch` is equivalent to `useFetch` with `lazy: true` option set. See [`useFetch`](/docs/4.x/api/composables/use-fetch) for full type definitions.

</note>

## Parameters

`useLazyFetch` accepts the same parameters as [`useFetch`](/docs/4.x/api/composables/use-fetch):

- `URL` (`string | Request | Ref<string | Request> | () => string | Request`): The URL or request to fetch.
- `options` (object): Same as [`useFetch` options](/docs/4.x/api/composables/use-fetch#parameters), with `lazy` automatically set to `true`.

<read-more to="/docs/4.x/api/composables/use-fetch#parameters">



</read-more>

## Return Values

Returns the same `AsyncData` object as [`useFetch`](/docs/4.x/api/composables/use-fetch):

<table>
<thead>
  <tr>
    <th>
      Name
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
        data
      </code>
    </td>
    
    <td>
      <code>
        Ref<DataT | undefined>
      </code>
    </td>
    
    <td>
      The result of the asynchronous fetch.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        refresh
      </code>
    </td>
    
    <td>
      <code>
        (opts?: AsyncDataExecuteOptions) => Promise<void>
      </code>
    </td>
    
    <td>
      Function to manually refresh the data.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        execute
      </code>
    </td>
    
    <td>
      <code>
        (opts?: AsyncDataExecuteOptions) => Promise<void>
      </code>
    </td>
    
    <td>
      Alias for <code>
        refresh
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        error
      </code>
    </td>
    
    <td>
      <code>
        Ref<ErrorT | undefined>
      </code>
    </td>
    
    <td>
      Error object if the data fetching failed.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        status
      </code>
    </td>
    
    <td>
      <code>
        Ref<'idle' | 'pending' | 'success' | 'error'>
      </code>
    </td>
    
    <td>
      Status of the data request.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        pending
      </code>
    </td>
    
    <td>
      <code>
        Ref<boolean>
      </code>
    </td>
    
    <td>
      Boolean flag indicating whether the current request is in progress.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        clear
      </code>
    </td>
    
    <td>
      <code>
        () => void
      </code>
    </td>
    
    <td>
      Resets <code>
        data
      </code>
      
       to <code>
        undefined
      </code>
      
      , <code>
        error
      </code>
      
       to <code>
        undefined
      </code>
      
      , sets <code>
        status
      </code>
      
       to <code>
        idle
      </code>
      
      , and cancels any pending requests.
    </td>
  </tr>
</tbody>
</table>

<read-more to="/docs/4.x/api/composables/use-fetch#return-values">



</read-more>

## Examples

### Handling Pending State

```vue [app/pages/index.vue]
<script setup lang="ts">
/* Navigation will occur before fetching is complete.
 * Handle 'pending' and 'error' states directly within your component's template
 */
const { status, data: posts } = await useLazyFetch('/api/posts')
watch(posts, (newPosts) => {
  // Because posts might start out null, you won't have access
  // to its contents immediately, but you can watch it.
})
</script>

<template>
  <div v-if="status === 'pending'">
    Loading ...
  </div>
  <div v-else>
    <div v-for="post in posts">
      <!-- do something -->
    </div>
  </div>
</template>
```

<read-more to="/docs/4.x/getting-started/data-fetching">



</read-more>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/fetch.ts)

## Use Cookie

# useCookie

> useCookie is an SSR-friendly composable to read and write cookies.

## Usage

Within your pages, components, and plugins, you can use `useCookie` to read and write cookies in an SSR-friendly way.

```ts
const cookie = useCookie(name, options)
```

<note>

`useCookie` only works in the [Nuxt context](/docs/4.x/guide/going-further/nuxt-app#the-nuxt-context).

</note>

<tip>

The returned ref will automatically serialize and deserialize cookie values to JSON.

</tip>

## Type

```ts [Signature]
import type { Ref } from 'vue'
import type { CookieParseOptions, CookieSerializeOptions } from 'cookie-es'

export interface CookieOptions<T = any> extends Omit<CookieSerializeOptions & CookieParseOptions, 'decode' | 'encode'> {
  decode?(value: string): T
  encode?(value: T): string
  default?: () => T | Ref<T>
  watch?: boolean | 'shallow'
  readonly?: boolean
  refresh?: boolean
}

export interface CookieRef<T> extends Ref<T> {}

export function useCookie<T = string | null | undefined> (
  name: string,
  options?: CookieOptions<T>,
): CookieRef<T>
```

## Parameters

`name`: The name of the cookie.

`options`: Options to control cookie behavior. The object can have the following properties:

Most of the options will be directly passed to the [cookie](https://github.com/jshttp/cookie) package.

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
      Default
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
        decode
      </code>
    </td>
    
    <td>
      <code>
        (value: string) => T
      </code>
    </td>
    
    <td>
      <code>
        decodeURIComponent
      </code>
      
       + <a href="https://github.com/unjs/destr" rel="nofollow">
        destr
      </a>
      
      .
    </td>
    
    <td>
      Custom function to decode the cookie value.  Since the value of a cookie has a limited character set (and must be a simple string), this function can be used to decode a previously encoded cookie value into a JavaScript string or other object. <br />
      
       <strong>
        Note:
      </strong>
      
       If an error is thrown from this function, the original, non-decoded cookie value will be returned as the cookie's value.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        encode
      </code>
    </td>
    
    <td>
      <code>
        (value: T) => string
      </code>
    </td>
    
    <td>
      <code>
        JSON.stringify
      </code>
      
       + <code>
        encodeURIComponent
      </code>
    </td>
    
    <td>
      Custom function to encode the cookie value. Since the value of a cookie has a limited character set (and must be a simple string), this function can be used to encode a value into a string suited for a cookie's value.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        default
      </code>
    </td>
    
    <td>
      <code>
        () => T | Ref<T>
      </code>
    </td>
    
    <td>
      <code>
        undefined
      </code>
    </td>
    
    <td>
      Function returning the default value if the cookie does not exist.  The function can also return a <code>
        Ref
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        watch
      </code>
    </td>
    
    <td>
      <code>
        boolean | 'shallow'
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Whether to watch for changes and update the cookie. <code>
        true
      </code>
      
       for deep watch, <code>
        'shallow'
      </code>
      
       for shallow watch, i.e. data changes for only top level properties, <code>
        false
      </code>
      
       to disable. <br />
      
       <strong>
        Note:
      </strong>
      
       Refresh <code>
        useCookie
      </code>
      
       values manually when a cookie has changed with <a href="/docs/4.x/api/utils/refresh-cookie">
        <code>
          refreshCookie
        </code>
      </a>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        refresh
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
      If <code>
        true
      </code>
      
      , the cookie expiration will be refreshed on every explicit write (e.g. <code>
        cookie.value = cookie.value
      </code>
      
      ), even if the value itself hasn’t changed. Note: the expiration is not refreshed automatically — you must assign to <code>
        .value
      </code>
      
       to trigger it.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        readonly
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
      If <code>
        true
      </code>
      
      , disables writing to the cookie.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        maxAge
      </code>
    </td>
    
    <td>
      <code>
        number
      </code>
    </td>
    
    <td>
      <code>
        undefined
      </code>
    </td>
    
    <td>
      Max age in seconds for the cookie, i.e. the value for the <a href="https://datatracker.ietf.org/doc/html/rfc6265#section-5.2.2" rel="nofollow">
        <code>
          Max-Age
        </code>
        
         <code>
          Set-Cookie
        </code>
        
         attribute
      </a>
      
      . The given number will be converted to an integer by rounding down. By default, no maximum age is set.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        expires
      </code>
    </td>
    
    <td>
      <code>
        Date
      </code>
    </td>
    
    <td>
      <code>
        undefined
      </code>
    </td>
    
    <td>
      Expiration date for the cookie. By default, no expiration is set. Most clients will consider this a "non-persistent cookie" and will delete it on a condition like exiting a web browser application. <br />
      
       <strong>
        Note:
      </strong>
      
       The <a href="https://datatracker.ietf.org/doc/html/rfc6265#section-5.3" rel="nofollow">
        cookie storage model specification
      </a>
      
       states that if both <code>
        expires
      </code>
      
       and <code>
        maxAge
      </code>
      
       is set, then <code>
        maxAge
      </code>
      
       takes precedence, but not all clients may obey this, so if both are set, they should point to the same date and time! <br />
      
      If neither of <code>
        expires
      </code>
      
       and <code>
        maxAge
      </code>
      
       is set, the cookie will be session-only and removed when the user closes their browser.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        httpOnly
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
      Sets the HttpOnly attribute. <br />
      
       <strong>
        Note:
      </strong>
      
       Be careful when setting this to <code>
        true
      </code>
      
      , as compliant clients will not allow client-side JavaScript to see the cookie in <code>
        document.cookie
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        secure
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
      Sets the <a href="https://datatracker.ietf.org/doc/html/rfc6265#section-5.2.5" rel="nofollow">
        <code>
          Secure
        </code>
        
         <code>
          Set-Cookie
        </code>
        
         attribute
      </a>
      
      . <br />
      
      <strong>
        Note:
      </strong>
      
       Be careful when setting this to <code>
        true
      </code>
      
      , as compliant clients will not send the cookie back to the server in the future if the browser does not have an HTTPS connection. This can lead to hydration errors.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        partitioned
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
      Sets the <a href="https://datatracker.ietf.org/doc/html/draft-cutler-httpbis-partitioned-cookies#section-2.1" rel="nofollow">
        <code>
          Partitioned
        </code>
        
         <code>
          Set-Cookie
        </code>
        
         attribute
      </a>
      
      . <br />
      
      <strong>
        Note:
      </strong>
      
       This is an attribute that has not yet been fully standardized, and may change in the future. <br />
      
      This also means many clients may ignore this attribute until they understand it.<br />
      
      More information can be found in the <a href="https://github.com/privacycg/CHIPS" rel="nofollow">
        proposal
      </a>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        domain
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        undefined
      </code>
    </td>
    
    <td>
      Sets the <a href="https://datatracker.ietf.org/doc/html/rfc6265#section-5.2.3" rel="nofollow">
        <code>
          Domain
        </code>
        
         <code>
          Set-Cookie
        </code>
        
         attribute
      </a>
      
      . By default, no domain is set, and most clients will consider applying the cookie only to the current domain.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        path
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        '/'
      </code>
    </td>
    
    <td>
      Sets the <a href="https://datatracker.ietf.org/doc/html/rfc6265#section-5.2.4" rel="nofollow">
        <code>
          Path
        </code>
        
         <code>
          Set-Cookie
        </code>
        
         attribute
      </a>
      
      . By default, the path is considered the <a href="https://datatracker.ietf.org/doc/html/rfc6265#section-5.1.4" rel="nofollow">
        "default path"
      </a>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        sameSite
      </code>
    </td>
    
    <td>
      <code>
        boolean | string
      </code>
    </td>
    
    <td>
      <code>
        undefined
      </code>
    </td>
    
    <td>
      Sets the <a href="https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-rfc6265bis-03#section-4.1.2.7" rel="nofollow">
        <code>
          SameSite
        </code>
        
         <code>
          Set-Cookie
        </code>
        
         attribute
      </a>
      
      . <br />
      
      - <code>
        true
      </code>
      
       will set the <code>
        SameSite
      </code>
      
       attribute to <code>
        Strict
      </code>
      
       for strict same-site enforcement.<br />
      
      - <code>
        false
      </code>
      
       will not set the <code>
        SameSite
      </code>
      
       attribute.<br />
      
      - <code>
        'lax'
      </code>
      
       will set the <code>
        SameSite
      </code>
      
       attribute to <code>
        Lax
      </code>
      
       for lax same-site enforcement.<br />
      
      - <code>
        'none'
      </code>
      
       will set the <code>
        SameSite
      </code>
      
       attribute to <code>
        None
      </code>
      
       for an explicit cross-site cookie.<br />
      
      - <code>
        'strict'
      </code>
      
       will set the <code>
        SameSite
      </code>
      
       attribute to <code>
        Strict
      </code>
      
       for strict same-site enforcement.
    </td>
  </tr>
</tbody>
</table>

## Return Values

Returns a Vue `Ref<T>` representing the cookie value. Updating the ref will update the cookie (unless `readonly` is set). The ref is SSR-friendly and will work on both client and server.

## Examples

### Basic Usage

The example below creates a cookie called `counter`. If the cookie doesn't exist, it is initially set to a random value. Whenever we update the `counter` variable, the cookie will be updated accordingly.

```vue [app/app.vue]
<script setup lang="ts">
const counter = useCookie('counter')

counter.value ||= Math.round(Math.random() * 1000)
</script>

<template>
  <div>
    <h1>Counter: {{ counter || '-' }}</h1>
    <button @click="counter = null">
      reset
    </button>
    <button @click="counter--">
      -
    </button>
    <button @click="counter++">
      +
    </button>
  </div>
</template>
```

### Readonly Cookies

```vue
<script setup lang="ts">
const user = useCookie(
  'userInfo',
  {
    default: () => ({ score: -1 }),
    watch: false,
  },
)

if (user.value) {
  // the actual `userInfo` cookie will not be updated
  user.value.score++
}
</script>

<template>
  <div>User score: {{ user?.score }}</div>
</template>
```

### Writable Cookies

```vue
<script setup lang="ts">
const list = useCookie(
  'list',
  {
    default: () => [],
    watch: 'shallow',
  },
)

function add () {
  list.value?.push(Math.round(Math.random() * 1000))
  // list cookie won't be updated with this change
}

function save () {
  // the actual `list` cookie will be updated
  list.value &&= [...list.value]
}
</script>

<template>
  <div>
    <h1>List</h1>
    <pre>{{ list }}</pre>
    <button @click="add">
      Add
    </button>
    <button @click="save">
      Save
    </button>
  </div>
</template>
```

### Refreshing Cookies

```vue
<script setup lang="ts">
const session = useCookie(
  'session', {
    maxAge: 60 * 60, // 1 hour
    refresh: true,
    default: () => 'active',
  })

// Even if the value does not change,
// the cookie expiration will be refreshed
// every time the setter is called
session.value = 'active'
</script>

<template>
  <div>Session: {{ session }}</div>
</template>
```

### Cookies in API Routes

You can use `getCookie` and `setCookie` from [`h3`](https://github.com/h3js/h3) package to set cookies in server API routes.

```ts [server/api/counter.ts]
export default defineEventHandler((event) => {
  // Read counter cookie
  let counter = getCookie(event, 'counter') || 0

  // Increase counter cookie by 1
  setCookie(event, 'counter', ++counter)

  // Send JSON response
  return { counter }
})
```

<link-example to="/docs/4.x/examples/advanced/use-cookie">



</link-example>

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/cookie.ts)

## Use State

# useState

> The useState composable creates a reactive and SSR-friendly shared state.

## Usage

```ts
// Create a reactive state and set default value
const count = useState('counter', () => Math.round(Math.random() * 100))
```

<read-more to="/docs/4.x/getting-started/state-management">



</read-more>

<important>

Because the data inside `useState` will be serialized to JSON, it is important that it does not contain anything that cannot be serialized, such as classes, functions or symbols.

</important>

<warning>

`useState` is a reserved function name transformed by the compiler, so you should not name your own function `useState`.

</warning>

<video-accordion title="Watch a video from Alexander Lichter about why and when to use useState" video-id="mv0WcBABcIk">



</video-accordion>

## Using `shallowRef`

If you don't need your state to be deeply reactive, you can combine `useState` with [`shallowRef`](https://vuejs.org/api/reactivity-advanced#shallowref). This can improve performance when your state contains large objects and arrays.

```ts
const state = useState('my-shallow-state', () => shallowRef({ deep: 'not reactive' }))
// isShallow(state) === true
```

## Type

```ts [Signature]
export function useState<T> (init?: () => T | Ref<T>): Ref<T>
export function useState<T> (key: string, init?: () => T | Ref<T>): Ref<T>
```

- `key`: A unique key ensuring that data fetching is properly de-duplicated across requests. If you do not provide a key, then a key that is unique to the file and line number of the instance of [`useState`](/docs/4.x/api/composables/use-state) will be generated for you.
- `init`: A function that provides initial value for the state when not initiated. This function can also return a `Ref`.
- `T`: (typescript only) Specify the type of state

## Troubleshooting

### `Cannot stringify arbitrary non-POJOs`

This error occurs when you try to store a non-serializable payload with `useState`, such as class instances.

If you want to store class instances with `useState` that are not supported by Nuxt, you can use [`definePayloadPlugin`](/docs/4.x/api/composables/use-nuxt-app#custom-reducerreviver) to add a custom serializer and deserializer for your classes.

<read-more to="/docs/4.x/api/composables/use-nuxt-app#payload">



</read-more>

<style>

html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/state.ts)

## Use Head

# useHead

> useHead customizes the head properties of individual pages of your Nuxt app.

## Usage

The `useHead` composable allows you to manage your head tags in a programmatic and reactive way, powered by [Unhead](https://unhead.unjs.io). It lets you customize the meta tags, links, scripts, and other elements in the `<head>` section of your HTML document.

```vue [app/app.vue]
<script setup lang="ts">
useHead({
  title: 'My App',
  meta: [
    { name: 'description', content: 'My amazing site.' },
  ],
  bodyAttrs: {
    class: 'test',
  },
  script: [{ innerHTML: 'console.log(\'Hello world\')' }],
})
</script>
```

<warning>

If the data comes from a user or other untrusted source, we recommend you check out [`useHeadSafe`](/docs/4.x/api/composables/use-head-safe).

</warning>

<note>

The properties of `useHead` can be dynamic, accepting `ref`, `computed` and `reactive` properties. The `meta` parameter can also accept a function returning an object to make the entire object reactive.

</note>

## Type

```ts [Signature]
export function useHead (meta: MaybeComputedRef<MetaObject>): ActiveHeadEntry<UseHeadInput>

interface MetaObject {
  title?: string
  titleTemplate?: string | ((title?: string) => string)
  base?: Base
  link?: Link[]
  meta?: Meta[]
  style?: Style[]
  script?: Script[]
  noscript?: Noscript[]
  htmlAttrs?: HtmlAttributes
  bodyAttrs?: BodyAttributes
}

interface ActiveHeadEntry<Input> {
  /**
   * Updates the entry with new input.
   *
   * Will first clear any side effects for previous input.
   */
  patch: (input: Input) => void
  /**
   * Dispose the entry, removing it from the active head.
   *
   * Will queue side effects for removal.
   */
  dispose: () => void
}
```

See [@unhead/schema](https://github.com/unjs/unhead/blob/main/packages/vue/src/types/schema.ts) for more detailed types.

## Parameters

`meta`: An object accepting head metadata properties to customize the page's `<head>` section. All properties support reactive values (`ref`, `computed`, `reactive`) or can be a function returning the metadata object.

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
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        title
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      Sets the page title.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        titleTemplate
      </code>
    </td>
    
    <td>
      <code>
        string | ((title?: string) => string)
      </code>
    </td>
    
    <td>
      Configures a dynamic template to customize the page title. Can be a string with <code>
        %s
      </code>
      
       placeholder or a function.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        base
      </code>
    </td>
    
    <td>
      <code>
        Base
      </code>
    </td>
    
    <td>
      Sets the <code>
        <base>
      </code>
      
       tag for the document.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        link
      </code>
    </td>
    
    <td>
      <code>
        Link[]
      </code>
    </td>
    
    <td>
      Array of link objects. Each element is mapped to a <code>
        <link>
      </code>
      
       tag, where object properties correspond to HTML attributes.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        meta
      </code>
    </td>
    
    <td>
      <code>
        Meta[]
      </code>
    </td>
    
    <td>
      Array of meta objects. Each element is mapped to a <code>
        <meta>
      </code>
      
       tag, where object properties correspond to HTML attributes.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        style
      </code>
    </td>
    
    <td>
      <code>
        Style[]
      </code>
    </td>
    
    <td>
      Array of style objects. Each element is mapped to a <code>
        <style>
      </code>
      
       tag, where object properties correspond to HTML attributes.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        script
      </code>
    </td>
    
    <td>
      <code>
        Script[]
      </code>
    </td>
    
    <td>
      Array of script objects. Each element is mapped to a <code>
        <script>
      </code>
      
       tag, where object properties correspond to HTML attributes.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        noscript
      </code>
    </td>
    
    <td>
      <code>
        Noscript[]
      </code>
    </td>
    
    <td>
      Array of noscript objects. Each element is mapped to a <code>
        <noscript>
      </code>
      
       tag, where object properties correspond to HTML attributes.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        htmlAttrs
      </code>
    </td>
    
    <td>
      <code>
        HtmlAttributes
      </code>
    </td>
    
    <td>
      Sets attributes of the <code>
        <html>
      </code>
      
       tag. Each object property is mapped to the corresponding attribute.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        bodyAttrs
      </code>
    </td>
    
    <td>
      <code>
        BodyAttributes
      </code>
    </td>
    
    <td>
      Sets attributes of the <code>
        <body>
      </code>
      
       tag. Each object property is mapped to the corresponding attribute.
    </td>
  </tr>
</tbody>
</table>

## Return Values

This composable does not return any value. It registers the head metadata with Unhead, which manages the actual DOM updates.

## Examples

### Basic Meta Tags

```vue [app/pages/about.vue]
<script setup lang="ts">
useHead({
  title: 'About Us',
  meta: [
    { name: 'description', content: 'Learn more about our company' },
    { property: 'og:title', content: 'About Us' },
    { property: 'og:description', content: 'Learn more about our company' },
  ],
})
</script>
```

### Reactive Meta Tags

```vue [app/pages/profile.vue]
<script setup lang="ts">
const profile = ref({ name: 'John Doe' })

useHead({
  title: computed(() => profile.value.name),
  meta: [
    {
      name: 'description',
      content: computed(() => `Profile page for ${profile.value.name}`),
    },
  ],
})
</script>
```

### Using a Function for Full Reactivity

```vue [app/pages/dynamic.vue]
<script setup lang="ts">
const count = ref(0)

useHead(() => ({
  title: `Count: ${count.value}`,
  meta: [
    { name: 'description', content: `Current count is ${count.value}` },
  ],
}))
</script>
```

### Adding External Scripts and Styles

```vue [app/pages/external.vue]
<script setup lang="ts">
useHead({
  link: [
    {
      rel: 'stylesheet',
      href: 'https://cdn.example.com/styles.css',
    },
  ],
  script: [
    {
      src: 'https://cdn.example.com/script.js',
      async: true,
    },
  ],
})
</script>
```

### Body and HTML Attributes

```vue [app/pages/themed.vue]
<script setup lang="ts">
const isDark = ref(true)

useHead({
  htmlAttrs: {
    lang: 'en',
    class: computed(() => isDark.value ? 'dark' : 'light'),
  },
  bodyAttrs: {
    class: 'themed-page',
  },
})
</script>
```

<read-more to="/docs/4.x/getting-started/seo-meta">



</read-more>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}

</style>

---

- [Source](https://github.com/unjs/unhead/blob/main/packages/vue/src/composables.ts)

## Use Seo Meta

# useSeoMeta

> The useSeoMeta composable lets you define your site's SEO meta tags as a flat object with full TypeScript support.

This helps you avoid common mistakes, such as using `name` instead of `property`, as well as typos - with over 100+ meta tags fully typed.

<important>

This is the recommended way to add meta tags to your site as it is XSS safe and has full TypeScript support.

</important>

<read-more to="/docs/4.x/getting-started/seo-meta">



</read-more>

## Usage

```vue [app/app.vue]
<script setup lang="ts">
useSeoMeta({
  title: 'My Amazing Site',
  ogTitle: 'My Amazing Site',
  description: 'This is my amazing site, let me tell you all about it.',
  ogDescription: 'This is my amazing site, let me tell you all about it.',
  ogImage: 'https://example.com/image.png',
  twitterCard: 'summary_large_image',
})
</script>
```

When inserting tags that are reactive, you should use the computed getter syntax (`() => value`):

```vue [app/app.vue]
<script setup lang="ts">
const title = ref('My title')

useSeoMeta({
  title,
  description: () => `This is a description for the ${title.value} page`,
})
</script>
```

## Parameters

There are over 100 parameters. See the [full list of parameters in the source code](https://github.com/harlan-zw/zhead/blob/main/packages/zhead/src/metaFlat.ts#L1035).

<read-more to="/docs/4.x/getting-started/seo-meta">



</read-more>

## Performance

In most instances, SEO meta tags don't need to be reactive as search engine robots primarily scan the initial page load.

For better performance, you can wrap your `useSeoMeta` calls in a server-only condition when the meta tags don't need to be reactive:

```vue [app/app.vue]
<script setup lang="ts">
if (import.meta.server) {
  // These meta tags will only be added during server-side rendering
  useSeoMeta({
    robots: 'index, follow',
    description: 'Static description that does not need reactivity',
    ogImage: 'https://example.com/image.png',
    // other static meta tags...
  })
}

const dynamicTitle = ref('My title')
// Only use reactive meta tags outside the condition when necessary
useSeoMeta({
  title: () => dynamicTitle.value,
  ogTitle: () => dynamicTitle.value,
})
</script>
```

This previously used the [`useServerSeoMeta`](/docs/4.x/api/composables/use-server-seo-meta) composable, but it has been deprecated in favor of this approach.

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/unjs/unhead/blob/main/packages/vue/src/composables.ts)

## Use Server Seo Meta

# useServerSeoMeta

> The useServerSeoMeta composable lets you define your site's SEO meta tags as a flat object with full TypeScript support.

<warning>

`useServerSeoMeta` is deprecated. Wrap [`useSeoMeta`](/docs/4.x/api/composables/use-seo-meta) in an `if (import.meta.server)` block instead. The auto-import is removed under `future.compatibilityVersion: 5`.

</warning>

`useServerSeoMeta` lets you define your site's SEO meta tags as a flat object with full TypeScript support, exactly like [`useSeoMeta`](/docs/4.x/api/composables/use-seo-meta), but it only runs server-side and is tree-shaken from the client bundle.

<read-more to="/docs/4.x/api/composables/use-seo-meta">



</read-more>

For new code, use the server-only pattern directly:

```vue [app/app.vue]
<script setup lang="ts">
if (import.meta.server) {
  useSeoMeta({
    robots: 'index, follow',
  })
}
</script>
```

Parameters are exactly the same as with [`useSeoMeta`](/docs/4.x/api/composables/use-seo-meta).

<read-more to="/docs/4.x/getting-started/seo-meta">



</read-more>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/unjs/unhead/blob/main/packages/vue/src/composables.ts)

## Use Route

# useRoute

> The useRoute composable returns the current route.

<note>

Within the template of a Vue component, you can access the route using `$route`.

</note>

The `useRoute` composable is a wrapper around the identically named composable from `vue-router`, providing access to the current route in a Nuxt application.

The key difference is that in Nuxt, the composable ensures that the route is updated **only after** the page content has changed after navigation.
In contrast, the `vue-router` version updates the route **immediately**, which can lead to synchronization issues between different parts of the template
that rely on the route metadata, for example.

## Example

In the following example, we call an API via [`useFetch`](/docs/4.x/api/composables/use-fetch) using a dynamic page parameter - `slug` - as part of the URL.

```html [~/pages/[slug].vue]
<script setup lang="ts">
const route = useRoute()
const { data: mountain } = await useFetch(`/api/mountains/${route.params.slug}`)
</script>

<template>
  <div>
    <h1>{{ mountain.title }}</h1>
    <p>{{ mountain.description }}</p>
  </div>
</template>
```

If you need to access the route query parameters (for example `example` in the path `/test?example=true`), then you can use `useRoute().query` instead of `useRoute().params`.

## API

Apart from dynamic parameters and query parameters, `useRoute()` also provides the following computed references related to the current route:

- `fullPath`: encoded URL associated with the current route that contains path, query and hash
- `hash`: decoded hash section of the URL that starts with a #
- `query`: access route query parameters
- `matched`: array of normalized matched routes with current route location
- `meta`: custom data attached to the record
- `name`: unique name for the route record
- `path`: encoded pathname section of the URL
- `redirectedFrom`: route location that was attempted to access before ending up on the current route location

## Common Pitfalls

### Route Synchronization Issues

It’s important to use the `useRoute()` composable from Nuxt rather than the one from `vue-router` to avoid synchronization issues during page navigation.
Importing `useRoute` directly from `vue-router` bypasses Nuxt's implementation.

```tstwoslash
// ❌ do not use `useRoute` from `vue-router`
// @errors: 2300
import { useRoute } from 'vue-router'
// ✅ use Nuxt's `useRoute` composable
import { useRoute } from '#app'
```

### Calling `useRoute` in Middleware

Using `useRoute` in middleware is not recommended because it can lead to unexpected behavior.
There is no concept of a "current route" in middleware.
The `useRoute()` composable should only be used in the setup function of a Vue component or in a Nuxt plugin.

<warning>

This applies to any composable that uses `useRoute()` internally too.

</warning>

<read-more to="/docs/4.x/directory-structure/app/middleware">

Read more about accessing the route in the middleware section.

</read-more>

### Hydration Issues with `route.fullPath`

Browsers don't send [URL fragments](https://url.spec.whatwg.org/#concept-url-fragment) (for example `#foo`) when making requests. So using `route.fullPath` to affect the template can trigger hydration issues because this will include the fragment on client but not the server.

<read-more to="https://router.vuejs.org/api/type-aliases/RouteLocationNormalizedLoaded.html" icon="i-simple-icons-vuedotjs">



</read-more>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts)

## Use Router

# useRouter

> The useRouter composable returns the router instance.

```vue [app/pages/index.vue]
<script setup lang="ts">
const router = useRouter()
</script>
```

If you only need the router instance within your template, use `$router`:

```vue [app/pages/index.vue]
<template>
  <button @click="$router.back()">
    Back
  </button>
</template>
```

If you have a `app/pages/` directory, `useRouter` is identical in behavior to the one provided by `vue-router`.

<read-more to="https://router.vuejs.org/api/interfaces/router#Properties-currentRoute-" icon="i-simple-icons-vuedotjs" target="_blank">

Read `vue-router` documentation about the `Router` interface.

</read-more>

## Basic Manipulation

- [`addRoute()`](https://router.vuejs.org/api/interfaces/router#addRoute-): Add a new route to the router instance. `parentName` can be provided to add new route as the child of an existing route.
- [`removeRoute()`](https://router.vuejs.org/api/interfaces/router#removeRoute-): Remove an existing route by its name.
- [`getRoutes()`](https://router.vuejs.org/api/interfaces/router#getRoutes-): Get a full list of all the route records.
- [`hasRoute()`](https://router.vuejs.org/api/interfaces/router#hasRoute-): Checks if a route with a given name exists.
- [`resolve()`](https://router.vuejs.org/api/interfaces/router#resolve-): Returns the normalized version of a route location. Also includes an `href` property that includes any existing base.

```ts [Example]
const router = useRouter()

router.addRoute({ name: 'home', path: '/home', component: Home })
router.removeRoute('home')
router.getRoutes()
router.hasRoute('home')
router.resolve({ name: 'home' })
```

<note>

`router.addRoute()` adds route details into an array of routes and it is useful while building [Nuxt plugins](/docs/4.x/directory-structure/app/plugins) while `router.push()` on the other hand, triggers a new navigation immediately and it is useful in pages, Vue components and composable.

</note>

## Based on History API

- [`back()`](https://router.vuejs.org/api/interfaces/router#back-): Go back in history if possible, same as `router.go(-1)`.
- [`forward()`](https://router.vuejs.org/api/interfaces/router#forward-): Go forward in history if possible, same as `router.go(1)`.
- [`go()`](https://router.vuejs.org/api/interfaces/router#go-): Move forward or backward through the history without the hierarchical restrictions enforced in `router.back()` and `router.forward()`.
- [`push()`](https://router.vuejs.org/api/interfaces/router#push-): Programmatically navigate to a new URL by pushing an entry in the history stack. **It is recommended to use navigateTo instead.**
- [`replace()`](https://router.vuejs.org/api/interfaces/router#replace-): Programmatically navigate to a new URL by replacing the current entry in the routes history stack. **It is recommended to use navigateTo instead.**

```ts [Example]
const router = useRouter()

router.back()
router.forward()
router.go(3)
router.push({ path: '/home' })
router.replace({ hash: '#bio' })
```

<read-more to="https://developer.mozilla.org/en-US/docs/Web/API/History" icon="i-simple-icons-mdnwebdocs" target="_blank">

Read more about the browser's History API.

</read-more>

## Navigation Guards

`useRouter` composable provides `afterEach`, `beforeEach` and `beforeResolve` helper methods that acts as navigation guards.

However, Nuxt has a concept of **route middleware** that simplifies the implementation of navigation guards and provides a better developer experience.

<read-more to="/docs/4.x/directory-structure/app/middleware">



</read-more>

## Promise and Error Handling

- [`isReady()`](https://router.vuejs.org/api/interfaces/router#isReady-): Returns a Promise that resolves when the router has completed the initial navigation.
- [`onError`](https://router.vuejs.org/api/interfaces/router#onError-): Adds an error handler that is called every time a non caught error happens during navigation.

<read-more to="https://router.vuejs.org/api/interfaces/router#Methods-" icon="i-simple-icons-vuedotjs" target="_blank" title="Vue Router Docs">



</read-more>

## Universal Router Instance

If you do not have a `app/pages/` folder, then [`useRouter`](/docs/4.x/api/composables/use-router)  will return a universal router instance with similar helper methods, but be aware that not all features may be supported or behave in exactly the same way as with `vue-router`.

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/router.ts)

## Use Runtime Config

# useRuntimeConfig

> Access runtime config variables with the useRuntimeConfig composable.

## Usage

```vue [app/app.vue]
<script setup lang="ts">
const config = useRuntimeConfig()
</script>
```

```ts [server/api/foo.ts]
export default defineEventHandler((event) => {
  const config = useRuntimeConfig(event)
})
```

<read-more to="/docs/4.x/guide/going-further/runtime-config">



</read-more>

## Define Runtime Config

The example below shows how to set a public API base URL and a secret API token that is only accessible on the server.

We should always define `runtimeConfig` variables inside `nuxt.config`.

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  runtimeConfig: {
    // Private keys are only available on the server
    apiSecret: '123',

    // Public keys that are exposed to the client
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || '/api',
    },
  },
})
```

<note>

Variables that need to be accessible on the server are added directly inside `runtimeConfig`. Variables that need to be accessible on both the client and the server are defined in `runtimeConfig.public`.

</note>

<read-more to="/docs/4.x/guide/going-further/runtime-config">



</read-more>

## Access Runtime Config

To access runtime config, we can use `useRuntimeConfig()` composable:

```ts [server/api/test.ts]
export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig(event)

  // Access public variables
  const result = await $fetch(`/test`, {
    baseURL: config.public.apiBase,
    headers: {
      // Access a private variable (only available on the server)
      Authorization: `Bearer ${config.apiSecret}`,
    },
  })
  return result
})
```

In this example, since `apiBase` is defined within the `public` namespace, it is universally accessible on both server and client-side, while `apiSecret` **is only accessible on the server-side**.

## Environment Variables

It is possible to update runtime config values using a matching environment variable name prefixed with `NUXT_`.

<read-more to="/docs/4.x/guide/going-further/runtime-config">



</read-more>

### Using the `.env` File

We can set the environment variables inside the `.env` file to make them accessible during **development** and **build/generate**.

```ini [.env]
NUXT_PUBLIC_API_BASE = "https://api.localhost:5555"
NUXT_API_SECRET = "123"
```

<note>

Any environment variables set within `.env` file are accessed using `process.env` in the Nuxt app during **development** and **build/generate**.

</note>

<warning>

In **production runtime**, you should use platform environment variables and `.env` is not used.

</warning>

<read-more to="/docs/4.x/directory-structure/env">



</read-more>

## `app` namespace

Nuxt uses `app` namespace in runtime-config with keys including `baseURL` and `cdnURL`. You can customize their values at runtime by setting environment variables.

<note>

This is a reserved namespace. You should not introduce additional keys inside `app`.

</note>

### `app.baseURL`

By default, the `baseURL` is set to `'/'`.

However, the `baseURL` can be updated at runtime by setting the `NUXT_APP_BASE_URL` as an environment variable.

Then, you can access this new base URL using `config.app.baseURL`:

```ts [/plugins/my-plugin.ts]
export default defineNuxtPlugin((NuxtApp) => {
  const config = useRuntimeConfig()

  // Access baseURL universally
  const baseURL = config.app.baseURL
})
```

### `app.cdnURL`

This example shows how to set a custom CDN url and access them using `useRuntimeConfig()`.

You can use a custom CDN for serving static assets inside `.output/public` using the `NUXT_APP_CDN_URL` environment variable.

And then access the new CDN url using `config.app.cdnURL`.

```ts [server/api/foo.ts]
export default defineEventHandler((event) => {
  const config = useRuntimeConfig(event)

  // Access cdnURL universally
  const cdnURL = config.app.cdnURL
})
```

<read-more to="/docs/4.x/guide/going-further/runtime-config">



</read-more>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/nuxt.ts)

## Use App Config

# useAppConfig

> Access the reactive app config defined in the project.

## Usage

```ts
const appConfig = useAppConfig()

console.log(appConfig)
```

<read-more to="/docs/4.x/directory-structure/app/app-config">



</read-more>

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/config.ts)

## Use Nuxt App

# useNuxtApp

> Access the shared runtime context of the Nuxt Application.

`useNuxtApp` is a built-in composable that provides a way to access shared runtime context of Nuxt, also known as the [Nuxt context](/docs/4.x/guide/going-further/nuxt-app#the-nuxt-context), which is available on both client and server side (but not within Nitro routes). It helps you access the Vue app instance, runtime hooks, runtime config variables and internal states, such as `ssrContext` and `payload`.

```vue [app/app.vue]
<script setup lang="ts">
const nuxtApp = useNuxtApp()
</script>
```

If runtime context is unavailable in your scope, `useNuxtApp` will throw an exception when called. You can use [`tryUseNuxtApp`](/docs/4.x/api/composables/use-nuxt-app#tryusenuxtapp) instead for composables that do not require `nuxtApp`, or to simply check if context is available or not without an exception.

## Methods

### `provide (name, value)`

`nuxtApp` is a runtime context that you can extend using [Nuxt plugins](/docs/4.x/directory-structure/app/plugins). Use the `provide` function to create Nuxt plugins to make values and helper methods available in your Nuxt application across all composables and components.

`provide` function accepts `name` and `value` parameters.

```ts
const nuxtApp = useNuxtApp()
nuxtApp.provide('hello', name => `Hello ${name}!`)

// Prints "Hello name!"
console.log(nuxtApp.$hello('name'))
```

As you can see in the example above, `$hello` has become the new and custom part of `nuxtApp` context and it is available in all places where `nuxtApp` is accessible.

### `hook(name, cb)`

Hooks available in `nuxtApp` allows you to customize the runtime aspects of your Nuxt application. You can use runtime hooks in Vue.js composables and [Nuxt plugins](/docs/4.x/directory-structure/app/plugins) to hook into the rendering lifecycle.

`hook` function is useful for adding custom logic by hooking into the rendering lifecycle at a specific point. `hook` function is mostly used when creating Nuxt plugins.

See [Runtime Hooks](/docs/4.x/api/advanced/hooks#app-hooks-runtime) for available runtime hooks called by Nuxt.

```ts [app/plugins/test.ts]
export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.hook('page:start', () => {
    /* your code goes here */
  })
  nuxtApp.hook('vue:error', (..._args) => {
    console.log('vue:error')
    // if (import.meta.client) {
    //   console.log(..._args)
    // }
  })
})
```

### `callHook(name, ...args)`

`callHook` returns a promise when called with any of the existing hooks.

```ts
await nuxtApp.callHook('my-plugin:init')
```

## Properties

`useNuxtApp()` exposes the following properties that you can use to extend and customize your app and share state, data and variables.

### `vueApp`

`vueApp` is the global Vue.js [application instance](https://vuejs.org/api/application#application-api) that you can access through `nuxtApp`.

Some useful methods:

- [`component()`](https://vuejs.org/api/application#app-component) - Registers a global component if passing both a name string and a component definition, or retrieves an already registered one if only the name is passed.
- [`directive()`](https://vuejs.org/api/application#app-directive) - Registers a global custom directive if passing both a name string and a directive definition, or retrieves an already registered one if only the name is passed[(example)](/docs/4.x/directory-structure/app/plugins#vue-directives).
- [`use()`](https://vuejs.org/api/application#app-use) - Installs a **Vue.js Plugin** [(example)](/docs/4.x/directory-structure/app/plugins#vue-plugins).

<read-more to="https://vuejs.org/api/application.html#application-api" icon="i-simple-icons-vuedotjs">



</read-more>

### `ssrContext`

`ssrContext` is generated during server-side rendering and it is only available on the server side.

Nuxt exposes the following properties through `ssrContext`:

- `url` (string) -  Current request url.
- `event` ([h3js/h3](https://github.com/h3js/h3) request event) - Access the request & response of the current route.
- `payload` (object) - NuxtApp payload object.

### `payload`

`payload` exposes data and state variables from server side to client side. The following keys will be available on the client after they have been passed from the server side:

- `serverRendered` (boolean) - Indicates if response is server-side-rendered.
- `data` (object) - When you fetch the data from an API endpoint using either [`useFetch`](/docs/4.x/api/composables/use-fetch) or [`useAsyncData`](/docs/4.x/api/composables/use-async-data) , resulting payload can be accessed from the `payload.data`. This data is cached and helps you prevent fetching the same data in case an identical request is made more than once.<code-group>

```vue [app/app.vue]
<script setup lang="ts">
const { data } = await useAsyncData('count', (_nuxtApp, { signal }) => $fetch('/api/count', { signal }))
</script>
```

```ts [server/api/count.ts]
export default defineEventHandler((event) => {
  return { count: 1 }
})
```

</code-group>

<br />

After fetching the value of `count` using [`useAsyncData`](/docs/4.x/api/composables/use-async-data) in the example above, if you access `payload.data`, you will see `{ count: 1 }` recorded there.<br />

When accessing the same `payload.data` from [`ssrcontext`](/docs/4.x/api/composables/use-nuxt-app#ssrcontext), you can access the same value on the server side as well.
- `state` (object) - When you use [`useState`](/docs/4.x/api/composables/use-state) composable in Nuxt to set shared state, this state data is accessed through `payload.state.[name-of-your-state]`.```ts [app/plugins/my-plugin.ts]
export const useColor = () => useState<string>('color', () => 'pink')

export default defineNuxtPlugin((nuxtApp) => {
  if (import.meta.server) {
    const color = useColor()
  }
})
```

<br />

It is also possible to use more advanced types, such as `ref`, `reactive`, `shallowRef`, `shallowReactive` and `NuxtError`.

#### Custom Reducer/Reviver

Since [Nuxt v3.4](https://nuxt.com/blog/v3-4#payload-enhancements), it is possible to define your own reducer/reviver for types that are not supported by Nuxt.

<video-accordion title="Watch a video from Alexander Lichter about serializing payloads, especially with regards to classes" video-id="8w6ffRBs8a4">



</video-accordion>

In the example below, we define a reducer (or a serializer) and a reviver (or deserializer) for the [Luxon](https://moment.github.io/luxon/#/) DateTime class, using a payload plugin.

```ts [app/plugins/date-time-payload.ts]
/**
 * This kind of plugin runs very early in the Nuxt lifecycle, before we revive the payload.
 * You will not have access to the router or other Nuxt-injected properties.
 *
 * Note that the "DateTime" string is the type identifier and must
 * be the same on both the reducer and the reviver.
 */
export default definePayloadPlugin((nuxtApp) => {
  definePayloadReducer('DateTime', (value) => {
    return value instanceof DateTime && value.toJSON()
  })
  definePayloadReviver('DateTime', (value) => {
    return DateTime.fromISO(value)
  })
})
```

### `isHydrating`

Use `nuxtApp.isHydrating` (boolean) to check if the Nuxt app is hydrating on the client side.

```ts [app/components/nuxt-error-boundary.ts]
export default defineComponent({
  setup (_props, { slots, emit }) {
    const nuxtApp = useNuxtApp()
    onErrorCaptured((err) => {
      if (import.meta.client && !nuxtApp.isHydrating) {
        // ...
      }
    })
  },
})
```

### `runWithContext`

<note>

You are likely here because you got a "Nuxt instance unavailable" message. Please use this method sparingly, and report examples that are causing issues, so that it can ultimately be solved at the framework level.

</note>

The `runWithContext` method is meant to be used to call a function and give it an explicit Nuxt context. Typically, the Nuxt context is passed around implicitly and you do not need to worry about this. However, when working with complex `async`/`await` scenarios in middleware/plugins, you can run into instances where the current instance has been unset after an async call.

```ts [app/middleware/auth.ts]
export default defineNuxtRouteMiddleware(async (to, from) => {
  const nuxtApp = useNuxtApp()
  let user
  try {
    user = await fetchUser()
    // the Vue/Nuxt compiler loses context here because of the try/catch block.
  } catch (e) {
    user = null
  }
  if (!user) {
    // apply the correct Nuxt context to our `navigateTo` call.
    return nuxtApp.runWithContext(() => navigateTo('/auth'))
  }
})
```

#### Usage

```ts
const result = nuxtApp.runWithContext(() => functionWithContext())
```

- `functionWithContext`: Any function that requires the context of the current Nuxt application. This context will be correctly applied automatically.

`runWithContext` will return whatever is returned by `functionWithContext`.

#### A Deeper Explanation of Context

Vue.js Composition API (and Nuxt composables similarly) work by depending on an implicit context. During the lifecycle, Vue sets the temporary instance of the current component (and Nuxt temporary instance of nuxtApp) to a global variable and unsets it in same tick. When rendering on the server side, there are multiple requests from different users and nuxtApp running in a same global context. Because of this, Nuxt and Vue immediately unset this global instance to avoid leaking a shared reference between two users or components.

What it does mean? The Composition API and Nuxt Composables are only available during lifecycle and in same tick before any async operation:

```ts
// --- Vue internal ---
const _vueInstance = null
const getCurrentInstance = () => _vueInstance
// ---

// Vue / Nuxt sets a global variable referencing to current component in _vueInstance when calling setup()
async function setup () {
  getCurrentInstance() // Works
  await someAsyncOperation() // Vue unsets the context in same tick before async operation!
  getCurrentInstance() // null
}
```

The classic solution to this, is caching the current instance on first call to a local variable like `const instance = getCurrentInstance()` and use it in the next composable call but the issue is that any nested composable calls now needs to explicitly accept the instance as an argument and not depend on the implicit context of composition-api. This is design limitation with composables and not an issue per-se.

To overcome this limitation, Vue does some behind the scenes work when compiling our application code and restores context after each call for `<script setup>`:

```ts
const __instance = getCurrentInstance() // Generated by Vue compiler
getCurrentInstance() // Works!
await someAsyncOperation() // Vue unsets the context
__restoreInstance(__instance) // Generated by Vue compiler
getCurrentInstance() // Still works!
```

For a better description of what Vue actually does, see [unjs/unctx#2 (comment)](https://github.com/unjs/unctx/issues/2#issuecomment-942193723).

#### Solution

This is where `runWithContext` can be used to restore context, similarly to how `<script setup>` works.

Nuxt internally uses [unjs/unctx](https://github.com/unjs/unctx) to support composables similar to Vue for plugins and middleware. This enables composables like `navigateTo()` to work without directly passing `nuxtApp` to them - bringing the DX and performance benefits of Composition API to the whole Nuxt framework.

Nuxt composables have the same design as the Vue Composition API and therefore need a similar solution to magically do this transform. Check out [unjs/unctx#2](https://github.com/unjs/unctx/issues/2) (proposal), [unjs/unctx#4](https://github.com/unjs/unctx/pull/4) (transform implementation), and [nuxt/framework#3884](https://github.com/nuxt/framework/pull/3884) (Integration to Nuxt).

Vue currently only supports async context restoration for `<script setup>` for async/await usage. In Nuxt, the transform support for `defineNuxtPlugin()` and `defineNuxtRouteMiddleware()` was added, which means when you use them Nuxt automatically transforms them with context restoration.

#### Remaining Issues

The `unjs/unctx` transformation to automatically restore context seems buggy with `try/catch` statements containing `await` which ultimately needs to be solved in order to remove the requirement of the workaround suggested above.

#### Native Async Context

Using a new experimental feature, it is possible to enable native async context support using [Node.js `AsyncLocalStorage`](https://nodejs.org/api/async_context.html#class-asynclocalstorage) and new unctx support to make async context available **natively** to **any nested async composable** without needing a transform or manual passing/calling with context.

<tip>

Native async context support works currently in Bun and Node.

</tip>

<read-more to="/docs/4.x/guide/going-further/experimental-features#asynccontext">



</read-more>

## tryUseNuxtApp

This function works exactly the same as `useNuxtApp`, but returns `null` if context is unavailable instead of throwing an exception.

You can use it for composables that do not require `nuxtApp`, or to simply check if context is available or not without an exception.

Example usage:

```ts [composable.ts]
export function useStandType () {
  // Always works on the client
  if (tryUseNuxtApp()) {
    return useRuntimeConfig().public.STAND_TYPE
  } else {
    return process.env.STAND_TYPE
  }
}
```

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/nuxt.ts)

## Use Error

# useError

> useError composable returns the global Nuxt error that is being handled.

## Usage

The `useError` composable returns the global Nuxt error that is being handled and is available on both client and server. It provides a reactive, SSR-friendly error state across your app.

```ts
const error = useError()
```

You can use this composable in your components, pages, or plugins to access or react to the current Nuxt error.

## Type

```ts
interface NuxtError<DataT = unknown> {
  status: number
  statusText?: string
  message: string
  data?: DataT
  cause?: unknown
  fatal: boolean
}

export const useError: () => Ref<NuxtError | undefined>
```

## Parameters

This composable does not take any parameters.

## Return Values

Returns a `Ref` containing the current Nuxt error (or `undefined` if there is no error). The error object is reactive and will update automatically when the error state changes.

## Example

```vue
<script setup lang="ts">
const error = useError()

if (error.value) {
  console.error('Nuxt error:', error.value)
}
</script>
```

<read-more to="/docs/4.x/getting-started/error-handling">



</read-more>

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/error.ts)

## Use Request Headers

# useRequestHeaders

> Use useRequestHeaders to access the incoming request headers.

You can use built-in [`useRequestHeaders`](/docs/4.x/api/composables/use-request-headers) composable to access the incoming request headers within your pages, components, and plugins.

```ts
// Get all request headers
const headers = useRequestHeaders()

// Get only cookie request header
const { cookie } = useRequestHeaders(['cookie'])
```

<tip>

In the browser, `useRequestHeaders` will return an empty object.

</tip>

## Example

We can use `useRequestHeaders` to access and proxy the initial request's `authorization` header to any future internal requests during SSR.

The example below adds the `authorization` request header to an isomorphic `$fetch` call.

```vue [app/pages/some-page.vue]
<script setup lang="ts">
const { data } = await useFetch('/api/confidential', {
  headers: useRequestHeaders(['authorization']),
})
</script>
```

<style>

html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts)

## Use Request Url

# useRequestURL

> Access the incoming request URL with the useRequestURL composable.

`useRequestURL` is a helper function that returns an [URL object](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) working on both server-side and client-side.

<important>

When utilizing [Hybrid Rendering](/docs/4.x/guide/concepts/rendering#hybrid-rendering) with cache strategies, all incoming request headers are dropped when handling the cached responses via the [Nitro caching layer](https://nitro.build/guide/cache) (meaning `useRequestURL` will return `localhost` for the `host`).

You can define the [`cache.varies` option](https://nitro.build/guide/cache#options) to specify headers that will be considered when caching and serving the responses, such as `host` and `x-forwarded-host` for multi-tenant environments.

</important>

<code-group>

```vue [app/pages/about.vue]
<script setup lang="ts">
const url = useRequestURL()
</script>

<template>
  <p>URL is: {{ url }}</p>
  <p>Path is: {{ url.pathname }}</p>
</template>
```

```html [Result in development]
<p>URL is: http://localhost:3000/about</p>
<p>Path is: /about</p>
```

</code-group>

<tip icon="i-simple-icons-mdnwebdocs" target="_blank" to="https://developer.mozilla.org/en-US/docs/Web/API/URL#instance_properties">

Read about the URL instance properties on the MDN documentation.

</tip>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/url.ts)

## Use Request Event

# useRequestEvent

> Access the incoming request event with the useRequestEvent composable.

Within the [Nuxt context](/docs/4.x/guide/going-further/nuxt-app#the-nuxt-context) you can use `useRequestEvent` to access the incoming request.

```ts
// Get underlying request event
const event = useRequestEvent()

// Get the URL
const url = event?.path
```

<tip>

In the browser, `useRequestEvent` will return `undefined`.

</tip>

<style>

html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts)

## Use Request Fetch

# useRequestFetch

> Forward the request context and headers for server-side fetch requests with the useRequestFetch composable.

You can use `useRequestFetch` to forward the request context and headers when making server-side fetch requests.

When making a client-side fetch request, the browser automatically sends the necessary headers.
However, when making a request during server-side rendering, due to security considerations, we need to forward the headers manually.

<note>

Headers that are **not meant to be forwarded** will **not be included** in the request. These headers include, for example:
`transfer-encoding`, `connection`, `keep-alive`, `upgrade`, `expect`, `host`, `accept`

</note>

<tip>

The [`useFetch`](/docs/4.x/api/composables/use-fetch) composable uses `useRequestFetch` under the hood to automatically forward the request context and headers.

</tip>

<code-group>

```vue [app/pages/index.vue]
<script setup lang="ts">
// This will forward the user's headers to the `/api/cookies` event handler
// Result: { cookies: { foo: 'bar' } }
const requestFetch = useRequestFetch()
const { data: forwarded } = await useAsyncData(() => requestFetch('/api/cookies'))

// This will NOT forward anything
// Result: { cookies: {} }
const { data: notForwarded } = await useAsyncData((_nuxtApp, { signal }) => $fetch('/api/cookies', { signal }))
</script>
```

```ts [server/api/cookies.ts]
export default defineEventHandler((event) => {
  const cookies = parseCookies(event)

  return { cookies }
})
```

</code-group>

<tip>

In the browser during client-side navigation, `useRequestFetch` will behave just like regular [`$fetch`](/docs/4.x/api/utils/dollarfetch).

</tip>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts)

## Use Request Header

# useRequestHeader

> Use useRequestHeader to access a certain incoming request header.

You can use the built-in [`useRequestHeader`](/docs/4.x/api/composables/use-request-header) composable to access any incoming request header within your pages, components, and plugins.

```ts
// Get the authorization request header
const authorization = useRequestHeader('authorization')
```

<tip>

In the browser, `useRequestHeader` will return `undefined`.

</tip>

## Example

We can use `useRequestHeader` to easily figure out if a user is authorized or not.

The example below reads the `authorization` request header to find out if a person can access a restricted resource.

```ts [app/middleware/authorized-only.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  if (!useRequestHeader('authorization')) {
    return navigateTo('/not-authorized')
  }
})
```

<style>

html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts)

## Use Response Header

# useResponseHeader

> Use useResponseHeader to set a server response header.

<important>

This composable is available in Nuxt v3.14+.

</important>

You can use the built-in [`useResponseHeader`](/docs/4.x/api/composables/use-response-header) composable to set any server response header within your pages, components, and plugins.

```ts
// Set a custom response header
const header = useResponseHeader('X-My-Header')
header.value = 'my-value'
```

## Example

We can use `useResponseHeader` to easily set a response header on a per-page basis.

```vue [app/pages/test.vue]
<script setup>
// pages/test.vue
const header = useResponseHeader('X-My-Header')
header.value = 'my-value'
</script>

<template>
  <h1>Test page with custom header</h1>
  <p>The response from the server for this "/test" page will have a custom "X-My-Header" header.</p>
</template>
```

We can use `useResponseHeader` for example in Nuxt [middleware](/docs/4.x/directory-structure/app/middleware) to set a response header for all pages.

```ts [app/middleware/my-header-middleware.ts]
export default defineNuxtRouteMiddleware((to, from) => {
  const header = useResponseHeader('X-My-Always-Header')
  header.value = `I'm Always here!`
})
```

<style>

html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts)

## Use Hydration

# useHydration

> Allows full control of the hydration cycle to set and receive data from the server.

`useHydration` is a built-in composable that provides a way to set data on the server side every time a new HTTP request is made and receive that data on the client side. This way `useHydration` allows you to take full control of the hydration cycle.

<note>

This is an advanced composable, primarily designed for use within plugins, mostly used by Nuxt modules.

</note>

<note>

`useHydration` is designed to **ensure state synchronization and restoration during SSR**. If you need to create a globally reactive state that is SSR-friendly in Nuxt, [`useState`](/docs/4.x/api/composables/use-state) is the recommended choice.

</note>

## Usage

The data returned from the `get` function on the server is stored in `nuxtApp.payload` under the unique key provided as the first parameter to `useHydration`. During hydration, this data is then retrieved on the client, preventing redundant computations or API calls.

<code-group>

```ts [With useHydration]
export default defineNuxtPlugin((nuxtApp) => {
  const myStore = new MyStore()

  useHydration(
    'myStoreState',
    () => myStore.getState(),
    data => myStore.setState(data),
  )
})
```

```ts [Without useHydration]
export default defineNuxtPlugin((nuxtApp) => {
  const myStore = new MyStore()

  if (import.meta.server) {
    nuxt.hooks.hook('app:rendered', () => {
      nuxtApp.payload.myStoreState = myStore.getState()
    })
  }

  if (import.meta.client) {
    nuxt.hooks.hook('app:created', () => {
      myStore.setState(nuxtApp.payload.myStoreState)
    })
  }
})
```

</code-group>

## Type

```ts [Signature]
export function useHydration<T> (key: string, get: () => T, set: (value: T) => void): void
```

## Parameters

<table>
<thead>
  <tr>
    <th>
      Parameter
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
        key
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      A unique key that identifies the data in your Nuxt application.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        get
      </code>
    </td>
    
    <td>
      <code>
        () => T
      </code>
    </td>
    
    <td>
      A function executed <strong>
        only on the server
      </strong>
      
       (called when SSR rendering is done) to set the initial value.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        set
      </code>
    </td>
    
    <td>
      <code>
        (value: T) => void
      </code>
    </td>
    
    <td>
      A function executed <strong>
        only on the client
      </strong>
      
       (called when initial Vue instance is created) to receive the data.
    </td>
  </tr>
</tbody>
</table>

## Return Values

This composable does not return any value.

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/hydrate.ts)

## Use Loading Indicator

# useLoadingIndicator

> This composable gives you access to the loading state of the app page.

## Description

A composable which returns the loading state of the page. Used by [`<NuxtLoadingIndicator>`](/docs/4.x/api/components/nuxt-loading-indicator) and controllable.
It hooks into [`page:loading:start`](/docs/4.x/api/advanced/hooks#app-hooks-runtime) and [`page:loading:end`](/docs/4.x/api/advanced/hooks#app-hooks-runtime) to change its state.

## Parameters

- `duration`: Duration of the loading bar, in milliseconds (default `2000`).
- `throttle`: Throttle the appearing and hiding, in milliseconds (default `200`).
- `estimatedProgress`: By default Nuxt will back off as it approaches 100%. You can provide a custom function to customize the progress estimation, which is a function that receives the duration of the loading bar (above) and the elapsed time. It should return a value between 0 and 100.

## Properties

### `isLoading`

- **type**: `Readonly<ShallowRef<boolean>>`
- **description**: The loading state

### `error`

- **type**: `Readonly<ShallowRef<boolean>>`
- **description**: The error state

### `progress`

- **type**: `Readonly<ShallowRef<number>>`
- **description**: The progress state. From `0` to `100`.

## Methods

### `start()`

Set `isLoading` to true and start to increase the `progress` value. `start` accepts a `{ force: true }` option to skip the interval and show the loading state immediately.

### `set()`

Set the `progress` value to a specific value. `set` accepts a `{ force: true }` option to skip the interval and show the loading state immediately.

### `finish()`

Set the `progress` value to `100`, stop all timers and intervals then reset the loading state `500` ms later. `finish` accepts a `{ force: true }` option to skip the interval before the state is reset, and `{ error: true }` to change the loading bar color and set the error property to true.

### `clear()`

Used by `finish()`. Clear all timers and intervals used by the composable.

## Example

```vue
<script setup lang="ts">
const { progress, isLoading, start, finish, clear } = useLoadingIndicator({
  duration: 2000,
  throttle: 200,
  // This is how progress is calculated by default
  estimatedProgress: (duration, elapsed) => (2 / Math.PI * 100) * Math.atan(elapsed / duration * 100 / 50),
})
</script>
```

```vue
<script setup lang="ts">
const { start, set } = useLoadingIndicator()
// same as set(0, { force: true })
// set the progress to 0, and show loading immediately
start({ force: true })
</script>
```

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/loading-indicator.ts)

## Use Announcer

# useAnnouncer

> A composable for announcing messages to screen readers.

<important>

This composable is available in Nuxt v4.4.2+.

</important>

## Description

A composable for announcing dynamic content changes to screen readers. Unlike [`useRouteAnnouncer`](/docs/4.x/api/composables/use-route-announcer) which automatically announces route changes, `useAnnouncer` gives you manual control over what and when to announce.

Use this for in-page updates like form validation, async operations, toast notifications, and live content changes.

## Parameters

- `politeness`: Sets the default urgency for screen reader announcements: `off` (disable the announcement), `polite` (waits for silence), or `assertive` (interrupts immediately). (default `polite`)

## Properties

### `message`

- **type**: `Ref<string>`
- **description**: The current message to announce

### `politeness`

- **type**: `Ref<'polite' | 'assertive' | 'off'>`
- **description**: Screen reader announcement urgency level

## Methods

### `set(message, politeness = "polite")`

Sets the message to announce with its urgency level.

### `polite(message)`

Sets the message with `politeness = "polite"`. Use for non-urgent updates that can wait for the screen reader to finish its current task.

### `assertive(message)`

Sets the message with `politeness = "assertive"`. Use for urgent updates that should interrupt the screen reader immediately.

## Example

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

## Use Cases

### Form Validation

```vue [app/components/LoginForm.vue]
<script setup lang="ts">
const { assertive } = useAnnouncer()

function validateForm () {
  const errors = []
  if (!email.value) { errors.push('Email is required') }
  if (!password.value) { errors.push('Password is required') }

  if (errors.length) {
    assertive(`Form has ${errors.length} errors: ${errors.join(', ')}`)
    return false
  }
  return true
}
</script>
```

### Loading States

```vue [app/pages/dashboard.vue]
<script setup lang="ts">
const { polite } = useAnnouncer()

const { data, status } = await useFetch('/api/data')

watch(status, (newStatus) => {
  if (newStatus === 'pending') {
    polite('Loading data...')
  } else if (newStatus === 'success') {
    polite('Data loaded successfully')
  }
})
</script>
```

### Search Results

```vue [app/components/Search.vue]
<script setup lang="ts">
const { polite } = useAnnouncer()

const results = ref([])

watch(results, (newResults) => {
  polite(`Found ${newResults.length} results`)
})
</script>
```

<callout>

You need to add the [`<NuxtAnnouncer>`](/docs/4.x/api/components/nuxt-announcer) component to your app for the announcements to be rendered in the DOM.

</callout>

<callout>

For automatic announcements of route/page changes, use [`useRouteAnnouncer`](/docs/4.x/api/composables/use-route-announcer) with the [`<NuxtRouteAnnouncer>`](/docs/4.x/api/components/nuxt-route-announcer) component instead.

</callout>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/announcer.ts)

## Use Route Announcer

# useRouteAnnouncer

> This composable observes the page title changes and updates the announcer message accordingly.

<important>

This composable is available in Nuxt v3.12+.

</important>

## Description

A composable which observes the page title changes and updates the announcer message accordingly. Used by [`<NuxtRouteAnnouncer>`](/docs/4.x/api/components/nuxt-route-announcer) and controllable.
It hooks into Unhead's `dom:rendered` hook to read the page's title and set it as the announcer message.

## Parameters

- `politeness`: Sets the urgency for screen reader announcements: `off` (disable the announcement), `polite` (waits for silence), or `assertive` (interrupts immediately).  (default `polite`).

## Properties

### `message`

- **type**: `Ref<string>`
- **description**: The message to announce

### `politeness`

- **type**: `Ref<string>`
- **description**: Screen reader announcement urgency level `off`, `polite`, or `assertive`

## Methods

### `set(message, politeness = "polite")`

Sets the message to announce with its urgency level.

### `polite(message)`

Sets the message with `politeness = "polite"`

### `assertive(message)`

Sets the message with `politeness = "assertive"`

## Example

```vue [app/pages/index.vue]
<script setup lang="ts">
const { message, politeness, set, polite, assertive } = useRouteAnnouncer({
  politeness: 'assertive',
})
</script>
```

<callout>

For announcing dynamic in-page content changes (form validation, toasts, loading states), use [`useAnnouncer`](/docs/4.x/api/composables/use-announcer) instead.

</callout>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/route-announcer.ts)

## Use Nuxt Data

# useNuxtData

> Access the current cached value of data fetching composables.

<note>

`useNuxtData` gives you access to the current cached value of [`useAsyncData`](/docs/4.x/api/composables/use-async-data) , [`useLazyAsyncData`](/docs/4.x/api/composables/use-lazy-async-data), [`useFetch`](/docs/4.x/api/composables/use-fetch) and [`useLazyFetch`](/docs/4.x/api/composables/use-lazy-fetch) with explicitly provided key.

</note>

## Usage

The `useNuxtData` composable is used to access the current cached value of data-fetching composables such as `useAsyncData`, `useLazyAsyncData`, `useFetch`, and `useLazyFetch`. By providing the key used during the data fetch, you can retrieve the cached data and use it as needed.

This is particularly useful for optimizing performance by reusing already-fetched data or implementing features like Optimistic Updates or cascading data updates.

To use `useNuxtData`, ensure that the data-fetching composable (`useFetch`, `useAsyncData`, etc.) has been called with an explicitly provided key.

<video-accordion title="Watch a video from LearnVue about useNuxtData" video-id="e-_u6swXRWk">



</video-accordion>

## Params

- `key`: The unique key that identifies the cached data. This key should match the one used during the original data fetch.

## Return Values

- `data`: A reactive reference to the cached data associated with the provided key. If no cached data exists, the value will be `undefined`. This `Ref` automatically updates if the cached data changes, allowing seamless reactivity in your components.

## Example

The example below shows how you can use cached data as a placeholder while the most recent data is being fetched from the server.

```vue [app/pages/posts.vue]
<script setup lang="ts">
// We can access same data later using 'posts' key
const { data } = await useFetch('/api/posts', { key: 'posts' })
</script>
```

```vue [app/pages/posts/[id].vue]
<script setup lang="ts">
// Access to the cached value of useFetch in posts.vue (parent route)
const { data: posts } = useNuxtData('posts')

const route = useRoute()

const { data } = useLazyFetch(`/api/posts/${route.params.id}`, {
  key: `post-${route.params.id}`,
  default () {
    // Find the individual post from the cache and set it as the default value.
    return posts.value.find(post => post.id === route.params.id)
  },
})
</script>
```

## Optimistic Updates

The example below shows how implementing Optimistic Updates can be achieved using useNuxtData.

Optimistic Updates is a technique where the user interface is updated immediately, assuming a server operation will succeed. If the operation eventually fails, the UI is rolled back to its previous state.

```vue [app/pages/todos.vue]
<script setup lang="ts">
// We can access same data later using 'todos' key
const { data } = await useAsyncData('todos', (_nuxtApp, { signal }) => $fetch('/api/todos', { signal }))
</script>
```

```vue [app/components/NewTodo.vue]
<script setup lang="ts">
const newTodo = ref('')
let previousTodos = []

// Access to the cached value of useAsyncData in todos.vue
const { data: todos } = useNuxtData('todos')

async function addTodo () {
  await $fetch('/api/addTodo', {
    method: 'post',
    body: {
      todo: newTodo.value,
    },
    onRequest () {
      // Store the previously cached value to restore if fetch fails.
      previousTodos = todos.value

      // Optimistically update the todos.
      todos.value = [...todos.value, newTodo.value]
    },
    onResponseError () {
      // Rollback the data if the request failed.
      todos.value = previousTodos
    },
    async onResponse () {
      // Invalidate todos in the background if the request succeeded.
      await refreshNuxtData('todos')
    },
  })
}
</script>
```

## Type

```ts [Signature]
export function useNuxtData<DataT = any> (key: string): { data: Ref<DataT | undefined> }
```

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/asyncData.ts)

## Use Preview Mode

# `usePreviewMode`

Preview mode allows you to see how your changes would be displayed on a live site without revealing them to users.

You can use the built-in `usePreviewMode` composable to access and control preview state in Nuxt. If the composable detects preview mode it will automatically force any updates necessary for [`useAsyncData`](/docs/4.x/api/composables/use-async-data) and [`useFetch`](/docs/4.x/api/composables/use-fetch) to rerender preview content.

```ts
const { enabled, state } = usePreviewMode()
```

## Options

### Custom `enable` check

You can specify a custom way to enable preview mode. By default the `usePreviewMode` composable will enable preview mode if there is a `preview` param in url that is equal to `true` (for example, `http://localhost:3000?preview=true`). You can wrap the `usePreviewMode` into custom composable, to keep options consistent across usages and prevent any errors.

```ts
export function useMyPreviewMode () {
  const route = useRoute()
  return usePreviewMode({
    shouldEnable: () => {
      return !!route.query.customPreview
    },
  })
}
```

### Modify default state

`usePreviewMode` will try to store the value of a `token` param from url in state. You can modify this state and it will be available for all [`usePreviewMode`](/docs/4.x/api/composables/use-preview-mode) calls.

```ts
const data1 = ref('data1')

const { enabled, state } = usePreviewMode({
  getState: (currentState) => {
    return { data1, data2: 'data2' }
  },
})
```

<note>

The `getState` function will append returned values to current state, so be careful not to accidentally overwrite important state.

</note>

### Customize the `onEnable` and `onDisable` callbacks

By default, when `usePreviewMode` is enabled, it will call `refreshNuxtData()` to re-fetch all data from the server.

When preview mode is disabled, the composable will attach a callback to call `refreshNuxtData()` to run after a subsequent router navigation.

You can specify custom callbacks to be triggered by providing your own functions for the `onEnable` and `onDisable` options.

```ts
const { enabled, state } = usePreviewMode({
  onEnable: () => {
    console.log('preview mode has been enabled')
  },
  onDisable: () => {
    console.log('preview mode has been disabled')
  },
})
```

## Example

The example below creates a page where part of a content is rendered only in preview mode.

```vue [app/pages/some-page.vue]
<script setup>
const { enabled, state } = usePreviewMode()

const { data } = await useFetch('/api/preview', {
  query: {
    apiKey: state.token,
  },
})
</script>

<template>
  <div>
    Some base content
    <p v-if="enabled">
      Only preview content: {{ state.token }}
      <br>
      <button @click="enabled = false">
        disable preview mode
      </button>
    </p>
  </div>
</template>
```

Now you can generate your site and serve it:

```bash [Terminal]
npx nuxt generate
npx nuxt preview
```

Then you can see your preview page by adding the query param `preview` to the end of the page you want to see once, for example `http://localhost:3000/?preview=true`.

<note>

`usePreviewMode` should be tested locally with `nuxt generate` and then `nuxt preview` rather than `nuxt dev`. (The [preview command](/docs/4.x/api/commands/preview) is not related to preview mode.)

</note>

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/preview.ts)

## Use Head Safe

# useHeadSafe

> The recommended way to provide head data with user input.

## Usage

The `useHeadSafe` composable is a wrapper around the [`useHead`](/docs/4.x/api/composables/use-head) composable that restricts the input to only allow safe values. This is the recommended way to manage head data when working with user input, as it prevents XSS attacks by sanitizing potentially dangerous attributes.

<warning>

When using `useHeadSafe`, potentially dangerous attributes like `innerHTML` in scripts or `http-equiv` in meta tags are automatically stripped out to prevent XSS attacks. Use this composable whenever you're working with user-generated content.

</warning>

## Type

```ts [Signature]
export function useHeadSafe (input: MaybeComputedRef<HeadSafe>): void
```

### Allowed Attributes

The following attributes are whitelisted for each head element type:

```ts
const WhitelistAttributes = {
  htmlAttrs: ['class', 'style', 'lang', 'dir'],
  bodyAttrs: ['class', 'style'],
  meta: ['name', 'property', 'charset', 'content', 'media'],
  noscript: ['textContent'],
  style: ['media', 'textContent', 'nonce', 'title', 'blocking'],
  script: ['type', 'textContent', 'nonce', 'blocking'],
  link: ['color', 'crossorigin', 'fetchpriority', 'href', 'hreflang', 'imagesrcset', 'imagesizes', 'integrity', 'media', 'referrerpolicy', 'rel', 'sizes', 'type'],
}
```

See [@unhead/vue](https://github.com/unjs/unhead/blob/main/packages/vue/src/types/safeSchema.ts) for more detailed types.

## Parameters

`input`: A `MaybeComputedRef<HeadSafe>` object containing head data. You can pass all the same values as [`useHead`](/docs/4.x/api/composables/use-head), but only safe attributes will be rendered.

## Return Values

This composable does not return any value.

## Example

```vue [app/pages/user-profile.vue]
<script setup lang="ts">
// User-generated content that might contain malicious code
const userBio = ref('<script>alert("xss")<' + '/script>')

useHeadSafe({
  title: `User Profile`,
  meta: [
    {
      name: 'description',
      content: userBio.value, // Safely sanitized
    },
  ],
})
</script>
```

<read-more target="_blank" to="https://unhead.unjs.io/docs/typescript/head/api/composables/use-head-safe">

Read more on the `Unhead` documentation.

</read-more>

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/unjs/unhead/blob/main/packages/vue/src/composables.ts)

## Use Runtime Hook

# useRuntimeHook

> Registers a runtime hook in a Nuxt application and ensures it is properly disposed of when the scope is destroyed.

<important>

This composable is available in Nuxt v3.14+.

</important>

```ts [signature]
function useRuntimeHook<THookName extends keyof RuntimeNuxtHooks> (
  name: THookName,
  fn: RuntimeNuxtHooks[THookName] extends HookCallback ? RuntimeNuxtHooks[THookName] : never,
): void
```

## Usage

### Parameters

- `name`: The name of the runtime hook to register. You can see the full list of [runtime Nuxt hooks here](/docs/4.x/api/advanced/hooks#app-hooks-runtime).
- `fn`: The callback function to execute when the hook is triggered. The function signature varies based on the hook name.

### Returns

The composable doesn't return a value, but it automatically unregisters the hook when the component's scope is destroyed.

## Example

```vue [pages/index.vue]twoslash
<script setup lang="ts">
// Register a hook that runs every time a link is prefetched, but which will be
// automatically cleaned up (and not called again) when the component is unmounted
useRuntimeHook('link:prefetch', (link) => {
  console.log('Prefetching', link)
})
</script>
```

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/runtime-hook.ts)

## On Prehydrate

# onPrehydrate

> Use onPrehydrate to run a callback on the client immediately before Nuxt hydrates the page.

<important>

This composable is available in Nuxt v3.12+.

</important>

`onPrehydrate` is a composable lifecycle hook that allows you to run a callback on the client immediately before Nuxt hydrates the page.

<note>

This is an advanced utility and should be used with care. For example, [`nuxt-time`](https://github.com/danielroe/nuxt-time/pull/251) and [`@nuxtjs/color-mode`](https://github.com/nuxt-modules/color-mode/blob/main/src/script.js) manipulate the DOM to avoid hydration mismatches.

</note>

## Usage

Call `onPrehydrate` in the setup function of a Vue component (e.g., in `<script setup>`) or in a plugin. It only has an effect when called on the server and will not be included in your client build.

## Type

```ts [Signature]
export function onPrehydrate (callback: (el: HTMLElement) => void): void
export function onPrehydrate (callback: string | ((el: HTMLElement) => void), key?: string): undefined | string
```

## Parameters

<table>
<thead>
  <tr>
    <th>
      Parameter
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
        callback
      </code>
    </td>
    
    <td>
      <code>
        ((el: HTMLElement) => void) | string
      </code>
    </td>
    
    <td>
      Yes
    </td>
    
    <td>
      A function (or stringified function) to run before Nuxt hydrates. It will be stringified and inlined in the HTML. Should not have external dependencies or reference variables outside the callback. Runs before Nuxt runtime initializes, so it should not rely on Nuxt or Vue context.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        key
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      No
    </td>
    
    <td>
      (Advanced) A unique key to identify the prehydrate script, useful for advanced scenarios like multiple root nodes.
    </td>
  </tr>
</tbody>
</table>

## Return Values

- Returns `undefined` when called with only a callback function.
- Returns a string (the prehydrate id) when called with a callback and a key, which can be used to set or access the `data-prehydrate-id` attribute for advanced use cases.

## Example

```vue [app/app.vue]twoslash
<script setup lang="ts">
declare const window: Window
// ---cut---
// Run code before Nuxt hydrates
onPrehydrate(() => {
  console.log(window)
})

// Access the root element
onPrehydrate((el) => {
  console.log(el.outerHTML)
  // <div data-v-inspector="app.vue:15:3" data-prehydrate-id=":b3qlvSiBeH:"> Hi there </div>
})

// Advanced: access/set `data-prehydrate-id` yourself
const prehydrateId = onPrehydrate((el) => {})
</script>

<template>
  <div>
    Hi there
  </div>
</template>
```

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/ssr.ts)

## Create Use Async Data

# createUseAsyncData

> A factory function to create a custom useAsyncData composable with pre-defined default options.

`createUseAsyncData` creates a custom [`useAsyncData`](/docs/4.x/api/composables/use-async-data) composable with pre-defined options. The resulting composable is fully typed and works exactly like `useAsyncData`, but with your defaults baked in.

<note>

`createUseAsyncData` is a compiler macro. It must be used as an **exported** declaration in the `composables/` directory (or any directory scanned by the Nuxt compiler). Nuxt automatically injects de-duplication keys at build time.

</note>

## Usage

```ts [app/composables/useCachedData.ts]
export const useCachedData = createUseAsyncData({
  getCachedData (key, nuxtApp) {
    return nuxtApp.payload.data[key] ?? nuxtApp.static.data[key]
  },
})
```

```vue [app/pages/index.vue]
<script setup lang="ts">
const { data: mountains } = await useCachedData(
  'mountains',
  () => $fetch('https://api.nuxtjs.dev/mountains'),
)
</script>
```

The resulting composable has the same signature and return type as [`useAsyncData`](/docs/4.x/api/composables/use-async-data), with all options available for the caller to use or override.

## Type

```ts [Signature]
function createUseAsyncData (
  options?: Partial<AsyncDataOptions>,
): typeof useAsyncData

function createUseAsyncData (
  options: (callerOptions: AsyncDataOptions) => Partial<AsyncDataOptions>,
): typeof useAsyncData
```

## Options

`createUseAsyncData` accepts all the same options as [`useAsyncData`](/docs/4.x/api/composables/use-async-data#params), including `server`, `lazy`, `immediate`, `default`, `transform`, `pick`, `getCachedData`, `deep`, `dedupe`, `timeout`, and `watch`.

See the full list of options in the [`useAsyncData` documentation](/docs/4.x/api/composables/use-async-data#params).

## Default vs Override Mode

### Default Mode (plain object)

When you pass a plain object, the factory options act as **defaults**. Callers can override any option:

```ts [app/composables/useLazyData.ts]
export const useLazyData = createUseAsyncData({
  lazy: true,
  server: false,
})
```

```ts
// Uses the defaults (lazy: true, server: false)
const { data } = await useLazyData('key', () => fetchSomeData())

// Caller overrides server to true
const { data } = await useLazyData('key', () => fetchSomeData(), { server: true })
```

### Override Mode (function)

When you pass a function, the factory options **override** the caller's options. The function receives the caller's options as its argument:

```ts [app/composables/useStrictData.ts]
// deep is always enforced as false
export const useStrictData = createUseAsyncData(callerOptions => ({
  deep: false,
}))
```

<read-more to="/docs/4.x/guide/recipes/custom-usefetch">



</read-more>

<read-more to="/docs/4.x/api/composables/use-async-data">



</read-more>

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/asyncData.ts)

## Create Use Fetch

# createUseFetch

> A factory function to create a custom useFetch composable with pre-defined default options.

`createUseFetch` creates a custom [`useFetch`](/docs/4.x/api/composables/use-fetch) composable with pre-defined options. The resulting composable is fully typed and works exactly like `useFetch`, but with your defaults baked in.

<note>

`createUseFetch` is a compiler macro. It must be used as an **exported** declaration in the `composables/` directory (or any directory scanned by the Nuxt compiler). Nuxt automatically injects de-duplication keys at build time.

</note>

## Usage

```ts [app/composables/useAPI.ts]
export const useAPI = createUseFetch({
  baseURL: 'https://api.nuxt.com',
})
```

```vue [app/pages/modules.vue]
<script setup lang="ts">
const { data: modules } = await useAPI('/modules')
</script>
```

The resulting `useAPI` composable has the same signature and return type as [`useFetch`](/docs/4.x/api/composables/use-fetch), with all options available for the caller to use or override.

## Type

```ts [Signature]
function createUseFetch (
  options?: Partial<UseFetchOptions>,
): typeof useFetch

function createUseFetch (
  options: (callerOptions: UseFetchOptions) => Partial<UseFetchOptions>,
): typeof useFetch
```

## Options

`createUseFetch` accepts all the same options as [`useFetch`](/docs/4.x/api/composables/use-fetch#parameters), including `baseURL`, `headers`, `query`, `onRequest`, `onResponse`, `server`, `lazy`, `transform`, `getCachedData`, and more.

See the full list of options in the [`useFetch` documentation](/docs/4.x/api/composables/use-fetch#parameters).

## Default vs Override Mode

### Default Mode (plain object)

When you pass a plain object, the factory options act as **defaults**. Callers can override any option:

```ts [app/composables/useAPI.ts]
export const useAPI = createUseFetch({
  baseURL: 'https://api.nuxt.com',
  lazy: true,
})
```

```ts
// Uses the default baseURL
const { data } = await useAPI('/modules')

// Caller overrides the baseURL
const { data } = await useAPI('/modules', { baseURL: 'https://other-api.com' })
```

### Override Mode (function)

When you pass a function, the factory options **override** the caller's options. The function receives the caller's options as its argument, so you can read them to compute your overrides:

```ts [app/composables/useAPI.ts]
// baseURL is always enforced, regardless of what the caller passes
export const useAPI = createUseFetch(callerOptions => ({
  baseURL: 'https://api.nuxt.com',
}))
```

This is useful for enforcing settings like authentication headers or a specific base URL that should not be changed by the caller.

## Combining with a Custom `$fetch`

You can pass a custom `$fetch` instance to `createUseFetch`:

```ts [app/composables/useAPI.ts]
export const useAPI = createUseFetch(callerOptions => ({
  $fetch: useNuxtApp().$api as typeof $fetch,
  ...callerOptions,
}))
```

<important>

The **function signature** (override mode) is required here so that [`useNuxtApp()`](/docs/4.x/api/composables/use-nuxt-app) is called in the setup context (at the composable call site) rather than in the module scope, where no Nuxt instance is available.

</important>

<read-more to="/docs/4.x/guide/recipes/custom-usefetch">



</read-more>

<read-more to="/docs/4.x/api/composables/use-fetch">



</read-more>

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/composables/fetch.ts)