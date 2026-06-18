# Astro - Server Rendering


## On Demand Rendering

# On-demand rendering

 Your Astro project code must be rendered to HTML in order to be displayed on the web.

By default, Astro pages, routes, and API endpoints will be pre-rendered at build time as static pages. However, you can choose to render some or all of your routes on demand by a server when a route is requested.

On-demand rendered pages and routes are generated per visit, and can be customized for each viewer. For example, a page rendered on demand can show a logged-in user their account information or display freshly updated data without requiring a full-site rebuild.

On-demand rendering on the server at request time is also known as server-side rendering (SSR) .

## Server adapters
 Section titled “Server adapters”
 To render any page on demand, you need to add an adapter . Each adapter allows Astro to output a script that runs your project on a specific runtime : the environment that runs code on the server to generate pages when they are requested (e.g. Netlify, Cloudflare).

You may also wish to add an adapter even if your site is entirely static and you are not rendering any pages on demand. For example, the Netlify adapter enables Netlify’s Image CDN, and server islands require an adapter installed to use `server:defer` on a component.

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

Astro maintains official adapters for Node.js , Netlify , Vercel , and Cloudflare . You can find both official and community adapters in our integrations directory . Choose the one that corresponds to your deployment environment .

### Add an Adapter
 Section titled “Add an Adapter”
 You can add any of the official adapter integrations maintained by Astro with the following `astro add` command. This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

For example, to install the Netlify adapter, run:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npx astro add netlify `

 Terminal window
```
` pnpm astro add netlify `
```

 Terminal window
```
` yarn astro add netlify `
```

 You can also add an adapter manually by installing the NPM package (e.g. `@astrojs/netlify`) and updating `astro.config.mjs` yourself.

Note that different adapters may have different configuration settings. Read each adapter’s documentation, and apply any necessary config options to your chosen adapter in `astro.config.mjs`

## Enabling on-demand rendering
 Section titled “Enabling on-demand rendering”
 By default, your entire Astro site will be prerendered , and static HTML pages will be sent to the browser. However, you may opt out of prerendering on any routes that require server rendering, for example, a page that checks for cookies and displays personalized content.

First, add an adapter integration for your server runtime to enable on-demand server rendering in your Astro project.

Then, add `export const prerender = false` at the top of the individual page or endpoint you want to render on demand. The rest of your site will remain a static site:

 src/pages/page-rendered-on-demand.astro ` --- export const prerender = false --- &#x3C; html > &#x3C;!-- This content will be server-rendered on demand! Just add an adapter integration for a server runtime! All other pages are statically-generated at build time! --> &#x3C; html > `  ">
 The following example shows opting out of prerendering in order to display a random number each time the endpoint is hit:

 src/pages/randomnumber.js ` export const prerender = false ;
 export async function GET () { let number = Math . random (); return new Response ( JSON . stringify ({ number , message: ` Here's a random number: ${ number } ` , }) , ); } `

### `'server'` mode
 Section titled “'server' mode”
 For a highly dynamic app , after adding an adapter, you can set your build output configuration to `output: 'server'` to server-render all your pages by default . This is the equivalent of opting out of prerendering on every page.

Then, if needed, you can choose to prerender any individual pages that do not require a server to execute, such as a privacy policy or about page.

 src/pages/about-my-app.astro ` --- export const prerender = true --- &#x3C; html > &#x3C;!-- `output: 'server'` is configured, but this page is static! The rest of my site is rendered on demand! --> &#x3C; html > `  ">
 Add `export const prerender = true` to any page or route to prerender a static page or endpoint:

 src/pages/myendpoint.js ` export const prerender = true ;
 export async function GET () { return new Response ( JSON . stringify ({ message: ` This is my static endpoint ` , }) , ); } `

 See more about the `output` setting in the configuration reference.

## On-demand rendering features
 Section titled “On-demand rendering features”

### HTML streaming
 Section titled “HTML streaming”
 With HTML streaming, a document is broken up into chunks, sent over the network in order, and rendered on the page in that order. Astro uses HTML streaming in on-demand rendering to send each component to the browser as it renders them. This makes sure the user sees your HTML as fast as possible, although network conditions can cause large documents to be downloaded slowly, and waiting for data fetches can block page rendering.

 Related recipe:

 Using streaming to improve page performance

### Cookies
 Section titled “Cookies”
 A page or API endpoint rendered on demand can check, set, get, and delete cookies.

The example below updates the value of a cookie for a page view counter:

 src/pages/index.astro ` --- export const prerender = false ; // Not needed in 'server' mode
 let counter = 0
 if (Astro . cookies . has ( ' counter ' )) { const cookie = Astro . cookies . get ( ' counter ' ) const value = cookie ?. number () if (value !== undefined &#x26;&#x26; ! isNaN (value)) counter = value + 1 }
 Astro . cookies . set ( ' counter ' , String (counter)) --- &#x3C; html > &#x3C; h1 > Counter = { counter } &#x3C;/ h1 > &#x3C;/ html > ` 
# Counter = {counter}
 ">
 See more details about `Astro.cookies` and the `AstroCookie` type in the API reference.

### `Response`
 Section titled “Response”
 `Astro.response` is a standard `ResponseInit` object. It can be used to set the response status and headers.

The example below sets a response status and status text for a product page when the product does not exist:

 src/pages/product/[id].astro ` --- export const prerender = false ; // Not needed in 'server' mode
 import { getProduct } from ' ../api ' ;
 const product = await getProduct (Astro . params . id );
 // No product found if ( ! product) { Astro . response . status = 404 ; Astro . response . statusText = ' Not found ' ; } --- &#x3C; html > &#x3C;!-- Page here... --> &#x3C;/ html > `   ">

#### `Astro.response.headers`
 Section titled “Astro.response.headers”
 You can set headers using the `Astro.response.headers` object:

 src/pages/index.astro ` --- export const prerender = false ; // Not needed in 'server' mode
 Astro . response . headers . set ( ' Cache-Control ' , ' public, max-age=3600 ' ); --- &#x3C; html > &#x3C;!-- Page here... --> &#x3C;/ html > `   ">

#### Return a `Response` object
 Section titled “Return a Response object”
 You can also return a Response object directly from any page using on-demand rendering either manually or with `Astro.redirect` .

