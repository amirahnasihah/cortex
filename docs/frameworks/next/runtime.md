# runtime

The `runtime` option allows you to select the JavaScript runtime used for rendering your route.

```tsx filename="layout.tsx | page.tsx | route.ts" switcher
export const runtime = 'nodejs'
// 'nodejs' | 'edge'
```

```js filename="layout.js | page.js | route.js" switcher
export const runtime = 'nodejs'
// 'nodejs' | 'edge'
```

* **`'nodejs'`** (default)
* **`'edge'`**

> **Good to know**:
>
> * Using `runtime: 'edge'` is **not supported** for Cache Components.
> * This option cannot be used in [Proxy](/docs/app/api-reference/file-conventions/proxy).