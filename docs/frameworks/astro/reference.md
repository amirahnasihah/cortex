# Astro - Reference


## Configuration Reference

# Configuration Reference

The following reference covers all supported configuration options in Astro. To learn more about configuring Astro, read our guide on Configuring Astro .

 - astro.config.mjs ` import { defineConfig } from ' astro/config '
 export default defineConfig ({ // your configuration options here... }) `

## Top-Level Options
 Section titled “Top-Level Options”

### site
 Section titled “site”
 Type: `string`

Your final, deployed URL. Astro uses this full URL to generate your sitemap and canonical URLs in your final build. It is strongly recommended that you set this configuration to get the most out of Astro.

 ` { site: ' https://www.my-site.dev ' } `

### base
 Section titled “base”
 Type: `string`

The base path to deploy to. Astro will use this path as the root for your pages and assets both in development and in production build.

In the example below, `astro dev` will start your server at `/docs`.

 ` { base: ' /docs ' } `
 When using this option, all of your static asset imports and URLs should add the base as a prefix. You can access this value via `import.meta.env.BASE_URL`.

The value of `import.meta.env.BASE_URL` will be determined by your `trailingSlash` config, no matter what value you have set for `base`.

A trailing slash is always included if `trailingSlash: "always"` is set. If `trailingSlash: "never"` is set, `BASE_URL` will not include a trailing slash, even if `base` includes one.

Additionally, Astro will internally manipulate the configured value of `config.base` before making it available to integrations. The value of `config.base` as read by integrations will also be determined by your `trailingSlash` configuration in the same way.

In the example below, the values of `import.meta.env.BASE_URL` and `config.base` when processed will both be `/docs`:

 ` { base: ' /docs/ ' , trailingSlash: " never " } `
 In the example below, the values of `import.meta.env.BASE_URL` and `config.base` when processed will both be `/docs/`:

 ` { base: ' /docs ' , trailingSlash: " always " } `

### trailingSlash
 Section titled “trailingSlash”
 Type: `'always' | 'never' | 'ignore'`
 Default: `'ignore'`

Set the route matching behavior for trailing slashes in the dev server and on-demand rendered pages. Choose from the following options:

 `'ignore'` - Match URLs regardless of whether a trailing ”/” exists. Requests for “/about” and “/about/” will both match the same route.

- `'always'` - Only match URLs that include a trailing slash (e.g: “/about/”). In production, requests for on-demand rendered URLs without a trailing slash will be redirected to the correct URL for your convenience. However, in development, they will display a warning page reminding you that you have `always` configured.

- `'never'` - Only match URLs that do not include a trailing slash (e.g: “/about”). In production, requests for on-demand rendered URLs with a trailing slash will be redirected to the correct URL for your convenience. However, in development, they will display a warning page reminding you that you have `never` configured.

When redirects occur in production for GET requests, the redirect will be a 301 (permanent) redirect. For all other request methods, it will be a 308 (permanent, and preserve the request method) redirect.

Trailing slashes on prerendered pages are handled by the hosting platform, and may not respect your chosen configuration.
See your hosting platform’s documentation for more information. You cannot use Astro redirects for this use case at this point.

 ` { // Example: Require a trailing slash during development trailingSlash: ' always ' } `
 See Also:

- build.format

### redirects
 Section titled “redirects”
 Type: `Record<string, RedirectConfig>`
 Default: `{}`

 Added in:
 `astro@2.9.0`

Specify a mapping of redirects where the key is the route to match
and the value is the path to redirect to.

You can redirect both static and dynamic routes, but only to the same kind of route.
For example, you cannot have a `'/article': '/blog/[...slug]'` redirect.

 ` export default defineConfig ({ redirects: { ' /old ' : ' /new ' , ' /blog/[...slug] ' : ' /articles/[...slug] ' , ' /about ' : ' https://example.com/about ' , ' /news ' : { status: 302 , destination: ' https://example.com/news ' }, // '/product1/', '/product1' // Note, this is not supported } }) `
 For statically-generated sites with no adapter installed, this will produce a client redirect using a `&#x3C;meta http-equiv="refresh">` tag and does not support status codes.

When using SSR or with a static adapter in `output: static`
mode, status codes are supported.
Astro will serve redirected GET requests with a status of `301`
and use a status of `308` for any other request method.

You can customize the redirection status code using an object in the redirect config:

 ` export default defineConfig ({ redirects: { ' /other ' : { status: 302 , destination: ' /place ' , }, } }) `

### output
 Section titled “output”
 Type: `'static' | 'server'`
 Default: `'static'`

Specifies the output target for builds.

- `'static'` - Prerender all your pages by default, outputting a completely static site if none of your pages opt out of prerendering.

- `'server'` - Use server-side rendering (SSR) for all pages by default, always outputting a server-rendered site.

 ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ output: ' static ' }) `
 See Also:

- adapter

### adapter
 Section titled “adapter”
 Type: `AstroIntegration`

Deploy to your favorite server, serverless, or edge host with build adapters. Import one of our first-party adapters ( Cloudflare , Netlify , Node.js , Vercel ) or explore community adapters to enable on-demand rendering in your Astro project.

See our on-demand rendering guide for more on Astro’s server rendering options.

 ` import netlify from ' @astrojs/netlify ' ; { // Example: Build for Netlify serverless deployment adapter: netlify (), } `
 See Also:

- output

### integrations
 Section titled “integrations”
 Type: `AstroIntegration[]`

Extend Astro with custom integrations. Integrations are your one-stop-shop for adding framework support (like Solid.js), new features (like sitemaps), and new libraries (like Partytown).

Read our Integrations Guide for help getting started with Astro Integrations.

 ` import react from ' @astrojs/react ' ; import mdx from ' @astrojs/mdx ' ; { // Example: Add React + MDX support to Astro integrations: [ react (), mdx ()] } `

### root
 Section titled “root”
 Type: `string`
 CLI: `--root`
 Default: `"."` (current working directory)

You should only provide this option if you run the `astro` CLI commands in a directory other than the project root directory. Usually, this option is provided via the CLI instead of the Astro config file, since Astro needs to know your project root before it can locate your config file.

If you provide a relative path (ex: `--root: './my-project'`) Astro will resolve it against your current working directory.

#### Examples
 Section titled “Examples”

```
` { root: ' ./my-project-directory ' } `
```

 Terminal window
```
` $ astro build --root ./my-project-directory `
```

### srcDir
 Section titled “srcDir”
 Type: `string`
 Default: `"./src"`

Set the directory that Astro will read your site from.

The value can be either an absolute file system path or a path relative to the project root.

 ` { srcDir: ' ./www ' } `

### publicDir
 Section titled “publicDir”
 Type: `string`
 Default: `"./public"`

Set the directory for your static assets. Files in this directory are served at `/` during dev and copied to your build directory during build. These files are always served or copied as-is, without transform or bundling.

The value can be either an absolute file system path or a path relative to the project root.

 ` { publicDir: ' ./my-custom-publicDir-directory ' } `

### outDir
 Section titled “outDir”
 Type: `string`
 Default: `"./dist"`

Set the directory that `astro build` writes your final build to.

The value can be either an absolute file system path or a path relative to the project root.

 ` { outDir: ' ./my-custom-build-directory ' } `
 See Also:

- build.server

### cacheDir
 Section titled “cacheDir”
 Type: `string`
 Default: `"./node_modules/.astro"`

Set the directory for caching build artifacts. Files in this directory will be used in subsequent builds to speed up the build time.

The value can be either an absolute file system path or a path relative to the project root.

 ` { cacheDir: ' ./my-custom-cache-directory ' } `

### compressHTML
 Section titled “compressHTML”
 Type: `boolean | "jsx"`
 Default: `true`

Controls how Astro handles whitespace in your HTML. This affects both development mode and the final build output.

By default, Astro removes whitespace from your HTML, including line breaks, in a lossless manner from `.astro` components. Some whitespace may be preserved as needed to maintain the visual rendering of your HTML.

Since 6.2.0, this option can also be set to `"jsx"`, Astro will apply the JSX whitespace stripping rules used by frameworks like React. Leading and trailing whitespace is only preserved when explicitly included in the source code through constructs such as `{" "}`, and is otherwise removed entirely.

Setting this option to false disables HTML compression and preserves all whitespace.

 ` { compressHTML: false // or: // compressHTML: 'jsx' } `

### scopedStyleStrategy
 Section titled “scopedStyleStrategy”
 Type: `'where' | 'class' | 'attribute'`
 Default: `'attribute'`

 Added in:
 `astro@2.4`

Specify the strategy used for scoping styles within Astro components. Choose from:

- `'where'` - Use `:where` selectors, causing no specificity increase.

- `'class'` - Use class-based selectors, causing a +1 specificity increase.

- `'attribute'` - Use `data-` attributes, causing a +1 specificity increase.

Using `'class'` is helpful when you want to ensure that element selectors within an Astro component override global style defaults (e.g. from a global stylesheet).
Using `'where'` gives you more control over specificity, but requires that you use higher-specificity selectors, layers, and other tools to control which selectors are applied.
Using `'attribute'` is useful when you are manipulating the `class` attribute of elements and need to avoid conflicts between your own styling logic and Astro’s application of styles.

### prerenderConflictBehavior
 Section titled “prerenderConflictBehavior”
 Type: `'error' | 'warn' | 'ignore'`
 Default: `'warn'`

 Added in:
 `astro@6.0`

Determines the default behavior when two routes generate the same prerendered URL:

- `error`: fail the build and display an error, forcing you to resolve the conflict

- `warn` (default): log a warning when conflicts occur, but build using the highest-priority route

- `ignore`: silently build using the highest-priority route when conflicts occur

 ` { prerenderConflictBehavior: ' error ' } `

### vite
 Section titled “vite”
 Type: `ViteUserConfig`

Pass additional configuration options to Vite. Useful when Astro doesn’t support some advanced configuration that you may need.

View the full `vite` configuration object documentation on vite.dev .

#### Examples
 Section titled “Examples”

```
` { vite: { ssr: { // Example: Force a broken package to skip SSR processing, if needed external: [ ' broken-npm-package ' ], } } } `
```

```
` { vite: { // Example: Add custom vite plugins directly to your Astro project plugins: [ myPlugin ()], } } `
```

### security
 Section titled “security”
 Type: `Record<"checkOrigin", boolean> | undefined`
 Default: `{checkOrigin: true}`

 Added in:
 `astro@4.9.0`

Enables security measures for an Astro website.

These features only exist for pages rendered on demand (SSR) using `server` mode or pages that opt out of prerendering in `static` mode.

By default, Astro will automatically check that the “origin” header
matches the URL sent by each request in on-demand rendered pages. You can
disable this behavior by setting `checkOrigin` to `false`:

 astro.config.mjs ` export default defineConfig ({ output: " server " , security: { checkOrigin: false } }) `

#### security.checkOrigin
 Section titled “security.checkOrigin”
 Type: `boolean`
 Default: `true`

 Added in:
 `astro@4.9.0`

Performs a check that the “origin” header, automatically passed by all modern browsers, matches the URL sent by each `Request`. This is used to provide Cross-Site Request Forgery (CSRF) protection.

The “origin” check is executed only for pages rendered on demand, and only for the requests `POST`, `PATCH`, `DELETE` and `PUT` with
one of the following `content-type` headers: `'application/x-www-form-urlencoded'`, `'multipart/form-data'`, `'text/plain'`.

If the “origin” header doesn’t match the `pathname` of the request, Astro will return a 403 status code and will not render the page.

#### security.allowedDomains
 Section titled “security.allowedDomains”
 Type: `Array<RemotePattern>`
 Default: `[]`

 Added in:
 `astro@5.14.2`

Defines a list of permitted host patterns for incoming requests when using SSR. When configured, Astro will validate the `X-Forwarded-Host` header
against these patterns for security. If the header doesn’t match any allowed pattern, the header is ignored and the request’s original host is used instead.

This prevents host header injection attacks where malicious actors can manipulate the `Astro.url` value by sending crafted `X-Forwarded-Host` headers.

Each pattern can specify `protocol`, `hostname`, and `port`. All three are validated if provided.
The patterns support wildcards for flexible hostname matching:

- `*.example.com` - matches exactly one subdomain level (e.g., `sub.example.com` but not `deep.sub.example.com`)

- `**.example.com` - matches any subdomain depth (e.g., both `sub.example.com` and `deep.sub.example.com`)

 ` { security: { // Example: Allow any subdomain of example.com on https allowedDomains: [ { hostname: ' **.example.com ' , protocol: ' https ' }, { hostname: ' staging.myapp.com ' , protocol: ' https ' , port: ' 443 ' } ] } } `
 In some specific contexts (e.g., applications behind trusted reverse proxies with dynamic domains), you may need to allow all domains. To do this, use an empty object:

 ` { security: { // Allow any domain - use this only when necessary allowedDomains: [{}] } } `
 When not configured, `X-Forwarded-Host` headers are not trusted and will be ignored.

#### security.actionBodySizeLimit
 Section titled “security.actionBodySizeLimit”
 Type: `number`
 Default: `1048576` (1 MB)

 Added in:
 `astro@5.18.0`

Sets the maximum size in bytes allowed for action request bodies.

By default, action request bodies are limited to 1 MB (1048576 bytes) to prevent abuse.
You can increase this limit if your actions need to accept larger payloads, for example when handling file uploads.

 astro.config.mjs ` export default defineConfig ({ security: { actionBodySizeLimit: 10 * 1024 * 1024 // 10 MB } }) `

#### security.serverIslandBodySizeLimit
 Section titled “security.serverIslandBodySizeLimit”
 Type: `number`
 Default: `1048576` (1 MB)

 Added in:
 `astro@6.0.0`

Sets the maximum size in bytes allowed for server island request bodies, which contain the encrypted props and slot HTML passed to the island component.

By default, server island request bodies are limited to 1 MB (1048576 bytes) to prevent abuse.
You can increase this limit if your server islands need to accept larger payloads.

 astro.config.mjs ` export default defineConfig ({ security: { serverIslandBodySizeLimit: 10 * 1024 * 1024 // 10 MB } }) `

#### security.csp
 Section titled “security.csp”
 Type: `boolean | object`
 Default: `false`

 Added in:
 `astro@6.0.0`

Enables support for Content Security Policy (CSP) to help minimize certain types of security threats by controlling which resources a document is allowed to load. This provides additional protection against cross-site scripting (XSS) attacks.

Enabling this feature adds additional security to Astro’s handling of processed and bundled scripts and styles by default, and allows you to further configure these, and additional, content types.

This feature comes with some limitations:

- External scripts and external styles are not supported out of the box, but you can provide your own hashes .

- Astro’s view transitions using the `&#x3C;ClientRouter />` are not supported, but you can consider migrating to the browser native View Transition API instead if you are not using Astro’s enhancements to the native View Transitions and Navigation APIs.

- Shiki isn’t currently supported. By design, Shiki functions use inline styles that cannot work with Astro CSP implementation. Consider using `&#x3C;Prism />` when your project requires both CSP and syntax highlighting.

- `unsafe-inline` directives are incompatible with Astro’s CSP implementation. By default, Astro will emit hashes for all its bundled scripts (e.g. client islands) and all modern browsers will automatically reject `unsafe-inline` when it occurs in a directive with a hash or nonce.

When enabled, Astro will add a `&#x3C;meta>` element inside the `&#x3C;head>` element of each page.
This element will have the `http-equiv="content-security-policy"` attribute, and the `content` attribute will provide values for the `script-src` and `style-src` directives based on the script and styles used in the page.

 ` &#x3C; head > &#x3C; meta http-equiv = " content-security-policy " content = " script-src 'self' 'sha256-somehash'; style-src 'self' 'sha256-somehash'; " > &#x3C;/ head > `   ">
 You can further customize the `&#x3C;meta>` element by enabling this feature with a configuration object that includes additional options.

 security.csp.algorithm Section titled “security.csp.algorithm”
 Type: `"SHA-256" | "SHA-384" | "SHA-512"`
 Default: `'SHA-256'`

 Added in:
 `astro@6.0.0`

The hash function to use when generating the hashes of the styles and scripts emitted by Astro.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ security: { csp: { algorithm: ' SHA-512 ' } } }); `
 security.csp.directives Section titled “security.csp.directives”
 Type: `Array<string>`
 Default: `[]`

 Added in:
 `astro@6.0.0`

A list of CSP directives (beyond `script-src` and `style-src` which are included by default) that defines valid sources for specific content types. These directives are added to all pages.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ security: { csp: { directives: [ " default-src 'self' " , " img-src 'self' https://images.cdn.example.com " ] } } }); `
 After the build, the `&#x3C;meta>` element will add your directives into the `content` value alongside Astro’s default directives:

 ` &#x3C; meta http-equiv = " content-security-policy " content = " default-src 'self'; img-src 'self' 'https://images.cdn.example.com'; script-src 'self' 'sha256-somehash'; style-src 'self' 'sha256-somehash'; " > ` ">
 security.csp.styleDirective Section titled “security.csp.styleDirective”
 Type: `CspStyleDirective`
 Default: `undefined`

 Added in:
 `astro@6.0.0`

A configuration object that allows you to override the default sources for the `style-src` directive with the `resources` property, or to provide additional hashes to be rendered.

 security.csp.styleDirective.hashes Section titled “security.csp.styleDirective.hashes”
 Type: `Array<CspHash>`
 Default: `[]`

 Added in:
 `astro@6.0.0`

A list of additional hashes to be rendered.

You must provide hashes that start with `sha384-`, `sha512-` or `sha256-`. Other values will cause a validation error. These hashes are added to all pages.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ security: { csp: { styleDirective: { hashes: [ " sha384-styleHash " , " sha512-styleHash " , " sha256-styleHash " ] } } } }); `
 After the build, the `&#x3C;meta>` element will include your additional hashes in the `style-src` directives:

 ` &#x3C; meta http-equiv = " content-security-policy " content = " style-src 'self' 'sha384-styleHash' 'sha512-styleHash' 'sha256-styleHash' 'sha256-generatedByAstro'; " > ` ">
 security.csp.styleDirective.resources Section titled “security.csp.styleDirective.resources”
 Type: `Array<string>`
 Default: `[]`

 Added in:
 `astro@6.0.0`

A list of valid sources for `style-src` directives to override Astro’s default sources. This will not include `'self'` by default, and must be included in this list if you wish to keep it. These resources are added to all pages.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ security: { csp: { styleDirective: { resources: [ " 'self' " , " https://styles.cdn.example.com " ] } } } }); `
 After the build, the `&#x3C;meta>` element will instead apply your sources to the `style-src` directives:

 ` &#x3C; head > &#x3C; meta http-equiv = " content-security-policy " content = " style-src 'self' https://styles.cdn.example.com 'sha256-somehash'; " > &#x3C;/ head > `   ">
 When resources are inserted multiple times or from multiple sources (e.g. defined in your `csp` config and added using the CSP runtime API ), Astro will merge and deduplicate all resources to create your `&#x3C;meta>` element.

 security.csp.scriptDirective Section titled “security.csp.scriptDirective”
 Type: `CspScriptDirective`
 Default: `undefined`

 Added in:
 `astro@6.0.0`