The example below looks up an ID in the database on a dynamic page and either it returns a 404 if the product does not exist, or it redirects the user to another page if the product is no longer available, or it displays the product:

 src/pages/product/[id].astro ` --- export const prerender = false ; // Not needed in 'server' mode
 import { getProduct } from ' ../api ' ;
 const product = await getProduct (Astro . params . id );
 // No product found if ( ! product) { return new Response ( null , { status: 404 , statusText: ' Not found ' }); }
 // The product is no longer available if ( ! product . isAvailable ) { return Astro . redirect ( " /products " , 301 ); } --- &#x3C; html > &#x3C;!-- Page here... --> &#x3C;/ html > `   ">

### `Request`
 Section titled “Request”
 `Astro.request` is a standard Request object. It can be used to get the `url`, `headers`, `method`, and even the body of the request.

You can access additional information from this object for pages that are not statically generated.

#### `Astro.request.headers`
 Section titled “Astro.request.headers”
 The headers for the request are available on `Astro.request.headers`. This works like the browser’s `Request.headers` . It is a Headers object where you can retrieve headers such as the cookie.

 src/pages/index.astro ` --- export const prerender = false ; // Not needed in 'server' mode
 const cookie = Astro . request . headers . get ( ' cookie ' ); // ... --- &#x3C; html > &#x3C;!-- Page here... --> &#x3C;/ html > `   ">

#### `Astro.request.method`
 Section titled “Astro.request.method”
 The HTTP method used in the request is available as `Astro.request.method`. This works like the browser’s `Request.method` . It returns the string representation of the HTTP method used in the request.

 src/pages/index.astro ` --- export const prerender = false ; // Not needed in 'server' mode
 console . log (Astro . request . method ) // GET (when navigated to in the browser) --- `
 See more details about `Astro.request` in the API reference.

### Server Endpoints
 Section titled “Server Endpoints”
 A server endpoint, also known as an API route , is a special function exported from a `.js` or `.ts` file within the `src/pages/` folder. A powerful feature of server-side rendering on demand, API routes are able to securely execute code on the server.

The function takes an endpoint context and returns a Response .

To learn more, see our Endpoints Guide .

 Learn

 Contribute

 Community

 Sponsor

## Server Islands

# Server islands

 Server islands allow you to on-demand render dynamic or personalized “islands” individually, without sacrificing the performance of the rest of the page.

This means your visitor will see the most important parts of your page sooner, and allows your main content to be more aggressively cached, providing faster performance.

## Server island components
 Section titled “Server island components”
 A server island is a normal server-rendered Astro component that is instructed to delay rendering until its contents are available.

Your page will be rendered immediately with any specified fallback content as a placeholder . Then, the component’s own contents are fetched on the client and displayed when available.

With an adapter installed to perform the delayed rendering, add the `server:defer` directive to any component on your page to turn it into its own island:

 - src/pages/index.astro ` --- import Avatar from ' ../components/Avatar.astro ' ; --- &#x3C; Avatar server:defer /> ` ">
 These components can do anything you normally would in an on-demand rendered page using an adapter, such as fetch content, and access cookies:

 src/components/Avatar.astro ` --- import { getUserAvatar } from ' ../sessions ' ; const userSession = Astro . cookies . get ( ' session ' ); const avatarURL = await getUserAvatar (userSession); --- &#x3C; img alt = " User avatar " src = { avatarURL } /> ` ">

### Passing props to server islands
 Section titled “Passing props to server islands”
 Props provided to server island components must be serializable : able to be translated into a format suitable for transfer over a network, or storage. Additionally, Astro does not serialize every type of serializable data structure. Therefore, there are some limitations on what can be passed as props to a server island.

Notably, functions cannot be passed to components marked with `server:defer` as they cannot be serialized. Objects with circular references are also not serializable.

The following prop types are supported:
plain object, `number`, `string`, `Array`, `Map`, `Set`, `RegExp`, `Date`, `BigInt`, `URL`, `Uint8Array`, `Uint16Array`, `Uint32Array`, and `Infinity`

## Server island fallback content
 Section titled “Server island fallback content”
 When using the `server:defer` attribute on a component to delay its rendering, you can “slot” in default loading content using the included named `"fallback"` slot.

Your fallback content will be rendered along with the rest of the page initially on page load and will be replaced with your component’s content when available.

To add fallback content, add `slot="fallback"` on a child (other components or HTML elements) passed to your server island component:

 ` --- import Avatar from ' ../components/Avatar.astro ' ; import GenericAvatar from ' ../components/GenericAvatar.astro ' ; --- &#x3C; Avatar server:defer > &#x3C; GenericAvatar slot = " fallback " /> &#x3C;/ Avatar > `   ">
 This fallback content can be things like:

 A generic avatar instead of the user’s own.

- Placeholder UI such as custom messages.

- Loading indicators such as spinners.

## How it works
 Section titled “How it works”
 Server island implementation happens mostly at build-time where component content is swapped out for a small script.

Each of the islands marked with `server:defer` is split off into its own special route which the script fetches at run time. When Astro builds your site it will omit the component and inject a script in its place, and any content you’ve marked with `slot="fallback"`.

When the page loads in the browser, these components will be requested to a special endpoint that renders them and returns the HTML. This means that users will see the most critical parts of the page instantly. Fallback content will be visible for a short amount of time before the dynamic islands are then loaded.

Each island is loaded independently from the rest. This means a slower island won’t delay the rest of your personalized content from being available.

This rendering pattern was built to be portable. It does not depend on any server infrastructure so it will work with any host you have, from a Node.js server in a Docker container to the serverless provider of your choice.

## Caching
 Section titled “Caching”
 The data for server islands is retrieved via a `GET` request, passing props as an encrypted string in the URL query. This allows caching data with the `Cache-Control` HTTP header using standard `Cache-Control` directives.

However, the browser limits URLs to a maximum length of 2048 bytes for practical reasons and to avoid causing denial-of-service problems. If your query string causes your URL to exceed this limit, Astro will instead send a `POST` request that contains all props in the body.

`POST` requests are not cached by browsers because they are used to submit data, and could cause data integrity or security issues. Therefore, any existing caching logic in your project will break. Whenever possible, pass only necessary props to your server islands and avoid sending entire data objects and arrays to keep your query small.

## Accessing the page URL in a server island
 Section titled “Accessing the page URL in a server island”
 In most cases you, your server island component can get information about the page rendering it by passing props like in normal components.

However, server islands run in their own isolated context outside of the page request. `Astro.url` and `Astro.request.url` in a server island component both return a URL that looks like `/_server-islands/Avatar` instead of the current page’s URL in the browser. Additionally, if you are prerendering the page you will not have access to information such as query parameters in order to pass as props.

