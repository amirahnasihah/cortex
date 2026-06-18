# Astro - Migration Guides


## Migrate To Astro

# Migrate an existing project to Astro

 Ready to convert your site to Astro? See one of our guides for migration tips.

## Migration Guides
 Section titled “Migration Guides”

 -

###

 Create React App

-

###

 Docusaurus

-

###

 Eleventy

-

###

 Gatsby

-

###

 GitBook

-

###

 Gridsome

-

###

 Hugo

-

###

 Jekyll

-

###

 Next.js

-

###

 NuxtJS

-

###

 Pelican

-

###

 SvelteKit

-

###

 VuePress

-

###

 WordPress

 Note that many of these pages are stubs : they’re collections of resources waiting for your contribution!

## Why migrate your site to Astro?
 Section titled “Why migrate your site to Astro?”
 Astro provides many benefits: performance, simplicity, and many of the features you want built right into the framework. When you do need to extend your site, Astro provides several official and 3rd-party community integrations .

Migrating may be less work than you think!

Depending on your existing project, you may be able to use your existing:

-
 UI framework components directly in Astro.

-
 CSS stylesheets or libraries including Tailwind.

-
 Markdown/MDX files , with a configurable Markdown processor that supports plugins.

-
 Content from a CMS through an integration or API.

## Which projects can I convert to Astro?
 Section titled “Which projects can I convert to Astro?”
 Many existing sites can be built with Astro . Astro is ideally suited for your existing content-based sites like blogs, landing pages, marketing sites and portfolios. Astro integrates with several popular headless CMSes, and allows you to connect eCommerce shop carts.

Astro allows you have a fully statically-generated website, a dynamic app with routes rendered on demand, or a combination of both with complete control over your project rendering , making it a great replacement for SSGs or for sites that need to fetch some page data on the fly.

## How will my project design change?
 Section titled “How will my project design change?”
 Depending on your existing project, you may need to think differently about:

-
Designing in Astro Islands to avoid sending unnecessary JavaScript to the browser.

-
Providing client-side interactivity with client-side `&#x3C;script>` tags or UI framework components .

-
Managing shared state with Nano Stores or local storage instead of app-wide hooks or wrappers.

 Recipes

 Contribute

 Community

 Sponsor

## V6

# Upgrade to Astro v6

 This guide will help you migrate from Astro v5 to Astro v6.

Need to upgrade an older project to v5 first? See our older migration guide .

Need to see the v5 docs? Visit this older version of the docs site (unmaintained v5.18.0 snapshot) .

## Upgrade Astro
 Section titled “Upgrade Astro”
 Update your project’s version of Astro to the latest version using your package manager:

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` # Upgrade Astro and official integrations together npx @astrojs/upgrade `

 Terminal window