A configuration object that allows you to override the default sources for the `script-src` directive with the `resources` property, or to provide additional hashes to be rendered.

 security.csp.scriptDirective.hashes Section titled “security.csp.scriptDirective.hashes”
 Type: `Array<CspHash>`
 Default: `[]`

 Added in:
 `astro@6.0.0`

A list of additional hashes to be rendered.

You must provide hashes that start with `sha384-`, `sha512-` or `sha256-`. Other values will cause a validation error. These hashes are added to all pages.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ security: { csp: { scriptDirective: { hashes: [ " sha384-scriptHash " , " sha512-scriptHash " , " sha256-scriptHash " ] } } } }); `
 After the build, the `&#x3C;meta>` element will include your additional hashes in the `script-src` directives:

 ` &#x3C; meta http-equiv = " content-security-policy " content = " script-src 'self' 'sha384-scriptHash' 'sha512-scriptHash' 'sha256-scriptHash' 'sha256-generatedByAstro'; " > ` ">
 security.csp.scriptDirective.resources Section titled “security.csp.scriptDirective.resources”
 Type: `Array<string>`
 Default: `[]`

 Added in:
 `astro@6.0.0`

A list of valid sources for the `script-src` directives to override Astro’s default sources. This will not include `'self'` by default, and must be included in this list if you wish to keep it. These resources are added to all pages.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ security: { csp: { scriptDirective: { resources: [ " 'self' " , " https://cdn.example.com " ] } } } }); `
 After the build, the `&#x3C;meta>` element will instead apply your sources to the `script-src` directives:

 ` &#x3C; head > &#x3C; meta http-equiv = " content-security-policy " content = " script-src 'self' https://cdn.example.com 'sha256-somehash'; " > &#x3C;/ head > `   ">
 When resources are inserted multiple times or from multiple sources (e.g. defined in your `csp` config and added using the CSP runtime API ), Astro will merge and deduplicate all resources to create your `&#x3C;meta>` element.

 security.csp.scriptDirective.strictDynamic Section titled “security.csp.scriptDirective.strictDynamic”
 Type: `boolean`
 Default: `false`

 Added in:
 `astro@6.0.0`