To access information from the page’s URL, you can check the Referer header, which will contain the address of the page that is loading the island in the browser:

 ` --- const referer = Astro . request . headers . get ( ' Referer ' ); const url = new URL (referer); const productId = url . searchParams . get ( ' product ' ); --- `

## Reusing the encryption key
 Section titled “Reusing the encryption key”
 Astro uses cryptography to encrypt props passed to server islands, protecting sensitive data from accidental exposure. This encryption relies on a new, random key that is generated on each build and embedded in the server bundle.

Most deploy hosts will handle keeping your front end and back end in sync automatically. However, you may need a constant encryption key if you are using rolling deployments, multi-region hosting or a CDN that caches pages containing server islands.

In environments with rolling deployments (e.g., Kubernetes) where your frontend assets (which encrypt props) and your backend functions (which decrypt props) may be temporarily using different keys, or when a CDN is still serving pages built with an old key, encrypted props passed to your server island cannot be decrypted.

In these situations, use the Astro CLI to generate a reusable, encoded encryption key to set as an environment variable in your build environment:

 Terminal window ` astro create-key `
 Use this value to configure the `ASTRO_KEY` environment variable (e.g. in a `.env` file) and include it in your CI/CD or host’s build settings. This ensures the same key is always reused in the generated bundle so that encryption and decryption remain in sync.

 Learn

 Contribute

 Community

 Sponsor

## Actions

# Actions

 Added in:
 `astro@4.15`

Astro Actions allow you to define and call backend functions with type-safety. Actions perform data fetching, JSON parsing, and input validation for you. This can greatly reduce the amount of boilerplate needed compared to using an API endpoint .

Use actions instead of API endpoints for seamless communication between your client and server code and to:

- Automatically validate JSON and form data inputs using Zod validation .

- Generate type-safe functions to call your backend from the client and even from HTML form actions . No need for manual `fetch()` calls.

- Standardize backend errors with the `ActionError` object.

## Basic usage
 Section titled “Basic usage”
 Actions are defined in a `server` object exported from `src/actions/index.ts`:

 - src/actions/index.ts ` import { defineAction } from ' astro:actions ' ; import { z } from ' astro/zod ' ;
 export const server = { myAction: defineAction ( { /* ... */ } ) } `
 Your actions are available as functions from the `astro:actions` module. Import `actions` and call them client-side within a UI framework component , a form POST request , or by using a `&#x3C;script>` tag in an Astro component.

When you call an action, it returns an object with either `data` containing the JSON-serialized result, or `error` containing thrown errors.

 src/pages/index.astro ` --- ---
 &#x3C; script > import { actions } from ' astro:actions ' ;
 async () => { const { data , error } = await actions . myAction ( { /* ... */ } ); } &#x3C;/ script > `

### Write your first action
 Section titled “Write your first action”
 Follow these steps to define an action and call it in a `script` tag in your Astro page.

Create a `src/actions/index.ts` file and export a `server` object.

 src/actions/index.ts ` export const server = { // action declarations } `

-
 Import the `defineAction()` utility from `astro:actions`, and the `z` object from `astro/zod`.

 src/actions/index.ts ` import { defineAction } from ' astro:actions ' ; import { z } from ' astro/zod ' ;
 export const server = { // action declarations } `

