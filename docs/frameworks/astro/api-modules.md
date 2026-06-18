# Astro - API Modules


## Astro Actions

# Actions API Reference

 Added in:
 `astro@4.15.0`

Actions help you build a type-safe backend you can call from client code and HTML forms. All utilities to define and call actions are exposed by the `astro:actions` module. For examples and usage instructions, see the Actions guide .

## Imports from `astro:actions`
 Section titled “Imports from astro:actions”
 -
```
` import { ACTION_QUERY_PARAMS, ActionError, actions, defineAction, getActionContext, getActionPath, isActionError, isInputError, } from ' astro:actions ' ; `
```

### `defineAction()`
 Section titled “defineAction()”
 Type: `({ accept, input, handler }) => ActionClient `

A utility to define new actions in the `src/actions/index.ts` file. This accepts a `handler()` function containing the server logic to run, and an optional `input` property to validate input parameters at runtime.

 src/actions/index.ts ` import { defineAction } from ' astro:actions ' ; import { z } from ' astro/zod ' ;
 export const server = { getGreeting: defineAction ( { input: z . object ( { name: z . string () , } ) , handler : async ( input , context ) => { return ` Hello, ${ input . name } ! ` } } ) } ` { return &#x60;Hello, ${input.name}!&#x60; } })}">

#### `handler()` property
 Section titled “handler() property”
 Type: `(input: TInputSchema, context: ActionAPIContext ) => TOutput | Promise<TOutput>`

A required function containing the server logic to run when the action is called. Data returned from the `handler()` is automatically serialized and sent to the caller.

The `handler()` is called with user input as its first argument. If an `input` validator is set, the user input will be validated before being passed to the handler. The second argument is a subset of Astro’s `context` object .

Return values are parsed using the devalue library . This supports JSON values and instances of `Date()`, `Map()`, `Set()`, and `URL()`.

#### `input` validator
 Section titled “input validator”
 Type: `ZodType | undefined`

An optional property that accepts a Zod validator (e.g. Zod object, Zod discriminated union) to validate handler inputs at runtime. If the action fails to validate, a `BAD_REQUEST` error is returned and the `handler` is not called.

If `input` is omitted, the `handler` will receive an input of type `unknown` for JSON requests and type `FormData` for form requests.

#### `accept` property
 Section titled “accept property”
 Type: `"form" | "json"`
 Default: `json`

Defines the format expected by an action:

 Use `form` when your action accepts `FormData`.

- Use `json`, the default, for all other cases.

When your action accepts form inputs, the `z.object()` validator will automatically parse `FormData` to a typed object. All Zod validators are supported to validate your inputs.

 Learn about using validators with form inputs in the Actions guide, including example usage and special input handling.

### `actions`
 Section titled “actions”
 Type: `Record<string, ActionClient >`

An object containing all your actions with the action name as key associated to a function to call this action.

 src/pages/index.astro ` --- ---
 &#x3C; script > import { actions } from ' astro:actions ' ;
 async () => { const { data , error } = await actions . myAction ( { /* ... */ } ); } &#x3C;/ script > `
 In order for Astro to recognize this property, you may need to restart the dev server or run the `astro sync` command (`s + enter`).

### `isInputError()`
 Section titled “isInputError()”
 Type: `(error?: unknown) => boolean`

A utility used to check whether an `ActionError` is an input validation error. When the `input` validator is a `z.object()`, input errors include a `fields` object with error messages grouped by name.

 See the form input errors guide for more on using `isInputError()`.

### `isActionError()`
 Section titled “isActionError()”
 Type: `(error?: unknown) => boolean`

A utility to check whether your action raised an `ActionError` within the handler property . This is useful when narrowing the type of a generic error.

 src/pages/index.astro ` --- ---
 &#x3C; script > import { isActionError , actions } from ' astro:actions ' ;
 async () => { const { data , error } = await actions . myAction ( { /* ... */ } ); if ( isActionError ( error )) { // Handle action-specific errors console . log ( error . code ); } } &#x3C;/ script > `

### `ActionError`
 Section titled “ActionError”
 The `ActionError()` constructor is used to create errors thrown by an action `handler`. This accepts a `code` property describing the error that occurred (example: `"UNAUTHORIZED"`), and an optional `message` property with further details.

The following example creates a new `ActionError` when the user is not logged in:

 src/actions/index.ts ` import { defineAction, ActionError } from " astro:actions " ;
 export const server = { getUserOrThrow: defineAction ( { accept: ' form ' , handler : async ( _ , { locals } ) => { if (locals . user ?. name !== ' florian ' ) { throw new ActionError ( { code: ' UNAUTHORIZED ' , message: ' Not logged in ' , } ) ; } return locals . user ; }, } ) , } ` { if (locals.user?.name !== &#x27;florian&#x27;) { throw new ActionError({ code: &#x27;UNAUTHORIZED&#x27;, message: &#x27;Not logged in&#x27;, }); } return locals.user; }, }),}">
 You can also use `ActionError` to narrow the error type when handling the results of an action:

 src/pages/index.astro ` --- ---
 &#x3C; script > import { ActionError , actions } from ' astro:actions ' ;
 async () => { const { data , error } = await actions . myAction ( { /* ... */ } ); if ( error instanceof ActionError ) { // Handle action-specific errors console . log ( error . code ); } } &#x3C;/ script > `

#### `code`
 Section titled “code”
 Type: ` ActionErrorCode `

Defines a human-readable version of an HTTP status code .

#### `message`
 Section titled “message”
 Type: `string`

An optional property to describe the error (e.g. “User must be logged in.”).

#### `stack`
 Section titled “stack”
 Type: `string`

An optional property to pass the stack trace.

### `getActionContext()`
 Section titled “getActionContext()”
 Type: `(context: APIContext ) => AstroActionContext`

 Added in:
 `astro@5.0.0`

A function called from your middleware handler to retrieve information about inbound action requests. This returns an `action` object with information about the request, a `deserializeActionResult()` method, and the `setActionResult()` and `serializeActionResult()` functions to programmatically set the value returned by `Astro.getActionResult()`.

`getActionContext()` lets you programmatically get and set action results using middleware, allowing you to persist action results from HTML forms, gate action requests with added security checks, and more.

 src/middleware.ts ` import { defineMiddleware } from ' astro:middleware ' ; import { getActionContext } from ' astro:actions ' ;
 export const onRequest = defineMiddleware ( async ( context , next ) => { const { action , setActionResult , serializeActionResult } = getActionContext (context) ; if (action ?. calledFrom === ' form ' ) { const result = await action . handler () ; setActionResult (action . name , serializeActionResult (result)) ; } return next () ; } ); ` { const { action, setActionResult, serializeActionResult } = getActionContext(context); if (action?.calledFrom === &#x27;form&#x27;) { const result = await action.handler(); setActionResult(action.name, serializeActionResult(result)); } return next();});">

#### `action`
 Section titled “action”
 Type: `{ calledFrom: “rpc” | “form”; name: string; handler: () => Promise< SafeResult >; } | undefined`

An object containing information about an inbound action request. It is available from `getActionContext()` , and provides the action `name`, `handler`, and whether the action was called from a client-side RPC function (e.g. `actions.newsletter()`) or an HTML form action.

 src/middleware.ts ` import { defineMiddleware } from ' astro:middleware ' ; import { getActionContext } from ' astro:actions ' ;
 export const onRequest = defineMiddleware ( async ( context , next ) => { const { action , setActionResult , serializeActionResult } = getActionContext (context) ; if (action ?. calledFrom === ' rpc ' &#x26;&#x26; action . name . startsWith ( ' private ' )) { // Check for a valid session token } // ... } ); ` { const { action, setActionResult, serializeActionResult } = getActionContext(context); if (action?.calledFrom === &#x27;rpc&#x27; &#x26;&#x26; action.name.startsWith(&#x27;private&#x27;)) { // Check for a valid session token } // ...});">
 `action.calledFrom` Section titled “action.calledFrom”
 Type: `"rpc" | "form"`

Whether an action was called using an RPC function or an HTML form action.

 `action.name` Section titled “action.name”
 Type: `string`

The name of the action. Useful to track the source of an action result during a redirect.

 `action.handler()` Section titled “action.handler()”
 Type: `() => Promise< SafeResult >`

A method to programmatically call an action to get the result.

#### `setActionResult()`
 Section titled “setActionResult()”
 Type: `(actionName: string, actionResult: SerializedActionResult) => void`

A function to programmatically set the value returned by `Astro.getActionResult()` in middleware. It is passed the action name and an action result serialized by `serializeActionResult()` . Calling this function from middleware will disable Astro’s own action result handling.

This is useful when calling actions from an HTML form to persist and load results from a session.

 src/middleware.ts ` import { defineMiddleware } from ' astro:middleware ' ; import { getActionContext } from ' astro:actions ' ; export const onRequest = defineMiddleware ( async ( context , next ) => { const { action , setActionResult , serializeActionResult } = getActionContext (context) ; if (action ?. calledFrom === ' form ' ) { const result = await action . handler () ; // ... handle the action result setActionResult (action . name , serializeActionResult (result)) ; } return next () ; } ); ` { const { action, setActionResult, serializeActionResult } = getActionContext(context); if (action?.calledFrom === &#x27;form&#x27;) { const result = await action.handler(); // ... handle the action result setActionResult(action.name, serializeActionResult(result)); } return next();});">

 See the advanced sessions guide for a sample implementation using Netlify Blob.

#### `serializeActionResult()`
 Section titled “serializeActionResult()”
 Type: `(res: SafeResult ) => SerializedActionResult`

Serializes an action result to JSON for persistence. This is required to properly handle non-JSON return values like `Map` or `Date` as well as the `ActionError` object.

Call this function when serializing an action result to be passed to `setActionResult()`:

 src/middleware.ts ` import { defineMiddleware } from ' astro:middleware ' ; import { getActionContext } from ' astro:actions ' ;
 export const onRequest = defineMiddleware ( async ( context , next ) => { const { action , setActionResult , serializeActionResult } = getActionContext (context) ; if (action) { const result = await action . handler () ; setActionResult (action . name , serializeActionResult (result)) ; } // ... } ); ` { const { action, setActionResult, serializeActionResult } = getActionContext(context); if (action) { const result = await action.handler(); setActionResult(action.name, serializeActionResult(result)); } // ...});">

#### `deserializeActionResult()`
 Section titled “deserializeActionResult()”
 Type: `(res: SerializedActionResult) => SafeResult `

Reverses the effect of `serializeActionResult()` and returns an action result to its original state. This is useful to access the `data` and `error` objects on a serialized action result.

### `getActionPath()`
 Section titled “getActionPath()”
 Type: `(action: ActionClient ) => string`

 Added in:
 `astro@5.1.0`

A utility that accepts an action and returns a URL path so you can execute an action call as a `fetch()` operation directly. This allows you to provide details such as custom headers when you call your action. Then, you can handle the custom-formatted returned data as needed, just as if you had called an action directly.

This example shows how to call a defined `like` action passing the `Authorization` header and the `keepalive` option:

 src/components/my-component.astro ` &#x3C; script > import { actions, getActionPath } from ' astro:actions '
 await fetch ( getActionPath ( actions . like ), { method: ' POST ' , headers: { ' Content-Type ' : ' application/json ' , Authorization: ' Bearer YOUR_TOKEN ' }, body: JSON . stringify ({ id: ' YOUR_ID ' }), keepalive: true }) &#x3C;/ script > `
 This example shows how to call the same `like` action using the `sendBeacon` API:

 src/components/my-component.astro ` &#x3C; script > import { actions, getActionPath } from ' astro:actions '
 navigator . sendBeacon ( getActionPath ( actions . like ), new Blob ([ JSON . stringify ({ id: ' YOUR_ID ' })], { type: ' application/json ' }) ) &#x3C;/ script > `

### `ACTION_QUERY_PARAMS`
 Section titled “ACTION_QUERY_PARAMS”
 Type: `{ actionName: string, actionPayload: string }`

An object containing the query parameter names used internally by Astro when handling form action submissions.

When you submit a form using an action, the following query parameters are added to the URL to track the action call:

- `actionName` - The query parameter that contains the name of the action being called

- `actionPayload` - The query parameter that contains the serialized form data

This constant can be useful when you need to clean up URLs after a form submission. For example, you might want to remove action-related query parameters during a redirect:

 src/pages/api/contact.ts ` import type { APIRoute } from " astro " ; import { ACTION_QUERY_PARAMS } from ' astro:actions '
 export const GET : APIRoute = ( { params , request } ) => { const link = request . url . searchParams ; link . delete ( ACTION_QUERY_PARAMS . actionName ) ; link . delete ( ACTION_QUERY_PARAMS . actionPayload ) ;
 return redirect (link , 303 ) ; } ; ` { const link = request.url.searchParams; link.delete(ACTION_QUERY_PARAMS.actionName); link.delete(ACTION_QUERY_PARAMS.actionPayload); return redirect(link, 303);};">

## `astro:actions` types
 Section titled “astro:actions types”

```
` import type { ActionAPIContext, ActionClient, ActionErrorCode, ActionInputSchema, ActionReturnType, SafeResult, } from ' astro:actions ' ; `
```

### `ActionAPIContext`
 Section titled “ActionAPIContext”
 A subset of the Astro context object . The following properties are not available: `callAction`, `getActionResult`, `props`, and `redirect`.

### `ActionClient`
 Section titled “ActionClient”
 Types:

-
`(input?: any) => Promise< SafeResult >`

- `{ queryString?: string; orThrow: (input?: any) => Promise&#x3C;Awaited&#x3C;TOutput>>; }`

Represents an action to be called on the client. You can use it as a function that accepts input data and returns a Promise with a `SafeResult` object containing the action result or validation errors.

The following example shows how you can provide error handling with an `if` statement when incrementing the like count fails:

 src/pages/posts/post-1.astro ` --- ---
 &#x3C;!-- your template -->
 &#x3C; script > import { actions } from ' astro:actions ' ;
 const post = document . querySelector ( ' article ' ); const button = document . querySelector ( ' button ' ); button ?. addEventListener ( ' click ' , async () => { const { data : updatedLikes , error } = await actions . likePost ( { postId: post ?. id } ); if ( error ) { /* handle error s */ } }) &#x3C;/ script > `
 Alternatively, you can use it as an object giving you access to the `queryString` and an alternative `orThrow()` method.

#### `ActionClient.queryString`
 Section titled “ActionClient.queryString”
 Type: `string`

A string representation of the action that can be used to construct form action URLs. This can be useful when your form component is used in multiple places but you need to redirect to a different URL on submit.

The following example uses `queryString` to construct a URL that will be passed to the form `action` attribute through a custom prop:

 src/pages/postal-service.astro ` --- import { actions } from ' astro:actions ' ; import FeedbackForm from " ../components/FeedbackForm.astro " ;
 const feedbackUrl = new URL ( ' /feedback ' , Astro . url ); feedbackUrl . search = actions . myAction . queryString ; --- &#x3C; FeedbackForm sendTo = { feedbackUrl . pathname } /> ` ">

#### `ActionClient.orThrow()`
 Section titled “ActionClient.orThrow()”
 Type: `(input?: any) => Promise&#x3C;Awaited&#x3C;TOutput>>`

A method that throws an error on failure instead of returning the errors. This is useful when you want exceptions rather than error handling.

The following example uses `orThrow()` to skip error handling when incrementing the like count fails:

 src/pages/posts/post-1.astro ` --- ---
 &#x3C;!-- your template -->
 &#x3C; script > import { actions } from ' astro:actions ' ;
 const post = document . querySelector ( ' article ' ); const button = document . querySelector ( ' button ' ); button ?. addEventListener ( ' click ' , async () => { const updatedLikes = await actions . likePost . orThrow ( { postId: post ?. id } ); }) &#x3C;/ script > `

### `ActionErrorCode`
 Section titled “ActionErrorCode”
 Type: `string`

A union type of standard HTTP status codes defined by IANA using the human-readable versions as uppercase strings separated by an underscore (e.g. `BAD_REQUEST` or `PAYLOAD_TOO_LARGE`).

### `ActionInputSchema`
 Section titled “ActionInputSchema”
 Type: `ZodType`

 Added in:
 `astro@5.16.0`

A utility type that automatically infers the TypeScript type of an action’s input based on its Zod schema. This can be useful to reference an action’s `input` validator type as an object in your own type definitions.

Returns `never` when `input` validator is omitted.

The following example uses `ActionInputSchema` on an action named `contact` to:

- Retrieve the Zod schema type for the input of the action.

- Retrieve the expected input type of the action’s validator.

 src/components/Form.astro ` --- import { actions, ActionInputSchema } from ' astro:actions ' ; import { z } from ' astro/zod ' ;
 type ContactSchema = ActionInputSchema &#x3C; typeof actions . contact >; type ContactInput = z . input &#x3C; ContactSchema >; --- ` ;type ContactInput = z.input ;---">

### `ActionReturnType`
 Section titled “ActionReturnType”
 Type: `Awaited&#x3C;ReturnType&#x3C;ActionHandler>>`

A utility type that extracts the output type from an action handler . This unwraps both the `Promise` (if the handler is async) and the `ReturnType` to give you the actual output type . This can be useful if you need to reference an action’s output type in your own type definitions.

The following example uses `ActionReturnType` to retrieve the expected output type for an action named `contact`:

 src/components/Form.astro ` --- import { actions, ActionReturnType } from ' astro:actions ' ;
 type ContactResult = ActionReturnType &#x3C; typeof actions . contact >; --- ` ;---">

### `SafeResult`
 Section titled “SafeResult”
 Type: `{ data: TOutput, error: undefined } | { data: undefined, error: ActionError }`

Represents the result of an action call:

- on success, `data` contains the output of the action and `error` is `undefined`.

- on failure, `error` contains an `ActionError` with validation errors or runtime errors, and `data` is `undefined`.

 Reference

 Contribute

 Community

 Sponsor

## Astro Assets

# Image and Assets API Reference

 Added in:
 `astro@3.0.0`

Astro provides built-in components and helper functions for optimizing and displaying your images. For features and usage examples, see our image guide .

## Imports from `astro:assets`
 Section titled “Imports from astro:assets”
 The following helpers are imported from the virtual assets module:

 - ` import { Image, Picture, Font, getImage, inferRemoteSize, getConfiguredImageService, imageConfig, fontData, experimental_getFontFileURL, } from ' astro:assets ' ; `

### `&#x3C;Image />`
 Section titled “&#x3C;Image />”
 The `&#x3C;Image />` component optimizes and transforms images.

 src/components/MyComponent.astro ` --- // import the Image component and the image import { Image } from ' astro:assets ' ; import myImage from " ../assets/my_image.png " ; // Image is 1600x900 ---
 &#x3C;!-- `alt` is mandatory on the Image component --> &#x3C; Image src = { myImage } alt = " A description of my image. " /> ` ">

```
` &#x3C;!-- Output --> &#x3C;!-- Image is optimized, proper attributes are enforced --> &#x3C; img src = " /_astro/my_image.hash.webp " width = " 1600 " height = " 900 " decoding = " async " loading = " lazy " alt = " A description of my image. " /> `
```
 ">
 The `&#x3C;Image />` component accepts the following listed properties in addition to all properties accepted by the HTML `&#x3C;img>` tag.

#### `src` (required)
 Section titled “src (required)”
 Type: ` ImageMetadata | string | Promise<{ default: ImageMetadata }>`

The format of the `src` value of your image file depends on where your image file is located:

 Local images in `src/` - you must also import the image using a relative file path or configure and use an import alias . Then use the import name as the `src` value:

 src/pages/index.astro ` --- import { Image } from ' astro:assets ' ; import myImportedImage from ' ../assets/my-local-image.png ' ; --- &#x3C; Image src = { myImportedImage } alt = " descriptive text " /> ` ">

-
 Images in the `public/` folder - use the image’s file path relative to the public folder :

 src/pages/index.astro ` --- import { Image } from ' astro:assets ' ; --- &#x3C; Image src = " /images/my-public-image.png " alt = " descriptive text " width = " 200 " height = " 150 " /> ` ">

-
 Remote images - use the image’s full URL as the property value:

 src/pages/index.astro ` --- import { Image } from ' astro:assets ' ; --- &#x3C; Image src = " https://example.com/remote-image.jpg " alt = " descriptive text " width = " 200 " height = " 150 " /> ` ">

#### `alt` (required)
 Section titled “alt (required)”
 Type: `string`

Use the required `alt` attribute to provide a string of descriptive alt text for images.

If an image is merely decorative (i.e. doesn’t contribute to the understanding of the page), set `alt=""` so that screen readers and other assistive technologies know to ignore the image.

#### `width` and `height` (required for images in `public/`)
 Section titled “width and height (required for images in public/)”
 Type: `number | `${number}` | undefined`

These properties define the dimensions to use for the image.

When a `layout` type is set, these are automatically generated based on the image’s dimensions and in most cases should not be set manually.

When using images in their original aspect ratio, `width` and `height` are optional. These dimensions can be automatically inferred from image files located in `src/`. For remote images, add the `inferSize` attribute set to `true` on the `&#x3C;Image />` or `&#x3C;Picture />` component or use `inferRemoteSize()` function .

However, both of these properties are required for images stored in your `public/` folder as Astro is unable to analyze these files.

#### `densities`
 Section titled “densities”
 Type: `(number | `${number}x`)[] | undefined`

 Added in:
 `astro@3.3.0`

A list of pixel densities to generate for the image.

The `densities` attribute is not compatible with having the `layout` prop or `image.layout` config set, and will be ignored if set.

If provided, this value will be used to generate a `srcset` attribute on the `&#x3C;img>` tag. Do not provide a value for `widths` when using this value.

Densities that are equal to widths larger than the original image will be ignored to avoid upscaling the image.

 src/components/MyComponent.astro ` --- import { Image } from ' astro:assets ' ; import myImage from ' ../assets/my_image.png ' ; --- &#x3C; Image src = { myImage } width = { myImage . width / 2 } densities = { [ 1.5 , 2 ] } alt = " A description of my image. " /> ` ">

```
` &#x3C;!-- Output --> &#x3C; img src = " /_astro/my_image.hash.webp " srcset = " /_astro/my_image.hash.webp 1.5x /_astro/my_image.hash.webp 2x " alt = " A description of my image. " width = " 800 " height = " 450 " loading = " lazy " decoding = " async " /> `
```
 ">

#### `widths`
 Section titled “widths”
 Type: `number[] | undefined`

 Added in:
 `astro@3.3.0`

A list of widths to generate for the image.

If provided, this value will be used to generate a `srcset` attribute on the `&#x3C;img>` tag. A `sizes` property must also be provided.

The `widths` and `sizes` attributes will be automatically generated for images using a `layout` property. Providing these values is generally not needed, but can be used to override any automatically generated values.

Do not provide a value for `densities` when using this value. Only one of these two values can be used to generate a `srcset`.

Widths that are larger than the original image will be ignored to avoid upscaling the image.

 src/components/MyComponent.astro ` --- import { Image } from ' astro:assets ' ; import myImage from ' ../assets/my_image.png ' ; // Image is 1600x900 --- &#x3C; Image src = { myImage } widths = { [ 240 , 540 , 720 , myImage . width ] } sizes = { ` (max-width: 360px) 240px, (max-width: 720px) 540px, (max-width: 1600px) 720px, ${ myImage . width } px ` } alt = " A description of my image. " /> ` ">

```
` &#x3C;!-- Output --> &#x3C; img src = " /_astro/my_image.hash.webp " srcset = " /_astro/my_image.hash.webp 240w, /_astro/my_image.hash.webp 540w, /_astro/my_image.hash.webp 720w, /_astro/my_image.hash.webp 1600w " sizes = " (max-width: 360px) 240px, (max-width: 720px) 540px, (max-width: 1600px) 720px, 1600px " alt = " A description of my image. " width = " 1600 " height = " 900 " loading = " lazy " decoding = " async " /> `
```
 ">

#### `sizes`
 Section titled “sizes”
 Type: `string | undefined`

 Added in:
 `astro@3.3.0`

Specifies the layout width of the image for each of a list of media conditions. Must be provided when specifying `widths`.

The `widths` and `sizes` attributes will be automatically generated for images using a `layout` property. Providing these values is generally not needed, but can be used to override any automatically generated values.

The generated `sizes` attribute for `constrained` and `full-width` images is based on the assumption that the image is displayed close to the full width of the screen when the viewport is smaller than the image’s width. If it is significantly different (e.g. if it’s in a multi-column layout on small screens), you may need to adjust the `sizes` attribute manually for best results.

#### `format`
 Section titled “format”
 Type: ` ImageOutputFormat | undefined`

You can optionally state the image file type output to be used.

By default, the `&#x3C;Image />` component will produce a `.webp` file.

#### `quality`
 Section titled “quality”
 Type: ` ImageQuality | undefined`

`quality` is an optional property that can either be:

- a preset (`low`, `mid`, `high`, `max`) that is automatically normalized between formats.

- a number from `0` to `100` (interpreted differently between formats).

#### `inferSize`
 Section titled “inferSize”
 Type: `boolean`
 Default: `false`

 Added in:
 `astro@4.4.0`

Allows you to set the original `width` and `height` of a remote image automatically.

By default, this value is set to `false` and you must manually specify both dimensions for your remote image.

Add `inferSize` to the `&#x3C;Image />` component (or `inferSize: true` to `getImage()`) to infer these values from the image content when fetched. This is helpful if you don’t know the dimensions of the remote image, or if they might change:

 src/components/MyComponent.astro ` --- import { Image } from ' astro:assets ' ; --- &#x3C; Image src = " https://example.com/cat.png " inferSize alt = " A cat sleeping in the sun. " /> ` ">
 As of Astro 5.17.3, `inferSize` only fetches dimensions for authorized remote image domains . Remote images outside the allowlist are not fetched.

#### `priority`
 Section titled “priority”
 Type: `boolean`
 Default: `false`

 Added in:
 `astro@5.10.0`

Allows you to automatically set the `loading`, `decoding`, and `fetchpriority` attributes to their optimal values for above-the-fold images.

 src/components/MyComponent.astro ` --- import { Image } from ' astro:assets ' ; import myImage from ' ../assets/my_image.png ' ; --- &#x3C; Image src = { myImage } priority alt = " A description of my image " /> ` ">
 When `priority="true"` (or the shorthand syntax `priority`) is added to the `&#x3C;Image />` or `&#x3C;Picture />` component, it will add the following attributes to instruct the browser to load the image immediately:

 ` loading="eager" decoding="sync" fetchpriority="high" `
 These individual attributes can still be set manually if you need to customize them further.

#### `layout`
 Section titled “layout”
 Type: `'constrained' | 'full-width' | 'fixed' | 'none'`
 Default: `image.layout | 'none'`

 Added in:
 `astro@5.10.0`

Determines how the image should resize when its container changes size. Can be used to override the default configured value for `image.layout` .

 MyComponent.astro ` --- import { Image } from ' astro:assets ' ; import myImage from ' ../assets/my_image.png ' ; --- &#x3C; Image src = { myImage } alt = " A description of my image. " layout = ' constrained ' width = { 800 } height = { 600 } /> ` ">
 When a layout is set, `srcset` and `sizes` attributes are automatically generated based on the image’s dimensions and the layout type. The previous `&#x3C;Image />` component will generate the following HTML output:

 ` &#x3C; img src = " /_astro/my_image.hash3.webp " srcset = " /_astro/my_image.hash1.webp 640w, /_astro/my_image.hash2.webp 750w, /_astro/my_image.hash3.webp 800w, /_astro/my_image.hash4.webp 828w, /_astro/my_image.hash5.webp 1080w, /_astro/my_image.hash6.webp 1280w, /_astro/my_image.hash7.webp 1600w " alt = " A description of my image " sizes = " (min-width: 800px) 800px, 100vw " loading = " lazy " decoding = " async " fetchpriority = " auto " width = " 800 " height = " 600 " style = " --fit: cover; --pos: center; " data-astro-image = " constrained " > ` ">
 `layout` supports the following values:

-
`constrained` - The image will scale down to fit the container, maintaining its aspect ratio, but will not scale up beyond the specified `width` and `height`, or the image’s original dimensions.

Use this if you want the image to display at the requested size where possible, but shrink to fit smaller screens. This matches the default behavior for images when using Tailwind. If you’re not sure, this is probably the layout you should choose.

-
`full-width` - The image will scale to fit the width of the container, maintaining its aspect ratio.

Use this for hero images or other images that should take up the full width of the page.

-
`fixed` - The image will maintain the requested dimensions and not resize. It will generate a `srcset` to support high density displays, but not for different screen sizes.

Use this if the image will not resize, for example icons or logos smaller than any screen width, or other images in a fixed-width container.

-
`none` - The image will not be responsive. No `srcset` or `sizes` will be automatically generated, and no styles will be applied.

This is useful if you have enabled a default layout, but want to disable it for a specific image.

For example, with `constrained` set as the default layout, you can override any individual image’s `layout` property:

 src/components/MyComponent.astro ` --- import { Image } from ' astro:assets ' ; import myImage from ' ../assets/my_image.png ' ; --- &#x3C; Image src = { myImage } alt = " This will use constrained layout " width = { 800 } height = { 600 } /> &#x3C; Image src = { myImage } alt = " This will use full-width layout " layout = " full-width " /> &#x3C; Image src = { myImage } alt = " This will disable responsive images " layout = " none " /> `   ">
 The value for `layout` also defines the default styles applied to the `&#x3C;img>` tag to determine how the image should resize according to its container:

 Responsive Image Styles ` :where ([ data-astro-image ]) { object-fit : var ( --fit ); object-position : var ( --pos ); } :where ([ data-astro-image = ' full-width ' ]) { width : 100 % ; } :where ([ data-astro-image = ' constrained ' ]) { max-width : 100 % ; } `

#### `fit`
 Section titled “fit”
 Type: `'contain' | 'cover' | 'fill' | 'none' | 'scale-down'`
 Default: `image.objectFit | 'cover'`

 Added in:
 `astro@5.10.0`

Defines how a image should be cropped if its aspect ratio is changed.

Values match those of CSS `object-fit`. Defaults to `cover`, or the value of `image.objectFit` if set. Can be used to override the default `object-fit` styles.

#### `position`
 Section titled “position”
 Type: `string`
 Default: `image.objectPosition | 'center'`

 Added in:
 `astro@5.10.0`

Defines the position of the image crop for a image if the aspect ratio is changed.

Values match those of CSS `object-position`. Defaults to `center`, or the value of `image.objectPosition` if set. Can be used to override the default `object-position` styles.

#### `background`
 Section titled “background”
 Type: `string | undefined`

 Added in:
 `astro@5.17.0`

The background color to use when flattening an image to transform it into the requested output `format`.

By default, Sharp uses a black background when flattening an image. Specifying a different background color is especially useful when transforming images with transparent backgrounds to a format that does not support transparency (e.g. `.jpeg`):

 src/components/MyComponent.astro ` &#x3C; Image src = { myImage } alt = " A description of my image " format = " jpeg " background = " #ffffff " /> ` ">
 Values are passed directly to the image service. Sharp accepts any value the `color-string` package can parse .

### `&#x3C;Picture />`
 Section titled “&#x3C;Picture />”

 Added in:
 `astro@3.3.0`

The `&#x3C;Picture />` component generates an optimized image with multiple formats and/or sizes.

 src/pages/index.astro ` --- import { Picture } from ' astro:assets ' ; import myImage from " ../assets/my_image.png " ; // Image is 1600x900 ---
 &#x3C;!-- `alt` is mandatory on the Picture component --> &#x3C; Picture src = { myImage } formats = { [ ' avif ' , ' webp ' ] } alt = " A description of my image. " /> ` ">

```
` &#x3C;!-- Output --> &#x3C; picture > &#x3C; source srcset = " /_astro/my_image.hash.avif " type = " image/avif " /> &#x3C; source srcset = " /_astro/my_image.hash.webp " type = " image/webp " /> &#x3C; img src = " /_astro/my_image.hash.png " width = " 1600 " height = " 900 " decoding = " async " loading = " lazy " alt = " A description of my image. " /> &#x3C;/ picture > `
```
     ">
 `&#x3C;Picture />` accepts all the properties of the `&#x3C;Image />` component plus the following:

#### `formats`
 Section titled “formats”
 Type: ` ImageOutputFormat []`

An array of image formats to use for the `&#x3C;source>` tags. Entries will be added as `&#x3C;source>` elements in the order they are listed, and this order determines which format is displayed. For the best performance, list the most modern format first (e.g. `webp` or `avif`). By default, this is set to `['webp']`.

#### `fallbackFormat`
 Section titled “fallbackFormat”
 Type: `ImageOutputFormat`

Format to use as a fallback value for the `&#x3C;img>` tag. Defaults to `.png` for static images (or `.jpg` if the image is a JPG), `.gif` for animated images, and `.svg` for SVG files.

#### `pictureAttributes`
 Section titled “pictureAttributes”
 Type: `HTMLAttributes&#x3C;'picture'>`

An object of attributes to be added to the `&#x3C;picture>` tag.

Use this property to apply attributes to the outer `&#x3C;picture>` element itself. Attributes applied to the `&#x3C;Picture />` component directly will apply to the inner `&#x3C;img>` element, except for those used for image transformation.

 src/components/MyComponent.astro ` --- import { Picture } from " astro:assets " ; import myImage from " ../my_image.png " ; // Image is 1600x900 ---
 &#x3C; Picture src = { myImage } alt = " A description of my image. " pictureAttributes = { { style: " background-color: red; " } } /> ` ">

```
` &#x3C;!-- Output --> &#x3C; picture style = " background-color: red; " > &#x3C; source srcset = " /_astro/my_image.hash.webp " type = " image/webp " /> &#x3C; img src = " /_astro/my_image.hash.png " alt = " A description of my image. " width = " 1600 " height = " 900 " loading = " lazy " decoding = " async " /> &#x3C;/ picture > `
```
    ">

### `&#x3C;Font />`
 Section titled “&#x3C;Font />”

 Added in:
 `astro@6.0.0`

The `&#x3C;Font />` component outputs style tags and can optionally output preload links for a given font family.

It must be imported and added to your page `&#x3C;head>`. This is commonly done in a component such as `Head.astro` that is used in a common site layout for global use but may be added to individual pages as needed.

With this component, you have control over which font family is used on which page, and which fonts are preloaded.

 src/components/Head.astro ` --- import { Font } from " astro:assets " ; ---
 &#x3C; Font cssVariable = " --font-roboto " /> ` ">
 The `&#x3C;Font />` component accepts the following properties:

#### `cssVariable` (required)
 Section titled “cssVariable (required)”
 Type: `CssVariable`
 Example type: `"--font-roboto" | "--font-comic-sans" | ...`

The `cssVariable` registered in your Astro configuration:

 src/components/Head.astro ` --- import { Font } from " astro:assets " ; ---
 &#x3C; Font cssVariable = " --font-roboto " /> ` ">

#### `preload`
 Section titled “preload”
 Type: `boolean | { weight?: string | number; style?: string; subset?: string }[]`
 Default: `false`

Whether to output preload links or not. With the `preload` directive, the browser will immediately begin downloading all possible font links during page load:

 src/components/Head.astro ` --- import { Font } from " astro:assets " ; ---
 &#x3C; Font cssVariable = " --font-roboto " preload /> ` ">
 Be very intentional about which fonts you preload. Preloading too many fonts can impact performance, as this can block loading other important resources or may download fonts that are not needed for the current page.

To selectively control which font files are preloaded, you can provide an array of objects describing any combination of font `weight`, `style`, or `subset` to preload:

 src/components/Head.astro ` --- import { Font } from " astro:assets " ; ---
 &#x3C; Font cssVariable = " --font-roboto " preload = { [ { subset: " latin " , style: " normal " }, { weight: " 400 " }, ] } /> ` ">
 Variable weight font files will be preloaded if any weight within its range is requested. For example, a font file for font weight `100 900` will be included when `400` is specified in a `preload` object.

### `getImage()`
 Section titled “getImage()”
 Type: `(options: UnresolvedImageTransform ) => Promise< GetImageResult >`

The `getImage()` function is intended for generating images destined to be used somewhere else than directly in HTML, for example in an API Route . It also allows you to create your own custom `&#x3C;Image />` component.

This takes an options object with the same properties as the Image component (except `alt`) and returns a `GetImageResult` object .

The following example generates an AVIF `background-image` for a `&#x3C;div />`:

 src/components/Background.astro ` --- import { getImage } from " astro:assets " ; import myBackground from " ../background.png "
 const optimizedBackground = await getImage ( {src: myBackground , format: ' avif ' } ) ---
 &#x3C; div style = { ` background-image: url( ${ optimizedBackground . src } ); ` } >&#x3C; slot />&#x3C;/ div > ` ">

### `inferRemoteSize()`
 Section titled “inferRemoteSize()”
 Type: `(url: string) => Promise<Omit< ImageMetadata , ‘src’ | ‘fsPath’>>`

 Added in:
 `astro@4.12.0`

A function to set the original `width` and `height` of a remote image automatically. This can be used as an alternative to passing the `inferSize` property.

 ` import { inferRemoteSize } from ' astro:assets ' ; const { width , height } = await inferRemoteSize ( " https://example.com/cat.png " ); `

### `getConfiguredImageService()`
 Section titled “getConfiguredImageService()”
 Type: `() => Promise< ImageService >`

 Added in:
 `astro@2.1.3`

Retrieves the resolved image service .

### `imageConfig`
 Section titled “imageConfig”
 Type: `AstroConfig["image"]`

 Added in:
 `astro@3.0.9`

The configuration options for images set by the user and merged with all defaults.

### `fontData`
 Section titled “fontData”
 Type: `Record<CssVariable, Array< FontData >>`

 Added in:
 `astro@6.0.0`

An object where each key is a `cssVariable` and the value is an array describing the associated fonts. Each font is an object containing an array of `src` available for that font and the following optional properties: `weight` and `style`:

 ` import { fontData } from " astro:assets "
 const data = fontData[ " --font-roboto " ] `

### `experimental_getFontFileURL()`
 Section titled “experimental_getFontFileURL()”
 Type: `(url: string, requestUrl?: URL) => Promise<string>`

 Added in:
 `astro@6.2.0`

Resolves a font file URL obtained from `fontData` :

 ` import { fontData, experimental_getFontFileURL } from " astro:assets " ;
 const fontPath = fontData[ " --font-roboto " ][ 0 ] ?. src [ 0 ] ?. url ;
 if (fontPath === undefined ) { throw new Error ( " Cannot find the font path. " ); }
 const url = experimental_getFontFileURL (fontPath); const buffer = await fetch (url) . then ( ( res ) => res . arrayBuffer ()); ` res.arrayBuffer());">
 When called on a route rendered on-demand , the request URL needs to be provided:

 ` import type { APIRoute } from " astro " ; import { fontData, experimental_getFontFileURL } from " astro:assets "
 export const prerender = false ; // Not needed in 'server' mode
 export const GET : APIRoute = async ( context ) => { // ... const url = experimental_getFontFileURL (fontPath , context . url ) ; // ... } ; ` { // ... const url = experimental_getFontFileURL(fontPath, context.url); // ...};">

## `astro:assets` types
 Section titled “astro:assets types”
 The following types are imported from the virtual assets module:

 ` import type { LocalImageProps, RemoteImageProps, FontData } from " astro/assets " ; `

### `LocalImageProps`
 Section titled “LocalImageProps”
 Type: `ImageSharedProps<T> & { src: ImageMetadata | Promise<{ default: ImageMetadata; }> }`

Describes the properties of a local image . This ensures that `src` matches the shape of an imported image.

 Learn more about imported images in `src/` with an example usage.

### `RemoteImageProps`
 Section titled “RemoteImageProps”
 Types:

- `ImageSharedProps&#x3C;T> &#x26; { src: string; inferSize: true; }`

- `ImageSharedProps&#x3C;T> &#x26; { src: string; inferSize?: false | undefined; }`

Describes the properties of a remote image . This ensures that when `inferSize` is not provided or is set to `false`, both `width` and `height` are required.

### `FontData`
 Section titled “FontData”
 Type: `{ src: Array<{ url: string; format?: string; tech?: string }>; weight?: string; style?: string; }`

 Added in:
 `astro@6.0.0`

Describes the font data associated with a given font family.

#### `FontData.src`
 Section titled “FontData.src”
 Type: `Array&#x3C;{ url: string; format?: string; tech?: string }>`

An array of objects describing the available font files for a given font family. Each object contains a `url` and, optionally, the associated `format` and `tech` .

#### `FontData.weight`
 Section titled “FontData.weight”
 Type: `string`

Specifies the font weight (e.g. `400`, `600`).

#### `FontData.style`
 Section titled “FontData.style”
 Type: `string`

Specifies the font style (e.g. `normal`, `italic`).

## Imports from `astro/assets`
 Section titled “Imports from astro/assets”
 The following helpers are imported from the regular assets module:

 ` import { baseService, getConfiguredImageService, getImage, isLocalService, } from " astro/assets " ; `

### `baseService`
 Section titled “baseService”
 Type: `Omit< LocalImageService , ‘transform’>`

The built-in local image service which can be extended to create a custom image service .

The following example reuses the `baseService` to create a new image service:

 src/image-service.ts ` import { baseService } from " astro/assets " ;
 const newImageService = { getURL: baseService . getURL , parseURL: baseService . parseURL , getHTMLAttributes: baseService . getHTMLAttributes , async transform ( inputBuffer , transformOptions ) { ... } } `

### `getConfiguredImageService()`
 Section titled “getConfiguredImageService()”
 See `getConfiguredImageService()` from `astro:assets`.

### `getImage()`
 Section titled “getImage()”
 Type: `(options: UnresolvedImageTransform , imageConfig: AstroConfig[‘image’] ) => Promise< GetImageResult >`

A function similar to `getImage()` from `astro:assets` with two required arguments: an `options` object with the same properties as the Image component and a second object for the image configuration .

### `isLocalService()`
 Section titled “isLocalService()”
 Type: `(service: ImageService | undefined) => boolean`

Checks the type of an image service and returns `true` when this is a local service .

## `astro/assets` types
 Section titled “astro/assets types”
 The following types are imported from the regular assets module:

 ` import type { LocalImageProps, RemoteImageProps, } from " astro/assets " ; `

### `LocalImageProps`
 Section titled “LocalImageProps”
 See `LocalImageProps` from `astro:assets`.

### `RemoteImageProps`
 Section titled “RemoteImageProps”
 See `RemoteImageProps` from `astro:assets`.

## Imports from `astro/assets/utils`
 Section titled “Imports from astro/assets/utils”
 The following helpers are imported from the `utils` directory in the regular assets module and can be used to build an image service :

 ` import { isRemoteAllowed, matchHostname, matchPathname, matchPattern, matchPort, matchProtocol, isESMImportedImage, isRemoteImage, resolveSrc, imageMetadata, emitImageMetadata, emitClientAsset, getOrigQueryParams, inferRemoteSize, propsToFilename, hashTransform, } from " astro/assets/utils " ; `

### `isRemoteAllowed()`
 Section titled “isRemoteAllowed()”
 Type: `(src: string, { domains, remotePatterns }: { domains: string[], remotePatterns: RemotePattern [] }) => boolean`

 Added in:
 `astro@4.0.0`

Determines whether a given remote resource, identified by its source URL, is allowed based on specified domains and remote patterns.

 ` import { isRemoteAllowed } from ' astro/assets/utils ' ;
 const url = new URL ( ' https://example.com/images/test.jpg ' ); const domains = [ ' example.com ' , ' anotherdomain.com ' ]; const remotePatterns = [ { protocol: ' https ' , hostname: ' images.example.com ' , pathname: ' /** ' , // Allow any path under this hostname } ];
 isRemoteAllowed (url . href , { domains, remotePatterns }); // Output: `true` `

### `matchHostname()`
 Section titled “matchHostname()”
 Type: `(url: URL, hostname?: string, allowWildcard = false) => boolean`

 Added in:
 `astro@4.0.0`

Matches a given URL’s hostname against a specified hostname, with optional support for wildcard patterns.

 ` import { matchHostname } from ' astro/assets/utils ' ;
 const url = new URL ( ' https://sub.example.com/path/to/resource ' );
 matchHostname (url, ' example.com ' ); // Output: `false` matchHostname (url, ' example.com ' , true ); // Output: `true` `

### `matchPathname()`
 Section titled “matchPathname()”
 Type: `(url: URL, pathname?: string, allowWildcard = false) => boolean`

 Added in:
 `astro@4.0.0`

Matches a given URL’s pathname against a specified pattern, with optional support for wildcards.

 ` import { matchPathname } from ' astro/assets/utils ' ;
 const testURL = new URL ( ' https://example.com/images/photo.jpg ' );
 matchPathname (testURL, ' /images/photo.jpg ' ); // Output: `true` matchPathname (testURL, ' /images/ ' ); // Output: `false` matchPathname (testURL, ' /images/* ' , true ); // Output: `true` `

### `matchPattern()`
 Section titled “matchPattern()”
 Type: `(url: URL, remotePattern: RemotePattern ) => boolean`

 Added in:
 `astro@4.0.0`

Evaluates whether a given URL matches the specified remote pattern based on protocol, hostname, port, and pathname.

 ` import { matchPattern } from ' astro/assets/utils ' ;
 const url = new URL ( ' https://images.example.com/photos/test.jpg ' ); const remotePattern = { protocol: ' https ' , hostname: ' images.example.com ' , pathname: ' /photos/** ' , // Allow all files under /photos/ } ;
 matchPattern (url, remotePattern); // Output: `true` `

### `matchPort()`
 Section titled “matchPort()”
 Type: `(url: URL, port?: string) => boolean`
 Default: `true`

 Added in:
 `astro@4.0.0`

Checks if the given URL’s port matches the specified port. If no port is provided, it returns `true`.

 ` import { matchPort } from ' astro/assets/utils ' ;
 const urlWithPort = new URL ( ' https://example.com:8080/resource ' ); const urlWithoutPort = new URL ( ' https://example.com/resource ' );
 matchPort (urlWithPort, ' 8080 ' ); // Output: `true` matchPort (urlWithoutPort, ' 8080 ' ); // Output: `false` `

### `matchProtocol()`
 Section titled “matchProtocol()”
 Type: `(url: URL, protocol?: string) => boolean`
 Default: `true`

 Added in:
 `astro@4.0.0`

Compares the protocol of the provided URL with a specified protocol. This returns `true` if the protocol matches or if no protocol is provided.

 ` import { matchProtocol } from ' astro/assets/utils ' ;
 const secureUrl = new URL ( ' https://example.com/resource ' ); const regularUrl = new URL ( ' http://example.com/resource ' );
 matchProtocol (secureUrl, ' https ' ); // Output: `true` matchProtocol (regularUrl, ' https ' ); // Output: `false` `

### `isESMImportedImage()`
 Section titled “isESMImportedImage()”
 Type: `(src: ImageMetadata | string) => boolean`

 Added in:
 `astro@4.0.0`

Determines if the given source is an ECMAScript Module (ESM) imported image.

 ` import { isESMImportedImage } from ' astro/assets/utils ' ;
 const imageMetadata = { src: ' /images/photo.jpg ' , width: 800 , height: 600 , format: ' jpg ' , } ; const filePath = ' /images/photo.jpg ' ;
 isESMImportedImage (imageMetadata); // Output: `true` isESMImportedImage (filePath); // Output: `false` `

### `isRemoteImage()`
 Section titled “isRemoteImage()”
 Type: `(src: ImageMetadata | string) => boolean`

 Added in:
 `astro@4.0.0`

Determines if the provided source is a remote image URL in the form of a string.

 ` import { isRemoteImage } from ' astro/assets/utils ' ;
 const imageUrl = ' https://example.com/images/photo.jpg ' ; const localImage = { src: ' /images/photo.jpg ' , width: 800 , height: 600 , format: ' jpg ' , } ;
 isRemoteImage (imageUrl); // Output: `true` isRemoteImage (localImage); // Output: `false` `

### `resolveSrc()`
 Section titled “resolveSrc()”
 Type: `(src: UnresolvedImageTransform[‘src’] ) => Promise<string | ImageMetadata >`

 Added in:
 `astro@4.0.0`

Returns the image source. This function ensures that if `src` is a Promise (e.g., a dynamic `import()`), it is awaited and the correct `src` is extracted. If `src` is already a resolved value, it is returned as-is.

 ` import { resolveSrc } from ' astro/assets/utils ' ; import localImage from " ./images/photo.jpg " ;
 const resolvedLocal = await resolveSrc (localImage); // Example value: `{ src: '/@fs/home/username/dev/astro-project/src/images/photo.jpg', width: 800, height: 600, format: 'jpg' }`
 const resolvedRemote = await resolveSrc ( " https://example.com/remote-img.jpg " ); // Value: `"https://example.com/remote-img.jpg"`
 const resolvedDynamic = await resolveSrc ( import ( " ./images/dynamic-image.jpg " )) // Example value: `{ src: '/@fs/home/username/dev/astro-project/src/images/dynamic-image.jpg', width: 800, height: 600, format: 'jpg' }` `

### `imageMetadata()`
 Section titled “imageMetadata()”
 Type: `(data: Uint8Array, src?: string) => Promise<Omit< ImageMetadata , ‘src’ | ‘fsPath’>>`

 Added in:
 `astro@4.0.0`

Extracts image metadata such as dimensions, format, and orientation from the provided image data.

 ` import { imageMetadata } from ' astro/assets/utils ' ;
 const binaryImage = new Uint8Array ([ /* ...binary image data... */ ]); const sourcePath = ' /images/photo.jpg ' ;
 const metadata = await imageMetadata (binaryImage , sourcePath); // Example value: // { // width: 800, // height: 600, // format: 'jpg', // orientation: undefined // } `

### `emitImageMetadata()`
 Section titled “emitImageMetadata()”
 Type: `(id: string | undefined, fileEmitter?: Rollup.EmitFile) => Promise<( ImageMetadata & { contents?: Buffer }) | undefined>`

 Added in:
 `astro@5.7.0`

Processes an image file and emits its metadata and optionally its contents. In build mode, the function uses `fileEmitter` to generate an asset reference. In development mode, it resolves to a local file URL with query parameters for metadata.

 ` import { emitImageMetadata } from ' astro/assets/utils ' ;
 const imageId = ' /images/photo.jpg ' ; const metadata = await emitImageMetadata (imageId); // Example value: // { // src: '/@fs/home/username/dev/astro-project/src/images/photo.jpg?origWidth=800&#x26;origHeight=600&#x26;origFormat=jpg', // width: 800, // height: 600, // format: 'jpg', // contents: Uint8Array([...]) // } `

### `emitClientAsset()`
 Section titled “emitClientAsset()”
 Type: `(pluginContext: Rollup.PluginContext , options: Rollup.EmitFile) => string`

 Added in:
 `astro@6.0.0`

Emits a client asset that will be moved to the client directory for assets (e.g. `dist/client/_astro/`) during SSR builds. This function is intended for integration authors who need to emit assets (such as images) from server-rendered content that should be available on the client.

Use this instead of Rollup `pluginContext.emitFile()` directly when working in a Vite plugin context and you need the emitted asset to be moved to the client output directory.

 ` import { emitClientAsset } from ' astro/assets/utils ' ;
 function myVitePlugin () { return { name: ' my-plugin ' , transform ( code , id ) { const handle = emitClientAsset ( this , { type: ' asset ' , name: ' my-image.png ' , source: imageBuffer , } ); // Returns the asset handle similar to `emitFile()` } } } `

### `getOrigQueryParams()`
 Section titled “getOrigQueryParams()”
 Type: `(params: URLSearchParams) => Pick< ImageMetadata , ‘width’ | ‘height’ | ‘format’> | undefined`

 Added in:
 `astro@4.0.0`

Retrieves the `width`, `height`, and `format` of an image from a `URLSearchParams` object . If any of these parameters are missing or invalid, the function returns `undefined`.

 ` import { getOrigQueryParams } from ' astro/assets/utils ' ;
 const url = new URL ( ' https://example.com/image.jpg?width=800&#x26;height=600&#x26;format=jpg ' ); const origParams = getOrigQueryParams (url . searchParams ); // Example value: // { // width: 800, // height: 600, // format: 'jpg' // } `

### `inferRemoteSize()`
 Section titled “inferRemoteSize()”
 Type: `(url: string) => Promise<Omit< ImageMetadata , ‘src’ | ‘fsPath’>>`

 Added in:
 `astro@4.0.0`

Infers the dimensions of a remote image by streaming its data and analyzing it progressively until sufficient metadata is available.

 ` import { inferRemoteSize } from ' astro/assets/utils ' ;
 const remoteImageUrl = ' https://example.com/image.jpg ' ; const imageSize = await inferRemoteSize (remoteImageUrl); // Example value: // { // width: 1920, // height: 1080, // format: 'jpg' // } `

### `propsToFilename()`
 Section titled “propsToFilename()”
 Type: `(filePath: string, transform: ImageTransform , hash: string) => string`

 Added in:
 `astro@4.0.0`

Generates a formatted filename for an image based on its source path, transformation properties, and a unique hash.

The formatted filename follows this structure:

`&#x3C;prefixDirname>/&#x3C;baseFilename>_&#x3C;hash>&#x3C;outputExtension>`

- `prefixDirname`: If the image is an ESM imported image, this is the directory name of the original file path; otherwise, it will be an empty string.

- `baseFilename`: The base name of the file or a hashed short name if the file is a `data:` URI.

- `hash`: A unique hash string generated to distinguish the transformed file.

- `outputExtension`: The desired output file extension derived from the `transform.format` or the original file extension.

 ` import { propsToFilename } from ' astro/assets/utils ' ;
 const filePath = ' /images/photo.jpg ' ; const transform = { format: ' png ' , src: filePath } ; const hash = ' abcd1234 ' ;
 const filename = propsToFilename (filePath , transform , hash); // Example value: '/images/photo_abcd1234.png' `

### `hashTransform()`
 Section titled “hashTransform()”
 Type: `(transform: ImageTransform , imageService: string, propertiesToHash: string[]) => string`

 Added in:
 `astro@4.0.0`

Transforms the provided `transform` object into a hash string based on selected properties and the specified `imageService`.

 ` import { hashTransform } from ' astro/assets/utils ' ;
 const transform = { src: ' /images/photo.jpg ' , width: 800 , height: 600 , format: ' jpg ' , } ; const imageService = ' astro/assets/services/sharp ' ; const propertiesToHash = [ ' width ' , ' height ' , ' format ' ];
 const hash = hashTransform (transform , imageService , propertiesToHash); // Example value: 'd41d8cd98f00b204e9800998ecf8427e' `

## `astro` types
 Section titled “astro types”

```
` import type { GetImageResult, ImageTransform, UnresolvedImageTransform, ImageMetadata, ImageInputFormat, ImageOutputFormat, ImageQuality, ImageQualityPreset, RemotePattern, ImageService, ExternalImageService, LocalImageService, ImageServiceConfig, } from " astro " ; `
```

### `GetImageResult`
 Section titled “GetImageResult”
 Type: `object`

 Added in:
 `astro@2.2.0`

Describes the result of the transformation after the call to `getImage()` .

#### `GetImageResult.attributes`
 Section titled “GetImageResult.attributes”
 Type: `Record&#x3C;string, any>`

Defines the additional HTML attributes needed to render the image (e.g. width, height, style).

#### `GetImageResult.options`
 Section titled “GetImageResult.options”
 Type: `ImageTransform`

Describes the transformation settings after validation.

#### `GetImageResult.rawOptions`
 Section titled “GetImageResult.rawOptions”
 Type: `ImageTransform`

Describes the original transformation settings.

#### `GetImageResult.src`
 Section titled “GetImageResult.src”
 Type: `string`

The path to the generated image.

#### `GetImageResult.srcSet`
 Section titled “GetImageResult.srcSet”
 Type: `{ values: { transform: ImageTransform ; descriptor?: string; attributes?: Record<string, any>; url: string; }[]; attribute: string; }`

 Added in:
 `astro@3.3.0`

An object describing how to render the `srcset` attribute .

 `GetImageResult.srcSet.values` Section titled “GetImageResult.srcSet.values”
 Type: `{ transform: ImageTransform ; descriptor?: string; attributes?: Record<string, any>; url: string; }[]`

An array of generated values where each entry includes a URL and a size descriptor. This can be used to manually generate the value of the `srcset` attribute.

 `GetImageResult.srcSet.attribute` Section titled “GetImageResult.srcSet.attribute”
 Type: `string`

A value ready to use in the `srcset` attribute.

### `ImageTransform`
 Section titled “ImageTransform”
 Type: `object`

Defines the options accepted by the image transformation service. This contains a required `src` property, optional predefined properties, and any additional properties required by the image service:

#### `ImageTransform.src`
 Section titled “ImageTransform.src”
 Type: ` ImageMetadata | string`

Defines the path to a local image in the `public` directory, the URL of a remote image, or the data from an imported image.

#### `ImageTransform.width`
 Section titled “ImageTransform.width”
 Type: `number | undefined`

The width of the image.

#### `ImageTransform.height`
 Section titled “ImageTransform.height”
 Type: `number | undefined`

The height of the image.

#### `ImageTransform.widths`
 Section titled “ImageTransform.widths”
 Type: `number[] | undefined`

 Added in:
 `astro@3.3.0`

A list of widths to generate for the image.

#### `ImageTransform.densities`
 Section titled “ImageTransform.densities”
 Type: `(number | `${number}x`)[] | undefined`

 Added in:
 `astro@3.3.0`

A list of pixel densities to generate for the image.

#### `ImageTransform.quality`
 Section titled “ImageTransform.quality”
 Type: ` ImageQuality | undefined`

The desired quality for the output image.

#### `ImageTransform.format`
 Section titled “ImageTransform.format”
 Type: ` ImageOutputFormat | undefined`

The desired format for the output image.

#### `ImageTransform.fit`
 Section titled “ImageTransform.fit”
 Type: `'fill' | 'contain' | 'cover' | 'none' | 'scale-down' | string | undefined`

 Added in:
 `astro@5.0.0`

Defines a list of allowed values for the `object-fit` CSS property, extensible with any string.

#### `ImageTransform.position`
 Section titled “ImageTransform.position”
 Type: `string | undefined`

 Added in:
 `astro@5.0.0`

Controls the value for the `object-position` CSS property.

### `UnresolvedImageTransform`
 Section titled “UnresolvedImageTransform”
 Type: `Omit< ImageTransform , “src”> & { src: ImageMetadata | string | Promise<{ default: ImageMetadata }>; inferSize?: boolean; }`

Represents an image with transformation options. This contains the same properties as the `ImageTransform` type with a different `src` type and an additional `inferSize` property.

#### `UnresolvedImageTransform.src`
 Section titled “UnresolvedImageTransform.src”
 Type: ` ImageMetadata | string | Promise<{ default: ImageMetadata }>`

The path to an image imported or located in the `public` directory, or the URL of a remote image.

#### `UnresolvedImageTransform.inferSize`
 Section titled “UnresolvedImageTransform.inferSize”
 Type: `boolean`

Determines whether the width and height of the image should be inferred.

 See also the `inferSize` attribute available on `&#x3C;Image />`.

### `ImageMetadata`
 Section titled “ImageMetadata”
 Type: `{ src: string; width: number; height: number; format: ImageInputFormat ; orientation?: number; }`

 Added in:
 `astro@2.1.3`

Describes the data collected during image import. This contains the following properties:

#### `ImageMetadata.src`
 Section titled “ImageMetadata.src”
 Type: `string`

The absolute path of the image on the filesystem.

#### `ImageMetadata.width`
 Section titled “ImageMetadata.width”
 Type: `number`

The width of the image.

#### `ImageMetadata.height`
 Section titled “ImageMetadata.height”
 Type: `number`

The height of the image.

#### `ImageMetadata.format`
 Section titled “ImageMetadata.format”
 Type: `ImageInputFormat`

The format of the image.

#### `ImageMetadata.orientation`
 Section titled “ImageMetadata.orientation”
 Type: `number`

 Added in:
 `astro@2.8.3`

The image orientation when its metadata contains this information.

### `ImageInputFormat`
 Section titled “ImageInputFormat”
 Type: `"jpeg" | "jpg" | "png" | "tiff" | "webp" | "gif" | "svg" | "avif"`

 Added in:
 `astro@2.2.0`

Describes a union of supported formats for imported images.

### `ImageOutputFormat`
 Section titled “ImageOutputFormat”
 Type: `string | "jpeg" | "jpg" | "png" | "webp" | "svg" | "avif"`

 Added in:
 `astro@2.2.0`

Specifies the format for output images. This can be a predefined literal or any string.

### `ImageQuality`
 Section titled “ImageQuality”
 Type: ` ImageQualityPreset | number`

 Added in:
 `astro@2.2.0`

Represents the perceptual quality of the output image as a union of predefined literals, a string, or a number.

### `ImageQualityPreset`
 Section titled “ImageQualityPreset”
 Type: `string | "low" | "mid" | "high" | "max"`

 Added in:
 `astro@2.2.0`

Defines the available presets to control image quality, extensible with any string.

### `RemotePattern`
 Section titled “RemotePattern”
 Type: `{ hostname?: string; pathname?: string; protocol?: string; port?: string; }`

 Added in:
 `astro@5.14.2`

Describes a remote host through four optional properties: `hostname`, `pathname`, `protocol`, and `port`.

### `ImageService`
 Section titled “ImageService”
 Type: ` ExternalImageService | LocalImageService `

Defines the hooks that a local or external image service must provide.

### `ExternalImageService`
 Section titled “ExternalImageService”
 Type: `object`

Defines the hooks that an external image transformation service must provide. This requires a `getUrl()` hook and supports three additional hooks .

 Learn how to build external services in the Image Service API reference with example usage.

### `LocalImageService`
 Section titled “LocalImageService”
 Type: `object`

Defines the hooks that a local image transformation service must provide. This requires `getUrl()` , `parseUrl()` , and `transform()` hooks, and supports additional hooks .

 Learn how to build local services in the Image Service API reference with example usage.

### `ImageServiceConfig`
 Section titled “ImageServiceConfig”
 Type: `{ entrypoint: 'astro/assets/services/sharp' | string; config?: T; }`

 Added in:
 `astro@2.3.3`

Describes the configuration object for an image service. This contains the following properties:

#### `ImageServiceConfig.entrypoint`
 Section titled “ImageServiceConfig.entrypoint”
 Type: `'astro/assets/services/sharp' | string`

A package or path to the image service module. This can be Astro’s built-in Sharp service or a third-party service.

#### `ImageServiceConfig.config`
 Section titled “ImageServiceConfig.config”
 Type: `Record&#x3C;string, any>`

A configuration object passed to the image service. The shape depends on the specific service being used.

 Reference

 Contribute

 Community

 Sponsor

## Astro Config

# Config imports API Reference

 Added in:
 `astro@5.7.0`

This virtual module `astro:config` exposes a non-exhaustive, serializable, type-safe version of the Astro configuration. There are two submodules for accessing different subsets of your configuration values: `/client` and `/server` .

All available config values can be accessed from `astro:config/server`. However, for code executed on the client, only those values exposed by `astro:config/client` will be available. This protects your information by only making some data available to the client.

## Imports from `astro:config/client`
 Section titled “Imports from astro:config/client”
 The following helpers are imported from the `client` directory of the virtual config module.

 - ` import { i18n, trailingSlash, base, build, site, compressHTML, } from " astro:config/client " ; `
 Use this submodule for client-side code:

 src/utils.js ` import { trailingSlash } from " astro:config/client " ;
 function addForwardSlash ( path ) { if ( trailingSlash === " always " ) { return path . endsWith ( " / " ) ? path : path + " / " } else { return path } } `
 See more about the configuration imports available from `astro:config/client`:

 `i18n`

- `trailingSlash`

- `base`

- `build.format`

- `site`

- `compressHTML`

## Imports from `astro:config/server`
 Section titled “Imports from astro:config/server”
 The following helpers are imported from the `server` directory of the virtual config module.

 ` import { i18n, trailingSlash, base, build, site, srcDir, cacheDir, outDir, publicDir, root, compressHTML, } from " astro:config/server " ; `
 These imports include everything available from `astro:config/client` as well as additional sensitive information about your file system configuration that is not safe to expose to the client.

Use this submodule for server side code:

 astro.config.mjs ` import { integration } from " ./integration.mjs " ;
 export default defineConfig ({ integrations: [ integration (), ] }); `
 integration.mjs
```
` import { outDir } from " astro:config/server " ; import { writeFileSync } from " node:fs " ; import { fileURLToPath } from " node:url " ;
 export default function () { return { name: " internal-integration " , hooks: { " astro:build:done " : () => { let file = new URL ( " result.json " , outDir ); // generate data from some operation let data = JSON . stringify ([]); writeFileSync ( fileURLToPath ( file ) , data , " utf-8 " ); } } } } `
```
 { let file = new URL(&#x22;result.json&#x22;, outDir); // generate data from some operation let data = JSON.stringify([]); writeFileSync(fileURLToPath(file), data, &#x22;utf-8&#x22;); } } }}">
 See more about the configuration imports available from `astro:config/server`:

- `i18n`

- `trailingSlash`

- `base`

- `build.format`

- `build.client`

- `build.server`

- `build.assetsPrefix`

- `site`

- `srcDir`

- `cacheDir`

- `outDir`

- `publicDir`

- `root`

- `compressHTML`

## Imports from `astro/config`
 Section titled “Imports from astro/config”
 The following helpers are imported from the regular config module:

 ` import { defineConfig, envField, fontProviders, getViteConfig, mergeConfig, passthroughImageService, sessionDrivers, sharpImageService, validateConfig, } from " astro/config " ; `

### `defineConfig()`
 Section titled “defineConfig()”
 Type: `(config: AstroUserConfig ) => AstroUserConfig`

Configures your project with type safety in a supported Astro configuration file .

### `envField`
 Section titled “envField”
 Type: `object`

 Added in:
 `astro@5.0.0`

Describes the supported data types when defining environment variables .

Each data type must define the variable type with `context` (`"client"` or `"server"`) and `access` (`"secret"` or `"public"`). In addition, you can define a `default` value, specify whether the variable is `optional` (default `false`), and some data types provide optional validation methods.

 Learn more about using type safe environment variables in your Astro project.

#### `envField.string()`
 Section titled “envField.string()”
 Type: `(options: StringFieldInput) => StringField`

Defines an environment variable of string type. You can perform string validation with Zod using the following properties: `max`, `min`, `length`, `url`, `includes`, `startsWith`, and `endsWith`.

The following example defines the expected shape for an environment variable storing an API URL:

 astro.config.mjs ` import { defineConfig, envField } from " astro/config " ;
 export default defineConfig ({ env: { schema: { API_URL: envField . string ({ context: " client " , access: " public " , optional: false , default: "" , min: 12 , url: true , includes: " astro " , startsWith: " https " , }), } } }) `

#### `envField.number()`
 Section titled “envField.number()”
 Type: `(options: NumberFieldInput) => NumberField`

Defines an environment variable of number type. You can perform number validation with Zod using the following properties: `gt`, `lt`, `min`, `max`, and `int`.

The following example defines the expected shape for an environment variable storing an API port:

 astro.config.mjs ` import { defineConfig, envField } from " astro/config " ;
 export default defineConfig ({ env: { schema: { API_PORT: envField . number ({ context: " server " , access: " public " , optional: true , default: 4321 , min: 2 , int: true , }), } } }) `

#### `envField.boolean()`
 Section titled “envField.boolean()”
 Type: `(options: BooleanFieldInput) => BooleanField`

Defines an environment variable of boolean type.

The following example defines the expected shape for an environment variable storing whether analytics are enabled:

 astro.config.mjs ` import { defineConfig, envField } from " astro/config " ;
 export default defineConfig ({ env: { schema: { ANALYTICS_ENABLED: envField . boolean ({ context: " client " , access: " public " , optional: true , default: true , }), } } }) `

#### `envField.enum()`
 Section titled “envField.enum()”
 Type: `(options: EnumFieldInput&#x3C;T>) => EnumField`

Defines an environment variable of enum type by providing the allowed `values` as an array.

The following example defines the expected shape for an environment variable storing the configured debug mode:

 astro.config.mjs ` import { defineConfig, envField } from " astro/config " ;
 export default defineConfig ({ env: { schema: { DEBUG_MODE: envField . enum ({ context: " server " , access: " public " , values: [ ' info ' , ' warnings ' , ' errors ' ], // required optional: true , default: ' errors ' , }), } } }) `

### `fontProviders`
 Section titled “fontProviders”
 Type: `object`

 Added in:
 `astro@6.0.0`

Describes the built-in provider used to retrieve the configured font .

### `getViteConfig()`
 Section titled “getViteConfig()”
 Type: `(userViteConfig: ViteUserConfig , inlineAstroConfig?: AstroInlineConfig ) => ViteUserConfigFn`

Retrieves the Vite configuration to use by merging a custom Vite configuration object and an optional Astro configuration object. This is useful to set up Vitest for testing .

### `mergeConfig()`
 Section titled “mergeConfig()”
 See `mergeConfig()` in the Programmatic API reference .

### `passthroughImageService()`
 Section titled “passthroughImageService()”
 Type: `() => ImageServiceConfig `

Retrieves a no-op image service. This is useful when your adapter does not support Astro’s built-in Sharp image optimization and you want to use the `&#x3C;Image />` and `&#x3C;Picture />` components .

The following example defines `passthroughImageService()` as image service in the Astro configuration file to avoid Sharp image processing:

 astro.config.mjs ` import { defineConfig, passthroughImageService } from " astro/config " ;
 export default defineConfig ({ image: { service: passthroughImageService () } }); `

 Learn more about configuring a no-op passthrough service .

### `sessionDrivers`
 Section titled “sessionDrivers”
 Type: `object`

 Added in:
 `astro@5.7.0`

Describes the built-in driver used for session storage .

The following example configures the Redis driver to enable sessions:

 astro.config.mjs ` import { defineConfig, sessionDrivers } from " astro/config " ;
 export default defineConfig ({ session: { driver: sessionDrivers . redis ({ url: process . env . REDIS_URL }), } }) `

 Learn more about using sessions in your Astro project.

### `sharpImageService()`
 Section titled “sharpImageService()”
 Type: `(config?: SharpImageServiceConfig) => ImageServiceConfig `

 Added in:
 `astro@2.4.1`

Retrieves the Sharp service used to process Astro’s image assets. This takes an optional object describing the configuration options for Sharp .

### `validateConfig()`
 Section titled “validateConfig()”
 See `validateConfig()` in the Programmatic API reference .

 Reference

 Contribute

 Community

 Sponsor

## Astro Content

# Content Collections API Reference

 Added in:
 `astro@2.0.0`

Build-time content collections offer APIs to configure, query, and render your local Markdown, MDX, Markdoc, YAML, TOML, or JSON files, as well as remote content.

 Added in:
 `astro@6.0.0`

Live content collections offer APIs to configure, query, and render fresh, up-to-the-moment live data from remote sources.

For features and usage examples, see our content collections guide .

## Imports from `astro:content`
 Section titled “Imports from astro:content”
 -
```
` import { defineCollection, defineLiveCollection, getCollection, getLiveCollection, getEntry, getLiveEntry, getEntries, reference, render } from ' astro:content ' ; `
```

### `defineCollection()`
 Section titled “defineCollection()”
 Type: `(input: CollectionConfig) => CollectionConfig`

 Added in:
 `astro@2.0.0`

A utility to configure a collection in a `src/content.config.*` file.

 src/content.config.ts ` import { defineCollection } from ' astro:content ' ; import { z } from ' astro/zod ' ; import { glob } from ' astro/loaders ' ;
 const blog = defineCollection ( { loader: glob ( { pattern: ' **/*.md ' , base: ' ./src/data/blog ' } ) , schema: z . object ( { title: z . string () , permalink: z . string () . optional () , } ) , } );
 // Expose your defined collection to Astro // with the `collections` export export const collections = { blog } ; `
 This function accepts the following properties:

#### `loader`
 Section titled “loader”
 Type: `() => Promise<Array<{ id: string, [key: string]: any }> | Record<string, Record<string, any>>> | Loader `

 Added in:
 `astro@5.0.0`

Either an object or a function that allows you to load data from any source, local or remote, into a build-time content collection. (For live collections, see the live `loader` property.)

 Learn about build-time collection loaders with guided explanations and example usage.

#### `schema`
 Section titled “schema”
 Type: `ZodType | (context: SchemaContext ) => ZodType`

 Added in:
 `astro@2.0.0`

An optional Zod object or function that returns a Zod object to configure the type and shape of document frontmatter for a collection. Each value must use a Zod validator . (For live collections, see the live `schema` property.)

 Learn about defining a collection schema using Zod with guided explanations, example usage, and common datatypes.

### `defineLiveCollection()`
 Section titled “defineLiveCollection()”
 Type: `(config: LiveCollectionConfig) => LiveCollectionConfig`

 Added in:
 `astro@6.0.0`

A utility to configure a live collection in a `src/live.config.*` file.

 src/live.config.ts ` import { defineLiveCollection } from ' astro:content ' ; import { storeLoader } from ' @example/astro-loader ' ;
 const products = defineLiveCollection ( { loader: storeLoader ( { apiKey: process . env . STORE_API_KEY , endpoint: ' https://api.example.com/v1 ' , } ) , } );
 // Expose your defined collection to Astro // with the `collections` export export const collections = { products } ; `
 This function accepts the following properties:

#### `loader`
 Section titled “loader”
 Type: `LiveLoader`

 Added in:
 `astro@6.0.0`

An object that allows you to load data at runtime from a remote source into a live content collection. (For build-time collections, see the build-time `loader` property.)

 Learn how to create a live loader with guided explanations and example usage.

#### `schema`
 Section titled “schema”
 Type: `ZodType`

 Added in:
 `astro@6.0.0`

An optional Zod object to configure the type and shape of your data for a live collection. Each value must use a Zod validator . (For build-time collections, see the build-time `schema` property.)

When you define a schema, it will take precedence over the live loader’s types when you query the collection.

 Learn about using Zod schemas with live collections through guided explanations and usage examples.

### `reference()`
 Section titled “reference()”
 Type: `(collection: CollectionKey ) => ZodEffects<ZodString, { collection: CollectionKey, id: string }>`

 Added in:
 `astro@2.5.0`

A function used in the content config to define a relationship, or “reference”, from one collection to another. This accepts a collection name and transforms the reference into an object containing the collection name and the reference id.

This example defines references from a blog author to the `authors` collection and an array of related posts to the same `blog` collection:

 src/content.config.ts ` import { defineCollection, reference } from ' astro:content ' ; import { z } from ' astro/zod ' ; import { glob, file } from ' astro/loaders ' ;
 const blog = defineCollection ( { loader: glob ( { pattern: ' **/*.md ' , base: ' ./src/data/blog ' } ) , schema: z . object ( { // Reference a single author from the `authors` collection by `id` author: reference ( ' authors ' ) , // Reference an array of related posts from the `blog` collection by `slug` relatedPosts: z . array ( reference ( ' blog ' )) , } ) } );
 const authors = defineCollection ( { loader: file ( " src/data/authors.json " ) , schema: z . object ( { /* ... */ } ) } );
 export const collections = { blog , authors } ; `
 Validation of referenced entries happens at runtime when using `getEntry()` or `getEntries()`:

 src/pages/[posts].astro ` // if a referenced entry is invalid, this will return undefined. const relatedPosts = await getEntries(blogPost.data.relatedPosts); `

 Learn how to define and use collection references with guided explanations and usage examples.

### `getCollection()`
 Section titled “getCollection()”
 Type: `(collection: CollectionKey , filter?: (entry: CollectionEntry ) => boolean) => CollectionEntry[]`

 Added in:
 `astro@2.0.0`

A function that retrieves a list of content collection entries by collection name.

It returns all items in the collection by default, and accepts an optional `filter` function to narrow by entry properties. This allows you to query for only some items in a collection based on `id` or frontmatter values via the `data` object.

 src/pages/blog/index.astro ` --- import { getCollection } from ' astro:content ' ;
 // Get all `src/data/blog/` entries const allBlogPosts = await getCollection ( ' blog ' );
 // Only return posts with `draft: true` in the frontmatter const draftBlogPosts = await getCollection ( ' blog ' , ( { data } ) => { return data . draft === true ; } ); --- ` { return data.draft === true;});---">

 Learn how to query build time collections with guided explanations and example usage.

### `getLiveCollection()`
 Section titled “getLiveCollection()”
 Type: `(collection: string, filter?: LiveLoaderCollectionFilterType) => Promise< LiveDataCollectionResult >`

 Added in:
 `astro@6.0.0`

A function that retrieves a list of live content collection entries by collection name.

It returns all items in the collection by default, and accepts an optional `filter` object whose shape is defined by the collection’s loader. This allows you to query for only some items in a collection or retrieve data in a different form, depending on your API’s capabilities.

 src/pages/shop/index.astro ` --- import { getLiveCollection } from ' astro:content ' ;
 // Get all `products` entries from your API const { entries : allProducts } = await getLiveCollection ( ' products ' );
 // Only return `products` that should be featured const { entries : featuredProducts } = await getLiveCollection ( ' products ' , { featured: true } ); --- `

 Learn how to access live collections data with guided explanations and example usage.

### `getEntry()`
 Section titled “getEntry()”
 Types:

`(collection: CollectionKey , id: string) => Promise< CollectionEntry | undefined>`

-
`({ collection: CollectionKey , id: string }) => Promise< CollectionEntry | undefined>`

 Added in:
 `astro@2.5.0`

A function that retrieves a single collection entry by collection name and the entry `id`. `getEntry()` can also be used to get referenced entries to access the `data` or `body` properties:

 src/pages/index.astro ` --- import { getEntry } from ' astro:content ' ;
 // Get `src/content/blog/enterprise.md` const enterprisePost = await getEntry ( ' blog ' , ' enterprise ' );
 // Get `src/content/captains/picard.json` const picardProfile = await getEntry ( ' captains ' , ' picard ' );
 // Get the profile referenced by `data.captain` const enterpriseCaptainProfile = await getEntry (enterprisePost . data . captain ); --- `

 Learn more about querying build time collections with guided explanations and example usage.

### `getLiveEntry()`
 Section titled “getLiveEntry()”
 Type: `(collection: string, filter: string | LiveLoaderEntryFilterType) => Promise< LiveDataEntryResult >`

 Added in:
 `astro@6.0.0`

A function that retrieves a single live collection entry by collection name and an optional filter, either as an `id` string or as a type-safe object.

 src/pages/blog/[id].astro ` --- import { getLiveEntry } from ' astro:content ' ;
 const { entry : liveCollectionsPost } = await getLiveEntry ( ' blog ' , Astro . params . id ); const { entry : mattDraft } = await getLiveEntry ( ' blog ' , { status: ' draft ' , author: ' matt ' , } ); --- `

 Learn how to access live collections data with guided explanations and example usage.

### `getEntries()`
 Section titled “getEntries()”
 Type: `({ collection: CollectionKey , id: string }[]) => CollectionEntry []`

 Added in:
 `astro@2.5.0`

A function that retrieves multiple collection entries from the same collection. This is useful for returning an array of referenced entries to access their associated `data` and `body` properties.

 src/pages/blog/enterprise/index.astro ` --- import { getEntries, getEntry } from ' astro:content ' ;
 const enterprisePost = await getEntry ( ' blog ' , ' enterprise ' );
 // Get related posts referenced by `data.relatedPosts` const enterpriseRelatedPosts = await getEntries (enterprisePost . data . relatedPosts ); --- `

### `render()`
 Section titled “render()”
 Type: `(entry: CollectionEntry ) => Promise<RenderResult>`

 Added in:
 `astro@5.0.0`

A function to compile a given entry for rendering. This returns the following properties:

- `&#x3C;Content />` - A component used to render the document’s contents in an Astro file.

- `headings` - A generated list of headings, mirroring Astro’s `getHeadings()` utility on Markdown and MDX imports.

- `remarkPluginFrontmatter ` - The modified frontmatter object after any Markdown plugins have been applied . Set to type `any`.

 src/pages/blog/entry-1.astro ` --- import { getEntry, render } from ' astro:content ' ; const entry = await getEntry ( ' blog ' , ' entry-1 ' );
 if ( ! entry) { // Handle Error, for example: throw new Error ( ' Could not find blog post 1 ' ); } const { Content , headings , remarkPluginFrontmatter } = await render (entry); --- `

 Learn how to render the body content of entries with guided explanations and example usage.

## `astro:content` types
 Section titled “astro:content types”

```
` import type { CollectionEntry, CollectionKey, SchemaContext, } from ' astro:content ' ; `
```

### `CollectionEntry`
 Section titled “CollectionEntry”
 Query functions including `getCollection()` , `getEntry()` , and `getEntries()` each return entries with the `CollectionEntry` type. This type is available as a utility from `astro:content`:

 ` import type { CollectionEntry } from ' astro:content ' ; `
 A generic type to use with the name of the collection you’re querying to represent a single entry in that collection.
For example, an entry in your `blog` collection would have the type `CollectionEntry&#x3C;'blog'>`.

Each `CollectionEntry` is an object with the following values:

#### `CollectionEntry.id`
 Section titled “CollectionEntry.id”
 Type: `string`

A unique ID. Note that all IDs from Astro’s built-in `glob()` loader are slugified.

#### `CollectionEntry.collection`
 Section titled “CollectionEntry.collection”
 Type: `CollectionKey`

The name of a collection in which entries are located. This is the name used to reference the collection in your schema and in querying functions.

#### `CollectionEntry.data`
 Section titled “CollectionEntry.data”
 Type: `CollectionSchema&#x3C;TCollectionName>`

An object of frontmatter properties inferred from your collection schema ( see `defineCollection()` reference ). Defaults to `any` if no schema is configured.

#### `CollectionEntry.body`
 Section titled “CollectionEntry.body”
 Type: `string | undefined`

A string containing the raw, uncompiled body of the Markdown or MDX document.

Note that if `retainBody` is set to `false`, this value will be `undefined` instead of containing the raw file contents.

#### `CollectionEntry.rendered`
 Section titled “CollectionEntry.rendered”
 Type: `RenderedContent | undefined`

The rendered content of an entry as stored by your loader . For example, this can be the rendered content of a Markdown entry, or HTML from a CMS.

#### `CollectionEntry.filePath`
 Section titled “CollectionEntry.filePath”
 Type: `string | undefined`

The path to an entry relative to your project directory. This value is only available for local entries.

### `CollectionKey`
 Section titled “CollectionKey”
 Example Type: `'blog' | 'authors' | ...`

 Added in:
 `astro@3.1.0`

A string union of all collection names defined in your `src/content.config.*` file. This type can be useful when defining a generic function wrapping the built-in `getCollection()`.

 src/utils/collections.ts ` import { type CollectionKey, getCollection } from ' astro:content ' ;
 export async function queryCollection ( collection : CollectionKey ) { return getCollection (collection , ( { data } ) => { return data . draft !== true ; }); } ` { return data.draft !== true; });}">

### `SchemaContext`
 Section titled “SchemaContext”
 The `context` object that `defineCollection` uses for the function shape of `schema`. This type can be useful when building reusable schemas for multiple collections.

This includes the following property:

- `image` - The `image()` schema helper that allows you to use local images in Content Collections

 src/content.config.ts ` import { defineCollection, type SchemaContext } from " astro:content " ; import { z } from ' astro/zod ' ; import { glob } from ' astro/loaders ' ;
 export const imageSchema = ( { image } : SchemaContext ) => z . object ( { image: image () , description: z . string () . optional () , } );
 const blog = defineCollection ( { loader: glob ( { pattern: ' **/*.md ' , base: ' ./src/data/blog ' } ) , schema : ( { image } ) => z . object ( { title: z . string () , permalink: z . string () . optional () , image: imageSchema ( { image } ) } ) , } ); `  z.object({ image: image(), description: z.string().optional(), });const blog = defineCollection({ loader: glob({ pattern: &#x27;**/*.md&#x27;, base: &#x27;./src/data/blog&#x27; }), schema: ({ image }) => z.object({ title: z.string(), permalink: z.string().optional(), image: imageSchema({ image }) }),});">

## `astro` types
 Section titled “astro types”

```
` import type { LiveDataCollectionResult, LiveDataEntryResult, } from " astro " ; `
```

### `LiveDataCollectionResult`
 Section titled “LiveDataCollectionResult”
 Type: `{ entries?: Array< LiveDataEntry <TData>>; error?: TError | LiveCollectionError; cacheHint?: CacheHint ; }`

 Added in:
 `astro@6.0.0`

An object returned by `getLiveCollection()` containing the data fetched by the live loader. It has the following properties:

#### `LiveDataCollectionResult.entries`
 Section titled “LiveDataCollectionResult.entries”
 Type: `Array< LiveDataEntry <TData>> | undefined`

An array of `LiveDataEntry` objects returned by the loader.

The following example accesses the returned entries for a live collection named `products`:

 src/pages/shop/index.astro ` --- import { getLiveCollection } from ' astro:content ' ;
 const { entries : allProducts } = await getLiveCollection ( ' products ' ); --- `

 Learn how to access live data with guided explanations and example usage.

#### `LiveDataCollectionResult.error`
 Section titled “LiveDataCollectionResult.error”
 Type: `TError | LiveCollectionError | undefined`

An error returned when the loader failed to load the collection. This can be a custom error defined by the loader or a built-in error.

The following example accesses the error returned when retrieving data from a live collection named `products`:

 src/pages/shop/index.astro ` --- import { getLiveCollection } from ' astro:content ' ;
 const { error } = await getLiveCollection ( ' products ' ); --- `

 Learn more about error handling with guided explanations and example usage.

#### `LiveDataCollectionResult.cacheHint`
 Section titled “LiveDataCollectionResult.cacheHint”
 Type: ` CacheHint | undefined`

An object providing guidance on how to cache this collection.

If you have experimental route caching enabled, pass the cache hint directly to `Astro.cache.set()`:

 src/pages/shop/index.astro ` --- import { getLiveCollection } from ' astro:content ' ; export const prerender = false ; // Not needed in 'server' mode
 const { cacheHint } = await getLiveCollection ( ' products ' );
 if (cacheHint) { Astro . cache . set (cacheHint); } Astro . cache . set ({ maxAge: 600 }); --- `
 You can also use cache hints to set response headers manually:

 src/pages/shop/index.astro ` --- import { getLiveCollection } from ' astro:content ' ;
 const { cacheHint } = await getLiveCollection ( ' products ' );
 if (cacheHint ?. tags ) { Astro . response . headers . set ( ' Cache-Tag ' , cacheHint . tags . join ( ' , ' )); } if (cacheHint ?. lastModified ) { Astro . response . headers . set ( ' Last-Modified ' , cacheHint . lastModified . toUTCString ()); } --- `

### `LiveDataEntryResult`
 Section titled “LiveDataEntryResult”
 Type: `{ entry?: LiveDataEntry <TData>; error?: TError | LiveCollectionError; cacheHint?: CacheHint ; }`

 Added in:
 `astro@6.0.0`

An object returned by `getLiveEntry()` containing the data fetched by the live loader. It has the following properties:

#### `LiveDataEntryResult.entry`
 Section titled “LiveDataEntryResult.entry”
 Type: ` LiveDataEntry <TData> | undefined`

The `LiveDataEntry` object returned by the loader.

The following example accesses the requested entry in a live collection named `products`:

 src/pages/shop/[id].astro ` --- import { getLiveEntry } from ' astro:content ' ;
 const { entry } = await getLiveEntry ( ' products ' , Astro . params . id ); --- `

 Learn how to access live data with guided explanations and example usage.

#### `LiveDataEntryResult.error`
 Section titled “LiveDataEntryResult.error”
 Type: `TError | LiveCollectionError | undefined`

An error returned when the loader failed to load the entry. This can be a custom error defined by the loader or a built-in error.

The following example accesses the requested entry in a live collection named `products` and any error, and redirects to the 404 page if an error exists:

 src/pages/shop/[id].astro ` --- import { getLiveEntry } from ' astro:content ' ;
 const { entry , error } = await getLiveEntry ( ' products ' , Astro . params . id );
 if (error) { return Astro . redirect ( ' /404 ' ); } --- &#x3C; h1 > { entry . data . name } &#x3C;/ h1 > `

 Learn more about error handling with guided explanations and example usage.

#### `LiveDataEntryResult.cacheHint`
 Section titled “LiveDataEntryResult.cacheHint”
 Type: ` CacheHint | undefined`

An object providing data that can be used to inform a caching strategy.

If you have experimental route caching enabled, pass the cache hint directly to `Astro.cache.set()`:

 src/pages/shop/[id].astro ` --- import { getLiveEntry } from ' astro:content ' ;
 export const prerender = false ; // Not needed in 'server' mode
 const { cacheHint } = await getLiveEntry ( ' products ' , Astro . params . id );
 if (cacheHint) { Astro . cache . set (cacheHint); } Astro . cache . set ({ maxAge: 300 }); --- `
 You can also use cache hints to set response headers manually:

 src/pages/shop/[id].astro
```
` --- import { getLiveEntry } from ' astro:content ' ;
 const { cacheHint } = await getLiveEntry ( ' products ' , Astro . params . id );
 if (cacheHint ?. tags ) { Astro . response . headers . set ( ' Cache-Tag ' , cacheHint . tags . join ( ' , ' )); } if (cacheHint ?. lastModified ) { Astro . response . headers . set ( ' Last-Modified ' , cacheHint . lastModified . toUTCString ()); } --- `
```

 Reference

 Contribute

 Community

 Sponsor

## Astro Env

# Environment Variables API Reference

 Added in:
 `astro@5.0.0`

The `astro:env` API lets you configure a type-safe schema for environment variables you have set. This allows you to indicate whether they should be available on the server or the client, and define their data type and additional properties. For examples and usage instructions, see the `astro:env` guide .

## Imports from `astro:env`
 Section titled “Imports from astro:env”

```
` import { getSecret, } from ' astro:env/server ' ; `
```

### `getSecret()`
 Section titled “getSecret()”

 Added in:
 `astro@5.0.0`

The `getSecret()` helper function allows retrieving the raw value of an environment variable by its key.

For example, you can retrieve a boolean value as a string:

 ` import { FEATURE_FLAG, // boolean getSecret } from ' astro:env/server '
 getSecret ( ' FEATURE_FLAG ' ) // string | undefined `
 This can also be useful to get a secret not defined in your schema, for example one that depends on dynamic data from a database or API.

If you need to retrieve environment variables programmatically, we recommend using `getSecret()` instead of `process.env` (or equivalent). Because its implementation is provided by your adapter, you won’t need to update all your calls if you switch adapters. It defaults to `process.env` in dev and build.

 Reference

 Contribute

 Community

 Sponsor

## Astro I18N

# Internationalization API Reference

 Added in:
 `astro@3.5.0`

This module provides functions to help you create URLs using your project’s configured locales.

Creating routes for your project with the i18n router will depend on certain configuration values you have set that affect your page routes. When creating routes with these functions, be sure to take into account your individual settings for:

- `base`

- `trailingSlash`

- `build.format`

- `site`

Also, note that the returned URLs created by these functions for your `defaultLocale` will reflect your `i18n.routing` configuration.

For features and usage examples, see our i18n routing guide .

## Imports from `astro:i18n`
 Section titled “Imports from astro:i18n”
 -
```
` import { getRelativeLocaleUrl, getAbsoluteLocaleUrl, getRelativeLocaleUrlList, getAbsoluteLocaleUrlList, getPathByLocale, getLocaleByPath, redirectToDefaultLocale, redirectToFallback, notFound, middleware, requestHasLocale, normalizeTheLocale, pathHasLocale, toCodes, toPaths } from ' astro:i18n ' ; `
```

### `getRelativeLocaleUrl()`
 Section titled “getRelativeLocaleUrl()”
 Type: `(locale: string, path?: string, options?: GetLocaleOptions) => string`

Use this function to retrieve a relative path for a locale. If the locale doesn’t exist, Astro throws an error.

 ` --- import { getRelativeLocaleUrl } from ' astro:i18n ' ;
 getRelativeLocaleUrl ( " fr " ); // returns /fr
 getRelativeLocaleUrl ( " fr " , "" ); // returns /fr/
 getRelativeLocaleUrl ( " fr " , " getting-started " ); // returns /fr/getting-started
 getRelativeLocaleUrl ( " fr_CA " , " getting-started " , { prependWith: " blog " }); // returns /blog/fr-ca/getting-started
 getRelativeLocaleUrl ( " fr_CA " , " getting-started " , { prependWith: " blog " , normalizeLocale: false }); // returns /blog/fr_CA/getting-started --- `

### `getAbsoluteLocaleUrl()`
 Section titled “getAbsoluteLocaleUrl()”
 Type: `(locale: string, path?: string, options?: GetLocaleOptions) => string`

Use this function to retrieve an absolute path for a locale when [`site`] has a value. If [`site`] isn’t configured, the function returns a relative URL. If the locale doesn’t exist, Astro throws an error.

 src/pages/index.astro ` --- import { getAbsoluteLocaleUrl } from ' astro:i18n ' ;
 // If `site` is set to be `https://example.com`
 getAbsoluteLocaleUrl ( " fr " ); // returns https://example.com/fr
 getAbsoluteLocaleUrl ( " fr " , "" ); // returns https://example.com/fr/
 getAbsoluteLocaleUrl ( " fr " , " getting-started " ); // returns https://example.com/fr/getting-started
 getAbsoluteLocaleUrl ( " fr_CA " , " getting-started " , { prependWith: " blog " }); // returns https://example.com/blog/fr-ca/getting-started
 getAbsoluteLocaleUrl ( " fr_CA " , " getting-started " , { prependWith: " blog " , normalizeLocale: false }); // returns https://example.com/blog/fr_CA/getting-started --- `

### `getRelativeLocaleUrlList()`
 Section titled “getRelativeLocaleUrlList()”
 Type: `(path?: string, options?: GetLocaleOptions) => string[]`

Use this like `getRelativeLocaleUrl` to return a list of relative paths for all the locales.

### `getAbsoluteLocaleUrlList()`
 Section titled “getAbsoluteLocaleUrlList()”
 Type: `(path?: string, options?: GetLocaleOptions) => string[]`

Use this like `getAbsoluteLocaleUrl` to return a list of absolute paths for all the locales.

### `getPathByLocale()`
 Section titled “getPathByLocale()”
 Type: `(locale: string) => string`

A function that returns the `path` associated to one or more `codes` when custom locale paths are configured.

 astro.config.mjs ` export default defineConfig ({ i18n: { locales: [ " es " , " en " , { path: " french " , codes: [ " fr " , " fr-BR " , " fr-CA " ] }] } }) `
 src/pages/index.astro
```
` --- import { getPathByLocale } from ' astro:i18n ' ;
 getPathByLocale ( " fr " ); // returns "french" getPathByLocale ( " fr-CA " ); // returns "french" --- `
```

### `getLocaleByPath()`
 Section titled “getLocaleByPath()”
 Type: `(path: string) => string`

A function that returns the `code` associated to a locale `path`.

 astro.config.mjs ` export default defineConfig ({ i18n: { locales: [ " es " , " en " , { path: " french " , codes: [ " fr " , " fr-BR " , " fr-CA " ] }] } }) `
 src/pages/index.astro
```
` --- import { getLocaleByPath } from ' astro:i18n ' ;
 getLocaleByPath ( " french " ); // returns "fr" because that's the first code configured --- `
```

### `redirectToDefaultLocale()`
 Section titled “redirectToDefaultLocale()”
 Type: `(context: APIContext, statusCode?: ValidRedirectStatus) => Promise<Response>`

 Added in:
 `astro@4.6.0`

A function that returns a `Response` that redirects to the `defaultLocale` configured. It accepts an optional valid redirect status code.

 middleware.js ` import { defineMiddleware } from " astro:middleware " ; import { redirectToDefaultLocale } from " astro:i18n " ;
 export const onRequest = defineMiddleware ( ( context , next ) => { if ( context . url . pathname . startsWith ( " /about " )) { return next () ; } else { return redirectToDefaultLocale ( context , 302 ) ; } } ) ` { if (context.url.pathname.startsWith(&#x22;/about&#x22;)) { return next(); } else { return redirectToDefaultLocale(context, 302); }})">

### `redirectToFallback()`
 Section titled “redirectToFallback()”
 Type: `(context: APIContext, response: Response) => Promise<Response>`

 Added in:
 `astro@4.6.0`

A function that allows you to use your `i18n.fallback` configuration in your own middleware.

 middleware.js ` import { defineMiddleware } from " astro:middleware " ; import { redirectToFallback } from " astro:i18n " ;
 export const onRequest = defineMiddleware ( async ( context , next ) => { const response = await next () ; if ( response . status >= 300 ) { return redirectToFallback ( context , response ) } return response ; } ) ` { const response = await next(); if (response.status >= 300) { return redirectToFallback(context, response) } return response;})">

### `notFound()`
 Section titled “notFound()”
 Type: `(context: APIContext, response?: Response) => Promise<Response> | undefined`

 Added in:
 `astro@4.6.0`

Use this function in your routing middleware to return a 404 when:

 the current path isn’t a root. e.g. `/` or `/&#x3C;base>`

- the URL doesn’t contain a locale

When a `Response` is passed, the new `Response` emitted by this function will contain the same headers of the original response.

 middleware.js ` import { defineMiddleware } from " astro:middleware " ; import { notFound } from " astro:i18n " ;
 export const onRequest = defineMiddleware ( ( context , next ) => { const pathNotFound = notFound ( context ) ; if ( pathNotFound ) { return pathNotFound ; } return next () ; } ) ` { const pathNotFound = notFound(context); if (pathNotFound) { return pathNotFound; } return next();})">

### `middleware()`
 Section titled “middleware()”
 Type: `(options: { fallbackType: "redirect" | "rewrite", prefixDefaultLocale: boolean, redirectToDefaultLocale: boolean }) => MiddlewareHandler`

 Added in:
 `astro@4.6.0`

A function that allows you to programmatically create the Astro i18n middleware.

This is useful when you still want to use the default i18n logic, but add only a few exceptions to your website.

 middleware.js ` import { middleware } from " astro:i18n " ; import { sequence, defineMiddleware } from " astro:middleware " ;
 const customLogic = defineMiddleware ( async ( context , next ) => { const response = await next () ;
 // Custom logic after resolving the response. // It's possible to catch the response coming from Astro i18n middleware.
 return response ; } );
 export const onRequest = sequence ( customLogic , middleware ( { prefixDefaultLocale: true , redirectToDefaultLocale: false , fallbackType: " redirect " , } ) , ); ` { const response = await next(); // Custom logic after resolving the response. // It&#x27;s possible to catch the response coming from Astro i18n middleware. return response;});export const onRequest = sequence( customLogic, middleware({ prefixDefaultLocale: true, redirectToDefaultLocale: false, fallbackType: &#x22;redirect&#x22;, }),);">

### `requestHasLocale()`
 Section titled “requestHasLocale()”
 Type: `(context: APIContext) => boolean`

 Added in:
 `astro@4.6.0`

Checks whether the current URL contains a configured locale. Internally, this function will use `APIContext#url.pathname`.

 middleware.js ` import { defineMiddleware } from " astro:middleware " ; import { requestHasLocale } from " astro:i18n " ;
 export const onRequest = defineMiddleware ( async ( context , next ) => { if ( requestHasLocale ( context )) { return next () ; } return new Response ( " Not found " , { status: 404 } ) ; } ) ` { if (requestHasLocale(context)) { return next(); } return new Response(&#x22;Not found&#x22;, { status: 404 });})">

### `normalizeTheLocale()`
 Section titled “normalizeTheLocale()”
 Type: `(locale: string) => string`

Replaces underscores (`_`) with hyphens (`-`) in the given locale before returning a lowercase version.

 src/pages/index.astro ` --- import { normalizeTheLocale } from " astro:i18n " ;
 normalizeTheLocale ( " it_VT " ) // returns `it-vt` // Assuming the current locale is `"pt-PT"`: normalizeTheLocale (Astro . currentLocale ) // returns `pt-pt` --- `

### `pathHasLocale()`
 Section titled “pathHasLocale()”
 Type: `(path: string) => boolean`

 Added in:
 `astro@4.6.0`

Checks whether the given path contains a configured locale.

This is useful to prevent errors before using an i18n utility that relies on a locale from a URL path.

 astro.config.mjs ` export default defineConfig ({ i18n: { locales: [ { codes: [ " it-VT " , " it " ], path: " italiano " }, " es " ] } }) `
 src/pages/index.astro
```
` --- import { pathHasLocale } from " astro:i18n " ;
 pathHasLocale ( " italiano " ); // returns `true` pathHasLocale ( " es " ); // returns `true` pathHasLocale ( ' /es/blog/ ' ); // returns `true` pathHasLocale ( " it-VT " ); // returns `false` --- `
```

### `toCodes()`
 Section titled “toCodes()”
 Type: `(locales: Locales) => string[]`

 Added in:
 `astro@4.0.0`

Retrieves the configured locale codes for each locale defined in your configuration. When multiple codes are associated to a locale, only the first one will be added to the array.

 astro.config.mjs ` export default defineConfig ({ i18n: { locales: [ { codes: [ " it-VT " , " it " ], path: " italiano " }, " es " ] } }) `
 src/pages/index.astro
```
` --- import { i18n } from " astro:config/client " ; import { toCodes } from " astro:i18n " ;
 toCodes (i18n !. locales ); // ["it-VT", "es"] --- `
```

### `toPaths()`
 Section titled “toPaths()”
 Type: `(locales: Locales) => string[]`

 Added in:
 `astro@4.0.0`

Retrieves the configured locale paths for each locale defined in your configuration.

 astro.config.mjs
```
` export default defineConfig ({ i18n: { locales: [ { codes: [ " it-VT " , " it " ], path: " italiano " }, " es " ] } }) `
```

 src/pages/index.astro
```
` --- import { i18n } from " astro:config/client " ; import { toPaths } from " astro:i18n " ;
 toPaths (i18n !. locales ); // ["italiano", "es"] --- `
```

 Reference

 Contribute

 Community

 Sponsor

## Astro Middleware

# Middleware API Reference

 Added in:
 `astro@2.6.0`

Middleware allows you to intercept requests and responses and inject behaviors dynamically every time a page or endpoint is about to be rendered. For features and usage examples, see our middleware guide .

## Imports from `astro:middleware`
 Section titled “Imports from astro:middleware”
 The following helpers are imported from the virtual middleware module:

 ` import { defineMiddleware, sequence, } from ' astro:middleware ' ; `

### `defineMiddleware()`
 Section titled “defineMiddleware()”
 Type: `(fn: MiddlewareHandler ) => MiddlewareHandler`

A function for defining a middleware function with type safety. When you use this utility, the `context` and `next()` arguments are automatically typed, and you will get a TypeScript error if you try to return a value not supported in your middleware .

 src/middleware.ts ` import { defineMiddleware } from " astro:middleware " ;
 export const onRequest = defineMiddleware ( ( context , next ) => { /* your middleware logic */ } ); ` { /* your middleware logic */});">

### `sequence()`
 Section titled “sequence()”
 Type: `(…handlers: MiddlewareHandler []) => MiddlewareHandler`

A function that accepts middleware functions as arguments, and will execute them in the order in which they are passed.

 src/middleware.js ` import { sequence } from " astro:middleware " ;
 async function validation ( context , next ) { /* ... */ } async function auth ( context , next ) { /* ... */ } async function greeting ( context , next ) { /* ... */ }
 export const onRequest = sequence ( validation , auth , greeting ); `

## Imports from `astro/middleware`
 Section titled “Imports from astro/middleware”
 The following helpers can be imported from the regular middleware module when you build an Astro Integration :

 ` import { createContext, defineMiddleware, sequence, trySerializeLocals, } from " astro/middleware " ; `

### `createContext()`
 Section titled “createContext()”
 Type: `(context: CreateContext ) => APIContext `

 Added in:
 `astro@2.8.0`

A low-level API to create an `APIContext` to be passed to an Astro middleware `onRequest()` function .

This function can be used by integrations/adapters to programmatically execute the Astro middleware.

### `defineMiddleware()`
 Section titled “defineMiddleware()”
 See `defineMiddleware()` from `astro:middleware`.

### `sequence()`
 Section titled “sequence()”
 See `sequence()` from `astro:middleware`.

### `trySerializeLocals()`
 Section titled “trySerializeLocals()”
 Type: `(value: unknown) => string`

 Added in:
 `astro@2.8.0`

A low-level API that takes in any value and tries to return a serialized version (a string) of it. If the value cannot be serialized, the function will throw a runtime error.

## `astro/middleware` types
 Section titled “astro/middleware types”
 The following types are imported from the regular middleware module:

 ` import type { CreateContext, } from " astro/middleware " ; `

### `CreateContext`
 Section titled “CreateContext”
 Type: `{ request: Request; params?: Params; userDefinedLocales?: string[]; defaultLocale: string; locals: App.Locals; clientAddress?: string }`

 Added in:
 `astro@2.8.0`

An object to create a context to be passed to an Astro middleware. This contains the following properties:

#### `CreateContext.request`
 Section titled “CreateContext.request”
 Type: `Request`

The incoming `Request` object.

#### `CreateContext.params`
 Section titled “CreateContext.params”
 Type: `Params`

An object containing the optional parameters to be passed to `Astro.params` .

#### `CreateContext.userDefinedLocales`
 Section titled “CreateContext.userDefinedLocales”
 Type: `string[]`

 Added in:
 `astro@3.5.0`

A list of supported locales defined in the user’s `i18n` configuration .

#### `CreateContext.defaultLocale`
 Section titled “CreateContext.defaultLocale”
 Type: `string`

 Added in:
 `astro@4.16.0`

The default locale defined in the user’s `i18n` configuration .

#### `CreateContext.locals`
 Section titled “CreateContext.locals”
 Type: `App.Locals`

 Added in:
 `astro@5.0.0`

An object for storing arbitrary information from a middleware, accessible to the user via `Astro.locals` .

 Learn more about storing data in `locals` with example usage.

#### `CreateContext.clientAddress`
 Section titled “CreateContext.clientAddress”
 Type: `string`

 Added in:
 `astro@6.0.0`

The IP address of the request.

This must be provided by the adapter or platform from a trusted source (e.g. socket address, platform-provided header).

If not provided, accessing `clientAddress` will throw an error.

## `astro` types
 Section titled “astro types”

```
` import type { MiddlewareHandler, MiddlewareNext, RewritePayload, } from " astro " ; `
```

### `MiddlewareHandler`
 Section titled “MiddlewareHandler”
 Type: `(context: APIContext , next: MiddlewareNext ) => Promise<Response> | Response | Promise<void> | void`

Represents an Astro middleware function. Middleware handlers receive two arguments and can either return a `Response` directly or call `next()` to invoke the next middleware in the chain. Alternatively, you can use `defineMiddleware()` to get type safety for your middleware.

The following example imports the `MiddlewareHandler` type to get type safety in the `onRequest()` function:

 src/middleware.ts ` import type { MiddlewareHandler } from " astro " ;
 export const onRequest : MiddlewareHandler = ( context , next ) => { /* the middleware logic */ } ; ` { /* the middleware logic */};">
 A middleware handler receives the following properties:

#### `context`
 Section titled “context”
 Type: `APIContext`

An Astro context object mirroring many of the `Astro` global properties.

#### `next()`
 Section titled “next()”
 Type: `MiddlewareNext`

A function that calls all the subsequent middleware in the chain and returns a `Response`. For example, other middleware could modify the HTML body of a response and awaiting the result of `next()` would allow your middleware to respond to those changes.

Since Astro v4.13.0, `next()` accepts an optional URL path parameter in the form of a string, `URL`, or `Request` to rewrite the current request without retriggering a new rendering phase.

The following example uses `next()` to serve content from a different path when the current path matches `/old-path`:

 src/middleware.ts ` import type { MiddlewareHandler } from " astro " ;
 export const onRequest : MiddlewareHandler = ( context , next ) => { if (context . url . pathname === ' /old-path ' ) { return next ( ' /new-path ' ) ; } return next () ; } ; ` { if (context.url.pathname === &#x27;/old-path&#x27;) { return next(&#x27;/new-path&#x27;); } return next();};">

### `MiddlewareNext`
 Section titled “MiddlewareNext”
 Type: `(rewritePayload?: RewritePayload ) => Promise<Response>`

Represents the `next()` function passed to middleware handlers.

### `RewritePayload`
 Section titled “RewritePayload”
 Type: `string | URL | Request`

 Added in:
 `astro@4.13.0`

Represents the destination for a rewrite when passed to the `next()` function.

## Middleware exports
 Section titled “Middleware exports”
 When defining your project’s middleware in `src/middleware.js`, export the following user-defined functions:

### `onRequest()`
 Section titled “onRequest()”
 Type: `MiddlewareHandler`

A required exported function from `src/middleware.js` that will be called before rendering every page or API route. It receives two arguments: `context` and `next()` . `onRequest()` must return a `Response`: either directly, or by calling `next()`.

 src/middleware.js
```
` export function onRequest ( context , next ) { // intercept response data from a request // optionally, transform the response // return a Response directly, or the result of calling `next()` return next (); }; `
```

 Reference

 Contribute

 Community

 Sponsor

## Astro Static Paths

# Static Paths API Reference

 Added in:
 `astro@6.0.0`

This module provides utilities to help adapters collect static paths from within their target runtime (e.g. `workerd`). This only provides a real implementation in the `prerender` Vite environment. In other environments, it returns a no-op implementation.

## Imports from `astro:static-paths`
 Section titled “Imports from astro:static-paths”

```
` import { StaticPaths, } from ' astro:static-paths ' ; `
```

### `StaticPaths`
 Section titled “StaticPaths”
 Allows adapters to collect all paths that need to be prerendered from within their target runtime. This is useful when implementing a custom prerenderer that runs in a non-Node environment:

The `StaticPaths` constructor accepts a required SSR manifest and an object describing the route cache and providing a method to access the component used to render the route. The preferred method to initiate a `StaticPaths` instance is to pass it an app instance .

The following example initializes a `StaticPaths` instance from an app in an adapter server entrypoint:

 my-adapter/server.js ` import { createApp } from ' astro/app/entrypoint ' ; import { StaticPaths } from ' astro:static-paths ' ;
 const app = createApp (); const staticPaths = new StaticPaths ( app );
 export const handler = ( event , context ) => { // do something with `staticPaths` } ; ` { // do something with &#x60;staticPaths&#x60;};">

#### `StaticPaths.getAll()`
 Section titled “StaticPaths.getAll()”
 Type: `() => Promise<Array<{ pathname: string, route: RouteData }>>`

Retrieves all paths that should be prerendered. This returns a promise that resolves to an array of objects describing the route path and its data.

The following example collects all static paths to be pre-rendered before returning them as `Response` in an adapter handler:

 my-adapter/handler.js
```
` import { StaticPaths } from ' astro:static-paths ' ;
 export function createHandler ( app ) { return async ( request ) => { const { pathname } = new URL ( request . url );
 // Endpoint to collect static paths during build if ( pathname === ' /__astro_static_paths ' ) { const staticPaths = new StaticPaths ( app ); const paths = await staticPaths . getAll (); // Returns array of { pathname: string, route: RouteData } return new Response ( JSON . stringify ({ paths })); }
 // ... handle other requests }; } `
```
 { const { pathname } = new URL(request.url); // Endpoint to collect static paths during build if (pathname === &#x27;/__astro_static_paths&#x27;) { const staticPaths = new StaticPaths(app); const paths = await staticPaths.getAll(); // Returns array of { pathname: string, route: RouteData } return new Response(JSON.stringify({ paths })); } // ... handle other requests };}">

 Reference

 Contribute

 Community

 Sponsor

## Astro Transitions

# View Transitions Router API Reference

 Added in:
 `astro@3.0.0`

These modules provide functions to control and interact with the View Transitions API and client-side router.

For features and usage examples, see our View Transitions guide .

## Imports from `astro:transitions`
 Section titled “Imports from astro:transitions”
 -
```
` import { ClientRouter, fade, slide, } from ' astro:transitions ' ; `
```

### `&#x3C;ClientRouter />`
 Section titled “&#x3C;ClientRouter />”

 Added in:
 `astro@5.0.0`

Opt in to using view transitions on individual pages by importing and adding the `&#x3C;ClientRouter />` routing component to `&#x3C;head>` on every desired page.

 src/pages/index.astro ` --- import { ClientRouter } from ' astro:transitions ' ; --- &#x3C; html lang = " en " > &#x3C; head > &#x3C; title > My Homepage &#x3C;/ title > &#x3C; ClientRouter /> &#x3C;/ head > &#x3C; body > &#x3C; h1 > Welcome to my website! &#x3C;/ h1 > &#x3C;/ body > &#x3C;/ html > `   My Homepage    
# Welcome to my website!
  ">
 See more about how to control the router and add transition directives to page elements and components.

The `&#x3C;ClientRouter />` component accepts the following props:

#### `fallback`

 Type: `Fallback`
 Default: `animate`

Defines the fallback strategy to use for browsers that do not support the View Transitions API .

### `fade`
 Section titled “fade”
 Type: `(opts: { duration?: string | number }) => TransitionDirectionalAnimations`

 Added in:
 `astro@3.0.0`

Utility function to support customizing the duration of the built-in `fade` animation.

 ` --- import { fade } from ' astro:transitions ' ; ---
 &#x3C;!-- Fade transition with the default duration --> &#x3C; div transition:animate = " fade " />
 &#x3C;!-- Fade transition with a duration of 400 milliseconds --> &#x3C; div transition:animate = { fade ( { duration: ' 0.4s ' } ) } /> `  ">

### `slide`
 Section titled “slide”
 Type: `(opts: { duration?: string | number }) => TransitionDirectionalAnimations`

 Added in:
 `astro@3.0.0`

Utility function to support customizing the duration of the built-in `slide` animation.

 ` --- import { slide } from ' astro:transitions ' ; ---
 &#x3C;!-- Slide transition with the default duration --> &#x3C; div transition:animate = " slide " />
 &#x3C;!-- Slide transition with a duration of 400 milliseconds --> &#x3C; div transition:animate = { slide ( { duration: ' 0.4s ' } ) } /> `  ">

## Imports from `astro:transitions/client`
 Section titled “Imports from astro:transitions/client”

```
` import { getFallback, navigate, supportsViewTransitions, swapFunctions, transitionEnabledOnThisPage, /* The following were deprecated in v6: */ isTransitionBeforePreparationEvent, isTransitionBeforeSwapEvent, TRANSITION_AFTER_PREPARATION, TRANSITION_AFTER_SWAP, TRANSITION_BEFORE_PREPARATION, TRANSITION_BEFORE_SWAP, TRANSITION_PAGE_LOAD, } from ' astro:transitions/client ' ; `
```

### `navigate()`
 Section titled “navigate()”
 Type: `(href: string, options?: Options) => void`

 Added in:
 `astro@3.2.0`

Executes a navigation to the given `href` using the View Transitions API.

This function signature is based on the `navigate` function from the browser Navigation API . Although based on the Navigation API, this function is implemented on top of the History API to allow for navigation without reloading the page.

`navigate()` does not perform sanitization on the `href` parameter. Sanitize user input if you use it to determine the URL to navigate to.

#### `history` option
 Section titled “history option”
 Type: `'auto' | 'push' | 'replace'`
 Default: `'auto'`

 Added in:
 `astro@3.2.0`

Defines how this navigation should be added to the browser history.

 `'push'`: the router will use `history.pushState` to create a new entry in the browser history.

- `'replace'`: the router will use `history.replaceState` to update the URL without adding a new entry into navigation.

- `'auto'` (default): the router will attempt `history.pushState`, but if the URL cannot be transitioned to, the current URL will remain with no changes to the browser history.

This option follows the `history` option from the browser Navigation API but simplified for the cases that can happen on an Astro project.

#### `formData` option
 Section titled “formData option”
 Type: `FormData`

 Added in:
 `astro@3.5.0`

A `FormData` object for `POST` requests.

When this option is provided, the requests to the navigation target page will be sent as a `POST` request with the form data object as the content.

Submitting an HTML form with view transitions enabled will use this method instead of the default navigation with page reload. Calling this method allows triggering the same behavior programmatically.

#### `info` option
 Section titled “info option”
 Type: `any`

 Added in:
 `astro@3.6.0`

Arbitrary data to be included in the `astro:before-preparation` and `astro:before-swap` events caused by this navigation.

This option mimics the `info` option from the browser Navigation API.

#### `state` option
 Section titled “state option”
 Type: `any`

 Added in:
 `astro@3.6.0`

Arbitrary data to be associated with the `NavigationHistoryEntry` object created by this navigation. This data can then be retrieved using the `history.getState` function from the History API.

This option mimics the `state` option from the browser Navigation API.

#### `sourceElement` option
 Section titled “sourceElement option”
 Type: `Element`

 Added in:
 `astro@3.6.0`

The element that triggered this navigation, if any. This element will be available in the following events:

- `astro:before-preparation`

- `astro:before-swap`

### `supportsViewTransitions`
 Section titled “supportsViewTransitions”
 Type: `boolean`

 Added in:
 `astro@3.2.0`

Whether or not view transitions are supported and enabled in the current browser.

### `transitionEnabledOnThisPage()`
 Section titled “transitionEnabledOnThisPage()”
 Type: `() => boolean`

 Added in:
 `astro@3.2.0`

Whether or not the current page has view transitions enabled for client-side navigation. This can be used to make components that behave differently when they are used on pages with view transitions.

### `getFallback()`
 Section titled “getFallback()”
 Type: `() => Fallback `
 Default: `animate`

 Added in:
 `astro@3.6.0`

Returns the fallback strategy to use (`animate` by default) in browsers that do not support view transitions.

 See the guide on Fallback control for how to choose and configure the fallback behavior.

### `swapFunctions`
 Section titled “swapFunctions”
 Type: `object`

 Added in:
 `astro@4.15.0`

An object containing the utility functions used to build Astro’s default swap function.
These can be useful when building a custom swap function .

`swapFunctions` provides the following methods:

#### `deselectScripts()`
 Section titled “deselectScripts()”
 Type: `(newDocument: Document) => void`

Marks scripts in the new document that should not be executed. Those scripts are already in the current document and are not flagged for re-execution using `data-astro-rerun` .

#### `swapRootAttributes()`
 Section titled “swapRootAttributes()”
 Type: `(newDocument: Document) => void`

Swaps the attributes between the document roots, like the `lang` attribute. This also includes Astro-injected internal attributes like `data-astro-transition`, which makes the transition direction available to Astro-generated CSS rules.

When making a custom swap function, it is important to call this function so as not to break the view transition’s animations.

#### `swapHeadElements()`
 Section titled “swapHeadElements()”
 Type: `(newDocument: Document) => void`

Removes every element from the current document’s `&#x3C;head>` that is not persisted to the new document. Then appends all new elements from the new document’s `&#x3C;head>` to the current document’s `&#x3C;head>`.

#### `saveFocus()`
 Section titled “saveFocus()”
 Type: `() => () => void`

Stores the element in focus on the current page and returns a function that when called, if the focused element was persisted, returns the focus to it.

#### `swapBodyElement()`
 Section titled “swapBodyElement()”
 Type: `(newBody: Element, oldBody: Element) => void`

Replaces the old body with the new body. Then, goes through every element in the old body that should be persisted and have a matching element in the new body and swaps the old element back in place.

### Deprecated imports
 Section titled “Deprecated imports”
 The following imports are deprecated in v6 and will be removed in v7. You can still use them in your project, but you may prefer to update your code now. See how to upgrade .

#### `isTransitionBeforePreparationEvent()`

 Type: `(value: any) => boolean`

 Added in:
 `astro@3.6.0`

Determines whether the given value matches a `TransitionBeforePreparationEvent` . This can be useful when you need to narrow the type of an event in an event listener.

 src/pages/index.astro ` --- ---
 &#x3C; script > import { isTransitionBeforePreparationEvent , TRANSITION_BEFORE_PREPARATION, } from " astro:transitions/client " ;
 function listener ( event : Event ) { const setting = isTransitionBeforePreparationEvent ( event ) ? 1 : 2 ; /* do something with setting */ }
 document . addEventListener ( TRANSITION_BEFORE_PREPARATION , listener ); &#x3C;/ script > `

#### `isTransitionBeforeSwapEvent()`

 Type: `(value: any) => boolean`

 Added in:
 `astro@3.6.0`

Determines whether the given value matches a `TransitionBeforeSwapEvent` . This can be useful when you need to narrow the type of an event in an event listener.

 src/pages/index.astro ` --- ---
 &#x3C; script > import { isTransitionBeforeSwapEvent , TRANSITION_BEFORE_SWAP, } from " astro:transitions/client " ;
 function listener ( event : Event ) { const setting = isTransitionBeforeSwapEvent ( event ) ? 1 : 2 ; /* do something with setting */ }
 document . addEventListener ( TRANSITION_BEFORE_SWAP , listener ); &#x3C;/ script > `

#### `TRANSITION_BEFORE_PREPARATION`

 Type: `'astro:before-preparation'`

 Added in:
 `astro@3.6.0`

A constant to avoid writing the `astro:before-preparation` event name in plain text when you define an event.

 src/pages/index.astro ` --- ---
 &#x3C; script > import { TRANSITION_BEFORE_PREPARATION } from " astro:transitions/client " ;
 document . addEventListener ( TRANSITION_BEFORE_PREPARATION , () => { /* the listener logic */ }); &#x3C;/ script > `

#### `TRANSITION_AFTER_PREPARATION`

 Type: `'astro:after-preparation'`

 Added in:
 `astro@3.6.0`

A constant to avoid writing the `astro:after-preparation` event name in plain text when you define an event.

 src/pages/index.astro ` --- ---
 &#x3C; script > import { TRANSITION_AFTER_PREPARATION } from " astro:transitions/client " ;
 document . addEventListener ( TRANSITION_AFTER_PREPARATION , () => { /* the listener logic */ }); &#x3C;/ script > `

#### `TRANSITION_BEFORE_SWAP`

 Type: `'astro:before-swap'`

 Added in:
 `astro@3.6.0`

A constant to avoid writing the `astro:before-swap` event name in plain text when you define an event.

 src/pages/index.astro ` --- ---
 &#x3C; script > import { TRANSITION_BEFORE_SWAP } from " astro:transitions/client " ;
 document . addEventListener ( TRANSITION_BEFORE_SWAP , () => { /* the listener logic */ }); &#x3C;/ script > `

#### `TRANSITION_AFTER_SWAP`

 Type: `'astro:after-swap'`

 Added in:
 `astro@3.6.0`

A constant to avoid writing the `astro:after-swap` event name in plain text when you define an event.

 src/pages/index.astro ` --- ---
 &#x3C; script > import { TRANSITION_AFTER_SWAP } from " astro:transitions/client " ;
 document . addEventListener ( TRANSITION_AFTER_SWAP , () => { /* the listener logic */ }); &#x3C;/ script > `

#### `TRANSITION_PAGE_LOAD`

 Type: `'astro:page-load'`

 Added in:
 `astro@3.6.0`

A constant to avoid writing the `astro:page-load` event name in plain text when you define an event.

 src/pages/index.astro ` --- ---
 &#x3C; script > import { TRANSITION_PAGE_LOAD } from " astro:transitions/client " ;
 document . addEventListener ( TRANSITION_PAGE_LOAD , () => { /* the listener logic */ }); &#x3C;/ script > `

## `astro:transitions/client` types
 Section titled “astro:transitions/client types”

```
` import type { Direction, Fallback, NavigationTypeString, Options, TransitionBeforePreparationEvent, TransitionBeforeSwapEvent, } from ' astro:transitions/client ' ; `
```

### `Direction`
 Section titled “Direction”
 Type: `'forward' | 'back'`

 Added in:
 `astro@3.2.0`

A union of animation directions:

- `forward`: navigating to the next page in the history or to a new page.

- `back`: navigating to the previous page in the history.

### `Fallback`
 Section titled “Fallback”
 Type: `'none' | 'animate' | 'swap'`

 Added in:
 `astro@3.2.0`

A union of fallback strategies to use in browsers that do not support view transitions:

- `animate`: Astro will simulate view transitions using custom attributes before updating page content.

- `swap`: Astro will not attempt to animate the page. Instead, the old page will be immediately replaced by the new one.

- `none`: Astro will not do any animated page transitions at all. Instead, you will get full page navigation in non-supporting browsers.

 Learn more about controlling the fallback strategy with the `ClientRouter`.

### `NavigationTypeString`
 Section titled “NavigationTypeString”
 Type: `'push' | 'replace' | 'traverse'`

 Added in:
 `astro@3.6.0`

A union of supported history navigation events.

### `TransitionBeforePreparationEvent`
 Section titled “TransitionBeforePreparationEvent”
 Type: `Event`

 Added in:
 `astro@3.6.0`

Represents an `astro:before-preparation` event . This can be useful to type the event received by a listener:

 src/pages/index.astro ` --- ---
 &#x3C; script > import type { TransitionBeforePreparationEvent } from " astro:transitions/client " ;
 function listener ( event : TransitionBeforePreparationEvent ) { /* do something */ }
 document . addEventListener ( " astro:before-preparation " , listener ); &#x3C;/ script > `

### `TransitionBeforeSwapEvent`
 Section titled “TransitionBeforeSwapEvent”
 Type: `Event`

 Added in:
 `astro@3.6.0`

Represents an `astro:before-swap` event . This can be useful to type the event received by a listener:

 src/pages/index.astro ` --- ---
 &#x3C; script > import type { TransitionBeforeSwapEvent } from " astro:transitions/client " ;
 function listener ( event : TransitionBeforeSwapEvent ) { /* do something */ }
 document . addEventListener ( " astro:before-swap " , listener ); &#x3C;/ script > `

## Lifecycle events
 Section titled “Lifecycle events”

### `astro:before-preparation` event
 Section titled “astro:before-preparation event”
 Type: `TransitionBeforePreparationEvent`

 Added in:
 `astro@3.6.0`

An event dispatched at the beginning of a navigation using the View Transitions router. This event happens before any request is made and any browser state is changed.

This event has the attributes:

- `info`

- `sourceElement`

- `navigationType`

- `direction`

- `from`

- `to`

- `formData`

- `loader()`

 Read more about how to use this event on the View Transitions guide .

### `astro:after-preparation` event
 Section titled “astro:after-preparation event”
 Type: `Event`

 Added in:
 `astro@3.6.0`

An event dispatched after the next page in a navigation using View Transitions router is loaded.

This event has no attributes.

 Read more about how to use this event on the View Transitions guide .

### `astro:before-swap` event
 Section titled “astro:before-swap event”
 Type: `TransitionBeforeSwapEvent`

 Added in:
 `astro@3.6.0`

An event dispatched after the next page is parsed, prepared, and linked into a document in preparation for the transition but before any content is swapped between the documents.

This event can’t be canceled. Calling `preventDefault()` is a no-op.

This event has the attributes:

- `info`

- `sourceElement`

- `navigationType`

- `direction`

- `from`

- `to`

- `viewTransition`

- `swap()`

 Read more about how to use this event on the View Transitions guide .

### `astro:after-swap` event
 Section titled “astro:after-swap event”
 Type: `Event`

An event dispatched after the contents of the page have been swapped but before the view transition ends.

The history entry and scroll position have already been updated when this event is triggered.

### `astro:page-load` event
 Section titled “astro:page-load event”
 Type: `Event`

An event dispatched after a page completes loading, whether from a navigation using view transitions or native to the browser.

When view transitions is enabled on the page, code that would normally execute on `DOMContentLoaded` should be changed to execute on this event.

### Lifecycle events attributes
 Section titled “Lifecycle events attributes”

 Added in:
 `astro@3.6.0`

The following attributes are common to both the `astro:before-preparation` and `astro:before-swap` events, except for some that are only available with one or the other.

#### `info`
 Section titled “info”
 Type: `any`

Arbitrary data defined during navigation.

This is the literal value passed on the `info` option of the `navigate()` function .

#### `sourceElement`
 Section titled “sourceElement”
 Type: `Element | undefined`

The element that triggered the navigation. This can be, for example, an `&#x3C;a>` element that was clicked.

When using the `navigate()` function , this will be the element specified in the call.

#### `newDocument`
 Section titled “newDocument”
 Type: `Document`

The document for the next page in the navigation. The contents of this document will be swapped in place of the contents of the current document.

#### `navigationType`
 Section titled “navigationType”
 Type: `NavigationTypeString`

Which kind of history navigation is happening.

- `push`: a new `NavigationHistoryEntry` is being created for the new page.

- `replace`: the current `NavigationHistoryEntry` is being replaced with an entry for the new page.

- `traverse`: no `NavigationHistoryEntry` is created. The position in the history is changing. The direction of the traversal is given on the `direction` attribute .

#### `direction`
 Section titled “direction”
 Type: `string`

The direction of the transition:

- In an `astro:before-preparation` event , this can be used to define custom directions. The property is writable and accepts any string.

- In an `astro:before-swap` event , this can be used to retrieve the transition direction. The property is readonly and its value can be a predefined `Direction` or any string that an `astro:before-preparation` event listener might have set.

#### `from`
 Section titled “from”
 Type: `URL`

The URL of the page initiating the navigation.

#### `to`
 Section titled “to”
 Type: `URL`

The URL of the page being navigated to. This property can be modified, the value at the end of the lifecycle will be used in the `NavigationHistoryEntry` for the next page.

#### `formData`
 Section titled “formData”
 Type: `FormData | undefined`
 Available in: `astro:before-preparation` event

When set, a `POST` request will be sent to the `to` URL with the given `FormData` object as the content instead of the normal `GET` request.

When submitting an HTML form with view transitions enabled, this field is automatically set to the data in the form. When using the `navigate()` function , this value is the same as given in the options.

#### `loader()`
 Section titled “loader()”
 Type: `() => Promise&#x3C;void>`
 Available in: `astro:before-preparation` event

Implementation of the following phase in the navigation (loading the next page). This implementation can be overridden to add extra behavior.

#### `viewTransition`
 Section titled “viewTransition”
 Type: `ViewTransition`
 Available in: `astro:before-swap` event

The view transition object used in this navigation. On browsers that do not support the View Transitions API , this is an object implementing the same API for convenience but without the DOM integration.

#### `swap()`
 Section titled “swap()”
 Type: `() => void`
 Available in: `astro:before-swap` event

Calls the default document swap logic. By default, this implementation will call the following functions in order:

- `deselectScripts()`

- `swapRootAttributes()`

- `swapHeadElements()`

- `saveFocus()`

- `swapBodyElement()`

 Read more about building a custom swap function in the View Transitions guide.

 Reference

 Contribute

 Community

 Sponsor

## Astro Zod

# Zod API Reference

 Zod is a TypeScript-based schema declaration and validation library. This allows you to define schemas you can use to validate data and transform data, from a simple type (e.g. `string`, `number`) to complex data structures (e.g. nested objects).

The `astro/zod` module exposes a re-export of Zod that gives you access to all the features of Zod v4. By using this module, you do not need to install Zod yourself. This also ensures that your project uses the same API versions as Astro when using features such as Content Collections or Actions .

 See the Zod website for complete documentation on how Zod works and what features are available.

## Imports from `astro/zod`
 Section titled “Imports from astro/zod”

```
` import { z } from ' astro/zod ' ; `
```

### `z`
 Section titled “z”
 Type: `object`

The `z` utility gives you access to validators for a wide range of data types, methods and types for working with your data.

 Learn more about the `z` utility in Zod documentation

#### Common data type validators
 Section titled “Common data type validators”
 With Zod, you can validate any type of data, such as primitives , objects , arrays and more.

The following example shows a cheatsheet of many common Zod data types to create a `user` schema:

 ` import { z } from ' astro/zod ' ;
 const user = z . object ( { username: z . string () , name: z . string () . min ( 2 ) , email: z . email () , role: z . enum ([ " admin " , " editor " ]) , language: z . enum ([ " en " , " fr " , " es " ]) . default ( " en " ) , hobbies: z . array (z . string ()) , age: z . number () , isEmailConfirmed: z . boolean () , inscriptionDate: z . date () , website: z . url () . optional () , } ); `

#### Extracting a TypeScript type
 Section titled “Extracting a TypeScript type”
 Zod allows you to create a TypeScript type from any schema using Zod type inference . This can be useful for describing an expected data structure when defining component props .

The following example create a `User` type based on the previous schema:

 ` type User = z . infer &#x3C; typeof user>;
 /* The `User` type will be: * type User = { * username: string; * name: string; * email: string; * role: "admin" | "editor"; * language: "en" | "fr" | "es"; * hobbies: string[]; * age: number; * isEmailConfirmed: boolean; * inscriptionDate: Date; * website?: string | undefined; * } */ ` ;/* The &#x60;User&#x60; type will be: * type User = { * username: string; * name: string; * email: string; * role: &#x22;admin&#x22; | &#x22;editor&#x22;; * language: &#x22;en&#x22; | &#x22;fr&#x22; | &#x22;es&#x22;; * hobbies: string[]; * age: number; * isEmailConfirmed: boolean; * inscriptionDate: Date; * website?: string | undefined; * } */">

#### Using Zod methods
 Section titled “Using Zod methods”
 Zod provides various schema methods to customize error messages , transform data , or create custom validation logics .

 ` // Customize the error message const nonEmptyStrings = z . array (z . string ()) . nonempty ( " Can't be empty! " );
 // Validate a data from a schema nonEmptyStrings . parse ([]); // will throws our custom error
 // Create an object from a URL for a decorative img const decorativeImg = z . string () . transform ( ( value ) => { return { src: value , alt: "" }; } );
 // Create a custom validator and error message for a string const constrainedString = z . string () . refine ( ( val ) => val . length > 0 &#x26;&#x26; val . length &#x3C;= 255 , { error: " Must be between 1 and 255 characters. " , }); ` { return { src: value, alt: &#x22;&#x22; };});// Create a custom validator and error message for a stringconst constrainedString = z .string() .refine((val) => val.length > 0 &#x26;&#x26; val.length

### Individual imports
 Section titled “Individual imports”
 Alternatively, you can import all the Zod validators, methods and types available in the `z` utility directly from the module.

The following example imports `coerce` to create a `Date` object from a date string:

```
` import { coerce } from ' astro/zod ' ;
 const publishedOn = coerce . date (); const publicationDate = publishedOn . parse ( " 2025-12-03 " ); `
```

 Reference

 Contribute

 Community

 Sponsor