Enables the `strict-dynamic` keyword to support the dynamic injection of scripts.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ security: { csp: { scriptDirective: { strictDynamic: true } } } }); `

## Build Options
 Section titled “Build Options”

### build.format
 Section titled “build.format”
 Type: `('file' | 'directory' | 'preserve')`
 Default: `'directory'`

Control the output file format of each page. This value may be set by an adapter for you.

- `'file'`: Astro will generate an HTML file named for each page route. (e.g. `src/pages/about.astro` and `src/pages/about/index.astro` both build the file `/about.html`)

- `'directory'`: Astro will generate a directory with a nested `index.html` file for each page. (e.g. `src/pages/about.astro` and `src/pages/about/index.astro` both build the file `/about/index.html`)

- `'preserve'`: Astro will generate HTML files exactly as they appear in your source folder. (e.g. `src/pages/about.astro` builds `/about.html` and `src/pages/about/index.astro` builds the file `/about/index.html`)

 ` { build: { // Example: Generate `page.html` instead of `page/index.html` during build. format: ' file ' } } `

#### Effect on Astro.url
 Section titled “Effect on Astro.url”
 Setting `build.format` controls what `Astro.url` is set to during the build. When it is:

- `directory` - The `Astro.url.pathname` will include a trailing slash to mimic folder behavior. (e.g. `/foo/`)

- `file` - The `Astro.url.pathname` will include `.html`. (e.g. `/foo.html`)

This means that when you create relative URLs using `new URL('./relative', Astro.url)`, you will get consistent behavior between dev and build.

To prevent inconsistencies with trailing slash behaviour in dev, you can restrict the `trailingSlash` option to `'always'` or `'never'` depending on your build format:

- `directory` - Set `trailingSlash: 'always'`

- `file` - Set `trailingSlash: 'never'`

### build.client
 Section titled “build.client”
 Type: `string`
 Default: `'./client'`

Controls the output directory of your client-side CSS and JavaScript when building a website with server-rendered pages.
`outDir` controls where the code is built to.

This value is relative to the `outDir`.

 ` { output: ' server ' , build: { client: ' ./client ' } } `

### build.server
 Section titled “build.server”
 Type: `string`
 Default: `'./server'`

Controls the output directory of server JavaScript when building to SSR.

This value is relative to the `outDir`.

 ` { build: { server: ' ./server ' } } `

### build.assets
 Section titled “build.assets”
 Type: `string`
 Default: `'_astro'`

 Added in:
 `astro@2.0.0`

Specifies the directory in the build output where Astro-generated assets (bundled JS and CSS for example) should live.

 ` { build: { assets: ' _custom ' } } `
 See Also:

- outDir

### build.assetsPrefix
 Section titled “build.assetsPrefix”
 Type: `string | Record<string, string>`
 Default: `undefined`

 Added in:
 `astro@2.2.0`

Specifies the prefix for Astro-generated asset links. This can be used if assets are served from a different domain than the current site.

This requires uploading the assets in your local `./dist/_astro` folder to a corresponding `/_astro/` folder on the remote domain.
To rename the `_astro` path, specify a new directory in `build.assets`.

To fetch all assets uploaded to the same domain (e.g. `https://cdn.example.com/_astro/...`), set `assetsPrefix` to the root domain as a string (regardless of your `base` configuration):

 ` { build: { assetsPrefix: ' https://cdn.example.com ' } } `
 Added in: `astro@4.5.0`

You can also pass an object to `assetsPrefix` to specify a different domain for each file type.
In this case, a `fallback` property is required and will be used by default for any other files.

 ` { build: { assetsPrefix: { ' js ' : ' https://js.cdn.example.com ' , ' mjs ' : ' https://js.cdn.example.com ' , ' css ' : ' https://css.cdn.example.com ' , ' fallback ' : ' https://cdn.example.com ' } } } `

### build.serverEntry
 Section titled “build.serverEntry”
 Type: `string`
 Default: `'entry.mjs'`

Specifies the file name of the server entrypoint when building to SSR.
This entrypoint is usually dependent on which host you are deploying to and
will be set by your adapter for you.

Note that it is recommended that this file ends with `.mjs` so that the runtime
detects that the file is a JavaScript module.

 ` { build: { serverEntry: ' main.mjs ' } } `

### build.redirects
 Section titled “build.redirects”
 Type: `boolean`
 Default: `true`

 Added in:
 `astro@2.6.0`

Specifies whether redirects will be output to HTML during the build.
This option only applies to `output: 'static'` mode; in SSR redirects
are treated the same as all responses.

This option is mostly meant to be used by adapters that have special
configuration files for redirects and do not need/want HTML based redirects.

 ` { build: { redirects: false } } `

### build.inlineStylesheets
 Section titled “build.inlineStylesheets”
 Type: `'always' | 'auto' | 'never'`
 Default: `auto`

 Added in:
 `astro@2.6.0`

Control whether project styles are sent to the browser in a separate css file or inlined into `&#x3C;style>` tags. Choose from the following options:

- `'always'` - project styles are inlined into `&#x3C;style>` tags

- `'auto'` - only stylesheets smaller than `ViteConfig.build.assetsInlineLimit` (default: 4kb) are inlined. Otherwise, project styles are sent in external stylesheets.

- `'never'` - project styles are sent in external stylesheets

 ` { build: { inlineStylesheets: ` never ` , }, } `

### build.concurrency
 Section titled “build.concurrency”
 Type: `number`
 Default: `1`

 Added in:
 `astro@4.16.0`

The number of pages to build in parallel.

 In most cases, you should not change the default value of `1`.

Use this option only when other attempts to reduce the overall rendering time (e.g. batch or cache long running tasks like fetch calls or data access) are not possible or are insufficient.
If the number is set too high, page rendering may slow down due to insufficient memory resources and because JS is single-threaded.

 ` { build: { concurrency: 2 } } `

## Server Options
 Section titled “Server Options”
 Customize the Astro dev server, used by both `astro dev` and `astro preview`.

 ` { server: { port: 1234 , host: true } } `
 To set different configuration based on the command run (“dev”, “preview”) a function can also be passed to this configuration option.

 ` { // Example: Use the function syntax to customize based on command server: ( { command } ) => ({ port: command === ' dev ' ? 4321 : 4000 }) } ` ({ port: command === &#x27;dev&#x27; ? 4321 : 4000 })}">

### server.host
 Section titled “server.host”
 Type: `string | boolean`
 Default: `false`

 Added in:
 `astro@0.24.0`

Set which network IP addresses the server should listen on (i.e. non-localhost IPs).

- `false` - do not expose on a network IP address

- `true` - listen on all addresses, including LAN and public addresses

- `[custom-address]` - expose on a network IP address at `[custom-address]` (ex: `192.168.0.1`)

### server.port
 Section titled “server.port”
 Type: `number`
 Default: `4321`

Set which port the server should listen on.

If the given port is already in use, Astro will automatically try the next available port.

 ` { server: { port: 8080 } } `

### server.allowedHosts
 Section titled “server.allowedHosts”
 Type: `Array<string> | true`
 Default: `[]`

 Added in:
 `astro@5.4.0`

A list of hostnames that Astro is allowed to respond to. When the value is set to `true`, any
hostname is allowed.

 ` { server: { allowedHosts: [ ' staging.example.com ' , ' qa.example.com ' ] } } `

### server.open
 Section titled “server.open”
 Type: `string | boolean`
 Default: `false`

 Added in:
 `astro@4.1.0`

Controls whether the dev server should open in your browser window on startup.

Pass a full URL string (e.g. “ http://example.com ”) or a pathname (e.g. “/about”) to specify the URL to open.

 ` { server: { open: " /about " } } `

### server.headers
 Section titled “server.headers”
 Type: `OutgoingHttpHeaders`
 Default: `{}`

 Added in:
 `astro@1.7.0`

Set custom HTTP response headers to be sent in `astro dev` and `astro preview`.

## Session Options
 Section titled “Session Options”

 Added in:
 `astro@5.7.0`

Configures session storage for your Astro project. This is used to store session data in a persistent way, so that it can be accessed across different requests.

Some adapters may provide a default session driver, but you can override it with your own configuration:

 astro.config.mjs ` import { defineConfig, sessionDrivers } from ' astro/config ' ;
 export default defineConfig ({ session: { driver: sessionDrivers . redis ({ // The options are driver-dependent and some may be required. url: process . env . REDIS_URL }), } }); `
 Session drivers are configured at build time. This means environment variables used in the driver configuration are inlined. You must create your own driver entrypoint to override the configuration at runtime .

See the sessions guide for more information.

### session.driver
 Section titled “session.driver”
 Type: `SessionDriverConfig | undefined`

 Added in:
 `astro@5.7.0`

The driver to use for session storage. The Node ,
 Cloudflare , and
 Netlify adapters automatically configure a default driver for you,
but you can specify your own if you would prefer or if you are using an adapter that does not provide one.

 astro.config.mjs ` import { defineConfig, sessionDrivers } from ' astro/config ' import vercel from ' @astrojs/vercel '
 export default defineConfig ({ adapter: vercel () session : { driver: sessionDrivers . redis ({ url: process . env . REDIS_URL }), } }) `

### session.options
 Section titled “session.options”
 Type: `Record<string, unknown> | undefined`
 Default: `{}`

 Added in:
 `astro@5.7.0`

The driver-specific options to use for session storage. The options depend on the driver you are using. See the Unstorage documentation
for more information on the options available for each driver.

 astro.config.mjs ` { session: { driver: " redis " , options: { url: process . env . REDIS_URL }, } } `

### session.cookie
 Section titled “session.cookie”
 Type: `string | AstroCookieSetOptions | undefined`
 Default: `{ name: "astro-session", sameSite: "lax", httpOnly: true, secure: true }`

 Added in:
 `astro@5.7.0`

The session cookie configuration. If set to a string, it will be used as the cookie name.
Alternatively, you can pass an object with additional options. These will be merged with the defaults.

 astro.config.mjs ` { session: { // If set to a string, it will be used as the cookie name. cookie: " my-session-cookie " , } } `
 astro.config.mjs
```
` { session: { // If set to an object, it will be used as the cookie options. cookie: { name: " my-session-cookie " , sameSite: " lax " , secure: true , } } } `
```

### session.ttl
 Section titled “session.ttl”
 Type: `number | undefined`
 Default: Infinity

 Added in:
 `astro@5.7.0`

An optional default time-to-live expiration period for session values, in seconds.

By default, session values persist until they are deleted or the session is destroyed, and do not automatically expire because a particular amount of time has passed.
Set `session.ttl` to add a default expiration period for your session values. Passing a `ttl` option to `session.set()` will override the global default
for that individual entry.

 astro.config.mjs ` { session: { // Set a default expiration period of 1 hour (3600 seconds) ttl: 3600 , } } `

## Dev Toolbar Options
 Section titled “Dev Toolbar Options”

### devToolbar.enabled
 Section titled “devToolbar.enabled”
 Type: `boolean`
 Default: `true`

Whether to enable the Astro Dev Toolbar. This toolbar allows you to inspect your page islands, see helpful audits on performance and accessibility, and more.

This option is scoped to the entire project, to only disable the toolbar for yourself, run `npm run astro preferences disable devToolbar`. To disable the toolbar for all your Astro projects, run `npm run astro preferences disable devToolbar --global`.

### devToolbar.placement
 Section titled “devToolbar.placement”
 Type: `'bottom-left' | 'bottom-center' | 'bottom-right'`
 Default: `'bottom-center'`

 Added in:
 `astro@5.17.0`

The default placement of the Astro Dev Toolbar on the screen.

The placement of the toolbar can still be changed via the toolbar settings UI. Once changed, the user’s preference is saved in `localStorage` and overrides this configuration value.

## Prefetch Options
 Section titled “Prefetch Options”
 Type: `boolean | object`

Enable prefetching for links on your site to provide faster page transitions.
(Enabled by default on pages using the `&#x3C;ClientRouter />` router. Set `prefetch: false` to opt out of this behaviour.)

This configuration automatically adds a prefetch script to every page in the project
giving you access to the `data-astro-prefetch` attribute.
Add this attribute to any `&#x3C;a />` link on your page to enable prefetching for that page.

 ` &#x3C; a href = " /about " data-astro-prefetch > About &#x3C;/ a > ` About ">
 Further customize the default prefetching behavior using the `prefetch.defaultStrategy` and `prefetch.prefetchAll` options.

See the Prefetch guide for more information.

### prefetch.prefetchAll
 Section titled “prefetch.prefetchAll”
 Type: `boolean`

Enable prefetching for all links, including those without the `data-astro-prefetch` attribute.
This value defaults to `true` when using the `&#x3C;ClientRouter />` router. Otherwise, the default value is `false`.

 ` prefetch: { prefetchAll: true } `
 When set to `true`, you can disable prefetching individually by setting `data-astro-prefetch="false"` on any individual links.

 ` &#x3C; a href = " /about " data-astro-prefetch = " false " > About &#x3C;/ a > ` About ">

### prefetch.defaultStrategy
 Section titled “prefetch.defaultStrategy”
 Type: `'tap' | 'hover' | 'viewport' | 'load'`
 Default: `'hover'`

The default prefetch strategy to use when the `data-astro-prefetch` attribute is set on a link with no value.

- `'tap'`: Prefetch just before you click on the link.

- `'hover'`: Prefetch when you hover over or focus on the link. (default)

- `'viewport'`: Prefetch as the links enter the viewport.

- `'load'`: Prefetch all links on the page after the page is loaded.

You can override this default value and select a different strategy for any individual link by setting a value on the attribute.

 ` &#x3C; a href = " /about " data-astro-prefetch = " viewport " > About &#x3C;/ a > ` About ">

## Image Options
 Section titled “Image Options”

### image.endpoint
 Section titled “image.endpoint”
 Type: `Object`
 Default: `{route: '/_image', entrypoint: undefined}`

 Added in:
 `astro@3.1.0`

Set the endpoint to use for image optimization in dev and SSR. The `entrypoint` property can be set to `undefined` to use the default image endpoint.

 ` { image: { // Example: Use a custom image endpoint at `/custom_endpoint` endpoint: { route: ' /custom_endpoint ' , entrypoint: ' src/my_endpoint.ts ' , }, }, } `

### image.service
 Section titled “image.service”
 Type: `Object`
 Default: `{entrypoint: 'astro/assets/services/sharp', config?: {}}`

 Added in:
 `astro@2.1.0`

Set which image service is used for Astro’s assets support.

The value should be an object with an entrypoint for the image service to use and optionally, a config object to pass to the service.

The service entrypoint can be either one of the included services, or a third-party package.

 ` { image: { // Example: Enable the Sharp-based image service with a custom config service: { entrypoint: ' astro/assets/services/sharp ' , config: { limitInputPixels: false , webp: { effort: 6 , alphaQuality: 80 , }, jpeg: { mozjpeg: true , }, }, }, }, } `

#### image.service.config.limitInputPixels
 Section titled “image.service.config.limitInputPixels”
 Type: `number | boolean`
 Default: `true`

 Added in:
 `astro@4.1.0`

Whether or not to limit the size of images that the Sharp image service will process.

Set `false` to bypass the default image size limit for the Sharp image service and process large images.

#### image.service.config.kernel
 Section titled “image.service.config.kernel”
 Type: `string | undefined`
 Default: `undefined`

 Added in:
 `astro@5.17.0`

The default kernel used for resizing images in the Sharp image service.

By default this is `undefined`, which maps to Sharp’s default kernel of `lanczos3`.

#### image.service.config.jpeg
 Section titled “image.service.config.jpeg”
 Type: `Record<string, any> | undefined`
 Default: `undefined`

 Added in:
 `astro@6.1.0`

The default encoder options passed to `sharp().jpeg()` when using Astro’s built-in Sharp image service.

This can be used for options such as `mozjpeg`, `progressive`, `chromaSubsampling`, or a default `quality`.
Per-image `quality` values from `&#x3C;Image />`, `&#x3C;Picture />`, and `getImage()` still take precedence.

#### image.service.config.webp
 Section titled “image.service.config.webp”
 Type: `Record<string, any> | undefined`
 Default: `undefined`

 Added in:
 `astro@6.1.0`

The default encoder options passed to `sharp().webp()` when using Astro’s built-in Sharp image service.

This can be used for options such as `effort`, `alphaQuality`, `lossless`, `nearLossless`, or a default `quality`.
Per-image `quality` values from `&#x3C;Image />`, `&#x3C;Picture />`, and `getImage()` still take precedence.

#### image.service.config.avif
 Section titled “image.service.config.avif”
 Type: `Record<string, any> | undefined`
 Default: `undefined`

 Added in:
 `astro@6.1.0`

The default encoder options passed to `sharp().avif()` when using Astro’s built-in Sharp image service.

This can be used for options such as `effort`, `chromaSubsampling`, `bitdepth`, `lossless`, or a default `quality`.
Per-image `quality` values from `&#x3C;Image />`, `&#x3C;Picture />`, and `getImage()` still take precedence.

#### image.service.config.png
 Section titled “image.service.config.png”
 Type: `Record<string, any> | undefined`
 Default: `undefined`

 Added in:
 `astro@6.1.0`

The default encoder options passed to `sharp().png()` when using Astro’s built-in Sharp image service.

This can be used for options such as `compressionLevel`, `effort`, `palette`, or a default `quality`.
Per-image `quality` values from `&#x3C;Image />`, `&#x3C;Picture />`, and `getImage()` still take precedence.

### image.dangerouslyProcessSVG
 Section titled “image.dangerouslyProcessSVG”
 Type: `boolean`
 Default: `false`

 Added in:
 `astro@6.3.0`

Allows SVG source images to be processed by the image optimization pipeline.

This is disabled by default as specifically formed SVGs can be prohibitively expensive to process and used by malicious actors to execute denial of service attacks. Only enable this option if you trust the source of your SVG images and understand the risks of processing them.

### image.domains
 Section titled “image.domains”
 Type: `Array<string>`
 Default: `[]`

 Added in:
 `astro@2.10.10`

Defines a list of permitted image source domains for remote image optimization. No other remote images will be optimized by Astro.

This option requires an array of individual domain names as strings. Wildcards are not permitted. Instead, use `image.remotePatterns` to define a list of allowed source URL patterns.

 astro.config.mjs ` { image: { // Example: Allow remote image optimization from a single domain domains: [ ' astro.build ' ], }, } `

### image.remotePatterns
 Section titled “image.remotePatterns”
 Type: `Array<RemotePattern>`
 Default: `[]`

 Added in:
 `astro@2.10.10`

Defines a list of permitted image source URL patterns for remote image optimization.

`remotePatterns` can be configured with four properties:

- protocol

- hostname

- port

- pathname

 ` { image: { // Example: allow processing all images from your aws s3 bucket remotePatterns: [{ protocol: ' https ' , hostname: ' **.amazonaws.com ' , }], }, } `
 You can use wildcards to define the permitted `hostname` and `pathname` values as described below. Otherwise, only the exact values provided will be configured.

`hostname` patterns:

- Start with `**.` to allow all subdomains (like `endsWith`).

- Start with `*.` to allow only one level of subdomain.

`pathname` patterns:

- End with `/**` to allow all sub-routes (like `startsWith`).

- End with `/*` to allow only one level of sub-route.

HTTP redirects are also followed when an image URL matches a remote pattern. The final destination URL must be among the allowed remote patterns to be loaded.

### image.responsiveStyles
 Section titled “image.responsiveStyles”
 Type: `boolean`
 Default: `false`

 Added in:
 `astro@5.10.0`

Whether to automatically add global styles for responsive images. You should enable this option unless you are styling the images yourself.

This option is only used when `layout` is set to `constrained`, `full-width`, or `fixed` using the configuration or the `layout` prop on the image component.

See the images docs for more information.

### image.layout
 Section titled “image.layout”
 Type: `ImageLayout`
 Default: `undefined`

 Added in:
 `astro@5.10.0`

The default layout type for responsive images. Can be overridden by the `layout` prop on the image component.

- `constrained` - The image will scale to fit the container, maintaining its aspect ratio, but will not exceed the specified dimensions.

- `fixed` - The image will maintain its original dimensions.

- `full-width` - The image will scale to fit the container, maintaining its aspect ratio.

See the `layout` component property for more details.

### image.objectFit
 Section titled “image.objectFit”
 Type: `ImageFit`
 Default: `"cover"`

 Added in:
 `astro@5.10.0`

The `object-fit` CSS property value for responsive images. Can be overridden by the `fit` prop on the image component.
Requires a value for `layout` to be set.

See the `fit` component property for more details.

### image.objectPosition
 Section titled “image.objectPosition”
 Type: `string`
 Default: `"center"`

 Added in:
 `astro@5.10.0`

The default `object-position` CSS property value for responsive images. Can be overridden by the `position` prop on the image component.
Requires a value for `layout` to be set.

See the `position` component property for more details.

### image.breakpoints
 Section titled “image.breakpoints”
 Type: `Array<number>`
 Default: `[640, 750, 828, 1080, 1280, 1668, 2048, 2560] | [640, 750, 828, 960, 1080, 1280, 1668, 1920, 2048, 2560, 3200, 3840, 4480, 5120, 6016]`

 Added in:
 `astro@5.10.0`

The breakpoints used to generate responsive images. Requires a value for `layout` to be set. The full list is not normally used,
but is filtered according to the source and output size. The defaults used depend on whether a local or remote image service is used. For remote services
the more comprehensive list is used, because only the required sizes are generated. For local services, the list is shorter to reduce the number of images generated.

## Markdown Options
 Section titled “Markdown Options”

### markdown.shikiConfig
 Section titled “markdown.shikiConfig”
 Type: `Partial&#x3C;ShikiConfig>`

Shiki is our default syntax highlighter. You can configure all options via the `markdown.shikiConfig` object:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ markdown: { shikiConfig: { // Choose from Shiki's built-in themes (or add your own) // https://shiki.style/themes theme: ' dracula ' , // Alternatively, provide multiple themes // See note below for using dual light/dark themes themes: { light: ' github-light ' , dark: ' github-dark ' , }, // Disable the default colors // https://shiki.style/guide/dual-themes#without-default-color // (Added in v4.12.0) defaultColor: false , // Add custom languages // Note: Shiki has countless langs built-in, including .astro! // https://shiki.style/languages langs: [], // Add custom aliases for languages // Map an alias to a Shiki language ID: https://shiki.style/languages#bundled-languages // https://shiki.style/guide/load-lang#custom-language-aliases langAlias: { cjs: " javascript " }, // Enable word wrap to prevent horizontal scrolling wrap: true , // Add custom transformers: https://shiki.style/guide/transformers // Find common transformers: https://shiki.style/packages/transformers transformers: [], }, }, }); `
 See the code syntax highlighting guide for usage and examples.

### markdown.syntaxHighlight
 Section titled “markdown.syntaxHighlight”
 Type: `SyntaxHighlightConfig | SyntaxHighlightConfigType | false`
 Default: `{ type: 'shiki', excludeLangs: ['math'] }`

Which syntax highlighter to use for Markdown code blocks (```), if any. This determines the CSS classes that Astro will apply to your Markdown code blocks.

- `shiki` - use the Shiki highlighter (`github-dark` theme configured by default)

- `prism` - use the Prism highlighter and provide your own Prism stylesheet

- `false` - do not apply syntax highlighting.

 ` { markdown: { // Example: Switch to use prism for syntax highlighting in Markdown syntaxHighlight: ' prism ' , } } `
 For more control over syntax highlighting, you can instead specify a configuration object with the properties listed below.

#### markdown.syntaxHighlight.type
 Section titled “markdown.syntaxHighlight.type”
 Type: `'shiki' | 'prism'`
 Default: `'shiki'`

 Added in:
 `astro@5.5.0`

The default CSS classes to apply to Markdown code blocks.
(If no other syntax highlighting configuration is needed, you can instead set `markdown.syntaxHighlight` directly to `shiki`, `prism`, or `false`.)

#### markdown.syntaxHighlight.excludeLangs
 Section titled “markdown.syntaxHighlight.excludeLangs”
 Type: `Array<string>`
 Default: `['math']`

 Added in:
 `astro@5.5.0`

An array of languages to exclude from the default syntax highlighting specified in `markdown.syntaxHighlight.type`.
This can be useful when using tools that create diagrams from Markdown code blocks, such as Mermaid.js and D2.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ markdown: { syntaxHighlight: { type: ' shiki ' , excludeLangs: [ ' mermaid ' , ' math ' ], }, }, }); `

### markdown.remarkPlugins
 Section titled “markdown.remarkPlugins”

 Type: `RemarkPlugins`

Pass remark plugins to customize how your Markdown is built. You can import and apply the plugin function (recommended), or pass the plugin name as a string.

 ` import remarkToc from ' remark-toc ' ; { markdown: { remarkPlugins: [ [ remarkToc , { heading: " contents " } ] ] } } `

### markdown.rehypePlugins
 Section titled “markdown.rehypePlugins”

 Type: `RehypePlugins`

Pass rehype plugins to customize how your Markdown’s output HTML is processed. You can import and apply the plugin function (recommended), or pass the plugin name as a string.

 ` import { rehypeAccessibleEmojis } from ' rehype-accessible-emojis ' ; { markdown: { rehypePlugins: [ rehypeAccessibleEmojis ] } } `

### markdown.gfm
 Section titled “markdown.gfm”

 Type: `boolean`
 Default: `true`

 Added in:
 `astro@2.0.0`

Astro uses GitHub-flavored Markdown by default. To disable this, set the `gfm` flag to `false`:

 ` { markdown: { gfm: false , } } `

### markdown.smartypants
 Section titled “markdown.smartypants”

 Type: `boolean | Smartypants`
 Default: `true`

 Added in:
 `astro@2.0.0`

Whether to use the SmartyPants formatter to transform straight quotes into smart quotes, dashes into en/em dashes, and triple dots into ellipses.

To disable this, set the `smartypants` flag to `false`.

For more control over typography, you can instead specify a configuration object with the properties supported by `retext-smartypants` .

### markdown.remarkRehype
 Section titled “markdown.remarkRehype”

 Type: `RemarkRehype`

Pass options to remark-rehype .

 ` { markdown: { // Example: Translate the footnotes text to another language, here are the default English values remarkRehype: { footnoteLabel: " Footnotes " , footnoteBackLabel: " Back to reference 1 " }, }, }; `

### markdown.processor
 Section titled “markdown.processor”
 Type: `MarkdownProcessor`

 Added in:
 `astro@6.4.0`
 New

Configures the Markdown processor used to render `.md` files. Defaults to `unified()` from
`@astrojs/markdown-remark` (the remark/rehype pipeline).

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { unified } from ' @astrojs/markdown-remark ' ; import remarkToc from ' remark-toc ' ;
 export default defineConfig ({ markdown: { processor: unified ({ remarkPlugins: [ remarkToc ], }), }, }); `

## i18n
 Section titled “i18n”
 Type: `object`

 Added in:
 `astro@3.5.0`

Configures i18n routing and allows you to specify some customization options.

See our guide for more information on internationalization in Astro

### i18n.locales
 Section titled “i18n.locales”
 Type: `Locales`

 Added in:
 `astro@3.5.0`

A list of all locales supported by the website. This is a required field.

Languages can be listed either as individual codes (e.g. `['en', 'es', 'pt-br']`) or mapped to a shared `path` of codes (e.g. `{ path: "english", codes: ["en", "en-US"]}`). These codes will be used to determine the URL structure of your deployed site.

No particular language code format or syntax is enforced, but your project folders containing your content files must match exactly the `locales` items in the list. In the case of multiple `codes` pointing to a custom URL path prefix, store your content files in a folder with the same name as the `path` configured.

### i18n.defaultLocale
 Section titled “i18n.defaultLocale”
 Type: `string`

 Added in:
 `astro@3.5.0`

The default locale of your website/application, that is one of the specified `locales`. This is a required field.

No particular language format or syntax is enforced, but we suggest using lower-case and hyphens as needed (e.g. “es”, “pt-br”) for greatest compatibility.

### i18n.fallback
 Section titled “i18n.fallback”
 Type: `Record<string, string>`

 Added in:
 `astro@3.5.0`

The fallback strategy when navigating to pages that do not exist (e.g. a translated page has not been created).

Use this object to declare a fallback `locale` route for each language you support. If no fallback is specified, then unavailable pages will return a 404.

 Example Section titled “Example”
 The following example configures your content fallback strategy to redirect unavailable pages in `/pt-br/` to their `es` version, and unavailable pages in `/fr/` to their `en` version. Unavailable `/es/` pages will return a 404.

 ` export default defineConfig ({ i18n: { defaultLocale: " en " , locales: [ " en " , " fr " , " pt-br " , " es " ], fallback: { pt: " es " , fr: " en " } } }) `

### i18n.routing
 Section titled “i18n.routing”
 Type: `object | "manual"`
 Default: `object`

 Added in:
 `astro@3.7.0`

Controls the routing strategy to determine your site URLs. Set this based on your folder/URL path configuration for your default language.

 ` export default defineConfig ({ i18n: { defaultLocale: " en " , locales: [ " en " , " fr " ], routing: { prefixDefaultLocale: false , redirectToDefaultLocale: true , fallbackType: " redirect " , } } }) `
 Since 4.6.0, this option can also be set to `manual`. When this routing strategy is enabled, Astro will disable its i18n middleware and no other `routing` options (e.g. `prefixDefaultLocale`) may be configured. You will be responsible for writing your own routing logic, or executing Astro’s i18n middleware manually alongside your own.

 ` export default defineConfig ({ i18n: { defaultLocale: " en " , locales: [ " en " , " fr " ], routing: " manual " } }) `

#### i18n.routing.prefixDefaultLocale
 Section titled “i18n.routing.prefixDefaultLocale”
 Type: `boolean`
 Default: `false`

 Added in:
 `astro@3.7.0`

When `false`, only non-default languages will display a language prefix.
The `defaultLocale` will not show a language prefix and content files do not exist in a localized folder.
URLs will be of the form `example.com/[locale]/content/` for all non-default languages, but `example.com/content/` for the default locale.

When `true`, all URLs will display a language prefix.
URLs will be of the form `example.com/[locale]/content/` for every route, including the default language.
Localized folders are used for every language, including the default.

 ` export default defineConfig ({ i18n: { defaultLocale: " en " , locales: [ " en " , " fr " , " pt-br " , " es " ], routing: { prefixDefaultLocale: true , } } }) `

#### i18n.routing.redirectToDefaultLocale
 Section titled “i18n.routing.redirectToDefaultLocale”
 Type: `boolean`
 Default: `false`

 Added in:
 `astro@4.2.0`

Configures whether or not the home URL (`/`) generated by `src/pages/index.astro`
will redirect to `/[defaultLocale]` when `prefixDefaultLocale: true` is set.

Set `redirectToDefaultLocale: true` to enable this automatic redirection at the root of your site:

 astro.config.mjs ` export default defineConfig ({ i18n:{ defaultLocale: " en " , locales: [ " en " , " fr " ], routing: { prefixDefaultLocale: true , redirectToDefaultLocale: true } } }) `

#### i18n.routing.fallbackType
 Section titled “i18n.routing.fallbackType”
 Type: `"redirect" | "rewrite"`
 Default: `"redirect"`

 Added in:
 `astro@4.15.0`

When `i18n.fallback` is configured to avoid showing a 404 page for missing page routes, this option controls whether to redirect to the fallback page, or to rewrite the fallback page’s content in place.

By default, Astro’s i18n routing creates pages that redirect your visitors to a new destination based on your fallback configuration. The browser will refresh and show the destination address in the URL bar.

When `i18n.routing.fallback: "rewrite"` is configured, Astro will create pages that render the contents of the fallback page on the original, requested URL.

With the following configuration, if you have the file `src/pages/en/about.astro` but not `src/pages/fr/about.astro`, the `astro build` command will generate `dist/fr/about.html` with the same content as the `dist/en/about.html` page.
Your site visitor will see the English version of the page at `https://example.com/fr/about/` and will not be redirected.

 astro.config.mjs ` export default defineConfig ({ i18n: { defaultLocale: " en " , locales: [ " en " , " fr " ], routing: { prefixDefaultLocale: false , fallbackType: " rewrite " , }, fallback: { fr: " en " , } }, }) `

### i18n.domains
 Section titled “i18n.domains”
 Type: `Record<string, string>`
 Default: `{}`

 Added in:
 `astro@4.3.0`

Configures the URL pattern of one or more supported languages to use a custom domain (or sub-domain).

When a locale is mapped to a domain, a `/[locale]/` path prefix will not be used.
However, localized folders within `src/pages/` are still required, including for your configured `defaultLocale`.

Any other locale not configured will default to a localized path-based URL according to your `prefixDefaultLocale` strategy (e.g. `https://example.com/[locale]/blog`).

 astro.config.mjs ` export default defineConfig ({ site: " https://example.com " , output: " server " , // required, with no prerendered pages adapter: node ({ mode: ' standalone ' , }), i18n: { defaultLocale: " en " , locales: [ " en " , " fr " , " pt-br " , " es " ], prefixDefaultLocale: false , domains: { fr: " https://fr.example.com " , es: " https://example.es " } }, }) `
 Both page routes built and URLs returned by the `astro:i18n` helper functions `getAbsoluteLocaleUrl()` and `getAbsoluteLocaleUrlList()` will use the options set in `i18n.domains`.

See the Internationalization Guide for more details, including the limitations of this feature.

## env
 Section titled “env”
 Type: `object`
 Default: `{}`

 Added in:
 `astro@5.0.0`

Configuration options for type-safe environment variables.

See our guide for more information on environment variables in Astro .

### env.schema
 Section titled “env.schema”
 Type: `EnvSchema`
 Default: `{}`

 Added in:
 `astro@5.0.0`

Defines environment variables to be enforced by Zod validation and for which TypeScript support (e.g. autocompletion, type-safety) is available. Each key corresponds to the variable name and the value to the data type and validations defined with `envField` .

Four data types are supported: string, number, enumeration, and boolean. Each type requires a `context` (client or server), an `access` level (public or secret), and additional validations, such as a `default` value and an indication of whether the variable is `optional` (defaults to `false`).

 astro.config.mjs ` import { defineConfig, envField } from " astro/config "
 export default defineConfig ({ env: { schema: { API_URL: envField . string ({ context: " client " , access: " public " , optional: true }), PORT: envField . number ({ context: " server " , access: " public " , default: 4321 }), API_SECRET: envField . string ({ context: " server " , access: " secret " }), } } }) `

### env.validateSecrets
 Section titled “env.validateSecrets”
 Type: `boolean`
 Default: `false`

 Added in:
 `astro@5.0.0`

Whether or not to validate secrets on the server when starting the dev server or running a build.

By default, only public variables are validated on the server when starting the dev server or a build, and private variables are validated at runtime only. If enabled, private variables will also be checked on start. This is useful in some continuous integration (CI) pipelines to make sure all your secrets are correctly set before deploying.

 astro.config.mjs ` import { defineConfig, envField } from " astro/config "
 export default defineConfig ({ env: { schema: { // ... }, validateSecrets: true } }) `

## fonts
 Section titled “fonts”
 Type: `Array<FontFamily>`
 Default: `[]`

 Added in:
 `astro@6.0.0`

Configures fonts and allows you to specify some customization options on a per-font basis.

See our guide for more information on using custom fonts in Astro .

### font.provider
 Section titled “font.provider”
 Type: `FontProvider`

 Added in:
 `astro@6.0.0`

The source of your font files. You can use a built-in provider or write your own custom provider :

 ` import { defineConfig, fontProviders } from " astro/config " ;
 export default defineConfig ({ fonts: [{ provider: fontProviders . google (), name: " Roboto " , cssVariable: " --font-roboto " }] }); `

### font.name
 Section titled “font.name”
 Type: `string`

 Added in:
 `astro@6.0.0`

The font family name, as identified by your font provider:

 ` name: " Roboto " `

### font.cssVariable
 Section titled “font.cssVariable”
 Type: `string`

 Added in:
 `astro@6.0.0`

A valid ident of your choosing in the form of a CSS variable (i.e. starting with `--`):

 ` cssVariable: " --font-roboto " `

### font.fallbacks
 Section titled “font.fallbacks”
 Type: `Array<string>`
 Default: `["sans-serif"]`

 Added in:
 `astro@6.0.0`

An array of fonts to use when your chosen font is unavailable, or loading. Fallback fonts will be chosen in the order listed. The first available font will be used:

 ` fallbacks: [ " CustomFont " , " serif " ] `
 To disable fallback fonts completely, configure an empty array:

 ` fallbacks: [] `
 Specify at least a generic family name matching the intended appearance of your font. Astro will then attempt to generate optimized fallbacks using font metrics. To disable this optimization, set `optimizedFallbacks` to false.

### font.optimizedFallbacks
 Section titled “font.optimizedFallbacks”
 Type: `boolean`
 Default: `true`

 Added in:
 `astro@6.0.0`

Whether or not to enable Astro’s default optimization when generating fallback fonts. You may disable this default optimization to have full control over how `fallbacks` are generated:

 ` optimizedFallbacks: false `

### font.weights
 Section titled “font.weights”
 Type: `Array<(number|string)>`
 Default: `[400]`

 Added in:
 `astro@6.0.0`

An array of font weights . If no value is specified in your configuration, only weight `400` is included by default to prevent unnecessary downloads. You will need to include this property to access any other font weights:

 ` weights: [ 200 , " 400 " , " bold " ] `
 If the associated font is a variable font , you can specify a range of weights:

 ` weights: [ " 100 900 " ] `

### font.styles
 Section titled “font.styles”
 Type: `Array<("normal"|"italic"|"oblique")>`
 Default: `["normal", "italic"]`

 Added in:
 `astro@6.0.0`

An array of font styles :

 ` styles: [ " normal " , " oblique " ] `

### font.subsets
 Section titled “font.subsets”
 Type: `Array<string>`
 Default: `["latin"]`

 Added in:
 `astro@6.0.0`

Defines a list of font subsets to preload.

 ` subsets: [ " latin " ] `

### font.formats
 Section titled “font.formats”
 Type: `Array<("woff2"|"woff"|"otf"|"ttf"|"eot")>`
 Default: `["woff2"]`

 Added in:
 `astro@6.0.0`

An array of font formats :

 ` formats: [ " woff2 " , " woff " ] `

### font.options
 Section titled “font.options”
 Type: `Record<string, any>`

 Added in:
 `astro@6.0.0`

An object to pass provider specific options. It is typed automatically based on the font family provider :

 ` options: { experimental: { glyphs: [ " a " ] } } `

### font.display
 Section titled “font.display”
 Type: `"auto" | "block" | "swap" | "fallback" | "optional"`
 Default: `"swap"`

 Added in:
 `astro@6.0.0`

Defines how a font displays based on when it is downloaded and ready for use:

 ` display: " block " `

### font.unicodeRange
 Section titled “font.unicodeRange”
 Type: `Array<string>`
 Default: `undefined`

 Added in:
 `astro@6.0.0`

Determines when a font must be downloaded and used based on a specific range of unicode characters . If a character on the page matches the configured range, the browser will download the font and all characters will be available for use on the page. To configure a subset of characters preloaded for a single font, see the subsets property instead.

This can be useful for localization to avoid unnecessary font downloads when a specific part of your website uses a different alphabet and will be displayed with a separate font. For example, a website that offers both English and Japanese versions can prevent the browser from downloading the Japanese font on English versions of the page that do not contain any of the Japanese characters provided in `unicodeRange`.

 ` unicodeRange: [ " U+26 " ] `

### font.stretch
 Section titled “font.stretch”
 Type: `string`
 Default: `undefined`

 Added in:
 `astro@6.0.0`

A font stretch :

 ` stretch: " condensed " `

### font.featureSettings
 Section titled “font.featureSettings”
 Type: `string`
 Default: `undefined`

 Added in:
 `astro@6.0.0`

Controls the typographic font features (e.g. ligatures, small caps, or swashes):

 ` featureSettings: " 'smcp' 2 " `

### font.variationSettings
 Section titled “font.variationSettings”
 Type: `string`
 Default: `undefined`

 Added in:
 `astro@6.0.0`

Font variation settings :

```
` variationSettings: " 'xhgt' 0.7 " `
```

 Reference

 Contribute

 Community

 Sponsor

## Cli Reference

# CLI Commands

 You can use the Command-Line Interface (CLI) provided by Astro to develop, build, and preview your project from a terminal window.

### `astro` commands
 Section titled “astro commands”
 Use the CLI by running one of the commands documented on this page with your preferred package manager, optionally followed by any flags . Flags customize the behavior of a command.

One of the commands you’ll use most often is `astro dev`. This command starts the development server and gives you a live, updating preview of your site in a browser as you work:

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` # start the development server npx astro dev `

 Terminal window
```
` # start the development server pnpm astro dev `
```

 Terminal window
```
` # start the development server yarn astro dev `
```

 You can type `astro --help` in your terminal to display a list of all available commands:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npx astro --help `

 Terminal window
```
` pnpm astro --help `
```

 Terminal window
```
` yarn astro --help `
```

 The following message will display in your terminal:

 Terminal window ` astro [command] [...flags]
 Commands add Add an integration. build Build your project and write it to disk. check Check your project for errors. create-key Create a cryptography key dev Start the development server. docs Open documentation in your web browser. info List info about your current Astro setup. preview Preview your build locally. sync Generate TypeScript types for all Astro modules. preferences Configure user preferences. telemetry Configure telemetry settings.
 Global Flags --config &#x3C;path> Specify your config file. --root &#x3C;path> Specify your project root folder. --site &#x3C;url> Specify your project site. --base &#x3C;pathname> Specify your project base. --verbose Enable verbose logging. --silent Disable all logging. --version Show the version number and exit. --help Show this help message. ` Specify your config file. --root Specify your project root folder. --site Specify your project site.--base Specify your project base. --verbose Enable verbose logging. --silent Disable all logging. --version Show the version number and exit. --help Show this help message.">
 You can add the `--help` flag after any command to get a list of all the flags for that command.

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` # get a list of all flags for the `dev` command npm run dev -- --help `

 Terminal window
```
` # get a list of all flags for the `dev` command pnpm dev --help `
```

 Terminal window
```
` # get a list of all flags for the `dev` command yarn dev --help `
```

 The following message will display in your terminal:

 Terminal window ` astro dev [...flags]
 Flags --port Specify which port to run on. Defaults to 4321. --host Listen on all addresses, including LAN and public addresses. --host &#x3C;custom-address> Expose on a network IP address at &#x3C;custom-address> --open Automatically open the app in the browser on server start --force Clear the content layer cache, forcing a full rebuild. --help (-h) See all available flags. ` Expose on a network IP address at  --open Automatically open the app in the browser on server start --force Clear the content layer cache, forcing a full rebuild. --help (-h) See all available flags.">

### `package.json` scripts
 Section titled “package.json scripts”
 You can also use scripts in `package.json` for shorter versions of these commands. Using a script allows you to use the same commands that you may be familiar with from other projects, such as `npm run build`.

The following scripts for the most common `astro` commands (`astro dev`, `astro build`, and `astro preview`) are added for you automatically when you create a project using the `create astro` wizard .

When you follow the instructions to install Astro manually , you are instructed to add these scripts yourself. You can also add more scripts to this list manually for any commands you use frequently.

 package.json ` { "scripts" : { "dev" : " astro dev " , "build" : " astro build " , "preview" : " astro preview " } } `
 You will often use these `astro` commands, or the scripts that run them, without any flags. Add flags to the command when you want to customize the command’s behavior. For example, you may wish to start the development server on a different port, or build your site with verbose logs for debugging.

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` # run the dev server on port 8080 using the `dev` script in `package.json` npm run dev -- --port 8080
 # build your site with verbose logs using the `build` script in `package.json` npm run build -- --verbose `

 Terminal window
```
` # run the dev server on port 8080 using the `dev` script in `package.json` pnpm dev --port 8080
 # build your site with verbose logs using the `build` script in `package.json` pnpm build --verbose `
```

 Terminal window
```
` # run the dev server on port 8080 using the `dev` script in `package.json` yarn dev --port 8080
 # build your site with verbose logs using the `build` script in `package.json` yarn build --verbose `
```

## `astro dev`
 Section titled “astro dev”
 Runs Astro’s development server. This is a local HTTP server that doesn’t bundle assets. It uses Hot Module Replacement (HMR) to update your browser as you save changes in your editor.

The following hotkeys can be used in the terminal where the Astro development server is running:

- `s + enter` to sync the content layer data (content and types).

- `o + enter` to open your Astro site in the browser.

- `q + enter` to quit the development server.

## `astro build`
 Section titled “astro build”
 Builds your site for deployment. By default, this will generate static files and place them in a `dist/` directory. If any routes are rendered on demand , this will generate the necessary server files to serve your site.

### Flags

The command accepts common flags and the following additional flags:

#### `--devOutput`
 Section titled “--devOutput”

 Added in:
 `astro@5.0.0`

Outputs a development-based build similar to code transformed in `astro dev`. This can be useful to test build-only issues with additional debugging information included.

## `astro preview`
 Section titled “astro preview”
 Starts a local server to serve the contents of your static directory (`dist/` by default) created by running `astro build`.

This command allows you to preview your site locally after building to catch any errors in your build output before deploying it. It is not designed to be run in production. For help with production hosting, check out our guide on Deploying an Astro Website .

The following hotkeys can be used in the terminal where the Astro preview server is running:

- `o` + `enter` to open your Astro site in the browser.

- `q` + `enter` to quit the preview server.

The `astro preview` command can be combined with the common flags documented below to further control the preview experience.

## `astro check`
 Section titled “astro check”
 Runs diagnostics (such as type-checking within `.astro` files) against your project and reports errors to the console. If any errors are found the process will exit with a code of 1 .

This command is intended to be used in CI workflows.

### Flags

Use these flags to customize the behavior of the command.

#### `--watch`
 Section titled “--watch”
 The command will watch for any changes in your project, and will report any errors.

#### `--root &#x3C;path-to-dir>`
 Section titled “--root &#x3C;path-to-dir>”
 Specifies a different root directory to check. Uses the current working directory by default.

#### `--tsconfig &#x3C;path-to-file>`
 Section titled “--tsconfig &#x3C;path-to-file>”
 Specifies a `tsconfig.json` file to use manually. If not provided, Astro will attempt to find a config, or infer the project’s config automatically.

#### `--minimumFailingSeverity &#x3C;error|warning|hint>`
 Section titled “--minimumFailingSeverity &#x3C;error|warning|hint>”
 Specifies the minimum severity needed to exit with an error code. Defaults to `error`.

For example, running `astro check --minimumFailingSeverity warning` will cause the command to exit with an error if any warnings are detected.

#### `--minimumSeverity &#x3C;error|warning|hint>`
 Section titled “--minimumSeverity &#x3C;error|warning|hint>”
 Specifies the minimum severity to output. Defaults to `hint`.

For example, running `astro check --minimumSeverity warning` will show errors and warning, but not hints.

#### `--preserveWatchOutput`
 Section titled “--preserveWatchOutput”
 Specifies not to clear the output between checks when in watch mode.

#### `--noSync`
 Section titled “--noSync”
 Specifies not to run `astro sync` before checking the project.

 Read more about type checking in Astro .

## `astro sync`
 Section titled “astro sync”

 Added in:
 `astro@2.0.0`

Generates TypeScript types for all Astro modules. This sets up a `.astro/types.d.ts` file for type inferencing, and defines modules for features that rely on generated types:

- The `astro:content` module for the Content Collections API .

- The `astro:db` module for Astro DB .

- The `astro:env` module for Astro Env .

- The `astro:actions` module for Astro Actions

## `astro add`
 Section titled “astro add”
 Adds an integration to your configuration. Read more in the integrations guide .

## `astro docs`
 Section titled “astro docs”
 Launches the Astro Docs website directly from the terminal.

## `astro info`
 Section titled “astro info”
 Reports useful information about your current Astro environment. Useful for providing information when opening an issue.

 Terminal window ` astro info `
 Example output:

 ` Astro v5.14.1 Vite v6.3.6 Node v22.17.1 System macOS (arm64) Package Manager npm Output static Adapter none Integrations @astrojs/starlight (v0.35.3) `

### Flags

 Use the following flags to customize the behavior of the command.

#### `--copy`
 Section titled “--copy”
 The command will copy the output to the clipboard without prompting.

## `astro preferences`
 Section titled “astro preferences”
 Manage user preferences with the `astro preferences` command. User preferences are specific to individual Astro users, unlike the `astro.config.mjs` file which changes behavior for everyone working on a project.

User preferences are scoped to the current project by default, stored in a local `.astro/settings.json` file.

Using the `--global` flag, user preferences can also be applied to every Astro project on the current machine. Global user preferences are stored in an operating system-specific location.

### Available preferences

- `devToolbar` — Enable or disable the development toolbar in the browser. (Default: `true`)

- `checkUpdates` — Enable or disable automatic update checks for the Astro CLI. (Default: `true`)

The `list` command prints the current settings of all configurable user preferences. It also supports a machine-readable `--json` output.

 Terminal window ` astro preferences list `
 Example terminal output:

 | ** Preference** | **Value** |
 | devToolbar.enabled | true |
 | checkUpdates.enabled | true |

You can `enable`, `disable`, or `reset` preferences to their default.

For example, to disable the devToolbar in a specific Astro project:

 Terminal window ` astro preferences disable devToolbar `
 To disable the devToolbar in all Astro projects on the current machine:

 Terminal window ` astro preferences disable --global devToolbar `
 The devToolbar can later be enabled with:

 Terminal window ` astro preferences enable devToolbar `
 The `reset` command resets a preference to its default value:

 Terminal window ` astro preferences reset devToolbar `

## `astro telemetry`
 Section titled “astro telemetry”
 Sets telemetry configuration for the current CLI user. Telemetry is anonymous data that provides the Astro team insights into which Astro features are most often used. For more information see Astro’s telemetry page .

Telemetry can be disabled with this CLI command:

 Terminal window ` astro telemetry disable `
 Telemetry can later be re-enabled with:

 Terminal window ` astro telemetry enable `
 The `reset` command resets the telemetry data:

 Terminal window ` astro telemetry reset `

## `astro create-key`
 Section titled “astro create-key”
 Generates a key to encrypt props passed to server islands.

 Terminal window ` astro create-key `
 Set this key as the `ASTRO_KEY` environment variable (e.g. in a `.env` file) and include it in your CI/CD or host’s build settings when you need a constant encryption key for your server islands for situations like rolling deployments, multi-region hosting or a CDN that caches pages containing server islands.

## Common flags
 Section titled “Common flags”

### `--root &#x3C;path>`
 Section titled “--root &#x3C;path>”
 Specifies the path to the project root. If not specified, the current working directory is assumed to be the root.

The root is used for finding the Astro configuration file.

 Terminal window ` astro --root myRootFolder/myProjectFolder dev `

### `--config &#x3C;path>`
 Section titled “--config &#x3C;path>”
 Specifies the path to the config file relative to the project root. Defaults to `astro.config.mjs`. Use this if you use a different name for your configuration file or have your config file in another folder.

 Terminal window ` astro --config config/astro.config.mjs dev `

### `--force &#x3C;string>`
 Section titled “--force &#x3C;string>”

 Added in:
 `astro@5.0.0`

Clear the content layer cache, forcing a full rebuild.

### `--mode &#x3C;string>`
 Section titled “--mode &#x3C;string>”

 Added in:
 `astro@5.0.0`

Configures the `mode` inline config for your project.

### `--outDir &#x3C;path>`
 Section titled “--outDir &#x3C;path>”

 Added in:
 `astro@3.3.0`

Configures the `outDir` for your project. Passing this flag will override the `outDir` value in your `astro.config.mjs` file, if one exists.

### `--site &#x3C;url>`
 Section titled “--site &#x3C;url>”
 Configures the `site` for your project. Passing this flag will override the `site` value in your `astro.config.mjs` file, if one exists.

### `--base &#x3C;pathname>`
 Section titled “--base &#x3C;pathname>”

 Added in:
 `astro@1.4.1`

Configures the `base` for your project. Passing this flag will override the `base` value in your `astro.config.mjs` file, if one exists.

### `--port &#x3C;number>`
 Section titled “--port &#x3C;number>”
 Specifies which port to run the dev server and preview server on. Defaults to `4321`.

### `--host [optional host address]`
 Section titled “--host [optional host address]”
 Sets which network IP addresses the dev server and preview server should listen on (i.e. non-localhost IPs). This can be useful for testing your project on local devices like a mobile phone during development.

- `--host` — listen on all addresses, including LAN and public addresses

- `--host &#x3C;custom-address>` — expose on a network IP address at `&#x3C;custom-address>`

### `--allowed-hosts`
 Section titled “--allowed-hosts”

 Added in:
 `astro@5.4.0`

Specifies the hostnames that Astro is allowed to respond to in `dev` or `preview` modes. Can be passed a comma-separated list of hostnames or `true` to allow any hostname.

Refer to Vite’s `allowedHosts` feature for more information, including security implications of allowing hostnames.

### `--verbose`
 Section titled “--verbose”
 Enables verbose logging, which is helpful when debugging an issue.

### `--silent`
 Section titled “--silent”
 Enables silent logging, which will run the server without any console output.

### `--open`
 Section titled “--open”
 Automatically opens the app in the browser on server start. Can be passed a full URL string (e.g. `--open http://example.com`) or a pathname (e.g. `--open /about`) to specify the URL to open.

## Global flags
 Section titled “Global flags”
 Use these flags to get information about the `astro` CLI.

### `--version`
 Section titled “--version”
 Prints the Astro version number and exits.

### `--help`
 Section titled “--help”
 Prints the help message and exits.

 Reference

 Contribute

 Community

 Sponsor

## Imports

# Imports reference

 Astro supports most static assets with zero configuration required. You can use the `import` statement anywhere in your project JavaScript (including your Astro frontmatter) and Astro will include a built, optimized copy of that static asset in your final build. `@import` is also supported inside of CSS &#x26; `&#x3C;style>` tags.

## Supported File Types
 Section titled “Supported File Types”
 The following file types are supported out-of-the-box by Astro:

- Astro Components (`.astro`)

- Markdown (`.md`, `.markdown`, etc.)

- JavaScript (`.js`, `.mjs`)

- TypeScript (`.ts`)

- NPM Packages

- JSON (`.json`)

- CSS (`.css`)

- CSS Modules (`.module.css`)

- Images &#x26; Assets (`.svg`, `.jpg`, `.png`, etc.)

Additionally, you can extend Astro to add support for different UI Frameworks like React, Svelte and Vue components. You can also install the Astro MDX integration or the Astro Markdoc integration to use `.mdx` or `.mdoc` files in your project.

### Files in `public/`
 Section titled “Files in public/”
 You can place any static asset in the `public/` directory of your project, and Astro will copy it directly into your final build untouched. `public/` files are not built or bundled by Astro, which means that any type of file is supported.

You can reference a `public/` file by a URL path directly in your HTML templates.

 - ` // To link to /public/reports/annual/2024.pdf Download the &#x3C; a href = " /reports/annual/2024.pdf " > 2024 annual statement as a PDF &#x3C;/ a > .
 // To display /public/assets/cats/ginger.jpg &#x3C; img src = " /assets/cats/ginger.jpg " alt = " An orange cat sleeping on a bed. " > ` 2024 annual statement as a PDF .// To display /public/assets/cats/ginger.jpg ">

## Import statements
 Section titled “Import statements”
 Astro uses ESM, the same `import` and `export` syntax supported in the browser.

### JavaScript
 Section titled “JavaScript”

```
` import { getUser } from ' ./user.js ' ; `
```

 JavaScript can be imported using normal ESM `import` &#x26; `export` syntax.

### TypeScript
 Section titled “TypeScript”

```
` import { getUser } from ' ./user ' ; import type { UserType } from ' ./user ' ; `
```

 Astro includes built-in support for TypeScript . You can import `.ts` and `.tsx` files directly in your Astro project, and even write TypeScript code directly inside your Astro component script and any script tags .

 Astro doesn’t perform any type checking itself. Type checking should be taken care of outside of Astro, either by your IDE or through a separate script. For type checking Astro files, the `astro check` command is provided.

 Read more about TypeScript support in Astro .

### NPM Packages
 Section titled “NPM Packages”
 If you’ve installed an NPM package, you can import it in Astro.

 ` --- import { Icon } from ' astro-icon ' ; --- `
 If a package was published using a legacy format, Astro will try to convert the package to ESM so that `import` statements work. In some cases, you may need to adjust your `vite` config for it to work.

### JSON
 Section titled “JSON”

```
` // Load the JSON object via the default export import json from ' ./data.json ' ; `
```

 Astro supports importing JSON files directly into your application. Imported files return the full JSON object in the default import.

### CSS
 Section titled “CSS”

```
` // Load and inject 'style.css' onto the page import ' ./style.css ' ; `
```

 Astro supports importing CSS files directly into your application. Imported styles expose no exports, but importing one will automatically add those styles to the page. This works for all CSS files by default, and can support compile-to-CSS languages like Sass &#x26; Less via plugins.

 Read more about advanced CSS import use cases such as a direct URL reference for a CSS file, or importing CSS as a string in the Styling guide .

### CSS Modules
 Section titled “CSS Modules”

```
` // 1. Converts './style.module.css' classnames to unique, scoped values. // 2. Returns an object mapping the original classnames to their final, scoped value. import styles from ' ./style.module.css ' ;
 // This example uses JSX, but you can use CSS Modules with any framework. return &#x3C; div className = { styles . error } > Your Error Message &#x3C;/ div > ; `
```
 Your Error Message ;">
 Astro supports CSS Modules using the `[name].module.css` naming convention. Like any CSS file, importing one will automatically apply that CSS to the page. However, CSS Modules export a special default `styles` object that maps your original classnames to unique identifiers.

CSS Modules help you enforce component scoping &#x26; isolation on the frontend with uniquely-generated class names for your stylesheets.

### Other Assets
 Section titled “Other Assets”

```
` // Returns an object with `src` and other properties import imgReference from ' ./image.png ' ; import svgReference from ' ./image.svg ' ;
 // HTML or UI Framework components use this to render the image &#x3C; img src = { imgReference . src } alt = " image description " /> ;
 // The Astro `&#x3C;Image />` and `&#x3C;Picture />` components access `src` by default &#x3C; Image src = { imgReference } alt = " image description " > `
```
 ;// The Astro &#x60; &#x60; and &#x60; &#x60; components access &#x60;src&#x60; by default ">
 All other assets not explicitly mentioned above can be imported via ESM `import` and will return a URL reference to the final built asset (e.g. `/_astro/my-video.C7vXpQtF.mp4`) instead of an object.

This can be useful for referencing non-JS assets by URL, like creating a video element with a `src` attribute pointing to that image.

It can also be useful to place images and other assets in the `public/` folder as explained on the project-structure page .

 Read more about appending Vite import parameters (e.g. `?url`, `?raw`) in Vite’s static asset handling guide .

## Aliases
 Section titled “Aliases”
 An alias is a way to create shortcuts for your imports.

Aliases can help improve the development experience in codebases with many directories or relative imports.

 src/pages/about/company.astro ` --- import Button from ' ../../components /controls/Button.astro ' ; import logoUrl from ' ../../assets /logo.png?url ' ; --- `
 In this example, a developer would need to understand the tree relationship between `src/pages/about/company.astro`, `src/components/controls/Button.astro`, and `src/assets/logo.png`. And then, if the `company.astro` file were to be moved, these imports would also need to be updated.

You can add import aliases in `tsconfig.json`.

 tsconfig.json ` { "compilerOptions" : { "paths" : { "@components/*" : [ " ./src/components/* " ], "@assets/*" : [ " ./src/assets/* " ] } } } `
 The development server will automatically restart after this configuration change. You can now import using the aliases anywhere in your project:

 src/pages/about/company.astro ` --- import Button from ' @components /controls/Button.astro ' ; import logoUrl from ' @assets /logo.png?url ' ; --- `

## `import.meta.glob()`
 Section titled “import.meta.glob()”
 Vite’s `import.meta.glob()` is a way to import many files at once using glob patterns to find matching file paths.

`import.meta.glob()` takes a relative glob pattern matching the local files you’d like to import as a parameter. It returns an array of each matching file’s exports. To load all matched modules up front, pass `{ eager: true }` as the second argument:

 src/components/my-component.astro ` --- // imports all files that end with `.md` in `./src/pages/post/` const matches = import. meta . glob ( ' ../pages/post/*.md ' , { eager: true } ); const posts = Object . values (matches); --- &#x3C;!-- Renders an &#x3C;article> for the first 5 blog posts --> &#x3C; div > { posts . slice ( 0 , 4 ) . map ( ( post ) => ( &#x3C; article > &#x3C; h2 > { post . frontmatter . title } &#x3C;/ h2 > &#x3C; p > { post . frontmatter . description } &#x3C;/ p > &#x3C; a href = { post . url } > Read more &#x3C;/ a > &#x3C;/ article > )) } &#x3C;/ div > ` {posts.slice(0, 4).map((post) => ( 
## {post.frontmatter.title}
 {post.frontmatter.description}
 Read more  ))} ">
Astro components imported using `import.meta.glob` are of type `AstroInstance` . You can render each component instance using its `default` property:

 src/pages/component-library.astro ` --- // imports all files that end with `.astro` in `./src/components/` const components = Object . values ( import. meta . glob ( ' ../components/*.astro ' , { eager: true } )); --- &#x3C;!-- Display all of our components --> { components . map ( ( component ) => ( &#x3C; div > &#x3C; component.default size = { 24 } /> &#x3C;/ div > )) } ` (   ))}">

### Supported Values
 Section titled “Supported Values”
 Vite’s `import.meta.glob()` function only supports static string literals. It does not support dynamic variables and string interpolation.

A common workaround is to instead import a larger set of files that includes all the files you need, then filter them:

 src/components/featured.astro ` --- const { postSlug } = Astro . props ; const pathToMyFeaturedPost = ` src/pages/blog/ ${ postSlug } .md ` ;
 const posts = Object . values ( import. meta . glob ( " ../pages/blog/*.md " , { eager: true } )); const myFeaturedPost = posts . find ( post => post . file . includes (pathToMyFeaturedPost)); ---
 &#x3C; p > Take a look at my favorite post, &#x3C; a href = { myFeaturedPost . url } > { myFeaturedPost . frontmatter . title } &#x3C;/ a > ! &#x3C;/ p > ` post.file.includes(pathToMyFeaturedPost));---  Take a look at my favorite post, {myFeaturedPost.frontmatter.title} !
">

### Import type utilities
 Section titled “Import type utilities”

#### Markdown files
 Section titled “Markdown files”
 Markdown files loaded with `import.meta.glob()` return the following `MarkdownInstance` interface:

 ` export interface MarkdownInstance&#x3C; T extends Record &#x3C; string , any >> { /* Any data specified in this file's YAML/TOML frontmatter */ frontmatter : T ; /* The absolute file path of this file */ file : string ; /* The rendered path of this file */ url : string | undefined ; /* Astro Component that renders the contents of this file */ Content : AstroComponentFactory ; /** (Markdown only) Raw Markdown file content, excluding layout HTML and YAML/TOML frontmatter */ rawContent () : string ; /** (Markdown only) Markdown file compiled to HTML, excluding layout HTML */ compiledContent () : string ; /* Function that returns an array of the h1...h6 elements in this file */ getHeadings () : Promise &#x3C;{ depth : number ; slug : string ; text : string }[]>; default : AstroComponentFactory ; } ` > { /* Any data specified in this file&#x27;s YAML/TOML frontmatter */ frontmatter: T; /* The absolute file path of this file */ file: string; /* The rendered path of this file */ url: string | undefined; /* Astro Component that renders the contents of this file */ Content: AstroComponentFactory; /** (Markdown only) Raw Markdown file content, excluding layout HTML and YAML/TOML frontmatter */ rawContent(): string; /** (Markdown only) Markdown file compiled to HTML, excluding layout HTML */ compiledContent(): string; /* Function that returns an array of the h1...h6 elements in this file */ getHeadings(): Promise ; default: AstroComponentFactory;}">
 You can optionally provide a type for the `frontmatter` variable using a TypeScript generic.

 ` --- import type { MarkdownInstance } from ' astro ' ; interface Frontmatter { title : string ; description ?: string ; }
 const posts = Object . values ( import. meta . glob &#x3C; MarkdownInstance &#x3C; Frontmatter >> ( ' ./posts/**/*.md ' , { eager: true } )); ---
 &#x3C; ul > { posts . map ( post => &#x3C; li > { post . frontmatter . title } &#x3C;/ li > ) } &#x3C;/ ul > ` >(&#x27;./posts/**/*.md&#x27;, { eager: true }));---  {posts.map(post => {post.frontmatter.title}
)} ">

#### Astro files
 Section titled “Astro files”
 Astro files have the following interface:

 ` export interface AstroInstance { /* The file path of this file */ file : string ; /* The URL for this file (if it is in the pages directory) */ url : string | undefined ; default : AstroComponentFactory ; } `

#### Other files
 Section titled “Other files”
 Other files may have various different interfaces, but `import.meta.glob()` accepts a TypeScript generic if you know exactly what an unrecognized file type contains.

 ` -- - interface CustomDataFile { default : Record &#x3C; string , any >; } const data = import. meta . glob &#x3C; CustomDataFile > ( ' ../data/**/*.js ' ); -- - ` ;}const data = import.meta.glob (&#x27;../data/**/*.js&#x27;);---">

### Glob Patterns
 Section titled “Glob Patterns”
 A glob pattern is a file path that supports special wildcard characters. This is used to reference multiple files in your project at once.

For example, the glob pattern `./pages/**/*.{md,mdx}` starts within the pages subdirectory, looks through all of its subdirectories (`/**`), and matches any filename (`/*`) that ends in either `.md` or `.mdx` (`.{md,mdx}`).

#### Glob Patterns in Astro
 Section titled “Glob Patterns in Astro”
 To use with `import.meta.glob()`, the glob pattern must be a string literal and cannot contain any variables.

Additionally, glob patterns must begin with one of the following:

- `./` (to start in the current directory)

- `../` (to start in the parent directory)

- `/` (to start at the root of the project)

 Read more about the glob pattern syntax .

### `import.meta.glob()` vs `getCollection()`
 Section titled “import.meta.glob() vs getCollection()”
 Content collections provide performant, content-focused APIs for loading multiple files instead of `import.meta.glob()`. Use `getCollection()` and `getLiveCollection()` to query your collections and return content entries.

## WASM
 Section titled “WASM”

```
` // Loads and initializes the requested WASM file const wasm = await WebAssembly . instantiateStreaming ( fetch ( ' /example.wasm ' )); `
```

 Astro supports loading WASM files directly into your application using the browser’s `WebAssembly` API.

## Node Builtins
 Section titled “Node Builtins”
 Astro supports Node.js built-ins, with some limitations, using Node’s newer `node:` prefix. There may be differences between development and production, and some features may be incompatible with on-demand rendering. Some adapters may also be incompatible with these built-ins modules or require configuration to support a subset (e.g., Cloudflare Workers or Deno ).

The following example imports the `util` module from Node to parse a media type (MIME):

 src/components/MyComponent.astro ` --- // Example: import the "util" built-in from Node.js import util from ' node:util ' ;
 export interface Props { mimeType : string , }
 const mime = new util . MIMEType (Astro . props . mimeType ) ---
 &#x3C; span > Type: { mime . type } &#x3C;/ span > &#x3C; span > SubType: { mime . subtype } &#x3C;/ span > ` Type: {mime.type}  SubType: {mime.subtype} ">

## Extending file type support
 Section titled “Extending file type support”
 With Vite and compatible Rollup plugins, you can import file types which aren’t natively supported by Astro. Learn where to find the plugins you need in the Finding Plugins section of the Vite Documentation.

 Related recipe:

 Installing a Vite or Rollup plugin

 Learn

 Contribute

 Community

 Sponsor

## Routing Reference

# Routing Reference

 There is no separate routing configuration in Astro.

Every supported page file located within the special `src/pages/` directory creates a route. When the file name contains a parameter , a route can create multiple pages dynamically, otherwise it creates a single page.

By default, all Astro page routes and endpoints are generated and prerendered at build time. On-demand server rendering can be set for individual routes, or as the default.

## `prerender`
 Section titled “prerender”
 Type: `boolean`
 Default: `true` in static mode (default); `false` with `output: 'server'` configuration

 Added in:
 `astro@1.0.0`

A value exported from each individual route to determine whether or not it is prerendered.

By default, all pages and endpoints are prerendered and will be statically generated at build time. You can opt out of prerendering on one or more routes, and you can have both static and on-demand rendered routes in the same project.

### Per-page override
 Section titled “Per-page override”
 You can override the default value to enable on demand rendering for an individual route by exporting `prerender` with the value `false` from that file:

 - src/pages/rendered-on-demand.astro ` --- export const prerender = false --- &#x3C;!-- server-rendered content --> &#x3C;!-- the rest of my site is static --> `

### Switch to `server` mode
 Section titled “Switch to server mode”
 You can override the default value for all routes by configuring `output: 'server'` . In this output mode, all pages and endpoints will be generated on the server upon request by default instead of being prerendered.

In `server` mode, enable prerendering for an individual route by exporting `prerender` with the value `true` from that file:

 src/pages/static-about-page.astro ` --- // with `output: 'server'` configured export const prerender = true --- &#x3C;!-- My static about page --> &#x3C;!-- All other pages are rendered on demand --> `

## `partial`
 Section titled “partial”
 Type: `boolean`
 Default: `false`

 Added in:
 `astro@3.4.0`

A value exported from an individual route to determine whether or not it should be rendered as a full HTML page.

By default, all files located within the reserved `src/pages/` directory automatically include the `&#x3C;!DOCTYPE html>` declaration and additional `&#x3C;head>` content such as Astro’s scoped styles and scripts.

You can override the default value to designate the content as a page partial for an individual route by exporting a value for `partial` from that file:

 src/pages/my-page-partial.astro ` --- export const partial = true --- &#x3C;!-- Generated HTML available at a URL --> &#x3C;!-- Available to a rendering library --> `
 The `export const partial` must be identifiable statically. It can have the value of:

 The boolean `true` .

- An environment variable using import.meta.env such as `import.meta.env.USE_PARTIALS`.

## `getStaticPaths()`
 Section titled “getStaticPaths()”
 Type: `(options: GetStaticPathsOptions) => Promise<GetStaticPathsResult> | GetStaticPathsResult`

 Added in:
 `astro@1.0.0`

A function to generate multiple, prerendered page routes from a single `.astro` page component with one or more parameters in its file path. Use this for routes that will be created at build time, also known as static site building.

The `getStaticPaths()` function must return an array of objects to determine which URL paths will be prerendered by Astro. Each object must include a `params` object, to specify route paths. The object may optionally contain a `props` object with data to be passed to each page template.

 src/pages/blog/[post].astro ` --- // In 'server' mode, opt in to prerendering: // export const prerender = true
 export async function getStaticPaths () { return [ // { params: { /* required */ }, props: { /* optional */ } }, { params: { post : ' 1 ' } } , // [ post ] is the parameter { params: { post : ' 2 ' } } , // must match the file name // ... ]; } --- &#x3C;!-- Your HTML template here. --> `
 `getStaticPaths()` can also be used in static file endpoints for dynamic routing .

### `params`
 Section titled “params”
 The `params` key of each object in the array returned by `getStaticPaths()` tells Astro what routes to build.

The keys in `params` must match the parameters defined in your component file path. The value for each `params` object must match the parameters used in the page name. `params` are encoded into the URL, so only strings are supported as values.

For example,`src/pages/posts/[id].astro`has an `id` parameter in its file name. The following `getStaticPaths()` function in this `.astro` component tells Astro to statically generate `posts/1`, `posts/2`, and `posts/3` at build time.

 src/pages/posts/[id].astro ` --- export async function getStaticPaths () { return [ { params: { id: ' 1 ' } } , { params: { id: ' 2 ' } } , { params: { id: ' 3 ' } } ]; }
 const { id } = Astro . params ; --- &#x3C; h1 > { id } &#x3C;/ h1 > `

### Data passing with `props`
 Section titled “Data passing with props”
 To pass additional data to each generated page, you can set a `props` value on each object in the array returned by `getStaticPaths()`. Unlike `params`, `props` are not encoded into the URL and so aren’t limited to only strings.

For example, if you generate pages with data fetched from a remote API, you can pass the full data object to the page component inside of `getStaticPaths()`. The page template can reference the data from each post using `Astro.props`.

 src/pages/posts/[id].astro ` --- export async function getStaticPaths () { const response = await fetch ( ' ... ' ); const data = await response . json ();
 return data . map ( ( post ) => { return { params: { id: post . id } , props: { post } , }; }); }
 const { id } = Astro . params ; const { post } = Astro . props ; --- &#x3C; h1 > { id } : { post . name } &#x3C;/ h1 > ` { return { params: { id: post.id }, props: { post }, }; });}const { id } = Astro.params;const { post } = Astro.props;---
# {id}: {post.name}
">

### `routePattern`
 Section titled “routePattern”
 Type: `string`

 Added in:
 `astro@5.14.0`

A property available in `getStaticPaths()` options to access the current `routePattern` as a string.

This provides data from the Astro render context that would not otherwise be available within the scope of `getStaticPaths()` and can be useful to calculate the `params` and `props` for each page route.

`routePattern` always reflects the original dynamic segment definition in the file path (e.g. `/[...locale]/[files]/[slug]`), unlike `params`, which are explicit values for a page (e.g. `/fr/fichiers/article-1/`).

The following example shows how to localize your route segments and return an array of static paths by passing `routePattern` to a custom `getLocalizedData()` helper function. The params object will be set with explicit values for each route segment: `locale`, `files`, and `slug`. Then, these values will be used to generate the routes and can be used in your page template via `Astro.params`.

 src/pages/[...locale]/[files]/[slug].astro ` --- import { getLocalizedData } from " ../../../utils/i18n " ;
 export async function getStaticPaths ( { routePattern } ) { const response = await fetch ( ' ... ' ); const data = await response . json ();
 console . log ( routePattern ); // [...locale]/[files]/[slug]
 // Call your custom helper with ` routePattern ` to generate the static paths return data . flatMap ( ( file ) => getLocalizedData (file , routePattern )); }
 const { locale , files , slug } = Astro . params ; --- ` getLocalizedData(file, routePattern));}const { locale, files, slug } = Astro.params;---">

### `paginate()`
 Section titled “paginate()”

 Added in:
 `astro@1.0.0`

A function that can be returned from `getStaticPaths()` to divide a collection of content items into separate pages.

`paginate()` will automatically generate the necessary array to return from `getStaticPaths()` to create one URL for every page of your paginated collection. The page number will be passed as a `param`, and the page data will be passed as a `page` prop.

The following example fetches and passes 150 items to the `paginate` function, and creates static, prerendered pages at build time that will display 10 items per page:

 src/pages/pokemon/[page].astro ` --- export async function getStaticPaths ( { paginate } ) { // Load your data with fetch(), getCollection(), etc. const response = await fetch ( ` https://pokeapi.co/api/v2/pokemon?limit=150 ` ); const result = await response . json (); const allPokemon = result . results ;
 // Return a paginated collection of paths for all items return paginate (allPokemon , { pageSize: 10 }); }
 const { page } = Astro . props ; --- `
 `paginate()` has the following arguments:

- `data` - array containing the page’s data passed to the `paginate()` function

- `options` - Optional object with the following properties:

 `pageSize` - The number of items shown per page (`10` by default)

- `params` - Send additional parameters for creating dynamic routes

- `props` - Send additional props to be available on each page

`paginate()` assumes a file name of `[page].astro` or `[...page].astro`. The `page` param becomes the page number in your URL:

- `/posts/[page].astro` would generate the URLs `/posts/1`, `/posts/2`, `/posts/3`, etc.

- `/posts/[...page].astro` would generate the URLs `/posts`, `/posts/2`, `/posts/3`, etc.

#### The pagination `page` prop
 Section titled “The pagination page prop”
 Type: `Page&#x3C;TData>`

Pagination will pass a `page` prop to every rendered page that represents a single page of data in the paginated collection. This includes the data that you’ve paginated (`page.data`) as well as metadata for the page (`page.url`, `page.start`, `page.end`, `page.total`, etc). This metadata is useful for things like a “Next Page” button or a “Showing 1-10 of 100” message.

 `page.data` Section titled “page.data”
 Type: `Array&#x3C;TData>`

Array of data returned from the `paginate()` function for the current page.

 `page.start` Section titled “page.start”
 Type: `number`

Index of the first item on the current page, starting at `0`. (e.g. if `pageSize: 25`, this would be `0` on page 1, `25` on page 2, etc.)

 `page.end` Section titled “page.end”
 Type: `number`

Index of the last item on the current page.

 `page.size` Section titled “page.size”
 Type: `number`
 Default: `10`

The total number of items per page.

 `page.total` Section titled “page.total”
 Type: `number`

The total number of items across all pages.

 `page.currentPage` Section titled “page.currentPage”
 Type: `number`

The current page number, starting with `1`.

 `page.lastPage` Section titled “page.lastPage”
 Type: `number`

The total number of pages.

 `page.url.current` Section titled “page.url.current”
 Type: `string`

Get the URL of the current page (useful for canonical URLs). If a value is set for `base` , the URL starts with that value.

 `page.url.prev` Section titled “page.url.prev”
 Type: `string | undefined`

Get the URL of the previous page (will be `undefined` if on page 1). If a value is set for `base` , prepend the base path to the URL.

 `page.url.next` Section titled “page.url.next”
 Type: `string | undefined`

Get the URL of the next page (will be `undefined` if no more pages). If a value is set for `base` , prepend the base path to the URL.

 `page.url.first` Section titled “page.url.first”
 Type: `string | undefined`

 Added in:
 `astro@4.12.0`

Get the URL of the first page (will be `undefined` if on page 1). If a value is set for `base` , prepend the base path to the URL.

 `page.url.last` Section titled “page.url.last”
 Type: `string | undefined`

 Added in:
 `astro@4.12.0`

Get the URL of the last page (will be `undefined` if no more pages). If a value is set for `base` , prepend the base path to the URL.

 Reference

 Contribute

 Community

 Sponsor

## Api Reference

# Astro render context

 When rendering a page, Astro provides a runtime API specific to the current render. This includes useful information such as the current page URL as well as APIs to perform actions like redirecting to another page.

In `.astro` components, this context is available from the `Astro` global object. Endpoint functions are also called with this same context object as their first argument, whose properties mirror the Astro global properties.

Some properties are only available for routes rendered on demand or may have limited functionality on prerendered pages.

The `Astro` global object is available to all `.astro` files. Use the `context` object in endpoint functions to serve static or live server endpoints and in middleware to inject behavior when a page or endpoint is about to be rendered.

## The context object
 Section titled “The context object”
 The following properties are available on the `Astro` global (e.g. `Astro.props`, `Astro.redirect()`) and are also available on the context object (e.g. `context.props`, `context.redirect()`) passed to endpoint functions and middleware.

### `props`
 Section titled “props”
 `props` is an object containing any values that have been passed as component attributes .

 - src/components/Heading.astro ` --- const { title , date } = Astro . props ; --- &#x3C; div > &#x3C; h1 > { title } &#x3C;/ h1 > &#x3C; p > { date } &#x3C;/ p > &#x3C;/ div > ` 
# {title}
 {date}
 ">
 src/pages/index.astro ` --- import Heading from ' ../components/Heading.astro ' ; --- &#x3C; Heading title = " My First Post " date = " 09 Aug 2022 " /> ` ">

 Learn more about how Markdown and MDX layouts handle props.

 The `props` object also contains any `props` passed from `getStaticPaths()` when rendering static routes.

 Astro.props

-

 context.props

 src/pages/posts/[id].astro ` --- export function getStaticPaths () { return [ { params: { id: ' 1 ' } , props: { author: ' Blu ' } } , { params: { id: ' 2 ' } , props: { author: ' Erika ' } } , { params: { id: ' 3 ' } , props: { author: ' Matthew ' } } ]; }
 const { id } = Astro . params ; const { author } = Astro . props ; --- `

 src/pages/posts/[id].json.ts
```
` import type { APIContext } from ' astro ' ;
 export function getStaticPaths () { return [ { params: { id: ' 1 ' } , props: { author: ' Blu ' } } , { params: { id: ' 2 ' } , props: { author: ' Erika ' } } , { params: { id: ' 3 ' } , props: { author: ' Matthew ' } } ]; }
 export function GET ( { props } : APIContext ) { return new Response ( JSON . stringify ({ author: props . author }) , ); } `
```

 See also: Data Passing with `props`

### `params`
 Section titled “params”
 `params` is an object containing the values of dynamic route segments matched for a request. Its keys must match the parameters in the page or endpoint file path.

In static builds, this will be the `params` returned by `getStaticPaths()` used for prerendering dynamic routes :

 -

 Astro.params

-

 context.params

 src/pages/posts/[id].astro ` --- export function getStaticPaths () { return [ { params: { id: ' 1 ' } } , { params: { id: ' 2 ' } } , { params: { id: ' 3 ' } } ]; } const { id } = Astro . params ; --- &#x3C; h1 > { id } &#x3C;/ h1 > `

 src/pages/posts/[id].json.ts
```
` import type { APIContext } from ' astro ' ;
 export function getStaticPaths () { return [ { params: { id: ' 1 ' } } , { params: { id: ' 2 ' } } , { params: { id: ' 3 ' } } ]; }
 export function GET ( { params } : APIContext ) { return new Response ( JSON . stringify ({ id: params . id }) , ); } `
```

 When routes are rendered on demand, `params` can be any value matching the path segments in the dynamic route pattern.

 src/pages/posts/[id].astro ` --- import { getPost } from ' ../api ' ;
 const post = await getPost ( Astro . params . id );
 // No posts found with this ID if ( ! post) { return Astro . redirect ( " /404 " ) } --- &#x3C; html > &#x3C; h1 > { post . name } &#x3C;/ h1 > &#x3C;/ html > ` 
# {post.name}
 ">
 See also: `params`

### `url`
 Section titled “url”
 Type: `URL`

 Added in:
 `astro@1.0.0`

`url` is a URL object constructed from the current `request.url` value. It is useful for interacting with individual properties of the request URL, like pathname and origin.

`Astro.url` is equivalent to doing `new URL(Astro.request.url)`.

`url` will be a `localhost` URL in dev mode. When building a site, prerendered routes will receive a URL based on the `site` and `base` options. If `site` is not configured, prerendered pages will receive a `localhost` URL during builds as well.

 src/pages/index.astro ` &#x3C; h1 > The current URL is: { Astro . url } &#x3C;/ h1 > &#x3C; h1 > The current URL pathname is: { Astro . url . pathname } &#x3C;/ h1 > &#x3C; h1 > The current URL origin is: { Astro . url . origin } &#x3C;/ h1 > `
 You can also use `url` to create new URLs by passing it as an argument to `new URL()` .

 src/pages/index.astro ` --- // Example: Construct a canonical URL using your production domain const canonicalURL = new URL ( Astro . url . pathname , Astro . site ); // Example: Construct a URL for SEO meta tags using your current domain const socialImageURL = new URL ( ' /images/preview.png ' , Astro . url ); --- &#x3C; link rel = " canonical " href = { canonicalURL } /> &#x3C; meta property = " og:image " content = { socialImageURL } /> ` ">

### `site`
 Section titled “site”
 Type: `URL | undefined`

`site` returns a `URL` made from `site` in your Astro config. It returns `undefined` if you have not set a value for `site` in your Astro config.

 src/pages/index.astro ` &#x3C; link rel = " alternate " type = " application/rss+xml " title = " Your Site's Title " href = { new URL ( " rss.xml " , Astro . site ) } /> ` ">

### `clientAddress`
 Section titled “clientAddress”
 Type: `string`

 Added in:
 `astro@1.0.0`

`clientAddress` specifies the IP address of the request. This property is only available for routes rendered on demand and cannot be used on prerendered pages.

 Astro.clientAddress

-

 context.clientAddress

 src/pages/ip-address.astro ` --- export const prerender = false ; // Not needed in 'server' mode ---
 &#x3C; div > Your IP address is: &#x3C; span class = " address " > { Astro . clientAddress } &#x3C;/ span >&#x3C;/ div > ` Your IP address is: {Astro.clientAddress} ">

 src/pages/ip-address.ts
```
` export const prerender = false ; // Not needed in 'server' mode import type { APIContext } from ' astro ' ;
 export function GET ( { clientAddress } : APIContext ) { return new Response ( ` Your IP address is: ${ clientAddress } ` ); } `
```

### `isPrerendered`
 Section titled “isPrerendered”
 Type : `boolean`

 Added in:
 `astro@5.0.0`

A boolean representing whether or not the current page is prerendered.

You can use this property to run conditional logic in middleware, for example, to avoid accessing headers in prerendered pages.

### `generator`
 Section titled “generator”
 Type: `string`

 Added in:
 `astro@1.0.0`

`generator` provides the current version of Astro your project is running. This is a convenient way to add a `&#x3C;meta name="generator">` tag with your current version of Astro. It follows the format `"Astro v5.x.x"`.

 -

 Astro.generator

-

 context.generator

 src/pages/site-info.astro ` &#x3C; html > &#x3C; head > &#x3C; meta name = " generator " content = { Astro . generator } /> &#x3C;/ head > &#x3C; body > &#x3C; footer > &#x3C; p > Built with &#x3C; a href = " https://astro.build " > { Astro . generator } &#x3C;/ a >&#x3C;/ p > &#x3C;/ footer > &#x3C;/ body > &#x3C;/ html > `        ">

 src/pages/site-info.json.ts
```
` import type { APIContext } from ' astro ' ;
 export function GET ( { generator , site } : APIContext ) { const body = JSON . stringify ( { generator , site } ); return new Response (body); } `
```

### `request`
 Section titled “request”
 Type: `Request`

`request` is a standard Request object. It can be used to get the `url`, `headers`, `method`, and even the body of the request.

 -

 Astro.request

-

 context.request

 src/pages/index.astro ` &#x3C; p > Received a { Astro . request . method } request to " { Astro . request . url } ". &#x3C;/ p > &#x3C; p > Received request headers: &#x3C;/ p > &#x3C; p >&#x3C; code > { JSON . stringify (Object . fromEntries ( Astro . request . headers )) } &#x3C;/ code >&#x3C;/ p > ` Received a {Astro.request.method} request to &#x22;{Astro.request.url}&#x22;.
Received request headers:
`{JSON.stringify(Object.fromEntries(Astro.request.headers))}`
">

 ` import type { APIContext } from ' astro ' ;
 export function GET ( { request } : APIContext ) { return new Response ( ` Hello ${ request . url } ` ); } `

### `response`
 Section titled “response”
 Type: `ResponseInit &#x26; { readonly headers: Headers }`

`response` is a standard `ResponseInit` object. It has the following structure.

- `status`: The numeric status code of the response, e.g., `200`.

- `statusText`: The status message associated with the status code, e.g., `'OK'`.

- `headers`: A `Headers` instance that you can use to set the HTTP headers of the response.

`Astro.response` is used to set the `status`, `statusText`, and `headers` for a page’s response.

 ` --- if (condition) { Astro . response . status = 404 ; Astro . response . statusText = ' Not found ' ; } --- `
 Or to set a header:

 ` --- Astro . response . headers . set ( ' Set-Cookie ' , ' a=b; Path=/; ' ); --- `

### `redirect()`
 Section titled “redirect()”
 Type: `(path: string, status?: number) => Response`

 Added in:
 `astro@1.5.0`

`redirect()` returns a Response object that allows you to redirect to another page, and optionally provide an HTTP response status code as a second parameter.

A page (and not a child component) must `return` the result of `Astro.redirect()` for the redirect to occur.

For statically-generated routes, this will produce a client redirect using a `&#x3C;meta http-equiv="refresh">` tag and does not support status codes.

For on-demand rendered routes, setting a custom status code is supported when redirecting. If not specified, redirects will be served with a `302` status code.

The following example redirects a user to a login page:

 -

 Astro.redirect()

-

 context.redirect()

 src/pages/account.astro ` --- import { isLoggedIn } from ' ../utils ' ;
 const cookie = Astro . request . headers . get ( ' cookie ' );
 // If the user is not logged in, redirect them to the login page if ( ! isLoggedIn (cookie)) { return Astro . redirect ( ' /login ' ); } ---
 &#x3C; p > User information &#x3C;/ p > ` User information
">

 ` import type { APIContext } from ' astro ' ;
 export function GET ( { redirect , request } : APIContext ) { const cookie = request . headers . get ( ' cookie ' ); if ( ! isLoggedIn (cookie)) { return redirect ( ' /login ' , 302 ); } else { // return user information } } `

### `rewrite()`
 Section titled “rewrite()”
 Type: `(rewritePayload: string | URL | Request) => Promise<Response>`

 Added in:
 `astro@4.13.0`

`rewrite()` allows you to serve content from a different URL or path without redirecting the browser to a new page.

The method accepts either a string, a `URL`, or a `Request` for the location of the path.

Use a string to provide an explicit path:

 -

 Astro.rewrite()

-

 context.rewrite()

 src/pages/index.astro ` --- return Astro . rewrite ( " /login " ) --- `

```
` import type { APIContext } from ' astro ' ;
 export function GET ( { rewrite } : APIContext ) { return rewrite ( ' /login ' ); } `
```

 Use a `URL` type when you need to construct the URL path for the rewrite. The following example renders a page’s parent path by creating a new URL from the relative `"../"` path:

 -

 Astro.rewrite()

-

 context.rewrite()

 src/pages/blog/index.astro ` --- return Astro . rewrite ( new URL ( " ../ " , Astro . url )) --- `

```
` import type { APIContext } from ' astro ' ;
 export function GET ( { rewrite } : APIContext ) { return rewrite ( new URL ( " ../ " , Astro . url )); } `
```

 Use a `Request` type for complete control of the `Request` sent to the server for the new path. The following example sends a request to render the parent page while also providing headers:

 -

 Astro.rewrite()

-

 context.rewrite()

 src/pages/blog/index.astro ` --- return Astro . rewrite ( new Request ( new URL ( " ../ " , Astro . url ), { headers: { " x-custom-header " : JSON . stringify (Astro . locals . someValue ) } })) --- `

```
` import type { APIContext } from ' astro ' ;
 export function GET ( { rewrite } : APIContext ) { return rewrite ( new Request ( new URL ( " ../ " , Astro . url ) , { headers: { " x-custom-header " : JSON . stringify (Astro . locals . someValue ) } })); } `
```

### `originPathname`
 Section titled “originPathname”
 Type: `string`

 Added in:
 `astro@5.0.0`

`originPathname` defines the original pathname of the request, before rewrites were applied.

 -

 Astro.originPathname

-

 context.originPathname

 src/pages/404.astro ` &#x3C; p > The origin path is { Astro . originPathname } &#x3C;/ p > &#x3C; p > The rewritten path is { Astro . url . pathname } &#x3C;/ p > ` The origin path is {Astro.originPathname}
The rewritten path is {Astro.url.pathname}
">

 src/middleware.ts ` import { defineMiddleware } from ' astro:middleware ' ;
 export const onRequest = defineMiddleware ( async ( context , next ) => { // Record the original pathname before any rewrites recordPageVisit (context . originPathname ) ; return next () ; } ); ` { // Record the original pathname before any rewrites recordPageVisit(context.originPathname); return next();});">

### `locals`
 Section titled “locals”

 Added in:
 `astro@2.4.0`

`locals` is an object used to store and access arbitrary information during the lifecycle of a request. `Astro.locals` is an object containing any values from the `context.locals` object set by middleware. Use this to access data returned by middleware in your `.astro` files.

Middleware functions can both read and write the values of `context.locals`:

 src/middleware.ts ` import type { MiddlewareHandler } from ' astro ' ;
 export const onRequest : MiddlewareHandler = ( { locals }, next ) => { if ( ! locals . title ) { locals . title = " Default Title " ; } return next () ; } ` { if (!locals.title) { locals.title = &#x22;Default Title&#x22;; } return next();}">
 Astro components and API endpoints can read values from `locals` when they render:

 -

 Astro.locals

-

 context.locals

 src/pages/Orders.astro ` --- const title = Astro . locals . title ; --- &#x3C; h1 > { title } &#x3C;/ h1 > `

 src/pages/hello.ts
```
` import type { APIContext } from ' astro ' ;
 export function GET ( { locals } : APIContext ) { return new Response ( locals . title ); // "Default Title" } `
```

### `preferredLocale`
 Section titled “preferredLocale”
 Type: `string | undefined`

 Added in:
 `astro@3.5.0`

`preferredLocale` is a computed value to find the best match between your visitor’s browser language preferences and the locales supported by your site.

It is computed by checking the configured locales in your `i18n.locales` array and the locales supported by the user’s browser via the header `Accept-Language`. This value is `undefined` if no such match exists.

This property is only available for routes rendered on demand and cannot be used on prerendered, static pages.

### `preferredLocaleList`
 Section titled “preferredLocaleList”
 Type: `string[] | undefined`

 Added in:
 `astro@3.5.0`

`preferredLocaleList` represents the array of all locales that are both requested by the browser and supported by your website. This produces a list of all compatible languages between your site and your visitor.

If none of the browser’s requested languages are found in your locales array, then the value is `[]`. This occurs when you do not support any of your visitor’s preferred locales.

If the browser does not specify any preferred languages, then this value will be `i18n.locales` : all of your supported locales will be considered equally preferred by a visitor with no preferences.

This property is only available for routes rendered on demand and cannot be used on prerendered, static pages.

### `currentLocale`
 Section titled “currentLocale”
 Type: `string | undefined`

 Added in:
 `astro@3.5.6`

The locale computed from the current URL, using the syntax specified in your `locales` configuration. If the URL does not contain a `/[locale]/` prefix, then the value will default to `i18n.defaultLocale` .

### `getActionResult()`
 Section titled “getActionResult()”
 Type: `(action: TAction) => ActionReturnType<TAction> | undefined`

 Added in:
 `astro@4.15.0`

`getActionResult()` is a function that returns the result of an Action submission. This accepts an action function as an argument (e.g. `actions.logout`) and returns a `data` or `error` object when a submission is received. Otherwise, it will return `undefined`.

 src/pages/index.astro ` --- import { actions } from ' astro:actions ' ;
 const result = Astro . getActionResult (actions . logout ); ---
 &#x3C; form action = { actions . logout } > &#x3C; button type = " submit " > Log out &#x3C;/ button > &#x3C;/ form > { result ?. error &#x26;&#x26; &#x3C; p > Failed to log out. Please try again. &#x3C;/ p > } `  Log out  {result?.error &#x26;&#x26; Failed to log out. Please try again.
}">

### `callAction()`
 Section titled “callAction()”

 Added in:
 `astro@4.15.0`

`callAction()` is a function used to call an Action handler directly from your Astro component. This function accepts an Action function as the first argument (e.g. `actions.logout`) and any input that action receives as the second argument. It returns the result of the action as a promise.

 src/pages/index.astro ` --- import { actions } from ' astro:actions ' ;
 const { data , error } = await Astro . callAction (actions . logout , { userId: ' 123 ' } ); --- `

### `routePattern`
 Section titled “routePattern”
 Type : `string`

 Added in:
 `astro@5.0.0`

The route pattern responsible for generating the current page or route. In file-based routing, this resembles the file path in your project used to create the route. When integrations create routes for your project, `context.routePattern` is identical to the value for `injectRoute.pattern`.

The value will start with a leading slash and look similar to the path of a page component relative to your `src/pages/` folder without a file extension.

For example, the file `src/pages/en/blog/[slug].astro` will return `/en/blog/[slug]` for `routePattern`. Every page on your site generated by that file (e.g. `/en/blog/post-1/`, `/en/blog/post-2/`, etc.) shares the same value for `routePattern`. In the case of `index.*` routes, the route pattern will not include the word “index.” For example, `src/pages/index.astro` will return `/`.

You can use this property to understand which route is rendering your component. This allows you to target or analyze similarly-generated page URLs together. For example, you can use it to conditionally render certain information, or collect metrics about which routes are slower.

### `cookies`
 Section titled “cookies”
 Type: `AstroCookies`

 Added in:
 `astro@1.4.0`

`cookies` contains utilities for reading and manipulating cookies for routes rendered on demand .

#### Cookie utilities
 Section titled “Cookie utilities”
 `cookies.get()` Section titled “cookies.get()”
 Type: `(key: string, options?: AstroCookieGetOptions ) => AstroCookie | undefined`

Gets the cookie as an `AstroCookie` object, which contains the `value` and utility functions for converting the cookie to non-string types.

 `cookies.has()` Section titled “cookies.has()”
 Type: `(key: string, options?: AstroCookieGetOptions ) => boolean`

Whether this cookie exists. If the cookie has been set via `Astro.cookies.set()` this will return true, otherwise, it will check cookies in the `Astro.request`.

 `cookies.set()` Section titled “cookies.set()”
 Type: `(key: string, value: string | object, options?: AstroCookieSetOptions ) => void`

Sets the cookie `key` to the given value. This will attempt to convert the cookie value to a string. Options provide ways to set cookie features , such as the `maxAge` or `httpOnly`.

 `cookies.delete()` Section titled “cookies.delete()”
 Type: `(key: string, options?: AstroCookieDeleteOptions) => void`

Invalidates a cookie by setting the expiration date in the past (0 in Unix time).

Once a cookie is “deleted” (expired), `Astro.cookies.has()` will return `false` and `Astro.cookies.get()` will return an `AstroCookie` with a `value` of `undefined`. Options available when deleting a cookie are: `domain`, `path`, `httpOnly`, `sameSite`, and `secure`.

 `cookies.merge()` Section titled “cookies.merge()”
 Type: `(cookies: AstroCookies) => void`

Merges a new `AstroCookies` instance into the current instance. Any new cookies will be added to the current instance and any cookies with the same name will overwrite existing values.

 `cookies.headers()` Section titled “cookies.headers()”
 Type: `() => Iterator&#x3C;string>`

Gets the header values for `Set-Cookie` that will be sent out with the response.

 `cookies.consume()` Section titled “cookies.consume()”
 Type: `() => Iterator<string>`

 Added in:
 `astro@6.3.0`

Marks the cookies as consumed and returns the `Set-Cookie` header values, similar to `cookies.headers()` . After calling `consume()`, any subsequent calls to `cookies.set()` will log a warning, since the cookie headers have already been sent to the browser. This is used internally by adapters to ensure cookies are only serialized once into the response.

#### `AstroCookie` Type
 Section titled “AstroCookie Type”
 The type returned from getting a cookie via `Astro.cookies.get()`. It has the following properties:

 `AstroCookie.value` Section titled “AstroCookie.value”
 Type: `string`

The raw string value of the cookie.

 `AstroCookie.json()` Section titled “AstroCookie.json()”
 Type: `() => Record&#x3C;string, any>`

Parses the cookie value via `JSON.parse()`, returning an object. Throws if the cookie value is not valid JSON.

 `AstroCookie.number()` Section titled “AstroCookie.number()”
 Type: `() => number`

Parses the cookie value as a Number. Returns NaN if not a valid number.

 `AstroCookie.boolean()` Section titled “AstroCookie.boolean()”
 Type: `() => boolean`

Converts the cookie value to a boolean.

#### `AstroCookieGetOptions`
 Section titled “AstroCookieGetOptions”

 Added in:
 `astro@4.1.0`

The `AstroCookieGetOption` interface allows you to specify options when you get a cookie.

 `AstroCookieGetOptions.decode()` Section titled “AstroCookieGetOptions.decode()”
 Type: `(value: string) => string`

Allows customization of how a cookie is deserialized into a value.

#### `AstroCookieSetOptions`
 Section titled “AstroCookieSetOptions”

 Added in:
 `astro@4.1.0`

`AstroCookieSetOptions` is an object that can be passed to `Astro.cookies.set()` when setting a cookie to customize how the cookie is serialized.

 `AstroCookieSetOptions.domain` Section titled “AstroCookieSetOptions.domain”
 Type: `string`

Specifies the domain. If no domain is set, most clients will interpret to apply to the current domain.

 `AstroCookieSetOptions.expires` Section titled “AstroCookieSetOptions.expires”
 Type: `Date`

Specifies the date on which the cookie will expire.

 `AstroCookieSetOptions.httpOnly` Section titled “AstroCookieSetOptions.httpOnly”
 Type: `boolean`

If true, the cookie will not be accessible client-side.

 `AstroCookieSetOptions.maxAge` Section titled “AstroCookieSetOptions.maxAge”
 Type: `number`

Specifies a number, in seconds, for which the cookie is valid.

 `AstroCookieSetOptions.path` Section titled “AstroCookieSetOptions.path”
 Type: `string`

Specifies a subpath of the domain in which the cookie is applied.

 `AstroCookieSetOptions.partitioned` Section titled “AstroCookieSetOptions.partitioned”
 Type: `boolean`

 Added in:
 `astro@5.17.0`

If true, the cookie is a partitioned cookie . Partitioned cookies can only be read within the context of the top-level site on which they were set, which allows cross-site tracking to be blocked while still enabling legitimate uses of third-party cookies.

Partitioned cookies must be set with `secure: true`.

 `AstroCookieSetOptions.sameSite` Section titled “AstroCookieSetOptions.sameSite”
 Type: `boolean | 'lax' | 'none' | 'strict'`

Specifies the value of the SameSite cookie header.

 `AstroCookieSetOptions.secure` Section titled “AstroCookieSetOptions.secure”
 Type: `boolean`

If true, the cookie is only set on https sites.

 `AstroCookieSetOptions.encode()` Section titled “AstroCookieSetOptions.encode()”
 Type: `(value: string) => string`

Allows customizing how the cookie is serialized.

### `session`
 Section titled “session”
 Type: `AstroSession`

 Added in:
 `astro@5.7.0`

`session` is an object that allows data to be stored between requests for routes rendered on demand . It is associated with a cookie that contains the session ID only: the data itself is not stored in the cookie.

The session is created when first used, and the session cookie is automatically set. The `session` object is `undefined` if no session storage has been configured, or if the current route is prerendered, and will log an error if you try to use it.

See the session guide for more information on how to use sessions in your Astro project.

#### `session.get()`
 Section titled “session.get()”
 Type : `(key: string) => Promise&#x3C;any>`

Returns the value of the given key in the session. If the key does not exist, it returns `undefined`.

 -

 Astro.session

-

 context.session

 src/components/Cart.astro ` --- const cart = await Astro . session ?. get ( ' cart ' ) ; --- &#x3C; button > 🛒 { cart ?. length } &#x3C;/ button > ` 🛒 {cart?.length} ">

 src/pages/api/cart.ts
```
` import type { APIContext } from ' astro ' ;
 export async function GET ( { session } : APIContext ) { const cart = await session . get ( ' cart ' ) ; return Response . json ({ cart }); } `
```

#### `session.set()`
 Section titled “session.set()”
 Type : `(key: string, value: any, options?: { ttl: number }) => void`

Sets the value of the given key in the session. The value can be any serializable type. This method is synchronous and the value is immediately available for retrieval, but it is not saved to the backend until the end of the request. The `ttl` option sets the value’s expiration time, in seconds.

 -

 Astro.session

-

 context.session

 src/pages/products/[slug].astro ` --- const { slug } = Astro . params ; Astro . session ?. set ( ' lastViewedProduct ' , slug) ; --- `

 src/pages/api/add-to-cart.ts
```
` import type { APIContext } from ' astro ' ;
 export async function POST ( { session , request } : APIContext ) { const cart = await session . get ( ' cart ' ); const newItem = await request . json (); cart . push (newItem); // Save the updated cart to the session session . set ( ' cart ' , cart) ; return Response . json ({ cart }); } `
```

#### `session.regenerate()`
 Section titled “session.regenerate()”
 Type : `() => void`

Regenerates the session ID. Call this when a user logs in or escalates their privileges, to prevent session fixation attacks.

 -

 Astro.session

-

 context.session

 src/pages/welcome.astro ` --- Astro . session ?. regenerate () ; --- `

 src/pages/api/login.ts
```
` import type { APIContext } from ' astro ' ;
 export async function POST ( { session } : APIContext ) { // Authenticate the user... doLogin (); // Regenerate the session ID to prevent session fixation attacks session . regenerate () ; return Response . json ({ success: true }); } `
```

#### `session.destroy()`
 Section titled “session.destroy()”
 Type : `() => void`

Destroys the session, deleting the cookie and the object from the backend. Call this when a user logs out or their session is otherwise invalidated.

 -

 Astro.session

-

 context.session

 src/pages/logout.astro ` --- Astro . session ?. destroy () ; return Astro . redirect ( ' /login ' ); --- `

 src/pages/api/logout.ts
```
` import type { APIContext } from ' astro ' ;
 export async function POST ( { session } : APIContext ) { session . destroy () ; return Response . json ({ success: true }); } `
```

#### `session.load()`
 Section titled “session.load()”
 Type : `(id: string) => Promise&#x3C;void>`

Loads a session by ID. In normal use, a session is loaded automatically from the request cookie. Use this method to load a session from a different ID. This is useful if you are handling the session ID yourself, or if you want to keep track of a session without using cookies.

 -

 Astro.session

-

 context.session

 src/pages/cart.astro ` --- // Load the session from a header instead of cookies const sessionId = Astro . request . headers . get ( ' x-session-id ' ); await Astro . session ?. load (sessionId); const cart = await Astro . session ?. get ( ' cart ' ); --- &#x3C; h1 > Your cart &#x3C;/ h1 > &#x3C; ul > { cart ?. map ( ( item ) => ( &#x3C; li > { item . name } &#x3C;/ li > )) } &#x3C;/ ul > `  {cart?.map((item) => ( - {item.name}
 ))} ">

 src/pages/api/load-session.ts
```
` import type { APIRoute } from ' astro ' ;
 export const GET : APIRoute = async ( { session , request } ) => { // Load the session from a header instead of cookies const sessionId = request . headers . get ( ' x-session-id ' ) ; await session . load (sessionId) ; const cart = await session . get ( ' cart ' ) ; return Response . json ( { cart } ) ; } ; `
```
 { // Load the session from a header instead of cookies const sessionId = request.headers.get(&#x27;x-session-id&#x27;); await session.load(sessionId); const cart = await session.get(&#x27;cart&#x27;); return Response.json({ cart });};">

### `csp`
 Section titled “csp”
 Type : `object | undefined`

 Added in:
 `astro@6.0.0`

Astro’s CSP runtime APIs enable support for Content Security Policy (CSP) to help minimize certain types of security threats by controlling which resources a document is allowed to load. This provides additional protection against cross-site scripting (XSS) attacks.

You can customize the `&#x3C;meta>` element per page from the `Astro` global inside `.astro` components, or the `APIContext` type in endpoints and middleware.

When resources are inserted multiple times or from multiple sources (e.g. defined in your `csp` config and added using the following CSP runtime APIs, Astro will merge and deduplicate all resources to create your `&#x3C;meta>` element.

#### `csp.insertDirective()`
 Section titled “csp.insertDirective()”
 Type: `(directive: CspDirective) => void`

 Added in:
 `astro@6.0.0`

Adds a single directive to the current page. You can call this method multiple times to add additional directives.

 src/pages/index.astro ` --- Astro . csp ?. insertDirective ( " default-src 'self' " ); Astro . csp ?. insertDirective ( " img-src 'self' https://images.cdn.example.com " ); --- `
 After the build, the `&#x3C;meta>` element for this individual page will incorporate your additional directives alongside the existing `script-src` and `style-src` directives:

 ` &#x3C; meta http-equiv = " content-security-policy " content = " default-src 'self'; img-src 'self' https://images.cdn.example.com; script-src 'self' 'sha256-somehash'; style-src 'self' 'sha256-somehash'; " > ` ">

#### `csp.insertStyleResource()`
 Section titled “csp.insertStyleResource()”
 Type: `(resource: string) => void`

 Added in:
 `astro@6.0.0`

Inserts a new resource to be used for the `style-src` directive.

 src/pages/index.astro ` --- Astro . csp ?. insertStyleResource ( " https://styles.cdn.example.com " ); --- `
 After the build, the `&#x3C;meta>` element for this individual page will add your source to the default `style-src` directive:

 ` &#x3C; meta http-equiv = " content-security-policy " content = " script-src 'self' 'sha256-somehash'; style-src https://styles.cdn.example.com 'sha256-somehash'; " > ` ">

#### `csp.insertStyleHash()`
 Section titled “csp.insertStyleHash()”
 Type: `(hash: CspHash) => void`

 Added in:
 `astro@6.0.0`

Adds a new hash to the `style-src` directive.

 src/pages/index.astro ` --- Astro . csp ?. insertStyleHash ( " sha512-styleHash " ); --- `
 After the build, the `&#x3C;meta>` element for this individual page will add your hash to the default `style-src` directive:

 ` &#x3C; meta http-equiv = " content-security-policy " content = " script-src 'self' 'sha256-somehash'; style-src 'self' 'sha256-somehash' 'sha512-styleHash'; " > ` ">

#### `csp.insertScriptResource()`
 Section titled “csp.insertScriptResource()”
 Type: `(resource: string) => void`

 Added in:
 `astro@6.0.0`

Inserts a new valid source to be used for the `script-src` directive.

 src/pages/index.astro ` --- Astro . csp ?. insertScriptResource ( " https://scripts.cdn.example.com " ); --- `
 After the build, the `&#x3C;meta>` element for this individual page will add your source to the default `script-src` directive:

 ` &#x3C; meta http-equiv = " content-security-policy " content = " script-src https://scripts.cdn.example.com 'sha256-somehash'; style-src 'self' 'sha256-somehash'; " > ` ">

#### `csp.insertScriptHash()`
 Section titled “csp.insertScriptHash()”
 Type: `(hash: CspHash) => void`

 Added in:
 `astro@6.0.0`

Adds a new hash to the `script-src` directive.

 src/pages/index.astro ` --- Astro . csp ?. insertScriptHash ( " sha512-scriptHash " ); --- `
 After the build, the `&#x3C;meta>` element for this individual page will add your hash to the default `script-src` directive:

```
` &#x3C; meta http-equiv = " content-security-policy " content = " script-src 'self' 'sha256-somehash' 'sha512-styleHash'; style-src 'self' 'sha256-somehash'; " > `
```
 ">

 Reference

 Contribute

 Community

 Sponsor