-
 Use the `defineAction()` utility to define a `getGreeting` action. The `input` property will be used to validate input parameters with a Zod schema and the `handler()` function includes the backend logic to run on the server.

 src/actions/index.ts ` import { defineAction } from ' astro:actions ' ; import { z } from ' astro/zod ' ;
 export const server = { getGreeting: defineAction ( { input: z . object ( { name: z . string () , } ) , handler : async ( input ) => { return ` Hello, ${ input . name } ! ` } } ) } ` { return &#x60;Hello, ${input.name}!&#x60; } })}">

-
 Create an Astro component with a button that will fetch a greeting using your `getGreeting` action when clicked.

 src/pages/index.astro ` --- ---
 &#x3C; button > Get greeting &#x3C;/ button >
 &#x3C; script > const button = document . querySelector ( ' button ' ); button ?. addEventListener ( ' click ' , async () => { // Show alert pop-up with greeting from action }); &#x3C;/ script > ` Get greeting ">

-
 To use your action, import `actions` from `astro:actions` and then call `actions.getGreeting()` in the click handler. The `name` option will be sent to your action’s `handler()` on the server and, if there are no errors, the result will be available as the `data` property.

 src/pages/index.astro ` --- ---
 &#x3C; button > Get greeting &#x3C;/ button >
 &#x3C; script > import { actions } from ' astro:actions ' ;
 const button = document . querySelector ( ' button ' ); button ?. addEventListener ( ' click ' , async () => { // Show alert pop-up with greeting from action const { data , error } = await actions . getGreeting ( { name: " Houston " } ); if ( ! error ) alert ( data ); }) &#x3C;/ script > ` Get greeting ">

 See the full Actions API documentation for details on `defineAction()` and its properties.

## Organizing actions
 Section titled “Organizing actions”
 All actions in your project must be exported from the `server` object in the `src/actions/index.ts` file. You can define actions inline or you can move action definitions to separate files and import them. You can even group related functions in nested objects.

For example, to colocate all of your user actions, you can create a `src/actions/user.ts` file and nest the definitions of both `getUser` and `createUser` inside a single `user` object.

 src/actions/user.ts ` import { defineAction } from ' astro:actions ' ;
 export const user = { getUser: defineAction ( /* ... */ ) , createUser: defineAction ( /* ... */ ) , } `
 Then, you can import this `user` object into your `src/actions/index.ts` file and add it as a top-level key to the `server` object alongside any other actions:

 src/actions/index.ts ` import { user } from ' ./user ' ;
 export const server = { myAction: defineAction ( { /* ... */ } ) , user , } `
 Now, all of your user actions are callable from the `actions.user` object:

- `actions.user.getUser()`

- `actions.user.createUser()`

## Handling returned data
 Section titled “Handling returned data”
 Actions return an object containing either `data` with the type-safe return value of your `handler()`, or an `error` with any backend errors. Errors may come from validation errors on the `input` property or thrown errors within the `handler()`.

Actions return a custom data format that can handle Dates, Maps, Sets, and URLs using the Devalue library . Therefore, you can’t easily inspect the response from the network like you can with regular JSON. For debugging, you can instead inspect the `data` object returned by actions.

 See the `handler()` API reference for full details.

### Checking for errors
 Section titled “Checking for errors”
 It’s best to check if an `error` is present before using the `data` property. This allows you to handle errors in advance and ensures `data` is defined without an `undefined` check.

 ` const { data , error } = await actions . example ();
 if (error) { // handle error cases return ; } // use `data` `

### Accessing `data` directly without an error check
 Section titled “Accessing data directly without an error check”
 To skip error handling, for example while prototyping or using a library that will catch errors for you, use the `.orThrow()` property on your action call to throw errors instead of returning an `error`. This will return the action’s `data` directly.

This example calls a `likePost()` action that returns the updated number of likes as a `number` from the action `handler`:

 ` const updatedLikes = await actions . likePost . orThrow ( { postId: ' example ' } ); // ^ type: number `

### Handling backend errors in your action
 Section titled “Handling backend errors in your action”
 You can use the provided `ActionError` to throw an error from your action `handler()`, such as “not found” when a database entry is missing, or “unauthorized” when a user is not logged in. This has two main benefits over returning `undefined`:

-
You can set a status code like `404 - Not found` or `401 - Unauthorized`. This improves debugging errors in both development and in production by letting you see the status code of each request.

-
In your application code, all errors are passed to the `error` object on an action result. This avoids the need for `undefined` checks on data, and allows you to display targeted feedback to the user depending on what went wrong.

#### Creating an `ActionError`
 Section titled “Creating an ActionError”
 To throw an error, import the `ActionError()` class from the `astro:actions` module. Pass it a human-readable status `code` (e.g. `"NOT_FOUND"` or `"BAD_REQUEST"`), and an optional `message` to provide further information about the error.

This example throws an error from a `likePost` action when a user is not logged in, after checking a hypothetical “user-session” cookie for authentication:

 src/actions/index.ts ` import { defineAction, ActionError } from " astro:actions " ; import { z } from " astro/zod " ;
 export const server = { likePost: defineAction ( { input: z . object ( { postId: z . string () } ) , handler : async ( input , ctx ) => { if ( ! ctx . cookies . has ( ' user-session ' )) { throw new ActionError ( { code: " UNAUTHORIZED " , message: " User must be logged in. " , } ) ; } // Otherwise, like the post }, } ) , } ; ` { if (!ctx.cookies.has(&#x27;user-session&#x27;)) { throw new ActionError({ code: &#x22;UNAUTHORIZED&#x22;, message: &#x22;User must be logged in.&#x22;, }); } // Otherwise, like the post }, }),};">

#### Handling an `ActionError`
 Section titled “Handling an ActionError”
 To handle this error, you can call the action from your application and check whether an `error` property is present. This property will be of type `ActionError` and will contain your `code` and `message`.

In the following example, a `LikeButton.tsx` component calls the `likePost()` action when clicked. If an authentication error occurs, the `error.code` attribute is used to determine whether to display a login link:

 src/components/LikeButton.tsx ` import { actions } from ' astro:actions ' ; import { useState } from ' preact/hooks ' ;
 export function LikeButton ( { postId } : { postId : string } ) { const [ showLogin , setShowLogin ] = useState ( false ); return ( &#x3C;> { showLogin &#x26;&#x26; &#x3C; a href = " /signin " > Log in to like a post. &#x3C;/ a > } &#x3C; button onClick = { async () => { const { data , error } = await actions . likePost ( { postId } ) ; if (error ?. code === ' UNAUTHORIZED ' ) setShowLogin ( true ) ; // Early return for unexpected errors else if (error) return ; // update likes } } > Like &#x3C;/ button > &#x3C;/> ) } `  { showLogin &#x26;&#x26; Log in to like a post.  } { const { data, error } = await actions.likePost({ postId }); if (error?.code === &#x27;UNAUTHORIZED&#x27;) setShowLogin(true); // Early return for unexpected errors else if (error) return; // update likes }}> Like   )}">

### Handling client redirects
 Section titled “Handling client redirects”
 When calling actions from the client, you can integrate with a client-side library like `react-router`, or you can use Astro’s `navigate()` function to redirect to a new page when an action succeeds.

This example navigates to the homepage after a `logout` action returns successfully:

 src/pages/LogoutButton.tsx ` import { actions } from ' astro:actions ' ; import { navigate } from ' astro:transitions/client ' ;
 export function LogoutButton () { return ( &#x3C; button onClick = { async () => { const { error } = await actions . logout () ; if ( ! error) navigate ( ' / ' ) ; } } > Logout &#x3C;/ button > ); } ` { const { error } = await actions.logout(); if (!error) navigate(&#x27;/&#x27;); }}> Logout  );}">

## Accepting form data from an action
 Section titled “Accepting form data from an action”
 Actions accept JSON data by default. To accept form data from an HTML form, set `accept: 'form'` in your `defineAction()` call:

 src/actions/index.ts ` import { defineAction } from ' astro:actions ' ; import { z } from ' astro/zod ' ;
 export const server = { comment: defineAction ( { accept: ' form ' , input: z . object ( /* ... */ ) , handler : async ( input ) => { /* ... */ }, } ) } ` { /* ... */ }, })}">

### Using validators with form inputs
 Section titled “Using validators with form inputs”
 When your action is configured to accept form data , you can use any Zod validators to validate your fields (e.g. `z.coerce.date()` for date inputs). Extension functions including `.refine()`, `.transform()`, and `.pipe()` are also supported on the `z.object()` validator.

Additionally, Astro provides special handling under the hood for your convenience to validate the following types of field inputs:

- Inputs of type `number` can be validated using `z.number()`

- Inputs of type `checkbox` can be validated using `z.coerce.boolean()`

- Inputs of type `file` can be validated using `z.instanceof(File)`

- Multiple inputs of the same `name` can be validated using `z.array(/* validator */)`

- All other inputs can be validated using `z.string()`

When your form is submitted with empty inputs, the output type may not match your `input` validator. Empty values are converted to `null` except when validating arrays or booleans. For example, if an input of type `text` is submitted with an empty value, the result will be `null` instead of an empty string (`""`).

To apply a union of different validators, use the `z.discriminatedUnion()` wrapper to narrow the type based on a specific form field. This example accepts a form submission to either “create” or “update” a user, using the form field with the name `type` to determine which object to validate against:

 src/actions/index.ts ` import { defineAction } from ' astro:actions ' ; import { z } from ' astro/zod ' ;
 export const server = { changeUser: defineAction ( { accept: ' form ' , input: z . discriminatedUnion ( ' type ' , [ z . object ({ // Matches when the `type` field has the value ` create ` type: z . literal ( ' create ' ), name: z . string (), email: z . email (), }), z . object ({ // Matches when the `type` field has the value ` update ` type: z . literal ( ' update ' ), id: z . number (), name: z . string (), email: z . email (), }), ]) , async handler ( input ) { if (input . type === ' create ' ) { // input is { type: ' create ', name: string, email: string } } else { // input is { type: ' update ', id: number, name: string, email: string } } }, } ) , } ; `

### Validating form data
 Section titled “Validating form data”
 Actions will parse submitted form data to an object, using the value of each input’s `name` attribute as the object keys. For example, a form containing `&#x3C;input name="search">` will be parsed to an object like `{ search: 'user input' }`. Your action’s `input` schema will be used to validate this object.

To receive the raw `FormData` object in your action handler instead of a parsed object, omit the `input` property in your action definition.

The following example shows a validated newsletter registration form that accepts a user’s email and requires a “terms of service” agreement checkbox.

-
Create an HTML form component with unique `name` attributes on each input:

 src/components/Newsletter.astro ` &#x3C; form > &#x3C; label for = " email " > E-mail &#x3C;/ label > &#x3C; input id = " email " required type = " email " name = " email " /> &#x3C; label > &#x3C; input required type = " checkbox " name = " terms " > I agree to the terms of service &#x3C;/ label > &#x3C; button > Sign up &#x3C;/ button > &#x3C;/ form > `  E-mail     I agree to the terms of service  Sign up  ">

-
 Define a `newsletter` action to handle the submitted form. Validate the `email` field using the `z.email()` validator, and the `terms` checkbox using `z.boolean()`:

 src/actions/index.ts ` import { defineAction } from ' astro:actions ' ; import { z } from ' astro/zod ' ;
 export const server = { newsletter: defineAction ( { accept: ' form ' , input: z . object ( { email: z . email () , terms: z . boolean () , } ) , handler : async ( { email , terms } ) => { /* ... */ }, } ) } ` { /* ... */ }, })}">

 See the `input` API reference for all available form validators.

-
 Add a `&#x3C;script>` to the HTML form to submit the user input. This example overrides the form’s default submit behavior to call `actions.newsletter()`, and redirects to `/confirmation` using the `navigate()` function:

 src/components/Newsletter.astro ` &#x3C; form > 7 collapsed lines &#x3C; label for = " email " > E-mail &#x3C;/ label > &#x3C; input id = " email " required type = " email " name = " email " /> &#x3C; label > &#x3C; input required type = " checkbox " name = " terms " > I agree to the terms of service &#x3C;/ label > &#x3C; button > Sign up &#x3C;/ button > &#x3C;/ form >
 &#x3C; script > import { actions } from ' astro:actions ' ; import { navigate } from ' astro:transitions/client ' ;
 const form = document . querySelector ( ' form ' ); form ?. addEventListener ( ' submit ' , async ( event ) => { event . preventDefault (); const formData = new FormData ( form ); const { error } = await actions . newsletter ( formData ); if ( ! error ) navigate ( ' /confirmation ' ); }) &#x3C;/ script > `  E-mail     I agree to the terms of service  Sign up  ">

 See “Call actions from an HTML form action” for an alternative way to submit form data.

### Displaying form input errors
 Section titled “Displaying form input errors”
 You can validate form inputs before submission using native HTML form validation attributes like `required`, `type="email"`, and `pattern`. For more complex `input` validation on the backend, you can use the provided `isInputError()` utility function.

To retrieve input errors, use the `isInputError()` utility to check whether an error was caused by invalid input. Input errors contain a `fields` object with messages for each input name that failed to validate. You can use these messages to prompt your user to correct their submission.

The following example checks the error with `isInputError()`, then checks whether the error is in the email field, before finally creating a message from the errors. You can use JavaScript DOM manipulation or your preferred UI framework to display this message to users.

 ` import { actions, isInputError } from ' astro:actions ' ;
 const form = document . querySelector ( ' form ' ); const formData = new FormData ( form ); const { error } = await actions . newsletter ( formData ); if ( isInputError ( error )) { // Handle input errors. if ( error . fields . email ) { const message = error . fields . email . join ( ' , ' ); } } `

## Call actions from an HTML form action
 Section titled “Call actions from an HTML form action”

 You can enable zero-JS form submissions with standard attributes on any `&#x3C;form>` element. Form submissions without client-side JavaScript may be useful both as a fallback for when JavaScript fails to load, or if you prefer to handle forms entirely from the server.

Calling Astro.getActionResult() on the server returns the result of your form submission (`data` or `error`), and can be used to dynamically redirect, handle form errors, update the UI, and more.

To call an action from an HTML form, add `method="POST"` to your `&#x3C;form>`, then set the form’s `action` attribute using your action, for example `action={actions.logout}`. This will set the `action` attribute to use a query string that is handled by the server automatically.

For example, this Astro component calls the `logout` action when the button is clicked and reloads the current page:

 src/components/LogoutButton.astro ` --- import { actions } from ' astro:actions ' ; ---
 &#x3C; form method = " POST " action = { actions . logout } > &#x3C; button > Log out &#x3C;/ button > &#x3C;/ form > `  Log out  ">
 Additional attributes on the `&#x3C;form>` element may be necessary for proper schema validation with Zod. For example, to include file uploads, add `enctype="multipart/form-data"` to ensure that files are sent in a format correctly recognized by `z.instanceof(File)`:

 src/components/FileUploadForm.astro ` --- import { actions } from ' astro:actions ' ; --- &#x3C; form method = " POST " action = { actions . upload } enctype = " multipart/form-data " > &#x3C; label for = " file " > Upload File &#x3C;/ label > &#x3C; input type = " file " id = " file " name = " file " /> &#x3C; button type = " submit " > Submit &#x3C;/ button > &#x3C;/ form > `  Upload File   Submit  ">

### Redirect on action success
 Section titled “Redirect on action success”
 If you need to redirect to a new route on success, you can use an action’s result on the server. A common example is creating a product record and redirecting to the new product’s page, e.g. `/products/[id]`.

For example, say you have a `createProduct` action that returns the generated product id:

 src/actions/index.ts ` import { defineAction } from ' astro:actions ' ; import { z } from ' astro/zod ' ;
 export const server = { createProduct: defineAction ( { accept: ' form ' , input: z . object ( { /* ... */ } ) , handler : async ( input ) => { const product = await persistToDatabase (input) ; return { id: product . id }; }, } ) } ` { const product = await persistToDatabase(input); return { id: product.id }; }, })}">
 You can retrieve the action result from your Astro component by calling `Astro.getActionResult()`. This returns an object containing `data` or `error` properties when an action is called, or `undefined` if the action was not called during this request.

