# Astro - Routing & Navigation


## Astro Pages

# Pages

 Pages are files that live in the `src/pages/` subdirectory of your Astro project. They are responsible for handling routing, data loading, and overall page layout for every page in your website.

## Supported page files
 Section titled “Supported page files”
 Astro supports the following file types in the `src/pages/` directory:

- `.astro`

- `.md`

- `.mdx` (with the MDX Integration installed )

- `.html`

- `.js`/`.ts` (as endpoints )

## File-based routing
 Section titled “File-based routing”
 Astro leverages a routing strategy called file-based routing . Each file in your `src/pages/` directory becomes an endpoint on your site based on its file path.

A single file can also generate multiple pages using dynamic routing . This allows you to create pages even if your content lives outside of the special `/pages/` directory, such as in a content collection or a CMS .

 Read more about Routing in Astro .

### Link between pages
 Section titled “Link between pages”
 Write standard HTML `&#x3C;a>` elements in your Astro pages to link to other pages on your site. Use a URL path relative to your root domain as your link, not a relative file path.

For example, to link to `https://example.com/authors/sonali/` from any other page on `example.com`:

 - src/pages/index.astro ` Read more &#x3C; a href = " /authors/sonali/ " > about Sonali &#x3C;/ a > . ` about Sonali .">

## Astro Pages
 Section titled “Astro Pages”
 Astro pages use the `.astro` file extension and support the same features as Astro components .

 src/pages/index.astro ` --- --- &#x3C; html lang = " en " > &#x3C; head > &#x3C; title > My Homepage &#x3C;/ title > &#x3C;/ head > &#x3C; body > &#x3C; h1 > Welcome to my website! &#x3C;/ h1 > &#x3C;/ body > &#x3C;/ html > `   My Homepage   
# Welcome to my website!
  ">
 A page must produce a full HTML document. If not explicitly included, Astro will add the necessary `&#x3C;!DOCTYPE html>` declaration and `&#x3C;head>` content to any `.astro` component located within `src/pages/` by default. You can opt-out of this behavior on a per-component basis by marking it as a partial page.

To avoid repeating the same HTML elements on every page, you can move common `&#x3C;head>` and `&#x3C;body>` elements into your own layout components . You can use as many or as few layout components as you’d like.

 src/pages/index.astro ` --- import MySiteLayout from " ../layouts/MySiteLayout.astro " ; --- &#x3C; MySiteLayout > &#x3C; p > My page content, wrapped in a layout! &#x3C;/ p > &#x3C;/ MySiteLayout > `  My page content, wrapped in a layout!
 ">

 Read more about layout components in Astro.

## Markdown/MDX Pages
 Section titled “Markdown/MDX Pages”
 Astro also treats any Markdown (`.md`) files inside of `src/pages/` as pages in your final website. If you have the MDX Integration installed , it also treats MDX (`.mdx`) files the same way.

Markdown files can use the special `layout` frontmatter property to specify a layout component that will wrap their Markdown content in a full `&#x3C;html>...&#x3C;/html>` page document.

 src/pages/page.md ` --- layout : ../layouts/MySiteLayout.astro title : My Markdown page --- # Title
 This is my page, written in ** Markdown. ** `

 Read more about Markdown in Astro.

## HTML Pages
 Section titled “HTML Pages”
 Files with the `.html` file extension can be placed in the `src/pages/` directory and used directly as pages on your site. Note that some key Astro features are not supported in HTML Components .

## Custom 404 Error Page
 Section titled “Custom 404 Error Page”
 For a custom 404 error page, you can create a `404.astro` or `404.md` file in `src/pages`.

This will build to a `404.html` page. Most deploy services will find and use it.

## Custom 500 Error Page
 Section titled “Custom 500 Error Page”
 For a custom 500 error page to show for pages that are rendered on demand , create the file `src/pages/500.astro`. This custom page is not available for prerendered pages.

If an error occurs rendering this page, your host’s default 500 error page will be shown to your visitor.

 Added in:
 `astro@4.10.3`

During development, if you have a `500.astro`, the error thrown at runtime is logged in your terminal, as opposed to being shown in the error overlay.

### `error`
 Section titled “error”

 Added in:
 `astro@4.11.0`

`src/pages/500.astro` is a special page that is automatically passed an `error` prop for any error thrown during rendering. This allows you to use the details of an error (e.g. from a page, from middleware, etc.) to display information to your visitor.

The `error` prop’s data type can be anything, which may affect how you type or use the value in your code:

 src/pages/500.astro ` --- interface Props { error : unknown ; }
 const { error } = Astro . props ; --- &#x3C; div > { error instanceof Error ? error . message : " Unknown error " } &#x3C;/ div > ` {error instanceof Error ? error.message : &#x22;Unknown error&#x22;} ">
 To avoid leaking sensitive information when displaying content from the `error` prop, consider evaluating the error first, and returning appropriate content based on the error thrown. For example, you should avoid displaying the error’s stack as it contains information about how your code is structured on the server.

## Page Partials
 Section titled “Page Partials”

 Added in:
 `astro@3.4.0`

Partials are page components located within `src/pages/` that are not intended to render as full pages.

Like components located outside of this folder, these files do not automatically include the `&#x3C;!DOCTYPE html>` declaration, nor any `&#x3C;head>` content such as scoped styles and scripts.

However, because they are located in the special `src/pages/` directory, the generated HTML is available at a URL corresponding to its file path. This allows a rendering library (e.g. htmx , Stimulus , jQuery ) to access it on the client and load sections of HTML dynamically on a page without a browser refresh or page navigation.

Partials, when combined with a rendering library, provide an alternative to Astro islands and `&#x3C;script>` tags for building dynamic content in Astro.

Page files that can export a value for `partial` (e.g. `.astro` and `.mdx`, but not `.md`) can be marked as partials.

 src/pages/partial.astro ` --- export const partial = true ; --- &#x3C; li > I'm a partial! &#x3C;/ li > ` I&#x27;m a partial!
">

### Using with a library
 Section titled “Using with a library”
 Partials are used to dynamically update a section of a page using a library such as htmx .

The following example shows an `hx-post` attribute set to a partial’s URL. The content from the partial page will be used to update the targeted HTML element on this page.

 src/pages/index.astro ` &#x3C; html > &#x3C; head > &#x3C; title > My page &#x3C;/ title > &#x3C; script src = " https://unpkg.com/htmx.org@1.9.6 " integrity = " sha384-FhXw7b6AlE/jyjlZH5iHa/tTe9EpJ1Y55RjcgPbjeWMskSxZt1v9qkxLJWNJaGni " crossorigin = " anonymous " >&#x3C;/ script > &#x3C;/ head > &#x3C; body > &#x3C; section > &#x3C; div id = " parent-div " > Target here &#x3C;/ div >
 &#x3C; button hx-post = " /partials/clicked/ " hx-trigger = " click " hx-target = " #parent-div " hx-swap = " innerHTML " > Click Me! &#x3C;/ button > &#x3C;/ section > &#x3C;/ body > &#x3C;/ html > `   My page      Target here   Click Me!    ">
 The `.astro` partial must exist at the corresponding file path, and include an export defining the page as a partial:

 src/pages/partials/clicked.astro ` --- export const partial = true ; --- &#x3C; div > I was clicked! &#x3C;/ div > ` I was clicked! ">
 See the htmx documentation for more details on using htmx.

 Learn

 Contribute

 Community

 Sponsor

## Routing

# Routing

 Astro uses file-based routing to generate your build URLs based on the file layout of your project `src/pages/` directory.

## Navigating between pages
 Section titled “Navigating between pages”
 Astro uses standard HTML `&#x3C;a>` elements to navigate between routes. There is no framework-specific `&#x3C;Link>` component provided.

 - src/pages/index.astro ` &#x3C; p > Read more &#x3C; a href = " /about/ " > about &#x3C;/ a > Astro! &#x3C;/ p >
 &#x3C;!-- With `base: "/docs"` configured --> &#x3C; p > Learn more in our &#x3C; a href = " /docs/reference/ " > reference &#x3C;/ a > section! &#x3C;/ p > ` Read more about Astro!
Learn more in our reference section!
">

## Static routes
 Section titled “Static routes”
 `.astro` page components as well as Markdown and MDX Files (`.md`, `.mdx`) within the `src/pages/` directory automatically become pages on your website . Each page’s route corresponds to its path and filename within the `src/pages/` directory.

 ` # Example: Static routes src/pages/index.astro -> mysite.com/ src/pages/about.astro -> mysite.com/about src/pages/about/index.astro -> mysite.com/about src/pages/about/me.astro -> mysite.com/about/me src/pages/posts/1.md -> mysite.com/posts/1 ` mysite.com/src/pages/about.astro -> mysite.com/aboutsrc/pages/about/index.astro -> mysite.com/aboutsrc/pages/about/me.astro -> mysite.com/about/mesrc/pages/posts/1.md -> mysite.com/posts/1">

## Dynamic routes
 Section titled “Dynamic routes”
 An Astro page file can specify dynamic route parameters in its filename to generate multiple, matching pages. For example, `src/pages/authors/[author].astro` generates a bio page for every author on your blog. `author` becomes a parameter that you can access from inside the page.

In Astro’s default static output mode, these pages are generated at build time, and so you must predetermine the list of `author`s that get a corresponding file. In SSR mode, a page will be generated on request for any route that matches.

### Static (SSG) Mode
 Section titled “Static (SSG) Mode”
 Because all routes must be determined at build time, a dynamic route must export a `getStaticPaths()` that returns an array of objects with a `params` property. Each of these objects will generate a corresponding route.

`[dog].astro` defines the dynamic `dog` parameter in its filename, so the objects returned by `getStaticPaths()` must include `dog` in their `params`. The page can then access this parameter using `Astro.params`.

 src/pages/dogs/[dog].astro ` --- export function getStaticPaths () { return [ { params: { dog: " clifford " }} , { params: { dog: " rover " }} , { params: { dog: " spot " }} , ]; }
 const { dog } = Astro . params ; --- &#x3C; div > Good dog, { dog } ! &#x3C;/ div > ` Good dog, {dog}! ">
 This will generate three pages: `/dogs/clifford`, `/dogs/rover`, and `/dogs/spot`, each displaying the corresponding dog name.

The filename can include multiple parameters, which must all be included in the `params` objects in `getStaticPaths()`:

 src/pages/[lang]-[version]/info.astro ` --- export function getStaticPaths () { return [ { params: { lang: " en " , version: " v1 " }} , { params: { lang: " fr " , version: " v2 " }} , ]; }
 const { lang , version } = Astro . params ; --- `
 This will generate `/en-v1/info` and `/fr-v2/info`.

Parameters can be included in separate parts of the path. For example, the file `src/pages/[lang]/[version]/info.astro` with the same `getStaticPaths()` above will generate the routes `/en/v1/info` and `/fr/v2/info`.

#### Decoding `params`
 Section titled “Decoding params”
 `params` returned by a `getStaticPaths()` function are not decoded. Use `decodeURI()` when you need to decode parameter values.

 src/pages/[slug].astro ` --- export function getStaticPaths () { return [ { params: { slug: decodeURI ( " %5Bpage%5D " ) }} , // decodes to "[page]" ] } --- `

 Learn more about `getStaticPaths()` .

 Related recipe:

 Add i18n features

#### Rest parameters
 Section titled “Rest parameters”
 If you need more flexibility in your URL routing, you can use a rest parameter (`[...path]`) in your `.astro` filename to match file paths of any depth:

 src/pages/sequences/[...path].astro ` --- export function getStaticPaths () { return [ { params: { path: " one/two/three " }} , { params: { path: " four " }} , { params: { path: undefined }} ] }
 const { path } = Astro . params ; --- `
 This will generate `/sequences/one/two/three`, `/sequences/four`, and `/sequences`. (Setting the rest parameter to `undefined` allows it to match the top level page.)

Rest parameters can be used with other named parameters . For example, GitHub’s file viewer can be represented with the following dynamic route:

 ` /[org]/[repo]/tree/[branch]/[...file] `
 In this example, a request for `/withastro/astro/tree/main/docs/public/favicon.svg` would be split into the following named parameters:

 ` { org: " withastro " , repo: " astro " , branch: " main " , file: " docs/public/favicon.svg " } `

#### Example: Dynamic pages at multiple levels
 Section titled “Example: Dynamic pages at multiple levels”
 In the following example, a rest parameter (`[...slug]`) and the `props` feature of `getStaticPaths()` generate pages for slugs of different depths.

 src/pages/[...slug].astro ` --- export function getStaticPaths () { const pages = [ { slug: undefined , title: " Astro Store " , text: " Welcome to the Astro store! " , } , { slug: " products " , title: " Astro products " , text: " We have lots of products for you " , } , { slug: " products/astro-handbook " , title: " The ultimate Astro handbook " , text: " If you want to learn Astro, you must read this book. " , } , ];
 return pages . map ( ( { slug , title , text } ) => { return { params: { slug } , props: { title , text } , }; }); }
 const { title , text } = Astro . props ; --- &#x3C; html > &#x3C; head > &#x3C; title > { title } &#x3C;/ title > &#x3C;/ head > &#x3C; body > &#x3C; h1 > { title } &#x3C;/ h1 > &#x3C; p > { text } &#x3C;/ p > &#x3C;/ body > &#x3C;/ html > ` { return { params: { slug }, props: { title, text }, }; });}const { title, text } = Astro.props;---   {title}   
