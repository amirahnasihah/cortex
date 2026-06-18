# Astro - Integrations


## React

#

 @astrojs/
 react

 v5.0.7

 GitHub

 npm

 Changelog

 This Astro integration enables rendering and client-side hydration for your React components.

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

To install `@astrojs/react`, run the following from your project directory and follow the prompts:

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add react `

 Terminal window
```
` pnpm astro add react `
```

 Terminal window
```
` yarn astro add react `
```

 If you run into any issues, feel free to report them to us on GitHub and try the manual installation steps below.

### Manual Install
 Section titled “Manual Install”
 First, install the `@astrojs/react` package:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/react `

 Terminal window
```
` pnpm add @astrojs/react `
```

 Terminal window
```
` yarn add @astrojs/react `
```

 Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'react'` (or similar) warning when you start up Astro, you’ll need to install `react` and `react-dom` with its type definitions:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install react react-dom @types/react @types/react-dom `

 Terminal window
```
` pnpm add react react-dom @types/react @types/react-dom `
```

 Terminal window
```
` yarn add react react-dom @types/react @types/react-dom `
```

 Then, apply the integration to your `astro.config.*` file using the `integrations` property:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import react from ' @astrojs/react ' ;
 export default defineConfig ({ // ... integrations: [ react () ], }); `
 And add the following code to the `tsconfig.json` file.

 tsconfig.json ` { "extends" : " astro/tsconfigs/strict " , "include" : [ " .astro/types.d.ts " , " **/* " ], "exclude" : [ " dist " ], "compilerOptions" : { "jsx" : " react-jsx " , "jsxImportSource" : " react " } } `

## Getting started
 Section titled “Getting started”
 To use your first React component in Astro, head to our UI framework documentation . You’ll explore:

- 📦 how framework components are loaded,

- 💧 client-side hydration options, and

- 🤝 opportunities to mix and nest frameworks together

## Integrate Actions with `useActionState()`
 Section titled “Integrate Actions with useActionState()”
 The `@astrojs/react` integration provides two functions for use with Astro Actions : `withState()` and `getActionState()`.

These are used with React’s useActionState() hook to read and update client-side state when triggering actions during form submission.

### `withState()`
 Section titled “withState()”
 Type: `(action: FormFn<T>) => (state: T, formData: FormData) => FormFn<T>`

 Added in:
 `@astrojs/react@4.4.0`

You can pass `withState()` and the action you want to trigger to React’s `useActionState()` hook as the form action function. The example below passes a `like` action to increase a counter along with an initial state of `0` likes.

 Like.tsx ` import { actions } from ' astro:actions ' ; import { withState } from ' @astrojs/react/actions ' ; import { useActionState } from " react " ;
 export function Like ( { postId } : { postId : string } ) { const [ state , action , pending ] = useActionState ( withState ( actions . like ) , { data: 0 , error: undefined } , // initial likes and errors );
 return ( &#x3C; form action = { action } > &#x3C; input type = " hidden " name = " postId " value = { postId } /> &#x3C; button disabled = { pending } > { state . data } ❤️ &#x3C;/ button > &#x3C;/ form > ); } `   {state.data} ❤️   );}">
 The `withState()` function will match the action’s types with React’s expectations and preserve metadata used for progressive enhancement, allowing it to work even when JavaScript is disabled on the user’s device.

### `getActionState()`
 Section titled “getActionState()”
 Type: `(context: ActionAPIContext) => Promise<T>`

 Added in:
 `@astrojs/react@4.4.0`

You can access the state stored by `useActionState()` on the server in your action `handler` with `getActionState()`. It accepts the Astro API context , and optionally, you can apply a type to the result.

