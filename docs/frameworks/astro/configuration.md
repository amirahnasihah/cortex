# Astro - Configuration


## Configuring Astro

# Configuration overview

 Astro is a flexible, unopinionated framework that allows you to configure your project in many different ways. This means that getting started with a new project might feel overwhelming: there is no “one best way” to set up your Astro project!

The guides in this “Configuration” section will help you familiarize yourself with the various files that allow you to configure and customize aspects of your project and development environment.

If this is your first Astro project, or if it’s been a while since you’ve set up a new project, use the following guides and reference in the documentation for assistance.

## The Astro config File
 Section titled “The Astro config File”
 The Astro config file is a JavaScript file included at the root of every starter project:

 astro.config.mjs ` import { defineConfig } from " astro/config " ;
 export default defineConfig ({ // your configuration options here... }); `
 It is only required if you have something to configure, but most projects will use this file. The `defineConfig()` helper provides automatic IntelliSense in your IDE and is where you will add all your configuration options to tell Astro how to build and render your project to HTML.

We recommend using the default file format `.mjs` in most cases, or `.ts` if you want to write TypeScript in your config file. However, `astro.config.js` is also supported.

 Read Astro’s configuration reference for a full overview of all supported configuration options.

## The TypeScript config File
 Section titled “The TypeScript config File”
 Every Astro starter project includes a `tsconfig.json` file in your project. Astro’s component script is TypeScript, which provides Astro’s editor tooling and allows you to optionally add syntax to your JavaScript for type checking of your own project code.

Use the `tsconfig.json` file to configure the TypeScript template that will perform type checks on your code, configure TypeScript plugins, set import aliases, and more.

 Read Astro’s TypeScript guide for a full overview of TypeScript options and Astro’s built-in utility types.

## Development Experience
 Section titled “Development Experience”
 While you work in development mode, you can take advantage of your code editor and other tools to improve the Astro developer experience.

Astro provides its own official VS Code extension and is compatible with several other popular editor tools. Astro also provides a customizable toolbar that displays in your browser preview while the dev server is running. You can install and even build your own toolbar apps for additional functionality.

 Read Astro’s guides to editor setup options and using the dev toolbar to learn how to customize your development experience.

## Common new project tasks
 Section titled “Common new project tasks”
 Here are some first steps you might choose to take with a new Astro project.

### Add your deployment domain
 Section titled “Add your deployment domain”
 For generating your sitemap and creating canonical URLs, configure your deployment URL in the `site` option. If you are deploying to a path (e.g. `www.example.com/docs`), you can also configure a `base` for the root of your project.

Additionally, different deployment hosts may have different behavior regarding trailing slashes at the end of your URLs. (e.g. `example.com/about` vs `example.com/about/`). Once your site is deployed, you may need to configure your `trailingSlash` preference.

 astro.config.mjs ` import { defineConfig } from " astro/config " ;
 export default defineConfig ({ site: " https://www.example.com " , base: " /docs " , trailingSlash: " always " , }); `

### Add site metadata
 Section titled “Add site metadata”
 Astro does not use its configuration file for common SEO or meta data, only for information required to build your project code and render it to HTML.

Instead, this information is added to your page `&#x3C;head>` using standard HTML `&#x3C;link>` and `&#x3C;meta>` tags, just as if you were writing plain HTML pages.

One common pattern for Astro sites is to create a `&#x3C;Head />` `.astro` component that can be added to a common layout component so it can apply to all your pages.

 src/components/MainLayout.astro ` --- import Head from " ./Head.astro " ;
 const { ... props } = Astro . props ; --- &#x3C; html > &#x3C; head > &#x3C; meta charset = " utf-8 " > &#x3C; Head /> &#x3C;!-- Additional head elements --> &#x3C;/ head > &#x3C; body > &#x3C;!-- Page content goes here --> &#x3C;/ body > &#x3C;/ html > `          ">
 Because `Head.astro` is just a regular Astro component, you can import files and receive props passed from other components, such as a specific page title.

 src/components/Head.astro
```
` --- import Favicon from " ../assets/Favicon.astro " ; import SomeOtherTags from " ./SomeOtherTags.astro " ;
 const { title = " My Astro Website " , ... props } = Astro . props ; --- &#x3C; link rel = " sitemap " href = " /sitemap-index.xml " > &#x3C; title > { title } &#x3C;/ title > &#x3C; meta name = " description " content = " Welcome to my new Astro site! " >
 &#x3C;!-- Web analytics --> &#x3C; script data-goatcounter = " https://my-account.goatcounter.com/count " async src = " //gc.zgo.at/count.js " >&#x3C;/ script >
 &#x3C;!-- Open Graph tags --> &#x3C; meta property = " og:title " content = " My New Astro Website " /> &#x3C; meta property = " og:type " content = " website " /> &#x3C; meta property = " og:url " content = " http://www.example.com/ " /> &#x3C; meta property = " og:description " content = " Welcome to my new Astro site! " /> &#x3C; meta property = " og:image " content = " https://www.example.com/_astro/seo-banner.BZD7kegZ.webp " > &#x3C; meta property = " og:image:alt " content = "" >
 &#x3C; SomeOtherTags />
 &#x3C; Favicon /> `
```
  {title}          ">

 Learn

 Contribute

 Community

 Sponsor

## Editor Setup

# Editor setup

 Customize your code editor to improve the Astro developer experience and unlock new features.

## VS Code
 Section titled “VS Code”
 VS Code is a popular code editor for web developers, built by Microsoft. The VS Code engine also powers popular in-browser code editors like GitHub Codespaces .

Astro works with any code editor. However, VS Code is our recommended editor for Astro projects. We maintain an official Astro VS Code Extension that unlocks several key features and developer experience improvements for Astro projects.

- Syntax highlighting for `.astro` files.

- TypeScript type information for `.astro` files.

- VS Code Intellisense for code completion, hints and more.

To get started, install the Astro VS Code Extension today.

 See how to set up TypeScript in your Astro project.

## Zed
 Section titled “Zed”
 Zed is a high-performance, multiplayer code editor that is optimized for speed and large projects. Their Astro extension includes features like syntax highlighting for `.astro` files, code completion, formatting, diagnostics, and go-to-definition.

## JetBrains IDEs
 Section titled “JetBrains IDEs”
 Webstorm is a JavaScript and TypeScript IDE that added support for the Astro Language Server in version 2024.2. This update brings features like syntax highlighting, code completion, and formatting.

Install the official plugin through JetBrains Marketplace or by searching for “Astro” in the IDE’s Plugins tab. You can toggle the language server in `Settings | Languages &#x26; Frameworks | TypeScript | Astro`.

For more information on Astro support in Webstorm, check out the official Webstorm Astro Documentation .

## Other Code Editors
 Section titled “Other Code Editors”
 Our amazing community maintains several extensions for other popular editors, including:

- VS Code Extension on Open VSX Official - The official Astro VS Code Extension, available on the Open VSX registry for editors like Cursor or VSCodium .

- Vim Plugin Community - Provides syntax highlighting, indentation, and code folding support for Astro inside of Vim or Neovim

- Neovim LSP and TreeSitter Plugins Community - Provides syntax highlighting, treesitter parsing, and code completion for Astro inside of Neovim

- Emacs - See instructions for Configuring Emacs and Eglot Community to work with Astro

- Astro syntax highlighting for Sublime Text Community - The Astro package for Sublime Text, available on the Sublime Text package manager.

- Nova Extension Community - Provides syntax highlighting and code completion for Astro inside of Nova

## In-Browser Editors
 Section titled “In-Browser Editors”
 In addition to local editors, Astro also runs well on in-browser hosted editors, including:

- StackBlitz and CodeSandbox - online editors that run in your browser, with built-in syntax highlighting support for `.astro` files. No installation or configuration required!