Use the `data` property to construct a URL to use with `Astro.redirect()`:

 src/pages/products/create.astro ` --- import { actions } from ' astro:actions ' ;
 const result = Astro . getActionResult (actions . createProduct ); if (result &#x26;&#x26; ! result . error ) { return Astro . redirect ( ` /products/ ${ result . data . id } ` ); } ---
 &#x3C; form method = " POST " action = { actions . createProduct } > &#x3C;!--...--> &#x3C;/ form > `   ">

### Handle form action errors
 Section titled “Handle form action errors”
 Calling `Astro.getActionResult()` in the Astro component containing your form gives you access to the `data` and `error` objects for custom error handling.

The following example displays a general failure message when a `newsletter` action fails:

 src/pages/index.astro ` --- import { actions } from ' astro:actions ' ;
 const result = Astro . getActionResult (actions . newsletter ); ---
 { result ?. error &#x26;&#x26; ( &#x3C; p class = " error " > Unable to sign up. Please try again later. &#x3C;/ p > ) } &#x3C; form method = " POST " action = { actions . newsletter } > &#x3C; label > E-mail &#x3C; input required type = " email " name = " email " /> &#x3C;/ label > &#x3C; button > Sign up &#x3C;/ button > &#x3C;/ form > ` Unable to sign up. Please try again later.
)}   E-mail   Sign up  ">
For more customization, you can use the `isInputError()` utility to check whether an error is caused by invalid input.