# {title}
 {text}
  ">

### On-demand dynamic routes
 Section titled “On-demand dynamic routes”
 For on-demand rendering with an adapter, dynamic routes are defined the same way: include `[param]` or `[...path]` brackets in your file names to match arbitrary strings or paths. But because the routes are no longer built ahead of time, the page will be served to any matching route. Since these are not “static” routes, `getStaticPaths` should not be used.

For on-demand rendered routes, only one rest parameter using the spread notation may be used in the file name (e.g. `src/pages/[locale]/[...slug].astro` or `src/pages/[...locale]/[slug].astro`, but not `src/pages/[...locale]/[...slug].astro`).

 src/pages/resources/[resource]/[id].astro ` --- export const prerender = false ; // Not needed in 'server' mode const { resource , id } = Astro . params ; --- &#x3C; h1 > { resource } : { id } &#x3C;/ h1 > `
 This page will be served for any value of `resource` and `id`: `resources/users/1`, `resources/colors/blue`, etc.

#### Modifying the `[...slug]` example for SSR
 Section titled “Modifying the [...slug] example for SSR”
 Because SSR pages can’t use `getStaticPaths()`, they can’t receive props. The previous example can be adapted for SSR mode by looking up the value of the `slug` param in an object. If the route is at the root (”/”), the `slug` param will be `undefined`. If the value doesn’t exist in the object, we redirect to a 404 page.

 src/pages/[...slug].astro ` --- const pages = [ { slug: undefined , title: ' Astro Store ' , text: ' Welcome to the Astro store! ' , }, { slug: ' products ' , title: ' Astro products ' , text: ' We have lots of products for you ' , }, { slug: ' products/astro-handbook ' , title: ' The ultimate Astro handbook ' , text: ' If you want to learn Astro, you must read this book. ' , } ];
 const { slug } = Astro . params ; const page = pages . find ( ( page ) => page . slug === slug); if ( ! page) return Astro . redirect ( " /404 " ); const { title , text } = page; --- &#x3C; html > &#x3C; head > &#x3C; title > { title } &#x3C;/ title > &#x3C;/ head > &#x3C; body > &#x3C; h1 > { title } &#x3C;/ h1 > &#x3C; p > { text } &#x3C;/ p > &#x3C;/ body > &#x3C;/ html > ` page.slug === slug);if (!page) return Astro.redirect(&#x22;/404&#x22;);const { title, text } = page;---   {title}   
# {title}
 {text}
  ">

## Redirects
 Section titled “Redirects”
 Sometimes you will need to redirect your readers to a new page, either permanently because your site structure has changed or in response to an action such as logging in to an authenticated route.

You can define rules to redirect users to permanently-moved pages in your Astro config. Or, redirect users dynamically as they use your site.

### Configured Redirects
 Section titled “Configured Redirects”

 Added in:
 `astro@2.9.0`

You can specify a mapping of permanent redirects in your Astro config with the `redirects` value.

For internal redirects, this is a mapping of an old route path to the new route. As of Astro v5.2.0, it is also possible to redirect to external URLs that start with `http` or `https` and can be parsed :

 astro.config.mjs ` import { defineConfig } from " astro/config " ;
 export default defineConfig ({ redirects: { " /old-page " : " /new-page " , " /blog " : " https://example.com/blog " } }); `
 These redirects follow the same priority rules as file-based routes and will always take lower precedence than an existing page file of the same name in your project. For example, `/old-page` will not redirect to `/new-page` if your project contains the file `src/pages/old-page.astro`.

Dynamic routes are allowed as long as both the new and old routes contain the same parameters, for example:

 ` { " /blog/[...slug] " : " /articles/[...slug] " } `
 Using SSR or a static adapter, you can also provide an object as the value, allowing you to specify the `status` code in addition to the new `destination`:

 astro.config.mjs ` import { defineConfig } from " astro/config " ;
 export default defineConfig ({ redirects: { " /old-page " : { status: 302 , destination: " /new-page " }, " /news " : { status: 302 , destination: " https://example.com/news " } } }); `
 When running `astro build`, Astro will output HTML files with the meta refresh tag by default. Supported adapters will instead write out the host’s configuration file with the redirects.

The status code is `301` by default. If building to HTML files the status code is not used by the server.

### Dynamic redirects
 Section titled “Dynamic redirects”
 On the `Astro` global, the `Astro.redirect` method allows you to redirect to another page dynamically. You might do this after checking if the user is logged in by getting their session from a cookie.

 src/pages/account.astro ` --- import { isLoggedIn } from " ../utils " ;
 const cookie = Astro . request . headers . get ( " cookie " );
 // If the user is not logged in, redirect them to the login page if ( ! isLoggedIn (cookie)) { return Astro . redirect ( " /login " ); } --- `
 Because Astro uses HTML streaming in on-demand rendering, redirects must be done at the page level, not inside child components.

## Rewrites
 Section titled “Rewrites”

 Added in:
 `astro@4.13.0`

A rewrite allows you to serve a different route without redirecting the browser to a different page. The browser will show the original address in the URL bar, but will instead display the content of the URL provided to `Astro.rewrite()` .

Rewrites can be useful for showing the same content at multiple paths (e.g. `/products/shoes/men/` and `/products/men/shoes/`) without needing to maintain two different source files.

Rewrites are also useful for SEO purposes and user experience. They allow you to display content that otherwise would require redirecting your visitor to a different page or would return a 404 status. One common use of rewrites is to show the same localized content for different variants of a language.

The following example uses a rewrite to render the `/es/` version of a page when the `/es-CU/` (Cuban Spanish) URL path is visited. When a visitor navigates to the URL `/es-cu/articles/introduction`, Astro will render the content generated by the file `src/pages/es/articles/introduction.astro`.

 src/pages/es-cu/articles/introduction.astro ` --- return Astro . rewrite ( " /es/articles/introduction " ); --- `
 Use `context.rewrite()` in your endpoint files to reroute to a different page:

 src/pages/api.js ` export function GET ( context ) { if ( ! context . locals . allowed ) { return context . rewrite ( " / " ); } } `
 If the URL passed to `Astro.rewrite()` emits a runtime error, Astro will show the overlay error in development and return a 500 status code in production. If the URL does not exist in your project, a 404 status code will be returned.

You can intentionally create a rewrite to render your `/404` page, for example to indicate that a product in your e-commerce shop is no longer available:

 src/pages/[item].astro ` --- const { item } = Astro . params ;
 if ( ! itemExists (item)) { return Astro . rewrite ( " /404 " ); } --- `
 You can also conditionally rewrite based on an HTTP response status, for example to display a certain page on your site when visiting a URL that doesn’t exist:

 src/middleware.mjs ` export const onRequest = async ( context , next ) => { const response = await next () ; if ( response . status === 404 ) { return context . rewrite ( " / " ) ; } return response ; } ` { const response = await next(); if (response.status === 404) { return context.rewrite(&#x22;/&#x22;); } return response;}">
 Before displaying the content from the specified rewrite path, the function `Astro.rewrite()` will trigger a new, complete rendering phase. This re-executes any middleware for the new route/request.

 See the `Astro.rewrite()` API reference for more information.

## Route Priority Order
 Section titled “Route Priority Order”
 It’s possible for multiple defined routes to attempt to build the same URL path. For example, all of these routes could build `/posts/create`:

 Directory src/pages/
 […slug].astro
- Directory posts/
 create.astro
- [page].astro
- [pid].ts
- […slug].astro

 Astro needs to know which route should be used to build the page. To do so, it sorts them according to the following rules in order:

- Astro reserved routes

- Routes with more path segments will take precedence over less specific routes. In the example above, all routes under `/posts/` take precedence over `/[...slug].astro` at the root.

- Static routes without path parameters will take precedence over dynamic routes. E.g. `/posts/create.astro` takes precedence over all the other routes in the example.

- Dynamic routes using named parameters take precedence over rest parameters. E.g. `/posts/[page].astro` takes precedence over `/posts/[...slug].astro`.

- Pre-rendered dynamic routes take precedence over server dynamic routes.

- Endpoints take precedence over pages.

- File-based routes take precedence over redirects.

- If none of the rules above decide the order, routes are sorted alphabetically based on the default locale of your Node installation.

Given the example above, here are a few examples of how the rules will match a requested URL to the route used to build the HTML:

- `pages/posts/create.astro` - Will build only `/posts/create`

- `pages/posts/[pid].ts` - Will build `/posts/abc`, `/posts/xyz`, etc. But not `/posts/create`

- `pages/posts/[page].astro` - Will build `/posts/1`, `/posts/2`, etc. But not `/posts/create`, `/posts/abc` nor `/posts/xyz`

- `pages/posts/[...slug].astro` - Will build `/posts/1/2`, `/posts/a/b/c`, etc. But not `/posts/create`, `/posts/1`, `/posts/abc`, etc.

- `pages/[...slug].astro` - Will build `/abc`, `/xyz`, `/abc/xyz`, etc. But not `/posts/create`, `/posts/1`, `/posts/abc`, etc.

### Reserved routes
 Section titled “Reserved routes”
 Internal routes take priority over any user-defined or integration-defined routes as they are required for Astro features to work. The following are Astro’s reserved routes:

- `_astro/`: Serves all of the static assets to the client, including CSS documents, bundled client scripts, optimized images, and any Vite assets.

- `_server_islands/`: Serves the dynamic components deferred into a server island .

- `_actions/`: Serves any defined actions .

## Pagination
 Section titled “Pagination”
 Astro supports built-in pagination for large collections of data that need to be split into multiple pages. Astro will generate common pagination properties, including previous/next page URLs, total number of pages, and more.

Paginated route names should use the same `[bracket]` syntax as a standard dynamic route. For instance, the file name `/astronauts/[page].astro` will generate routes for `/astronauts/1`, `/astronauts/2`, etc, where `[page]` is the generated page number.

You can use the `paginate()` function to generate these pages for an array of values like so:

 src/pages/astronauts/[page].astro ` --- export function getStaticPaths ( { paginate } ) { const astronautPages = [ { astronaut: " Neil Armstrong " } , { astronaut: " Buzz Aldrin " } , { astronaut: " Sally Ride " } , { astronaut: " John Glenn " } , ];
 // Generate pages from our array of astronauts, with 2 to a page return paginate (astronautPages , { pageSize: 2 }); } // All paginated data is passed on the "page" prop const { page } = Astro . props ; --- &#x3C;!-- Display the current page number. `Astro.params.page` can also be used! --> &#x3C; h1 > Page { page . currentPage } &#x3C;/ h1 > &#x3C; ul > &#x3C;!-- List the array of astronaut info --> { page . data . map ( ( { astronaut } ) => &#x3C; li > { astronaut } &#x3C;/ li > ) } &#x3C;/ ul > `   {page.data.map(({ astronaut }) => - {astronaut}
)} ">
 This generates the following pages, with 2 items to a page:

- `/astronauts/1` - Page 1: Displays “Neil Armstrong” and “Buzz Aldrin”

- `/astronauts/2` - Page 2: Displays “Sally Ride” and “John Glenn”

### The `page` prop
 Section titled “The page prop”
 When you use the `paginate()` function, each page will be passed its data via a `page` prop. The `page` prop has many useful properties that you can use to build pages and links between them:

 ` interface Page&#x3C; T = any > { /** array containing the page’s slice of data that you passed to the paginate() function */ data : T []; /** metadata */ /** the count of the first item on the page, starting from 0 */ start : number ; /** the count of the last item on the page, starting from 0 */ end : number ; /** total number of results */ total : number ; /** the current page number, starting from 1 */ currentPage : number ; /** number of items per page (default: 10) */ size : number ; /** number of last page */ lastPage : number ; url : { /** url of the current page */ current : string ; /** url of the previous page (if there is one) */ prev : string | undefined ; /** url of the next page (if there is one) */ next : string | undefined ; /** url of the first page (if the current page is not the first page) */ first : string | undefined ; /** url of the last page (if the current page in not the last page) */ last : string | undefined ; }; } ` { /** array containing the page’s slice of data that you passed to the paginate() function */ data: T[]; /** metadata */ /** the count of the first item on the page, starting from 0 */ start: number; /** the count of the last item on the page, starting from 0 */ end: number; /** total number of results */ total: number; /** the current page number, starting from 1 */ currentPage: number; /** number of items per page (default: 10) */ size: number; /** number of last page */ lastPage: number; url: { /** url of the current page */ current: string; /** url of the previous page (if there is one) */ prev: string | undefined; /** url of the next page (if there is one) */ next: string | undefined; /** url of the first page (if the current page is not the first page) */ first: string | undefined; /** url of the last page (if the current page in not the last page) */ last: string | undefined; };}">
 The following example displays current information for the page along with links to navigate between pages:

 src/pages/astronauts/[page].astro ` --- // Paginate same list of `{ astronaut }` objects as the previous example export function getStaticPaths ( { paginate } ) { /* ... */ } const { page } = Astro . props ; --- &#x3C; h1 > Page { page . currentPage } &#x3C;/ h1 > &#x3C; ul > { page . data . map ( ( { astronaut } ) => &#x3C; li > { astronaut } &#x3C;/ li > ) } &#x3C;/ ul > { page . url . first ? &#x3C; a href = { page . url . first } > First &#x3C;/ a > : null } { page . url . prev ? &#x3C; a href = { page . url . prev } > Previous &#x3C;/ a > : null } { page . url . next ? &#x3C; a href = { page . url . next } > Next &#x3C;/ a > : null } { page . url . last ? &#x3C; a href = { page . url . last } > Last &#x3C;/ a > : null } `  {page.data.map(({ astronaut }) => - {astronaut}
)} {page.url.first ? First : null}{page.url.prev ? Previous : null}{page.url.next ? Next : null}{page.url.last ? Last : null}">

 Learn more about the pagination `page` prop .

### Nested Pagination
 Section titled “Nested Pagination”
 A more advanced use-case for pagination is nested pagination. This is when pagination is combined with other dynamic route params. You can use nested pagination to group your paginated collection by some property or tag.

For example, if you want to group your paginated Markdown posts by some tag, you would use nested pagination by creating a `/src/pages/[tag]/[page].astro` page that would match the following URLS:

- `/red/1` (tag=red)

- `/red/2` (tag=red)

- `/blue/1` (tag=blue)

- `/green/1` (tag=green)

Nested pagination works by returning an array of `paginate()` results from `getStaticPaths()`, one for each grouping.

In the following example, we will implement nested pagination to build the URLs listed above:

 src/pages/[tag]/[page].astro ` --- export function getStaticPaths ( { paginate } ) { const allTags = [ " red " , " blue " , " green " ]; const allPosts = Object . values ( import. meta . glob ( " ../pages/post/*.md " , { eager: true } )); // For every tag, return a `paginate()` result. // Make sure that you pass `{ params: { tag }}` to `paginate()` // so that Astro knows which tag grouping the result is for. return allTags . flatMap ( ( tag ) => { const filteredPosts = allPosts . filter ( ( post ) => post . frontmatter . tag === tag ); return paginate (filteredPosts , { params: { tag } , pageSize: 10 }); }); }
 const { page } = Astro . props ; const params = Astro . params ; ` { const filteredPosts = allPosts.filter((post) => post.frontmatter.tag === tag); return paginate(filteredPosts, { params: { tag }, pageSize: 10 }); });}const { page } = Astro.props;const params = Astro.params;">

## Excluding pages
 Section titled “Excluding pages”
 You can exclude pages or directories within `src/pages` from being built by prefixing their names with an underscore (`_`). Files with the `_` prefix won’t be recognized by the router and won’t be placed into the `dist/` directory.

You can use this to temporarily disable pages, and also to put tests, utilities, and components in the same folder as their related pages.

In this example, only `src/pages/index.astro` and `src/pages/projects/project1.md` will be built as page routes and HTML files.

 - Directory src/pages/
 Directory _hidden-directory/
 page1.md
- page2.md
 - _hidden-page.astro
- index.astro
- Directory projects/
 _SomeComponent.astro
- _utils.js
- project1.md

 Learn

 Contribute

 Community

 Sponsor

## Endpoints

# Endpoints

 Astro lets you create custom endpoints to serve any kind of data. You can use this to generate images, expose an RSS document, or use them as API Routes to build a full API for your site.

In statically-generated sites, your custom endpoints are called at build time to produce static files. If you opt in to SSR mode, custom endpoints turn into live server endpoints that are called on request. Static and SSR endpoints are defined similarly, but SSR endpoints support additional features.

## Static File Endpoints
 Section titled “Static File Endpoints”
 To create a custom endpoint, add a `.js` or `.ts` file to the `/pages` directory. The `.js` or `.ts` extension will be removed during the build process, so the name of the file should include the extension of the data you want to create. For example, `src/pages/data.json.ts` will build a `/data.json` endpoint.

Endpoints export a `GET` function (optionally `async`) that receives a context object with properties similar to the `Astro` global. Here, it returns a `Response` object with a `name` and `url`, and Astro will call this at build time and use the contents of the body to generate the file.

 - src/pages/builtwith.json.ts ` // Outputs: /builtwith.json export function GET ( { params , request } ) { return new Response ( JSON . stringify ({ name: " Astro " , url: " https://astro.build/ " , }) , ); } `
 Since Astro v3.0, the returned `Response` object doesn’t have to include the `encoding` property anymore. For example, to produce a binary `.png` image:

 src/pages/astro-logo.png.ts ` export async function GET ( { params , request } ) { const response = await fetch ( " https://docs.astro.build/assets/full-logo-light.png " , );
 return new Response ( await response . arrayBuffer ()); } `
 You can also get type safety in your endpoint functions using the `APIRoute` type with the `satisfies` operator:

 ` import type { APIRoute } from " astro " ;
 export const GET = ( async ( { params , request } ) => { /* ... */ } ) satisfies APIRoute ; ` { /* ... */ }) satisfies APIRoute;">
 Note that endpoints whose URLs include a file extension (e.g. `src/pages/sitemap.xml.ts`) can only be accessed without a trailing slash (e.g. `/sitemap.xml`), regardless of your `build.trailingSlash` configuration.

### `params` and Dynamic routing
 Section titled “params and Dynamic routing”
 Endpoints support the same dynamic routing features that pages do. Name your file with a bracketed parameter name and export a `getStaticPaths()` function . Then, you can access the parameter using the `params` property passed to the endpoint function:

 src/pages/api/[id].json.ts ` import type { APIRoute } from " astro " ;
 const usernames = [ " Sarah " , " Chris " , " Yan " , " Elian " ];
 export const GET = ( ( { params , request } ) => { const id = params . id ;
 return new Response ( JSON . stringify ( { name: usernames[id] , } ) , ) ; } ) satisfies APIRoute ;
 export function getStaticPaths () { return [ { params: { id: " 0 " } } , { params: { id: " 1 " } } , { params: { id: " 2 " } } , { params: { id: " 3 " } } , ]; } ` { const id = params.id; return new Response( JSON.stringify({ name: usernames[id], }), );}) satisfies APIRoute;export function getStaticPaths() { return [ { params: { id: &#x22;0&#x22; } }, { params: { id: &#x22;1&#x22; } }, { params: { id: &#x22;2&#x22; } }, { params: { id: &#x22;3&#x22; } }, ];}">
 This will generate four JSON endpoints at build time: `/api/0.json`, `/api/1.json`, `/api/2.json` and `/api/3.json`. Dynamic routing with endpoints works the same as it does with pages. In static mode, you can pass props to the endpoint using `getStaticPaths()` . However, with on-demand rendering, since the endpoint is a function and not a component, passing props is not supported.

### `request`
 Section titled “request”
 All endpoints receive a `request` property, but in static mode, you only have access to `request.url`. This returns the full URL of the current endpoint and works the same as Astro.request.url does for pages.

 src/pages/request-path.json.ts ` import type { APIRoute } from " astro " ;
 export const GET = ( ( { params , request } ) => { return new Response ( JSON . stringify ( { path: new URL (request . url ) . pathname , } ) , ) ; } ) satisfies APIRoute ; ` { return new Response( JSON.stringify({ path: new URL(request.url).pathname, }), );}) satisfies APIRoute;">

## Server Endpoints (API Routes)
 Section titled “Server Endpoints (API Routes)”
 Everything described in the static file endpoints section can also be used in SSR mode: files can export a `GET` function which receives a context object with properties similar to the `Astro` global.

But, unlike in `static` mode, when you enable on-demand rendering for a route, the endpoint will be built when it is requested. This unlocks new features that are unavailable at build time, and allows you to build API routes that listen for requests and securely execute code on the server at runtime.

Your routes will be rendered on demand by default in `server` mode. In `static` mode, you must opt out of prerendering for each custom endpoint with `export const prerender = false`.

 Related recipe:

 Call endpoints from the server

Server endpoints can access `params` without exporting `getStaticPaths`, and they can return a `Response` object, allowing you to set status codes and headers:

 src/pages/[id].json.js ` import { getProduct } from " ../db " ;
 export async function GET ( { params } ) { const id = params . id ; const product = await getProduct ( id );
 if ( ! product ) { return new Response ( null , { status: 404 , statusText: " Not found " , }); }
 return new Response ( JSON . stringify ( product ) , { status: 200 , headers: { " Content-Type " : " application/json " , } , }); } `
 This will respond to any request that matches the dynamic route. For example, if we navigate to `/helmet.json`, `params.id` will be set to `helmet`. If `helmet` exists in the mock product database, the endpoint will use a `Response` object to respond with JSON and return a successful HTTP status code . If not, it will use a `Response` object to respond with a `404`.

In SSR mode, certain providers require the `Content-Type` header to return an image. In this case, use a `Response` object to specify a `headers` property. For example, to produce a binary `.png` image:

 src/pages/astro-logo.png.ts ` export async function GET ( { params , request } ) { const response = await fetch ( " https://docs.astro.build/assets/full-logo-light.png " , ); const buffer = Buffer . from ( await response . arrayBuffer ());
 return new Response (buffer , { headers: { " Content-Type " : " image/png " } , }); } `

### HTTP methods
 Section titled “HTTP methods”
 In addition to the `GET` function, you can export a function with the name of any HTTP method . When a request comes in, Astro will check the method and call the corresponding function.

You can also export an `ALL` function to match any method that doesn’t have a corresponding exported function. If there is a request with no matching method, it will redirect to your site’s 404 page .

 src/pages/methods.json.ts ` export const GET = ( ( { params , request } ) => { return new Response ( JSON . stringify ( { message: " This was a GET! " , } ) , ) ; } ) satisfies APIRoute ;
 export const POST = ( ( { request } ) => { return new Response ( JSON . stringify ( { message: " This was a POST! " , } ) , ) ; } ) satisfies APIRoute ;
 export const DELETE = ( ( { request } ) => { return new Response ( JSON . stringify ( { message: " This was a DELETE! " , } ) , ) ; } ) satisfies APIRoute ;
 export const ALL = ( ( { request } ) => { return new Response ( JSON . stringify ( { message: ` This was a ${ request . method } ! ` , } ) , ) ; } ) satisfies APIRoute ; ` { return new Response( JSON.stringify({ message: &#x22;This was a GET!&#x22;, }), );}) satisfies APIRoute;export const POST = (({ request }) => { return new Response( JSON.stringify({ message: &#x22;This was a POST!&#x22;, }), );}) satisfies APIRoute;export const DELETE = (({ request }) => { return new Response( JSON.stringify({ message: &#x22;This was a DELETE!&#x22;, }), );}) satisfies APIRoute;export const ALL = (({ request }) => { return new Response( JSON.stringify({ message: &#x60;This was a ${request.method}!&#x60;, }), );}) satisfies APIRoute;">
 If you define a `GET` function but no `HEAD` function, Astro will automatically handle `HEAD` requests by calling the `GET` function and stripping the body from the response.

 Related recipes

 Verify a Captcha

-

 Build forms with API routes

### `request`
 Section titled “request”
 In SSR mode, the `request` property returns a fully usable `Request` object that refers to the current request. This allows you to accept data and check headers:

 src/pages/test-post.json.ts ` export const POST = ( async ( { request } ) => { if (request . headers . get ( " Content-Type " ) === " application/json " ) { const body = await request . json () ; const name = body . name ;
 return new Response ( JSON . stringify ( { message: " Your name was: " + name , } ) , { status: 200 , }, ) ; }
 return new Response ( null , { status: 400 } ) ; } ) satisfies APIRoute ; ` { if (request.headers.get(&#x22;Content-Type&#x22;) === &#x22;application/json&#x22;) { const body = await request.json(); const name = body.name; return new Response( JSON.stringify({ message: &#x22;Your name was: &#x22; + name, }), { status: 200, }, ); } return new Response(null, { status: 400 });}) satisfies APIRoute;">

### Redirects
 Section titled “Redirects”
 The endpoint context exports a `redirect()` utility similar to `Astro.redirect`:

 src/pages/links/[id].js
```
` import { getLinkUrl } from " ../db " ;
 export async function GET ( { params , redirect } ) { const { id } = params ; const link = await getLinkUrl ( id );
 if ( ! link ) { return new Response ( null , { status: 404 , statusText: " Not found " , }); }
 return redirect ( link , 307 ); } `
```

 Learn

 Contribute

 Community

 Sponsor

## Middleware

# Middleware

 Middleware allows you to intercept requests and responses and inject behaviors dynamically every time a page or endpoint is about to be rendered. This rendering occurs at build time for all prerendered pages, but occurs when the route is requested for pages rendered on demand, making additional SSR features like cookies and headers available.

Middleware also allows you to set and share request-specific information across endpoints and pages by mutating a `locals` object that is available in all Astro components and API endpoints. This object is available even when this middleware runs at build time.

## Basic Usage
 Section titled “Basic Usage”

-
 Create `src/middleware.js|ts` (Alternatively, you can create `src/middleware/index.js|ts`.)

-
Inside this file, export an `onRequest()` function that can be passed a `context` object and `next()` function. This must not be a default export.

 src/middleware.js ` export function onRequest ( context , next ) { // intercept data from a request // optionally, modify the properties in `locals` context . locals . title = " New title " ;
 // return a Response or the result of calling `next()` return next (); }; `

-
 Inside any `.astro` file, access response data using `Astro.locals`.

 src/components/Component.astro ` --- const data = Astro . locals ; --- &#x3C; h1 > { data . title } &#x3C;/ h1 > &#x3C; p > This { data . property } is from middleware. &#x3C;/ p > ` This {data.property} is from middleware.
">

### The `context` object
 Section titled “The context object”
 The `context` object includes information to be made available to other middleware, API routes and `.astro` routes during the rendering process.

This is an optional argument passed to `onRequest()` that may contain the `locals` object as well as any additional properties to be shared during rendering. For example, the `context` object may include cookies used in authentication.

### Storing data in `context.locals`
 Section titled “Storing data in context.locals”
 `context.locals` is an object that can be manipulated inside the middleware.

This `locals` object is forwarded across the request handling process and is available as a property to `APIContext` and `AstroGlobal` . This allows data to be shared between middlewares, API routes, and `.astro` pages. This is useful for storing request-specific data, such as user data, across the rendering step.

You can store any type of data inside `locals`: strings, numbers, and even complex data types such as functions and maps.

 src/middleware.js ` export function onRequest ( context , next ) { // intercept data from a request // optionally, modify the properties in `locals` context . locals . user . name = " John Wick " ; context . locals . welcomeTitle = () => { return " Welcome back " + locals . user . name ; };
 // return a Response or the result of calling `next()` return next (); }; ` { return &#x22;Welcome back &#x22; + locals.user.name; }; // return a Response or the result of calling &#x60;next()&#x60; return next();};">
 Then you can use this information inside any `.astro` file with `Astro.locals`.

 src/pages/orders.astro ` --- const title = Astro . locals . welcomeTitle (); const orders = Array . from (Astro . locals . orders . entries ()); const data = Astro . locals ; --- &#x3C; h1 > { title } &#x3C;/ h1 > &#x3C; p > This { data . property } is from middleware. &#x3C;/ p > &#x3C; ul > { orders . map ( order => { return &#x3C; li > { /* do something with each order */ } &#x3C;/ li > ; }) } &#x3C;/ ul > ` This {data.property} is from middleware.
  {orders.map(order => { return - {/* do something with each order */}
; })} ">
`locals` is an object that lives and dies within a single Astro route; when your route page is rendered, `locals` won’t exist anymore and a new one will be created. Information that needs to persist across multiple page requests must be stored elsewhere.

## Example: redacting sensitive information
 Section titled “Example: redacting sensitive information”
 The example below uses middleware to replace “PRIVATE INFO” with the word “REDACTED” to allow you to render modified HTML on your page:

 src/middleware.js ` export const onRequest = async ( context , next ) => { const response = await next () ; const html = await response . text () ; const redactedHtml = html . replaceAll ( " PRIVATE INFO " , " REDACTED " ) ;
 return new Response ( redactedHtml , { status: 200 , headers: response . headers } ) ; } ; ` { const response = await next(); const html = await response.text(); const redactedHtml = html.replaceAll(&#x22;PRIVATE INFO&#x22;, &#x22;REDACTED&#x22;); return new Response(redactedHtml, { status: 200, headers: response.headers });};">

## Middleware types
 Section titled “Middleware types”
 You can import and use the utility function `defineMiddleware()` to take advantage of type safety:

 src/middleware.ts ` import { defineMiddleware } from " astro:middleware " ;
 // `context` and `next` are automatically typed export const onRequest = defineMiddleware ( ( context , next ) => {
 } ); ` {});">
 Instead, if you’re using JsDoc to take advantage of type safety, you can use `MiddlewareHandler`:

 src/middleware.js ` /** * @type {import("astro").MiddlewareHandler} */ // `context` and `next` are automatically typed export const onRequest = ( context , next ) => {
 } ; ` {};">
 To type the information inside `Astro.locals`, which gives you autocompletion inside `.astro` files and middleware code, extend the global types by declaring a global namespace in the `env.d.ts` file:

 src/env.d.ts ` type User = { id : number ; name : string ; };
 declare namespace App { interface Locals { user : User ; welcomeTitle : () => string ; orders : Map &#x3C; string , object >; session : import ( " ./lib/server/session " ). Session | null ; } } ` string; orders: Map ; session: import(&#x22;./lib/server/session&#x22;).Session | null; }}">
 Then, inside the middleware file, you can take advantage of autocompletion and type safety.

## Chaining middleware
 Section titled “Chaining middleware”
 Multiple middlewares can be joined in a specified order using `sequence()` :

 src/middleware.js ` import { sequence } from " astro:middleware " ;
 async function validation ( _ , next ) { console . log ( " validation request " ); const response = await next (); console . log ( " validation response " ); return response ; }
 async function auth ( _ , next ) { console . log ( " auth request " ); const response = await next (); console . log ( " auth response " ); return response ; }
 async function greeting ( _ , next ) { console . log ( " greeting request " ); const response = await next (); console . log ( " greeting response " ); return response ; }
 export const onRequest = sequence ( validation , auth , greeting ); `
 This will result in the following console order:

 Terminal window ` validation request auth request greeting request greeting response auth response validation response `

## Rewriting
 Section titled “Rewriting”

 Added in:
 `astro@4.13.0`

The `APIContext` exposes a method called `rewrite()` which works the same way as Astro.rewrite .

Use `context.rewrite()` inside middleware to display a different page’s content without redirecting your visitor to a new page. This will trigger a new rendering phase, causing any middleware to be re-executed.

 src/middleware.js ` import { isLoggedIn } from " ~/auth.js " export function onRequest ( context , next ) { if ( ! isLoggedIn ( context )) { // If the user is not logged in, update the Request to render the `/login` route and // add header to indicate where the user should be sent after a successful login. // Re-execute middleware. return context . rewrite ( new Request ( " /login " , { headers: { " x-redirect-to " : context . url . pathname } })); }
 return next (); }; `
 You can also pass the `next()` function an optional URL path parameter to rewrite the current `Request` without retriggering a new rendering phase. The location of the rewrite path can be provided as a string, URL, or `Request`:

 src/middleware.js ` import { isLoggedIn } from " ~/auth.js " export function onRequest ( context , next ) { if ( ! isLoggedIn ( context )) { // If the user is not logged in, update the Request to render the `/login` route and // add header to indicate where the user should be sent after a successful login. // Return a new `context` to any following middlewares. return next ( new Request ( " /login " , { headers: { " x-redirect-to " : context . url . pathname } })); }
 return next (); }; `
 The `next()` function accepts the same payload of the `Astro.rewrite()` function . The location of the rewrite path can be provided as a string, URL, or `Request`.

When you have multiple middleware functions chained via sequence() , submitting a path to `next()` will rewrite the `Request` in place and the middleware will not execute again. The next middleware function in the chain will receive the new `Request` with its updated `context`.

Calling `next()` with this signature will create a new `Request` object using the old `ctx.request`. This means that trying to consume `Request.body`, either before or after this rewrite, will throw a runtime error. This error is often raised with Astro Actions that use HTML forms . In these cases, we recommend handling rewrites from your Astro templates using `Astro.rewrite()` instead of using middleware.

 src/middleware.js ` // Current URL is https://example.com/blog
 // First middleware function async function first ( context , next ) { console . log ( context . url . pathname ) // this will log "/blog" // Rewrite to a new route, the homepage // Return updated `context` which is passed to next function return next ( " / " ) }
 // Current URL is still https://example.com/blog
 // Second middleware function async function second ( context , next ) { // Receives updated `context` console . log ( context . url . pathname ) // this will log "/" return next () }
 export const onRequest = sequence ( first , second ); `

## Error pages
 Section titled “Error pages”
 Middleware will attempt to run for all on-demand rendered pages, even when a matching route cannot be found. This includes Astro’s default (blank) 404 page and any custom 404 pages. However, it is up to the adapter to decide whether that code runs. Some adapters may serve a platform-specific error page instead.

Middleware will also attempt to run before serving a 500 error page, including a custom 500 page, unless the server error occurred in the execution of the middleware itself. If your middleware does not run successfully, then you will not have access to `Astro.locals` to render your 500 page.

 Learn

 Contribute

 Community

 Sponsor

## Internationalization

# Internationalization (i18n) Routing

 Astro’s internationalization (i18n) features allow you to adapt your project for an international audience. This routing API helps you generate, use, and verify the URLs that your multi-language site produces.

Astro’s i18n routing allows you to bring your multilingual content with support for configuring a default language, computing relative page URLs, and accepting preferred languages provided by your visitor’s browser. You can also specify fallback languages on a per-language basis so that your visitors can always be directed to existing content on your site.

## Routing Logic
 Section titled “Routing Logic”
 Astro uses a middleware to implement its routing logic. This middleware function is placed in the first position where it awaits every `Response` coming from any additional middleware and each page route before finally executing its own logic.

This means that operations (e.g. redirects) from your own middleware and your page logic are run first, your routes are rendered, and then the i18n middleware performs its own actions such as verifying that a localized URL corresponds to a valid route.

You can also choose to add your own i18n logic in addition to or instead of Astro’s i18n middleware , giving you even more control over your routes while still having access to the `astro:i18n` helper functions.

## Configure i18n routing
 Section titled “Configure i18n routing”
 Both a list of all supported languages ( `locales` ) and a default language ( `defaultLocale` ), which must be one of the languages listed in `locales`, need to be specified in an `i18n` configuration object. Additionally, you can configure more specific routing and fallback behavior to match your desired URLs.

 - astro.config.mjs ` import { defineConfig } from " astro/config " export default defineConfig ({ i18n: { locales: [ " es " , " en " , " pt-br " ], defaultLocale: " en " , } }) `

### Create localized folders
 Section titled “Create localized folders”
 Organize your content folders with localized content by language. Create individual `/[locale]/` folders anywhere within `src/pages/` and Astro’s file-based routing will create your pages at corresponding URL paths.

Your folder names must match the items in `locales` exactly. Include a localized folder for your `defaultLocale` only if you configure `prefixDefaultLocale: true` to show a localized URL path for your default language (e.g. `/en/about/`).

 Directory src
 Directory pages
 about.astro
- index.astro
- Directory es
 about.astro
- index.astro
 - Directory pt-br
 about.astro
- index.astro

### Create links
 Section titled “Create links”
 With i18n routing configured, you can now compute links to pages within your site using the helper functions such as `getRelativeLocaleUrl()` available from the `astro:i18n` module . These generated links will always provide the correct, localized route and can help you correctly use, or check, URLs on your site.

You can also still write the links manually.

 src/pages/es/index.astro ` --- import { getRelativeLocaleUrl } from ' astro:i18n ' ;
 // defaultLocale is "es" const aboutURL = getRelativeLocaleUrl ( " es " , " about " ); ---
 &#x3C; a href = " /get-started/ " > ¡Vamos! &#x3C;/ a > &#x3C; a href = { getRelativeLocaleUrl ( ' es ' , ' blog ' ) } > Blog &#x3C;/ a > &#x3C; a href = { aboutURL } > Acerca &#x3C;/ a > ` ¡Vamos!  Blog  Acerca ">

## `routing`
 Section titled “routing”
 Astro’s built-in file-based routing automatically creates URL routes for you based on your file structure within `src/pages/`.

When you configure i18n routing, information about this file structure (and the corresponding URL paths generated) is available to the i18n helper functions so they can generate, use, and verify the routes in your project. Many of these options can be used together for even more customization and per-language flexibility.

You can even choose to implement your own routing logic manually for even greater control.

### `prefixDefaultLocale`
 Section titled “prefixDefaultLocale”

 Added in:
 `astro@3.5.0`

This routing option defines whether or not your default language’s URLs should use a language prefix (e.g. `/en/about/`).

All non-default supported languages will use a localized prefix (e.g. `/fr/` or `/french/`) and content files must be located in appropriate folders. This configuration option allows you to specify whether your default language should also follow a localized URL structure.

This setting also determines where the page files for your default language must exist (e.g. `src/pages/about/` or `src/pages/en/about`) as the file structure and URL structure must match for all languages.

-
`"prefixDefaultLocale: false"` (default): URLs in your default language will not have a `/[locale]/` prefix. All other locales will.

-
`"prefixDefaultLocale: true"`: All URLs, including your default language, will have a `/[locale]/` prefix.

#### `prefixDefaultLocale: false`
 Section titled “prefixDefaultLocale: false”
 astro.config.mjs
```
` import { defineConfig } from " astro/config " export default defineConfig ({ i18n: { locales: [ " es " , " en " , " fr " ], defaultLocale: " en " , routing: { prefixDefaultLocale: false } } }) `
```

 This is the default value. Set this option when URLs in your default language will not have a `/[locale]/` prefix and files in your default language exist at the root of `src/pages/`:

 - Directory src
 Directory pages
 about.astro
- index.astro
- Directory es
 about.astro
- index.astro
 - Directory fr
 about.astro
- index.astro

- `src/pages/about.astro` will produce the route `example.com/about/`

- `src/pages/fr/about.astro` will produce the route `example.com/fr/about/`

#### `prefixDefaultLocale: true`
 Section titled “prefixDefaultLocale: true”
 astro.config.mjs
```
` import { defineConfig } from " astro/config " export default defineConfig ({ i18n: { locales: [ " es " , " en " , " fr " ], defaultLocale: " en " , routing: { prefixDefaultLocale: true } } }) `
```

 Set this option when all routes will have their `/locale/` prefix in their URL and when all page content files, including those for your `defaultLocale`, exist in a localized folder:

 - Directory src
 Directory pages
 index.astro // Note: this file is always required
- Directory en
 index.astro
- about.astro
 - Directory es
 about.astro
- index.astro
 - Directory pt-br
 about.astro
- index.astro

- URLs without a locale prefix, (e.g. `example.com/about/`) will return a 404 (not found) status code unless you specify a fallback strategy .

#### Opting out of redirects for the home URL
 Section titled “Opting out of redirects for the home URL”
 Even with your default locale routes prefixed, this behaviour does not apply by default to your site’s index page. This allows you to have a home page that exists outside of your configured locale structure, where all of your localized routes are prefixed except the home URL of your site.

You can opt out of this behavior so that your main site URL will also redirect to a prefixed, localized route for your default locale. When `prefixDefaultLocale: true` is set, you can additionally configure `redirectToDefaultLocale: true`. This will ensure that the home URL (`/`) generated by `src/pages/index.astro` will redirect to `/[defaultLocale]/`.

### `manual`
 Section titled “manual”

 Added in:
 `astro@4.6.0`

When this option is enabled, Astro will disable its i18n middleware so that you can implement your own custom logic. No other `routing` options (e.g. `prefixDefaultLocale`) may be configured with `routing: "manual"`.

You will be responsible for writing your own routing logic, or executing Astro’s i18n middleware manually alongside your own.

 astro.config.mjs ` import { defineConfig } from " astro/config " export default defineConfig ({ i18n: { locales: [ " es " , " en " , " fr " ], defaultLocale: " en " , routing: " manual " } }) `
 Astro provides helper functions for your middleware so you can control your own default routing, exceptions, fallback behavior, error catching, etc: `redirectToDefaultLocale()` , `notFound()` , and `redirectToFallback()` :

 src/middleware.js ` import { defineMiddleware } from " astro:middleware " ; import { redirectToDefaultLocale } from " astro:i18n " ; // function available with `manual` routing export const onRequest = defineMiddleware ( async ( ctx , next ) => { if ( ctx . url . startsWith ( " /about " )) { return next () ; } else { return redirectToDefaultLocale ( 302 ) ; } } ) ` { if (ctx.url.startsWith(&#x22;/about&#x22;)) { return next(); } else { return redirectToDefaultLocale(302); }})">

#### middleware function
 Section titled “middleware function”
 The `middleware()` function manually creates Astro’s i18n middleware. This allows you to extend Astro’s i18n routing instead of completely replacing it.

You can run `middleware()` with routing options in combination with your own middleware, using the `sequence()` utility to determine the order:

 src/middleware.js ` import { defineMiddleware, sequence } from " astro:middleware " ; import { middleware } from " astro:i18n " ; // Astro's own i18n routing config
 export const userMiddleware = defineMiddleware ( async ( ctx , next ) => { // this response might come from Astro's i18n middleware, and it might return a 404 const response = await next () ; // the /about page is an exception and we want to render it if ( ctx . url . pathname . startsWith ( " /about " )) { return new Response ( " About page " , { status: 200 , } ) ; } else { return response ; } } );
 export const onRequest = sequence ( userMiddleware , middleware ( { redirectToDefaultLocale: false , prefixDefaultLocale: true , fallbackType: " redirect " , } ) , ); ` { // this response might come from Astro&#x27;s i18n middleware, and it might return a 404 const response = await next(); // the /about page is an exception and we want to render it if (ctx.url.pathname.startsWith(&#x22;/about&#x22;)) { return new Response(&#x22;About page&#x22;, { status: 200, }); } else { return response; }});export const onRequest = sequence( userMiddleware, middleware({ redirectToDefaultLocale: false, prefixDefaultLocale: true, fallbackType: &#x22;redirect&#x22;, }),);">

## `domains`
 Section titled “domains”

 Added in:
 `astro@4.9.0`

This routing option allows you to customize your domains on a per-language basis for `server` rendered projects using the `@astrojs/node` or `@astrojs/vercel` adapter with a `site` configured.

Add `i18n.domains` to map any of your supported `locales` to custom URLs:

 astro.config.mjs ` import { defineConfig } from " astro/config " export default defineConfig ({ site: " https://example.com " , output: " server " , // required, with no prerendered pages adapter: node ({ mode: ' standalone ' , }), i18n: { locales: [ " es " , " en " , " fr " , " ja " ], defaultLocale: " en " , routing: { prefixDefaultLocale: false }, domains: { fr: " https://fr.example.com " , es: " https://example.es " } } }) `
 All non-mapped `locales` will follow your `prefixDefaultLocales` configuration.

With the above configuration:

- The file `/fr/about.astro` will create the URL `https://fr.example.com/about`.

- The file `/es/about.astro` will create the URL `https://example.es/about`.

- The file `/ja/about.astro` will create the URL `https://example.com/ja/about`.

- The file `/about.astro` will create the URL `https://example.com/about`.

The above URLs will also be returned by the `getAbsoluteLocaleUrl()` and `getAbsoluteLocaleUrlList()` functions.

## Fallback
 Section titled “Fallback”
 When a page in one language doesn’t exist (e.g. a page that is not yet translated), instead of displaying a 404 page, you can choose to display fallback content from another `locale` on a per-language basis. This is useful when you do not yet have a page for every route, but you want to still provide some content to your visitors.

Your fallback strategy consists of two parts: choosing which languages should fallback to which other languages ( `i18n.fallback` ) and choosing whether to perform a redirect or a rewrite to show the fallback content ( `i18n.routing.fallbackType` added in Astro v4.15.0).

For example, when you configure `i18n.fallback: { fr: "es" }`, Astro will ensure that a page is built in `src/pages/fr/` for every page that exists in `src/pages/es/`.

If any page does not already exist, then a page will be created depending on your `fallbackType`:

- With a redirect to the corresponding `es` route (default behavior).

- With the content of the `/es/` page (`i18n.routing.fallbackType: "rewrite"`).

For example, the configuration below sets `es` as the fallback locale for any missing `fr` routes. This means that a user visiting `example.com/fr/my-page/` will be shown the content for `example.com/es/my-page/` (without being redirected) instead of being taken to a 404 page when `src/pages/fr/my-page.astro` does not exist.

 astro.config.mjs ` import { defineConfig } from " astro/config " export default defineConfig ({ i18n: { locales: [ " es " , " en " , " fr " ], defaultLocale: " en " , fallback: { fr: " es " }, routing: { fallbackType: " rewrite " } } }) `

## Custom locale paths
 Section titled “Custom locale paths”
 In addition to defining your site’s supported `locales` as strings (e.g. “en”, “pt-br”), Astro also allows you to map an arbitrary number of browser-recognized language `codes` to a custom URL `path`. While locales can be strings of any format as long as they correspond to your project folder structure, `codes` must follow the browser’s accepted syntax.

Pass an object to the `locales` array with a `path` key to define a custom URL prefix, and `codes` to indicate the languages mapped to this URL. In this case, your `/[locale]/` folder name must match exactly the value of the `path` and your URLs will be generated using the `path` value.

This is useful if you support multiple variations of a language (e.g. `"fr"`, `"fr-BR"`, and `"fr-CA"`) and you want to have all these variations mapped under the same URL `/fr/`, or even customize it entirely (e.g. `/french/`):

 astro.config.mjs ` import { defineConfig } from " astro/config " export default defineConfig ({ i18n: { locales: [ " es " , " en " , " fr " ], locales: [ " es " , " en " , { path: " french " , // no slashes included codes: [ " fr " , " fr-BR " , " fr-CA " ] }], defaultLocale: " en " , routing: { prefixDefaultLocale: true } } }) `
 When using functions from the `astro:i18n` virtual module to compute valid URL paths based on your configuration (e.g. `getRelativeLocaleUrl()`), use the `path` as the value for `locale` .

#### Limitations
 Section titled “Limitations”
 This feature has some restrictions:

- The `site` option is mandatory.

- The `output` option must be set to `"server"`.

- There cannot be any individual prerendered pages.

Astro relies on the following headers in order to support the feature:

- `X-Forwarded-Host` and `Host` . Astro will use the former, and if not present, will try the latter.

- `X-Forwarded-Proto` and `URL#protocol` of the server request.

Make sure that your server proxy/hosting platform is able to provide this information. Failing to retrieve these headers will result in a 404 (status code) page.

## Browser language detection
 Section titled “Browser language detection”
 Astro’s i18n routing allows you to access two properties for browser language detection in pages rendered on demand: `Astro.preferredLocale` and `Astro.preferredLocaleList`. All pages, including static prerendered pages, have access to `Astro.currentLocale`.

These combine the browser’s `Accept-Language` header, and your `locales` (strings or `codes`) to automatically respect your visitor’s preferred languages.

-
 `Astro.preferredLocale` : Astro can compute a preferred locale for your visitor if their browser’s preferred locale is included in your `locales` array. This value is undefined if no such match exists.

-
 `Astro.preferredLocaleList` : An array of all locales that are both requested by the browser and supported by your website. This produces a list of all compatible languages between your site and your visitor. The value is `[]` if none of the browser’s requested languages are found in your `locales` array. If the browser does not specify any preferred languages, then this value will be `i18n.locales` .

-
 `Astro.currentLocale` : The locale computed from the current URL, using the syntax specified in your `locales` configuration. If the URL does not contain a `/[locale]/` prefix, then the value will default to `i18n.defaultLocale` .

In order to successfully match your visitors’ preferences, provide your `codes` using the same pattern used by the browser .

 Learn

 Contribute

 Community

 Sponsor

## Prefetch

# Prefetch

 Page load times play a big role in the usability and overall enjoyment of a site. Astro’s opt-in prefetching brings the benefits of near-instant page navigations to your multi-page application (MPA) as your visitors interact with the site.

## Enable prefetching
 Section titled “Enable prefetching”
 You can enable prefetching with the `prefetch` config:

 - astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ prefetch: true }); `
 A prefetch script will be added to all pages of your site. You can then add the `data-astro-prefetch` attribute to any `&#x3C;a />` links on your site to opt-in to prefetching. When you hover over the link, the script will fetch the page in the background.

 ` &#x3C; a href = " /about " data-astro-prefetch > ` ">
 Note that prefetching only works for links within your site, and not external links.

## Prefetch configuration
 Section titled “Prefetch configuration”
 The `prefetch` config also accepts an option object to further customize prefetching.

### Prefetch strategies
 Section titled “Prefetch strategies”
 Astro supports 4 prefetch strategies for various use cases:

 `hover` (default): Prefetch when you hover over or focus on the link.

- `tap`: Prefetch just before you click on the link.

- `viewport`: Prefetch as the links enter the viewport.

- `load`: Prefetch all links on the page after the page is loaded.

You can specify a strategy for an individual link by passing it to the `data-astro-prefetch` attribute:

 ` &#x3C; a href = " /about " data-astro-prefetch = " tap " > About &#x3C;/ a > ` About ">
 Each strategy is fine-tuned to only prefetch when needed and save your users’ bandwidth. For example:

- If a visitor is using data saver mode or has a slow connection , prefetch will fallback to the `tap` strategy.

- Quickly hovering or scrolling over links will not prefetch them.

### Default prefetch strategy
 Section titled “Default prefetch strategy”
 The default prefetch strategy when adding the `data-astro-prefetch` attribute is `hover`. To change it, you can configure `prefetch.defaultStrategy` in your `astro.config.mjs` file:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ prefetch: { defaultStrategy: ' viewport ' } }); `

### Prefetch all links by default
 Section titled “Prefetch all links by default”
 If you want to prefetch all links, including those without the `data-astro-prefetch` attribute, you can set `prefetch.prefetchAll` to `true`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ prefetch: { prefetchAll: true } }); `
 You can then opt-out of prefetching for individual links by setting `data-astro-prefetch="false"`:

 ` &#x3C; a href = " /about " data-astro-prefetch = " false " > About &#x3C;/ a > ` About ">
 The default prefetch strategy for all links can be changed with `prefetch.defaultStrategy` as shown in the Default prefetch strategy section .

## Prefetch programmatically
 Section titled “Prefetch programmatically”
 As some navigation might not always appear as `&#x3C;a />` links, you can also prefetch programmatically with the `prefetch()` API from the `astro:prefetch` module:

 ` &#x3C; button id = " btn " > Click me &#x3C;/ button >
 &#x3C; script > import { prefetch } from ' astro:prefetch ' ;
 const btn = document . getElementById ( ' btn ' ); btn . addEventListener ( ' click ' , () => { prefetch ( ' /about ' ); }); &#x3C;/ script > ` Click me ">
 The `prefetch()` API includes the same data saver mode and slow connection detection so that it only prefetches when needed.

To ignore slow connection detection, you can use the `ignoreSlowConnection` option:

 ` // Prefetch even on data saver mode or slow connection prefetch ( ' /about ' , { ignoreSlowConnection: true }); `

### `eagerness`
 Section titled “eagerness”
 Type: `'immediate' | 'eager' | 'moderate' | 'conservative'`
 Default: `'immediate'`

 Added in:
 `astro@5.6.0`

With the experimental `clientPrerender` flag enabled, you can use the `eagerness` option on `prefetch()` to suggest to the browser how eagerly it should prefetch/prerender link targets.

This follows the same API described in the Speculation Rules API and defaults to `immediate` (the most eager option). In decreasing order of eagerness, the other options are `eager`, `moderate`, and `conservative`.

The `eagerness` option allows you to balance the benefit of reduced wait times against bandwidth, memory, and CPU costs for your site visitors. Some browsers, such as Chrome, have limits in place to guard against over-speculating (prerendering/prefetching too many links).

 ` --- --- &#x3C; script > // Control prefetching eagerness with `experimental.clientPrerender` import { prefetch } from ' astro:prefetch ' ;
 // This page is resource-intensive prefetch ( ' /data-heavy-dashboard ' , { eagerness: ' conservative ' });
 // This page is critical to the visitor's journey prefetch ( ' /getting-started ' ); // defaults to `{ eagerness: 'immediate' }`
 // This page may not be visited prefetch ( ' /terms-of-service ' , { eagerness: ' moderate ' }); &#x3C;/ script > `
 To use `prefetch()` programmatically with large sets of links, you can set `eagerness: 'moderate'` to take advantage of First In, First Out (FIFO) strategies and browser heuristics to let the browser decide when to prerender/prefetch them and in what order:

 ` &#x3C; a class = " link-moderate " href = " /nice-link-1 " > A Nice Link 1 &#x3C;/ a > &#x3C; a class = " link-moderate " href = " /nice-link-2 " > A Nice Link 2 &#x3C;/ a > &#x3C; a class = " link-moderate " href = " /nice-link-3 " > A Nice Link 3 &#x3C;/ a > &#x3C; a class = " link-moderate " href = " /nice-link-4 " > A Nice Link 4 &#x3C;/ a > ... &#x3C; a class = " link-moderate " href = " /nice-link-20 " > A Nice Link 20 &#x3C;/ a >
 &#x3C; script > import { prefetch } from ' astro:prefetch ' ;
 const linkModerate = document . getElementsByClassName ( ' link-moderate ' ); linkModerate . forEach ( ( link ) => prefetch ( link . getAttribute ( ' href ' ), {eagerness: ' moderate ' } ));
 &#x3C;/ script > ` A Nice Link 1  A Nice Link 2  A Nice Link 3  A Nice Link 4 ... A Nice Link 20 ">
 Make sure to only import `prefetch()` in client-side scripts as it relies on browser APIs.

## Using with View Transitions
 Section titled “Using with View Transitions”
 When you use Astro’s `&#x3C;ClientRouter />` on a page, prefetching will also be enabled by default. It sets a default configuration of `{ prefetchAll: true }` which enables prefetching for all links on the page.

You can customize the prefetch configuration in `astro.config.mjs` to override the default. For example:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ // Disable prefetch completely prefetch: false }); `
 astro.config.mjs
```
` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ // Keep prefetch, but only prefetch for links with `data-astro-prefetch` prefetch: { prefetchAll: false } }); `
```

## Browser support
 Section titled “Browser support”
 Astro’s prefetching uses `&#x3C;link rel="prefetch">` if supported by the browser, and falls back to the `fetch()` API otherwise.

The most common browsers support Astro’s prefetching with subtle differences:

### Chrome
 Section titled “Chrome”
 Chrome supports `&#x3C;link rel="prefetch">`. Prefetching works as intended.

It also fully supports `&#x3C;script type="speculationrules">` from the Speculation Rules API , which can be used to further describe prefetching strategies and rules , enhancing user experience for your Chrome users. You’ll need to enable `clientPrerender` experiment to utilize this functionality with `prefetch()`

### Firefox
 Section titled “Firefox”
 Firefox supports `&#x3C;link rel="prefetch">` but may display errors or fail entirely:

- Without an explicit cache header (e.g. `Cache-Control` or `Expires` ), prefetching will error with `NS_BINDING_ABORTED`.

- Even in the event of an error, if the response has a proper `ETag` header, it will be re-used on navigation.

- Otherwise, if it errors with no other cache headers, the prefetch will not work.

### Safari
 Section titled “Safari”
 Safari does not support `&#x3C;link rel="prefetch">` and will fall back to the `fetch()` API which requires cache headers (e.g. `Cache-Control` , `Expires` , and `ETag` ) to be set. Otherwise, the prefetch will not work.

 Edge case: `ETag` headers do not work in private windows.

### Recommendations
 Section titled “Recommendations”
 To best support all browsers, make sure your pages have the proper cache headers.

For static or prerendered pages, the `ETag` header is often automatically set by the deployment platform and is expected to work out of the box.

For dynamic and server-side rendered pages, set the appropriate cache headers yourself based on the page content. Visit the MDN documentation on HTTP caching for more information.

## Migrating from `@astrojs/prefetch`
 Section titled “Migrating from @astrojs/prefetch”
 The `@astrojs/prefetch` integration was deprecated in v3.5.0 and is no longer maintained. Use the following instructions to migrate to Astro’s built-in prefetching which replaces this integration.

-
Remove the `@astrojs/prefetch` integration and enable the `prefetch` config in `astro.config.mjs`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import prefetch from ' @astrojs/prefetch ' ;
 export default defineConfig ({ integrations: [ prefetch ()], prefetch: true }); `

-
 Convert from `@astrojs/prefetch`’s configuration options:

The deprecated integration used the `selector` config option to specify which links should be prefetched upon entering the viewport.

Add `data-astro-prefetch="viewport"` to these individual links instead.

 ` &#x3C; a href = " /about " data-astro-prefetch = " viewport " > ` ">

-
 The deprecated integration used the `intentSelector` config option to specify which links should be prefetched when they were hovered over or focused.

Add `data-astro-prefetch` or `data-astro-prefetch="hover"` to these individual links instead:

 ` &#x3C;!-- You can omit the value if `defaultStrategy` is set to `hover` (default) --> &#x3C; a href = " /about " data-astro-prefetch >
 &#x3C;!-- Otherwise, you can explicitly define the prefetch strategy --> &#x3C; a href = " /about " data-astro-prefetch = " hover " > `  ">

-
 The `throttles` option from `@astrojs/prefetch` is no longer needed as the new prefetch feature will automatically schedule and prefetch optimally.

 Learn

 Contribute

 Community

 Sponsor

## View Transitions

# View transitions

 View transitions are animated transitions between different website views. They are a popular design choice for preserving visual continuity as visitors move between states or views of an application.

Astro’s view transitions and client-side routing support is powered by the View Transitions browser API and also includes:

- A few built-in animation options , such as `fade`, `slide`, and `none`.

- Support for both forwards and backwards navigation animations.

- The ability to fully customize all aspects of transition animation , and build your own animations.

- A way to carry HTML elements from the current page to the next during navigation.

- The option to prevent client-side navigation for non-page links .

- Control over fallback behavior for browsers that do not yet support the View Transition APIs.

- Automatic support for `prefers-reduced-motion` .

## Differences between browser-native view transitions and Astro’s `&#x3C;ClientRouter />`
 Section titled “Differences between browser-native view transitions and Astro’s &#x3C;ClientRouter />”
 Browser-native, cross-document view transitions can be used in Astro to animate the navigation between documents in a multi-page app (MPA), often providing the experience of client-side routing of single-page applications. They don’t alter the core functionality of a multi-page application, nor do they affect any existing scripts or add additional JavaScript to your page load. They simply add animations.

For enhanced client-side routing and view transition features not yet fully supported by the View Transition API, Astro provides a built-in, lightweight component to enable client-side routing and turn your multi-page app into a single-page app with smooth animations on navigation.

That comes with some benefits, like shared state across pages and persistent elements, and some drawbacks, such as needing to manually reinitialize scripts or state after navigation.

Adding Astro’s built-in `&#x3C;ClientRouter />` component:

- intercepts page navigation and gives you considerable control over this process.

- extends and enhances some View Transition/Navigation API features.

- allows you to configure fallback strategies for when native browser support is lacking .

However, as browser APIs and web standards evolve, using Astro’s `&#x3C;ClientRouter />` for this additional functionality will increasingly become unnecessary . We recommend keeping up with the current state of browser APIs so you can decide whether you still need Astro’s client-side routing for the specific features you use.

## Enabling view transitions (SPA mode)
 Section titled “Enabling view transitions (SPA mode)”
 Import and add the `&#x3C;ClientRouter />` component to your common `&#x3C;head>` or shared layout component. Astro will create default page animations based on the similarities between the old and new page, and will also provide fallback behavior for unsupported browsers.

The example below shows adding Astro’s default page navigation animations site-wide, including the default fallback control option for non-supporting browsers, by importing and adding this component to a `&#x3C;CommonHead />` Astro component:

 - src/components/CommonHead.astro ` --- import { ClientRouter } from " astro:transitions " ; --- &#x3C; link rel = " icon " type = " image/svg+xml " href = " /favicon.svg " /> &#x3C; meta name = " generator " content = { Astro . generator } />
 &#x3C;!-- Primary Meta Tags --> &#x3C; title > { title } &#x3C;/ title > &#x3C; meta name = " title " content = { title } /> &#x3C; meta name = " description " content = { description } />
 &#x3C; ClientRouter /> `   {title}    ">
 No other configuration is necessary to enable Astro’s default client-side navigation!

Use transition directives or override default client-side navigation on individual elements for finer control.

## Transition Directives
 Section titled “Transition Directives”
 Astro will automatically assign corresponding elements found in both the old page and the new page a shared, unique `view-transition-name`. This pair of matching elements is inferred by both the type of element and its location in the DOM.

Use optional `transition:*` directives on page elements in your `.astro` components for finer control over the page transition behaviour during navigation.

 `transition:name`: Allows you to override Astro’s default element matching for old/new content animation and specify a transition name to associate a pair of DOM elements.

- `transition:animate`: Allows you to override Astro’s default animation while replacing the old element with the new one by specifying an animation type. Use Astro’s built-in animation directives or create custom transition animations .

- `transition:persist`: Allows you to override Astro’s default replacing old elements for new ones and instead persist components and HTML elements when navigating to another page.

### Naming a transition
 Section titled “Naming a transition”
 In some cases, you may want or need to identify the corresponding view transition elements yourself. You can specify a name for a pair of elements using the `transition:name` directive.

 src/pages/old-page.astro ` &#x3C; aside transition:name = " hero " > ` You can also manually identify corresponding elements if the island/element is in a different component between the two pages.

 src/pages/old-page.astro ` &#x3C; video controls muted autoplay transition:name = " media-player " transition:persist /> ` ">
 src/pages/new-page.astro
```
` &#x3C; MyVideo controls muted autoplay transition:name = " media-player " transition:persist /> `
```
 ">
 As a convenient shorthand, `transition:persist` can alternatively take a transition name as a value.

 src/pages/index.astro ` &#x3C; video controls muted autoplay transition:persist = " media-player " > ` ">

#### `transition:persist-props`
 Section titled “transition:persist-props”

 Added in:
 `astro@4.5.0`

This allows you to control whether or not an island’s props should be persisted upon navigation.

By default, when you add `transition:persist` to an island, the state is retained upon navigation, but your component will re-render with new props. This is useful, for example, when a component receives page-specific props such as the current page’s `title`.

You can override this behavior by setting `transition:persist-props` in addition to `transition:persist`. Adding this directive will keep an island’s existing props (not re-render with new values) in addition to maintaining its existing state.

### Built-in Animation Directives
 Section titled “Built-in Animation Directives”
 Astro comes with a few built-in animations to override the default `fade` transition. Add the `transition:animate` directive to individual elements to customize the behavior of specific transitions.

- `fade` (default): An opinionated crossfade animation. The old content fades out and the new content fades in.

- `initial`: Opt out of Astro’s opinionated crossfade animation and use the browser’s default styling.

- `slide`: An animation where the old content slides out to the left and new content slides in from the right. On backwards navigation, the animations are the opposite.

- `none`: Disable the browser’s default animations. Use on a page’s `&#x3C;html>` element to disable the default fade for every element on the page.

Combine directives for full control over your page animation. Set a page default on the `&#x3C;html>` element, and override on any individual elements as desired.

The example below produces a slide animation for the body content while disabling the browser’s default fade animation for the rest of the page:

```
` --- import CommonHead from " ../components/CommonHead.astro " ; ---
 &#x3C; html transition:name = " root " transition:animate = " none " > &#x3C; head > &#x3C; CommonHead /> &#x3C;/ head > &#x3C; body > &#x3C; header > ... &#x3C;/ header > &#x3C;!-- Override your page default on a single element --> &#x3C; main transition:animate = " slide " > ... &#x3C;/ main > &#x3C;/ body > &#x3C;/ html > `
```
         ...