```
` # Upgrade Astro and official integrations together pnpm dlx @astrojs/upgrade `
```

 Terminal window
```
` # Upgrade Astro and official integrations together yarn dlx @astrojs/upgrade `
```

 You can also upgrade your Astro integrations manually if needed, and you may also need to upgrade other dependencies in your project.

Astro v6.0 includes potentially breaking changes , as well as the removal and deprecation of some features.

If your project doesn’t work as expected after upgrading to v6.0, check this guide for an overview of all breaking changes and instructions on how to update your codebase.

See the Astro changelog for full release notes.

## Dependency Upgrades
 Section titled “Dependency Upgrades”
 Any major upgrades to Astro’s dependencies may cause breaking changes in your project.

### Node 22
 Section titled “Node 22”

 Implementation PR: feat!: drop node 18 and 20 (#14427)

 Node 18 reached its End of Life in March 2025 and Node 20 is scheduled to reach its End of Life in April 2026.

Astro v6.0 drops Node 18 and Node 20 support entirely so that all Astro users can take advantage of Node’s more modern features.

#### What should I do?
 Section titled “What should I do?”
 Check that both your development environment and your deployment environment are using Node `22.12.0` or higher .

Check your local version of Node using:

 Terminal window ` node -v `

-
 Check your deployment environment’s own documentation to verify that they support Node 22.

You can specify Node `22.12.0` for your Astro project either in a dashboard configuration setting or a `.nvmrc` file.

 .nvmrc ` 22.12.0 `

### Vite 7.0
 Section titled “Vite 7.0”

 Implementation PR: feat: update vite (#14445)

 Astro v6.0 upgrades to Vite v7.0 as the development server and production bundler.

#### What should I do?
 Section titled “What should I do?”
 If you are using Vite-specific plugins, configuration, or APIs, check the Vite migration guide for their breaking changes and upgrade your project as needed.

Using Astro’s `getViteConfig()` helper requires at least Vitest v3.2 or v4.1 beta 5.

### Vite Environment API
 Section titled “Vite Environment API”

 Implementation PR: feat: integrate vite environments (#14306)

 Astro v6.0 introduces significant changes to how Astro manages different runtime environments (client, server, and prerender) after an internal refactor to use Vite’s new Environments API .

#### What should I do?
 Section titled “What should I do?”
 Integration and adapter maintainers should pay special attention to changes affecting these parts of the Integration API and Adapter API (full details included below with other breaking changes to these APIs):

- Rollup output file name config path

- integration hooks and HMR access patterns

- `SSRManifest` structure

- generating routes with `RouteData`

- routes with percent-encoded percent signs (e.g. `%25`)

- `astro:ssr-manifest` virtual module

- `NodeApp` from `astro/app/node`

- `loadManifest()` and `loadApp()` from `astro/app/node`

- `createExports()` and `start()`

### Zod 4
 Section titled “Zod 4”
 Astro v6.0 upgrades to Zod 4, a major dependency update that may require changes to custom Zod schemas in your project.

#### What should I do?
 Section titled “What should I do?”
 If you have custom Zod schemas in your `content.config.ts` or other configuration files, you’ll need to update them for Zod 4. Refer to the Zod migration guide for detailed changes in the Zod API.

Notably, many `string()` formats have been deprecated (e.g. `z.string().email()`, `z.string.url()`), and their APIs have been moved to the top-level `z` namespace. You may need to update how you validate form input for your Astro Actions:

 src/actions/index.ts ` email: z . string () . email (), email: z . email (), `
 Additionally, Zod has made some changes to handling error messages and has dropped support for a custom `errorsMap` which was useful to redefine or translate your error messages. You may need to update any custom error messages:

 src/actions/index.ts ` z . string () . min ( 5 , { message: " Too short. " }); z . string () . min ( 5 , { error: " Too short. " }); `
 Also, if you use `.default()` with transforms , you may need to update your schemas. In Zod 4, default values must match the output type (after transforms), not the input type. The default value short-circuits parsing when the input is `undefined`:

 src/content.config.ts ` import { z } from ' astro/zod ' ;
 const blog = defineCollection ( { schema: z . object ( { // Zod 3: default matched input type (string) views: z . string () . transform (Number) . default ( " 0 " ) , // Zod 4: default must match output type (number) views: z . string () . transform (Number) . default ( 0 ) , } ) } ); `
 For the old behavior where defaults are parsed, use the new `.prefault()` method.

These are only some of the many changes upgrading from Zod 3 to Zod 4. If you encounter any issues with your Zod schemas after upgrading to Astro 6, please consult the Zod 4 changelog for complete upgrade guidance.

Additionally, a community codemod , which can potentially automate some of these changes when migrating from Zod 3 to Zod 4, is also available.

You can ensure you’re the same version of Zod that Astro uses internally by importing Zod from `astro/zod` .

 ` import { z } from ' astro/zod ' ; `

 See more about the `astro/zod` module .

### Shiki 4.0
 Section titled “Shiki 4.0”

 Implementation PR: chore(deps): update shiki to v4 (#15726)

 Astro v6.0 upgrades to Shiki v4.0 for syntax highlighting.

#### What should I do?
 Section titled “What should I do?”
 If you are using Shiki-specific APIs, check the Shiki migration guide for their breaking changes and upgrade your project as needed.

### Official Astro integrations
 Section titled “Official Astro integrations”
 All of Astro’s official server adapters have also updated to a new major version to accompany the upgrade to Vite v7.0 with Vite’s Environment API as the development server and production bundler.

In particular, Astro’s Cloudflare adapter has undergone significant changes, and breaking changes to your existing Cloudflare setup are expected.

 See the Cloudflare adapter upgrade instructions for detailed migration guidance.

#### What should I do?
 Section titled “What should I do?”
 If you are using an Astro adapter for on-demand rendering or other platform-specific features, please check your specific adapter’s changelog for upgrade guidance:

- `@astrojs/cloudflare` CHANGELOG

- `@astrojs/netlify` CHANGELOG

- `@astrojs/node` CHANGELOG

- `@astrojs/vercel` CHANGELOG

## Legacy
 Section titled “Legacy”
 The following features are now considered legacy features. They should function normally but are no longer recommended and are in maintenance mode. They will see no future improvements and documentation will not be updated. These features will eventually be deprecated, and then removed entirely.

### Legacy: content collections backwards compatibility
 Section titled “Legacy: content collections backwards compatibility”
 In Astro 5.x, projects could delay upgrading to the new Content Layer API introduced for content collections because of some existing automatic backwards compatibility that was not previously behind a flag. This meant that it was possible to upgrade from Astro 4 to Astro 5 without updating your content collections, even if you had not enabled the `legacy.collections` flag. Projects would continue to build, and no errors or warnings would be displayed.

Astro v6.0 removes this automatic legacy content collections support, along with the `legacy.collections` flag . All content collections must now use the Content Layer API introduced in Astro v5.0 that powers all content collections.

#### What should I do?
 Section titled “What should I do?”
 If you experience content collections errors after updating to v6, check your project for any removed legacy features that may need updating to the Content Layer API.

 See the Astro v5 upgrade guide for detailed instructions on upgrading legacy collections to the new Content Layer API.

 If you are unable to update immediately, you can enable the `legacy.collectionsBackwardsCompat` flag as a temporary migration helper:

 astro.config.mjs ` export default defineConfig ({ legacy: { collectionsBackwardsCompat: true , }, }); `
 This flag preserves some legacy v4 content collections features:

- Supports the legacy configuration file `src/content/config.ts`

- Supports `type: 'content'` and `type: 'data'` without loaders

- Preserves legacy entry API: `entry.slug` and `entry.render()`

- Uses path-based entry IDs instead of slug-based IDs

 This is a temporary migration helper. Migrate your collections to the Content Layer API as soon as possible, then disable this flag.

## Deprecated
 Section titled “Deprecated”
 The following deprecated features are no longer supported and are no longer documented. Please update your project accordingly.

Some deprecated features may temporarily continue to function until they are completely removed. Others may silently have no effect, or throw an error prompting you to update your code.

### Deprecated: `Astro` in `getStaticPaths()`
 Section titled “Deprecated: Astro in getStaticPaths()”

 Implementation PR: feat: deprecate Astro in getStaticPaths (#14432)

 In Astro 5.x, it was possible to access an `Astro` object inside `getStaticPaths()`. However, despite being typed the same as the `Astro` object accessible in the frontmatter, this object only had `site` and `generator` properties. This could lead to confusion about which `Astro` object properties were available inside `getStaticPaths()`.

Astro 6.0 deprecates this object for `getStaticPaths()` to avoid confusion and improves error handling when attempting to access `Astro` values that are unavailable. Using `Astro.site` or `Astro.generator` within `getStaticPaths()` will now log a deprecation warning, and accessing any other property will throw a specific error with a helpful message. In a future major version, this object will be removed entirely, and accessing `Astro.site` or `Astro.generator` will also throw an error.

#### What should I do?
 Section titled “What should I do?”
 Update your `getStaticPaths()` function if you were attempting to access any `Astro` properties inside its scope. Remove `Astro.generator` entirely, and replace all occurrences of `Astro.site` with `import.meta.env.SITE`:

 src/pages/blog/[slug].astro ` --- import { getPages } from " ../../../utils/data " ;
 export async function getStaticPaths () { console . log (Astro . generator ); return getPages (Astro . site ); return getPages ( import. meta . env . SITE ); } --- `

 Read more about built-in environment variables such as `import.meta.env.SITE` that are accessible when using `getStaticPaths()` to dynamically generate static routes .

### Deprecated: `import.meta.env.ASSETS_PREFIX`
 Section titled “Deprecated: import.meta.env.ASSETS_PREFIX”

 Implementation PR: feat: deprecate import.meta.env.ASSETS_PREFIX (#14461)

 In Astro 5.x, it was possible to access `build.assetsPrefix` in your Astro config via the built-in environment variable `import.meta.env.ASSETS_PREFIX`. However, Astro v5.7.0 introduced the `astro:config` virtual module to expose a non-exhaustive, serializable, type-safe version of the Astro configuration which included access to `build.assetsPrefix` directly. This became the preferred way to access the prefix for Astro-generated asset links when set, although the environment variable still existed.

Astro 6.0 deprecates this variable in favor of `build.assetsPrefix` from the `astro:config/server` module.

#### What should I do?
 Section titled “What should I do?”
 Replace any occurrences of `import.meta.env.ASSETS_PREFIX` with the `build.assetsPrefix` import from `astro:config/server`. This is a drop-in replacement to provide the existing value, and no other changes to your code should be necessary:

 ` import { someLogic } from " ./utils " import { build } from " astro:config/server "
 someLogic ( import. meta . env . ASSETS_PREFIX ) someLogic (build . assetsPrefix ) `

 Read more about the `astro:config` virtual module .

### Deprecated: `astro:schema` and `z` from `astro:content`
 Section titled “Deprecated: astro:schema and z from astro:content”

 Implementation PR: feat!: consolidate zod export (#14923)

 In Astro 5.x, `astro:schema` was introduced as an alias of `astro/zod`. `z` was also exported from `astro:content` for convenience. However this occasionally created confusion for users who were unsure about where they should be importing from.

Astro 6.0 deprecates `astro:schema` and `z` from `astro:content` in favor of `astro/zod`.

#### What should I do?
 Section titled “What should I do?”
 Replace any occurrences of `astro:schema` with `astro/zod`:

 ` import { z } from " astro:schema " import { z } from " astro/zod " `
 Remove `z` from your `astro:content` imports and import `z` separately from `astro/zod` instead:

 src/content.config.ts ` import { defineCollection, z } from " astro:content " import { defineCollection } from " astro:content " import { z } from " astro/zod " `

 See more about defining collection schemas with Zod .

### Deprecated: exposed `astro:transitions` internals
 Section titled “Deprecated: exposed astro:transitions internals”

 Implementation PR: feat!: deprecate transitions exports (#14989)

 In Astro 5.x, some internals were exported from `astro:transitions` and `astro:transitions/client` that were not meant to be exposed for public use.

Astro 6.0 removes the following functions and types as exports from the `astro:transitions` and `astro:transitions/client` virtual modules. These can no longer be imported in your project files:

- `createAnimationScope()`

- `isTransitionBeforePreparationEvent()`

- `isTransitionBeforeSwapEvent()`

- `TRANSITION_BEFORE_PREPARATION`

- `TRANSITION_AFTER_PREPARATION`

- `TRANSITION_BEFORE_SWAP`

- `TRANSITION_AFTER_SWAP`

- `TRANSITION_PAGE_LOAD`

#### What should I do?
 Section titled “What should I do?”
 Remove any occurrences of `createAnimationScope()`:

 ` import { createAnimationScope } from ' astro:transitions ' ; `
 Update any occurrences of the other deprecated exports:

 ` import { isTransitionBeforePreparationEvent, TRANSITION_AFTER_SWAP, } from ' astro:transitions/client ' ;
 console . log ( isTransitionBeforePreparationEvent (event)); console . log (event . type === ' astro:before-preparation ' );
 console . log ( TRANSITION_AFTER_SWAP ); console . log ( ' astro:after-swap ' ); `

 Learn more about all utilities available in the View Transitions Router API Reference .

### Deprecated: session driver string signature
 Section titled “Deprecated: session driver string signature”

 Implementation PR: feat(sessions): drivers (#15006)

 In Astro 5.x, any unstorage provider name or a custom entrypoint could be provided to define a session driver, and options were also provided directly to the `session` configuration. However, we felt that this API was limited and inconsistent with other parts of the Astro config.

Astro 6.0 deprecates the driver string signature and options in favor of a new object shape.

#### What should I do?
 Section titled “What should I do?”
 Update your session config to use the newly exported `sessionDrivers`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' import { defineConfig, sessionDrivers } from ' astro/config '
 export default defineConfig ({ session: { driver: ' redis ' , options: { url: process . env . REDIS_URL }, driver: sessionDrivers . redis ({ url: process . env . REDIS_URL }), cookie: { secure: true }, ttl: 3600 } }) `

 Learn more about available session drivers .

### Deprecated: `NodeApp` from `astro/app/node` (Adapter API)
 Section titled “Deprecated: NodeApp from astro/app/node (Adapter API)”

 Implementation PR: feat: deprecate NodeApp (#15535)

 In Astro 5.x, adapters could implement their server entrypoint using `App` for standard web requests/responses, or `NodeApp` for node requests/responses.

Astro 6.0 deprecates `NodeApp` in favor of `createApp()` and new utilities: `createRequest()` and `writeResponse()`. This allows a more consistent API while preserving the same features as before. It also deprecates the `NodeAppHeadersJson` type.

#### What should I do?
 Section titled “What should I do?”
 If you have built an adapter, update any usage of `NodeApp` with `createApp()`:

 my-adapter/server.js ` import { NodeApp } from ' astro/app/node ' ;
 export function createExports ( manifest ) { const app = new NodeApp ( manifest );
 const handler = async ( req , res ) => { const response = await app . render ( req ) ; await NodeApp . writeResponse ( response , res ) ; } ;
 return { handler }; } import { createApp } from ' astro/app/entrypoint ' ; import { createRequest, writeResponse } from ' astro/app/node ' ;
 const app = createApp ();
 export const handler = async ( req , res ) => { const request = createRequest ( req ) ; const response = await app . render ( request ) ; await writeResponse ( response , res ) ; } ` { const response = await app.render(req); await NodeApp.writeResponse(response, res); }; return { handler };}import { createApp } from &#x27;astro/app/entrypoint&#x27;;import { createRequest, writeResponse } from &#x27;astro/app/node&#x27;;const app = createApp();export const handler = async (req, res) => { const request = createRequest(req); const response = await app.render(request); await writeResponse(response, res);}">

 Learn more about the `astro/app/node` module .

### Deprecated: `loadManifest()` and `loadApp()` from `astro/app/node` (Adapter API)
 Section titled “Deprecated: loadManifest() and loadApp() from astro/app/node (Adapter API)”

 Implementation PR: feat: deprecate NodeApp (#15535)

 In Astro 5.x, the `astro/app/node` exposed `loadManifest()` and `loadApp()` utilities to allow loading the SSR manifest or a `NodeApp` instance from a `URL` instance. However, these were not documented and are no longer recommended usage with the v6 Adapter API.

Astro 6.0 deprecates both functions.

#### What should I do?
 Section titled “What should I do?”
 If you have built an adapter, remove `loadManifest()` and replace `loadApp()` by `createApp()`:

 my-adapter/server.js ` import { loadManifest, loadApp, NodeApp } from ' astro/app/node ' ;
 const manifest = await loadManifest ( new URL ( import. meta . url )); const app1 = new NodeApp ( loadManifest ); const app2 = await loadApp ( new URL ( import. meta . url )); import { createApp } from ' astro/app/entrypoint ' ;
 const app = createApp (); `

 Learn more about the `astro/app/entrypoint` module .

### Deprecated: `createExports()` and `start()` (Adapter API)
 Section titled “Deprecated: createExports() and start() (Adapter API)”

 Implementation PR: feat: improve naming of new adapter api (#15461)

 In Astro 5.x, adapters had to provide the exports required by the host in their server entrypoint using a `createExports()` function before passing them to `setAdapter()` as an `exports` list.

Astro 6.0 introduces a simpler yet more powerful way of making server entrypoints. This relies on passing a new option `entrypointResolution: "auto"` to `setAdapter()`.

However, for backwards compatibility with existing adapters, the default value of `entrypointResolution` (`"explicit"`) mimics Astro 5.x API behavior. This means that your adapters can continue to function until you can fully migrate your adapter to the `auto` value, as shown below.

Note that `entrypointResolution: "explicit"` (maintaining v5 API behavior) is considered deprecated usage, but the option has been provided so that no immediate change to your adapter is required and to allow adapter authors time to update. This option will be removed in a future major version in favor of all adapters using `entrypointResolution: "auto"`.

#### What should I do?
 Section titled “What should I do?”
 If you are an adapter author with a public repository and include the `astro-adapter` keyword in your `package.json` , the Astro core team will attempt to make a PR to your repository directly to help you migrate your code if you have not yet followed the steps below.

If you are seeing warnings because you are using a community adapter that is not yet updated, please reach out to the adapter author directly to let them know. It is ultimately their responsibility to update their adapters. You can also let the Astro core team know in the `#integrations` channel of our Discord and we will attempt to help the adapter author upgrade.

If you have built an adapter, follow these steps to remove the legacy v5 behavior:

-
Update your `setAdapter()`: set `entrypointResolution: "auto"`, remove `exports` and `args`

 my-adapter.mjs ` setAdapter ({ // ... entrypointResolution: ' auto ' , exports: [ ' handler ' ], args: { assets: config . build . assets } }) `

-
 Update your server entrypoint to provide any required exports without `createExports()`:

 my-adapter/server.js ` import { App } from ' astro/app ' ;
 export function createExports ( manifest ) { const app = new App ( manifest );
 const handler = ( event , context ) => { // ... } ;
 return { handler }; } import { createApp } from ' astro/app/entrypoint ' ;
 const app = createApp ();
 export const handler = ( event , context ) => { // ... } ` { // ... }; return { handler };}import { createApp } from &#x27;astro/app/entrypoint&#x27;;const app = createApp();export const handler = (event, context) => { // ...}">

-
 If your adapter provides a `start()` function, update your server entrypoint to call the code directly:

 my-adapter/server.js ` import { App } from ' astro/app ' ;
 export function start ( manifest ) { const app = new App ( manifest );
 addEventListener ( ' fetch ' , event => { // ... }); } import { createApp } from ' astro/app/entrypoint ' ;
 const app = createApp ();
 addEventListener ( ' fetch ' , event => { // ... }); ` { // ... });}import { createApp } from &#x27;astro/app/entrypoint&#x27;;const app = createApp();addEventListener(&#x27;fetch&#x27;, event => { // ...});">

-
 If you were relying on `args`, create a virtual module to pass the build time configuration and import them from the virtual module instead:

 my-adapter/server.js ` export function createExports ( manifest , { assets } ) { // ... } import { assets } from ' virtual:@example/my-adapter:config ' ; `

 Learn more about the Adapter API .

## Removed
 Section titled “Removed”
 The following features have now been entirely removed from the code base and can no longer be used. Some of these features may have continued to work in your project even after deprecation. Others may have silently had no effect.

Projects now containing these removed features will be unable to build, and there will no longer be any supporting documentation prompting you to remove these features.

### Removed: legacy content collections
 Section titled “Removed: legacy content collections”

 Implementation PR: fix: remove legacy content collections (#14407)

 In Astro 5.x, it was still possible to use the original Content Collections API first introduced in Astro v2.0 , either through a `legacy` configuration flag or via built-in backwards compatibility . These methods allowed you to upgrade to Astro v5 even if you were not yet ready or able to update your existing content collections to those powered by the new Content Layer API.

Astro v6.0 removes this previously deprecated Content Collections API support entirely, including the `legacy.collections` flag and some existing backwards compatibility that was not previously behind a flag . All content collections must now use the Content Layer API introduced in Astro v5.0 that powers all content collections. No backwards compatibility support is available.

#### What should I do?
 Section titled “What should I do?”
 If you had previously enabled the legacy flag, you must remove it.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ legacy: { collections: true , } }) `
 Additionally, if you did not upgrade your collections for Astro v5.0, ensure that your content collections are fully updated for the new API.

Astro v5.x included some automatic backwards compatibility to allow content collections to continue to work even if they had not been updated to use the new API. Therefore, your v5 collections may contain one or more legacy features that need updating to the newer API for v6, even if your project was previously error-free.

If you have content collections errors or warnings after upgrading to v6, use the following list to help you identify and upgrade any legacy features that may exist in your code.

 If you have… Section titled “If you have…”
 no content collections configuration file
Create `src/content.config.ts` and define your collections in it.

 a configuration file located at `src/content/config.ts` / ( `LegacyContentConfigError` )
Rename and move this file to `src/content.config.ts`

 a collection that does not define a `loader` / ( `ContentCollectionMissingALoaderError` ) Import Astro’s built-in `glob()` loader and define the `pattern` and `base` for your collection entries:
 src/content.config.ts ` import { defineCollection } from ' astro:content ' ; import { z } from ' astro/zod ' ; import { glob } from ' astro/loaders ' ;
 const blog = defineCollection ( { loader: glob ( { pattern: ' **/[^_]*.{md,mdx} ' , base: " ./src/data/blog " } ) , schema: z . object ( { title: z . string () , description: z . string () , pubDate: z . coerce . date () , updatedDate: z . coerce . date () . optional () , } ) , } ); `
 a collection that defines a collection type (`type: 'content'` or `type: 'data'`) / ( `ContentCollectionInvalidTypeError` )
There are no longer different types of collections. This must be deleted from your collection definition.
 src/content.config.ts ` import { defineCollection } from ' astro:content ' ; import { z } from ' astro/zod ' ; import { glob } from ' astro/loaders ' ;
 const blog = defineCollection ( { // For content layer you no longer define a `type` type: ' content ' , loader: glob ( { pattern: ' **/[^_]*.{md,mdx} ' , base: " ./src/data/blog " } ) , schema: z . object ( { title: z . string () , description: z . string () , pubDate: z . coerce . date () , updatedDate: z . coerce . date () . optional () , } ) , } ); `
 legacy collection querying methods `getDataEntryById()` and `getEntryBySlug()` / ( `GetEntryDeprecationError` )
Replace both methods with `getEntry()` .

 legacy collection querying and rendering methods that depend on a `slug` property / ( `ContentSchemaContainsSlugError` )
Previously, the `id` was based on the filename, and there was a `slug` property that could be used in a URL. Now the `CollectionEntry` `id` is a slug. If you need access to the filename (previously available as the `id`), use the `filePath` property. Replace instances of `slug` with `id`:
 src/pages/[slug].astro ` --- export async function getStaticPaths () { const posts = await getCollection ( ' blog ' ); return posts . map ( ( post ) => ({ params: { slug: post . slug } , params: { slug: post . id } , props: post , })); } --- ` ({ params: { slug: post.slug }, params: { slug: post.id }, props: post, }));}---">
 content rendered using `entry.render()`
Collection entries no longer have a `render()` method. Instead, import the `render()` function from `astro:content` and use `render(entry)`:
 src/pages/index.astro ` --- import { getEntry , render } from ' astro:content ' ;
 const post = await getEntry ( ' pages ' , ' homepage ' );
 const { Content , headings } = await post . render (); const { Content , headings } = await render (post); --- &#x3C; Content /> ` ">

 See the Astro v5 upgrade guide for previous guidance about backwards compatibility of legacy collections in Astro v5 and full step-by-step instructions for upgrading legacy collections to the new Content Layer API.

### Removed: `&#x3C;ViewTransitions />` component
 Section titled “Removed: &#x3C;ViewTransitions /> component”

 Implementation PR: Remove deprecated ViewTransitions component (#14400)

 In Astro 5.0, the `&#x3C;ViewTransitions />` component was renamed to `&#x3C;ClientRouter />` to clarify the role of the component. The new name makes it more clear that the features you get from Astro’s `&#x3C;ClientRouter />` routing component are slightly different from the native CSS-based MPA router. However, a deprecated version of the `&#x3C;ViewTransitions />` component still existed and may have functioned in Astro 5.x.

Astro 6.0 removes the `&#x3C;ViewTransitions />` component entirely and it can no longer be used in your project. Update to the `&#x3C;ClientRouter />` component to continue to use these features.

#### What should I do?
 Section titled “What should I do?”
 Replace all occurrences of the `ViewTransitions` import and component with `ClientRouter`:

 src/layouts/MyLayout.astro ` import { ViewTransitions } from 'astro:transitions'; import { ClientRouter } from 'astro:transitions';
 &#x3C; html > &#x3C; head > ... &#x3C; ViewTransitions /> &#x3C; ClientRouter /> &#x3C;/ head > &#x3C;/ html > `   ...    ">

 Read more about view transitions and client-side routing in Astro .

### Removed: `emitESMImage()`
 Section titled “Removed: emitESMImage()”

 Implementation PR: feat!: remove emitESMImage() (#14426)

 In Astro 5.6.2, the `emitESMImage()` function was deprecated in favor of `emitImageMetadata()`, which removes two deprecated arguments that were not meant to be exposed for public use: `_watchMode` and `experimentalSvgEnabled`.

Astro 6.0 removes `emitESMImage()` entirely. Update to `emitImageMetadata()` to keep your current behavior.

#### What should I do?
 Section titled “What should I do?”
 Replace all occurrences of the `emitESMImage()` with `emitImageMetadata()` and remove unused arguments:

 ` import { emitESMImage } from ' astro/assets/utils ' ; import { emitImageMetadata } from ' astro/assets/utils ' ;
 const imageId = ' /images/photo.jpg ' ; const result = await emitESMImage (imageId , false , false ); const result = await emitImageMetadata (imageId); `

 Read more about `emitImageMetadata()` .

### Removed: `Astro.glob()`
 Section titled “Removed: Astro.glob()”

 Implementation PR: feat!: remove Astro.glob (#14421)

 In Astro 5.0, `Astro.glob()` was deprecated in favor of using `getCollection()` to query your collections, and `import.meta.glob()` to query other source files in your project.

Astro 6.0 removes `Astro.glob()` entirely. Update to `import.meta.glob()` to keep your current behavior.

#### What should I do?
 Section titled “What should I do?”
 Replace all use of `Astro.glob()` with `import.meta.glob()`. Note that `import.meta.glob()` no longer returns a `Promise`, so you may have to update your code accordingly. You should not require any updates to your glob patterns .

 src/pages/blog.astro ` --- const posts = await Astro . glob ( ' ./posts/*.md ' ); const posts = Object . values ( import. meta . glob ( ' ./posts/*.md ' , { eager: true } )); ---
 { posts . map ( ( post ) => &#x3C; li >&#x3C; a href = { post . url } > { post . frontmatter . title } &#x3C;/ a >&#x3C;/ li > ) } ` - {post.frontmatter.title}
)}">
 Where appropriate, consider using content collections to organize your content, which has its own newer, more performant querying functions.

You may also wish to consider using glob packages from NPM, such as `fast-glob` .

 Learn more about importing files with `import.meta.glob` .

### Removed: exposed `astro:actions` internals
 Section titled “Removed: exposed astro:actions internals”

 Implementation PR: refactor: cleanup public actions API (#14844)

 In Astro 5.x, some internals were exported from `astro:actions` that were not meant to be exposed for public use.

Astro 6.0 removes the following functions, classes and types as exports from the `astro:actions` virtual module. These can no longer be imported in your project files:

- `ACTION_ERROR_CODES`

- `ActionInputError`

- `appendForwardSlash`

- `astroCalledServerError`

- `callSafely`

- `deserializeActionResult`

- `formDataToObject`

- `getActionQueryString`

- `serializeActionResult`

- `type Actions`

- `type ActionAccept`

- `type AstroActionContext`

- `type SerializedActionResult`

#### What should I do?
 Section titled “What should I do?”
 Replace all imports of `serializeActionResult()` and `deserializeActionResult()` with `getActionContext()`. These two methods are now available through `getActionContext()`:

 src/middleware.ts ` import { defineMiddleware } from ' astro:middleware ' ; import { serializeActionResult, deserializeActionResult } from ' astro:actions ' ; import { getActionContext } from ' astro:actions ' ;
 export const onRequest = defineMiddleware ( async ( context , next ) => { const { serializeActionResult , deserializeActionResult } = getActionContext (context) ; // ... } ); ` { const { serializeActionResult, deserializeActionResult } = getActionContext(context); // ...});">
 Remove any occurrences of the other removed exports:

 ` import { ACTION_ERROR_CODES, ActionInputError, appendForwardSlash, astroCalledServerError, callSafely, formDataToObject, getActionQueryString, type Actions, type ActionAccept, type AstroActionContext, type SerializedActionResult, } from ' astro:actions ' ; `

 Learn more about all utilities available in the Actions API Reference .

### Removed: Percent-Encoding in routes
 Section titled “Removed: Percent-Encoding in routes”

 Implementation PR: feat: integrate vite environments (#14306)

 In Astro 5.x, it was possible to include a percent-encoded percent sign (`%25`) in filenames.

Astro 6.0 removes support for the characters `%25` in filenames for security reasons. This restriction prevents encoding-based security bypasses where `%25` decodes to `%`, potentially leading to ambiguous or invalid encoding sequences.

#### What should I do?
 Section titled “What should I do?”
 If you have route files with `%25` in the filename, rename them to use a different character:

 Terminal window ` src/pages/test%25file.astro src/pages/test-file.astro `

### Removed: `astro:ssr-manifest` virtual module (Integration API)
 Section titled “Removed: astro:ssr-manifest virtual module (Integration API)”

 Implementation PR: feat: integrate vite environments (#14306)

 In Astro 5.x, the deprecated `astro:ssr-manifest` virtual module could still be used to access configuration values.

Astro 6.0 removes the `astro:ssr-manifest` virtual module entirely. It is no longer used by integrations or internally by Astro. The manifest is now passed directly through integration hooks and adapter APIs rather than through a virtual module. For build-specific manifest data, use the `astro:build:ssr` integration hook, which receives the manifest as a parameter.

#### What should I do?
 Section titled “What should I do?”
 If your integration or code imports from `astro:ssr-manifest`, use `astro:config/server` instead to access configuration values:

 ` import { manifest } from ' astro:ssr-manifest ' ; import { srcDir, outDir, root } from ' astro:config/server ' ; // Use srcDir, outDir, root, etc. for configuration values `

 Learn more about the `astro:config` virtual module .

### Removed: `RouteData.generate()` (Adapter API)
 Section titled “Removed: RouteData.generate() (Adapter API)”

 Implementation PR: feat: integrate vite environments (#14306)

 In Astro 5.x, routes could be generated using the `generate()` method on `RouteData`.

Astro 6.0 removes `RouteData.generate()` because route generation is now handled internally by Astro.

#### What should I do?
 Section titled “What should I do?”
 Remove any calls to `route.generate()` in your code. This method is no longer needed:

 ` const generated = route . generate (params); `

 Learn more about the Adapter API .

### Removed: `routes` on `astro:build:done` hook (Integration API)
 Section titled “Removed: routes on astro:build:done hook (Integration API)”

 Implementation PR: feat: cleanup integration api (#14446)

 In Astro 5.0, accessing `routes` on the `astro:build:done` hook was deprecated.

Astro 6.0 removes the `routes` array passed to this hook entirely. Instead, the `astro:routes:resolved` hook should be used.

#### What should I do?
 Section titled “What should I do?”
 Remove any instance of `routes` passed to `astro:build:done` and replace it with the new `astro:routes:resolved` hook. Access `distURL` on the newly exposed `assets` map:

 my-integration.mjs ` const integration = () => { let routes return { name: ' my-integration ' , hooks: { ' astro:routes:resolved ' : ( params ) => { routes = params . routes }, ' astro:build:done ' : ( { routes assets } ) => { for ( const route of routes ) { const distURL = assets . get ( route . pattern ) if ( distURL ) { Object . assign ( route , { distURL } ) } } console . log ( routes ) } } } } ` { let routes return { name: &#x27;my-integration&#x27;, hooks: { &#x27;astro:routes:resolved&#x27;: (params) => { routes = params.routes }, &#x27;astro:build:done&#x27;: ({ routes assets }) => { for (const route of routes) { const distURL = assets.get(route.pattern) if (distURL) { Object.assign(route, { distURL }) } } console.log(routes) } } }}">

 Learn more about the Integration API `astro:routes:resolved` hook for building integrations.

### Removed: `entryPoints` on `astro:build:ssr` hook (Integration API)
 Section titled “Removed: entryPoints on astro:build:ssr hook (Integration API)”

 Implementation PR: feat: cleanup integration api (#14446)

 In Astro 5.0, `functionPerRoute` was deprecated . That meant that `entryPoints` on the `astro:build:ssr` hook was always empty.

Astro 6.0 removes the `entryPoints` map passed to this hook entirely.

#### What should I do?
 Section titled “What should I do?”
 Remove any instance of `entryPoints` passed to `astro:build:ssr`:

 my-integration.mjs ` const integration = () => { return { name: ' my-integration ' , hooks: { ' astro:build:ssr ' : ( params ) => { someLogic ( params . entryPoints ) }, } } } ` { return { name: &#x27;my-integration&#x27;, hooks: { &#x27;astro:build:ssr&#x27;: (params) => { someLogic(params.entryPoints) }, } }}">

### Removed: old `app.render()` signature (Adapter API)
 Section titled “Removed: old app.render() signature (Adapter API)”

 Implementation PR: feat: clean deprecated APIs (#14462)

 In Astro 4.0, the `app.render()` signature that allowed passing `routeData` and `locals` as optional arguments was deprecated in favor of a single optional `renderOptions` argument.

Astro 6.0 removes this signature entirely. Attempting to pass these separate arguments will now cause an error in your project.

#### What should I do?
 Section titled “What should I do?”
 Review your `app.render()` calls and pass `routeData` and `locals` as properties of an object instead of as multiple independent arguments:

 my-adapter/entrypoint.ts ` app . render (request, routeData, locals) app . render (request, { routeData, locals }) `

 Learn more about the Adapter API .

### Removed: `app.setManifestData()` (Adapter API)
 Section titled “Removed: app.setManifestData() (Adapter API)”

 Implementation PR: chore(astro)!: remove app.setManifestData() (#14758)

 In Astro 5.0, the `app.setManifestData()` method was available on `App` and `NodeApp`, but is no longer used nor needed.

Astro 6.0 removes this method entirely.

#### What should I do?
 Section titled “What should I do?”
 Remove any call to `app.setManifestData()`. If you need to update the manifest, create a new `App` instance.

 Learn more about the Adapter API .

### Removed: `handleForms` prop for the `&#x3C;ClientRouter />` component
 Section titled “Removed: handleForms prop for the &#x3C;ClientRouter /> component”

 Implementation PR: feat: clean deprecated APIs (#14462)

 In Astro 4.0, the `handleForms` prop of the `&#x3C;ClientRouter />` component was deprecated, as it was no longer necessary to opt in to handling `submit` events for `form` elements. This functionality has been built in by default and the property, if still included in your project, silently had no impact on form submission.

Astro 6.0 removes this prop entirely and it now must be removed to avoid errors in your project.

#### What should I do?
 Section titled “What should I do?”
 Remove the `handleForms` property from your `&#x3C;ClientRouter />` component if it exists. It has provided no additional functionality, and so removing it should not change any behavior in your project:

 src/pages/index.astro ` --- import { ClientRouter } from " astro:transitions " ; --- &#x3C; html > &#x3C; head > &#x3C; ClientRouter handleForms /> &#x3C;/ head > &#x3C; body > &#x3C;!-- stuff here --> &#x3C;/ body > &#x3C;/ html > `        ">

 Learn more about transitions with forms .

### Removed: `prefetch()` `with` option
 Section titled “Removed: prefetch() with option”

 Implementation PR: feat: clean deprecated APIs (#14462)

 In Astro 4.8.4, the `with` option of the programmatic `prefetch()` function was deprecated in favor of a more sensible default behavior that no longer required specifying the priority of prefetching for each page.

Astro 6.0 removes this option entirely and it is no longer possible to configure the priority of prefetching by passing the `with` option. Attempting to do so will now cause errors.

By default, Astro’s prefetching now uses an automatic approach that will always try to use `&#x3C;link rel="prefetch>` if supported, or will fall back to `fetch()`.

#### What should I do?
 Section titled “What should I do?”
 Review your `prefetch()` calls and remove the `with` option if it still exists:

 ` prefetch ( ' /about ' , { with: ' fetch ' }); prefetch ( ' /about ' ); `

 Learn more about prefetching .

### Removed: `rewrite()` from Actions context
 Section titled “Removed: rewrite() from Actions context”

 Implementation PR: feat!: remove rewrite from action context (#14477)

 In Astro 5.5.6, the `ActionAPIContext.rewrite()` method was deprecated because custom endpoints should be used instead of rewrites.

Astro 6.0 removes the `rewrite()` method from `ActionAPIContext` entirely and it may no longer be used.

#### What should I do?
 Section titled “What should I do?”
 Review your Actions handlers and remove any call to `rewrite()`:

 src/actions/index.ts ` import { defineAction } from ' astro:actions ' ; import { z } from ' astro/zod ' ;
 export const server = { getGreeting: defineAction ( { input: z . object ( { // ... } ) , handler : async ( input , context ) => { context . rewrite ( ' / ' ) // ... } } ) } ` { context.rewrite(&#x27;/&#x27;) // ... } })}">

 Learn more about rewrites .

### Removed: schema function signature (Content Loader API)
 Section titled “Removed: schema function signature (Content Loader API)”

 Implementation PR: feat: loader.createSchema() (#14759)

 In Astro 5.x, a content loader could choose to define a schema as a function instead of defining a Zod schema object for validation. This is useful to dynamically generate the schema based on the configuration options or by introspecting an API.

Astro 6.0 removes this signature and introduces a new `createSchema()` property as a replacement for those who still want to dynamically define a schema in their content loader.

Providing a schema function in the old way will log a warning message that the loader’s schema is being ignored, but otherwise the loader will continue to work as if no schema had been provided. In a future major version, loaders that provide a schema function will throw an error and cannot be used.

#### What should I do?
 Section titled “What should I do?”
 If you are building a content loader and using a function to dynamically return a collection `schema` property, you must remove your existing function and use the new `createSchema()` property to define your schema instead.

For example, you can reproduce Astro’s previous behavior by using `zod-to-ts` directly with `createSchema()` and any previous function logic:

 ` import type { Loader } from ' astro/loaders ' import { createTypeAlias, zodToTs } from ' zod-to-ts ' import { getSchemaFromApi } from ' ./utils '
 function myLoader () { return { name: ' my-loader ' , load : async ( context ) => { // ... } , schema : async () => await getSchemaFromApi () , createSchema : async () => { const schema = await getSchemaFromApi () const identifier = ' Entry ' const { node } = zodToTs (schema , identifier) const typeAlias = createTypeAlias (node , identifier)
 return { schema , types: ` export ${ typeAlias } ` } } } satisfies Loader } ` { // ... }, schema: async () => await getSchemaFromApi(), createSchema: async () => { const schema = await getSchemaFromApi() const identifier = &#x27;Entry&#x27; const { node } = zodToTs(schema, identifier) const typeAlias = createTypeAlias(node, identifier) return { schema, types: &#x60;export ${typeAlias}&#x60; } } } satisfies Loader}">

 Learn more about `createSchema()` in the Content Loader API reference.

### Removed: session `test` driver
 Section titled “Removed: session test driver”

 Implementation PR: feat(sessions): drivers (#15006)

 In Astro 5.x, the internal session `test` driver was exported in the Astro config types, but it was not meant to be exposed for public use.

Astro 6.0 removes the session `test` driver as it is no longer used internally to test `context.session`.

#### What should I do?
 Section titled “What should I do?”
 It is unlikely that you are using this internal API. If you do, you must remove any usage of the session `test` driver:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' import { createMockStorage } from ' ./utils '
 export default defineConfig ({ session: { driver: ' test ' , options: { mockStorage: createMockStorage () } } }) `

 Learn more about the Session Driver API .

### Removed: support for CommonJS config files
 Section titled “Removed: support for CommonJS config files”

 Implementation PR: Drop cjs config support (#15192)

 In Astro 5.x, the Astro config file could use any of the following extensions: `.mjs`, `.js`, `.ts`, `.mts`, `.cjs` and `.cts`.

Astro 6.0 removes `.cjs` and `.cts` extensions.

#### What should I do?
 Section titled “What should I do?”
 If you have a `astro.config.cjs` or `astro.config.cts` file, update it to use of the supported extensions: `.mjs`, `.js`, `.ts` or `.mts`.

 Learn more about the Astro config file .

### Experimental Flags
 Section titled “Experimental Flags”
 Experimental flags allow you to opt in to features while they are in early development. Astro may also use experimental flags to test breaking changes to default behavior. The following experimental flags have been removed in Astro 6.0 and are now stable, or the new default behavior.

Remove these experimental flags from your Astro config if you were previously using them:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ experimental: { csp: true , fonts: true , liveContentCollections: true , preserveScriptOrder: true , staticImportMetaEnv: true , headingIdCompat: true , failOnPrerenderConflict: true }, }) `

#### Experimental features now stable:
 Section titled “Experimental features now stable:”

- `csp` (See the `security.csp` configuration reference to learn more about Content Security Policy.)

- `fonts` (See the updated fonts guide to learn more about adding custom fonts to your project.)

- `liveContentCollections` (See the updated content collections docs to learn more about live collections.)

- `failOnPrerenderConflict` (See the new `prerenderConflictBehavior` configuration option.)

#### New default or recommended behavior:
 Section titled “New default or recommended behavior:”

- `preserveScriptOrder` (See below for breaking changes to default `&#x3C;script>` and `&#x3C;style>` behavior .)

- `staticImportMetaEnv` (See below for breaking changes to `import.meta.env` .)

- `headingIdCompat` (See below for breaking changes to Markdown heading ID generation .)

 Read about exciting new features and more in the v6.0 Blog post .

## Changed Defaults
 Section titled “Changed Defaults”
 Some default behavior has changed in Astro v6.0 and your project code may need updating to account for these changes.

In most cases, the only action needed is to review your existing project’s deployment and ensure that it continues to function as you expect, making updates to your code as necessary. In some cases, there may be a configuration setting to allow you to continue to use the previous default behavior.

### Changed: `i18n.routing.redirectToDefaultLocale` default value
 Section titled “Changed: i18n.routing.redirectToDefaultLocale default value”

 Implementation PR: feat(astro)!: update i18n.redirectToDefaultLocale default (#14406)

 In Astro v5.0, the `i18n.routing.redirectToDefaultLocale` default value was `true`. When combined with the `i18n.routing.prefixDefaultLocale` default value of `false`, the resulting redirects could cause infinite loops.

In Astro v6.0, `i18n.routing.redirectToDefaultLocale` now defaults to `false`. Additionally, it can now only be used if `i18n.routing.prefixDefaultLocale` is set to `true`.

#### What should I do?
 Section titled “What should I do?”
 Review your Astro `i18n` config as you may now need to explicitly set values for `redirectToDefaultLocale` and `prefixDefaultLocale` to recreate your project’s previous behavior.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ i18n: { routing: { prefixDefaultLocale: true , redirectToDefaultLocale: true } } }) `
 If you are using manual routing, you may also need to update your middleware configuration:

 src/middleware.js ` import { middleware } from " astro:i18n " ; // Astro's own i18n routing config
 export const onRequest = middleware ( { prefixDefaultLocale: false , prefixDefaultLocale: true , redirectToDefaultLocale: true , } ) `

 Learn more about Internationalization routing .

### Changed: `&#x3C;script>` and `&#x3C;style>` tags are rendered in the order they are defined
 Section titled “Changed: &#x3C;script> and &#x3C;style> tags are rendered in the order they are defined”

 Implementation PR: feat: stabilize experimental preserveScriptOrder option (#14480)

 In Astro v5.5, the `experimental.preserveScriptOrder` flag was introduced to render multiple `&#x3C;style>` and `&#x3C;script>` tags in the same order as they were declared in the source code. Astro 5.x reversed their order in your generated HTML output. This could give unexpected results, for example, CSS styles being overridden by earlier defined style tags when your site was built.

Astro 6.0 removes this experimental flag and makes this the new default behavior in Astro: scripts and styles are now rendered in the order defined in your code.

#### What should I do?
 Section titled “What should I do?”
 If you were previously using this experimental feature, you must remove this experimental flag from your configuration as it no longer exists.

Review your `&#x3C;script>` and `&#x3C;style>` tags to make sure they behave as desired. You may need to reverse their order:

 src/components/MyComponent.astro ` &#x3C; p > I am a component &#x3C;/ p > &#x3C; style > body { background : red ; background : yellow ; } &#x3C;/ style > &#x3C; style > body { background : yellow ; background : red ; } &#x3C;/ style > &#x3C; script > console . log ( " hello " ) console . log ( " world " ) &#x3C;/ script > &#x3C; script > console . log ( " world! " ) console . log ( " hello! " ) &#x3C;/ script > ` I am a component
">

 Read more about using `script` and `style` tags.

### Changed: how responsive image styles are emitted
 Section titled “Changed: how responsive image styles are emitted”

 Implementation PR: support responsive images (#15407)

 In Astro 5.x, images were computed at runtime and the `fit` and `pos` responsive image styles were injected in a `style` attribute. This did not allow compatibility with Astro’s Content Security Policy (CSP) for many reasons.

Astro 6 generates image styles inside a virtual module at build time based on project configuration, resulting in a hash class and `data-*` attributes to apply responsive styling to your images.

#### What should I do?
 Section titled “What should I do?”
 Visually inspect your images to ensure that they are rendering as expected. This is an implementation detail that should not affect the expected use of responsive images.

However, if you were relying on the inline styles previously generated for your images:

 ` &#x3C; img style = " --fit: &#x3C;value>; --pos: &#x3C;value> " > ` ; --pos: &#x22; >">
 then you will need to update your project code to account for the new `data-*` attributes instead:

 ` &#x3C; img class = " __a_HaSh350 " data-astro-fit = " value " data-astro-pos = " value " > ` ">

## Breaking Changes
 Section titled “Breaking Changes”
 The following changes are considered breaking changes in Astro v6.0. Breaking changes may or may not provide temporary backwards compatibility. If you were using these features, you may have to update your code as recommended in each entry.

### Changed: endpoints with a file extension cannot be accessed with a trailing slash
 Section titled “Changed: endpoints with a file extension cannot be accessed with a trailing slash”

 Implementation PR: feat!: trailing slash never for endpoints with file extension (#14457)

 In Astro v5.0, custom endpoints whose URL ended in a file extension (e.g. `/src/pages/sitemap.xml.ts` ) could be accessed with a trailing slash (`/sitemap.xml/`) or without (`/sitemap.xml`), regardless of the value configured for `build.trailingSlash`.

In Astro v6.0, these endpoints can only be accessed without a trailing slash. This is true regardless of your `build.trailingSlash` configuration.

#### What should I do?
 Section titled “What should I do?”
 Review your links to your custom endpoints that include a file extension in the URL and remove any trailing slashes:

 src/pages/index.astro ` &#x3C; a href = " /sitemap.xml/ " > Sitemap &#x3C;/ a > &#x3C; a href = " /sitemap.xml " > Sitemap &#x3C;/ a > ` Sitemap  Sitemap ">

 Learn more about custom endpoints .

### Changed: `import.meta.env` values are always inlined
 Section titled “Changed: import.meta.env values are always inlined”

 Implementation PR: feat: stabilize static import meta env (#14485)

 In Astro 5.13, the `experimental.staticImportMetaEnv` flag was introduced to update the behavior when accessing `import.meta.env` directly to align with Vite’s handling of environment variables and ensures that `import.meta.env` values are always inlined.

In Astro 5.x, non-public environment variables were replaced by a reference to `process.env`. Additionally, Astro could also convert the value type of your environment variables used through `import.meta.env`, which could prevent access to some values such as the strings `"true"` (which was converted to a boolean value), and `"1"` (which was converted to a number).

Astro 6 removes this experimental flag and makes this the new default behavior in Astro: `import.meta.env` values are always inlined and never coerced.

#### What should I do?
 Section titled “What should I do?”
 If you were previously using this experimental feature, you must remove this experimental flag from your configuration as it no longer exists.

If you were relying on coercion, you may need to update your project code to apply it manually:

 src/components/MyComponent.astro ` const enabled : boolean = import. meta . env . ENABLED ; const enabled : boolean = import. meta . env . ENABLED === " true " ; `
 If you were relying on the transformation into `process.env`, you may need to update your project code to apply it manually:

 src/components/MyComponent.astro ` const enabled : boolean = import. meta . env . DB_PASSWORD ; const enabled : boolean = process . env . DB_PASSWORD ; `
 You may also need to update types:

 src/env.d.ts ` interface ImportMetaEnv { readonly PUBLIC_POKEAPI : string ; readonly DB_PASSWORD : string ; readonly ENABLED : boolean ; readonly ENABLED : string ; }
 interface ImportMeta { readonly env : ImportMetaEnv ; }
 namespace NodeJS { interface ProcessEnv { DB_PASSWORD : string ; } } `
 If you need more control over environment variables in Astro, we recommend you use `astro:env`.

 Learn more about environment variables in Astro, including `astro:env`.

### Changed: Cropping by default in default image service
 Section titled “Changed: Cropping by default in default image service”

 Implementation PR: feat(assets): Always allow cropping and never upscale (#14629)

 In Astro 5.0, the default image service would only apply cropping when the `fit` option was provided.

Astro 6.0 applies cropping by default without requiring setting the `fit` option.

#### What should I do?
 Section titled “What should I do?”
 No changes are needed to your existing cropped images as the `fit` property is still valid. However, if you were previously setting `fit` to `contain` (its default value) in order to crop your images, you may now remove this option and still achieve the same cropping behavior by specifying `width` and `height` alone:

 src/components/MyImage.astro ` -- - import { Image } from ' astro:assets ' ; import myImage from ' ../assets/photo.jpg ' ; -- - &#x3C; Image src = {myImage} width = { 400 } height = { 300 } fit = " contain " /> &#x3C; Image src = {myImage} width = { 400 } height = { 300 } /> `  ">

### Changed: Never upscale images in default image service
 Section titled “Changed: Never upscale images in default image service”

 Implementation PR: feat(assets): Always allow cropping and never upscale (#14629)

 In Astro 5.x, the default image service would upscale images when the requested dimensions were larger than the source image.

Astro 6.0 removes this behavior: the default image service never upscales images.

#### What should I do?
 Section titled “What should I do?”
 Review your images and update dimensions as needed. If you do need to upscale images, you may consider upscaling the images manually or using a custom image service that supports upscaling.

### Changed: SVG rasterization
 Section titled “Changed: SVG rasterization”

 Implementation PR: add support for SVG rasterization (#15180)

 In Astro v5.x, Astro’s default Sharp image service was unable to convert SVG files to raster files (e.g. PNG, WebP). This meant that the `&#x3C;Image />` component would ignore any value set for `format` when optimizing and transforming SVG files.

Astro 6.0 now supports SVG rasterization. This is subject to many limitations , for instance, SVGs with embedded fonts might not be converted properly. However, when the `format` property is set, the image service will now attempt to convert SVG images.

#### What should I do?
 Section titled “What should I do?”
 If you were previously relying on the fact that the image service would automatically skip converting SVGs, you must now check the format of your images beforehand to avoid converting SVGs to raster images:

 ` &#x3C; Image src = { imageThatMightBeAnSvg } format = " avif " alt = " example " />
 &#x3C; Image src = { imageThatMightBeAnSvg } format = { imageThatMightBeAnSvg . format === " svg " ? " svg " : " avif " } alt = " example " /> `  ">

 Learn more about the `format` image property .

### Changed: `getImage()` throws when called on the client
 Section titled “Changed: getImage() throws when called on the client”

 Implementation PR: feat: disallow getImage on the client (#15800)

 In Astro 5.x, calling `getImage()` from `astro:assets` on the client would silently fail or produce incorrect results.

Astro 6.0 throws a runtime error when `getImage()` is called on the client.

#### What should I do?
 Section titled “What should I do?”
 Call `getImage()` on the server and pass the resulting `src` to the client instead:

 src/components/ClientImage.astro ` --- import { getImage } from " astro:assets " ; import myBackground from " ../background.png " ;
 const optimizedBackground = await getImage ( { src: myBackground , format: " avif " } ); ---
 &#x3C; div id = " background " data-src = { optimizedBackground . src } >&#x3C;/ div >
 &#x3C; script > const src = document . getElementById ( " background " ) . dataset . src ; // use src client-side as needed &#x3C;/ script > ` ">

 See generating images with `getImage()` for a full example.

### Changed: Markdown heading ID generation
 Section titled “Changed: Markdown heading ID generation”

 Implementation PR: feat!: stabilize experimental.headingIdCompat (#14494)

 In Astro 5.x, an additional default processing step to Markdown stripped trailing hyphens from the end of IDs for section headings ending in special characters. This provided a cleaner `id` value, but could lead to incompatibilities rendering your Markdown across platforms.

In Astro 5.5, the `experimental.headingIdCompat` flag was introduced to allow you to make the IDs generated by Astro for Markdown headings compatible with common platforms like GitHub and npm, using the popular `github-slugger` package.

Astro 6.0 removes this experimental flag and makes this the new default behavior in Astro: trailing hyphens from the end of IDs for headings ending in special characters are no longer removed.

#### What should I do?
 Section titled “What should I do?”
 If you have manual links to headings, you may need to update the anchor link value with a new trailing hyphen. For example, the following Markdown heading:

 ` ## `&#x3C;Picture />` ` &#x60;">
 will now generate the following HTML with a trailing hyphen in the heading `id`:

 ` &#x3C; h2 id = " picture - " >&#x3C; code > &#x26;lt; Picture / &#x26;gt; &#x3C;/ code >&#x3C;/ h2 > `
 and must now be linked to as:

 ` See [ the Picture component ] ( /en/guides/images/#picture - ) for more details. `
 If you were previously using the experimental feature to enforce trailing hyphens, you must remove this experimental flag from your configuration as it no longer exists.

If you were previously using the `rehypeHeadingIds` plugin directly to enforce compatibility, remove the `headingIdCompat` option as it no longer exists:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { rehypeHeadingIds } from ' @astrojs/markdown-remark ' ; import { otherPluginThatReliesOnHeadingIDs } from ' some/plugin/source ' ;
 export default defineConfig ({ markdown: { rehypePlugins: [ [ rehypeHeadingIds , { headingIdCompat: true }], [ rehypeHeadingIds ], otherPluginThatReliesOnHeadingIDs , ], }, }); `
 If you want to keep the old ID generation for backward compatibility reasons, you can create a custom rehype plugin that will generate headings IDs like Astro 5.x. This will allow you to continue to use your existing anchor links without adding trailing hyphens.

 Create a custom rehype plugin to strip trailing hyphens
-
Install required dependencies:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm i github-slugger hast-util-heading-rank unist-util-visit hast-util-to-string `

 Terminal window
```
` pnpm add github-slugger hast-util-heading-rank unist-util-visit hast-util-to-string `
```

 Terminal window
```
` yarn add github-slugger hast-util-heading-rank unist-util-visit hast-util-to-string `
```

-
 Create a custom rehype plugin that will generate headings IDs like Astro v5:

 plugins/rehype-slug.mjs ` import GithubSlugger from ' github-slugger ' ; import { headingRank } from ' hast-util-heading-rank ' ; import { visit } from ' unist-util-visit ' ; import { toString } from ' hast-util-to-string ' ;
 const slugs = new GithubSlugger ();
 export function rehypeSlug () { /** * @param {import('hast').Root} tree */ return ( tree ) => { slugs . reset (); visit ( tree , ' element ' , ( node ) => { if ( headingRank ( node ) &#x26;&#x26; ! node . properties . id ) { let slug = slugs . slug ( toString ( node )); // Strip trailing hyphens like in Astro v5 and below: if ( slug . endsWith ( ' - ' )) slug = slug . slice ( 0 , - 1 ); node . properties . id = slug ; } }); }; } ` { slugs.reset(); visit(tree, &#x27;element&#x27;, (node) => { if (headingRank(node) &#x26;&#x26; !node.properties.id) { let slug = slugs.slug(toString(node)); // Strip trailing hyphens like in Astro v5 and below: if (slug.endsWith(&#x27;-&#x27;)) slug = slug.slice(0, -1); node.properties.id = slug; } }); };}">

-
 Add the custom plugin to your Markdown configuration in `astro.config.mjs`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { rehypeSlug } from ' ./plugins/rehype-slug ' ;
 export default defineConfig ({ markdown: { rehypePlugins: [ rehypeSlug ], }, }); `

 Learn more about Heading IDs .

### Changed: `getStaticPaths()` cannot return `params` of type number
 Section titled “Changed: getStaticPaths() cannot return params of type number”

 Implementation PR: fix!: disallow number in getStaticPaths params (#14586)

 In Astro 5.x, `getStaticPaths()` could return `params` of type number, which would always be stringified by Astro. However, that could be confusing because it conflicted with `Astro.params` types.

Astro 6.0 removes this behavior: `getStaticPaths()` must now return string or undefined `params` values.

#### What should I do?
 Section titled “What should I do?”
 Review your dynamic routes using `getStaticPaths()` and convert any number params to strings:

 src/pages/post/[id]/[label].astro ` --- export function getStaticPaths () { return [ { params: { id: 1 , id: " 1 " , label: " foo " , } } , { params: { id: 2 , id: " 2 " , label: " bar " , } } , ] } --- `

 Learn more about dynamic SSG routes with `getStaticPaths()` .

### Changed: Astro components cannot be rendered in Vitest client environments (Container API)
 Section titled “Changed: Astro components cannot be rendered in Vitest client environments (Container API)”

 Implementation PR: feat: remove Vitest workaround for client environment (#14895)

 In Astro 5.x, rendering an Astro component on the client was forbidden. However we temporarily allowed this behavior in Vitest client environments such as `jsdom` or `happy-dom` using the experimental Container API .

Astro 6.0 removes the ability to render Astro components in Vitest client environments: tests that render Astro components must now run in a server environment like `node`.

#### What should I do?
 Section titled “What should I do?”
 If you use Vitest to run tests that render Astro components in client environments like `jsdom` or `happy-dom`, update your Vitest config to use the `node` environment for these:

 vitest.config.ts ` import { defineConfig } from ' vitest/config ' ;
 export default defineConfig ({ test: { environment: ' jsdom ' , environment: ' node ' , }, }); `

 Learn more about testing Astro components .

### Changed: Rollup output file name config path (Vite config)
 Section titled “Changed: Rollup output file name config path (Vite config)”

 Implementation PR: feat: integrate vite environments (#14306)

 In Astro 5.x, custom Rollup output file name options for client assets could be configured at `vite.build.rollupOptions.output`.

Astro 6.0 scopes client build output configuration to Vite’s client environment. If you customize `entryFileNames`, `chunkFileNames`, or `assetFileNames` for client assets, use `vite.environments.client.build.rollupOptions.output`.

#### What should I do?
 Section titled “What should I do?”
 Move your config from `vite.build.rollupOptions.output` to `vite.environments.client.build.rollupOptions.output`:

 astro.config.mjs ` export default defineConfig ({ vite: { environments: { client: { build: { rollupOptions: { output: { entryFileNames: ' js/[name]-[hash].js ' , }, }, }, }, }, }, }); `

### Changed: Integration hooks and HMR access patterns (Integration API)
 Section titled “Changed: Integration hooks and HMR access patterns (Integration API)”

 Implementation PR: feat: integrate vite environments (#14306)

 In Astro 5.x, Astro relied on certain patterns for integration hooks and HMR access that were incompatible with or could be improved by integrating Vite’s Environment API.

Astro 6.0 uses Vite’s new Environment API for build configuration and dev server interactions. This primarily enables dev mode in runtimes like workerd, but means that some integration hooks and HMR access patterns have changed.

#### What should I do?
 Section titled “What should I do?”
 For integrations using `astro:build:setup`:

The hook is now called once with all environments configured (`ssr`, `client`, `prerender`), instead of being called separately for each build target. Remove the `target` parameter and use `vite.environments` to configure specific environments:

 my-integration.mjs ` { hooks: { ' astro:build:setup ' : ( { target , vite } ) => { if (target === ' client ' ) { vite . build . minify = false ; } } ' astro:build:setup ' : ( { vite } ) => { vite . environments . client . build . minify = false ; } } } ` { if (target === &#x27;client&#x27;) { vite.build.minify = false; } } &#x27;astro:build:setup&#x27;: ({ vite }) => { vite.environments.client.build.minify = false; } }}">
 For dev toolbar and integration code accessing HMR:

Replace `server.hot.send()` with `server.environments.client.hot.send()`:

 ` server . hot . send (event) server . environments . client . hot . send (event) `

 Learn more about the Vite Environment API and Astro integration hooks .

### Changed: `SSRManifest` interface structure (Adapter API)
 Section titled “Changed: SSRManifest interface structure (Adapter API)”

 Implementation PR: feat: integrate vite environments (#14306)

 In Astro 5.x, path properties of the `SSRManifest` interface like `srcDir`, `outDir`, `cacheDir`, `publicDir`, `buildClientDir`, and `buildServerDir` were URL strings.

Astro 6.0 changes the form of these path properties to `URL` objects instead of URL strings. With this change, several new properties are now available on the manifest, and others have been updated or removed.

#### What should I do?
 Section titled “What should I do?”
 If you were treating these path properties as strings, you will now need to handle the `URL` object. For example, you will now need to access the `href` property of the `URL` object:

 ` // To retrieve the same format (e.g., "file:///path/to/src"), make the following change: const srcPath = manifest . srcDir ; const srcPath = manifest . srcDir . href ; `
 If you were accessing the `hrefRoot` property, you will need to remove it, as it is no longer available on the manifest.

Update any use of `serverIslandMappings` and `sessionDriver`. These are now async methods:

 ` const mappings = manifest . serverIslandMappings ; const driver = manifest . sessionDriver ; const mappings = await manifest . serverIslandMappings ?. (); const driver = await manifest . sessionDriver ?. (); `

 Learn more about the Adapter API .

### Changed: schema types are inferred instead of generated (Content Loader API)
 Section titled “Changed: schema types are inferred instead of generated (Content Loader API)”

 Implementation PR: feat: loader.createSchema() (#14759)

 In Astro 5.x, the types for content collections were generated using `zod-to-ts` when provided by a content loader and not defined by a user-provided schema.

Astro 6.0 removes this behavior: types are no longer generated using `zod-to-ts`. Instead, types are inferred.

#### What should I do?
 Section titled “What should I do?”
 If you are providing a `schema` in a content loader, you must use the TypeScript’ `satisfies` operator :

 ` import type { Loader } from ' astro/loaders '
 function myLoader () : Loader { function myLoader () { return { name: ' my-loader ' , load : async ( context ) => { // ... } , schema: z . object ({ /* ... */ }) } } satisfies Loader } ` { // ... }, schema: z.object({/* ... */}) } } satisfies Loader}">

 Learn more about defining loader schema types .

## Known Issues
 Section titled “Known Issues”
 Please check Astro’s issues on GitHub for any reported issues, or to file an issue yourself.

 Upgrade Guides

 Contribute

 Community

 Sponsor

## V5

# Upgrade to Astro v5

 This guide will help you migrate from Astro v4 to Astro v5.

Need to upgrade an older project to v4 first? See our older migration guide .

Need to see the v4 docs? Visit this older version of the docs site (unmaintained v4.16 snapshot) .

## Upgrade Astro
 Section titled “Upgrade Astro”
 Update your project’s version of Astro to the latest version using your package manager:

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` # Upgrade Astro and official integrations together npx @astrojs/upgrade `

 Terminal window
```
` # Upgrade Astro and official integrations together pnpm dlx @astrojs/upgrade `
```

 Terminal window
```
` # Upgrade Astro and official integrations together yarn dlx @astrojs/upgrade `
```

 You can also upgrade your Astro integrations manually if needed, and you may also need to upgrade other dependencies in your project.

Astro v5.0 includes potentially breaking changes , as well as the removal and deprecation of some features.

If your project doesn’t work as expected after upgrading to v5.0, check this guide for an overview of all breaking changes and instructions on how to update your codebase.

See the Astro changelog for full release notes.

## Dependency Upgrades
 Section titled “Dependency Upgrades”
 Any major upgrades to Astro’s dependencies may cause breaking changes in your project.

### Vite 6.0
 Section titled “Vite 6.0”
 Astro v5.0 upgrades to Vite v6.0 as the development server and production bundler.

#### What should I do?
 Section titled “What should I do?”
 If you are using Vite-specific plugins, configuration, or APIs, check the Vite migration guide for their breaking changes and upgrade your project as needed.

### `@astrojs/mdx`
 Section titled “@astrojs/mdx”

 Implementation PR: Cleanup unused JSX code (#11741)

 In Astro v4.x, Astro performed internal JSX handling for the `@astrojs/mdx` integration.

Astro v5.0 moves this responsibility to handle and render JSX and MDX to the `@astrojs/mdx` package directly. This means that Astro 5.0 is no longer compatible with older versions of the MDX integration.

#### What should I do?
 Section titled “What should I do?”
 If your project includes `.mdx` files, you must upgrade `@astrojs/mdx` to the latest version (v4.0.0) so that your JSX can be handled properly by the integration.

If you are using an MDX server renderer with the experimental Astro Container API you must update the import to reflect the new location:

 ` import mdxRenderer from " astro/jsx/server.js " ; import mdxRenderer from " @astrojs/mdx/server.js " ; `

 Learn more about using MDX in your project .

## Legacy
 Section titled “Legacy”
 The following features are now considered legacy features. They should function normally but are no longer recommended and are in maintenance mode. They will see no future improvements and documentation will not be updated. These features will eventually be deprecated, and then removed entirely.

### Legacy: v2.0 Content Collections API
 Section titled “Legacy: v2.0 Content Collections API”
 In Astro 4.x, content collections were defined, queried, and rendered using the Content Collections API first introduced in Astro v2.0 . All collection entries were local files within the reserved `src/content/` folder. Additionally, Astro’s file name convention to exclude building individual pages was built in to the Content Collections API.

Astro 5.0 introduces a new version of content collections using the Content Layer API which brings several performance improvements and added capabilities. While old (legacy) and new (Content Layer API) collections can continue exist together in this release, there are potentially breaking changes to existing legacy collections.

This release also removes the option to prefix collection entry file names with an underscore (`_`) to prevent building a route.

#### What should I do?
 Section titled “What should I do?”
 We recommend converting any existing collections to the new Content Layer API as soon as you are able and making any new collections using the Content Layer API.

If you are unable to convert your collections, then please consult the legacy collections breaking changes to see whether your existing collections are affected and require updating.

If you are unable to make any changes to your collections at this time, you can enable the `legacy.collections` flag which will allow you to keep your collections in their current state until the legacy flag is no longer supported.

 Learn more about the updated content collections .

 Updating existing collections Section titled “Updating existing collections”
 See the instructions below for updating an existing content collection (`type: 'content'` or `type: 'data'`) to use the Content Layer API.

 Step-by-step instructions to update a collection

 Move the content config file . This file no longer lives within the `src/content/` folder. This file should now exist at `src/content.config.ts`.

-
 Edit the collection definition . Your updated collection requires a `loader` which indicates both a folder for the location of your collection (`base`) and a `pattern` defining the collection entry filenames and extensions to match. (You may need to update the example below accordingly. You can use globster.xyz to check your glob pattern.) The option to select a collection `type` is no longer available.

 src/content.config.ts ` import { defineCollection, z } from ' astro:content ' ; import { glob } from ' astro/loaders ' ;
 const blog = defineCollection ( { // For content layer you no longer define a `type` type: ' content ' , loader: glob ( { pattern: ' **/[^_]*.{md,mdx} ' , base: " ./src/data/blog " } ) , schema: z . object ( { title: z . string () , description: z . string () , pubDate: z . coerce . date () , updatedDate: z . coerce . date () . optional () , } ) , } ); `

-
 Change references from `slug` to `id` . Content layer collections do not have a reserved `slug` field. Instead, all updated collections will have an `id`:

 src/pages/[slug].astro ` --- export async function getStaticPaths () { const posts = await getCollection ( ' blog ' ); return posts . map ( ( post ) => ({ params: { slug: post . slug } , params: { slug: post . id } , props: post , })); } --- ` ({ params: { slug: post.slug }, params: { slug: post.id }, props: post, }));}---">
 You can also update the dynamic routing file names to match the value of the changed `getStaticPaths()` parameter.

-
 Switch to the new `render()` function . Entries no longer have a `render()` method, as they are now serializable plain objects. Instead, import the `render()` function from `astro:content`.

 src/pages/index.astro ` --- import { getEntry , render } from ' astro:content ' ;
 const post = await getEntry ( ' blog ' , params . slug );
 const { Content , headings } = await post . render (); const { Content , headings } = await render (post); --- &#x3C; Content /> ` ">

 Breaking changes to legacy `content` and `data` collections Section titled “Breaking changes to legacy content and data collections”

 Implementation PR: Implement legacy collections using glob (#11976)

 By default, collections that use the old `type` property (`content` or `data`) and do not define a `loader` are now implemented under the hood using the Content Layer API’s built-in `glob()` loader, with extra backward-compatibility handling.

Additionally, temporary backwards compatibility exists for keeping the content config file in its original location of `src/content/config.ts`.

This backwards compatibility implementation is able to emulate most of the features of legacy collections and will allow many legacy collections to continue to work even without updating your code. However, there are some differences and limitations that may cause breaking changes to existing collections :

- In previous versions of Astro, collections would be generated for all folders in `src/content/`, even if they were not defined in `src/content/config.ts`. This behavior is now deprecated, and collections should always be defined in `src/content.config.ts`. For existing collections, these can just be empty declarations (e.g. `const blog = defineCollection({})`) and Astro will implicitly define your legacy collection for you in a way that is compatible with the new loading behavior.

- The special `layout` field is not supported in Markdown collection entries. This property is intended only for standalone page files located in `src/pages/` and not likely to be in your collection entries. However, if you were using this property, you must now create dynamic routes that include your page styling.

- Sort order of generated collections is non-deterministic and platform-dependent. This means that if you are calling `getCollection()`, the order in which entries are returned may be different than before. If you need a specific order, you must sort the collection entries yourself.

- `image().refine()` is not supported. If you need to validate the properties of an image you will need to do this at runtime in your page or component.

- The `key` argument of `getEntry(collection, key)` is typed as `string`, rather than having types for every entry.

- Previously when calling `getEntry(collection, key)` with a static string as the key, the return type was not nullable. The type now includes `undefined` so you must check if the entry is defined before using the result or you will have type errors.

 Enabling the `legacy.collections` flag Section titled “Enabling the legacy.collections flag”

 Implementation PR: Implement legacy collections using glob (#11976)

 If you are not yet ready to update your existing collections, you can enable the `legacy.collections` flag and your existing collections will continue to function as before.

## Deprecated
 Section titled “Deprecated”
 The following deprecated features are no longer supported and are no longer documented. Please update your project accordingly.

Some deprecated features may temporarily continue to function until they are completely removed. Others may silently have no effect, or throw an error prompting you to update your code.

### Deprecated: `Astro.glob()`
 Section titled “Deprecated: Astro.glob()”

 Implementation PR: Deprecate glob (#11826)

 In Astro v4.x, you could use `Astro.glob()` in your `.astro` components to query multiple files in your project. This had some limitations (where it could be used, performance, etc.), and using querying functions from the Content Collections API or Vite’s own `import.meta.glob()` often provided more function and flexibility.

Astro 5.0 deprecates `Astro.glob()` in favor of using `getCollection()` to query your collections, and `import.meta.glob()` to query other source files in your project.

#### What should I do?
 Section titled “What should I do?”
 Replace all use of `Astro.glob()` with `import.meta.glob()`. Note that `import.meta.glob()` no longer returns a `Promise`, so you may have to update your code accordingly. You should not require any updates to your glob patterns .

 src/pages/blog.astro ` --- const posts = await Astro . glob ( ' ./posts/*.md ' ); const posts = Object . values ( import. meta . glob ( ' ./posts/*.md ' , { eager: true } )); ---
 { posts . map ( ( post ) => &#x3C; li >&#x3C; a href = { post . url } > { post . frontmatter . title } &#x3C;/ a >&#x3C;/ li > ) } ` - {post.frontmatter.title}
)}">
 Where appropriate, consider using content collections to organize your content, which has its own newer, more performant querying functions.

You may also wish to consider using glob packages from NPM, such as `fast-glob` .

 Learn more about importing files with `import.meta.glob` .

### Deprecated: `functionPerRoute` (Adapter API)
 Section titled “Deprecated: functionPerRoute (Adapter API)”

 Implementation PR: Remove functionPerRoute option (#11714)

 In Astro v4.x, you could opt into creating a separate file for each route defined in the project, mirroring your `src/pages/` directory in the build folder. By default, Astro emitted a single `entry.mjs` file, which was responsible for emitting the rendered page on each request.

Astro v5.0 removes the option to opt out of the default behavior. This behavior is now standard, and non-configurable.

Remove the `functionPerRoute` property from your `adapterFeatures` configuration. It is no longer available.

 my-adapter.mjs ` export default function createIntegration () { return { name: ' @matthewp/my-adapter ' , hooks: { ' astro:config:done ' : ( { setAdapter } ) => { setAdapter ({ name: ' @matthewp/my-adapter ' , serverEntrypoint: ' @matthewp/my-adapter/server.js ' , adapterFeatures: { functionPerRoute: true } }); } , } , }; } ` { setAdapter({ name: &#x27;@matthewp/my-adapter&#x27;, serverEntrypoint: &#x27;@matthewp/my-adapter/server.js&#x27;, adapterFeatures: { functionPerRoute: true } }); }, }, };}">

 Learn more about the Adapter API for building adapter integrations.

### Deprecated: `routes` on `astro:build:done` hook (Integration API)
 Section titled “Deprecated: routes on astro:build:done hook (Integration API)”

 Implementation PR: feat(next): astro:routes:resolved (#12329)

 In Astro v4.x, integrations accessed routes from the `astro:build:done` hook.

Astro v5.0 deprecates the `routes` array passed to this hook. Instead, it exposes a new `astro:routes:resolved` hook that runs before `astro:config:done`, and whenever a route changes in development. It has all the same properties of the deprecated `routes` list, except `distURL` which is only available during build.

#### What should I do?
 Section titled “What should I do?”
 Remove any instance of `routes` passed to `astro:build:done` and replace it with the new `astro:routes:resolved` hook. Access `distURL` on the newly exposed `assets` map:

 my-integration.mjs ` const integration = () => { let routes return { name: ' my-integration ' , hooks: { ' astro:routes:resolved ' : ( params ) => { routes = params . routes }, ' astro:build:done ' : ( { routes assets } ) => { for ( const route of routes ) { const distURL = assets . get ( route . pattern ) if ( distURL ) { Object . assign ( route , { distURL } ) } } console . log ( routes ) } } } } ` { let routes return { name: &#x27;my-integration&#x27;, hooks: { &#x27;astro:routes:resolved&#x27;: (params) => { routes = params.routes }, &#x27;astro:build:done&#x27;: ({ routes assets }) => { for (const route of routes) { const distURL = assets.get(route.pattern) if (distURL) { Object.assign(route, { distURL }) } } console.log(routes) } } }}">

 Learn more about the Integration API `astro:routes:resolved` hook for building integrations.

## Removed
 Section titled “Removed”
 The following features have now been entirely removed from the code base and can no longer be used. Some of these features may have continued to work in your project even after deprecation. Others may have silently had no effect.

Projects now containing these removed features will be unable to build, and there will no longer be any supporting documentation prompting you to remove these features.

### Removed: The Lit integration
 Section titled “Removed: The Lit integration”

 Implementation PR: Remove `@astrojs/lit` (#11680)

 In Astro v4.x, Lit was a core-maintained framework library through the `@astrojs/lit` package.

Astro v5.0 removes the integration and it will not receive further updates for compatibility with 5.x and above.

#### What should I do?
 Section titled “What should I do?”
 You can continue to use Lit for client components by adding a client-side script tag. For example:

 ` &#x3C; script > import " ../components/MyTabs " ; &#x3C;/ script >
 &#x3C; my-tabs title = " These are my tabs " > ... &#x3C;/ my-tabs > ` ... ">
 If you’re interested in maintaining a Lit integration yourself, you may wish to use the last published version of `@astrojs/lit` as a starting point and upgrade the relevant packages.

 Learn more about Astro’s official integrations .

### Removed: `hybrid` rendering mode
 Section titled “Removed: hybrid rendering mode”

 Implementation PR: Merge output:hybrid and output:static (#11824)

 In Astro v4.x, Astro provided three rendering `output` rendering modes: `'static'`, `'hybrid'`, and `'server'`

Astro v5.0 merges the `output: 'hybrid'` and `output: 'static'` configurations into one single configuration (now called `'static'`) that works the same way as the previous hybrid option.

It is no longer necessary to specify `output: 'hybrid'` in your Astro config to use server-rendered pages. The new `output: 'static'` has this capability included.

Astro will now automatically allow you to opt out of prerendering in your static site with no change to your output configuration required. Any page route or endpoint can include `export const prerender = false` to be server-rendered on demand, while the rest of your site is statically generated.

#### What should I do?
 Section titled “What should I do?”
 If your project used hybrid rendering, you must now remove the `output: 'hybrid'` option from your Astro config as it no longer exists. However, no other changes to your project are required, and you should have no breaking changes. The previous `'hybrid'` behavior is now the default, under a new name `'static'`.

 astro.config.mjs ` import { defineConfig } from " astro/config " ;
 export default defineConfig ({ output: ' hybrid ' , }); `
 If you were using the `output: 'static'` (default) option, you can continue to use it as before. By default, all of your pages will continue to be prerendered and you will have a completely static site. You should have no breaking changes to your project.

An adapter is still required to deploy an Astro project with any server-rendered pages, no matter which `output` mode your project uses. Failure to include an adapter will result in a warning in development and an error at build time.

 Learn more about on-demand rendering in Astro .

### Removed: support for dynamic `prerender` values in routes
 Section titled “Removed: support for dynamic prerender values in routes”

 Implementation PR: Merge output:hybrid and output:static (#11824)

 In Astro 4.x, environment variables could be used to dynamically set the value of `prerender` exports in routes, for example `export const prerender = import.meta.env.SOME_VAR`.

Astro v5.0 removes support for dynamic values in `prerender` exports. Only the static values `true` and `false` are supported.

#### What should I do?
 Section titled “What should I do?”

-
 Remove any dynamic `prerender` exports in your routes:

 src/pages/blog/[slug].astro ` --- export const prerender = import. meta . env . SOME_VAR ; --- `

-
 Use an Astro integration in your `astro.config.mjs` file to set `prerender` values that need to be dynamic in the `"astro:route:setup"` hook:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { loadEnv } from ' vite ' ;
 export default defineConfig ({ integrations: [ { name: ' set-prerender ' , hooks: { ' astro:route:setup ' : ( { route } ) => { // Load environment variables from .env files (if needed) const { PRERENDER } = loadEnv ( process . env . NODE_ENV , process . cwd () , '' ); // Find routes matching the expected filename. if ( route . component . endsWith ( ' /blog/[slug].astro ' )) { // Set the prerender value on routes as needed. route . prerender = PRERENDER ; } }, }, } ], }); ` { // Load environment variables from .env files (if needed) const { PRERENDER } = loadEnv(process.env.NODE_ENV, process.cwd(), &#x27;&#x27;); // Find routes matching the expected filename. if (route.component.endsWith(&#x27;/blog/[slug].astro&#x27;)) { // Set the prerender value on routes as needed. route.prerender = PRERENDER; } }, }, } ],});">

### Removed: Squoosh image service
 Section titled “Removed: Squoosh image service”

 Implementation PR: remove the squoosh image service (#11770)

 In Astro 4.x, you could configure `image.service: squooshImageService()` to use Squoosh to transform your images instead of Sharp. However, the underlying library `libsquoosh` is no longer maintained and has memory and performance issues.

Astro 5.0 removes the Squoosh image optimization service entirely.

#### What should I do?
 Section titled “What should I do?”
 To switch to the built-in Sharp image service, remove the `squooshImageService` import from your Astro config. By default, you will use Sharp for `astro:assets`.

 astro.config.mjs ` import { squooshImageService } from " astro/config " ; import { defineConfig } from " astro/config " ;
 export default defineConfig ({ image: { service: squooshImageService () } }); `
 If you are using a strict package manager like `pnpm`, you may need to install the `sharp` package manually to use the Sharp image service, even though it is built into Astro by default.

If your adapter does not support Astro’s built-in Sharp image optimization, you can configure a no-op image service to allow you to use the `&#x3C;Image />` and `&#x3C;Picture />` components.

Alternatively, you may wish to consider a community-maintained Squoosh image service if you are unable to use the Sharp image service.

 For adapters Section titled “For adapters”
 If your adapter previously precised its compatibility status with Squoosh, you should now remove this information from your adapter configuration.

 my-adapter.mjs ` supportedAstroFeatures: { assets: { isSquooshCompatible: true } } `

 Read more about configuring your default image service .

### Removed: some public-facing types
 Section titled “Removed: some public-facing types”

 Implementation PR: Refactor/types (#11715)

 In Astro v4.x, `@types/astro.ts` exposed all types publicly to users, whether or not they were still actively used or only intended for internal use.

Astro v5.0 refactors this file to remove outdated and internal types. This refactor brings improvements to your editor (e.g. faster completions, lower memory usage, and more relevant completion options). However, this refactor may cause errors in some projects that have been relying on types that are no longer available to the public.

#### What should I do?
 Section titled “What should I do?”
 Remove any types that now cause errors in your project as you no longer have access to them. These are mostly APIs that have previously been deprecated and removed, but may also include types that are now internal.

 See the public types exposed for use .

### Experimental Flags
 Section titled “Experimental Flags”
 The following experimental flags have been removed in Astro v5.0 and these features are available for use:

- `env`

- `serverIslands`

Additionally, the following experimental flags have been removed and are now the default or recommended behavior in Astro v5.0 .

- `directRenderScript` (See below for breaking changes to default `&#x3C;script>` behavior .)

- `globalRoutePriority` (See below for breaking changes to default route priority order .)

- `contentLayer` (See guidance for upgrading existing content collections to the new, preferred Content Layer API.)

The following experimental flags have been removed and their corresponding features are not part of Astro v5.0 .

- `contentCollectionsCache`

Remove these experimental flags if you were previously using them, and move your `env` configuration to the root of your Astro config:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ experimental: { directRenderScript: true , globalRoutePriority: true , contentLayer: true , serverIslands: true , contentCollectionsCache: true , env: { schema: { ... } } }, env: { schema: { ... } } }) `
 These features are all available by default in Astro v5.0.

 Read about these exciting features and more in the v5.0 Blog post .

## Changed Defaults
 Section titled “Changed Defaults”
 Some default behavior has changed in Astro v5.0 and your project code may need updating to account for these changes.

In most cases, the only action needed is to review your existing project’s deployment and ensure that it continues to function as you expect, making updates to your code as necessary. In some cases, there may be a configuration setting to allow you to continue to use the previous default behavior.

### CSRF protection is now set by default
 Section titled “CSRF protection is now set by default”

 Implementation PR: change default value of checkOrigin (#11788)

 In Astro v4.x, The default value of `security.checkOrigin` was `false`. Previously, you had to explicitly set this value to `true` to enable Cross-Site Request Forgery (CSRF) protection.

Astro v5.0 changes the default value of this option to `true`, and will automatically check that the “origin” header matches the URL sent by each request in on-demand rendered pages.

#### What should I do?
 Section titled “What should I do?”
 If you had previously configured `security.checkOrigin: true`, you no longer need this line in your Astro config. This is now the default.

To disable this behavior, you must explicitly set `security.checkOrigin: false`.

 astro.config.mjs ` export default defineConfig ({ output: " server " , security: { checkOrigin: false } }) `

 Read more about security configuration options

### Route priority order for injected routes and redirects
 Section titled “Route priority order for injected routes and redirects”

 Implementation PR: Remove legacy route prioritization (#11798)

 In Astro v4.x, `experimental.globalRoutePriority` was an optional flag that ensured that injected routes, file-based routes, and redirects were all prioritized using the route priority order rules for all routes . This allowed more control over routing in your project by not automatically prioritizing certain kinds of routes and standardizing the route priority order.

Astro v5.0 removes this experimental flag and makes this the new default behavior in Astro: redirects and injected routes are now prioritized equally alongside file-based project routes.

Note that this was already the default behavior in Starlight, and should not affect updated Starlight projects.

#### What should I do?
 Section titled “What should I do?”
 If your project includes injected routes or redirects, please check that your routes are building page URLs as expected. An example of the new expected behavior is shown below.

In a project containing the following routes:

- File-based route: `/blog/post/[pid]`

- File-based route: `/[page]`

- Injected route: `/blog/[...slug]`

- Redirect: `/blog/tags/[tag] -> /[tag]`

- Redirect: `/posts -> /blog`

The following URLs will be built (instead of following the route priority order of Astro v4.x):

- `/blog/tags/astro` is built by the redirect to `/tags/[tag]` (instead of the injected route `/blog/[...slug]`)

- `/blog/post/0` is built by the file-based route `/blog/post/[pid]` (instead of the injected route `/blog/[...slug]`)

- `/posts` is built by the redirect to `/blog` (instead of the file-based route `/[page]`)

In the event of route collisions, where two routes of equal route priority attempt to build the same URL, Astro will log a warning identifying the conflicting routes.

 Read more about the route priority order rules .

### `&#x3C;script>` tags are rendered directly as declared
 Section titled “&#x3C;script> tags are rendered directly as declared”

 Implementation PR: Make directRenderScript the default (#11791)

 In Astro v4.x, `experimental.directRenderScript` was an optional flag to directly render `&#x3C;scripts>` as declared in `.astro` files (including existing features like TypeScript, importing `node_modules`, and deduplicating scripts). This strategy prevented scripts from being executed in places where they were not used. Additionally, conditionally rendered scripts were previously implicitly inlined, as if an `is:inline` directive was automatically added to them.

Astro 5.0 removes this experimental flag and makes this the new default behavior in Astro: scripts are no longer hoisted to the `&#x3C;head>`, multiple scripts on a page are no longer bundled together, and a `&#x3C;script>` tag may interfere with CSS styling. Additionally, conditionally rendered scripts are no longer implicitly inlined.

#### What should I do?
 Section titled “What should I do?”
 Please review your `&#x3C;script>` tags and ensure they behave as desired.

If you previously had conditionally rendered `&#x3C;script>` tags, you will need to add an `is:inline` attribute to preserve the same behavior as before:

 src/components/MyComponent.astro ` --- type Props = { showAlert : boolean }
 const { showAlert } = Astro . props ; --- { showAlert &#x26;&#x26; &#x3C; script is : inline > alert("Some very important code!!") &#x3C;/ script > } `

 Read more about using `script` tags in Astro .

## Breaking Changes
 Section titled “Breaking Changes”
 The following changes are considered breaking changes in Astro v5.0. Breaking changes may or may not provide temporary backwards compatibility. If you were using these features, you may have to update your code as recommended in each entry.

### Renamed: `&#x3C;ViewTransitions />` component
 Section titled “Renamed: &#x3C;ViewTransitions /> component”

 Implementation PR: Rename the ViewTransitions component to ClientRouter (#11980)

 In Astro 4.x, Astro’s View Transitions API included a `&#x3C;ViewTransitions />` router component to enable client-side routing, page transitions, and more.

Astro 5.0 renames this component to `&#x3C;ClientRouter />` to clarify the role of the component within the API. This makes it more clear that the features you get from Astro’s `&#x3C;ClientRouter />` routing component are slightly different from the native CSS-based MPA router.

No functionality has changed. This component has only changed its name.

#### What should I do?
 Section titled “What should I do?”
 Replace all occurrences of the `ViewTransitions` import and component with `ClientRouter`:

 src/layouts/MyLayout.astro ` import { ViewTransitions } from 'astro:transitions'; import { ClientRouter } from 'astro:transitions';
 &#x3C; html > &#x3C; head > ... &#x3C; ViewTransitions /> &#x3C; ClientRouter /> &#x3C;/ head > &#x3C;/ html > `   ...    ">

 Read more about view transitions and client-side routing in Astro .

### Changed: TypeScript configuration
 Section titled “Changed: TypeScript configuration”

 Implementation PR: better tsconfig (#11859)

 In Astro v4.x, Astro relied on a `src/env.d.ts` file for type inferencing and defining modules for features that relied on generated types.

Astro 5.0 instead uses a `.astro/types.d.ts` file for type inferencing, and now recommends setting `include` and `exclude` in `tsconfig.json` to benefit from Astro types and avoid checking built files.

Running `astro sync` no longer creates, nor updates, `src/env.d.ts` as it is not required for type-checking standard Astro projects.

#### What should I do?
 Section titled “What should I do?”
 To update your project to Astro’s recommended TypeScript settings, add the following `include` and `exclude` properties to your existing `tsconfig.json`:

 tsconfig.json ` { " extends " : " astro/tsconfigs/base " , " include " : [ " .astro/types.d.ts " , " **/* " ], " exclude " : [ " dist " ] } `
 Note that `src/env.d.ts` is only necessary if you have added custom configurations, or if you’re not using a `tsconfig.json` file.

 Read more about TypeScript configuration in Astro .

### Changed: Actions submitted by HTML forms no longer use cookie redirects
 Section titled “Changed: Actions submitted by HTML forms no longer use cookie redirects”

 Implementation PR: Actions middleware (#12373)

 In Astro 4.x, actions called from an HTML form would trigger a redirect with the result forwarded using cookies. This caused issues for large form errors and return values that exceeded the 4 KB limit of cookie-based storage.

Astro 5.0 now renders the result of an action as a POST result without any forwarding. This will introduce a “confirm form resubmission?” dialog when a user attempts to refresh the page, though it no longer imposes a 4 KB limit on action return value.

#### What should I do?
 Section titled “What should I do?”
 You should update handling for action results that relies on redirects, and optionally address the “confirm form resubmission?” dialog with middleware.

 To redirect to the previous route on error Section titled “To redirect to the previous route on error”
 If your HTML form action is directed to a different route (i.e. `action={"/success-page" + actions.name}`), Astro will no longer redirect to the previous route on error. You can implement this behavior manually using redirects from your Astro component. This example instead redirects to a new route on success, and handles errors on the current page otherwise:

 src/pages/newsletter.astro ` --- import { actions } from ' astro:actions ' ;
 const result = Astro . getActionResult (actions . newsletter ); if ( ! result ?. error ) { // Embed relevant result data in the URL if needed // example: redirect(`/confirmation?email=${result.data.email}`); return redirect ( ' /confirmation ' ); } ---
 &#x3C; form method = " POST " action = { ' /confirmation ' + actions . newsletter } > &#x3C; label > E-mail &#x3C; input required type = " email " name = " email " />&#x3C;/ label > &#x3C; button > Sign up &#x3C;/ button > &#x3C;/ form > `  E-mail  Sign up  ">
 (Optional) To remove the confirm dialog on refresh Section titled “(Optional) To remove the confirm dialog on refresh”
 To address the “confirm form resubmission?” dialog on refresh, or to preserve action results across sessions, you can now customize action result handling from middleware .

We recommend using a session storage provider as described in our Netlify Blob example . However, if you prefer the cookie forwarding behavior from 4.X and accept the 4 KB size limit, you can implement the pattern as shown in this sample snippet:

 src/middleware.ts ` import { defineMiddleware } from ' astro:middleware ' ; import { getActionContext } from ' astro:actions ' ;
 export const onRequest = defineMiddleware ( async ( context , next ) => { // Skip requests for prerendered pages if (context . isPrerendered ) return next () ;
 const { action , setActionResult , serializeActionResult } = getActionContext (context) ;
 // If an action result was forwarded as a cookie, set the result // to be accessible from `Astro.getActionResult()` const payload = context . cookies . get ( ' ACTION_PAYLOAD ' ) ; if (payload) { const { actionName , actionResult } = payload . json () ; setActionResult (actionName , actionResult) ; context . cookies . delete ( ' ACTION_PAYLOAD ' , { path: ' / ' } ) ; return next () ; }
 // If an action was called from an HTML form action, // call the action handler and redirect with the result as a cookie. if (action ?. calledFrom === ' form ' ) { const actionResult = await action . handler () ;
 context . cookies . set ( ' ACTION_PAYLOAD ' , { actionName: action . name , actionResult: serializeActionResult (actionResult) , }, { path: ' / ' , httpOnly: true , sameSite: ' lax ' , maxAge: 60 } ) ;
 if (actionResult . error ) { // Redirect back to the previous page on error const referer = context . request . headers . get ( ' Referer ' ) ; if ( ! referer) { throw new Error ( ' Internal: Referer unexpectedly missing from Action POST request. ' ) ; } return context . redirect (referer) ; } // Redirect to the destination page on success return context . redirect (context . originPathname ) ; }
 return next () ; } ) ` { // Skip requests for prerendered pages if (context.isPrerendered) return next(); const { action, setActionResult, serializeActionResult } = getActionContext(context); // If an action result was forwarded as a cookie, set the result // to be accessible from &#x60;Astro.getActionResult()&#x60; const payload = context.cookies.get(&#x27;ACTION_PAYLOAD&#x27;); if (payload) { const { actionName, actionResult } = payload.json(); setActionResult(actionName, actionResult); context.cookies.delete(&#x27;ACTION_PAYLOAD&#x27;, { path: &#x27;/&#x27; }); return next(); } // If an action was called from an HTML form action, // call the action handler and redirect with the result as a cookie. if (action?.calledFrom === &#x27;form&#x27;) { const actionResult = await action.handler(); context.cookies.set(&#x27;ACTION_PAYLOAD&#x27;, { actionName: action.name, actionResult: serializeActionResult(actionResult), }, { path: &#x27;/&#x27;, httpOnly: true, sameSite: &#x27;lax&#x27;, maxAge: 60 }); if (actionResult.error) { // Redirect back to the previous page on error const referer = context.request.headers.get(&#x27;Referer&#x27;); if (!referer) { throw new Error(&#x27;Internal: Referer unexpectedly missing from Action POST request.&#x27;); } return context.redirect(referer); } // Redirect to the destination page on success return context.redirect(context.originPathname); } return next();})">

### Changed: `compiledContent()` is now an async function
 Section titled “Changed: compiledContent() is now an async function”

 Implementation PR: Remove TLA by making compiledContent async (#11782)

 In Astro 4.x, top level await was included in Markdown modules. This caused some issues with custom image services and images inside Markdown, causing Node to suddenly exit with no error message.

Astro 5.0 makes the `compiledContent()` property on Markdown import an async function, requiring an `await` to resolve the content.

#### What should I do?
 Section titled “What should I do?”
 Update your code to use `await` when calling `compiledContent()`.

 src/pages/post.astro ` --- import * as myPost from " ../blog/post.md " ;
 const content = myPost . compiledContent (); const content = await myPost . compiledContent (); ---
 &#x3C; Fragment set:html = { content } /> ` ">

 Read more about the `compiledContent()` function for returning compiled Markdown.

### Changed: `astro:content` can no longer be used on the client
 Section titled “Changed: astro:content can no longer be used on the client”

 Implementation PR: Prevent usage of `astro:content` in the client (#11827)

 In Astro 4.x, it was possible to access the `astro:content` module on the client.

Astro 5.0 removes this access as it was never intentionally exposed for client use. Using `astro:content` this way had limitations and bloated client bundles.

#### What should I do?
 Section titled “What should I do?”
 If you are currently using `astro:content` in the client, pass the data you need through props to your client components instead:

 src/pages/blog.astro ` --- import { getCollection } from ' astro:content ' ; import ClientComponent from ' ../components/ClientComponent ' ;
 const posts = await getCollection ( ' blog ' ); const postsData = posts . map ( post => post . data ); ---
 &#x3C; ClientComponent posts = { postsData } /> ` post.data);--- ">

 Read more about the `astro:content` API .

### Renamed: Shiki `css-variables` theme color token names
 Section titled “Renamed: Shiki css-variables theme color token names”

 Implementation PR: Update to new shiki token names (#11661)

 In Astro v4.x, the Shiki `css-variables` theme used the `--astro-code-color-text` and `--astro-code-color-background` tokens for styling the foreground and background colors of code blocks respectively.

Astro v5.0 renames them to `--astro-code-foreground` and `--astro-code-background` respectively to better align with the Shiki v1 defaults.

#### What should I do?
 Section titled “What should I do?”
 You can perform a global find and replace in your project to migrate to the new token names.

 src/styles/global.css ` :root { --astro-code-color-text : # 000 ; --astro-code-color-background : # fff ; --astro-code-foreground : # 000 ; --astro-code-background : # fff ; } `

 Read more about syntax highlighting in Astro .

### Changed: internal Shiki rehype plugin for highlighting code blocks
 Section titled “Changed: internal Shiki rehype plugin for highlighting code blocks”

 Implementation PR: Refactor createShikiHighlighter (#11825)

 In Astro 4.x, Astro’s internal Shiki rehype plugin highlighted code blocks as HTML.

Astro 5.0 updates this plugin to highlight code blocks as hast. This allows a more direct Markdown and MDX processing and improves the performance when building the project. However, this may cause issues with existing Shiki transformers.

#### What should I do?
 Section titled “What should I do?”
 If you are using Shiki transformers passed to `markdown.shikiConfig.transformers`, you must make sure they do not use the `postprocess` hook. This hook no longer runs on code blocks in `.md` and `.mdx` files. (See the Shiki documentation on transformer hooks for more information).

Code blocks in `.mdoc` files and Astro’s built-in `&#x3C;Code />` component do not use the internal Shiki rehype plugin and are unaffected.

 Read more about syntax highlighting in Astro .

### Changed: Automatic `charset=utf-8` behavior for Markdown and MDX pages
 Section titled “Changed: Automatic charset=utf-8 behavior for Markdown and MDX pages”

 Implementation PR: Unset charset=utf-8 content-type for md/mdx pages (#12231)

 In Astro 4.0, Markdown and MDX pages (located in `src/pages/`) automatically responded with `charset=utf-8` in the `Content-Type` header, which allowed rendering non-ASCII characters in your pages.

Astro 5.0 updates the behaviour to add the `&#x3C;meta charset="utf-8">` tag instead, and only for pages that do not use Astro’s special `layout` frontmatter property. Similarly for MDX pages, Astro will only add the tag if the MDX content does not import a wrapping `Layout` component.

If your Markdown or MDX pages use the `layout` frontmatter property, or if the MDX page content imports a wrapping `Layout` component, then the HTML encoding will be handled by the designated layout component instead, and the `&#x3C;meta charset="utf-8">` tag will not be added to your page by default.

#### What should I do?
 Section titled “What should I do?”
 If you require `charset=utf-8` to render your page correctly, make sure that your layout components contain the `&#x3C;meta charset="utf-8">` tag. You may need to add this if you have not already done so.

 Read more about Markdown layouts .

### Changed: Astro-specific metadata attached in remark and rehype plugins
 Section titled “Changed: Astro-specific metadata attached in remark and rehype plugins”

 Implementation PR: Clean up Astro metadata in vfile.data (#11861)

 In Astro 4.x, the Astro-specific metadata attached to `vfile.data` in remark and rehype plugins was attached in different locations with inconsistent names.

Astro 5 cleans up the API and the metadata is now renamed as below:

- `vfile.data.__astroHeadings` -> `vfile.data.astro.headings`

- `vfile.data.imagePaths` -> `vfile.data.astro.imagePaths`

The types of `imagePaths` has also been updated from `Set&#x3C;string>` to `string[]`. The `vfile.data.astro.frontmatter` metadata is left unchanged.

#### What should I do?
 Section titled “What should I do?”
 While we don’t consider these APIs public, they can be accessed by remark and rehype plugins that want to re-use Astro’s metadata. If you are using these APIs, make sure to access them in the new locations.

 Read more about using Markdown plugins in Astro .

### Changed: image endpoint configuration
 Section titled “Changed: image endpoint configuration”

 Implementation PR: Allow customising the route of the image endpoint (#11908)

 In Astro 4.x, you could set an endpoint in your `image` configuration to use for image optimization.

Astro 5.0 allows you to customize a `route` and `entrypoint` of the `image.endpoint` config. This can be useful in niche situations where the default route `/_image` conflicts with an existing route or your local server setup.

#### What should I do?
 Section titled “What should I do?”
 If you had previously customized `image.endpoint`, move this endpoint to the new `endpoint.entrypoint` property. Optionally, you may customize a `route`:

 astro.config.mjs ` import { defineConfig } from " astro/config " ;
 defineConfig ({ image: { endpoint: ' ./src/image-endpoint.ts ' , endpoint: { route: " /image " , entrypoint: " ./src/image_endpoint.ts " } }, }) `

 Read more about setting an endpoint to use for image optimization .

### Changed: `build.client` and `build.server` resolve behavior
 Section titled “Changed: build.client and build.server resolve behavior”

 Implementation PR: Fix build.client and build.server resolve behaviour (#11916)

 In Astro v4.x, the `build.client` and `build.server` options were documented to resolve relatively from the `outDir` option, but it didn’t always work as expected.

Astro 5.0 fixes the behavior to correctly resolve from the `outDir` option. For example, if `outDir` is set to `./dist/nested/`, then by default:

- `build.client` will resolve to `&#x3C;root>/dist/nested/client/`

- `build.server` will resolve to `&#x3C;root>/dist/nested/server/`

Previously the values were incorrectly resolved:

- `build.client` was resolved to `&#x3C;root>/dist/nested/dist/client/`

- `build.server` was resolved to `&#x3C;root>/dist/nested/dist/server/`

#### What should I do?
 Section titled “What should I do?”
 If you were relying on the previous build paths, make sure that your project code is updated to the new build paths.

 Read more about `build` configuration options in Astro .

### Changed: JS dependencies in config file are no longer processed by Vite
 Section titled “Changed: JS dependencies in config file are no longer processed by Vite”

 Implementation PR: Set external: true when loading astro config (#11819)

 In Astro 4.x, locally-linked JS dependencies (e.g. `npm link`, in a monorepo, etc) were able to use Vite features like `import.meta.glob` when imported by the Astro config file.

Astro 5 updates the Astro config loading flow to ignore processing locally-linked JS dependencies with Vite. Dependencies exporting raw TypeScript files are unaffected. Instead, these JS dependencies will be normally imported by the Node.js runtime the same way as other dependencies from `node_modules`.

This change was made as the previous behavior caused confusion among integration authors who tested against a package that worked locally, but not when published. It also restricted using CJS-only dependencies because Vite required the code to be ESM. While this change only affects JS dependencies, it’s also recommended for packages to export JavaScript instead of raw TypeScript where possible to prevent accidental Vite-specific usage as it’s an implementation detail of Astro’s config loading flow.

#### What should I do?
 Section titled “What should I do?”
 Make sure your locally-linked JS dependencies are built before running your Astro project. Then, the config loading should work as before.

 Read more about Vite configuration settings in Astro .

### Changed: URLs returned by `paginate()`
 Section titled “Changed: URLs returned by paginate()”

 Implementation PR: Add base to paginate (#11253)

 In Astro v4.x, the URL returned by `paginate()` (e.g. `page.url.next`, `page.url.first`, etc.) did not include the value set for `base` in your Astro config. You had to manually prepend your configured value for `base` to the URL path.

Astro 5.0 automatically includes the `base` value in `page.url`.

#### What should I do?
 Section titled “What should I do?”
 If you are using the `paginate()` function for these URLs, remove any existing `base` value as it is now added for you:

 ` --- export async function getStaticPaths ( { paginate } ) { const astronautPages = [{ astronaut: ' Neil Armstrong ' , } , { astronaut: ' Buzz Aldrin ' , } , { astronaut: ' Sally Ride ' , } , { astronaut: ' John Glenn ' , }]; return paginate (astronautPages , { pageSize: 1 }); } const { page } = Astro . props ; // `base: /'docs'` configured in `astro.config.mjs` const prev = " /docs " + page . url . prev ; const prev = page . url . prev ; --- &#x3C; a id = " prev " href = { prev } > Back &#x3C;/ a > ` Back ">

 Read more about pagination in Astro .

### Changed: non-boolean HTML attribute values
 Section titled “Changed: non-boolean HTML attribute values”

 Implementation PR: Fix attribute rendering for boolean values (take 2) (#11660)

 In Astro v4.x, non- boolean HTML attributes may not have included their values when rendered to HTML.

Astro v5.0 renders the values explicitly as `="true"` or `="false"`, matching proper attribute handling in browsers.

In the following `.astro` examples, only `allowfullscreen` is a boolean attribute:

 src/pages/index.astro ` &#x3C;!-- `allowfullscreen` is a boolean attribute --> &#x3C; p allowfullscreen = { true } >&#x3C;/ p > &#x3C; p allowfullscreen = { false } >&#x3C;/ p > &#x3C;!-- `inherit` is *not* a boolean attribute --> &#x3C; p inherit = { true } >&#x3C;/ p > &#x3C; p inherit = { false } >&#x3C;/ p > &#x3C;!-- `data-*` attributes are not boolean attributes --> &#x3C; p data-light = { true } >&#x3C;/ p > &#x3C; p data-light = { false } >&#x3C;/ p > `





">
Astro v5.0 now preserves the full data attribute with its value when rendering the HTML of non-boolean attributes:

 ` &#x3C; p allowfullscreen >&#x3C;/ p > &#x3C; p >&#x3C;/ p >
 &#x3C; p inherit = " true " >&#x3C;/ p > &#x3C; p inherit >&#x3C;/ p > &#x3C; p inherit = " false " >&#x3C;/ p >
 &#x3C; p data-light >&#x3C;/ p > &#x3C; p data-light = " true " >&#x3C;/ p > &#x3C; p >&#x3C;/ p > &#x3C; p data-light = " false " >&#x3C;/ p > `








">

#### What should I do?
 Section titled “What should I do?”
 If you rely on attribute values, for example, to locate elements or to conditionally render, update your code to match the new non-boolean attribute values:

 ` el . getAttribute ( ' inherit ' ) === '' el . getAttribute ( ' inherit ' ) === ' false '
 el . hasAttribute ( ' data-light ' ) el . dataset . light === ' true ' `

 Read more about using HTML attributes in Astro .

### Changed: adding values to `context.locals`
 Section titled “Changed: adding values to context.locals”

 Implementation PR: TODOs (#11987)

 In Astro 4.x, it was possible to completely replace the entire `locals` object in middleware, API endpoints, and pages when adding new values.

Astro 5.0 requires you to append values to the existing `locals` object without deleting it. Locals in middleware, API endpoints, and pages, can no longer be completely overridden.

#### What should I do?
 Section titled “What should I do?”
 Where you previously were overwriting the object, you must now instead assign values to it:

 src/middleware.js ` ctx . locals = { Object.assign(ctx. locals , { one: 1 , two: 2 } }) `

 See more about storing data in `context.locals` .

### Changed: `params` no longer decoded
 Section titled “Changed: params no longer decoded”

 Implementation PR: decode pathname early, don't decode params (#12079)

 In Astro v4.x, `params` passed to `getStaticPath()` were automatically decoded using `decodeURIComponent`.

Astro v5.0 no longer decodes the value of `params` passed to `getStaticPaths`. You must manually decode them yourself if needed.

#### What should I do?
 Section titled “What should I do?”
 If you were previously relying on the automatic decoding, use `decodeURI` when passing `params`.

 src/pages/[id].astro ` --- export function getStaticPaths () { return [ { params: { id: " %5Bpage%5D " } } , { params: { id: decodeURI ( " %5Bpage%5D " ) } } , ] }
 const { id } = Astro . params ; --- `
 Note that the use of `decodeURIComponent` is discouraged for `getStaticPaths` because it decodes more characters than it should, for example `/`, `?`, `#` and more.

 Read more about creating dynamic routes with `params` .

### Changed: `RouteData` type replaced by `IntegrationsRouteData` (Integrations API)
 Section titled “Changed: RouteData type replaced by IntegrationsRouteData (Integrations API)”

 Implementation PR: send `IntegrationRouteData` to integrations (#11864)

 In Astro v4.x, the `entryPoints` type inside the `astro:build:ssr` and `astro:build:done` hooks was `RouteData`.

Astro v5.0 the `entryPoints` type is now `IntegrationRouteData`, which contains a subset of the `RouteData` type. The fields `isIndex` and `fallbackRoutes` were removed.

#### What should I do?
 Section titled “What should I do?”
 Update your adapter to change the type of `entryPoints` from `RouteData` to `IntegrationRouteData`.

 ` import type {RouteData} from ' astro ' ; import type {IntegrationRouteData} from " astro "
 function useRoute ( route : RouteData ) { function useRoute ( route : IntegrationRouteData ) { } `

### Changed: `distURL` is now an array (Integrations API)
 Section titled “Changed: distURL is now an array (Integrations API)”

 Implementation PR: send `IntegrationRouteData` to integrations (#11864)

 In Astro v4.x, `RouteData.distURL` was `undefined` or a `URL`.

Astro v5.0 updates the shape of `IntegrationRouteData.distURL` to be `undefined` or an array of `URL`s. This fixes a previous error because a route can generate multiple files on disk, especially when using dynamic routes such as `[slug]` or `[...slug]`.

#### What should I do?
 Section titled “What should I do?”
 Update your code to handle `IntegrationRouteData.distURL` as an array.

 ` if ( route . distURL ) { if ( route . distURL . endsWith ( ' index.html ' )) { // do something } for ( const url of route . distURL ) { if ( url . endsWith ( ' index.html ' )) { // do something } } } `

 See the API reference for `distURL` .

### Changed: Arguments passed to `app.render()` (Adapter API)
 Section titled “Changed: Arguments passed to app.render() (Adapter API)”

 Implementation PR: TODOs (#11987)

 In Astro 4.x, The Adapter API method `app.render()` could receive three arguments: a mandatory `request`, an object of options or a `routeData` object, and `locals`.

Astro 5.0 combines these last two arguments into a single options argument named `renderOptions`.

#### What should I do?
 Section titled “What should I do?”
 Pass an object as the second argument to `app.render()`, which can include `routeData` and `locals` as properties.

 ` const response = await app . render ( request , routeData , locals ); const response = await app . render ( request , { routeData , locals } ); `

 See the Adapter API reference for `renderOptions` .

### Changed: Properties on `supportedAstroFeatures` (Adapter API)
 Section titled “Changed: Properties on supportedAstroFeatures (Adapter API)”

 Implementation PR: rework supportedAstroFeatures (#11806)

 In Astro 4.x, `supportedAstroFeatures`, which allows adapter authors to specify which features their integration supports, included an `assets` property to specify which of Astro’s image services were supported.

Astro 5.0 replaces this property with a dedicated `sharpImageService` property, used to determine whether the adapter is compatible with the built-in sharp image service.

v5.0 also adds a new `limited` value for the different properties of `supportedAstroFeatures` for adapters, which indicates that the adapter is compatible with the feature, but with some limitations. This is useful for adapters that support a feature, but not in all cases or with all options.

Additionally, the value of the different properties on `supportedAstroFeatures` for adapters can now be objects, with `support` and `message` properties. The content of the `message` property will show a helpful message in the Astro CLI when the adapter is not compatible with a feature. This is notably useful with the new `limited` value, to explain to the user why support is limited.

#### What should I do?
 Section titled “What should I do?”
 If you were using the `assets` property, remove this as it is no longer available. To specify that your adapter supports the built-in sharp image service, replace this with `sharpImageService`.

You may also wish to update your supported features with the new `limited` option and include a message about your adapter’s support.

 my-adapter.mjs ` supportedAstroFeatures: { assets: { supportKind: " stable " , isSharpCompatible: true , isSquooshCompatible: true , }, sharpImageService: { support: " limited " , message: ' This adapter supports the built-in sharp image service, but with some limitations. ' } } `

 Read more about specifying supported Astro features in an adapter .

### Removed: Deprecated definition shape for dev toolbar apps (Dev Toolbar API)
 Section titled “Removed: Deprecated definition shape for dev toolbar apps (Dev Toolbar API)”

 Implementation PR: Remove deprecated dev toolbar app shape (#11987)

 In Astro 4.x, when building a dev toolbar app, it was still possible to use the previously deprecated `addDevToolbarApp(string);` signature. The `id`, `title`, and `icon` properties to define the app were then made available through the default export of the app’s `entrypoint`.

Astro 5.0 completely removes this option entirely in favor of the current object shape when defining a dev toolbar app in an integration that’s more intuitive and allows Astro to provide better errors when toolbar apps fail to load correctly.

#### What should I do?
 Section titled “What should I do?”
 If you were using the deprecated shape, update your dev toolbar app to use the new shape:

 my-integration.mjs ` // Old shape addDevToolbarApp ( " ./my-dev-toolbar-app.mjs " );
 // New shape addDevToolbarApp ({ id: " my-app " , name: " My App " , icon: " &#x3C;svg>...&#x3C;/svg> " , entrypoint: " ./my-dev-toolbar-app.mjs " , }); ` ... &#x22;, entrypoint: &#x22;./my-dev-toolbar-app.mjs&#x22;,});">
 my-dev-toolbar-app.mjs
```
` export default { id: ' my-dev-toolbar-app ' , title: ' My Dev Toolbar App ' , icon: ' 🚀 ' , init () { // ... } } `
```

 Read more about developing a dev toolbar app for Astro using the Dev Toolbar API .

### Removed: configuring TypeScript during `create-astro`
 Section titled “Removed: configuring TypeScript during create-astro”

 Implementation PR: create-astro updates (#12083)

 In Astro v4.x, it was possible to choose between Astro’s three TypeScript settings when creating a new project using `create astro`, either by answering a question or by passing an associated `--typescript` flag with the desired TypeScript setting.

Astro 5.0 updates the `create astro` CLI command to remove the TypeScript question and its associated `--typescript` flag. The “strict” preset is now the default for all new projects created with the command line and it is no longer possible to customize this at that time. However, the TypeScript template can still be changed manually in `tsconfig.json`.

#### What should I do?
 Section titled “What should I do?”
 If you were using the `--typescript` flag with `create-astro`, remove it from your command.

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm create astro@latest -- --template &#x3C;example-name> --typescript strict npm create astro@latest -- --template &#x3C;example-name> ` --typescript strictnpm create astro@latest -- --template ">

 Terminal window
```
` pnpm create astro@latest --template &#x3C;example-name> --typescript strict pnpm create astro@latest --template &#x3C;example-name> `
```
 --typescript strictpnpm create astro@latest --template ">

 Terminal window
```
` yarn create astro --template &#x3C;example-name> --typescript strict yarn create astro --template &#x3C;example-name> `
```
 --typescript strictyarn create astro --template ">

 See all the available `create astro` command flags

## Community Resources
 Section titled “Community Resources”
 Know a good resource for Astro v5.0? Edit this page and add a link below!

## Known Issues
 Section titled “Known Issues”
 Please check Astro’s issues on GitHub for any reported issues, or to file an issue yourself.

 Upgrade Guides

 Contribute

 Community

 Sponsor

## V4

# Upgrade to Astro v4

 This guide will help you migrate from Astro v3 to Astro v4.

Need to upgrade an older project to v3? See our older migration guide .

Need to see the v3 docs? Visit this older version of the docs site (unmaintained v3.6 snapshot) .

## Upgrade Astro
 Section titled “Upgrade Astro”
 Update your project’s version of Astro and all official integrations to the latest versions using your package manager.

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` # Upgrade Astro and official integrations together npx @astrojs/upgrade `

 Terminal window
```
` # Upgrade Astro and official integrations together pnpm dlx @astrojs/upgrade `
```

 Terminal window
```
` # Upgrade Astro and official integrations together yarn dlx @astrojs/upgrade `
```

 You can also upgrade your Astro integrations manually if needed, and you may also need to upgrade other dependencies in your project.

Astro v4.0 includes potentially breaking changes , as well as the removal of some previously deprecated features .

If your project doesn’t work as expected after upgrading to v4.0, check this guide for an overview of all breaking changes and instructions on how to update your codebase.

See the changelog for full release notes.

## Astro v4.0 Experimental Flags Removed
 Section titled “Astro v4.0 Experimental Flags Removed”
 Remove the `devOverlay` experimental flag and move any `i18n` config to the top level in `astro.config.mjs`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ experimental: { devOverlay: true , i18n: { locales: [ " en " , " fr " , " pt-br " , " es " ], defaultLocale: " en " , } }, i18n: { locales: [ " en " , " fr " , " pt-br " , " es " ], defaultLocale: " en " , }, }) `
 These configurations, `i18n` and the renamed `devToolbar`, are now available in Astro v4.0.

Read more about these two exciting features and more in the v4.0 Blog post !

## Upgrades
 Section titled “Upgrades”
 Any major upgrades to Astro’s dependencies may cause breaking changes in your project.

### Upgraded: Vite 5.0
 Section titled “Upgraded: Vite 5.0”
 In Astro v3.0, Vite 4 was used as the development server and production bundler.

Astro v4.0 upgrades from Vite 4 to Vite 5.

#### What should I do?
 Section titled “What should I do?”
 If you are using Vite-specific plugins, configuration, or APIs, check the Vite migration guide for their breaking changes and upgrade your project as needed. There are no breaking changes to Astro itself.

### Upgraded: unified, remark, and rehype dependencies
 Section titled “Upgraded: unified, remark, and rehype dependencies”
 In Astro v3.x, unified v10 and its related compatible remark/rehype packages were used to process Markdown and MDX.

Astro v4.0 upgrades unified to v11 and the other remark/rehype packages to the latest version.

#### What should I do?
 Section titled “What should I do?”
 If you used custom remark/rehype packages, update all of them to the latest version using your package manager to ensure they support unified v11. The packages you are using can be found in `astro.config.mjs`.

There should not be any significant breaking changes if you use actively updated packages, but some packages may not yet be compatible with unified v11.
Visually inspect your Markdown/MDX pages before deploying to ensure your site is functioning as intended.

## Breaking Changes
 Section titled “Breaking Changes”
 The following changes are considered breaking changes in Astro. Breaking changes may or may not provide temporary backwards compatibility, and all documentation is updated to refer to only the current, supported code.

If you need to refer to the documentation for a v3.x project, you can browse this (unmaintained) snapshot of the docs from before v4.0 was released .

### Renamed: `entrypoint` (Integrations API)
 Section titled “Renamed: entrypoint (Integrations API)”
 In Astro v3.x, the property of the `injectRoute` integrations API that specified the route entry point was named `entryPoint`.

Astro v4.0 renames this property to `entrypoint` to be consistent with other Astro APIs. The `entryPoint` property is deprecated but will continue to work and logs a warning prompting you to update your code.

#### What should I do?
 Section titled “What should I do?”
 If you have integrations that use the `injectRoute` API, rename the `entryPoint` property to `entrypoint`. If you’re a library author who wants to support both Astro 3 and 4, you can specify both `entryPoint` and `entrypoint`, in which case, a warning will not be logged.

 ` injectRoute ({ pattern: ' /fancy-dashboard ' , entryPoint: ' @fancy/dashboard/dashboard.astro ' entrypoint : ' @fancy/dashboard/dashboard.astro ' }); `

### Changed: `app.render` signature in Integrations API
 Section titled “Changed: app.render signature in Integrations API”
 In Astro v3.0, the `app.render()` method accepted `routeData` and `locals` as separate, optional arguments.

Astro v4.0 changes the `app.render()` signature. These two properties are now available in a single object. Both the object and these two properties are still optional.

#### What should I do?
 Section titled “What should I do?”
 If you are maintaining an adapter, the current signature will continue to work until the next major version. To migrate to the new signature, pass `routeData` and `locals` as properties of an object instead of as multiple independent arguments.

 ` app . render ( request , routeData , locals ) app . render ( request , { routeData , locals }) `

### Changed: adapters must now specify supported features
 Section titled “Changed: adapters must now specify supported features”
 In Astro v3.x, adapters were not required to specify the features they support.

Astro v4.0 requires adapters to pass the `supportedAstroFeatures{}` property to specify a list of features they support. This property is no longer optional.

#### What should I do?
 Section titled “What should I do?”
 Adapter authors need to pass the `supportedAstroFeatures{}` option to specify a list of features they support.

 my-adapter.mjs ` export default function createIntegration () { return { name: ' @matthewp/my-adapter ' , hooks: { ' astro:config:done ' : ( { setAdapter } ) => { setAdapter ({ name: ' @matthewp/my-adapter ' , serverEntrypoint: ' @matthewp/my-adapter/server.js ' , supportedAstroFeatures: { staticOutput: ' stable ' } }); } , } , }; } ` { setAdapter({ name: &#x27;@matthewp/my-adapter&#x27;, serverEntrypoint: &#x27;@matthewp/my-adapter/server.js&#x27;, supportedAstroFeatures: { staticOutput: &#x27;stable&#x27; } }); }, }, };}">

### Removed: Shiki language `path` property
 Section titled “Removed: Shiki language path property”
 In Astro v3.x, a Shiki language passed to `markdown.shikiConfig.langs` was automatically converted to a Shikiji-compatible language. Shikiji is the internal tooling used by Astro for syntax highlighting.

Astro v4.0 removes support for the `path` property of a Shiki language, which was confusing to configure. It is replaced by an import which can be passed to `langs` directly.

#### What should I do?
 Section titled “What should I do?”
 The language JSON file should be imported and passed to the option instead.

 astro.config.js ` import customLang from ' ./custom.tmLanguage.json '
 export default defineConfig ({ markdown: { shikiConfig: { langs: [ { path: ' ../../custom.tmLanguage.json ' }, customLang , ], }, }, }) `

## Deprecated
 Section titled “Deprecated”
 The following deprecated features are no longer supported and are no longer documented. Please update your project accordingly.

Some deprecated features may temporarily continue to function until they are completely removed. Others may silently have no effect, or throw an error prompting you to update your code.

### Deprecated: `handleForms` for View Transitions `submit` events
 Section titled “Deprecated: handleForms for View Transitions submit events”
 In Astro v3.x, projects using the `&#x3C;ViewTransitions />` component were required to opt-in to handling `submit` events for `form` elements. This was done by passing a `handleForms` prop.

Astro v4.0 handles `submit` events for `form` elements by default when `&#x3C;ViewTransitions />` are used. The `handleForms` prop has been deprecated and no longer has any effect.

#### What should I do?
 Section titled “What should I do?”
 Remove the `handleForms` property from your `ViewTransitions` component. It is no longer necessary.

 src/pages/index.astro ` --- import { ViewTransitions } from " astro:transitions " ; --- &#x3C; html > &#x3C; head > &#x3C; ViewTransitions handleForms /> &#x3C;/ head > &#x3C; body > &#x3C;!-- stuff here --> &#x3C;/ body > &#x3C;/ html > `        ">
 To opt out of `submit` event handling, add the `data-astro-reload` attribute to relevant `form` elements.

 src/components/Form.astro ` &#x3C; form action = " /contact " data-astro-reload > &#x3C;!-- --> &#x3C;/ form > `   ">

## Previously deprecated features now removed
 Section titled “Previously deprecated features now removed”
 The following deprecated features have now been entirely removed from the code base and can no longer be used. Some of these features may have continued to work in your project even after deprecation. Others may have silently had no effect.

Projects now containing these removed features will be unable to build, and there will no longer be any supporting documentation prompting you to remove these features.

### Removed: returning simple objects from endpoints
 Section titled “Removed: returning simple objects from endpoints”
 In Astro v3.x, returning simple objects from endpoints was deprecated, but was still supported to maintain compatibility with Astro v2. A `ResponseWithEncoding` utility was also provided to ease the migration.

Astro v4.0 removes support for simple objects and requires endpoints to always return a `Response`. The `ResponseWithEncoding` utility is also removed in favor of a proper `Response` type.

#### What should I do?
 Section titled “What should I do?”
 Update your endpoints to return a `Response` object directly.

 ` export async function GET () { return { body: { " title " : " Bob's blog " }}; return new Response ( JSON . stringify ({ " title " : " Bob's blog " })); } `
 To remove usage of `ResponseWithEncoding`, refactor your code to use an `ArrayBuffer` instead:

 ` export async function GET () { const file = await fs . readFile ( ' ./bob.png ' ); return new ResponseWithEncoding (file . toString ( ' binary ' ) , undefined , ' binary ' ); return new Response (file . buffer ); } `

### Removed: `build.split` and `build.excludeMiddleware`
 Section titled “Removed: build.split and build.excludeMiddleware”
 In Astro v3.0, `build.split` and `build.excludeMiddleware` build config options were deprecated and replaced with adapter configuration options to perform the same tasks.

Astro v4.0 removes these properties entirely.

#### What should I do?
 Section titled “What should I do?”
 If you are using the deprecated `build.split` or `build.excludeMiddleware`, you must now remove them as these no longer exist.

Please see the v3 migration guide to update these deprecated middleware properties with adapter configurations.

### Removed: `Astro.request.params`
 Section titled “Removed: Astro.request.params”
 In Astro v3.0, the `Astro.request.params` API was deprecated, but preserved for backwards compatibility.

Astro v4.0 removes this option entirely.

#### What should I do?
 Section titled “What should I do?”
 Update all occurrences to `Astro.params` , which is the supported replacement.

 ` const { id } = Astro.request.params; const { id } = Astro.params; `

### Removed: `markdown.drafts`
 Section titled “Removed: markdown.drafts”
 In Astro v3.0, using `markdown.drafts` to control the building of draft posts was deprecated.

Astro v4.0 removes this option entirely.

#### What should I do?
 Section titled “What should I do?”
 If you are using the deprecated `markdown.drafts`, you must now remove it as it no longer exists.

To continue to mark some pages in your project as drafts, migrate to content collections and manually filter out pages with the `draft: true` frontmatter property instead.

### Removed: `getHeaders()`
 Section titled “Removed: getHeaders()”
 In Astro v3.0, the `getHeaders()` Markdown export was deprecated and replaced with `getHeadings()`.

Astro v4.0 removes this option entirely.

#### What should I do?
 Section titled “What should I do?”
 If you are using the deprecated `getHeaders()`, you must now remove it as it no longer exists. Replace any instances with `getHeadings()`, which is the supported replacement.

 ` const posts = await Astro . glob ( ' ../content/blog/*.mdx ' ); const firstPostHeadings = posts . at ( 0 ) . getHeaders (); const firstPostHeadings = posts . at ( 0 ) . getHeadings (); `

### Removed: using `rss` in `getStaticPaths()`
 Section titled “Removed: using rss in getStaticPaths()”
 In Astro v3.0, using the deprecated `rss` helper in `getStaticPaths()` would throw an error.

Astro v4.0 removes this helper entirely.

#### What should I do?
 Section titled “What should I do?”
 If you are using the unsupported method for generating RSS feeds, you must now use the `@astrojs/rss` integration for a complete RSS setup.

### Removed: lowercase HTTP method names
 Section titled “Removed: lowercase HTTP method names”
 In Astro v3.0, using lowercase HTTP request method names (`get`, `post`, `put`, `all`, `del`) was deprecated.

Astro v4.0 removes support for lowercase names entirely. All HTTP request methods must now be written using uppercase.

#### What should I do?
 Section titled “What should I do?”
 If you are using the deprecated lowercase names, you must now replace them with their uppercase equivalents.

Please see the v3 migration guide for guidance using uppercase HTTP request methods .

### Removed: 301 redirects when missing a `base` prefix
 Section titled “Removed: 301 redirects when missing a base prefix”
 In Astro v3.x, the Astro preview server returned a 301 redirect when accessing public directory assets without a base path.

Astro v4.0 returns a 404 status without a base path prefix for public directory assets when the preview server is running, matching the behavior of the dev server.

#### What should I do?
 Section titled “What should I do?”
 When using the Astro preview server, all of your static asset imports and URLs from the public directory must have the base value prefixed to the path.

The following example shows the `src` attribute required to display an image from the public folder when `base: '/docs'` is configured:

 src/pages/index.astro ` // To access public/images/my-image.png:
 &#x3C; img src = " /docs /images/my-image.png " alt = "" > ` ">

### Removed: `astro/client-image` auto-conversion
 Section titled “Removed: astro/client-image auto-conversion”
 In Astro v3.x, the `astro/client-image` type (used for the deprecated image integration) was removed but was auto-converted to the default Astro type `astro/client` if found in your `env.d.ts` file.

Astro v4.0 ignores `astro/client-image` and will no longer update `env.d.ts` for you automatically.

#### What should I do?
 Section titled “What should I do?”
 If you had types configured for `@astrojs/image` in `src/env.d.ts` and upgrading to v3.0 did not automatically convert the type for you, replace the `astro/client-image` type manually with `astro/client`.

 src/env.d.ts ` /// &#x3C;reference types="astro/client-image" /> /// &#x3C;reference types="astro/client" /> `  /// ">

## Community Resources
 Section titled “Community Resources”
 Know a good resource for Astro v4.0? Edit this page and add a link below!

## Known Issues
 Section titled “Known Issues”
 Please check Astro’s issues on GitHub for any reported issues, or to file an issue yourself.

 Upgrade Guides

 Contribute

 Community

 Sponsor