The following example renders an error banner under the `email` input field when an invalid email is submitted:

 src/pages/index.astro ` --- import { actions, isInputError } from ' astro:actions ' ;
 const result = Astro . getActionResult (actions . newsletter ); const inputErrors = isInputError (result ?. error ) ? result . error . fields : {} ; ---
 &#x3C; form method = " POST " action = { actions . newsletter } > &#x3C; label > E-mail &#x3C; input required type = " email " name = " email " aria-describedby = " error " /> &#x3C;/ label > { inputErrors . email &#x26;&#x26; &#x3C; p id = " error " > { inputErrors . email . join ( ' , ' ) } &#x3C;/ p > } &#x3C; button > Sign up &#x3C;/ button > &#x3C;/ form > `   E-mail   {inputErrors.email &#x26;&#x26; {inputErrors.email.join(&#x27;,&#x27;)}
} Sign up  ">

#### Preserve input values on error
 Section titled “Preserve input values on error”
 Inputs will be cleared whenever a form is submitted. To persist input values, you can enable view transitions and apply the `transition:persist` directive to each input:

 ` &#x3C; input transition:persist required type = " email " name = " email " /> ` ">

### Update the UI with a form action result
 Section titled “Update the UI with a form action result”
 To use an action’s return value to display a notification to the user on success, pass the action to `Astro.getActionResult()`. Use the returned `data` property to render the UI you want to display.

This example uses the `productName` property returned by an `addToCart` action to show a success message.

 src/pages/products/[slug].astro ` --- import { actions } from ' astro:actions ' ;
 const result = Astro . getActionResult (actions . addToCart ); ---
 { result &#x26;&#x26; ! result . error &#x26;&#x26; ( &#x3C; p class = " success " > Added { result . data . productName } to cart &#x3C;/ p > ) }
 &#x3C;!--...--> ` Added {result.data.productName} to cart
)}">

### Advanced: Persist action results with a session
 Section titled “Advanced: Persist action results with a session”

 Added in:
 `astro@5.0.0`

Action results are displayed as a POST submission. This means that the result will be reset to `undefined` when a user closes and revisits the page. The user will also see a “confirm form resubmission?” dialog if they attempt to refresh the page.

To customize this behavior, you can add middleware to handle the result of the action manually. You may choose to persist the action result using a cookie or session storage.