The example below gets the current value of likes from a counter, typed as a number, in order to create an incrementing `like` action:

 actions.ts ` import { defineAction, type SafeResult } from ' astro:actions ' ; import { z } from ' astro/zod ' ; import { getActionState } from ' @astrojs/react/actions ' ;
 export const server = { like: defineAction ( { input: z . object ( { postId: z . string () , } ) , handler : async ( { postId }, ctx ) => { const { data : currentLikes = 0 , error } = await getActionState &#x3C; SafeResult &#x3C; any , number >> (ctx) ;
 // handle errors if (error) throw error ;
 // write to database return currentLikes + 1 ; }, } ) } ; ` { const { data: currentLikes = 0, error } = await getActionState >(ctx); // handle errors if (error) throw error; // write to database return currentLikes + 1; }, })};">

## Options
 Section titled “Options”

### Combining multiple JSX frameworks
 Section titled “Combining multiple JSX frameworks”
 When you are using multiple JSX frameworks (React, Preact, Solid) in the same project, Astro needs to determine which JSX framework-specific transformations should be used for each of your components. If you have only added one JSX framework integration to your project, no extra configuration is needed.

Use the `include` (required) and `exclude` (optional) configuration options to specify which files belong to which framework. Provide an array of files and/or folders to `include` for each framework you are using. Wildcards may be used to include multiple file paths.

We recommend placing common framework components in the same folder (e.g. `/components/react/` and `/components/solid/`) to make specifying your includes easier, but this is not required:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import preact from ' @astrojs/preact ' ; import react from ' @astrojs/react ' ; import svelte from ' @astrojs/svelte ' ; import vue from ' @astrojs/vue ' ; import solid from ' @astrojs/solid-js ' ;
 export default defineConfig ({ // Enable many frameworks to support all different kinds of components. // No `include` is needed if you are only using a single JSX framework! integrations: [ preact ({ include: [ ' **/preact/* ' ], }), react ({ include: [ ' **/react/* ' ], }), solid ({ include: [ ' **/solid/* ' ], }), ], }); `

### Children parsing
 Section titled “Children parsing”
 Children passed into a React component from an Astro component are parsed as plain strings, not React nodes.

For example, the `&#x3C;ReactComponent />` below will only receive a single child element:

 ` --- import ReactComponent from ' ./ReactComponent ' ; ---
 &#x3C; ReactComponent > &#x3C; div > one &#x3C;/ div > &#x3C; div > two &#x3C;/ div > &#x3C;/ ReactComponent > `  one  two  ">
 If you are using a library that expects more than one child element to be passed, for example so that it can slot certain elements in different places, you might find this to be a blocker.

You can set the experimental flag `experimentalReactChildren` to tell Astro to always pass children to React as React virtual DOM nodes. There is some runtime cost to this, but it can help with compatibility.

You can enable this option in the configuration for the React integration:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import react from ' @astrojs/react ' ;
 export default defineConfig ({ // ... integrations: [ react ({ experimentalReactChildren: true , }), ], }); `

### Disable streaming (experimental)
 Section titled “Disable streaming (experimental)”
 Astro streams the output of React components by default. However, you can disable this behavior by enabling the `experimentalDisableStreaming` option. This is particularly helpful for supporting libraries that don’t work well with streaming, like some CSS-in-JS solutions.

To disable streaming for all React components in your project, configure `@astrojs/react` with `experimentalDisableStreaming: true`:

 astro.config.mjs
```
` import { defineConfig } from ' astro/config ' ; import react from ' @astrojs/react ' ;
 export default defineConfig ({ // ... integrations: [ react ({ experimentalDisableStreaming: true , }) ] }); `
```

## More integrations

### Front-end frameworks

 -

###

 @astrojs/ alpinejs

-

###

 @astrojs/ preact

-

###

 @astrojs/ react

-

###

 @astrojs/ solid⁠-⁠js

-

###

 @astrojs/ svelte

-

###

 @astrojs/ vue

### Adapters

 -

###

 @astrojs/ cloudflare

-

###

 @astrojs/ netlify

-

###

 @astrojs/ node

-

###

 @astrojs/ vercel

### Other integrations

 -

###

 @astrojs/ db

-

###

 @astrojs/ markdoc

-

###

 @astrojs/ mdx

-

###

 @astrojs/ partytown

-

###

 @astrojs/ sitemap

 Learn

 Contribute

 Community

 Sponsor

## Vue

#

 @astrojs/
 vue

 v6.0.1

 GitHub

 npm

 Changelog

 This Astro integration enables rendering and client-side hydration for your Vue 3 components.

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

To install `@astrojs/vue`, run the following from your project directory and follow the prompts:

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add vue `

 Terminal window
```
` pnpm astro add vue `
```

 Terminal window
```
` yarn astro add vue `
```

 If you run into any issues, feel free to report them to us on GitHub and try the manual installation steps below.

### Manual Install
 Section titled “Manual Install”
 First, install the `@astrojs/vue` package:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/vue `

 Terminal window
```
` pnpm add @astrojs/vue `
```

 Terminal window
```
` yarn add @astrojs/vue `
```

 Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'vue'` (or similar) warning when you start up Astro, you’ll need to install Vue:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install vue `

 Terminal window
```
` pnpm add vue `
```

 Terminal window
```
` yarn add vue `
```

 Then, apply the integration to your `astro.config.*` file using the `integrations` property:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vue from ' @astrojs/vue ' ;
 export default defineConfig ({ // ... integrations: [ vue () ], }); `

## Getting started
 Section titled “Getting started”
 To use your first Vue component in Astro, head to our UI framework documentation . You’ll explore:

- 📦 how framework components are loaded,

- 💧 client-side hydration options, and

- 🤝 opportunities to mix and nest frameworks together

## Troubleshooting
 Section titled “Troubleshooting”
 For help, check out the `#support` channel on Discord . Our friendly Support Squad members are here to help!

You can also check our Astro Integration Documentation for more on integrations.

## Contributing
 Section titled “Contributing”
 This package is maintained by Astro’s Core team. You’re welcome to submit an issue or PR!

## Options
 Section titled “Options”
 This integration is powered by `@vitejs/plugin-vue`. To customize the Vue compiler, options can be provided to the integration. See the `@vitejs/plugin-vue` docs for more details.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vue from ' @astrojs/vue ' ;
 export default defineConfig ({ // ... integrations: [ vue ({ template: { compilerOptions: { // treat any tag that starts with ion- as custom elements isCustomElement : ( tag ) => tag . startsWith ( ' ion- ' ), }, }, // ... }), ], }); ` tag.startsWith(&#x27;ion-&#x27;), }, }, // ... }), ],});">

### `appEntrypoint`
 Section titled “appEntrypoint”
 Type: `string`

 Added in:
 `@astrojs/vue@1.2.0`

You can extend the Vue `app` instance setting the `appEntrypoint` option to a root-relative import specifier (for example, `appEntrypoint: "/src/pages/_app"`).

The default export of this file should be a function that accepts a Vue `App` instance prior to rendering, allowing the use of custom Vue plugins , `app.use`, and other customizations for advanced use cases.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vue from ' @astrojs/vue ' ;
 export default defineConfig ({ // ... integrations: [ vue ({ appEntrypoint: ' /src/pages/_app ' })], }); `
 src/pages/_app.ts
```
` import type { App } from ' vue ' ; import i18nPlugin from ' my-vue-i18n-plugin ' ;
 export default ( app : App ) => { app . use (i18nPlugin); }; `
```
 { app.use(i18nPlugin);};">

### `jsx`
 Section titled “jsx”
 Type: `boolean | object`

 Added in:
 `@astrojs/vue@1.2.0`

You can use Vue JSX by setting `jsx: true`.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vue from ' @astrojs/vue ' ;
 export default defineConfig ({ // ... integrations: [ vue ({ jsx: true })], }); `
 This will enable rendering for both Vue and Vue JSX components. To customize the Vue JSX compiler, pass an options object instead of a boolean. See the `@vitejs/plugin-vue-jsx` docs for more details.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vue from ' @astrojs/vue ' ;
 export default defineConfig ({ // ... integrations: [ vue ({ jsx: { // treat any tag that starts with ion- as custom elements isCustomElement : ( tag ) => tag . startsWith ( ' ion- ' ), }, }), ], }); ` tag.startsWith(&#x27;ion-&#x27;), }, }), ],});">

### `devtools`
 Section titled “devtools”
 Type: `boolean | object`

 Added in:
 `@astrojs/vue@4.2.0`

You can enable Vue DevTools in development by passing an object with `devtools: true` to your `vue()` integration config:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vue from ' @astrojs/vue ' ;
 export default defineConfig ({ // ... integrations: [ vue ({ devtools: true })], }); `

#### Customizing Vue DevTools
 Section titled “Customizing Vue DevTools”

 Added in:
 `@astrojs/vue@4.3.0`

For more customization, you can instead pass options that the Vue DevTools Vite Plugin supports. (Note: `appendTo` is not supported.)

For example, you can set `launchEditor` to your preferred editor if you are not using Visual Studio Code:

 astro.config.mjs
```
` import { defineConfig } from " astro/config " ; import vue from " @astrojs/vue " ;
 export default defineConfig ({ // ... integrations: [ vue ({ devtools: { launchEditor: " webstorm " }, }), ], }); `
```

## More integrations

### Front-end frameworks

 -

###

 @astrojs/ alpinejs

-

###

 @astrojs/ preact

-

###

 @astrojs/ react

-

###

 @astrojs/ solid⁠-⁠js

-

###

 @astrojs/ svelte

-

###

 @astrojs/ vue

### Adapters

 -

###

 @astrojs/ cloudflare

-

###

 @astrojs/ netlify

-

###

 @astrojs/ node

-

###

 @astrojs/ vercel

### Other integrations

 -

###

 @astrojs/ db

-

###

 @astrojs/ markdoc

-

###

 @astrojs/ mdx

-

###

 @astrojs/ partytown

-

###

 @astrojs/ sitemap

 Learn

 Contribute

 Community

 Sponsor

## Svelte

#

 @astrojs/
 svelte

 v8.1.2

 GitHub

 npm

 Changelog

 This Astro integration enables rendering and client-side hydration for your Svelte 5 components. For Svelte 3 and 4 support, install `@astrojs/svelte@5` instead.

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

To install `@astrojs/svelte`, run the following from your project directory and follow the prompts:

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add svelte `

 Terminal window
```
` pnpm astro add svelte `
```

 Terminal window
```
` yarn astro add svelte `
```

 If you run into any issues, feel free to report them to us on GitHub and try the manual installation steps below.

### Manual Install
 Section titled “Manual Install”
 First, install the `@astrojs/svelte` package:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/svelte `

 Terminal window
```
` pnpm add @astrojs/svelte `
```

 Terminal window
```
` yarn add @astrojs/svelte `
```

 Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'svelte'` (or similar) warning when you start up Astro, you’ll need to install Svelte and TypeScript:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install svelte typescript `

 Terminal window
```
` pnpm add svelte typescript `
```

 Terminal window
```
` yarn add svelte typescript `
```

 Then, apply the integration to your `astro.config.*` file using the `integrations` property:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import svelte from ' @astrojs/svelte ' ;
 export default defineConfig ({ // ... integrations: [ svelte () ], }); `
 And create a new file called `svelte.config.js` in your project root directory and add the following code:

 svelte.config.js ` import { vitePreprocess } from ' @astrojs/svelte ' ;
 export default { preprocess: vitePreprocess (), } `

## Getting started
 Section titled “Getting started”
 To use your first Svelte component in Astro, head to our UI framework documentation . You’ll explore:

- 📦 how framework components are loaded,

- 💧 client-side hydration options, and

- 🤝 opportunities to mix and nest frameworks together

## Options
 Section titled “Options”
 This integration is powered by `@sveltejs/vite-plugin-svelte`. To customize the Svelte compiler, options can be provided to the integration. See the `@sveltejs/vite-plugin-svelte` docs for more details.

You can set options either by passing them to the `svelte` integration in `astro.config.mjs` or in `svelte.config.js`. The options in `astro.config.mjs` will take precedence over the options in `svelte.config.js` if both are present:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import svelte from ' @astrojs/svelte ' ;
 export default defineConfig ({ integrations: [ svelte ({ extensions: [ ' .svelte ' ] })], }); `
 svelte.config.js
```
` export default { extensions: [ ' .svelte ' ], }; `
```

## Preprocessors
 Section titled “Preprocessors”

 Added in:
 `@astrojs/svelte@2.0.0`

 If you’re using SCSS or Stylus in your Svelte files, you can create a `svelte.config.js` file so that they are preprocessed by Svelte, and the Svelte IDE extension can correctly parse the Svelte files.

 svelte.config.js ` import { vitePreprocess } from ' @astrojs/svelte ' ;
 export default { preprocess: vitePreprocess (), }; `
 This config file will be automatically added for you when you run `astro add svelte`. See the `@sveltejs/vite-plugin-svelte` docs for more details about `vitePreprocess`.

## More integrations

### Front-end frameworks

 -

###

 @astrojs/ alpinejs

-

###

 @astrojs/ preact

-

###

 @astrojs/ react

-

###

 @astrojs/ solid⁠-⁠js

-

###

 @astrojs/ svelte

-

###

 @astrojs/ vue

### Adapters

 -

###

 @astrojs/ cloudflare

-

###

 @astrojs/ netlify

-

###

 @astrojs/ node

-

###

 @astrojs/ vercel

### Other integrations

 -

###

 @astrojs/ db

-

###

 @astrojs/ markdoc

-

###

 @astrojs/ mdx

-

###

 @astrojs/ partytown

-

###

 @astrojs/ sitemap

 Learn

 Contribute

 Community

 Sponsor

## Solid Js

#

 @astrojs/
 solid-js

 v6.0.1

 GitHub

 npm

 Changelog

 This Astro integration enables rendering and client-side hydration for your SolidJS components.

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

To install `@astrojs/solid-js`, run the following from your project directory and follow the prompts:

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add solid `

 Terminal window
```
` pnpm astro add solid `
```

 Terminal window
```
` yarn astro add solid `
```

 If you run into any issues, feel free to report them to us on GitHub and try the manual installation steps below.

### Manual Install
 Section titled “Manual Install”
 First, install the `@astrojs/solid-js` package:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/solid-js `

 Terminal window
```
` pnpm add @astrojs/solid-js `
```

 Terminal window
```
` yarn add @astrojs/solid-js `
```

 Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'solid-js'` (or similar) warning when you start up Astro, you’ll need to install SolidJS:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install solid-js `

 Terminal window
```
` pnpm add solid-js `
```

 Terminal window
```
` yarn add solid-js `
```

 Then, apply the integration to your `astro.config.*` file using the `integrations` property:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import solidJs from ' @astrojs/solid-js ' ;
 export default defineConfig ({ // ... integrations: [ solidJs () ], }); `
 And add the following code to the `tsconfig.json` file.

 tsconfig.json ` { "extends" : " astro/tsconfigs/strict " , "include" : [ " .astro/types.d.ts " , " **/* " ], "exclude" : [ " dist " ], "compilerOptions" : { "jsx" : " preserve " , "jsxImportSource" : " solid-js " } } `

## Getting started
 Section titled “Getting started”
 To use your first SolidJS component in Astro, head to our UI framework documentation . You’ll explore:

- 📦 how framework components are loaded,

- 💧 client-side hydration options, and

- 🤝 opportunities to mix and nest frameworks together

## Configuration
 Section titled “Configuration”

### `devtools`
 Section titled “devtools”
 Type: `boolean`

 Added in:
 `@astrojs/solid-js@4.2.0`

You can enable Solid DevTools in development by passing an object with `devtools: true` to your `solid()` integration config and adding `solid-devtools` to your project dependencies:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install solid-devtools `

 Terminal window
```
` pnpm add solid-devtools `
```

 Terminal window
```
` yarn add solid-devtools `
```

 astro.config.mjs
```
` import { defineConfig } from ' astro/config ' ; import solid from ' @astrojs/solid-js ' ;
 export default defineConfig ({ // ... integrations: [ solid ({ devtools: true })], }); `
```

## Options
 Section titled “Options”

### Combining multiple JSX frameworks
 Section titled “Combining multiple JSX frameworks”
 When you are using multiple JSX frameworks (React, Preact, Solid) in the same project, Astro needs to determine which JSX framework-specific transformations should be used for each of your components. If you have only added one JSX framework integration to your project, no extra configuration is needed.

Use the `include` (required) and `exclude` (optional) configuration options to specify which files belong to which framework. Provide an array of files and/or folders to `include` for each framework you are using. Wildcards may be used to include multiple file paths.

We recommend placing common framework components in the same folder (e.g. `/components/react/` and `/components/solid/`) to make specifying your includes easier, but this is not required:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import preact from ' @astrojs/preact ' ; import react from ' @astrojs/react ' ; import svelte from ' @astrojs/svelte ' ; import vue from ' @astrojs/vue ' ; import solid from ' @astrojs/solid-js ' ;
 export default defineConfig ({ // Enable many frameworks to support all different kinds of components. // No `include` is needed if you are only using a single JSX framework! integrations: [ preact ({ include: [ ' **/preact/* ' ], }), react ({ include: [ ' **/react/* ' ], }), solid ({ include: [ ' **/solid/* ' , ' **/node_modules/@suid/material/** ' ], }), ], }); `

## Usage
 Section titled “Usage”
 Use a SolidJS component as you would any UI framework component .

### Suspense Boundaries
 Section titled “Suspense Boundaries”
 In order to support Solid Resources and Lazy Components without excessive configuration, server-only and hydrating components are automatically wrapped in top-level Suspense boundaries and rendered on the server using the `renderToStringAsync` function. Therefore, you do not need to add a top-level Suspense boundary around async components.

For example, you can use Solid’s `createResource` to fetch async remote data on the server. The remote data will be included in the initial server-rendered HTML from Astro:

 CharacterName.tsx ` function CharacterName () { const [ name ] = createResource ( () => fetch ( ' https://swapi.dev/api/people/1 ' ) . then ( ( result ) => result . json ()) . then ( ( data ) => data . name ) );
 return ( &#x3C;> &#x3C; h2 > Name: &#x3C;/ h2 > { /* Luke Skywalker */ } &#x3C; div > { name () } &#x3C;/ div > &#x3C;/> ); } `  fetch(&#x27;https://swapi.dev/api/people/1&#x27;) .then((result) => result.json()) .then((data) => data.name) ); return ( <>
## Name:
 {/* Luke Skywalker */} {name()}   );}">
 Similarly, Solid’s Lazy Components will also be resolved and their HTML will be included in the initial server-rendered page.

Non-hydrating `client:only` components are not automatically wrapped in Suspense boundaries.

Feel free to add additional Suspense boundaries according to your preference.

## More integrations

### Front-end frameworks

 -

###

 @astrojs/ alpinejs

-

###

 @astrojs/ preact

-

###

 @astrojs/ react

-

###

 @astrojs/ solid⁠-⁠js

-

###

 @astrojs/ svelte

-

###

 @astrojs/ vue

### Adapters

 -

###

 @astrojs/ cloudflare

-

###

 @astrojs/ netlify

-

###

 @astrojs/ node

-

###

 @astrojs/ vercel

### Other integrations

 -

###

 @astrojs/ db

-

###

 @astrojs/ markdoc

-

###

 @astrojs/ mdx

-

###

 @astrojs/ partytown

-

###

 @astrojs/ sitemap

 Learn

 Contribute

 Community

 Sponsor

## Preact

#

 @astrojs/
 preact

 v5.1.5

 GitHub

 npm

 Changelog

 This Astro integration enables rendering and client-side hydration for your Preact components.

## Why Preact?
 Section titled “Why Preact?”
 Preact is a library that lets you build interactive UI components for the web. If you want to build interactive features on your site using JavaScript, you may prefer using its component format instead of using browser APIs directly.

Preact is also a great choice if you have previously used React. Preact provides the same API as React, but in a much smaller 3kB package. It even supports rendering many React components using the `compat` configuration option (see below).

 Want to learn more about Preact before using this integration?
Check out “Learn Preact” , an interactive tutorial on their website.

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

To install `@astrojs/preact`, run the following from your project directory and follow the prompts:

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add preact `

 Terminal window
```
` pnpm astro add preact `
```

 Terminal window
```
` yarn astro add preact `
```

 If you run into any issues, feel free to report them to us on GitHub and try the manual installation steps below.

### Manual Install
 Section titled “Manual Install”
 First, install the `@astrojs/preact` package:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/preact `

 Terminal window
```
` pnpm add @astrojs/preact `
```

 Terminal window
```
` yarn add @astrojs/preact `
```

 Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'preact'` (or similar) warning when you start up Astro, you’ll need to install Preact:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install preact `

 Terminal window
```
` pnpm add preact `
```

 Terminal window
```
` yarn add preact `
```

 Then, apply the integration to your `astro.config.*` file using the `integrations` property:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import preact from ' @astrojs/preact ' ;
 export default defineConfig ({ // ... integrations: [ preact () ], }); `
 And add the following code to the `tsconfig.json` file.

 tsconfig.json ` { "extends" : " astro/tsconfigs/strict " , "include" : [ " .astro/types.d.ts " , " **/* " ], "exclude" : [ " dist " ], "compilerOptions" : { "jsx" : " react-jsx " , "jsxImportSource" : " preact " } } `

## Usage
 Section titled “Usage”
 To use your first Preact component in Astro, head to our UI framework documentation . You’ll explore:

- 📦 how framework components are loaded,

- 💧 client-side hydration options, and

- 🤝 opportunities to mix and nest frameworks together

Also check our Astro Integration Documentation for more on integrations.

## Configuration
 Section titled “Configuration”
 The Astro Preact integration handles how Preact components are rendered and it has its own options. Change these in the `astro.config.mjs` file which is where your project’s integration settings live.

For basic usage, you do not need to configure the Preact integration.

### `compat`
 Section titled “compat”
 Type: `boolean`

 Added in:
 `@astrojs/preact@0.3.0`

You can enable `preact/compat`, Preact’s compatibility layer for rendering React components without needing to install or ship React’s larger libraries to your users’ web browsers.

To do so, pass an object to the Preact integration and set `compat: true`.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import preact from ' @astrojs/preact ' ;
 export default defineConfig ({ integrations: [ preact ({ compat: true })], }); `
 With the `compat` option enabled, the Preact integration will render React components as well as Preact components in your project and also allow you to import React components inside Preact components. Read more in “Switching to Preact (from React)” on the Preact website.

When importing React component libraries, in order to swap out the `react` and `react-dom` dependencies as `preact/compat`, you can use `overrides` to do so.

 package.json ` { "overrides" : { "react" : " npm:@preact/compat@latest " , "react-dom" : " npm:@preact/compat@latest " } } `
 Check out the `pnpm` overrides and `yarn` resolutions docs for their respective overrides features.

### `babel`
 Section titled “babel”
 Type: `BabelOptions`

 Added in:
 `@astrojs/preact@5.1.0`
 New

You can pass additional Babel configuration options to the Preact Vite plugin. This allows you to customize the Babel transformation applied to your Preact components.

For example, the following configuration tells Babel to load `.babelrc` when processing your Preact components:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import preact from ' @astrojs/preact ' ;
 export default defineConfig ({ integrations: [ preact ({ babel: { babelrc: true , }, }), ], }); `

### `devtools`
 Section titled “devtools”
 Type: `boolean`

 Added in:
 `@astrojs/preact@3.3.0`

You can enable Preact devtools in development by passing an object with `devtools: true` to your `preact()` integration config:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import preact from ' @astrojs/preact ' ;
 export default defineConfig ({ // ... integrations: [ preact ({ devtools: true })], }); `

## Options
 Section titled “Options”

### Combining multiple JSX frameworks
 Section titled “Combining multiple JSX frameworks”
 When you are using multiple JSX frameworks (React, Preact, Solid) in the same project, Astro needs to determine which JSX framework-specific transformations should be used for each of your components. If you have only added one JSX framework integration to your project, no extra configuration is needed.

Use the `include` (required) and `exclude` (optional) configuration options to specify which files belong to which framework. Provide an array of files and/or folders to `include` for each framework you are using. Wildcards may be used to include multiple file paths.

We recommend placing common framework components in the same folder (e.g. `/components/react/` and `/components/solid/`) to make specifying your includes easier, but this is not required:

 astro.config.mjs
```
` import { defineConfig } from ' astro/config ' ; import preact from ' @astrojs/preact ' ; import react from ' @astrojs/react ' ; import svelte from ' @astrojs/svelte ' ; import vue from ' @astrojs/vue ' ; import solid from ' @astrojs/solid-js ' ;
 export default defineConfig ({ // Enable many frameworks to support all different kinds of components. // No `include` is needed if you are only using a single JSX framework! integrations: [ preact ({ include: [ ' **/preact/* ' ], }), react ({ include: [ ' **/react/* ' ], }), solid ({ include: [ ' **/solid/* ' ], }), ], }); `
```

## Examples
 Section titled “Examples”

- The Astro Preact example shows how to use an interactive Preact component in an Astro project.

- The Astro Nanostores example shows how to share state between different components — and even different frameworks! — in an Astro project.

## More integrations

### Front-end frameworks

 -

###

 @astrojs/ alpinejs

-

###

 @astrojs/ preact

-

###

 @astrojs/ react

-

###

 @astrojs/ solid⁠-⁠js

-

###

 @astrojs/ svelte

-

###

 @astrojs/ vue

### Adapters

 -

###

 @astrojs/ cloudflare

-

###

 @astrojs/ netlify

-

###

 @astrojs/ node

-

###

 @astrojs/ vercel

### Other integrations

 -

###

 @astrojs/ db

-

###

 @astrojs/ markdoc

-

###

 @astrojs/ mdx

-

###

 @astrojs/ partytown

-

###

 @astrojs/ sitemap

 Learn

 Contribute

 Community

 Sponsor

## Alpinejs

#

 @astrojs/
 alpinejs

 v0.5.0

 GitHub

 npm

 Changelog

 This Astro integration adds Alpine.js to your project so that you can use Alpine.js anywhere on your page.

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

To install `@astrojs/alpinejs`, run the following from your project directory and follow the prompts:

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add alpinejs `

 Terminal window
```
` pnpm astro add alpinejs `
```

 Terminal window
```
` yarn astro add alpinejs `
```

 If you run into any issues, feel free to report them to us on GitHub and try the manual installation steps below.

### Manual Install
 Section titled “Manual Install”
 First, install the `@astrojs/alpinejs` package.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/alpinejs `

 Terminal window
```
` pnpm add @astrojs/alpinejs `
```

 Terminal window
```
` yarn add @astrojs/alpinejs `
```

 Most package managers will install associated peer dependencies as well. However, if you see a `Cannot find package 'alpinejs'` (or similar) warning when you start up Astro, you’ll need to manually install Alpine.js yourself:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install alpinejs @types/alpinejs `

 Terminal window
```
` pnpm add alpinejs @types/alpinejs `
```

 Terminal window
```
` yarn add alpinejs @types/alpinejs `
```

 Then, apply the integration to your `astro.config.*` file using the `integrations` property:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import alpinejs from ' @astrojs/alpinejs ' ;
 export default defineConfig ({ // ... integrations: [ alpinejs () ], }); `

## Configuration Options
 Section titled “Configuration Options”

### `entrypoint`
 Section titled “entrypoint”
 Type: `string`

 Added in:
 `@astrojs/alpinejs@0.4.0`

You can extend Alpine by setting the `entrypoint` option to a root-relative import specifier (e.g. `entrypoint: "/src/entrypoint"`).

The default export of this file should be a function that accepts an Alpine instance prior to starting. This allows the use of custom directives, plugins and other customizations for advanced use cases.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import alpinejs from ' @astrojs/alpinejs ' ;
 export default defineConfig ({ // ... integrations: [ alpinejs ({ entrypoint: ' /src/entrypoint ' })], }); `
 src/entrypoint.ts
```
` import type { Alpine } from ' alpinejs ' import intersect from ' @alpinejs/intersect '
 export default ( Alpine : Alpine ) => { Alpine . plugin ( intersect ) } `
```
 { Alpine.plugin(intersect)}">

## Usage
 Section titled “Usage”
 Once the integration is installed, you can use Alpine.js directives and syntax inside any Astro component. The Alpine.js script is automatically added and enabled on every page of your website so no client directives are needed. Add plugin scripts to the page `&#x3C;head>`.

The following example adds Alpine’s Collapse plugin to expand and collapse paragraph text:

 src/pages/index.astro ` --- --- &#x3C; html > &#x3C; head > &#x3C;!-- ... --> &#x3C; script defer src = " https://cdn.jsdelivr.net/npm/@alpinejs/collapse@3.x.x/dist/cdn.min.js " >&#x3C;/ script > &#x3C;/ head > &#x3C; body > &#x3C;!-- ... --> &#x3C; div x-data = " { expanded: false } " > &#x3C; button @click = " expanded = ! expanded " > Toggle Content &#x3C;/ button >
 &#x3C; p id = " foo " x-show = " expanded " x-collapse > Lorem ipsum &#x3C;/ p > &#x3C;/ div > &#x3C;/ body > &#x3C;/ html > `         Toggle Content   Lorem ipsum
   ">

## Intellisense for TypeScript
 Section titled “Intellisense for TypeScript”
 The `@astrojs/alpine` integration adds `Alpine` to the global window object . For IDE autocompletion, add the following to your `src/env.d.ts`:

 src/env.d.ts
```
` interface Window { Alpine : import ( ' alpinejs ' ). Alpine ; } `
```

## Examples
 Section titled “Examples”

- The Astro Alpine.js example shows how to use Alpine.js in an Astro project.

## More integrations

### Front-end frameworks

 -

###

 @astrojs/ alpinejs

-

###

 @astrojs/ preact

-

###

 @astrojs/ react

-

###

 @astrojs/ solid⁠-⁠js

-

###

 @astrojs/ svelte

-

###

 @astrojs/ vue

### Adapters

 -

###

 @astrojs/ cloudflare

-

###

 @astrojs/ netlify

-

###

 @astrojs/ node

-

###

 @astrojs/ vercel

### Other integrations

 -

###

 @astrojs/ db

-

###

 @astrojs/ markdoc

-

###

 @astrojs/ mdx

-

###

 @astrojs/ partytown

-

###

 @astrojs/ sitemap

 Learn

 Contribute

 Community

 Sponsor

## Cloudflare

#

 @astrojs/
 cloudflare

 v13.7.0

 GitHub

 npm

 Changelog

 This adapter allows Astro to deploy your on-demand rendered routes and features to Cloudflare , including server islands , actions , and sessions .

If you’re using Astro as a static site builder, you don’t need an adapter.

Learn how to deploy your Astro site in our Cloudflare deployment guide .

## Why Astro Cloudflare
 Section titled “Why Astro Cloudflare”
 Cloudflare’s Developer Platform lets you develop full-stack applications with access to resources such as storage and AI, all deployed to a global edge network. This adapter builds your Astro project for deployment through Cloudflare.

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

Add the Cloudflare adapter to enable server-rendering in your Astro project with the `astro add` command. This will install `@astrojs/cloudflare` and make the appropriate changes to your `astro.config.mjs` file in one step.

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add cloudflare `

 Terminal window
```
` pnpm astro add cloudflare `
```

 Terminal window
```
` yarn astro add cloudflare `
```

 Now, you can enable on-demand rendering per page , or set your build output configuration to `output: 'server'` to server-render all your pages by default .

### Manual Install
 Section titled “Manual Install”

 Add the `@astrojs/cloudflare` adapter to your project’s dependencies using your preferred package manager.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/cloudflare `

 Terminal window
```
` pnpm add @astrojs/cloudflare `
```

 Terminal window
```
` yarn add @astrojs/cloudflare `
```

-
 Add the adapter to your `astro.config.mjs` file:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import cloudflare from ' @astrojs/cloudflare ' ;
 export default defineConfig ({ adapter: cloudflare (), }); `

-
 Astro will automatically generate a default configuration, using the package.json name field or the folder name as the Worker name. You can optionally create a Wrangler configuration file if you need custom settings. This example declares Cloudflare KV bindings:

 wrangler.jsonc ` { "name" : " my-astro-app " , // Add your bindings here, e.g.: // "kv_namespaces": [{ "binding": "MY_KV", "id": "&#x3C;namespace_id>" }] } ` &#x22; }]}">

## Options
 Section titled “Options”
 The Cloudflare adapter accepts the following options from `@cloudflare/vite-plugin` :

- `auxiliaryWorkers`

- `configPath`

- `inspectorPort`

- `persistState`

- `remoteBindings`

- `experimental.headersAndRedirectsDevModeSupport`

It also accepts the following:

### `imageService`
 Section titled “imageService”
 Type: `'passthrough' | 'cloudflare' | 'cloudflare-binding' | 'compile' | 'custom' | { build: 'compile', runtime?: 'cloudflare-binding' | 'passthrough' }`
 Default: `'cloudflare-binding'`

Determines which image service is used by the adapter. The adapter will default to `cloudflare-binding` mode when an incompatible image service is configured. Otherwise, it will use the globally configured image service:

- `cloudflare`: Uses the Cloudflare Image Resizing service.

- `cloudflare-binding`: Uses the Cloudflare Images binding for image transformation. The binding is automatically provisioned when you deploy.

- `passthrough`: Uses the existing `noop` service.

- `compile`: Uses a combination of internal dependencies to transform images locally at build time for prerendered routes. The noop `passthrough` option is configured for on-demand rendered pages.

- `custom`: Always uses the image service configured in Image Options . This option will not check to see whether the configured image service works in Cloudflare’s `workerd` runtime.

It is also possible to configure your image service as an object, setting both a build time and runtime service independently. Currently, `'compile'` is the only available build-time option. The supported runtime options are `'passthrough'` (default) and `'cloudflare-binding'`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import cloudflare from ' @astrojs/cloudflare ' ;
 export default defineConfig ({ adapter: cloudflare ({ imageService: { build: ' compile ' , runtime: ' cloudflare-binding ' } }), }); `

### `sessionKVBindingName`
 Section titled “sessionKVBindingName”
 Type: `string`
 Default: `SESSION`

 Added in:
 `@astrojs/cloudflare@12.4.0`

Sets the name of the KV binding used for session storage. By default, the KV namespace is automatically provisioned when you deploy, and is named `SESSION`. You can change this name by setting the binding manually in your wrangler config. See Sessions for more information.

 astro.config.mjs ` export default defineConfig ({ adapter: cloudflare ({ sessionKVBindingName: ' MY_SESSION_BINDING ' , }), }); `
 wrangler.jsonc
```
` { "kv_namespaces" : [ { "binding" : " MY_SESSION_BINDING " , } ] } `
```

### `imagesBindingName`
 Section titled “imagesBindingName”
 Type: `string`
 Default: `IMAGES`

Sets the name of the Images binding used when `imageService` is set to `cloudflare-binding`. By default, the binding is automatically provisioned with the name `IMAGES` when you deploy. You can change it by setting the binding manually in your wrangler config:

 astro.config.mjs ` export default defineConfig ({ adapter: cloudflare ({ imageService: ' cloudflare-binding ' , imagesBindingName: ' MY_IMAGES ' , }), }); `
 wrangler.jsonc
```
` { "images" : { "binding" : " MY_IMAGES " } } `
```

### `prerenderEnvironment`
 Section titled “prerenderEnvironment”
 Type: `'workerd' | 'node'`
 Default: `'workerd'`

 Added in:
 `@astrojs/cloudflare@13.1.0`

Controls which runtime is used for prerendering static pages at build time and during development.

By default, prerendered pages are built using Cloudflare’s `workerd` runtime to match the production environment as closely as possible. Set this option to `'node'` when your prerendered pages depend on Node.js APIs or NPM packages that are not compatible with `workerd`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import cloudflare from ' @astrojs/cloudflare ' ;
 export default defineConfig ({ adapter: cloudflare ({ prerenderEnvironment : ' node ' , }), }); `
 For example, if a prerendered page reads from the file system using `node:fs`, set `prerenderEnvironment` to `'node'`. On-demand rendered pages are unaffected by this option and always run in `workerd`.

## Cloudflare runtime
 Section titled “Cloudflare runtime”
 The Cloudflare runtime gives you access to environment variables, bindings to Cloudflare resources, and other Cloudflare-specific APIs.

### Environment variables and bindings
 Section titled “Environment variables and bindings”
 Environment variables and bindings are defined in your `wrangler.jsonc` configuration file.

Define environment variables that do not store sensitive information in `wrangler.jsonc`:

 wrangler.jsonc ` { "vars" : { "MY_VARIABLE" : " test " , }, } `
 Secrets are a special type of environment variable that allow you to attach encrypted text values to your Worker. They need to be defined differently to ensure they are not visible within Wrangler or Cloudflare dashboard after you set them.

To define `secrets`, add them through the Wrangler CLI rather than in your Wrangler config file:

 Terminal window ` npx wrangler secret put &#x3C;KEY> ` ">
 To set secrets for local development, add a `.dev.vars` file to the root of the Astro project:

 .dev.vars ` DB_PASSWORD =myPassword `
 Cloudflare environment variables and secrets can be imported from `"cloudflare:workers"`:

 src/pages/index.astro ` --- import { env } from ' cloudflare:workers ' ;
 const myVariable = env . MY_VARIABLE ; const myKVNamespace = env . MY_KV ; --- `
 They are also compatible with the `astro:env` API :

 ` import { MY_VARIABLE } from ' astro:env/server ' ; `
 See the list of all supported bindings in the Cloudflare documentation.

### The `cf` object
 Section titled “The cf object”
 The Cloudflare `cf` object contains request metadata such as geolocation information. Access it directly from the request:

 src/pages/index.astro ` --- const cf = Astro . request . cf ; const country = cf ?. country ; --- `

### Execution context
 Section titled “Execution context”
 Access the Cloudflare `ExecutionContext` through `Astro.locals.cfContext`. This is useful for operations like `waitUntil()` , or accessing Durable Object exports within your page.

 src/pages/index.astro ` --- const cfContext = Astro . locals . cfContext ; cfContext . exports . Greeter . greet ( ' Astro ' ); cfContext . waitUntil ( someAsyncOperation ()); --- `

### Typing
 Section titled “Typing”
 `wrangler` provides a `types` command to generate TypeScript types for your bindings. This allows you to type your environment without the need for manual type definitions.

Run `wrangler types` every time you change your configuration files (e.g. `wrangler.jsonc`, `.dev.vars`).

## Cloudflare Platform
 Section titled “Cloudflare Platform”

### Headers
 Section titled “Headers”
 Add custom headers for static assets by creating a `_headers` file in your Astro project’s `public/` folder. This file will be copied to the build output directory. Headers in `_headers` are not applied to responses generated by your Worker code.

### Assets
 Section titled “Assets”
 Assets built by Astro are all named with a hash and, therefore, can be given long cache headers. By default, Astro on Cloudflare will add such a header for these files.

### Redirects
 Section titled “Redirects”
 Declare custom redirects for static assets by adding a `_redirects` file in your Astro project’s `public/` folder. This file will be copied to your build output directory. For dynamic routes, configure redirects in Astro directly instead.

### Routes
 Section titled “Routes”
 Routing for static assets is based on the file structure in the build directory (e.g. `./dist`). If no match is found, this will fall back to the Worker for on-demand rendering. Read more about static asset routing with Cloudflare Workers .

## Sessions
 Section titled “Sessions”
 The Astro Sessions API allows you to easily store user data between requests. This can be used for things like user data and preferences, shopping carts, and authentication credentials. Unlike cookie storage, there are no size limits on the data, and it can be restored on different devices.

Astro automatically configures Workers KV for session storage when using the Cloudflare adapter. Wrangler can automatically provision the KV namespace when you deploy, so no manual setup is required. Alternatively, you can define the KV binding manually in your `wrangler.jsonc` file and set a custom binding name using the `sessionKVBindingName` adapter option.

 src/components/CartButton.astro ` --- export const prerender = false ; // Not needed in 'server' mode const cart = await Astro . session ?. get ( ' cart ' ); ---
 &#x3C; a href = " /checkout " > 🛒 { cart ?. length ?? 0 } items &#x3C;/ a > ` 🛒 {cart?.length ?? 0} items ">
 By default, the KV binding is named `SESSION`. To use a different name, set the `sessionKVBindingName` option in the adapter config.

## Cloudflare Module Imports
 Section titled “Cloudflare Module Imports”
 The Cloudflare `workerd` runtime supports imports of some non-standard module types . Most additional file types are also available in Astro:

- `.wasm` or `.wasm?module`: exports a `WebAssembly.Module` that can then be instantiated

- `.bin`: exports an `ArrayBuffer` of the raw binary contents of the file

- `.txt`: exports a string of the file contents

All module types export a single default value. Modules can be imported both from server-side rendered pages, or from prerendered pages for static site generation.

The following is an example of importing a Wasm module that then responds to requests by adding the request’s number parameters together.

 pages/add/[a]/[b].js ` // Import the WebAssembly module import mod from ' ../util/add.wasm ' ;
 // Instantiate first in order to use it const addModule : any = new WebAssembly . Instance ( mod );
 export async function GET ( context ) { const a = Number . parseInt ( context . params . a ); const b = Number . parseInt ( context . params . b ); return new Response ( ` ${ addModule . exports . add ( a , b ) } ` ); } `
 While this example is trivial, Wasm can be used to accelerate computationally intensive operations which do not involve significant I/O such as embedding an image processing library, or embedding a small pre-indexed database for search over a read-only dataset.

## Node.js compatibility
 Section titled “Node.js compatibility”
 Cloudflare Workers support most Node.js runtime APIs through the `nodejs_compat` compatibility flag. This includes commonly used modules like `node:buffer`, `node:crypto`, `node:path`, and many others. See the full list of supported Node.js APIs in Cloudflare’s documentation.

To enable Node.js compatibility, add the `nodejs_compat` flag to your Wrangler configuration:

 wrangler.jsonc ` { "compatibility_flags" : [ " nodejs_compat " ], } `
 Then use the `node:*` import syntax in your server-side code:

 src/pages/api/endpoint.js ` export const prerender = false ; // Not needed in 'server' mode import { Buffer } from ' node:buffer ' ; `
 For Node.js APIs not yet supported in the Workers runtime, Wrangler can inject polyfills (requires `nodejs_compat` and a compatibility date of 2024-09-23 or later).

 See the Cloudflare documentation on Node.js compatibility for the complete list of supported APIs and configuration details.

## Local preview
 Section titled “Local preview”
 After building your project with `astro build`, use `astro preview` to test your Cloudflare Workers application locally. The preview runs using Cloudflare’s `workerd` runtime, closely mirroring production behavior.

### Meaningful error messages
 Section titled “Meaningful error messages”
 By default, errors occurring while running your application in Wrangler are minified. For better debugging, add `vite.build.minify = false` to your `astro.config.mjs`:

 astro.config.mjs ` export default defineConfig ({ adapter: cloudflare (), vite: { build: { minify: false , }, }, }); `

## Upgrading to v13 and Astro 6
 Section titled “Upgrading to v13 and Astro 6”
 Astro 6 brings significant improvements to the Cloudflare development experience and requires `@astrojs/cloudflare` v13 or later. Now, `astro dev` uses Cloudflare’s Vite plugin and `workerd` runtime to closely mirror production behavior.

 See the Astro 6 upgrade guide for full instructions on upgrading Astro itself.

### Development server now uses workerd
 Section titled “Development server now uses workerd”
 The biggest change for Cloudflare users in Astro 6 is that `astro dev` and `astro preview` now use the Cloudflare Vite plugin to run your site using the real Workers runtime (`workerd`) instead of Node.js. This means your development environment is now a much closer replica of your production environment, with the same runtime, APIs, and behavior.

This change helps you catch issues during development that would have previously only appeared in production, and features like Durable Objects, R2 bindings, and Workers AI now work exactly as they do when deployed to Cloudflare’s platform.

This change is transparent for most projects. If your project had special configuration for `astro dev` or was relying on Node.js-specific behavior in development, adjust your code or configuration accordingly.

### New: `prerenderEnvironment` option
 Section titled “New: prerenderEnvironment option”
 In Astro 6, prerendered pages now run in Cloudflare’s `workerd` runtime by default during development and build. Previously, these pages always ran in Node.js.

If your prerendered pages depend on Node.js APIs (for example `node:fs`) or NPM packages that are not compatible with `workerd`, set `prerenderEnvironment: 'node'` in your Cloudflare adapter config to restore the previous behavior for prerendering.

On-demand rendered pages are not affected by this option and continue to run in `workerd`.

 See `prerenderEnvironment` for configuration details.

### Some dependencies might need to be pre-compiled
 Section titled “Some dependencies might need to be pre-compiled”
 The new workerd environment does not support CommonJS syntax, including Node.js specific syntax such as `require` and `module.exports`. This means that some of your project dependencies may throw errors in the development server or during the build.

If you have control over the dependency, you can create a Vite plugin and pre-compile the dependency using the `optimizeDeps.include` option.

For example, you can create a Vite plugin to pre-compile the dependency `postcss` in order to use the Expressive Code syntax highlighter:

 ` function noExternalPlugin () { return { name: " optimize-dependencies " , configEnvironment ( environment ) { // We're only interested in server environments if ( environment !== ' client ' ) { return { optimizeDeps: { include: [ " postcss " // Or you can use this syntax if you don't depend directly on a dependency // "expressive-code > postcss" ] } } } } } } ` postcss&#x22; ] } } } } }}">

### Changed: Wrangler entrypoint configuration
 Section titled “Changed: Wrangler entrypoint configuration”
 Previously, the `main` field in your Wrangler configuration pointed to the built worker file (e.g. `dist/_worker.js/index.js`). With Astro 6, this has changed to point to a new unified entrypoint provided by the Cloudflare adapter: `@astrojs/cloudflare/entrypoints/server`.

Update your `wrangler.jsonc` to use the new entrypoint:

 wrangler.jsonc ` { "main" : " dist/_worker.js/index.js " , "main" : " @astrojs/cloudflare/entrypoints/server " , "name" : " my-astro-app " , // ... rest of config } `
 This single entrypoint handles both `astro dev` and production deployments.

### Removed: `Astro.locals.runtime` API
 Section titled “Removed: Astro.locals.runtime API”
 The `Astro.locals.runtime` object has been removed in favor of direct access to Cloudflare Workers APIs. Access environment variables, the `cf` object, caches, and execution context directly through the provided interfaces.

 Accessing environment variables:

Previously, environment variables were accessed through `Astro.locals.runtime.env`. Now import `env` directly instead:

 ` const { env } = Astro . locals . runtime ; import { env } from ' cloudflare:workers ' ; `
 Accessing the `cf` object:

Previously, the `cf` object was accessed through `Astro.locals.runtime.cf`. Now access it directly from the request:

 ` const { cf } = Astro . locals . runtime ; const cf = Astro . request . cf ; `
 Accessing the caches API:

Previously, the caches API was accessed through `Astro.locals.runtime.caches`. Now use the global `caches` object directly:

 ` const { caches } = Astro . locals . runtime ;
 caches . default . put ( request , response ); `
 Accessing the execution context:

The `Astro.locals.runtime.ctx` object is replaced with `Astro.locals.cfContext`, which contains the Cloudflare `ExecutionContext`:

 ` const ctx = Astro . locals . runtime . ctx ; const ctx = Astro . locals . cfContext ; `

### Changed: Wrangler configuration file is now optional
 Section titled “Changed: Wrangler configuration file is now optional”
 The Wrangler configuration file is now optional for simple projects. If you don’t have custom configuration, such as Cloudflare bindings (KV, D1, Durable Objects, etc.), Astro will automatically generate a default configuration for you.

If your `wrangler.jsonc` only contains basic configuration like this:

 ` { "main" : " @astrojs/cloudflare/entrypoints/server " , "compatibility_date" : " 2025-05-21 " , "assets" : { "directory" : " ./dist " , "binding" : " ASSETS " , }, } `
 You can safely delete this file. Astro handles this configuration automatically. Alternatively, create a minimal `wrangler.jsonc` with just your project name and other custom settings:

 wrangler.jsonc ` { "name" : " my-astro-app " , } `

### Changed: Custom entrypoint API
 Section titled “Changed: Custom entrypoint API”
 If you were using a custom `workerEntryPoint` configuration in the adapter options, this has been removed. Instead, specify your custom entrypoint in your Wrangler configuration and create a standard Cloudflare Worker export object directly, rather than using the `createExports()` function.

-
Remove the `workerEntryPoint` option from your adapter config:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import cloudflare from ' @astrojs/cloudflare ' ;
 export default defineConfig ({ adapter: cloudflare ({ workerEntryPoint: { path: ' src/worker.ts ' , namedExports: [ ' MyDurableObject ' ], }, }), }); `

-
 Specify the entrypoint in `wrangler.jsonc` instead:

 wrangler.jsonc ` { "main" : " ./src/worker.ts " } `

-
 Update your custom worker entry file to use standard Worker syntax. Import the handler from `@astrojs/cloudflare/handler` and export a standard Cloudflare Worker object, alongside any custom exports like Durable Objects:

 src/worker.ts ` import { handle } from ' @astrojs/cloudflare/handler ' ; import { DurableObject } from ' cloudflare:workers ' ;
 export class MyDurableObject extends DurableObject &#x3C; Env > { // ... }
 export default { async fetch ( request , env , ctx ) { await env . MY_QUEUE . send ( ' log ' ); return handle (request, env, ctx); }, async queue ( batch , _env ) { let messages = JSON . stringify (batch . messages ); console . log ( ` consumed from our queue: ${ messages } ` ); }, } satisfies ExportedHandler &#x3C; Env >; ` { // ...}export default { async fetch(request, env, ctx) { await env.MY_QUEUE.send(&#x27;log&#x27;); return handle(request, env, ctx); }, async queue(batch, _env) { let messages = JSON.stringify(batch.messages); console.log(&#x60;consumed from our queue: ${messages}&#x60;); },} satisfies ExportedHandler ;">

 The manifest is now created internally by the adapter, so it does not need to be passed to your handler.

### Removed: `cloudflareModules` option
 Section titled “Removed: cloudflareModules option”
 The `cloudflareModules` adapter option has been removed because it is no longer necessary. Cloudflare natively supports importing `.sql`, `.wasm`, and other module types.

Remove the `cloudflareModules` option from your Cloudflare adapter configuration if you were using it:

 astro.config.mjs ` import cloudflare from ' @astrojs/cloudflare ' ;
 export default defineConfig ({ adapter: cloudflare ({ cloudflareModules: true }) }); `

### New: `astro preview` support
 Section titled “New: astro preview support”
 Use `astro preview` to test your Cloudflare Workers application locally before deploying. The preview runs using Cloudflare’s `workerd` runtime, closely mirroring production behavior. Run `astro build` followed by `astro preview` to start the preview server.

### Removed: Cloudflare Pages support
 Section titled “Removed: Cloudflare Pages support”
 The Astro Cloudflare adapter no longer supports deployment on Cloudflare Pages. For the best experience and feature support, you should migrate to Cloudflare Workers.

 See Cloudflare’s migration guide from Pages to Workers for detailed migration instructions.

### Changed: `imageService` default
 Section titled “Changed: imageService default”
 The default value of `imageService` has changed from `'compile'` to `'cloudflare-binding'` for an improved experience when working with images.

The `cloudflare-binding` service uses the Cloudflare Images binding to transform images at runtime, and the binding is automatically provisioned when you deploy.

To revert to the previous behavior, where image transformation was only available on prerendered routes at build time, set `imageService: 'compile'` explicitly in your adapter config.

### Changed: Deploy to Cloudflare Environment
 Section titled “Changed: Deploy to Cloudflare Environment”
 In Astro 5.x, you could build your Astro project once and deploy it to a specific Cloudflare environment with `wrangler deploy --env some-env`.

Since Astro 6.0, the integration relies on the Cloudflare Vite plugin and this behavior has changed. The environment is now determined during the build phase. Therefore, you must build your project separately for each environment.

To deploy to a specific Cloudflare environment, prefix your command with the `CLOUDFLARE_ENV` variable. For example, the command `CLOUDFLARE_ENV=some-env astro build &#x26;&#x26; wrangler deploy` will build your Astro project and deploy it with Wrangler using the `some-env` environment.

 Learn how to update your Cloudflare environments in the Migrate from wrangler dev guide .

## More integrations

### Front-end frameworks

 -

###

 @astrojs/ alpinejs

-

###

 @astrojs/ preact

-

###

 @astrojs/ react

-

###

 @astrojs/ solid⁠-⁠js

-

###

 @astrojs/ svelte

-

###

 @astrojs/ vue

### Adapters

 -

###

 @astrojs/ cloudflare

-

###

 @astrojs/ netlify

-

###

 @astrojs/ node

-

###

 @astrojs/ vercel

### Other integrations

 -

###

 @astrojs/ db

-

###

 @astrojs/ markdoc

-

###

 @astrojs/ mdx

-

###

 @astrojs/ partytown

-

###

 @astrojs/ sitemap

 Learn

 Contribute

 Community

 Sponsor

## Netlify

#

 @astrojs/
 netlify

 v7.0.13

 GitHub

 npm

 Changelog

 This adapter allows Astro to deploy your on-demand rendered routes and features to Netlify , including server islands , actions , and sessions .

If you’re using Astro as a static site builder, you only need this adapter if you are using additional Netlify services that require a server (e.g. Netlify Image CDN ). Otherwise, you do not need an adapter to deploy your static site.

Learn how to deploy your Astro site in our Netlify deployment guide .

## Why Astro Netlify
 Section titled “Why Astro Netlify”
 Netlify is a deployment platform that allows you to host your site by connecting directly to your GitHub repository. This adapter enhances the Astro build process to prepare your project for deployment through Netlify.

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

Add the Netlify adapter to enable on-demand rendering in your Astro project with the `astro add` command.
This will install `@astrojs/netlify` and make the appropriate changes to your `astro.config.mjs` file in one step.

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add netlify `

 Terminal window
```
` pnpm astro add netlify `
```

 Terminal window
```
` yarn astro add netlify `
```

 Now, you can enable on-demand rendering per page , or set your build output configuration to `output: 'server'` to server-render all your pages by default .

### Manual Install
 Section titled “Manual Install”
 First, install the Netlify adapter to your project’s dependencies using your preferred package manager:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/netlify `

 Terminal window
```
` pnpm add @astrojs/netlify `
```

 Terminal window
```
` yarn add @astrojs/netlify `
```

 Then, add the adapter to your `astro.config.*` file:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import netlify from ' @astrojs/netlify ' ;
 export default defineConfig ({ // ... adapter: netlify (), }); `

## Usage
 Section titled “Usage”
 Read the full deployment guide here.

Follow the instructions to build your site locally . After building, you will have a `.netlify/` folder containing both Netlify Functions in the `.netlify/functions-internal/` folder and Netlify Edge Functions in the`.netlify/edge-functions/` folder.

To deploy your site, install the Netlify CLI and run:

 Terminal window ` netlify deploy `
 The Netlify Blog post on Astro and the Netlify Docs provide more information on how to use this integration to deploy to Netlify.

### Running Astro middleware on Netlify Edge Functions
 Section titled “Running Astro middleware on Netlify Edge Functions”
 By default, Astro middleware is applied to pre-rendered pages at build-time and to on-demand-rendered pages at runtime.

To implement redirects, access control, or custom response headers for pre-rendered pages, run your middleware on Netlify Edge Functions by setting the `middlewareMode` option to `edge`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import netlify from ' @astrojs/netlify ' ;
 export default defineConfig ({ // ... adapter: netlify ({ middlewareMode: ' edge ' , }), }); `
 When `middlewareMode` is set to `'edge'`, an edge function will execute your middleware code for all requests, including static assets, prerendered pages, and on-demand rendered pages.

For on-demand rendered pages, the `context.locals` object is serialized using JSON and sent in a header for the serverless function, which performs the rendering. As a security measure, the serverless function will refuse to serve requests with a `403 Forbidden` response unless they come from the generated edge function.

### Accessing edge context from your site
 Section titled “Accessing edge context from your site”
 Netlify Edge Functions provide a context object that includes metadata about the request such as a user’s IP, geolocation data, and cookies.

This can be accessed through the `Astro.locals.netlify.context` object:

 ` --- const { geo : { city }, } = Astro . locals . netlify . context ; ---
 &#x3C; h1 > Hello there, friendly visitor from { city } ! &#x3C;/ h1 > `
 If you’re using TypeScript, you can get proper typings by updating `src/env.d.ts` to use `NetlifyLocals`:

 src/env.d.ts ` type NetlifyLocals = import ( ' @astrojs/netlify ' ). NetlifyLocals
 declare namespace App { interface Locals extends NetlifyLocals { // ... } } `
 This is not available on prerendered pages.

### Netlify Image CDN support
 Section titled “Netlify Image CDN support”
 This adapter by default uses the Netlify Image CDN to transform images on-the-fly without impacting build times.
It’s implemented using an Astro Image Service under the hood.

To opt out of Netlify’s Image CDN remote image optimization, use the `imageCDN` option:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import netlify from ' @astrojs/netlify ' ;
 export default defineConfig ({ // ... adapter: netlify ({ imageCDN: false , }), }); `
 If you are using images hosted on another domain, you must authorize the domain or URL patterns using the `image.domains` or `image.remotePatterns` configuration options:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import netlify from ' @astrojs/netlify ' ;
 export default defineConfig ({ // ... adapter: netlify (), image: { domains: [ ' example.com ' ], }, }); `
 For more information, see the guide to authorizing remote images . This is not required for images hosted on the same domain as your site.

### Static sites with the Netlify Adapter
 Section titled “Static sites with the Netlify Adapter”
 For static sites (`output: 'static'`) hosted on Netlify, you usually don’t need an adapter. However, some deployment features are only available through an adapter.

Static sites will need to install this adapter to use and configure Netlify’s image service .

If you use `redirects` configuration in your Astro config, the Netlify adapter can be used to translate this to the proper `_redirects` format.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import netlify from ' @astrojs/netlify ' ;
 export default defineConfig ({ // ... adapter: netlify (), redirects: { ' /blog/old-post ' : ' /blog/new-post ' , }, }); `
 Once you run `astro build` there will be a `dist/_redirects` file. Netlify will use that to properly route pages in production.

### Sessions
 Section titled “Sessions”
 The Astro Sessions API allows you to easily store user data between requests. This can be used for things like user data and preferences, shopping carts, and authentication credentials. Unlike cookie storage, there are no size limits on the data, and it can be restored on different devices.

Astro automatically configures Netlify Blobs for session storage when using the Netlify adapter. If you would prefer to use a different session storage driver, you can specify it in your Astro config. See the `session` configuration reference for more details.

### Caching Pages
 Section titled “Caching Pages”
 On-demand rendered pages without any dynamic content can be cached to improve performance and lower resource usage.
Enabling the `cacheOnDemandPages` option in the adapter will cache all server-rendered pages for up to one year:

 astro.config.mjs ` export default defineConfig ({ // ... adapter: netlify ({ cacheOnDemandPages: true , }), }); `
 This can be changed on a per-page basis by adding caching headers to your response:

 pages/index.astro ` --- import Layout from ' ../components/Layout.astro ' ;
 Astro . response . headers . set ( ' CDN-Cache-Control ' , ' public, max-age=45, must-revalidate ' ); ---
 &#x3C; Layout title = " Astro on Netlify " > { new Date () } &#x3C;/ Layout > `  {new Date()} ">
 With fine-grained cache control , Netlify supports
standard caching headers like `CDN-Cache-Control` or `Vary`.
Refer to the docs to learn about implementing e.g. time to live (TTL) or stale while revalidate (SWR) caching: https://docs.netlify.com/platform/caching

### Skew Protection
 Section titled “Skew Protection”

 Added in:
 `@astrojs/netlify@6.6.0`

Netlify’s skew protection ensures that users accessing your site during a deployment continue to receive content from the same deploy version. The Netlify adapter automatically configures skew protection for Astro features like actions, server islands, view transitions, and prefetch requests by injecting the current deploy ID into internal requests. This prevents version mismatches between the client and server during active deployments.

While Astro automatically adds the skew protection header for its built-in features, if you are making your own fetch requests to your site, you can include the header manually using the `DEPLOY_ID` environment variable:

 ` const response = await fetch ( ' /api/endpoint ' , { headers: { ' X-Netlify-Deploy-ID ' : import. meta . env . DEPLOY_ID , }, } ); `

### Including or excluding files from Netlify Functions
 Section titled “Including or excluding files from Netlify Functions”
 When deploying an Astro site with on-demand rendering to Netlify, the generated functions automatically trace and include server dependencies. However, you may need to customize which files are included in your Netlify Functions.

#### `includeFiles`
 Section titled “includeFiles”
 Type: `string[]`
 Default: `[]`

 Added in:
 `astro@5.3.0`

The `includeFiles` property allows you to explicitly specify additional files that should be bundled with your function. This is useful for files that aren’t automatically detected as dependencies, such as:

- Data files loaded using `fs` operations

- Configuration files

- Template files

Provide an array of additional files to include with file paths relative to your project’s `root` . Absolute paths may not work as expected.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import netlify from ' @astrojs/netlify ' ;
 export default defineConfig ({ // ... adapter: netlify ({ includeFiles: [ ' ./my-data.json ' ], // relative to `root` }), }); `

#### `excludeFiles`
 Section titled “excludeFiles”
 Type: `string[]`
 Default: `[]`

 Added in:
 `astro@5.3.0`

You can use the `excludeFiles` property to prevent specific files from being bundled that would otherwise be included. This is helpful for:

- Reducing bundle size

- Excluding large binaries

- Preventing unwanted files from being deployed

Provide an array of specific files to exclude with file paths relative to your project’s `root` . Absolute paths may not work as expected.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import netlify from ' @astrojs/netlify ' ;
 export default defineConfig ({ // ... adapter: netlify ({ excludeFiles: [ ' ./src/some_big_file.jpg ' ], // relative to `root` }), }); `

#### Using glob patterns
 Section titled “Using glob patterns”
 Both `includeFiles` and `excludeFiles` support glob patterns for matching multiple files:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import netlify from ' @astrojs/netlify ' ;
 export default defineConfig ({ adapter: netlify ({ includeFiles: [ ' ./data/**/*.json ' ], excludeFiles: [ ' ./node_modules/package/**/* ' , ' ./src/**/*.test.js ' ] }), }); `

### Local development features
 Section titled “Local development features”
 When running `astro dev`, the adapter enables several Netlify platform features to ensure the environment matches production as closely as possible. These include:

- A local Netlify Image CDN server. This is used for images by default.

- A local Netlify Blobs server. This is used for sessions by default

- Redirects, rewrites and headers from your Netlify config

- Access to Netlify Edge Context in on-demand pages

- Environment variables from your Netlify site

These work best when your local site is linked to a Netlify site using `netlify link`.

You can enable or disable some of these features using the `devFeatures` option in your adapter configuration. By default, all features are enabled except for environment variables.

#### `devFeatures`
 Section titled “devFeatures”
 Type: `boolean | object`
 Default: `{ images: true, environmentVariables: false }`

 Added in:
 `@astrojs/netlify@6.5.1`

The `devFeatures` option can be either a boolean to enable or disable all features, or an object to enable specific features.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import netlify from ' @astrojs/netlify ' ;
 export default defineConfig ({ // ... adapter: netlify ({ devFeatures: { // Enable Netlify Image CDN support in dev. Defaults to true. images: false , // Inject Netlify environment variables in dev. Defaults to false. environmentVariables: true , }, }), }); `
 `devFeatures.images` Section titled “devFeatures.images”
 Type: `boolean`
 Default: `true`

 Added in:
 `@astrojs/netlify@6.5.1`

Enables support for the local Netlify Image CDN in development.

This uses a local version of the Netlify Image CDN, rather than the default Astro image service.

 `devFeatures.environmentVariables` Section titled “devFeatures.environmentVariables”
 Type: `boolean`
 Default: `false`

 Added in:
 `@astrojs/netlify@6.5.1`

Injects environment variables from your Netlify site into the development environment.

This allows you to use the same values in development as you would in production. See the Netlify docs on environment variables for more information, including how to use different variables for different environments.

### `staticHeaders`
 Section titled “staticHeaders”
 Type: `boolean`
 Default: `false`

 Added in:
 `@astrojs/netlify@7.0.0`
 New

Enables specifying custom headers for prerendered pages in Netlify’s configuration.

If enabled, the adapter will save static headers in the Framework API config file when provided by Astro features, such as Content Security Policy.

For example, when Content Security Policy is enabled, `staticHeaders` can be used to add the CSP `headers` to your Netlify configuration, instead of creating a `&#x3C;meta>` element:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import netlify from ' @astrojs/netlify ' ;
 export default defineConfig ({ security: { csp: true }, adapter: netlify ({ staticHeaders: true }) }); `

## Examples
 Section titled “Examples”

-
 The Astro Netlify Edge Starter provides an example and a guide in the README.

-
 Browse Astro Netlify projects on GitHub for more examples!

## More integrations

### Front-end frameworks

 -

###

 @astrojs/ alpinejs

-

###

 @astrojs/ preact

-

###

 @astrojs/ react

-

###

 @astrojs/ solid⁠-⁠js

-

###

 @astrojs/ svelte

-

###

 @astrojs/ vue

### Adapters

 -

###

 @astrojs/ cloudflare

-

###

 @astrojs/ netlify

-

###

 @astrojs/ node

-

###

 @astrojs/ vercel

### Other integrations

 -

###

 @astrojs/ db

-

###

 @astrojs/ markdoc

-

###

 @astrojs/ mdx

-

###

 @astrojs/ partytown

-

###

 @astrojs/ sitemap

 Learn

 Contribute

 Community

 Sponsor

## Node

#

 @astrojs/
 node

 v10.1.4

 GitHub

 npm

 Changelog

 This adapter allows Astro to deploy your on-demand rendered routes and features to Node targets, including server islands , actions , and sessions .

If you’re using Astro as a static site builder, you don’t need an adapter.

## Why Astro Node.js
 Section titled “Why Astro Node.js”
 Node.js is a JavaScript runtime for server-side code. @astrojs/node can be used either in standalone mode or as middleware for other http servers, such as Express .

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

Add the Node adapter to enable on-demand rendering in your Astro project with the `astro add` command.
This will install `@astrojs/node` and make the appropriate changes to your `astro.config.*` file in one step.

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add node `

 Terminal window
```
` pnpm astro add node `
```

 Terminal window
```
` yarn astro add node `
```

 Now, you can enable on-demand rendering per page , or set your build output configuration to `output: 'server'` to server-render all your pages by default .

### Manual Install
 Section titled “Manual Install”
 First, add the Node adapter to your project’s dependencies using your preferred package manager.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/node `

 Terminal window
```
` pnpm add @astrojs/node `
```

 Terminal window
```
` yarn add @astrojs/node `
```

 Then, add the adapter to your `astro.config.*` file:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import node from ' @astrojs/node ' ;
 export default defineConfig ({ adapter: node ({ mode: ' standalone ' , }), }); `

## Configuration
 Section titled “Configuration”
 @astrojs/node can be configured by passing options into the adapter function. The following options are available:

### `mode`
 Section titled “mode”
 Type: `'middleware' | 'standalone'`

Controls whether the adapter builds to `middleware` or `standalone` mode.

- `middleware` mode allows the built output to be used as middleware for another Node.js server, like Express.js or Fastify.

- `standalone` mode builds a server that automatically starts when the entry module is run. This allows you to more easily deploy your build to a host without needing additional code.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import node from ' @astrojs/node ' ;
 export default defineConfig ({ adapter: node ({ mode: ' middleware ' , }), }); `

### `staticHeaders`
 Section titled “staticHeaders”
 Type: `boolean`
 Default: `false`

 Added in:
 `@astrojs/node@10.0.0`

If enabled, the adapter will serve the headers of prerendered pages using the `Response` object when provided by Astro features, such as Content Security Policy.

For example, when Content Security Policy is enabled, `staticHeaders` can be used to add the CSP headers to the `Response` object instead of creating a `&#x3C;meta>` element:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import node from ' @astrojs/node ' ;
 export default defineConfig ({ security: { csp: true }, adapter: node ({ mode: ' standalone ' , staticHeaders: true , }) }); `

### `experimentalDisableStreaming`
 Section titled “experimentalDisableStreaming”
 Type: `boolean`
 Default: `false`

 Added in:
 `@astrojs/node@9.3.0`

Disables Astro’s default HTML streaming for pages rendered on demand.

HTML streaming helps with performance and generally provides a better visitor experience. In most cases, disabling streaming is not recommended.

However, when you need to disable HTML streaming (e.g. your host only supports non-streamed HTML caching at the CDN level), you can opt out of the default behavior:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import node from ' @astrojs/node ' ;
 export default defineConfig ({ adapter: node ({ mode: ' standalone ' , experimentalDisableStreaming: true , }), }); `

### `bodySizeLimit`
 Section titled “bodySizeLimit”
 Type: `number`
 Default: `1073741824` (1 GB)

 Added in:
 `@astrojs/node@10.0.0`

Sets the maximum allowed request body size in bytes. When the body of an incoming request exceeds this limit, an error will be thrown when the body is consumed.

Set to `Infinity` or `0` to disable the limit entirely. This may be useful if you need to accept very large request bodies, such as for video uploads.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import node from ' @astrojs/node ' ;
 export default defineConfig ({ adapter: node ({ mode: ' standalone ' , bodySizeLimit: 5 * 1024 * 1024 * 1024 , // 5 GB }), }); `

## Usage
 Section titled “Usage”
 First, performing a build . Depending on which `mode` selected (see above) follow the appropriate steps below:

### Middleware
 Section titled “Middleware”
 The server entrypoint is built to `./dist/server/entry.mjs` by default. This module exports a `handler` function that can be used with any framework that supports the Node `request` and `response` objects.

For example, with Express:

 run-server.mjs ` import express from ' express ' ; import { handler as ssrHandler } from ' ./dist/server/entry.mjs ' ;
 const app = express (); // Change this based on your astro.config.mjs, `base` option. // They should match. The default value is "/". const base = ' / ' ; app . use ( base , express . static ( ' dist/client/ ' )); app . use ( ssrHandler );
 app . listen ( 8080 ); `
 Or, with Fastify (>4):

 run-server.mjs ` import Fastify from ' fastify ' ; import fastifyMiddie from ' @fastify/middie ' ; import fastifyStatic from ' @fastify/static ' ; import { fileURLToPath } from ' node:url ' ; import { handler as ssrHandler } from ' ./dist/server/entry.mjs ' ;
 const app = Fastify ( { logger: true } );
 await app . register ( fastifyStatic , { root: fileURLToPath ( new URL ( ' ./dist/client ' , import. meta . url )), }) . register ( fastifyMiddie ); app . use ( ssrHandler );
 app . listen ({ port: 8080 }); `
 Additionally, you can also pass in an object to be accessed with `Astro.locals` or in Astro middleware:

 run-server.mjs ` import express from ' express ' ; import { handler as ssrHandler } from ' ./dist/server/entry.mjs ' ;
 const app = express (); app . use ( express . static ( ' dist/client/ ' )); app . use ( ( req , res , next ) => { const locals = { title: ' New title ' , } ;
 ssrHandler ( req , res , next , locals ); });
 app . listen ( 8080 ); ` { const locals = { title: &#x27;New title&#x27;, }; ssrHandler(req, res, next, locals);});app.listen(8080);">
 Note that middleware mode does not do file serving. You’ll need to configure your HTTP framework to do that for you. By default the client assets are written to `./dist/client/`.

### Standalone
 Section titled “Standalone”
 In standalone mode a server starts when the server entrypoint is run. By default it is built to `./dist/server/entry.mjs`. You can run it with:

 Terminal window ` node ./dist/server/entry.mjs `
 For standalone mode the server handles file serving in addition to the page and API routes.

#### Custom host and port
 Section titled “Custom host and port”
 You can override the host and port the standalone server runs on by passing them as environment variables at runtime:

 Terminal window ` HOST = 0.0.0.0 PORT = 4321 node ./dist/server/entry.mjs `

#### HTTPS
 Section titled “HTTPS”
 By default the standalone server uses HTTP. This works well if you have a proxy server in front of it that does HTTPS. If you need the standalone server to run HTTPS itself you need to provide your SSL key and certificate.

You can pass the path to your key and certification via the environment variables `SERVER_CERT_PATH` and `SERVER_KEY_PATH`. This is how you might pass them in bash:

 Terminal window ` SERVER_KEY_PATH = ./private/key.pem SERVER_CERT_PATH = ./private/cert.pem node ./dist/server/entry.mjs `

#### Assets
 Section titled “Assets”
 In standalone mode, assets in your `dist/client/` folder are served via the standalone server. You might be deploying these assets to a CDN, in which case the server will never actually be serving them. But in some cases, such as intranet sites, it’s fine to serve static assets directly from the application server.

Assets in the `dist/client/_astro/` folder are the ones that Astro has built. These assets are all named with a hash and therefore can be given long cache headers. Internally the adapter adds this header for these assets:

 ` Cache-Control: public, max-age=31536000, immutable `

## Sessions
 Section titled “Sessions”
 The Astro Sessions API allows you to easily store user data between requests. This can be used for things like user data and preferences, shopping carts, and authentication credentials. Unlike cookie storage, there are no size limits on the data, and it can be restored on different devices.

Astro uses the local filesystem for session storage when using the Node adapter. If you would prefer to use a different session storage driver, you can specify it in your Astro config. See the `session` configuration reference for more details.

## Environment variables
 Section titled “Environment variables”
 When using the `astro:env` secrets or `process.env` at runtime, neither Astro nor the adapter loads environment variables for you.

Some hosts may expose the environment variables you configure through their dashboard during the build and at runtime. Check your host’s documentation for setting and using environment variables within the specific platform.

When self-hosting, you can load environment variables through CLI commands or configuration files as appropriate:

 -

 Inline

-

 dotenvx

-

 Docker

 Terminal window
```
` DB_HOST = ... DB_PASSWORD = ... node ./dist/server/entry.mjs `
```

 Terminal window
```
` npx @dotenvx/dotenvx run -- node ./dist/server/entry.mjs `
```

 Dockerfile
```
` FROM node:lts AS runtime WORKDIR /app
 COPY . .
 RUN npm install RUN npm run build
 ENV DB_HOST=... ENV DB_PASSWORD=... CMD node ./dist/server/entry.mjs `
```

## More integrations

### Front-end frameworks

 -

###

 @astrojs/ alpinejs

-

###

 @astrojs/ preact

-

###

 @astrojs/ react

-

###

 @astrojs/ solid⁠-⁠js

-

###

 @astrojs/ svelte

-

###

 @astrojs/ vue

### Adapters

 -

###

 @astrojs/ cloudflare

-

###

 @astrojs/ netlify

-

###

 @astrojs/ node

-

###

 @astrojs/ vercel

### Other integrations

 -

###

 @astrojs/ db

-

###

 @astrojs/ markdoc

-

###

 @astrojs/ mdx

-

###

 @astrojs/ partytown

-

###

 @astrojs/ sitemap

 Learn

 Contribute

 Community

 Sponsor

## Vercel

#

 @astrojs/
 vercel

 v10.0.8

 GitHub

 npm

 Changelog

 This adapter allows Astro to deploy your on-demand rendered routes and features to Vercel , including server islands , actions , and sessions .

If you’re using Astro as a static site builder, you only need this adapter if you are using additional Vercel services (e.g. Vercel Web Analytics , Vercel Image Optimization ). Otherwise, you do not need an adapter to deploy your static site.

Learn how to deploy your Astro site in our Vercel deployment guide .

## Why Astro Vercel?
 Section titled “Why Astro Vercel?”
 Vercel is a deployment platform that allows you to host your site by connecting directly to your GitHub repository. This adapter enhances the Astro build process to prepare your project for deployment through Vercel.

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

Add the Vercel adapter to enable on-demand rendering in your Astro project with the following `astro add` command. This will install `@astrojs/vercel` and make the appropriate changes to your `astro.config.mjs` file in one step.

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add vercel `

 Terminal window
```
` pnpm astro add vercel `
```

 Terminal window
```
` yarn astro add vercel `
```

 Now, you can enable on-demand rendering per page , or set your build output configuration to `output: 'server'` to server-render all your pages by default .

### Manual Install
 Section titled “Manual Install”
 First, add the `@astrojs/vercel` adapter to your project’s dependencies using your preferred package manager:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/vercel `

 Terminal window
```
` pnpm add @astrojs/vercel `
```

 Terminal window
```
` yarn add @astrojs/vercel `
```

 Then, add the adapter to your `astro.config.*` file:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ // ... adapter: vercel (), }); `

## Usage
 Section titled “Usage”

 Find out more about deploying your project to Vercel .

 You can deploy by CLI (`vercel deploy`) or by connecting your new repo in the Vercel Dashboard . Alternatively, you can create a production build locally:

 Terminal window ` astro build vercel deploy --prebuilt `

## Configuration
 Section titled “Configuration”
 To configure this adapter, pass an object to the `vercel()` function call in `astro.config.mjs`:

### `webAnalytics`
 Section titled “webAnalytics”
 Type: `VercelWebAnalyticsConfig`
 Available for: Serverless, Static

 Added in:
 `@astrojs/vercel@3.8.0`

With `@vercel/analytics@1.3.x` or earlier, you can set `webAnalytics: { enabled: true }` in your Astro config to inject Vercel’s tracking scripts into all of your pages.

For `@vercel/analytics@1.4.0` and later, use Vercel’s Analytics component to enable Vercel Web Analytics instead.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ // ... adapter: vercel ({ webAnalytics: { enabled: true , }, }), }); `

### `imagesConfig`
 Section titled “imagesConfig”
 Type: `VercelImageConfig`
 Available for: Serverless, Static

 Added in:
 `@astrojs/vercel@3.3.0`

Configuration options for Vercel’s Image Optimization API . See Vercel’s image configuration documentation for a complete list of supported parameters.

The `domains` and `remotePatterns` properties will automatically be filled using the Astro corresponding `image` settings .

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ // ... output: ' static ' , adapter: vercel ({ imagesConfig: { sizes: [ 320 , 640 , 1280 ], }, }), }); `

### `imageService`
 Section titled “imageService”
 Type: `boolean`
 Available for: Serverless, Static

 Added in:
 `@astrojs/vercel@3.3.0`

When enabled, an Image Service powered by the Vercel Image Optimization API will be automatically configured and used in production. In development, the image service specified by `devImageService` will be used instead.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ // ... output: ' static ' , adapter: vercel ({ imageService: true , }), }); `
 src/pages/index.astro
```
` --- import { Image } from ' astro:assets ' ; import astroLogo from ' ../assets/logo.png ' ; ---
 &#x3C;!-- This component --> &#x3C; Image src = { astroLogo } alt = " My super logo! " />
 &#x3C;!-- will become the following HTML --> &#x3C; img src = " /_vercel/image?url=_astro/logo.hash.png&#x26;w=...&#x26;q=... " alt = " My super logo! " loading = " lazy " decoding = " async " width = " ... " height = " ... " /> `
```
  ">

### `devImageService`
 Section titled “devImageService”
 Type: `'sharp' | string`
 Default: `sharp`
 Available for: Serverless, Static

 Added in:
 `@astrojs/vercel@3.8.0`

Allows you to configure which image service to use in development when imageService is enabled. This can be useful if you cannot install Sharp’s dependencies on your development machine, but using another image service like Squoosh would allow you to preview images in your dev environment. Build is unaffected and will always use Vercel’s Image Optimization.

It can also be set to any arbitrary value in order to use a custom image service instead of Astro’s built-in ones.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ // ... adapter: vercel ({ imageService: true , devImageService: ' sharp ' , }), }); `

### `isr`
 Section titled “isr”
 Type: `boolean | VercelISRConfig`
 Default: `false`
 Available for: Serverless

 Added in:
 `@astrojs/vercel@7.2.0`

Allows your project to be deployed as an ISR (Incremental Static Regeneration) function, which caches your on-demand rendered pages in the same way as prerendered pages after first request.

To enable this feature, set `isr` to true in your Vercel adapter configuration in `astro.config.mjs`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ // ... adapter: vercel ({ isr: true , }), }); `
 Note that ISR function requests do not include search params, similar to requests in static mode.

#### ISR cache invalidation
 Section titled “ISR cache invalidation”
 By default, an ISR function caches for the duration of your deployment. You can further control caching by setting an expiration time, or by excluding particular routes from caching entirely.

 Time-based invalidation Section titled “Time-based invalidation”
 By default, when ISR is enabled, routes use Vercel’s cache shielding and any Cache-Control headers are ignored. Configuring an `expiration` value (in seconds) allows you to control how long routes are cached. This means Cache-Control directives set by your application are also respected.

The following example defines `expiration` to cache all pages on first request and save them for 1 day:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ // ... adapter: vercel ({ isr: { expiration: 60 * 60 * 24 , }, }), }); `
 On-demand invalidation Section titled “On-demand invalidation”
 To programmatically invalidate cached pages, create a bypass token and provide it to the `isr` config:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ adapter: vercel ({ isr: { // A secret random string that you create. bypassToken: " 005556d774a8 " , } }) }) `
 You can then invalidate a cached page by sending a HEAD or GET request to the page URL with the `x-prerender-revalidate` header set to your bypass token. See Vercel’s on-demand ISR documentation for details.

 Draft mode Section titled “Draft mode”
 To bypass the ISR cache and render fresh content (e.g., for previewing unpublished CMS content), use Vercel’s Draft mode . This requires defining a `bypassToken` in your configuration and reusing its value in your pages to set a cookie named `__prerender_bypass`.

 Excluding paths from caching Section titled “Excluding paths from caching”
 Use the `exclude` option to prevent specific routes from being cached by ISR. These paths will always be rendered fresh on each request:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ adapter: vercel ({ isr: { // Paths that will always be served fresh. exclude: [ ' /preview ' , ' /auth/[page] ' , / ^ \/ api \/ . + / // Regular expressions supported since @astrojs/vercel@v8.1.0 ] } }) }) `

### `includeFiles`
 Section titled “includeFiles”
 Type: `string[]`
 Available for: Serverless

Use this property to force files to be bundled with your function. This is helpful when you notice missing files.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ // ... adapter: vercel ({ includeFiles: [ ' ./my-data.json ' ], }), }); `

### `excludeFiles`
 Section titled “excludeFiles”
 Type: `string[]`
 Available for: Serverless

Use this property to exclude any files from the bundling process that would otherwise be included.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ // ... adapter: vercel ({ excludeFiles: [ ' ./src/some_big_file.jpg ' ], }), }); `

### `maxDuration`
 Section titled “maxDuration”
 Type: `number`
 Available for: Serverless

Use this property to extend or limit the maximum duration (in seconds) that Serverless Functions can run before timing out. See the Vercel documentation for the default and maximum limit for your account plan.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ // ... adapter: vercel ({ maxDuration: 60 }), }); `

### `skewProtection`
 Section titled “skewProtection”
 Type: `boolean`
 Available for: Serverless

 Added in:
 `@astrojs/vercel@7.6.0`

Use this property to enable Vercel Skew protection (available with Vercel Pro and Enterprise accounts).

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ // ... adapter: vercel ({ skewProtection: true }), }); `

### `staticHeaders`
 Section titled “staticHeaders”
 Type: `boolean`
 Default: `false`
 Available for: Serverless

 Added in:
 `@astrojs/vercel@10.0.0`
 New

Enables specifying custom headers for prerendered pages in Vercel’s configuration.

If enabled, the adapter will save static headers in the Vercel `vercel.json` file when provided by Astro features, such as Content Security Policy.

For example, when Content Security Policy is enabled, `staticHeaders` can be used to add the CSP `headers` to your Vercel configuration, instead of creating a `&#x3C;meta>` element:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ security: { csp: true }, adapter: vercel ({ staticHeaders: true }) }); `

### Running Astro middleware on Vercel Edge Functions
 Section titled “Running Astro middleware on Vercel Edge Functions”
 The `@astrojs/vercel` adapter can create an edge function from an Astro middleware in your code base. When `middlewareMode` is set to `'edge'`, an edge function will execute your middleware code for all requests, including static assets, prerendered pages, and on-demand rendered pages.

For on-demand rendered pages, the `context.locals` object is serialized using JSON and sent in a header for the serverless function, which performs the rendering. As a security measure, the serverless function will refuse to serve requests with a `403 Forbidden` response unless they come from the generated edge function.

This is an opt-in feature. To enable it, set `middlewareMode` to `'edge'`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ // ... adapter: vercel ({ middlewareMode: ' edge ' , }), }); `
 The edge middleware has access to Vercel’s `RequestContext` as `ctx.locals.vercel.edge`. If you’re using TypeScript, you can get proper typings by updating `src/env.d.ts` to use `EdgeLocals`:

 ` type EdgeLocals = import ( ' @astrojs/vercel ' ). EdgeLocals
 declare namespace App { interface Locals extends EdgeLocals { // ... } } `

### Sessions
 Section titled “Sessions”
 The Astro Sessions API allows you to easily store user data between requests. This can be used for things like user data and preferences, shopping carts, and authentication credentials. Unlike cookie storage, there are no size limits on the data, and it can be restored on different devices.

When using sessions on Vercel, you need to configure a driver for session storage. You can install a storage provider from the Vercel marketplace .

For example, if you have installed a Redis integration and linked a database to your site:

-
Install the `ioredis` package:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install ioredis `

 Terminal window
```
` pnpm install ioredis `
```

 Terminal window
```
` yarn add ioredis `
```

-
 Use the Vercel CLI to load your environment variables:

 Terminal window ` vercel env pull .env.local `
 This will create a `.env.local` file in your project root with the environment variables needed to connect to your Redis database when developing locally.

-
Configure the session driver:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import vercel from ' @astrojs/vercel ' ;
 export default defineConfig ({ adapter: vercel (), session: { driver: ' redis ' , options: { url: process . env . REDIS_URL , }, }, }); `

## Node.js Version Support
 Section titled “Node.js Version Support”
 The `@astrojs/vercel` adapter supports specific Node.js versions for deploying your Astro project on Vercel. To view the supported Node.js versions on Vercel, click on the settings tab for a project and scroll down to “Node.js Version” section.

Check out the Vercel documentation to learn more.

## More integrations

### Front-end frameworks

 -

###

 @astrojs/ alpinejs

-

###

 @astrojs/ preact

-

###

 @astrojs/ react

-

###

 @astrojs/ solid⁠-⁠js

-

###

 @astrojs/ svelte

-

###

 @astrojs/ vue

### Adapters

 -

###

 @astrojs/ cloudflare

-

###

 @astrojs/ netlify

-

###

 @astrojs/ node

-

###

 @astrojs/ vercel

### Other integrations

 -

###

 @astrojs/ db

-

###

 @astrojs/ markdoc

-

###

 @astrojs/ mdx

-

###

 @astrojs/ partytown

-

###

 @astrojs/ sitemap

 Learn

 Contribute

 Community

 Sponsor

## Db

#

 @astrojs/
 db

 v0.21.3

 GitHub

 npm

 Changelog

 Astro DB is a fully-managed SQL database designed for the Astro ecosystem: develop locally in Astro and deploy to any libSQL-compatible database .

With Astro DB you have a powerful, local, type-safe tool to query and model content as a relational database.

 See the Astro DB guide for full usage and examples.

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

Run one of the following commands in a new terminal window.

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add db `

 Terminal window
```
` pnpm astro add db `
```

 Terminal window
```
` yarn astro add db `
```

#### Manual Installation
 Section titled “Manual Installation”
 If you prefer to set things up from scratch yourself, skip `astro add` and follow these instructions to install Astro DB yourself.

 1. Install the integration from npm via a package manager Section titled “1. Install the integration from npm via a package manager”

 npm

-

 pnpm

-

 Yarn

 Terminal window
```
` npm install @astrojs/db `
```

 Terminal window
```
` pnpm add @astrojs/db `
```

 Terminal window
```
` yarn add @astrojs/db `
```

 2. Add the integration to `astro.config.mjs` Section titled “2. Add the integration to astro.config.mjs”
 astro.config.mjs
```
` import { defineConfig } from ' astro/config ' ; import db from ' @astrojs/db ' ;
 export default defineConfig ({ integrations: [ db () ] }); `
```

 3. Configure your database Section titled “3. Configure your database”
 Create a `db/config.ts` file at the root of your project. This is a special file that Astro will automatically load and use to configure your database tables.

 db/config.ts ` import { defineDb } from ' astro:db ' ;
 export default defineDb ({ tables: {}, }) `

## Configuration
 Section titled “Configuration”

### `mode`
 Section titled “mode”
 Type: `'node' | 'web'`
 Default: `'node'`

 Added in:
 `@astrojs/db@0.18.0`

Configures the driver to use to connect to your database in production.

By default, Astro DB uses a Node.js-based libSQL driver for production deployments. The `node` driver mode is sufficient for most Astro hosted or self-hosted websites with Node.js runtimes. This allows you to connect to your database over several protocols, including `memory:`, `file:`, `ws:`, `wss:`, `libsql`, `http`, and `https`, as well as allowing for more advanced features such as embedded replicas .

When deploying to a serverless environment on a non-Node.js runtime, such as Cloudflare Workers or Deno, a web-based libSQL driver is available. When deploying using the `web` mode, you will be able to make web-based connections over `libsql`, `http`, or `https`.

To use the web libSQL driver mode for non-Node.js environments, set the `mode` property in your adapter’s configuration:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import db from ' @astrojs/db ' ;
 export default defineConfig ({ integrations: [ db ({ mode: ' web ' }) ] }); `

## Table configuration reference
 Section titled “Table configuration reference”

### `columns`
 Section titled “columns”
 Type: `ColumnsConfig`

Table columns are configured using the `columns` object:

 ` import { defineTable, column, NOW } from ' astro:db ' ;
 const Comment = defineTable ( { columns: { id: column . number ( { primaryKey: true } ) , author: column . text () , content: column . text ( { optional: true } ) , published: column . date ( { default: NOW } ) , }, } ); `
 Columns are configured using the `column` utility. `column` supports the following types:

- `column.text(...)` - store either plain or rich text content

- `column.number(...)` - store integer and floating point values

- `column.boolean(...)` - store true / false values

- `column.date(...)` - store `Date` objects, parsed as ISO strings for data storage

- `column.json(...)` - store arbitrary JSON blobs, parsed as stringified JSON for data storage

There are a few shared configuration values across all columns:

- `primaryKey` - Set a `number` or `text` column as the unique identifier.

- `optional` - Astro DB uses `NOT NULL` for all columns by default. Set `optional` to `true` to allow null values.

- `default` - Set the default value for newly inserted entries. This accepts either a static value or a string of `sql` for generated values like timestamps.

- `unique` - Mark a column as unique. This prevents duplicate values across entries in the table.

- `references` - Reference a related table by column. This establishes a foreign key constraint, meaning each column value must have a matching value in the referenced table.

A `text` column can optionally define a list of string literals to serve as an enum for generating types. However, no runtime validation will be performed . Removing, adding, and changing values should be handled in your project code.

 db/config.ts ` import { defineTable, column } from ' astro:db ' ;
 // Table definition const UserTable = defineTable ( { columns: { id: column . number ( { primaryKey: true } ) , name: column . text () , rank: column . text ( { enum: [ ' user ' , ' mod ' , ' admin ' ] } ) , }, } );
 // Resulting type definition type UserTableInferInsert = { id ?: string ; name : string ; rank : " user " | " mod " | " admin " ; } `

### `indexes`
 Section titled “indexes”
 Type: `{ on: string | string[]; unique?: boolean | undefined; name?: string | undefined; }[]`

Table indexes are used to improve lookup speeds on a given column or combination of columns. The `indexes` property accepts an array of configuration objects specifying the columns to index:

 db/config.ts ` import { defineTable, column } from ' astro:db ' ;
 const Comment = defineTable ( { columns: { authorId: column . number () , published: column . date () , body: column . text () , }, indexes: [ { on: [ " authorId " , " published " ], unique: true }, ] } ); `
 This will generate a unique index on the `authorId` and `published` columns with the name `Comment_authorId_published_idx`.

The following configuration options are available for each index:

- `on` - A single column or array of column names to index.

- `unique` (optional) - Set to `true` to enforce unique values across the indexed columns.

- `name` (optional) - A custom name for the unique index. This will override Astro’s generated name based on the table and column names being indexed (e.g. `Comment_authorId_published_idx`). Custom names are global, so ensure index names do not conflict between tables.

### `foreignKeys`
 Section titled “foreignKeys”
 Type: `{ columns: string | string[]; references: () => Column | Column[]; }[]`

Foreign keys are used to establish a relationship between two tables. The `foreignKeys` property accepts an array of configuration objects that may relate one or more columns between tables:

 db/config.ts ` import { defineTable, column } from ' astro:db ' ;
 const Author = defineTable ( { columns: { firstName: column . text () , lastName: column . text () , }, } );
 const Comment = defineTable ( { columns: { authorFirstName: column . text () , authorLastName: column . text () , body: column . text () , }, foreignKeys: [ { columns: [ " authorFirstName " , " authorLastName " ], references : () => [Author . columns . firstName , Author . columns . lastName ], }, ] , } ); ` [Author.columns.firstName, Author.columns.lastName], }, ],});">
 Each foreign key configuration object accepts the following properties:

- `columns` - A single column or array of column names to relate to the referenced table.

- `references` - A function that returns a single column or an array of columns from the referenced table.

## Astro DB CLI reference
 Section titled “Astro DB CLI reference”
 Astro DB includes a set of CLI commands to interact with your local and libSQL-compatible database.

These commands are called automatically when using a GitHub CI action, and can be called manually using the `astro db` CLI.

### `astro db push`
 Section titled “astro db push”
 Flags:

- `--db-app-token &#x3C;token>` Provide the remote database app token directly instead of `ASTRO_DB_APP_TOKEN`.

- `--dry-run` Print the generated SQL statements without applying them.

- `--force-reset` Reset all production data if a breaking schema change is required.

- `--remote` Push to your remote database instead of the local database file. Requires the `ASTRO_DB_REMOTE_URL` environment variable to be set, and either `ASTRO_DB_APP_TOKEN` to be set in the environment or a value passed with the `--db-app-token` command-line argument.

Safely push database configuration changes to your project database. This will check for any risk of data loss and guide you on any recommended migration steps. Use `--remote` to apply changes to your remote database. If a breaking schema change must be made, use `--force-reset` to reset all production data.

### `astro db verify`
 Section titled “astro db verify”
 Flags:

- `--db-app-token &#x3C;token>` Provide the remote database app token directly instead of `ASTRO_DB_APP_TOKEN`.

- `--json` Print a machine-readable JSON result from `verify`.

- `--remote` Compare against your remote database instead of the local database file. Requires the `ASTRO_DB_REMOTE_URL` environment variable to be set, and either `ASTRO_DB_APP_TOKEN` to be set in the environment or a value passed with the `--db-app-token` command-line argument.

Compares your local schema against the remote database to check for any differences between your local and remote database configurations. This is automatically run by `astro db push`.

`verify` will compare your local `db/config.ts` file with the remote database and warn if changes are detected. It will exit with a non-zero code if changes are required or unsafe, making it useful for CI.

### `astro db execute &#x3C;file-path>`
 Section titled “astro db execute &#x3C;file-path>”
 Flags:

- `--db-app-token &#x3C;token>` Provide the remote database app token directly instead of `ASTRO_DB_APP_TOKEN`.

- `--remote` Run against your libSQL-compatible database. Omit to run against your local database file. Requires the `ASTRO_DB_REMOTE_URL` environment variable to be set, and either `ASTRO_DB_APP_TOKEN` to be set in the environment or a value passed with the `--db-app-token` command-line argument.

Execute a `.ts` or `.js` file to read or write to your database. This accepts a file path as an argument, and supports usage of the `astro:db` module to write type-safe queries. Use the `--remote` flag to run against your libSQL-compatible database, or omit the flag to run against your local database file. See how to seed development data for an example file.

### `astro db shell --query &#x3C;sql-string>`
 Section titled “astro db shell --query &#x3C;sql-string>”
 Flags:

- `--query` Raw SQL query to execute.

- `--remote` Run against your libSQL-compatible database. Omit to run against your local database file. Requires the `ASTRO_DB_REMOTE_URL` environment variable to be set, and either `ASTRO_DB_APP_TOKEN` to be set in the environment or a value passed with the `--db-app-token` command-line argument.

Execute a raw SQL query against your database.

The following example selects all rows from a `Comment` table in a remote database:

 Terminal window ` npx astro db shell --query " SELECT * FROM Comment; " --remote `

## Astro DB utility reference
 Section titled “Astro DB utility reference”
 The following utilities are imported from the `astro:db` module:

 ` import { isDbError, getDbError } from " astro:db " ; `

### `isDbError()`
 Section titled “isDbError()”
 Type: `(err: unknown) => boolean`

 Added in:
 `@astrojs/db@0.9.1`

Checks if an error is a libSQL database exception. This may include a foreign key constraint error when using references, or missing fields when inserting data. You can combine `isDbError()` with a try / catch block to handle database errors in your application:

 src/pages/api/comment/[id].ts ` import { db, Comment, isDbError } from ' astro:db ' ; import type { APIRoute } from ' astro ' ;
 export const POST : APIRoute = ( ctx ) => { try { await db . insert (Comment) . values ( { id: ctx . params . id , content: ' Hello, world! ' } ) ; } catch (e) { if ( isDbError (e)) { return new Response ( ` Cannot insert comment with id ${ id } \n\n ${ e . message } ` , { status: 400 } ) ; } return new Response ( ' An unexpected error occurred ' , { status: 500 } ) ; }
 return new Response ( null , { status: 201 } ) ; } ; ` { try { await db.insert(Comment).values({ id: ctx.params.id, content: &#x27;Hello, world!&#x27; }); } catch (e) { if (isDbError(e)) { return new Response(&#x60;Cannot insert comment with id ${id}\n\n${e.message}&#x60;, { status: 400 }); } return new Response(&#x27;An unexpected error occurred&#x27;, { status: 500 }); } return new Response(null, { status: 201 });};">

### `getDbError()`
 Section titled “getDbError()”
 Type: `(err: unknown) => LibsqlError | undefined`

 Added in:
 `@astrojs/db@0.21.0`
 New

Walks through an error’s cause chain to find the underlying libSQL database exception. This returns a `LibsqlError` or `undefined` if the error is not from LibSQL. This is useful when another error (e.g. `DrizzleQueryError`) may wrap the database error.

The following example extracts the database error from a caught exception and returns the error code and message in the response:

 src/pages/api/comment/[id].ts
```
` import { getDbError } from ' astro:db ' ;
 export const POST : APIRoute = ( ctx ) => { try { await db . insert (Comment) . values ( { id: ctx . params . id , content: ' Hello, world! ' } ) ; } catch (e) { const dbError = getDbError (e) ; if (dbError) { return new Response ( ` Database error: ${ dbError . code } \n\n ${ dbError . message } ` , { status: 400 } ) ; } return new Response ( ' An unexpected error occurred ' , { status: 500 } ) ; }
 return new Response ( null , { status: 201 } ) ; } ; `
```
 { try { await db.insert(Comment).values({ id: ctx.params.id, content: &#x27;Hello, world!&#x27; }); } catch (e) { const dbError = getDbError(e); if (dbError) { return new Response(&#x60;Database error: ${dbError.code}\n\n${dbError.message}&#x60;, { status: 400 }); } return new Response(&#x27;An unexpected error occurred&#x27;, { status: 500 }); } return new Response(null, { status: 201 });};">

## More integrations

### Front-end frameworks

 -

###

 @astrojs/ alpinejs

-

###

 @astrojs/ preact

-

###

 @astrojs/ react

-

###

 @astrojs/ solid⁠-⁠js

-

###

 @astrojs/ svelte

-

###

 @astrojs/ vue

### Adapters

 -

###

 @astrojs/ cloudflare

-

###

 @astrojs/ netlify

-

###

 @astrojs/ node

-

###

 @astrojs/ vercel

### Other integrations

 -

###

 @astrojs/ db

-

###

 @astrojs/ markdoc

-

###

 @astrojs/ mdx

-

###

 @astrojs/ partytown

-

###

 @astrojs/ sitemap

 Learn

 Contribute

 Community

 Sponsor

## Mdx

#

 @astrojs/
 mdx

 v6.0.3

 GitHub

 npm

 Changelog

 This Astro integration enables the usage of MDX components and allows you to create pages as `.mdx` files.

## Why MDX?
 Section titled “Why MDX?”
 MDX allows you to use variables, JSX expressions and components within Markdown content in Astro. If you have existing content authored in MDX, this integration allows you to bring those files to your Astro project.

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

Run one of the following commands in a new terminal window.

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add mdx `

 Terminal window
```
` pnpm astro add mdx `
```

 Terminal window
```
` yarn astro add mdx `
```

 If you run into any issues, feel free to report them to us on GitHub and try the manual installation steps below.

### Manual Install
 Section titled “Manual Install”
 First, install the `@astrojs/mdx` package:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/mdx `

 Terminal window
```
` pnpm add @astrojs/mdx `
```

 Terminal window
```
` yarn add @astrojs/mdx `
```

 Then, apply the integration to your `astro.config.*` file using the `integrations` property:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import mdx from ' @astrojs/mdx ' ;
 export default defineConfig ({ // ... integrations: [ mdx () ], }); `

### Editor Integration
 Section titled “Editor Integration”
 For editor support in VS Code , install the official MDX extension .

For other editors, use the MDX language server .

## Usage
 Section titled “Usage”
 Visit the MDX docs to learn about using standard MDX features.

## MDX in Astro
 Section titled “MDX in Astro”
 Adding the MDX integration enhances your Markdown authoring with JSX variables, expressions and components.

It also adds extra features to standard MDX, including support for Markdown-style frontmatter in MDX. This allows you to use most of Astro’s built-in Markdown features .

`.mdx` files must be written in MDX syntax rather than Astro’s HTML-like syntax.

### Using local MDX with content collections
 Section titled “Using local MDX with content collections”
 To include your local MDX files in a content collection, make sure that your collection loader is configured to load content from `.mdx` files:

 src/content.config.ts ` import { defineCollection } from ' astro:content ' ; import { glob } from ' astro/loaders ' ; import { z } from ' astro/zod ' ;
 const blog = defineCollection ( { loader: glob ( { pattern: " **/*.{md, mdx } " , base: " ./src/blog " } ) , schema: z . object ( { title: z . string () , description: z . string () , pubDate: z . coerce . date () , } ) } );
 export const collections = { blog } ; `

### Using Exported Variables in MDX
 Section titled “Using Exported Variables in MDX”
 MDX supports using `export` statements to add variables to your MDX content or to export data to a component that imports it.

For example, you can export a `title` field from an MDX page or component to use as a heading with `{JSX expressions}`:

 /src/blog/posts/post-1.mdx ` export const title = ' My first MDX post '
 # { title } `
 Or you can use that exported `title` in your page using `import` and `import.meta.glob()` statements:

 src/pages/index.astro ` --- const matches = import. meta . glob ( ' ./posts/*.mdx ' , { eager: true } ); const posts = Object . values (matches); ---
 { posts . map ( post => &#x3C; p > { post . title } &#x3C;/ p > ) } ` {post.title}
)}">

#### Exported Properties
 Section titled “Exported Properties”
 The following properties are available to a `.astro` component when using an `import` statement or `import.meta.glob()`:

- `file` - The absolute file path (e.g. `/home/user/projects/.../file.mdx`).

- `url` - The URL of the page (e.g. `/en/guides/markdown-content`).

- `frontmatter` - Contains any data specified in the file’s YAML/TOML frontmatter.

- `getHeadings()` - An async function that returns an array of all headings (`&#x3C;h1>` to `&#x3C;h6>`) in the file with the type: `{ depth: number; slug: string; text: string }[]`. Each heading’s `slug` corresponds to the generated ID for a given heading and can be used for anchor links. Headings from imported files are not included.

- `&#x3C;Content />` - A component that returns the full, rendered contents of the file.

- (any `export` value) - MDX files can also export data with an `export` statement.

### Using Frontmatter Variables in MDX
 Section titled “Using Frontmatter Variables in MDX”
 The Astro MDX integration includes support for using frontmatter in MDX by default. Add frontmatter properties just as you would in Markdown files, and these variables are available to use in the template, and as named properties when importing the file somewhere else.

 /src/blog/posts/post-1.mdx ` --- title : ' My first MDX post ' author : ' Houston ' ---
 # { frontmatter . title }
 Written by: { frontmatter . author } `

### Using Components in MDX
 Section titled “Using Components in MDX”
 After installing the MDX integration, you can import and use both Astro components and UI framework components in MDX (`.mdx`) files just as you would use them in any other Astro component.

Don’t forget to include a `client:directive` on your UI framework components, if necessary!

See more examples of using import and export statements in the MDX docs .

 src/blog/post-1.mdx ` --- title : My first post --- import ReactCounter from ' ../components/ReactCounter.jsx ' ;
 I just started my new Astro blog!
 Here is my counter component, working in MDX: &#x3C; ReactCounter client : load /> ` ">

#### Assigning Custom Components to HTML elements
 Section titled “Assigning Custom Components to HTML elements”
 With MDX, you can map Markdown syntax to custom components instead of their standard HTML elements. This allows you to write in standard Markdown syntax, but apply special component styling to selected elements.

For example, you can create a `Blockquote.astro` component to provide custom styling for `&#x3C;blockquote>` content:

 src/components/Blockquote.astro ` --- const props = Astro . props ; --- &#x3C; blockquote { ... props } class = " bg-blue-50 p-4 " > &#x3C; span class = " text-4xl text-blue-600 mb-2 " > “ &#x3C;/ span > &#x3C; slot /> &#x3C;!-- Be sure to add a `&#x3C;slot/>` for child content! --> &#x3C;/ blockquote > `  “   ">
 Import your custom component into your `.mdx` file, then export a `components` object that maps the standard HTML element to your custom component:

 src/blog/posts/post-1.mdx ` import Blockquote from ' ../components/Blockquote.astro ' ; export const components = {blockquote: Blockquote }
 > This quote will be a custom Blockquote ` This quote will be a custom Blockquote">
 Visit the MDX website for a full list of HTML elements that can be overwritten as custom components.

#### Passing `components` to MDX content
 Section titled “Passing components to MDX content”
 When rendering imported MDX content with the `&#x3C;Content />` component, including rendering MDX entries using content collections, custom components can be passed via the `components` prop. These components must first be imported to make them available to the `&#x3C;Content />` component.

The `components` object maps HTML element names (`h1`, `h2`, `blockquote`, etc.) to your custom components. You can also include all components exported from the MDX file itself using the spread operator (`...`), which must also be imported from your MDX file as `components`.

If you are importing MDX directly from a single file for use in an Astro component, import both the `Content` component and any exported components from your MDX file.

 src/pages/page.astro ` --- import { Content, components } from ' ../content.mdx ' ; import Heading from ' ../Heading.astro ' ; --- &#x3C;!-- Creates a custom &#x3C;h1> for the # syntax, _and_ applies any custom components defined in `content.mdx` --> &#x3C; Content components = { { ... components , h1: Heading } } /> ` ">
 If your MDX file is a content collections entry, then use the `render()` function from `astro:content` to access the `&#x3C;Content />` component.

The following example passes a custom heading to the `&#x3C;Content />` component via the `components` prop to be used in place of all `&#x3C;h1>` HTML elements:

 src/pages/blog/post-1.astro ` --- import { getEntry, render } from ' astro:content ' ; import CustomHeading from ' ../../components/CustomHeading.astro ' ; const entry = await getEntry ( ' blog ' , ' post-1 ' ); const { Content } = await render (entry); --- &#x3C; Content components = { { h1: CustomHeading } } /> ` ">

## Configuration
 Section titled “Configuration”
 Once the MDX integration is installed, no configuration is necessary to use `.mdx` files in your Astro project.

You can configure how your MDX is rendered with the following options:

- Options inherited from Markdown config

- `processor`

- `extendMarkdownConfig`

- `recmaPlugins`

- `optimize`

### Options inherited from Markdown config
 Section titled “Options inherited from Markdown config”
 All `markdown` configuration options can be configured separately in the MDX integration, including the Markdown processor , syntax highlighting, and more. Options will default to those in your Markdown config ( see the `extendMarkdownConfig` option to modify this).

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { unified } from ' @astrojs/markdown-remark ' ; import mdx from ' @astrojs/mdx ' ; import remarkToc from ' remark-toc ' ; import rehypePresetMinify from ' rehype-preset-minify ' ;
 export default defineConfig ({ // ... integrations: [ mdx ({ syntaxHighlight: ' shiki ' , shikiConfig: { theme: ' dracula ' }, processor: unified ({ remarkPlugins: [ remarkToc ], rehypePlugins: [ rehypePresetMinify ], remarkRehype: { footnoteLabel: ' Footnotes ' }, gfm: false }), }), ], }); `

 See the Markdown Options reference for a complete list of options.

### `processor`
 Section titled “processor”
 Type: `MarkdownProcessor`
 Default: inherited from `markdown.processor`

 Added in:
 `@astrojs/mdx@6.0.0`
 New

By default, `.mdx` files render through the same Markdown processor as your `.md` files. Set `processor` to use a different processor, or the same processor with different options, for `.mdx` files only.

For example, to keep the default remark/rehype processor for `.md` files while rendering `.mdx` files with Sätteri using `@astrojs/markdown-satteri`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { satteri } from ' @astrojs/markdown-satteri ' ; import mdx from ' @astrojs/mdx ' ;
 export default defineConfig ({ integrations: [ mdx ({ processor: satteri () }), ], }); `

### `extendMarkdownConfig`
 Section titled “extendMarkdownConfig”
 Type: `boolean`
 Default: `true`

 Added in:
 `@astrojs/mdx@0.15.0`

MDX will extend your project’s existing Markdown configuration by default. To override individual options, you can specify their equivalent in your MDX configuration.

For example, say you need a different syntax highlighter and a different set of plugins for `.mdx` files. You can apply these options like so, with `extendMarkdownConfig` enabled by default:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { unified } from ' @astrojs/markdown-remark ' ; import mdx from ' @astrojs/mdx ' ;
 export default defineConfig ({ // ... markdown: { syntaxHighlight: ' prism ' , processor: unified ({ remarkPlugins: [ remarkPlugin1 ] }), }, integrations: [ mdx ({ // Markdown `syntaxHighlight` overridden, // `.mdx` files use Shiki instead. syntaxHighlight: ' shiki ' ,
 // `markdown.processor` gets overridden for `.mdx` files by this option processor: unified ({ remarkPlugins: [ remarkPlugin2 ] }), }), ], }); `
 You may also need to disable `markdown` config extension in MDX. For this, set `extendMarkdownConfig` to `false`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { unified } from ' @astrojs/markdown-remark ' ; import mdx from ' @astrojs/mdx ' ;
 export default defineConfig ({ // ... markdown: { processor: unified ({ remarkPlugins: [ remarkPlugin ] }), }, integrations: [ mdx ({ // Markdown config now ignored extendMarkdownConfig: false , // Default `unified()` processor used }), ], }); `

### `recmaPlugins`
 Section titled “recmaPlugins”
 Type: `PluggableList`
 Default: `[]`

 Added in:
 `@astrojs/mdx@0.11.5`

These are plugins that modify the output estree directly. This is useful for modifying or injecting JavaScript variables in your MDX files.

We suggest using AST Explorer to play with estree outputs, and trying `estree-util-visit` for searching across JavaScript nodes.

### `optimize`
 Section titled “optimize”
 Type: `boolean | { ignoreElementNames?: string[] }`
 Default: `false`

 Added in:
 `@astrojs/mdx@0.19.5`

This is an optional configuration setting to optimize the MDX output for faster builds and rendering via an internal rehype plugin. This may be useful if you have many MDX files and notice slow builds. However, this option may generate some unescaped HTML, so make sure your site’s interactive parts still work correctly after enabling it.

This is disabled by default. To enable MDX optimization, add the following to your MDX integration configuration:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import mdx from ' @astrojs/mdx ' ;
 export default defineConfig ({ // ... integrations: [ mdx ({ optimize: true , }), ], }); `

#### `ignoreElementNames`
 Section titled “ignoreElementNames”
 Type: `string[]`

 Added in:
 `@astrojs/mdx@3.0.0`

Previously known as `customComponentNames`.

An optional property of `optimize` to prevent the MDX optimizer from handling certain element names, like custom components passed to imported MDX content via the components prop .

You will need to exclude these components from optimization as the optimizer eagerly converts content into a static string, which will break custom components that needs to be dynamically rendered.

For example, the intended MDX output of the following is `&#x3C;Heading>...&#x3C;/Heading>` in place of every `"&#x3C;h1>...&#x3C;/h1>"`:

 ` --- import { Content, components } from ' ../content.mdx ' ; import Heading from ' ../Heading.astro ' ; ---
 &#x3C; Content components = { { ... components , h1: Heading } } /> ` ">
 To configure optimization for this using the `ignoreElementNames` property, specify an array of HTML element names that should be treated as custom components:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import mdx from ' @astrojs/mdx ' ;
 export default defineConfig ({ // ... integrations: [ mdx ({ optimize: { // Prevent the optimizer from handling `h1` elements ignoreElementNames: [ ' h1 ' ], }, }), ], }); `
 Note that if your MDX file configures custom components using `export const components = { ... }` , then you do not need to manually configure this option. The optimizer will automatically detect them.

## Examples
 Section titled “Examples”

- The Astro MDX starter template shows how to use MDX files in your Astro project.

## More integrations

### Front-end frameworks

 -

###

 @astrojs/ alpinejs

-

###

 @astrojs/ preact

-

###

 @astrojs/ react

-

###

 @astrojs/ solid⁠-⁠js

-

###

 @astrojs/ svelte

-

###

 @astrojs/ vue

### Adapters

 -

###

 @astrojs/ cloudflare

-

###

 @astrojs/ netlify

-

###

 @astrojs/ node

-

###

 @astrojs/ vercel

### Other integrations

 -

###

 @astrojs/ db

-

###

 @astrojs/ markdoc

-

###

 @astrojs/ mdx

-

###

 @astrojs/ partytown

-

###

 @astrojs/ sitemap

 Learn

 Contribute

 Community

 Sponsor

## Markdoc

#

 @astrojs/
 markdoc

 v1.0.6

 GitHub

 npm

 Changelog

 This Astro integration enables the usage of Markdoc to create components, pages, and content collection entries.

## Why Markdoc?
 Section titled “Why Markdoc?”
 Markdoc allows you to enhance your Markdown with Astro components . If you have existing content authored in Markdoc, this integration allows you to bring those files to your Astro project using content collections.

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

Run one of the following commands in a new terminal window.

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add markdoc `

 Terminal window
```
` pnpm astro add markdoc `
```

 Terminal window
```
` yarn astro add markdoc `
```

 If you run into any issues, feel free to report them to us on GitHub and try the manual installation steps below.

### Manual Install
 Section titled “Manual Install”
 First, install the `@astrojs/markdoc` package:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/markdoc `

 Terminal window
```
` pnpm add @astrojs/markdoc `
```

 Terminal window
```
` yarn add @astrojs/markdoc `
```

 Then, apply the integration to your `astro.config.*` file using the `integrations` property:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import markdoc from ' @astrojs/markdoc ' ; export default defineConfig ({ // ... integrations: [ markdoc () ], }); `

### VS Code Editor Integration
 Section titled “VS Code Editor Integration”
 If you are using VS Code, there is an official Markdoc language extension that includes syntax highlighting and autocomplete for configured tags. See the language server on GitHub for more information.

To set up the extension, create a `markdoc.config.json` file in the project root with following content:

 markdoc.config.json ` [ { "id" : " my-site " , "path" : " src/content " , "schema" : { "path" : " markdoc.config.mjs " , "type" : " esm " , "property" : " default " , "watch" : true } } ] `
 Set `markdoc.config.mjs` as your configuration file with the `schema` object, and define where your Markdoc files are stored using the `path` property. Since Markdoc is specific to content collections, you can use `src/content`.

## Usage
 Section titled “Usage”
 Markdoc files can only be used within content collections. Add entries to any content collection using the `.mdoc` extension:

 - Directory src/
 Directory content/
 Directory docs/
 why-markdoc.mdoc
- quick-start.mdoc

 Then, query and display your posts and collections :

 src/pages/why-markdoc.astro ` --- import { getEntry, render } from ' astro:content ' ;
 const entry = await getEntry ( ' docs ' , ' why-markdoc ' ); const { Content } = await render (entry); ---
 &#x3C;!--Access frontmatter properties with `data`--> &#x3C; h1 > { entry . data . title } &#x3C;/ h1 > &#x3C;!--Render Markdoc contents with the Content component--> &#x3C; Content /> ` ">

 See the Astro Content Collection docs for more information.

## Pass Markdoc variables
 Section titled “Pass Markdoc variables”
 You may need to pass variables to your content. This is useful when passing SSR parameters like A/B tests.

Variables can be passed as props via the `Content` component:

 src/pages/why-markdoc.astro ` --- import { getEntry, render } from ' astro:content ' ;
 const entry = await getEntry ( ' docs ' , ' why-markdoc ' ); const { Content } = await render (entry); ---
 &#x3C;!--Pass the `abTest` param as a variable--> &#x3C; Content abTestGroup = { Astro . params . abTestGroup } /> ` ">
 Now, `abTestGroup` is available as a variable in `docs/why-markdoc.mdoc`:

 src/content/docs/why-markdoc.mdoc ` {% if $abTestGroup === 'image-optimization-lover' %}
 Let me tell you about image optimization...
 {% /if %} `
 To make a variable global to all Markdoc files, you can use the `variables` attribute from your `markdoc.config.mjs|ts`:

 markdoc.config.mjs ` import { defineMarkdocConfig } from ' @astrojs/markdoc/config ' ;
 export default defineMarkdocConfig ({ variables: { environment: process . env . IS_PROD ? ' prod ' : ' dev ' , }, }); `

### Access frontmatter from your Markdoc content
 Section titled “Access frontmatter from your Markdoc content”
 To access frontmatter, you can pass the entry `data` property as a variable where you render your content:

 src/pages/why-markdoc.astro ` --- import { getEntry, render } from ' astro:content ' ;
 const entry = await getEntry ( ' docs ' , ' why-markdoc ' ); const { Content } = await render (entry); ---
 &#x3C; Content frontmatter = { entry . data } /> ` ">
 This can now be accessed as `$frontmatter` in your Markdoc.

## Render components
 Section titled “Render components”
 `@astrojs/markdoc` offers configuration options to use all of Markdoc’s features and connect UI components to your content.

### Use Astro components as Markdoc tags
 Section titled “Use Astro components as Markdoc tags”
 You can configure Markdoc tags that map to `.astro` components. You can add a new tag by creating a `markdoc.config.mjs|ts` file at the root of your project and configuring the `tag` attribute.

This example renders an `Aside` component, and allows a `type` prop to be passed as a string:

 markdoc.config.mjs ` import { defineMarkdocConfig, component } from ' @astrojs/markdoc/config ' ;
 export default defineMarkdocConfig ({ tags: { aside: { render: component ( ' ./src/components/Aside.astro ' ), attributes: { // Markdoc requires type defs for each attribute. // These should mirror the `Props` type of the component // you are rendering. // See Markdoc's documentation on defining attributes // https://markdoc.dev/docs/attributes#defining-attributes type: { type: String }, }, }, }, }); `
 This component can now be used in your Markdoc files with the `{% aside %}` tag. Children will be passed to your component’s default slot:

 ` # Welcome to Markdoc 👋
 {% aside type="tip" %}
 Use tags like this fancy "aside" to add some _ flair _ to your docs.
 {% /aside %} `

### Use client-side UI components
 Section titled “Use client-side UI components”
 Tags and nodes are restricted to `.astro` files. To embed client-side UI components in Markdoc, use a wrapper `.astro` component that renders a framework component with your desired `client:` directive.

This example wraps a React `Aside.tsx` component with a `ClientAside.astro` component:

 src/components/ClientAside.astro ` --- import Aside from ' ./Aside ' ; ---
 &#x3C; Aside { ... Astro . props } client:load /> ` This example shows a Markdoc partial for a footer to be used inside blog collection entries:

 src/content/blog/_footer.mdoc ` Social links:
 - [ Twitter / X ] ( https://twitter.com/astrodotbuild ) - [ Discord ] ( https://astro.build/chat ) - [ GitHub ] ( https://github.com/withastro/astro ) `
 Use the `{% partial /%}` tag with to render the footer at the bottom of a blog post entry. Apply the `file` attribute with the path to the file, using either a relative path or an import alias:

 src/content/blog/post.mdoc ` # My Blog Post
 {% partial file="./_footer.mdoc" /%} `

## Syntax highlighting
 Section titled “Syntax highlighting”
 `@astrojs/markdoc` provides Shiki and Prism extensions to highlight your code blocks.

### Shiki
 Section titled “Shiki”
 Apply the `shiki()` extension to your Markdoc config using the `extends` property. You can optionally pass a shiki configuration object:

 markdoc.config.mjs ` import { defineMarkdocConfig } from ' @astrojs/markdoc/config ' ; import shiki from ' @astrojs/markdoc/shiki ' ;
 export default defineMarkdocConfig ({ extends: [ shiki ({ // Choose from Shiki's built-in themes (or add your own) // Default: 'github-dark' // https://shiki.style/themes theme: ' dracula ' , // Enable word wrap to prevent horizontal scrolling // Default: false wrap: true , // Pass custom languages // Note: Shiki has countless langs built-in, including `.astro`! // https://shiki.style/languages langs: [], }), ], }); `

### Prism
 Section titled “Prism”
 Apply the `prism()` extension to your Markdoc config using the `extends` property.

 markdoc.config.mjs ` import { defineMarkdocConfig } from ' @astrojs/markdoc/config ' ; import prism from ' @astrojs/markdoc/prism ' ;
 export default defineMarkdocConfig ({ extends: [ prism ()], }); `

 To learn about configuring Prism stylesheets, see our syntax highlighting guide .

## Custom Markdoc nodes / elements
 Section titled “Custom Markdoc nodes / elements”
 You may want to render standard Markdown elements, such as paragraphs and bolded text, as Astro components. For this, you can configure a Markdoc node . If a given node receives attributes, they will be available as component props.

This example renders blockquotes with a custom `Quote.astro` component:

 markdoc.config.mjs ` import { defineMarkdocConfig, nodes, component } from ' @astrojs/markdoc/config ' ;
 export default defineMarkdocConfig ({ nodes: { blockquote: { ...nodes . blockquote , // Apply Markdoc's defaults for other options render: component ( ' ./src/components/Quote.astro ' ), }, }, }); `

 See the Markdoc nodes documentation to learn about all the built-in nodes and attributes.

### Custom headings
 Section titled “Custom headings”
 `@astrojs/markdoc` automatically adds anchor links to your headings, and generates a list of `headings` via the content collections API . To further customize how headings are rendered, you can apply an Astro component as a Markdoc node .

This example renders a `Heading.astro` component using the `render` property:

 markdoc.config.mjs ` import { defineMarkdocConfig, nodes, component } from ' @astrojs/markdoc/config ' ;
 export default defineMarkdocConfig ({ nodes: { heading: { ...nodes . heading , // Preserve default anchor link generation render: component ( ' ./src/components/Heading.astro ' ), }, }, }); `
 All Markdown headings will render the `Heading.astro` component and pass the following `attributes` as component props:

- `level: number` The heading level 1 - 6

- `id: string` An `id` generated from the heading’s text contents. This corresponds to the `slug` generated by the content `render()` function .

For example, the heading `### Level 3 heading!` will pass `level: 3` and `id: 'level-3-heading'` as component props.

### Custom image components
 Section titled “Custom image components”
 Astro’s `&#x3C;Image />` component cannot be used directly in Markdoc. However, you can configure an Astro component to override the default image node every time the native `![]()` image syntax is used, or as a custom Markdoc tag to allow you to specify additional image attributes.

#### Override Markdoc’s default image node
 Section titled “Override Markdoc’s default image node”
 To override the default image node, you can configure an `.astro` component to be rendered in place of a standard `&#x3C;img>`.

-
Build a custom `MarkdocImage.astro` component to pass the required `src` and `alt` properties from your image to the `&#x3C;Image />` component:

 src/components/MarkdocImage.astro ` --- import type { ImageMetadata } from " astro " ; import { Image } from " astro:assets " ; interface Props { src : ImageMetadata ; alt : string ; } const { src , alt } = Astro . props ; --- &#x3C; Image src = { src } alt = { alt } /> ` ">

-
 The `&#x3C;Image />` component requires a `width` and `height` for remote images which cannot be provided using the `![]()` syntax. To avoid errors when using remote images, update your component to render a standard HTML `&#x3C;img>` tag when a remote URL `src` is found:

 src/components/MarkdocImage.astro ` --- import type { ImageMetadata } from " astro " ; import { Image } from " astro:assets " ; interface Props { src : ImageMetadata | string ; alt : string ; } const { src , alt } = Astro . props ; --- &#x3C; Image src = { src } alt = { alt } /> { typeof src === ' string ' ? &#x3C; img src = { src } alt = { alt } /> : &#x3C; Image src = { src } alt = { alt } /> } ` { typeof src === &#x27;string&#x27; ? : }">

-
 Configure Markdoc to override the default image node and render `MarkdocImage.astro`:

 markdoc.config.mjs ` import { defineMarkdocConfig, nodes, component } from ' @astrojs/markdoc/config ' ;
 export default defineMarkdocConfig ({ nodes: { image: { ...nodes . image , // Apply Markdoc's defaults for other options render: component ( ' ./src/components/MarkdocImage.astro ' ), }, }, }); `

-
 The native image syntax in any `.mdoc` file will now use the `&#x3C;Image />` component to optimize your local images. Remote images may still be used, but will not be rendered by Astro’s `&#x3C;Image />` component.

 src/content/blog/post.mdoc ` &#x3C;!-- Optimized by &#x3C;Image /> --> ![ A picture of a cat ] ( /cat.jpg )
 &#x3C;!-- Unoptimized &#x3C;img> --> ![ A picture of a dog ] ( https://example.com/dog.jpg ) `

#### Create a custom Markdoc image tag
 Section titled “Create a custom Markdoc image tag”
 A Markdoc `image` tag allows you to set additional attributes on your image that are not possible with the `![]()` syntax. For example, custom image tags allow you to use Astro’s `&#x3C;Image />` component for remote images that require a `width` and `height`.

The following steps will create a custom Markdoc image tag to display a `&#x3C;figure>` element with a caption, using the Astro `&#x3C;Image />` component to optimize the image.

-
Create a `MarkdocFigure.astro` component to receive the necessary props and render an image with a caption:

 src/components/MarkdocFigure.astro ` --- import type { ImageMetadata } from " astro " ; import { Image } from " astro:assets " ;
 interface Props { src : ImageMetadata | string ; alt : string ; width : number ; height : number ; caption : string ; }
 const { src , alt , width , height , caption } = Astro . props ; --- &#x3C; figure > &#x3C; Image { src } { alt } { width } { height } /> { caption &#x26;&#x26; &#x3C; figcaption > { caption } &#x3C;/ figcaption > } &#x3C;/ figure > `   {caption &#x26;&#x26; {caption} } ">

-
 Configure your custom image tag to render your Astro component:

 markdoc.config.mjs ` import { component, defineMarkdocConfig, nodes } from ' @astrojs/markdoc/config ' ;
 export default defineMarkdocConfig ({ tags: { image: { attributes: { width: { type: String, }, height: { type: String, }, caption: { type: String, }, ... nodes . image . attributes }, render: component ( ' ./src/components/MarkdocFigure.astro ' ), }, }, }); `

-
 Use the `image` tag in Markdoc files to display a figure with caption, providing all the necessary attributes for your component:

 ` {% image src="./astro-logo.png" alt="Astro Logo" width="100" height="100" caption="a caption!" /%} `

## Advanced Markdoc configuration
 Section titled “Advanced Markdoc configuration”
 The `markdoc.config.mjs|ts` file accepts all Markdoc configuration options , including tags and functions .

You can pass these options from the default export in your `markdoc.config.mjs|ts` file:

 markdoc.config.mjs ` import { defineMarkdocConfig } from ' @astrojs/markdoc/config ' ;
 export default defineMarkdocConfig ({ functions: { getCountryEmoji: { transform ( parameters ) { const [ country ] = Object . values ( parameters ); const countryToEmojiMap = { japan: ' 🇯🇵 ' , spain: ' 🇪🇸 ' , france: ' 🇫🇷 ' , } ; return countryToEmojiMap [ country ] ?? ' 🏳 ' ; }, }, }, }); `
 Now, you can call this function from any Markdoc content entry:

 ` ¡Hola {% getCountryEmoji("spain") %}! `

 See the Markdoc documentation for more on using variables or functions in your content.

### Set the root HTML element
 Section titled “Set the root HTML element”
 Markdoc wraps documents with an `&#x3C;article>` tag by default. This can be changed from the `document` Markdoc node. This accepts an HTML element name or `null` if you prefer to remove the wrapper element:

 markdoc.config.mjs ` import { defineMarkdocConfig, nodes } from ' @astrojs/markdoc/config ' ;
 export default defineMarkdocConfig ({ nodes: { document: { ...nodes . document , // Apply defaults for other options render: null , // default 'article' }, }, }); `

## Integration config options
 Section titled “Integration config options”
 The Astro Markdoc integration handles configuring Markdoc options and capabilities that are not available through the `markdoc.config.js` file.

### `allowHTML`
 Section titled “allowHTML”
 Type: `boolean`
 Default: `false`

 Added in:
 `@astrojs/markdoc@0.4.4`

Enables writing HTML markup alongside Markdoc tags and nodes.

By default, Markdoc will not recognize HTML markup as semantic content.

To achieve a more Markdown-like experience, where HTML elements can be included alongside your content, set `allowHTML:true` as a `markdoc` integration option. This will enable HTML parsing in Markdoc markup.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import markdoc from ' @astrojs/markdoc ' ;
 export default defineConfig ({ // ... integrations: [ markdoc ({ allowHTML: true })], }); `

### `ignoreIndentation`
 Section titled “ignoreIndentation”
 Type: `boolean`
 Default: `false`

 Added in:
 `@astrojs/markdoc@0.7.0`

By default, any content that is indented by four spaces is treated as a code block. Unfortunately, this behavior makes it difficult to use arbitrary levels of indentation to improve the readability of documents with complex structure.

When using nested tags in Markdoc, it can be helpful to indent the content inside of tags so that the level of depth is clear. To support arbitrary indentation, we have to disable the indent-based code blocks and modify several other markdown-it parsing rules that account for indent-based code blocks. These changes can be applied by enabling the ignoreIndentation option.

 astro.config.mjs
```
` import { defineConfig } from ' astro/config ' ; import markdoc from ' @astrojs/markdoc ' ;
 export default defineConfig ({ // ... integrations: [ markdoc ({ ignoreIndentation: true })], }); `
```

```
` # Welcome to Markdoc with indented tags 👋
 # Note: Can use either spaces or tabs for indentation
 {% custom-tag %} {% custom-tag %} ### Tags can be indented for better readability
 {% another-custom-tag %} This is easier to follow when there is a lot of nesting {% /another-custom-tag %}
 {% /custom-tag %} {% /custom-tag %} `
```

## Examples
 Section titled “Examples”

- The Astro Markdoc starter template shows how to use Markdoc files in your Astro project.

## More integrations

### Front-end frameworks

 -

###

 @astrojs/ alpinejs

-

###

 @astrojs/ preact

-

###

 @astrojs/ react

-

###

 @astrojs/ solid⁠-⁠js

-

###

 @astrojs/ svelte

-

###

 @astrojs/ vue

### Adapters

 -

###

 @astrojs/ cloudflare

-

###

 @astrojs/ netlify

-

###

 @astrojs/ node

-

###

 @astrojs/ vercel

### Other integrations

 -

###

 @astrojs/ db

-

###

 @astrojs/ markdoc

-

###

 @astrojs/ mdx

-

###

 @astrojs/ partytown

-

###

 @astrojs/ sitemap

 Learn

 Contribute

 Community

 Sponsor

## Sitemap

#

 @astrojs/
 sitemap

 v3.7.3

 GitHub

 npm

 Changelog

 This Astro integration generates a sitemap based on your pages when you build your Astro project.

## Why Astro Sitemap
 Section titled “Why Astro Sitemap”
 A Sitemap is an XML file that outlines all of the pages, videos, and files on your site. Search engines like Google read this file to crawl your site more efficiently. See Google’s own advice on sitemaps to learn more.

A sitemap file is recommended for large multi-page sites. If you don’t use a sitemap, most search engines will still be able to list your site’s pages, but a sitemap is a great way to ensure that your site is as search engine friendly as possible.

With Astro Sitemap, you don’t have to worry about creating this XML file yourself: the Astro Sitemap integration will crawl your statically-generated routes and create the sitemap file, including dynamic routes like `[...slug]` or `src/pages/[lang]/[version]/info.astro` generated by `getStaticPaths()`.

This integration cannot generate sitemap entries for dynamic routes in SSR mode .

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

Run one of the following commands in a new terminal window.

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add sitemap `

 Terminal window
```
` pnpm astro add sitemap `
```

 Terminal window
```
` yarn astro add sitemap `
```

 If you run into any issues, feel free to report them to us on GitHub and try the manual installation steps below.

### Manual Install
 Section titled “Manual Install”
 First, install the `@astrojs/sitemap` package using your package manager.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/sitemap `

 Terminal window
```
` pnpm add @astrojs/sitemap `
```

 Terminal window
```
` yarn add @astrojs/sitemap `
```

 Then, apply the integration to your `astro.config.*` file using the `integrations` property:

 ` import { defineConfig } from ' astro/config ' ; import sitemap from ' @astrojs/sitemap ' ;
 export default defineConfig ({ // ... integrations: [ sitemap () ], }); `

## Usage
 Section titled “Usage”
 `@astrojs/sitemap` needs to know your site’s deployed URL to generate a sitemap.

Add your site’s URL as the `site` option in `astro.config.mjs`. This must begin with `http://` or `https://`.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap from ' @astrojs/sitemap ' ;
 export default defineConfig ({ site: ' https://example.com ' , integrations: [ sitemap ()], // ... }); `
 With the sitemap integration configured, `sitemap-index.xml` and `sitemap-0.xml` files will be added to your output directory when building your site.

`sitemap-index.xml` links to all the numbered sitemap files.
`sitemap-0.xml` lists the pages on your site.
For extremely large sites, there may also be additional numbered files like `sitemap-1.xml` and `sitemap-2.xml`.

 Example of generated files for a two-page website sitemap-index.xml ` &#x3C;? xml version = " 1.0 " encoding = " UTF-8 " ?> &#x3C; sitemapindex xmlns = " http://www.sitemaps.org/schemas/sitemap/0.9 " > &#x3C; sitemap > &#x3C; loc > https://example.com/sitemap-0.xml &#x3C;/ loc > &#x3C;/ sitemap > &#x3C;/ sitemapindex > `    https://example.com/sitemap-0.xml   "> sitemap-0.xml
```
` &#x3C;? xml version = " 1.0 " encoding = " UTF-8 " ?> &#x3C; urlset xmlns = " http://www.sitemaps.org/schemas/sitemap/0.9 " xmlns:news = " http://www.google.com/schemas/sitemap-news/0.9 " xmlns:xhtml = " http://www.w3.org/1999/xhtml " xmlns:image = " http://www.google.com/schemas/sitemap-image/1.1 " xmlns:video = " http://www.google.com/schemas/sitemap-video/1.1 " > &#x3C; url > &#x3C; loc > https://example.com/ &#x3C;/ loc > &#x3C;/ url > &#x3C; url > &#x3C; loc > https://example.com/second-page/ &#x3C;/ loc > &#x3C;/ url > &#x3C;/ urlset > `
```
    https://example.com/    https://example.com/second-page/   ">

### Sitemap discovery
 Section titled “Sitemap discovery”
 You can make it easier for crawlers to find your sitemap with links in your site’s `&#x3C;head>` and `robots.txt` file.

#### Sitemap link in `&#x3C;head>`
 Section titled “Sitemap link in &#x3C;head>”
 Add a `&#x3C;link rel="sitemap">` element to your site’s `&#x3C;head>` pointing to the sitemap index file:

 src/layouts/Layout.astro ` &#x3C; head > &#x3C; link rel = " sitemap " href = " /sitemap-index.xml " /> &#x3C;/ head > `  -  ">

#### Sitemap link in `robots.txt`
 Section titled “Sitemap link in robots.txt”
 If you have a `robots.txt` for your website, you can add the URL for the sitemap index to help crawlers:

 public/robots.txt ` User-agent: * Allow: /
 Sitemap: https://&#x3C;YOUR SITE>/sitemap-index.xml ` /sitemap-index.xml">
 If you want to reuse the `site` value from `astro.config.mjs`, you can also generate `robots.txt` dynamically.
Instead of using a static file in the `public/` directory, create a `src/pages/robots.txt.ts` file and add the following code:

 src/pages/robots.txt.ts ` import type { APIRoute } from ' astro ' ;
 const getRobotsTxt = ( sitemapURL : URL ) => ` \ User-agent: * Allow: /
 Sitemap: ${ sitemapURL . href } ` ;
 export const GET : APIRoute = ( { site } ) => { const sitemapURL = new URL ( ' sitemap-index.xml ' , site) ; return new Response ( getRobotsTxt (sitemapURL)) ; } ; ` &#x60;\User-agent: *Allow: /Sitemap: ${sitemapURL.href}&#x60;;export const GET: APIRoute = ({ site }) => { const sitemapURL = new URL(&#x27;sitemap-index.xml&#x27;, site); return new Response(getRobotsTxt(sitemapURL));};">

## Configuration
 Section titled “Configuration”
 To configure this integration, pass an object to the `sitemap()` function in `astro.config.mjs`.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap from ' @astrojs/sitemap ' ;
 export default defineConfig ({ integrations: [ sitemap ({ // configuration options }), ], }); `

### `filter()`
 Section titled “filter()”
 Type: `(page: string) => boolean`

All pages are included in your sitemap by default. By adding a custom `filter()` function, you can filter included pages by URL.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap from ' @astrojs/sitemap ' ;
 export default defineConfig ({ site: ' https://example.com ' , integrations: [ sitemap ({ filter : ( page ) => page !== ' https://example.com/secret-vip-lounge/ ' , }), ], }); ` page !== &#x27;https://example.com/secret-vip-lounge/&#x27;, }), ],});">
 The function will be called for every page on your site. The `page` function parameter is the full URL of the page currently under consideration, including your `site` domain. Return `true` to include the page in your sitemap, and `false` to leave it out.

To filter multiple pages, add arguments with target URLs.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap from ' @astrojs/sitemap ' ;
 export default defineConfig ({ site: ' https://example.com ' , integrations: [ sitemap ({ filter : ( page ) => page !== ' https://example.com/secret-vip-lounge-1/ ' &#x26;&#x26; page !== ' https://example.com/secret-vip-lounge-2/ ' &#x26;&#x26; page !== ' https://example.com/secret-vip-lounge-3/ ' &#x26;&#x26; page !== ' https://example.com/secret-vip-lounge-4/ ' , }), ], }); `  page !== &#x27;https://example.com/secret-vip-lounge-1/&#x27; &#x26;&#x26; page !== &#x27;https://example.com/secret-vip-lounge-2/&#x27; &#x26;&#x26; page !== &#x27;https://example.com/secret-vip-lounge-3/&#x27; &#x26;&#x26; page !== &#x27;https://example.com/secret-vip-lounge-4/&#x27;, }), ],});">

### `customPages`
 Section titled “customPages”
 Type: `string[]`

An array of externally-generated pages to be included in the generated sitemap file.

Use this option to include pages in your sitemap that are a part of your deployed site but are not created by Astro.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap from ' @astrojs/sitemap ' ;
 export default defineConfig ({ site: ' https://example.com ' , integrations: [ sitemap ({ customPages: [ ' https://example.com/external-page1 ' , ' https://example.com/external-page2 ' ], }), ], }); `

### `customSitemaps`
 Section titled “customSitemaps”
 Type: `string[]`
 Default: `[]`

 Added in:
 `@astrojs/sitemap@3.5.0`

An array of externally-generated sitemaps to be included in the `sitemap-index.xml` file along with the generated sitemap entries.

Use this option to include external sitemaps in the `sitemap-index.xml` file created by Astro for sections of your deployed site that have their own sitemaps not created by Astro. This is helpful when you host multiple services under the same domain.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap from ' @astrojs/sitemap ' ;
 export default defineConfig ({ site: ' https://example.com ' , integrations: [ sitemap ({ customSitemaps: [ ' https://example.com/blog/sitemap.xml ' , ' https://example.com/shop/sitemap.xml ' ], }), ], }); `

### `entryLimit`
 Section titled “entryLimit”
 Type: `number`
 Default: `45000`

The maximum number entries per sitemap file. The default value is 45000. A sitemap index and multiple sitemaps are created if you have more entries. See this explanation of splitting up a large sitemap .

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap from ' @astrojs/sitemap ' ;
 export default defineConfig ({ site: ' https://example.com ' , integrations: [ sitemap ({ entryLimit: 10000 , }), ], }); `

### `changefreq`, `lastmod`, and `priority`
 Section titled “changefreq, lastmod, and priority”
 Type: `{ changefreq?: ChangeFreq ; lastmod?: Date; priority?: number; }`

 Added in:
 `@astrojs/sitemap@0.2.0`

These options correspond to the `&#x3C;changefreq>`, `&#x3C;lastmod>`, and `&#x3C;priority>` tags in the Sitemap XML specification.

Note that `changefreq` and `priority` are ignored by Google.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap from ' @astrojs/sitemap ' ;
 export default defineConfig ({ site: ' https://example.com ' , integrations: [ sitemap ({ changefreq: ' weekly ' , priority: 0.7 , lastmod: new Date ( ' 2022-02-24 ' ), }), ], }); `

### `serialize()`
 Section titled “serialize()”
 Type: `(item: SitemapItem ) => SitemapItem | Promise<SitemapItem | undefined> | undefined`

Generates an editable representation of each sitemap entry before returning either a `SitemapItem` or `undefined` to remove it from the sitemap. This function can be asynchronous and is called for each sitemap entry just before writing to disk.

The following example filters a page from the sitemap and updates a specific entry to modify its `changefreq`, `lastmod`, and `priority` properties:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap, { ChangeFreqEnum } from ' @astrojs/sitemap ' ;
 export default defineConfig ({ site: ' https://example.com ' , integrations: [ sitemap ({ serialize ( item ) { if ( / exclude-from-sitemap / . test ( item . url )) { return undefined ; } if ( / your-special-page / . test ( item . url )) { item . changefreq = ChangeFreqEnum . DAILY ; item . lastmod = new Date () . toISOString (); item . priority = 0.9 ; } return item ; }, }), ], }); `

### `chunks`
 Section titled “chunks”
 Type: `Record<string, (item: SitemapItem ) => SitemapItem | undefined>`

 Added in:
 `@astrojs/sitemap@3.7.0`
 New

A map of functions that allows you to split your sitemap into multiple files based on custom logic. Each key in the object becomes the name of a separate sitemap file, and its corresponding function determines which URLs will be included in that chunk. This can be useful for instance if a specific section of your website changes very often and you’d like to specify a different change frequency for its entries.

Each chunk function receives a `SitemapItem` and for each item returns either:

 the modified `SitemapItem`, if the URL should be included in this chunk

- `undefined`, if the URL should not be included in this chunk

The example below shows how to split URLs into different sitemap files based on their path:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap, { ChangeFreqEnum } from ' @astrojs/sitemap ' ;
 export default defineConfig ({ site: ' https://example.com ' , integrations: [ sitemap ({ chunks: { ' blog ' : ( item ) => { if ( / blog / . test ( item . url )) { item . changefreq = ChangeFreqEnum . WEEKLY ; item . lastmod = new Date () . toISOString (); item . priority = 0.9 ; return item ; } }, ' glossary ' : ( item ) => { if ( / glossary / . test ( item . url )) { item . changefreq = ChangeFreqEnum . MONTHLY ; item . lastmod = new Date () . toISOString (); item . priority = 0.7 ; return item ; } } }, }), ], }); ` { if (/blog/.test(item.url)) { item.changefreq = ChangeFreqEnum.WEEKLY; item.lastmod = new Date().toISOString(); item.priority = 0.9; return item; } }, &#x27;glossary&#x27;: (item) => { if (/glossary/.test(item.url)) { item.changefreq = ChangeFreqEnum.MONTHLY; item.lastmod = new Date().toISOString(); item.priority = 0.7; return item; } } }, }), ],});">
 This configuration will generate the following files:

- `sitemap-blog-0.xml`

- `sitemap-glossary-0.xml`

URLs that don’t match any chunk will be placed in a default `sitemap-pages-0.xml` file.

### `i18n`
 Section titled “i18n”
 Type: `{ defaultLocale: string; locales: Record&#x3C;string, string>; }`

To localize a sitemap , pass an object to this `i18n` option.

This object has two required properties:

- `defaultLocale`: Its value must exist as one of `locales` keys.

- `locales`: key/value - pairs. The key is used to look for a locale part in a page path. The value is a language attribute , only English alphabet and hyphen allowed.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap from ' @astrojs/sitemap ' ;
 export default defineConfig ({ site: ' https://example.com ' , integrations: [ sitemap ({ i18n: { defaultLocale: ' en ' , // All urls that don't contain `es` or `fr` after `https://example.com/` will be treated as default locale, i.e. `en` locales: { en: ' en-US ' , // The `defaultLocale` value must present in `locales` keys es: ' es-ES ' , fr: ' fr-CA ' , }, }, }), ], }); `
 The resulting sitemap looks like this:

 sitemap-0.xml ` ... &#x3C; url > &#x3C; loc > https://example.com/ &#x3C;/ loc > &#x3C; xhtml:link rel = " alternate " hreflang = " en-US " href = " https://example.com/ " /> &#x3C; xhtml:link rel = " alternate " hreflang = " es-ES " href = " https://example.com/es/ " /> &#x3C; xhtml:link rel = " alternate " hreflang = " fr-CA " href = " https://example.com/fr/ " /> &#x3C;/ url > &#x3C; url > &#x3C; loc > https://example.com/es/ &#x3C;/ loc > &#x3C; xhtml:link rel = " alternate " hreflang = " en-US " href = " https://example.com/ " /> &#x3C; xhtml:link rel = " alternate " hreflang = " es-ES " href = " https://example.com/es/ " /> &#x3C; xhtml:link rel = " alternate " hreflang = " fr-CA " href = " https://example.com/fr/ " /> &#x3C;/ url > &#x3C; url > &#x3C; loc > https://example.com/fr/ &#x3C;/ loc > &#x3C; xhtml:link rel = " alternate " hreflang = " en-US " href = " https://example.com/ " /> &#x3C; xhtml:link rel = " alternate " hreflang = " es-ES " href = " https://example.com/es/ " /> &#x3C; xhtml:link rel = " alternate " hreflang = " fr-CA " href = " https://example.com/fr/ " /> &#x3C;/ url > &#x3C; url > &#x3C; loc > https://example.com/es/second-page/ &#x3C;/ loc > &#x3C; xhtml:link rel = " alternate " hreflang = " es-ES " href = " https://example.com/es/second-page/ " /> &#x3C; xhtml:link rel = " alternate " hreflang = " fr-CA " href = " https://example.com/fr/second-page/ " /> &#x3C; xhtml:link rel = " alternate " hreflang = " en-US " href = " https://example.com/second-page/ " /> &#x3C;/ url > ... `  https://example.com/       https://example.com/es/       https://example.com/fr/       https://example.com/es/second-page/     ...">

### `xslURL`
 Section titled “xslURL”
 Type: `string`

 Added in:
 `@astrojs/sitemap@3.2.0`

The URL of an XSL stylesheet to style and prettify your sitemap.

The value set can be either a path relative to your configured `site` URL for a local stylesheet, or can be an absolute URL link to an external stylesheet.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap from ' @astrojs/sitemap ' ;
 export default defineConfig ({ site: ' https://example.com ' , integrations: [ sitemap ({ xslURL: ' /sitemap.xsl ' }), ], }); `

### `filenameBase`
 Section titled “filenameBase”
 Type: `string`
 Default: `sitemap`

 Added in:
 `@astrojs/sitemap@3.4.0`

The name prefix string used when generating the sitemap XML files. The default value is `sitemap`.

This option may be useful when integrating an Astro site into a domain with preexisting sitemap files.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap from ' @astrojs/sitemap ' ;
 export default defineConfig ({ site: ' https://example.com ' , integrations: [ sitemap ({ filenameBase: ' astronomy-sitemap ' }), ], }); `
 The given configuration will generate sitemap files at `https://example.com/astronomy-sitemap-0.xml` and `https://example.com/astronomy-sitemap-index.xml`.

### `namespaces`
 Section titled “namespaces”
 Type: `{ news?: boolean; xhtml?: boolean; image?: boolean; video?: boolean; }`
 Default: `{ news: true, xhtml: true, image: true, video: true }`

 Added in:
 `@astrojs/sitemap@3.6.0`

An object of XML namespaces to exclude from the generated sitemap.

Excluding unused namespaces can help create more focused sitemaps that are faster for search engines to parse and use less bandwidth. For example, if your site doesn’t have news content, videos, or multiple languages, you can exclude those namespaces to reduce XML bloat.

By default, all configurable namespaces (`news`, `xhtml`, `image`, and `video`) are included in your generated sitemap XML. To exclude one or more of these namespaces from your sitemap generation, add a `namespaces` configuration object and set individual options to `false`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap from ' @astrojs/sitemap ' ;
 export default defineConfig ({ site: ' https://example.com ' , integrations: [ sitemap ({ namespaces: { news: false , xhtml: false , } }) ] }); `

## Astro Sitemap utilities reference
 Section titled “Astro Sitemap utilities reference”

```
` import { ChangeFreqEnum, } from " @astrojs/sitemap " ; `
```

### `ChangeFreqEnum`
 Section titled “ChangeFreqEnum”

 Added in:
 `@astrojs/sitemap@1.3.2`

A TypeScript enumeration where each key is the uppercase version of a valid value defined in the specification of `&#x3C;changefreq>` .

The following example uses `serialize()` to update the `changefreq` of the blog index:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap, { ChangeFreqEnum } from ' @astrojs/sitemap ' ;
 export default defineConfig ({ site: ' https://example.com ' , integrations: [ sitemap ({ serialize ( item ) { if ( / blog / . test ( item . url )) { item . changefreq = ChangeFreqEnum . DAILY ; }
 return item ; }, }), ], }); `

## Astro Sitemap types reference
 Section titled “Astro Sitemap types reference”

```
` import type { ChangeFreq, LinkItem, SitemapItem, SitemapOptions, } from " @astrojs/sitemap " ; `
```

### `ChangeFreq`
 Section titled “ChangeFreq”
 Type: `"daily" | "monthly" | "always" | "hourly" | "weekly" | "yearly" | "never"`

A union of valid values to specify the update frequency of an entry.

### `LinkItem`
 Section titled “LinkItem”
 Type: `{ lang: string; hreflang?: string; url: string; }`

Describes the URL of a page. This could be the default version of the document or one of its translations.

#### `LinkItem.lang`
 Section titled “LinkItem.lang”
 Type: `string`

Specifies the language code supported by this version of the page. When a value is set, you do not need to also set `hreflang` .

#### `LinkItem.hreflang`
 Section titled “LinkItem.hreflang”
 Type: `string`

Specifies the language code supported by this version of the page. When a value is set, you do not need to also set `lang` .

#### `LinkItem.url`
 Section titled “LinkItem.url”
 Type: `string`

Specifies the absolute URL of the page for the specified language.

### `SitemapItem`
 Section titled “SitemapItem”
 Type: `{ url: string; lastmod?: string | undefined; changefreq?: ChangeFreqEnum | undefined; priority?: number | undefined; links?: LinkItem[] | undefined; }`

Describes an entry in a sitemap. This contains its `url` and additional optional properties.

#### `SitemapItem.url`
 Section titled “SitemapItem.url”
 Type: `string`

Specifies the absolute page URL.

#### `SitemapItem.lastmod`
 Section titled “SitemapItem.lastmod”
 Type: `string | undefined`

Defines the ISO formatted date of last modification of the page as a string.

#### `SitemapItem.changefreq`
 Section titled “SitemapItem.changefreq”
 Type: ` ChangeFreqEnum | undefined`

Defines how frequently the page is likely to change.

#### `SitemapItem.priority`
 Section titled “SitemapItem.priority”
 Type: `number | undefined`

Defines the priority of this URL relative to other URLs on your site. The value should be a number in the range from `0.0` to `1.0`.

#### `SitemapItem.links`
 Section titled “SitemapItem.links”
 Type: ` LinkItem [] | undefined`

Defines a list of alternate pages, including the current page.

### `SitemapOptions`
 Section titled “SitemapOptions”
 Type: `object`

Describes the configuration options .

## Examples
 Section titled “Examples”

- The official Astro website uses Astro Sitemap to generate its sitemap .

- Browse projects with Astro Sitemap on GitHub for more examples!

## More integrations

### Front-end frameworks

 -

###

 @astrojs/ alpinejs

-

###

 @astrojs/ preact

-

###

 @astrojs/ react

-

###

 @astrojs/ solid⁠-⁠js

-

###

 @astrojs/ svelte

-

###

 @astrojs/ vue

### Adapters

 -

###

 @astrojs/ cloudflare

-

###

 @astrojs/ netlify

-

###

 @astrojs/ node

-

###

 @astrojs/ vercel

### Other integrations

 -

###

 @astrojs/ db

-

###

 @astrojs/ markdoc

-

###

 @astrojs/ mdx

-

###

 @astrojs/ partytown

-

###

 @astrojs/ sitemap

 Learn

 Contribute

 Community

 Sponsor

## Partytown

#

 @astrojs/
 partytown

 v2.1.7

 GitHub

 npm

 Changelog

 This Astro integration enables Partytown in your Astro project.

## Why Astro Partytown
 Section titled “Why Astro Partytown”
 Partytown is a lazy-loaded library to help relocate resource intensive scripts into a web worker , and off of the main thread .

If you’re using third-party scripts for things like analytics or ads, Partytown is a great way to make sure that they don’t slow down your site.

The Astro Partytown integration installs Partytown for you and makes sure it’s enabled on all of your pages.

## Installation
 Section titled “Installation”
 Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can install integrations manually instead.

Run one of the following commands in a new terminal window.

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npx astro add partytown `

 Terminal window
```
` pnpm astro add partytown `
```

 Terminal window
```
` yarn astro add partytown `
```

 If you run into any issues, feel free to report them to us on GitHub and try the manual installation steps below.

### Manual Install
 Section titled “Manual Install”
 First, install the `@astrojs/partytown` package:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/partytown `

 Terminal window
```
` pnpm add @astrojs/partytown `
```

 Terminal window
```
` yarn add @astrojs/partytown `
```

 Then, apply the integration to your `astro.config.*` file using the `integrations` property:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import partytown from ' @astrojs/partytown ' ;
 export default defineConfig ({ // ... integrations: [ partytown () ], }); `

## Usage
 Section titled “Usage”
 Partytown should be ready to go with zero config. If you have an existing 3rd party script on your site, try adding the `type="text/partytown"` attribute:

 ` &#x3C; script type = " text/partytown " src = " fancy-analytics.js " >&#x3C;/ script > `
 If you open the “Network” tab from your browser’s dev tools , you should see the `partytown` proxy intercepting this request.

## Configuration
 Section titled “Configuration”
 To configure this integration, pass a ‘config’ object to the `partytown()` function call in `astro.config.mjs`.

 astro.config.mjs ` export default defineConfig ({ // ... integrations: [ partytown ({ config: { // options go here }, }), ], }); `
 This mirrors the Partytown config object and all options can be set in `partytown.config`. Some common configuration options for Astro projects are described on this page.

### Enabling debug mode
 Section titled “Enabling debug mode”
 Partytown ships with a `debug` mode; enable or disable it by passing `true` or `false` to `config.debug`. If `debug` mode is enabled, it will output detailed logs to the browser console.

If this option isn’t set, `debug` mode will be on by default in dev or preview mode.

 astro.config.mjs ` export default defineConfig ({ // ... integrations: [ partytown ({ // Example: Disable debug mode. config: { debug: false }, }), ], }); `

### Forwarding variables
 Section titled “Forwarding variables”
 Third-party scripts typically add variables to the `window` object so that you can communicate with them throughout your site. But when a script is loaded in a web-worker, it doesn’t have access to that global `window` object.

To solve this, Partytown can “patch” variables to the global window object and forward them to the appropriate script.

You can specify which variables to forward with the `config.forward` option. Read more in Partytown’s documentation.

 astro.config.mjs ` export default defineConfig ({ // ... integrations: [ partytown ({ // Example: Add dataLayer.push as a forwarding-event. config: { forward: [ ' dataLayer.push ' ], }, }), ], }); `

### Proxying requests
 Section titled “Proxying requests”
 Some third-party scripts may require proxying through `config.resolveUrl()`, which runs inside the service worker. You can set this configuration option to check for a specific URL, and optionally return a proxied URL instead:

 astro.config.mjs ` export default defineConfig ({ // ... integrations: [ partytown ({ // Example: proxy Facebook's analytics script config: { resolveUrl : ( url ) => { const proxyMap = { " connect.facebook.net " : " my-proxy.com " } url . hostname = proxyMap [ url . hostname ] || url . hostname ; return url ; }, } }), ], }); ` { const proxyMap = { &#x22;connect.facebook.net&#x22;: &#x22;my-proxy.com&#x22; } url.hostname = proxyMap[url.hostname] || url.hostname; return url; }, } }), ],});">
 However since the `config` object is serialized when sent to the client, some limitations on functions passed to your configuration apply:

- Functions cannot reference anything outside of the function scope.

- Functions can only be written in JavaScript.

In some advanced use cases, you may need to pass data to this function while initializing Partytown. To do so, you can set `resolveUrl()` on `window.partytown` instead of the integration config:

 Head.astro
```
` --- const proxyMap = { " connect.facebook.net " : " my-proxy.com " } ; ---
 &#x3C; script is:inline set:html = { ` window.partytown = { resolveUrl: (url) => { const proxyMap = ${ JSON . stringify (proxyMap) } ; url.hostname = proxyMap[url.hostname] || url.hostname; return url; }, }; ` } /> `
```

 Contribute

 Community

 Sponsor