- GitHub.dev - allows you to install the Astro VS Code extension as a web extension , which gives you access to only some of the full extension features. Currently, only syntax highlighting is supported.

## Other tools
 Section titled “Other tools”

### ESLint
 Section titled “ESLint”
 ESLint is a popular linter for JavaScript and JSX. For Astro support, a community maintained plugin can be installed.

See the project’s User Guide for more information on how to install and set up ESLint for your project.

### Stylelint
 Section titled “Stylelint”
 Stylelint is a popular linter for CSS. A community maintained Stylelint configuration provides Astro support.

Installation instructions, editor integration, and additional information can be found in the project’s README.

### Biome
 Section titled “Biome”
 Biome is an all-in-one linter and formatter for the web. Biome currently has experimental support for `.astro` files , and can be used to lint and format the frontmatter in `.astro` files.

### Prettier
 Section titled “Prettier”
 Prettier is a popular formatter for JavaScript, HTML, CSS, and more. If you’re using the Astro VS Code Extension , code formatting with Prettier is included.

To add support for formatting `.astro` files outside of the editor (e.g. CLI) or inside editors that don’t support our editor tooling, install the official Astro Prettier plugin .

-
Install `prettier` and `prettier-plugin-astro`.

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npm install --save-dev --save-exact prettier prettier-plugin-astro `

 Terminal window
```
` pnpm add --save-dev --save-exact prettier prettier-plugin-astro `
```

 Terminal window
```
` yarn add --dev --exact prettier prettier-plugin-astro `
```

-
 Create a `.prettierrc` configuration file (or `.prettierrc.json`, `.prettierrc.mjs`, or other supported formats ) in the root of your project and add `prettier-plugin-astro` to it.

In this file, also manually specify the parser for Astro files.

 .prettierrc ` { "plugins" : [ " prettier-plugin-astro " ], "overrides" : [ { "files" : " *.astro " , "options" : { "parser" : " astro " } } ] } `

-
 Optionally, install other Prettier plugins for your project, and add them to the configuration file. These additional plugins may need to be listed in a specific order. For example, if you use Tailwind, `prettier-plugin-tailwindcss` must be the last Prettier plugin in the plugins array .

 .prettierrc ` { "plugins" : [ " prettier-plugin-astro " , " prettier-plugin-tailwindcss " // needs to be last ], "overrides" : [ { "files" : " *.astro " , "options" : { "parser" : " astro " } } ] } `

-
 Run the following command in your terminal to format your files.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npx prettier . --write `

 Terminal window
```
` pnpm exec prettier . --write `
```

 Terminal window
```
` yarn exec prettier . --write `
```

 See the Prettier plugin’s README for more information about its supported options, how to set up Prettier inside VS Code, and more.

### dprint
 Section titled “dprint”
 dprint is a highly-configurable code formatter that supports many languages, including JavaScript, TypeScript, CSS, and more. Support for `.astro` files can be added using the markup_fmt plugin .

 Learn

 Contribute

 Community

 Sponsor

## Typescript

# TypeScript

 Astro ships with built-in support for TypeScript . You can import `.ts` and `.tsx` files in your Astro project, write TypeScript code directly inside your Astro component , and even use an `astro.config.ts` file for your Astro configuration if you like.

Using TypeScript, you can prevent errors at runtime by defining the shapes of objects and components in your code. For example, if you use TypeScript to type your component’s props , you’ll get an error in your editor if you set a prop that your component doesn’t accept.

You don’t need to write TypeScript code in your Astro projects to benefit from it. Astro always treats your component code as TypeScript, and the Astro VS Code Extension will infer as much as it can to provide autocompletion, hints, and errors in your editor.

The Astro dev server won’t perform any type checking, but you can use a separate script to check for type errors from the command line.

## Setup
 Section titled “Setup”
 Astro starter projects include a `tsconfig.json` file in your project. Even if you don’t write TypeScript code, this file is important so that tools like Astro and VS Code know how to understand your project. Some features (like npm package imports) aren’t fully supported in the editor without a `tsconfig.json` file. If you install Astro manually, be sure to create this file yourself.

### TSConfig templates
 Section titled “TSConfig templates”
 Three extensible `tsconfig.json` templates are included in Astro: `base`, `strict`, and `strictest`. The `base` template enables support for modern JavaScript features and is also used as a basis for the other templates. We recommend using `strict` or `strictest` if you plan to write TypeScript in your project. You can view and compare the three template configurations at astro/tsconfigs/ .

To inherit from one of the templates, use the `extends` setting :

 - tsconfig.json ` { "extends" : " astro/tsconfigs/base " } `
 Additionally, we recommend setting `include` and `exclude` as follows to benefit from Astro types and avoid checking built files:

 tsconfig.json ` { "extends" : " astro/tsconfigs/base " , "include" : [ " .astro/types.d.ts " , " **/* " ], "exclude" : [ " dist " ] } `

### TypeScript editor plugin
 Section titled “TypeScript editor plugin”
 The Astro TypeScript plugin can be installed separately when you are not using the official Astro VS Code extension . This plugin is automatically installed and configured by the VS Code extension, and you do not need to install both.

This plugin runs only in the editor. When running `tsc` in the terminal, `.astro` files are ignored entirely. Instead, you can use the `astro check` CLI command to check both `.astro` and `.ts` files.

This plugin also supports importing `.astro` files from `.ts` files (which can be useful for re-exporting).

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/ts-plugin `

 Terminal window
```
` pnpm add @astrojs/ts-plugin `
```

 Terminal window
```
` yarn add @astrojs/ts-plugin `
```

 Then, add the following to your `tsconfig.json`:

 tsconfig.json ` { "compilerOptions" : { "plugins" : [ { "name" : " @astrojs/ts-plugin " }, ], } } `
 To check that the plugin is working, create a `.ts` file and import an Astro component into it. You should have no warning messages from your editor.

### UI Frameworks
 Section titled “UI Frameworks”
 If your project uses a UI framework , additional settings depending on the framework might be needed. Please see your framework’s TypeScript documentation for more information. ( Vue , React , Preact , Solid , Svelte )

## Type Imports
 Section titled “Type Imports”
 Use explicit type imports and exports whenever possible.

 ` import { SomeType } from " ./script " ; import type { SomeType } from " ./script " ; `
 This way, you avoid edge cases where Astro’s bundler may try to incorrectly bundle your imported types as if they were JavaScript.

You can configure TypeScript to enforce type imports in your `tsconfig.json` file. Set `verbatimModuleSyntax` to `true`. TypeScript will check your imports and tell you when `import type` should be used. This setting is enabled by default in all our presets.

 tsconfig.json ` { "compilerOptions" : { "verbatimModuleSyntax" : true } } `

## Import Aliases
 Section titled “Import Aliases”
 Astro supports import aliases that you define in your `tsconfig.json` `paths` configuration. Read our imports guide to learn more.

 src/pages/about/nate.astro ` --- import HelloWorld from " @components /HelloWorld.astro " ; import Layout from " @layouts /Layout.astro " ; --- `
 tsconfig.json
```
` { "compilerOptions" : { "paths" : { "@components/*" : [ " ./src/components/* " ], "@layouts/*" : [ " ./src/layouts/* " ] } } } `
```

## Extending global types
 Section titled “Extending global types”
 You can create `src/env.d.ts` as a convention for adding custom types declarations, or to benefit from Astro types if you don’t have a `tsconfig.json`:

 src/env.d.ts ` // Custom types declarations declare var myString : string ;
 // Astro types, not necessary if you already have a `tsconfig.json` /// &#x3C; reference path = " ../.astro/types.d.ts " /> ` ">

### `window` and `globalThis`
 Section titled “window and globalThis”
 You may want to add a property to the global object. You can do this by adding top-level declarations using the `declare` keyword to your `env.d.ts` file:

 src/env.d.ts ` declare var myString : string ; declare function myFunction () : boolean ; `
 This will provide typing to `globalThis.myString` and `globalThis.myFunction`, as well as `window.myString` and `window.myFunction`.

Note that `window` is only available in client-side code. `globalThis` is available both server-side and client-side, but its server-side value won’t be shared with the client.

If you only want to type a property on the `window` object, provide a `Window` interface instead:

 src/env.d.ts ` interface Window { myFunction () : boolean ; } `

### Add non-standard attributes
 Section titled “Add non-standard attributes”
 You may want to define a type for custom attributes or CSS properties. You can extend the default JSX definitions to add non-standard attributes by redeclaring the `astroHTML.JSX` namespace in a `.d.ts` file.

 src/env.d.ts ` declare namespace astroHTML . JSX { interface HTMLAttributes { " data-count " ?: number ; " data-label " ?: string ; }
 // Add a CSS custom property to the style object interface CSSProperties { " --theme-color " ?: " black " | " white " ; } } `

### Using imports
 Section titled “Using imports”
 You may want to extend global types by reusing types declared elsewhere in your project or from an external library. To do this, use dynamic imports :

 src/env.d.ts ` type Product = { id : string ; name : string ; price : number ; };
 declare namespace App { interface Locals { orders : Map &#x3C; string , Product []> session : import ( " ./lib/server/session " ). Session | null ; user : import ( " my-external-library " ). User ; } } `  session: import(&#x22;./lib/server/session&#x22;).Session | null; user: import(&#x22;my-external-library&#x22;).User; }}">
 A `.d.ts` file is an ambient module declaration. While its syntax is similar to ES modules, these files do not allow top-level imports/exports. If TypeScript encounters one, the file will be considered a module augmentation and this will break your global types.

## Component Props
 Section titled “Component Props”
 Astro supports typing your component props via TypeScript. To enable, add a TypeScript `Props` interface to your component frontmatter. An `export` statement may be used, but is not necessary. The Astro VS Code Extension will automatically look for the `Props` interface and give you proper TS support when you use that component inside another template.

 src/components/HelloProps.astro ` --- interface Props { name : string ; greeting ?: string ; }
 const { greeting = " Hello " , name } = Astro . props ; --- &#x3C; h2 > { greeting } , { name } ! &#x3C;/ h2 > `

### Common prop type patterns
 Section titled “Common prop type patterns”

- If your component takes no props or slotted content, you can use `type Props = Record&#x3C;string, never>`.

- If your component must be passed children to its default slot, you can enforce this by using `type Props = { children: any; };`.

## Type Utilities
 Section titled “Type Utilities”

 Added in:
 `astro@1.6.0`

Astro comes with some built-in utility types for common prop type patterns. These are available under the `astro/types` entrypoint.

### Built-in HTML attributes
 Section titled “Built-in HTML attributes”
 Astro provides the `HTMLAttributes` type to check that your markup is using valid HTML attributes. You can use these types to help build component props.

For example, if you were building a `&#x3C;Link>` component, you could do the following to mirror the default HTML attributes for `&#x3C;a>` tags in your component’s prop types.

 src/components/Link.astro ` --- import type { HTMLAttributes } from " astro/types " ;
 // use a `type` type Props = HTMLAttributes &#x3C; " a " >;
 // or extend with an `interface` interface Props extends HTMLAttributes &#x3C; " a " > { myProp ?: boolean ; }
 const { href , ... attrs } = Astro . props ; --- &#x3C; a href = { href } { ... attrs }> &#x3C; slot /> &#x3C;/ a > ` ;// or extend with an &#x60;interface&#x60;interface Props extends HTMLAttributes { myProp?: boolean;}const { href, ...attrs } = Astro.props;---   ">

### `ComponentProps` type
 Section titled “ComponentProps type”

 Added in:
 `astro@4.3.0`

This type export allows you to reference the `Props` accepted by another component, even if that component doesn’t export that `Props` type directly.

The following example shows using the `ComponentProps` utility from `astro/types` to reference a `&#x3C;Button />` component’s `Props` types:

 src/pages/index.astro ` --- import type { ComponentProps } from " astro/types " ; import Button from " ./Button.astro " ;
 type ButtonProps = ComponentProps &#x3C; typeof Button>; --- ` ;---">

### Polymorphic type
 Section titled “Polymorphic type”

 Added in:
 `astro@2.5.0`

Astro includes a helper to make it easier to build components that can render as different HTML elements with full type safety. This is useful for components like `&#x3C;Link>` that can render as either `&#x3C;a>` or `&#x3C;button>` depending on the props passed to it.

The example below implements a fully-typed, polymorphic component that can render as any HTML element. The `HTMLTag` type is used to ensure that the `as` prop is a valid HTML element.

 ` --- import type { HTMLTag, Polymorphic } from " astro/types " ;
 type Props&#x3C; Tag extends HTMLTag > = Polymorphic &#x3C;{ as : Tag }>;
 const { as : Tag , ... props } = Astro . props ; --- &#x3C; Tag { ... props } /> ` = Polymorphic ;const { as: Tag, ...props } = Astro.props;--- ">

### Infer `getStaticPaths()` types
 Section titled “Infer getStaticPaths() types”

 Added in:
 `astro@2.1.0`

Astro includes helpers for working with the types returned by your `getStaticPaths()` function for dynamic routes.

You can get the type of `Astro.params` with `InferGetStaticParamsType` and the type of `Astro.props` with `InferGetStaticPropsType` or you can use `GetStaticPaths` to infer both at once:

 src/pages/posts/[...id].astro ` --- import type { InferGetStaticParamsType, InferGetStaticPropsType, GetStaticPaths, } from " astro " ;
 export const getStaticPaths = ( async () => { const posts = await getCollection ( " blog " ) ; return posts . map ( ( post ) => { return { params: { id: post . id }, props: { draft: post . data . draft , title: post . data . title }, }; } ) ; } ) satisfies GetStaticPaths ;
 type Params = InferGetStaticParamsType &#x3C; typeof getStaticPaths>; type Props = InferGetStaticPropsType &#x3C; typeof getStaticPaths>;
 const { id } = Astro . params as Params ; // ^? { id: string; }
 const { title } = Astro . props ; // ^? { draft: boolean; title: string; } --- ` { const posts = await getCollection(&#x22;blog&#x22;); return posts.map((post) => { return { params: { id: post.id }, props: { draft: post.data.draft, title: post.data.title }, }; });}) satisfies GetStaticPaths;type Params = InferGetStaticParamsType ;type Props = InferGetStaticPropsType ;const { id } = Astro.params as Params;// ^? { id: string; }const { title } = Astro.props;// ^? { draft: boolean; title: string; }---">

## Type checking
 Section titled “Type checking”
 To see type errors in your editor, please make sure that you have the Astro VS Code extension installed. Please note that the `astro start` and `astro build` commands will transpile the code with esbuild, but will not run any type checking. To prevent your code from building if it contains TypeScript errors, change your “build” script in `package.json` to the following:

 package.json ` { "scripts" : { "build" : " astro build " , "build" : " astro check &#x26;&#x26; astro build " , }, } `

 Read more about `.ts` file imports in Astro.

 Read more about TypeScript Configuration .

## Troubleshooting
 Section titled “Troubleshooting”

### Errors typing multiple JSX frameworks at the same time
 Section titled “Errors typing multiple JSX frameworks at the same time”
 An issue may arise when using multiple JSX frameworks in the same project, as each framework requires different, sometimes conflicting, settings inside `tsconfig.json`.

 Solution : Set the `jsxImportSource` setting to `react` (default), `preact` or `solid-js` depending on your most-used framework. Then, use a pragma comment inside any conflicting file from a different framework.

For the default setting of `jsxImportSource: react`, you would use:

```
` // For Preact /** @jsxImportSource preact */
 // For Solid /** @jsxImportSource solid-js */ `
```

 Learn

 Contribute

 Community

 Sponsor

## Environment Variables

# Using environment variables

 Astro gives you access to Vite’s built-in environment variables support and includes some default environment variables for your project that allow you to access configuration values for your current project (e.g. `site`, `base`), whether your project is running in development or production, and more.

Astro also provides a way to use and organize your environment variables with type safety . It is available for use inside the Astro context (e.g. Astro components, routes and endpoints, UI framework components, middleware), and managed with a schema in your Astro configuration .

## Vite’s built-in support
 Section titled “Vite’s built-in support”
 Astro uses Vite’s built-in support for environment variables, which are statically replaced at build time, and lets you use any of its methods to work with them.

Note that while all environment variables are available in server-side code, only environment variables prefixed with `PUBLIC_` are available in client-side code for security purposes.

 - .env ` SECRET_PASSWORD =password123 PUBLIC_ANYBODY =there `
 In this example, `PUBLIC_ANYBODY` (accessible via `import.meta.env.PUBLIC_ANYBODY`) will be available in server or client code, while `SECRET_PASSWORD` (accessible via `import.meta.env.SECRET_PASSWORD`) will be server-side only.

### IntelliSense for TypeScript
 Section titled “IntelliSense for TypeScript”
 By default, Astro provides a type definition for `import.meta.env` in `astro/client.d.ts`.

While you can define more custom env variables in `.env.[mode]` files, you may want to get TypeScript IntelliSense for user-defined env variables which are prefixed with `PUBLIC_`.

To achieve this, you can create an `env.d.ts` in `src/` to extend the global types and configure `ImportMetaEnv` like this:

 src/env.d.ts ` interface ImportMetaEnv { readonly DB_PASSWORD : string ; readonly PUBLIC_POKEAPI : string ; // more env variables... }
 interface ImportMeta { readonly env : ImportMetaEnv ; } `

## Default environment variables
 Section titled “Default environment variables”
 Astro includes a few environment variables out of the box:

 `import.meta.env.MODE`: The mode your site is running in. This is `development` when running `astro dev` and `production` when running `astro build`.

- `import.meta.env.PROD`: `true` if your site is running in production; `false` otherwise.

- `import.meta.env.DEV`: `true` if your site is running in development; `false` otherwise. Always the opposite of `import.meta.env.PROD`.

- `import.meta.env.BASE_URL`: The base URL your site is being served from. This is determined by the `base` config option .

- `import.meta.env.SITE`: This is set to the `site` option specified in your project’s `astro.config`.

Use them like any other environment variable.

 ` const isProd = import. meta . env . PROD ; const isDev = import. meta . env . DEV ; `

## Setting environment variables
 Section titled “Setting environment variables”

### `.env` files
 Section titled “.env files”
 Environment variables can be loaded from `.env` files in your project directory.

Just create a `.env` file in the project directory and add some variables to it.

 .env ` # This will only be available when run on the server! DB_PASSWORD = " foobar "
 # This will be available everywhere! PUBLIC_POKEAPI = " https://pokeapi.co/api/v2 " `
 You can also add `.production`, `.development` or a custom mode name to the filename itself (e.g `.env.testing`, `.env.staging`). This allows you to use different sets of environment variables at different times.

The `astro dev` and `astro build` commands default to `"development"` and `"production"` modes, respectively. You can run these commands with the `--mode` flag to pass a different value for `mode` and load the matching `.env` file.

This allows you to run the dev server or build your site connecting to different APIs:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` # Run the dev server connected to a "staging" API npm run astro dev -- --mode staging
 # Build a site that connects to a "production" API with additional debug information npm run astro build -- --devOutput
 # Build a site that connects to a "testing" API npm run astro build -- --mode testing `

 Terminal window
```
` # Run the dev server connected to a "staging" API pnpm astro dev --mode staging
 # Build a site that connects to a "production" API with additional debug information pnpm astro build --devOutput
 # Build a site that connects to a "testing" API pnpm astro build --mode testing `
```

 Terminal window
```
` # Run the dev server connected to a "staging" API yarn astro dev --mode staging
 # Build a site that connects to a "production" API with additional debug information yarn astro build --devOutput
 # Build a site that connects to a "testing" API yarn astro build --mode testing `
```

 For more on `.env` files, see the Vite documentation .

### In the Astro config file
 Section titled “In the Astro config file”
 Astro evaluates configuration files before it loads your other files. This means that you cannot use `import.meta.env` in `astro.config.mjs` to access environment variables that were set in `.env` files.

You can use `process.env` in a configuration file to access other environment variables, like those set by the CLI .

You can also use Vite’s `loadEnv` helper to manually load `.env` files.

 astro.config.mjs ` import { loadEnv } from " vite " ;
 const { SECRET_PASSWORD } = loadEnv ( process . env . NODE_ENV , process . cwd () , "" ); `

### Using the CLI
 Section titled “Using the CLI”
 You can also add environment variables as you run your project:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` PUBLIC_POKEAPI = https://pokeapi.co/api/v2 npm run dev `

 Terminal window
```
` PUBLIC_POKEAPI = https://pokeapi.co/api/v2 pnpm run dev `
```

 Terminal window
```
` PUBLIC_POKEAPI = https://pokeapi.co/api/v2 yarn run dev `
```

## Getting environment variables
 Section titled “Getting environment variables”
 Environment variables in Astro are accessed with `import.meta.env`, using the `import.meta` feature added in ES2020 , instead of `process.env`.

For example, use `import.meta.env.PUBLIC_POKEAPI` to get the `PUBLIC_POKEAPI` environment variable.

 ` // When import.meta.env.SSR === true const data = await db ( import. meta . env . DB_PASSWORD );
 // When import.meta.env.SSR === false const data = fetch ( ` ${ import. meta . env . PUBLIC_POKEAPI } /pokemon/squirtle ` ); `
 When using SSR, environment variables can be accessed at runtime based on the SSR adapter being used. With most adapters you can access environment variables with `process.env`, but some adapters work differently. For the Deno adapter, you will use `Deno.env.get()`. See how to access the Cloudflare runtime to handle environment variables when using the Cloudflare adapter. Astro will first check the server environment for variables, and if they don’t exist, Astro will look for them in `.env` files.

## Type safe environment variables
 Section titled “Type safe environment variables”
 The `astro:env` API lets you configure a type-safe schema for environment variables you have set . This allows you to indicate whether they should be available on the server or the client, and define their data type and additional properties.

 Developing an adapter? See how to make an adapter compatible with `astro:env` .

### Basic Usage
 Section titled “Basic Usage”

#### Define your schema
 Section titled “Define your schema”
 To configure a schema, add the `env.schema` option to your Astro config:

 astro.config.mjs ` import { defineConfig } from " astro/config " ;
 export default defineConfig ({ env: { schema: { // ... } } }) `
 You can then register variables as a string, number, enum, or boolean using the `envField` helper. Define the kind of environment variable by providing a `context` (`"client"` or `"server"`) and `access` (`"secret"` or `"public"`) for each variable, and pass any additional properties such as `optional` or `default` in an object:

 astro.config.mjs ` import { defineConfig, envField } from " astro/config " ;
 export default defineConfig ({ env: { schema: { API_URL: envField . string ({ context: " client " , access: " public " , optional: true }), PORT: envField . number ({ context: " server " , access: " public " , default: 4321 }), API_SECRET: envField . string ({ context: " server " , access: " secret " }), } } }) `
 Types will be generated for you when running `astro dev` or `astro build`, but you can run `astro sync` to generate types only.

#### Use variables from your schema
 Section titled “Use variables from your schema”
 Import and use your defined variables from the appropriate `/client` or `/server` module:

 ` --- import { API_URL } from " astro:env/client " ; import { API_SECRET_TOKEN } from " astro:env/server " ;
 const data = await fetch ( ` ${ API_URL } /users ` , { method: " GET " , headers: { " Content-Type " : " application/json " , " Authorization " : ` Bearer ${ API_SECRET_TOKEN } ` }, } ) ---
 &#x3C; script > import { API_URL } from " astro:env/client " ;
 fetch ( ` ${ API_URL } /ping ` ) &#x3C;/ script > `

### Variable types
 Section titled “Variable types”
 There are three kinds of environment variables, determined by the combination of `context` (`"client"` or `"server"`) and `access` (`"secret"` or `"public"`) settings defined in your schema:

-
 Public client variables : These variables end up in both your final client and server bundles, and can be accessed from both client and server through the `astro:env/client` module:

 ` import { API_URL } from " astro:env/client " ; `

-
 Public server variables : These variables end up in your final server bundle and can be accessed on the server through the `astro:env/server` module:

 ` import { PORT } from " astro:env/server " ; `

-
 Secret server variables : These variables are not part of your final bundle and can be accessed on the server through the `astro:env/server` module:

 ` import { API_SECRET } from " astro:env/server " ; `
 By default, all secrets are validated whenever anything is imported from the `astro:env/server` module. This means, secrets may be validated even when they are not imported. You may need to pass dummy environment variables to satisfy this validation during the build.

You can also enable validating secrets on start by configuring `validateSecrets: true` .

### Data types
 Section titled “Data types”
 There are currently four data types supported: strings, numbers, enums, and booleans:

 ` import { envField } from " astro/config " ;
 envField . string ({ // context &#x26; access optional: true , default: " foo " , })
 envField . number ({ // context &#x26; access optional: true , default: 15 , })
 envField . boolean ({ // context &#x26; access optional: true , default: true , })
 envField . enum ({ // context &#x26; access values: [ " foo " , " bar " , " baz " ], optional: true , default: " baz " , }) `

 For a complete list of validation fields, see the `envField` API reference .

### Retrieving secrets dynamically
 Section titled “Retrieving secrets dynamically”
 Despite defining your schema, you may want to retrieve the raw value of a given secret or to retrieve secrets not defined in your schema. In this case, you can use `getSecret()` exported from `astro:env/server`:

 ` import { FOO, // boolean getSecret } from " astro:env/server " ;
 getSecret ( " FOO " ); // string | undefined `

 Learn more in the API reference .

### Limitations
 Section titled “Limitations”
 `astro:env` is a virtual module which means it can only be used inside the Astro context. For example, you can use it in:

- Middlewares

- Astro routes and endpoints

- Astro components

- Framework components

- Modules

You cannot use it in the following and will have to resort to `process.env`:

- `astro.config.mjs`

- Scripts

 Learn

 Contribute

 Community

 Sponsor

## Integrations

# Working with integrations

 Astro integrations add new functionality and behaviors for your project with only a few lines of code. You can use an official integration, integrations built by the community or even build a custom integration yourself .

Integrations can…

- Unlock React, Vue, Svelte, Solid, and other popular UI frameworks with a renderer .

- Enable on-demand rendering with an SSR adapter .

- Integrate tools like MDX, and Partytown with a few lines of code.

- Add new features to your project, like automatic sitemap generation.

- Write custom code that hooks into the build process, dev server, and more.

## Official integrations
 Section titled “Official integrations”
 The following integrations are maintained by Astro.

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

## Automatic integration setup
 Section titled “Automatic integration setup”
 Astro includes an `astro add` command to automate the setup of official integrations. Several community plugins can also be added using this command. Please check each integration’s own documentation to see whether `astro add` is supported, or whether you must install manually .

Run the `astro add` command using the package manager of your choice and our automatic integration wizard will update your configuration file and install any necessary dependencies.

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

 It’s even possible to add multiple integrations at the same time!

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npx astro add react sitemap partytown `

 Terminal window
```
` pnpm astro add react sitemap partytown `
```

 Terminal window
```
` yarn astro add react sitemap partytown `
```

### Manual installation
 Section titled “Manual installation”
 Astro integrations are always added through the `integrations` property in your `astro.config.mjs` file.

There are three common ways to import an integration into your Astro project:

-
 Install an npm package integration .

-
Import your own integration from a local file inside your project.

-
Write your integration inline, directly in your config file.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import installedIntegration from ' @astrojs/vue ' ; import localIntegration from ' ./my-integration.js ' ;
 export default defineConfig ({ integrations: [ // 1. Imported from an installed npm package installedIntegration (), // 2. Imported from a local JS file localIntegration (), // 3. An inline object { name: ' namespace:id ' , hooks: { /* ... */ } }, ] }); `

 Check out the Integration API reference to learn all of the different ways that you can write an integration.

#### Installing an npm package
 Section titled “Installing an npm package”
 Install an npm package integration using a package manager, and then update `astro.config.mjs` manually.

For example, to install the `@astrojs/sitemap` integration:

-
Install the integration to your project dependencies using your preferred package manager:

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

-
 Import the integration to your `astro.config.mjs` file, and add it to your `integrations[]` array, along with any configuration options:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import sitemap from ' @astrojs/sitemap ' ;
 export default defineConfig ({ // ... integrations: [ sitemap () ], // ... }); `
 Note that different integrations may have different configuration settings. Read each integration’s documentation, and apply any necessary config options to your chosen integration in `astro.config.mjs`.

### Custom options
 Section titled “Custom options”
 Integrations are almost always authored as factory functions that return the actual integration object. This lets you pass arguments and options to the factory function that customize the integration for your project.

 ` integrations: [ // Example: Customize your integration with function arguments sitemap ({ filter: true }) ] `

### Toggle an integration
 Section titled “Toggle an integration”
 Falsy integrations are ignored, so you can toggle integrations on &#x26; off without worrying about left-behind `undefined` and boolean values.

 ` integrations: [ // Example: Skip building a sitemap on Windows process . platform !== ' win32 ' &#x26;&#x26; sitemap () ] `

## Upgrading integrations
 Section titled “Upgrading integrations”
 To upgrade all official integrations at once, run the `@astrojs/upgrade` command. This will upgrade both Astro and all official integrations to their latest versions.

### Automatic upgrading
 Section titled “Automatic upgrading”

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window
```
` # Upgrade Astro and official integrations together to latest npx @astrojs/upgrade `
```

 Terminal window
```
` # Upgrade Astro and official integrations together to latest pnpm dlx @astrojs/upgrade `
```

 Terminal window
```
` # Upgrade Astro and official integrations together to latest yarn dlx @astrojs/upgrade `
```

### Manual upgrading
 Section titled “Manual upgrading”
 To upgrade one or more integrations manually, use the appropriate command for your package manager.

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` # Example: upgrade React and Partytown integrations npm install @astrojs/react@latest @astrojs/partytown@latest `

 Terminal window
```
` # Example: upgrade React and Partytown integrations pnpm add @astrojs/react@latest @astrojs/partytown@latest `
```

 Terminal window
```
` # Example: upgrade React and Partytown integrations yarn add @astrojs/react@latest @astrojs/partytown@latest `
```

## Removing an integration
 Section titled “Removing an integration”

-
 To remove an integration, first uninstall the integration from your project.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm uninstall @astrojs/react `

 Terminal window
```
` pnpm remove @astrojs/react `
```

 Terminal window
```
` yarn remove @astrojs/react `
```

-
 Next, remove the integration from your `astro.config.*` file:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import react from ' @astrojs/react ' ;
 export default defineConfig ({ integrations: [ react () ] }); `

## Finding more integrations
 Section titled “Finding more integrations”
 You can find many integrations developed by the community in the Astro Integrations Directory . Follow links there for detailed usage and configuration instructions.

## Building your own integration
 Section titled “Building your own integration”
 Astro’s Integration API is inspired by Rollup and Vite, and designed to feel familiar to anyone who has ever written a Rollup or Vite plugin before.

Check out the Integration API reference to learn what integrations can do and how to write one yourself.

## Publishing your integration to npm
 Section titled “Publishing your integration to npm”
 Publishing an Astro component is a great way to reuse your existing work across your projects, and to share with the wider Astro community at large. Astro components can be published directly to and installed from npm, just like any other JavaScript package.

Looking for inspiration? Check out some of our favorite themes and components from the Astro community. You can also search npm to see the entire public catalog.

### Quick start
 Section titled “Quick start”
 To get started developing your component quickly, you can use a template already set up for you.

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` # Initialize the Astro Component template in a new directory npm create astro@latest my-new-component-directory -- --template component `

 Terminal window
```
` # Initialize the Astro Component template in a new directory pnpm create astro@latest my-new-component-directory -- --template component `
```

 Terminal window
```
` # Initialize the Astro Component template in a new directory yarn create astro my-new-component-directory --template component `
```

### Creating a package
 Section titled “Creating a package”

 To create a new package, configure your development environment to use workspaces within your project. This will allow you to develop your component alongside a working copy of Astro.

 - Directory my-new-component-directory/
 Directory demo/
 … for testing and demonstration
 - package.json
- Directory packages/
 Directory my-component/
 index.js
- package.json
- … additional files used by the package

 This example, named `my-project`, creates a project with a single package, named `my-component`, and a `demo/` directory for testing and demonstrating the component.

This is configured in the project root’s `package.json` file:

 ` { "name" : " my-project " , "workspaces" : [ " demo " , " packages/* " ] } `
 In this example, multiple packages can be developed together from the `packages` directory. These packages can also be referenced from `demo`, where you can install a working copy of Astro.

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm create astro@latest demo -- --template minimal `

 Terminal window
```
` pnpm create astro@latest demo -- --template minimal `
```

 Terminal window
```
` yarn create astro demo --template minimal `
```

 There are two initial files that will make up your individual package: `package.json` and `index.js`.

#### `package.json`
 Section titled “package.json”
 The `package.json` in the package directory includes all of the information related to your package, including its description, dependencies, and any other package metadata.

 ` { "name" : " my-component " , "description" : " Component description " , "version" : " 1.0.0 " , "homepage" : " https://github.com/owner/project#readme " , "type" : " module " , "exports" : { "." : " ./index.js " , "./astro" : " ./MyAstroComponent.astro " , "./react" : " ./MyReactComponent.jsx " }, "files" : [ " index.js " , " MyAstroComponent.astro " , " MyReactComponent.jsx " ], "keywords" : [ " astro-component " , " withastro " , " ... etc " , " ... etc " ] } `
 `description` Section titled “description”
 A short description of your component used to help others know what it does.

 ` { "description" : " An Astro Element Generator " } `
 `type` Section titled “type”
 The module format used by Node.js and Astro to interpret your `index.js` files.

 ` { "type" : " module " } `
 Use `"type": "module"` so that your `index.js` can be used as an entrypoint with `import` and `export` .

 `homepage` Section titled “homepage”
 The url to the project homepage.

 ` { "homepage" : " https://github.com/owner/project#readme " } `
 This is a great way to direct users to an online demo, documentation, or homepage for your project.

 `exports` Section titled “exports”
 The entry points of a package when imported by name.

 ` { "exports" : { "." : " ./index.js " , "./astro" : " ./MyAstroComponent.astro " , "./react" : " ./MyReactComponent.jsx " } } `
 In this example, importing `my-component` would use `index.js`, while importing `my-component/astro` or `my-component/react` would use `MyAstroComponent.astro` or `MyReactComponent.jsx` respectively.

 `files` Section titled “files”
 An optional optimization to exclude unnecessary files from the bundle shipped to users via npm. Note that only files listed here will be included in your package , so if you add or change files necessary for your package to work, you must update this list accordingly.

 ` { "files" : [ " index.js " , " MyAstroComponent.astro " , " MyReactComponent.jsx " ] } `
 `keywords` Section titled “keywords”
 An array of keywords relevant to your component, used to help others find your component on npm and in any other search catalogs.

Add `astro-component`, `astro-integration`, or `withastro` as a special keyword to maximize its discoverability in the Astro ecosystem.

 ` { "keywords" : [ " astro-component " , " withastro " , " ... etc " , " ... etc " ] } `

#### `index.js`
 Section titled “index.js”
 The main package entrypoint used whenever your package is imported.

 ` export { default as MyAstroComponent } from ' ./MyAstroComponent.astro ' ; export { default as MyReactComponent } from ' ./MyReactComponent.jsx ' ; `
 This allows you to package multiple components together into a single interface.

 Example: Using named imports Section titled “Example: Using named imports”

```
` --- import { MyAstroComponent } from ' my-component ' ; import { MyReactComponent } from ' my-component ' ; --- &#x3C; MyAstroComponent /> &#x3C; MyReactComponent /> `
```
  ">
 Example: Using namespace imports Section titled “Example: Using namespace imports”

```
` --- import * as Example from ' example-astro-component ' ; --- &#x3C; Example . MyAstroComponent /> &#x3C; Example . MyReactComponent /> `
```
  ">
 Example: Using individual imports Section titled “Example: Using individual imports”

```
` --- import MyAstroComponent from ' example-astro-component/astro ' ; import MyReactComponent from ' example-astro-component/react ' ; --- &#x3C; MyAstroComponent /> &#x3C; MyReactComponent /> `
```
  ">

### Developing your package
 Section titled “Developing your package”
 Astro does not have a dedicated “package mode” for development. Instead, you should use a demo project to develop and test your package inside of your project. This can be a private website only used for development, or a public demo/documentation website for your package.

If you are extracting components from an existing project, you can even continue to use that project to develop your now-extracted components.

### Testing your component
 Section titled “Testing your component”
 Astro does not currently ship a test runner. (If you are interested in helping out with this, join us on Discord! )

In the meantime, our current recommendation for testing is:

-
Add a test `fixtures` directory to your `demo/src/pages` directory.

-
Add a new page for every test that you’d like to run.

-
Each page should include some different component usage that you’d like to test.

-
Run `astro build` to build your fixtures, then compare the output of the `dist/__fixtures__/` directory to what you expected.

 Directory my-project/demo/src/pages/__fixtures__/
 test-name-01.astro
- test-name-02.astro
- test-name-03.astro

### Publishing your component
 Section titled “Publishing your component”
 Once you have your package ready, you can publish it to npm using the `npm publish` command. If that fails, make sure that you have logged in via `npm login` and that your `package.json` is correct. If it succeeds, you’re done!

Notice that there was no `build` step for Astro packages. Any file type that Astro supports natively, such as `.astro`, `.ts`, `.jsx`, and `.css`, can be published directly without a build step.

If you need another file type that isn’t natively supported by Astro, add a build step to your package. This advanced exercise is left up to you.

### Integrations library
 Section titled “Integrations library”
 Share your hard work by adding your integration to our integrations library !

#### `package.json` data
 Section titled “package.json data”
 The library is automatically updated weekly, pulling in every package published to npm with the `astro-component`, `astro-integration`, or `withastro` keyword.

The integrations library reads the `name`, `description`, `repository`, and `homepage` data from your `package.json`.

Avatars are a great way to highlight your brand in the library! Once your package is published you can file a GitHub issue with your avatar attached and we will add it to your listing.

#### Categories
 Section titled “Categories”
 In addition to the required `astro-component`, `astro-integration`, or `withastro` keyword, special keywords are also used to automatically organize packages. Including any of the keywords below will add your integration to the matching category in our integrations library.

 | ** category** | **keywords** |
 | Accessibility | `a11y`, `accessibility` |
| Adapters | `astro-adapter` |
| Analytics | `analytics` |
| CSS + UI | `css`, `ui`, `icon`, `icons`, `renderer` |
| Frameworks | `renderer` |
| Content Loaders | `astro-loader` |
| Images + Media | `media`, `image`, `images`, `video`, `audio` |
| Performance + SEO | `performance`, `perf`, `seo`, `optimization` |
| Dev Toolbar | `devtools`, `dev-overlay`, `dev-toolbar` |
| Utilities | `tooling`, `utils`, `utility` |

Packages that don’t include any keyword matching a category will be shown as `Uncategorized`.

### Share
 Section titled “Share”
 We encourage you to share your work, and we really do love seeing what our talented Astronauts create. Come and share what you create with us in our Discord or mention @astrodotbuild in a Tweet!

 Learn

 Contribute

 Community

 Sponsor

## Build With Ai

# Building Astro sites with AI tools

 AI-powered editors and agentic coding tools generally have good knowledge of Astro’s core APIs and concepts. However, some may use older APIs and may not be aware of newer features or recent changes to the framework.

This guide covers how to enhance AI tools with up-to-date Astro knowledge and provides best practices for building Astro sites with AI assistance.

## Astro Docs MCP Server
 Section titled “Astro Docs MCP Server”
 You can ensure your AI tools have current Astro knowledge through the Astro Docs MCP (Model Context Protocol) server. This provides real-time access to the latest documentation, helping AI tools avoid outdated recommendations and ensuring they understand current best practices.

Unlike AI models trained on static data, the MCP server provides access to the latest Astro documentation. The server is free, open-source, and runs remotely with nothing to install locally.

The Astro Docs MCP server uses the kapa.ai API to maintain an up-to-date index of the Astro documentation.

### Server Details
 Section titled “Server Details”

- Name : Astro Docs

- URL : `https://mcp.docs.astro.build/mcp`

- Transport : Streamable HTTP

### Installation
 Section titled “Installation”
 The setup process varies depending on your AI development tool. You may see some tools refer to MCP servers as connectors, adapters, extensions, or plugins.

#### Manual setup
 Section titled “Manual setup”
 Many tools support a common JSON configuration format for MCP servers. If there are not specific instructions for your chosen tool, you may be able to add the Astro Docs MCP server by including the following configuration in your tool’s MCP settings:

 -

 Streamable HTTP

-

 Local Proxy

 - MCP Configuration ` { "mcpServers" : { "Astro docs" : { "type" : " http " , "url" : " https://mcp.docs.astro.build/mcp " } } } `

 MCP Configuration
```
` { "mcpServers" : { "Astro docs" : { "type" : " stdio " , "command" : " npx " , "args" : [ " -y " , " mcp-remote " , " https://mcp.docs.astro.build/mcp " ] } } } `
```

#### Claude Code CLI
 Section titled “Claude Code CLI”
 Claude Code is an agentic coding tool that runs on the command line. Enabling the Astro Docs MCP server allows it to access the latest documentation while generating Astro code.

Install using the terminal command:

 Terminal window ` claude mcp add --transport http astro-docs https://mcp.docs.astro.build/mcp `
 More info on using MCP servers with Claude Code

#### Claude Code GitHub Action
 Section titled “Claude Code GitHub Action”
 Claude Code also provides a GitHub Action that can be used to run commands in response to GitHub events. Enabling the Astro Docs MCP server allows it to access the latest documentation while answering questions in comments or generating Astro code.

You can configure it to use the Astro Docs MCP server for documentation access by adding the following to the workflow file:

 .github/workflows/claude.yml ` # ...rest of your workflow configuration - uses : anthropics/claude-code-action@beta with : anthropic_api_key : ${{ secrets.ANTHROPIC_API_KEY }} mcp_config : | { "mcpServers": { "astro-docs": { "type": "http", "url": "https://mcp.docs.astro.build/mcp" } } } allowed_tools : " mcp__astro-docs__search_astro_docs " `
 More info on using MCP servers with the Claude Code GitHub Action

#### Codex CLI
 Section titled “Codex CLI”
 Codex CLI is a command-line AI coding tool that can use the Astro Docs MCP server to access documentation while generating Astro code.

You can configure MCP servers at the global level in the `~/.codex/config.toml` file, or in a `.codex/config.toml` file in a project root.

 ~/.codex/config.toml ` [mcp_servers.astro-docs] command = " npx " args = [ " -y " , " mcp-remote " , " https://mcp.docs.astro.build/mcp " ] `
 More info on using MCP servers with Codex CLI

#### Cursor
 Section titled “Cursor”
 Cursor is an AI code editor. Adding the Astro Docs MCP server allows Cursor to access the latest Astro documentation while performing development tasks.

Install by clicking the button below:

 Add to Cursor

 More info on using MCP servers with Cursor

#### Visual Studio Code
 Section titled “Visual Studio Code”
 Visual Studio Code supports MCP servers when using Copilot Chat. Adding the Astro Docs MCP server allows VS Code to access the latest Astro documentation when answering questions or performing coding tasks.

Install by clicking the button below:

 Add to VS Code

 More info on using MCP servers with VS Code

#### Warp
 Section titled “Warp”
 Warp (formerly Warp Terminal) is an agent development environment built for coding with multiple AI agents. Adding the Astro Docs MCP server allows Warp to access the latest Astro documentation when answering questions or performing coding tasks.

 Open your Warp settings and go to AI > MCP Servers > Manage MCP Servers.

- Click “Add”.

- Enter the following configuration. You can optionally configure the Astro MCP server to activate on startup using the `start_on_launch` flag:
 MCP Configuration ` { "mcpServers" : { "Astro docs" : { "command" : " npx " , "args" : [ " -y " , " mcp-remote " , " https://mcp.docs.astro.build/mcp " ], "env" : {}, "working_directory" : null , "start_on_launch" : true } } } `

- Click “Save”.

 More info on using MCP servers with Warp

#### Claude.ai / Claude Desktop
 Section titled “Claude.ai / Claude Desktop”
 Claude.ai is a general-purpose AI assistant. Adding the Astro Docs MCP server allows it to access the latest documentation when answering Astro questions or generating Astro code.

- Navigate to the Claude.ai connector settings .

- Click “Add custom connector”. You may need to scroll down to find this option.

- Enter the server URL: `https://mcp.docs.astro.build/mcp`.

- Set the name to “Astro docs”.

 More info on using MCP servers with Claude.ai

#### Windsurf
 Section titled “Windsurf”
 Windsurf is an AI-powered agentic coding tool, available as editor plugins or a standalone editor. It can use the Astro Docs MCP server to access documentation while performing coding tasks.

Windsurf doesn’t support streaming HTTP, so it requires a local proxy configuration:

-
Open `~/.codeium/windsurf/mcp_config.json` in your editor.

-
Add the following configuration to your Windsurf MCP settings:

 MCP Configuration ` { "mcpServers" : { "Astro docs" : { "command" : " npx " , "args" : [ " -y " , " mcp-remote " , " https://mcp.docs.astro.build/mcp " ] } } } `

-
 Save the configuration and restart Windsurf.

 More info on using MCP servers with Windsurf

#### Gemini CLI
 Section titled “Gemini CLI”
 Gemini CLI is a command-line AI coding tool that can use the Astro Docs MCP server to access documentation while generating Astro code.

You can configure MCP servers at the global level in the `~/.gemini/settings.json` file, or in a `.gemini/settings.json` file in a project root.

 .gemini/settings.json ` { "mcpServers" : { "Astro docs" : { "httpUrl" : " https://mcp.docs.astro.build/mcp " , } } } `
 More info on using MCP servers with Gemini CLI

#### Google Antigravity
 Section titled “Google Antigravity”
 Google Antigravity is an agentic development platform.

- Open `~/.gemini/antigravity/mcp_config.json` by following the Connecting Custom MCP Servers guide .

- Add the following configuration to `mcp_config.json`:
 mcp_config.json ` { "mcpServers" : { "astro-docs" : { "serverUrl" : " https://mcp.docs.astro.build/mcp " } } } `

- Save the file and click “Refresh” in the “Manage MCPs” tab.

#### Zed
 Section titled “Zed”
 Zed supports MCP servers when using its AI capabilities. It can use the Astro Docs MCP server to access documentation while performing coding tasks.

-
Open `~/.config/zed/settings.json` in your editor.

-
Add the following configuration to your Zed MCP settings:

 MCP Configuration ` { "context_servers" : { "Astro docs" : { "settings" : {}, "enabled" : true , "url" : " https://mcp.docs.astro.build/mcp " } } } `

-
 Save the configuration.

 More info on using MCP servers with Zed

#### ChatGPT
 Section titled “ChatGPT”
 Refer to the OpenAI MCP documentation for specific setup instructions.

#### Raycast
 Section titled “Raycast”
 Raycast can connect to MCP servers to enhance its AI capabilities. Adding the Astro Docs MCP server allows Raycast to access the latest Astro documentation while answering questions.

Install by clicking the button below:

 Add to Raycast

 More info on using MCP servers with Raycast

#### Opencode AI
 Section titled “Opencode AI”
 Opencode AI is an open-source, terminal-based AI coding tool that can use the Astro Docs MCP server to access documentation while generating Astro code.

You can configure MCP servers in your Opencode configuration file, typically named `opencode.json`, located in your project root or your global configuration directory (e.g. `~/.config/opencode/opencode.json`).

 MCP Configuration ` { "$schema" : " https://opencode.ai/config.json " , "mcp" : { "Astro docs" : { "type" : " remote " , "url" : " https://mcp.docs.astro.build/mcp " , "enabled" : true } } } `
 More info on using Opencode AI

#### GitHub Copilot Coding Agent
 Section titled “GitHub Copilot Coding Agent”
 GitHub Copilot can be used as a coding agent powered by GitHub Actions. Enabling the Astro Docs MCP server allows it to access the latest Astro documentation when answering questions or performing coding tasks.

You can configure it to use the Astro Docs MCP server for documentation access by adding the following to your repository’s Copilot coding agent settings available at `https://github.com/&#x3C;your-org>/&#x3C;your-repo>/settings/copilot/coding_agent`:

 MCP Configuration ` { "mcpServers" : { "astro-docs" : { "type" : " http " , "url" : " https://mcp.docs.astro.build/mcp " , "tools" : [ " mcp__astro-docs__search_astro_docs " ] } } } `
 Learn more about extending GitHub Copilot coding agent with MCP servers .

### Usage
 Section titled “Usage”
 Once configured, you can ask your AI tool questions about Astro, and it will retrieve information directly from the latest docs. Coding agents will be able to consult the latest documentation when performing coding tasks, and chatbots will be able to accurately answer questions about Astro features, APIs, and best practices.

### Troubleshooting
 Section titled “Troubleshooting”
 If you encounter issues:

- Verify that your tool supports streamable HTTP transport.

- Check that the server URL is correct: `https://mcp.docs.astro.build/mcp`.

- Ensure your tool has proper internet access.

- Consult your specific tool’s MCP integration documentation.

If you are still having problems, open an issue in the Astro Docs MCP Server repository .

## Discord AI Support
 Section titled “Discord AI Support”
 The same technology that powers Astro’s MCP server is also available as a chatbot in the Astro Discord for self-serve support. Visit the `#support-ai` channel to ask questions about Astro or your project code in natural language. Your conversation is automatically threaded, and you can ask an unlimited number of follow-up questions.

 Conversations with the chatbot are public, and are subject to the same server rules for language and behavior as the rest of our channels , but they are not actively visited by our volunteer support members. For assistance from the community, please create a thread in our regular `#support` channel.

## Tips for AI-Powered Astro Development
 Section titled “Tips for AI-Powered Astro Development”

- Start with templates : Rather than building from scratch, ask AI tools to start with an existing Astro template or use `npm create astro@latest` with a template option.

- Use `astro add` for integrations : Ask AI tools to use `astro add` for official integrations (e.g. `astro add tailwind`, `astro add react`). For other packages, install using the command for your preferred package manager rather than editing `package.json` directly.

- Verify current APIs : AI tools may use outdated patterns. Ask them to check the latest documentation, especially for newer features like sessions and actions. This is also important for features that have seen significant changes since their initial launch, such as content collections, or previously experimental features that may no longer be experimental.

- Use project rules : If your AI tool supports it, set up project rules to enforce best practices and coding standards, such as the ones listed above.

 Learn

 Contribute

 Community

 Sponsor

## Dev Toolbar

# Dev toolbar

 While the dev server is running, Astro includes a dev toolbar at the bottom of every page in your local browser preview.

This toolbar includes a number of useful tools for debugging and inspecting your site during development and can be extended with more dev toolbar apps found in the integrations directory. You can even build your own toolbar apps using the Dev Toolbar API !

This toolbar is enabled by default and appears when you hover over the bottom of the page. It is a development tool only and will not appear on your published site.

## Built-in apps
 Section titled “Built-in apps”

### Astro Menu
 Section titled “Astro Menu”
 The Astro Menu app provides easy access to various information about the current project and links to extra resources. Notably, it provides one-click access to the Astro documentation, GitHub repository, and Discord server.

This app also includes a “Copy debug info” button which will run the `astro info` command and copy the output to your clipboard. This can be useful when asking for help or reporting issues.

### Inspect
 Section titled “Inspect”
 The Inspect app provides information about any islands on the current page. This will show you the properties passed to each island, and the client directive that is being used to render them.

### Audit
 Section titled “Audit”
 The Audit app automatically runs a series of audits on the current page, checking for the most common performance and accessibility issues. When an issue is found, a red dot will appear in the toolbar. Clicking on the app will pop up a list of results from the audit and will highlight the related elements directly in the page.

### Settings
 Section titled “Settings”
 The Settings app allows you to configure options for the dev toolbar, such as verbose logging, disabling notifications, and adjusting its placement on your screen.

## Extending the dev toolbar
 Section titled “Extending the dev toolbar”
 Astro integrations can add new apps to the dev toolbar, allowing you to extend it with custom tools that are specific to your project. You can find more dev tool apps to install in the integrations directory or using the Astro Menu .

Install additional dev toolbar app integrations in your project just like any other Astro integration according to its own installation instructions.

 Related recipe:

 Create a dev toolbar app

## Disabling the dev toolbar
 Section titled “Disabling the dev toolbar”
 The dev toolbar is enabled by default for every site. You can choose to disable it for individual projects and/or users as needed.

### Per-project
 Section titled “Per-project”
 To disable the dev toolbar for everyone working on a project, set `devToolbar: false` in the Astro config file .

 astro.config.mjs ` import { defineConfig } from " astro/config " ;
 export default defineConfig ({ devToolbar: { enabled: false } }); `
 To enable the dev toolbar again, remove these lines from your configuration, or set `enabled: true`.

### Per-user
 Section titled “Per-user”
 To disable the dev toolbar for yourself on a specific project, run the `astro preferences` command.

 Terminal window ` astro preferences disable devToolbar `
 To disable the dev toolbar in all Astro projects for a user on the current machine, add the `--global` flag when running `astro-preferences`:

 Terminal window ` astro preferences disable --global devToolbar `
 The dev toolbar can later be enabled with:

 Terminal window
```
` astro preferences enable devToolbar `
```

 Learn

 Contribute

 Community

 Sponsor