Start by creating a middleware file and importing the `getActionContext()` utility from `astro:actions`. This function returns an `action` object with information about the incoming action request, including the action handler and whether the action was called from an HTML form. `getActionContext()` also returns the `setActionResult()` and `serializeActionResult()` functions to programmatically set the value returned by `Astro.getActionResult()`:

 src/middleware.ts ` import { defineMiddleware } from ' astro:middleware ' ; import { getActionContext } from ' astro:actions ' ;
 export const onRequest = defineMiddleware ( async ( context , next ) => { const { action , setActionResult , serializeActionResult } = getActionContext (context) ; if (action ?. calledFrom === ' form ' ) { const result = await action . handler () ; // ... handle the action result setActionResult (action . name , serializeActionResult (result)) ; } return next () ; } ); ` { const { action, setActionResult, serializeActionResult } = getActionContext(context); if (action?.calledFrom === &#x27;form&#x27;) { const result = await action.handler(); // ... handle the action result setActionResult(action.name, serializeActionResult(result)); } return next();});">
 A common practice to persist HTML form results is the POST / Redirect / GET pattern . This redirect removes the “confirm form resubmission?” dialog when the page is refreshed, and allows action results to be persisted throughout the user’s session.

This example applies the POST / Redirect / GET pattern to all form submissions using session storage with the Netlify server adapter installed. Action results are written to a session store using Netlify Blob , and retrieved after a redirect using a session ID:

 src/middleware.ts ` import { defineMiddleware } from ' astro:middleware ' ; import { getActionContext } from ' astro:actions ' ; import { randomUUID } from " node:crypto " ; import { getStore } from " @netlify/blobs " ;
 export const onRequest = defineMiddleware ( async ( context , next ) => { // Skip requests for prerendered pages if (context . isPrerendered ) return next () ;
 const { action , setActionResult , serializeActionResult } = getActionContext (context) ; // Create a Blob store to persist action results with Netlify Blob const actionStore = getStore ( " action-session " ) ;
 // If an action result was forwarded as a cookie, set the result // to be accessible from `Astro.getActionResult()` const sessionId = context . cookies . get ( " action-session-id " ) ?. value ; const session = sessionId ? await actionStore . get (sessionId , { type: " json " , } ) : undefined ;
 if (session) { setActionResult (session . actionName , session . actionResult ) ;
 // Optional: delete the session after the page is rendered. // Feel free to implement your own persistence strategy await actionStore . delete (sessionId) ; context . cookies . delete ( " action-session-id " ) ; return next () ; }
 // If an action was called from an HTML form action, // call the action handler and redirect to the destination page if (action ?. calledFrom === " form " ) { const actionResult = await action . handler () ;
 // Persist the action result using session storage const sessionId = randomUUID () ; await actionStore . setJSON (sessionId , { actionName: action . name , actionResult: serializeActionResult (actionResult) , } ) ;
 // Pass the session ID as a cookie // to be retrieved after redirecting to the page context . cookies . set ( " action-session-id " , sessionId) ;
 // Redirect back to the previous page on error if (actionResult . error ) { const referer = context . request . headers . get ( " Referer " ) ; if ( ! referer) { throw new Error ( " Internal: Referer unexpectedly missing from Action POST request. " , ) ; } return context . redirect (referer) ; } // Redirect to the destination page on success return context . redirect (context . originPathname ) ; }
 return next () ; } ); ` { // Skip requests for prerendered pages if (context.isPrerendered) return next(); const { action, setActionResult, serializeActionResult } = getActionContext(context); // Create a Blob store to persist action results with Netlify Blob const actionStore = getStore(&#x22;action-session&#x22;); // If an action result was forwarded as a cookie, set the result // to be accessible from &#x60;Astro.getActionResult()&#x60; const sessionId = context.cookies.get(&#x22;action-session-id&#x22;)?.value; const session = sessionId ? await actionStore.get(sessionId, { type: &#x22;json&#x22;, }) : undefined; if (session) { setActionResult(session.actionName, session.actionResult); // Optional: delete the session after the page is rendered. // Feel free to implement your own persistence strategy await actionStore.delete(sessionId); context.cookies.delete(&#x22;action-session-id&#x22;); return next(); } // If an action was called from an HTML form action, // call the action handler and redirect to the destination page if (action?.calledFrom === &#x22;form&#x22;) { const actionResult = await action.handler(); // Persist the action result using session storage const sessionId = randomUUID(); await actionStore.setJSON(sessionId, { actionName: action.name, actionResult: serializeActionResult(actionResult), }); // Pass the session ID as a cookie // to be retrieved after redirecting to the page context.cookies.set(&#x22;action-session-id&#x22;, sessionId); // Redirect back to the previous page on error if (actionResult.error) { const referer = context.request.headers.get(&#x22;Referer&#x22;); if (!referer) { throw new Error( &#x22;Internal: Referer unexpectedly missing from Action POST request.&#x22;, ); } return context.redirect(referer); } // Redirect to the destination page on success return context.redirect(context.originPathname); } return next();});">

## Security when using actions
 Section titled “Security when using actions”
 Actions are accessible as public endpoints based on the name of the action. For example, the action `blog.like()` will be accessible from `/_actions/blog.like`. This is useful for unit testing action results and debugging production errors. However, this means you must use same authorization checks that you would consider for API endpoints and on-demand rendered pages.

### Authorize users from an action handler
 Section titled “Authorize users from an action handler”
 To authorize action requests, add an authentication check to your action handler. You may want to use an authentication library to handle session management and user information.

Actions expose a subset of the `APIContext` object to access properties passed from middleware using `context.locals`. When a user is not authorized, you can raise an `ActionError` with the `UNAUTHORIZED` code:

 src/actions/index.ts ` import { defineAction, ActionError } from ' astro:actions ' ;
 export const server = { getUserSettings: defineAction ( { handler : async ( _input , context ) => { if ( ! context . locals . user ) { throw new ActionError ( { code: ' UNAUTHORIZED ' } ) ; } return { /* data on success */ }; } } ) } ` { if (!context.locals.user) { throw new ActionError({ code: &#x27;UNAUTHORIZED&#x27; }); } return { /* data on success */ }; } })}">

### Gate actions from middleware
 Section titled “Gate actions from middleware”

 Added in:
 `astro@5.0.0`

Astro recommends authorizing user sessions from your action handler to respect permission levels and rate-limiting on a per-action basis. However, you can also gate requests to all actions (or a subset of actions) from middleware.

Use the `getActionContext()` function from your middleware to retrieve information about any inbound action requests. This includes the action name and whether that action was called using a client-side remote procedure call (RPC) function (e.g. `actions.blog.like()`) or an HTML form.

The following example rejects all action requests that do not have a valid session token. If the check fails, a “Forbidden” response is returned. Note: this method ensures that actions are only accessible when a session is present, but is not a substitute for secure authorization.

 src/middleware.ts ` import { defineMiddleware } from ' astro:middleware ' ; import { getActionContext } from ' astro:actions ' ;
 export const onRequest = defineMiddleware ( async ( context , next ) => { const { action } = getActionContext (context) ; // Check if the action was called from a client-side function if (action ?. calledFrom === ' rpc ' ) { // If so, check for a user session token if ( ! context . cookies . has ( ' user-session ' )) { return new Response ( ' Forbidden ' , { status: 403 } ) ; } }
 context . cookies . set ( ' user-session ' , /* session token */ ) ; return next () ; } ); ` { const { action } = getActionContext(context); // Check if the action was called from a client-side function if (action?.calledFrom === &#x27;rpc&#x27;) { // If so, check for a user session token if (!context.cookies.has(&#x27;user-session&#x27;)) { return new Response(&#x27;Forbidden&#x27;, { status: 403 }); } } context.cookies.set(&#x27;user-session&#x27;, /* session token */); return next();});">

## Call actions from Astro components and server endpoints
 Section titled “Call actions from Astro components and server endpoints”
 You can call actions directly from Astro component scripts using the `Astro.callAction()` wrapper (or `context.callAction()` when using a server endpoint ). This is common to reuse logic from your actions in other server code.

Pass the action as the first argument and any input parameters as the second argument. This returns the same `data` and `error` objects you receive when calling actions on the client:

 src/pages/products.astro
```
` --- import { actions } from ' astro:actions ' ;
 const searchQuery = Astro . url . searchParams . get ( ' search ' ); if (searchQuery) { const { data , error } = await Astro . callAction (actions . findProduct , { query: searchQuery } ); // handle result } --- `
```

 Learn

 Contribute

 Community

 Sponsor

## Sessions

# Sessions

 Added in:
 `astro@5.7.0`

Sessions are used to share data between requests for on-demand rendered pages .

Unlike `cookies` , sessions are stored on the server, so you can store larger amounts of data without worrying about size limits or security issues. They are useful for storing things like user data, shopping carts, and form state, and they work without any client-side JavaScript:

 - src/components/CartButton.astro ` --- export const prerender = false ; // Not needed with 'server' output const cart = await Astro . session ?. get ( ' cart ' ); ---
 &#x3C; a href = " /checkout " > 🛒 { cart ?. length ?? 0 } items &#x3C;/ a > ` 🛒 {cart?.length ?? 0} items ">

## Configuring sessions
 Section titled “Configuring sessions”
 Sessions require a storage driver to store the session data. The Node , Cloudflare , and Netlify adapters automatically configure a default driver for you, but other adapters currently require you to specify a driver manually .

 astro.config.mjs ` import { defineConfig, sessionDrivers } from ' astro/config ' import vercel from ' @astrojs/vercel '
 export default defineConfig ({ adapter: vercel () session : { driver: sessionDrivers . lruCache ({ max: 800 , }), } }) `

 See the `session` configuration option for more details on setting a storage driver, and other configurable options.

### Overriding the configuration at runtime
 Section titled “Overriding the configuration at runtime”
 By default, session drivers are configured at build time, and any environment variables used will be inlined into the build. This means you cannot override the configuration at runtime.

When you need a different configuration (e.g. to connect to an external service), define it in a separate file. Then use that file as the driver’s entrypoint .

The following example takes advantage of Unstorage compatibility to configure the Redis driver in its own entrypoint:

Install the `unstorage` package :

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install unstorage `

 Terminal window
```
` pnpm add unstorage `
```

 Terminal window
```
` yarn add unstorage `
```

-
 Create a file for the driver configuration (e.g. `src/session-driver.ts`) and export a default function that returns the driver instance:

 src/session-driver.ts ` import type { SessionDriver } from " astro " ; import redisDriver from " unstorage/drivers/redis " ; import { REDIS_HOST, REDIS_PORT } from " astro:env " ;
 export default function () : SessionDriver { return redisDriver ({ host: REDIS_HOST , port: REDIS_PORT , }); } `

-
 Use this file as the driver’s entrypoint in your Astro configuration:

 astro.config.mjs ` import { defineConfig, envField, sessionDrivers } from " astro/config " ; import vercel from " @astrojs/vercel " ;
 export default defineConfig ({ adapter: vercel (), env: { REDIS_HOST: envField . string ({ context: " server " , access: " public " , default: " localhost " }), REDIS_PORT: envField . number ({ context: " server " , access: " public " , default: 6379 }), }, session: { driver: { entrypoint: new URL ( ' ./src/session-driver.ts ' , import. meta . url ), } } }); `

## Interacting with session data
 Section titled “Interacting with session data”
 The `session` object allows you to interact with the stored user state (e.g. adding items to a shopping cart) and the session ID (e.g. deleting the session ID cookie when logging out). The object is accessible as `Astro.session` in your Astro components and pages and as `context.session` object in API endpoints, middleware, and actions.

The session is generated automatically when it is first used and can be regenerated at any time with `session.regenerate()` or destroyed with `session.destroy()` .

For many use cases, you will only need to use `session.get()` and `session.set()` .

 See the Sessions API reference for more details.

### Astro components and pages
 Section titled “Astro components and pages”
 In `.astro` components and pages, you can access the session object via the global `Astro` object. For example, to display the number of items in a shopping cart:

 src/components/CartButton.astro ` --- export const prerender = false ; // Not needed with 'server' output const cart = await Astro . session ?. get ( ' cart ' ); ---
 &#x3C; a href = " /checkout " > 🛒 { cart ?. length ?? 0 } items &#x3C;/ a > ` 🛒 {cart?.length ?? 0} items ">

### API endpoints
 Section titled “API endpoints”
 In API endpoints, the session object is available on the `context` object. For example, to add an item to a shopping cart:

 src/pages/api/addToCart.ts ` export async function POST ( context : APIContext ) { const cart = await context . session ?. get ( ' cart ' ) || []; const data = await context . request . json &#x3C;{ item : string }> (); if ( ! data ?. item ) { return new Response ( ' Item is required ' , { status: 400 }); } cart . push (data . item ); await context . session ?. set ( ' cart ' , cart); return Response . json (cart); } ` (); if(!data?.item) { return new Response(&#x27;Item is required&#x27;, { status: 400 }); } cart.push(data.item); await context.session?.set(&#x27;cart&#x27;, cart); return Response.json(cart);}">

### Actions
 Section titled “Actions”
 In actions, the session object is available on the `context` object. For example, to add an item to a shopping cart:

 src/actions/addToCart.ts ` import { defineAction } from ' astro:actions ' ; import { z } from ' astro/zod ' ;
 export const server = { addToCart: defineAction ( { input: z . object ( { productId: z . string () } ) , handler : async ( input , context ) => { const cart = await context . session ?. get ( ' cart ' ) ; cart . push (input . productId ) ; await context . session ?. set ( ' cart ' , cart) ; return cart ; }, } ) , } ; ` { const cart = await context.session?.get(&#x27;cart&#x27;); cart.push(input.productId); await context.session?.set(&#x27;cart&#x27;, cart); return cart; }, }),};">

### Middleware
 Section titled “Middleware”

 In middleware, the session object is available on the `context` object. For example, to set the last visit time in the session:

 src/middleware.ts ` import { defineMiddleware } from ' astro:middleware ' ;
 export const onRequest = defineMiddleware ( async ( context , next ) => { context . session ?. set ( ' lastVisit ' , new Date ()) ; return next () ; } ); ` { context.session?.set(&#x27;lastVisit&#x27;, new Date()); return next();});">

## Session data types
 Section titled “Session data types”
 By default session data is untyped, and you can store arbitrary data in any key. Values are serialized and deserialized using devalue , which is the same library used in content collections and actions. This means that supported types are the same, and include strings, numbers, `Date`, `Map`, `Set`, `URL`, arrays, and plain objects.

You can optionally define TypeScript types for your session data by creating a `src/env.d.ts` file and adding a declaration for the `App.SessionData` type:

 src/env.d.ts ` declare namespace App { interface SessionData { user : { id : string ; name : string ; }; cart : string []; } } `
 This will allow you to access the session data with type-checking and auto-completion in your editor:

 src/components/CartButton.astro
```
` -- - const cart = await Astro . session ?. get ( ' cart ' ); // const cart: string[] | undefined
 const something = await Astro . session ?. get ( ' something ' ); // const something: any
 Astro . session ?. set ( ' user ' , { id: 1 , name: ' Houston ' }); // Error: Argument of type '{ id: number; name: string }' is not assignable to parameter of type '{ id: string; name: string; }'. -- - `
```

 Learn

 Contribute

 Community

 Sponsor