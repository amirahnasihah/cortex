# Astro - Template Syntax


## Astro Syntax

# Template expressions reference

 Astro component syntax is a superset of HTML. The syntax was designed to feel familiar to anyone with experience writing HTML or JSX, and adds support for including components and JavaScript expressions.

## JSX-like Expressions
 Section titled “JSX-like Expressions”
 You can define local JavaScript variables inside of the frontmatter component script between the two code fences (`---`) of an Astro component. You can then inject these variables into the component’s HTML template using JSX-like expressions!

### Variables
 Section titled “Variables”
 Local variables can be added into the HTML using the curly braces syntax:

 - src/components/Variables.astro ` --- const name = " Astro " ; --- &#x3C; div > &#x3C; h1 > Hello { name } ! &#x3C;/ h1 > &#x3C;!-- Outputs &#x3C;h1>Hello Astro!&#x3C;/h1> --> &#x3C;/ div > ` 
# Hello {name}!
  ">

### Dynamic Attributes
 Section titled “Dynamic Attributes”
 Local variables can be used in curly braces to pass attribute values to both HTML elements and components:

 src/components/DynamicAttributes.astro ` --- const name = " Astro " ; --- &#x3C; h1 class = { name } > Attribute expressions are supported &#x3C;/ h1 >
 &#x3C; MyComponent templateLiteralNameAttribute = { ` MyNameIs ${ name } ` } /> ` ">

### Dynamic HTML
 Section titled “Dynamic HTML”
 Local variables can be used in JSX-like functions to produce dynamically-generated HTML elements:

 src/components/DynamicHtml.astro ` --- const items = [ " Dog " , " Cat " , " Platypus " ]; --- &#x3C; ul > { items . map ( ( item ) => ( &#x3C; li > { item } &#x3C;/ li > )) } &#x3C;/ ul > `  {items.map((item) => ( {item}
 ))} ">
 Astro can conditionally display HTML using JSX logical operators and ternary expressions.

 src/components/ConditionalHtml.astro ` --- const visible = true ; --- { visible &#x26;&#x26; &#x3C; p > Show me! &#x3C;/ p > }
 { visible ? &#x3C; p > Show me! &#x3C;/ p > : &#x3C; p > Else show me! &#x3C;/ p > } ` Show me!
}{visible ? Show me!
 : Else show me!
}">

### Dynamic Tags
 Section titled “Dynamic Tags”
 You can also use dynamic tags by assigning an HTML tag name to a variable or with a component import reassignment:

 src/components/DynamicTags.astro ` --- import MyComponent from " ./MyComponent.astro " ; const Element = ' div ' const Component = MyComponent; --- &#x3C; Element > Hello! &#x3C;/ Element > &#x3C;!-- renders as &#x3C;div>Hello!&#x3C;/div> --> &#x3C; Component /> &#x3C;!-- renders as &#x3C;MyComponent /> --> ` Hello!  ">
 When using dynamic tags:

-
 Variable names must be capitalized. For example, use `Element`, not `element`. Otherwise, Astro will try to render your variable name as a literal HTML tag.

-
 Hydration directives are not supported. When using `client:*` hydration directives , Astro needs to know which components to bundle for production, and the dynamic tag pattern prevents this from working.

-
 The define:vars directive is not supported. If you cannot wrap the children with an extra element (e.g `&#x3C;div>`), then you can manually add a `style={`--myVar:${value}`}` to your Element.

### Fragments
 Section titled “Fragments”
 Astro supports `&#x3C;> &#x3C;/>` notation and also provides a built-in `&#x3C;Fragment />` component. This component can be useful to avoid wrapper elements when adding `set:*` directives to inject an HTML string.

The following example renders paragraph text using the `&#x3C;Fragment />` component:

 src/components/SetHtml.astro ` --- const htmlString = ' &#x3C;p>Raw HTML content&#x3C;/p> ' ; --- &#x3C; Fragment set:html = { htmlString } /> ` Raw HTML content
&#x27;;--- ">

### Differences between Astro and JSX
 Section titled “Differences between Astro and JSX”
 Astro component syntax is a superset of HTML. It was designed to feel familiar to anyone with HTML or JSX experience, but there are a couple of key differences between `.astro` files and JSX.

#### Attributes
 Section titled “Attributes”
 In Astro, you use the standard `kebab-case` format for all HTML attributes instead of the `camelCase` used in JSX. This even works for `class`, which is not supported by React.

 example.astro ` &#x3C; div className = " box " dataValue = " 3 " /> &#x3C; div class = " box " data-value = " 3 " /> `  ">

#### Multiple Elements
 Section titled “Multiple Elements”
 An Astro component template can render multiple elements with no need to wrap everything in a single `&#x3C;div>` or `&#x3C;>`, unlike JavaScript or JSX.

 src/components/RootElements.astro ` --- // Template with multiple elements --- &#x3C; p > No need to wrap elements in a single containing element. &#x3C;/ p > &#x3C; p > Astro supports multiple root elements in a template. &#x3C;/ p > ` No need to wrap elements in a single containing element.
Astro supports multiple root elements in a template.
">

#### Comments
 Section titled “Comments”
 In Astro, you can use standard HTML comments or JavaScript-style comments.

 example.astro ` --- --- &#x3C;!-- HTML comment syntax is valid in .astro files --> { /* JS comment syntax is also valid */ } `

## Component utilities
 Section titled “Component utilities”

### `Astro.slots`
 Section titled “Astro.slots”
 `Astro.slots` contains utility functions for modifying an Astro component’s slotted children.

#### `Astro.slots.has()`
 Section titled “Astro.slots.has()”
 Type: `(slotName: string) => boolean`

You can check whether content for a specific slot name exists with `Astro.slots.has()`. This can be useful when you want to wrap slot contents but only want to render the wrapper elements when the slot is being used.

 src/pages/index.astro ` --- --- &#x3C; slot />
 { Astro . slots . has ( ' more ' ) &#x26;&#x26; ( &#x3C; aside > &#x3C; h2 > More &#x3C;/ h2 > &#x3C; slot name = " more " /> &#x3C;/ aside > ) } ` {Astro.slots.has(&#x27;more&#x27;) &#x26;&#x26; ( )}">

#### `Astro.slots.render()`
 Section titled “Astro.slots.render()”
 Type: `(slotName: string, args?: any[]) => Promise&#x3C;string>`

You can asynchronously render the contents of a slot to a string of HTML using `Astro.slots.render()`.

 ` --- const html = await Astro . slots . render ( ' default ' ); --- &#x3C; Fragment set:html = { html } /> ` ">

 `Astro.slots.render()` optionally accepts a second argument: an array of parameters that will be forwarded to any function children. This can be useful for custom utility components.

For example, this `&#x3C;Shout />` component converts its `message` prop to uppercase and passes it to the default slot:

 src/components/Shout.astro ` --- const message = Astro . props . message . toUpperCase (); let html = '' ; if (Astro . slots . has ( ' default ' )) { html = await Astro . slots . render ( ' default ' , [message]) ; } --- &#x3C; Fragment set:html = { html } /> ` ">
 A callback function passed as `&#x3C;Shout />`’s child will receive the all-caps `message` parameter:

 src/pages/index.astro ` --- import Shout from " ../components/Shout.astro " ; --- &#x3C; Shout message = " slots! " > { ( message ) => &#x3C; div > { message } &#x3C;/ div > } &#x3C;/ Shout >
 &#x3C;!-- renders as &#x3C;div>SLOTS!&#x3C;/div> --> `  {(message) => {message} } ">
 Callback functions can be passed to named slots inside a wrapping HTML element tag with a `slot` attribute. This element is only used to transfer the callback to a named slot and will not be rendered onto the page.

 ` &#x3C; Shout message = " slots! " > &#x3C; fragment slot = " message " > { ( message ) => &#x3C; div > { message } &#x3C;/ div > } &#x3C;/ fragment > &#x3C;/ Shout > `   {(message) => {message} }  ">
 Use a standard HTML element for the wrapping tag or any lowercase tag (e.g. `&#x3C;fragment>` instead of `&#x3C;Fragment />`) that will not be interpreted as a component. Do not use the HTML `&#x3C;slot>` element as this will be interpreted as an Astro slot.

### `Astro.self`
 Section titled “Astro.self”
 `Astro.self` allows Astro components to be recursively called. This behavior lets you render an Astro component from within itself by using `&#x3C;Astro.self>` in the component template. This can help iterate over large data stores and nested data structures.

 NestedList.astro ` --- const { items } = Astro . props ; --- &#x3C; ul class = " nested-list " > { items . map ( ( item ) => ( &#x3C; li > &#x3C;!-- If there is a nested data-structure we render ` &#x3C; Astro.self > ` --> &#x3C;!-- and can pass props through with the recursive call --> { Array . isArray (item) ? ( &#x3C; Astro.self items = { item } /> ) : ( item ) } &#x3C;/ li > ))} &#x3C;/ ul > `  {items.map((item) => ( -    {Array.isArray(item) ? (  ) : ( item )}
 ))} ">
 This component could then be used like this:

 ` --- import NestedList from ' ./NestedList.astro ' ; --- &#x3C; NestedList items = { [ ' A ' , [ ' B ' , ' C ' ], ' D ' ] } /> ` ">
 And would render HTML like this:

```
` &#x3C; ul class = " nested-list " > &#x3C; li > A &#x3C;/ li > &#x3C; li > &#x3C; ul class = " nested-list " > &#x3C; li > B &#x3C;/ li > &#x3C; li > C &#x3C;/ li > &#x3C;/ ul > &#x3C;/ li > &#x3C; li > D &#x3C;/ li > &#x3C;/ ul > `
```
  - A
 -   B
 - C
   - D
 ">

 Reference

 Contribute

 Community

 Sponsor

## Directives Reference

# Template directives reference

 Template directives are a special kind of HTML attribute available inside of any Astro component template (`.astro` files), and some can also be used in `.mdx` files.

Template directives are used to control an element or component’s behavior in some way. A template directive could enable some compiler feature that makes your life easier (like using `class:list` instead of `class`). Or, a directive could tell the Astro compiler to do something special with that component (like hydrating with `client:load`).

This page describes all of the template directives available to you in Astro, and how they work.

## Rules
 Section titled “Rules”
 For a template directive to be valid, it must:

- Include a colon `:` in its name, using the form `X:Y` (ex: `client:load`).

- Be visible to the compiler (ex: `&#x3C;X {...attr}>` would not work if `attr` contained a directive).

Some template directives, but not all, can take a custom value:

- `&#x3C;X client:load />` (takes no value)

- `&#x3C;X class:list={['some-css-class']} />` (takes an array)

A template directive is never included directly in the final HTML output of a component.

## Common Directives
 Section titled “Common Directives”

### `class:list`
 Section titled “class:list”
 `class:list={...}` takes an array of class values and converts them into a class string. This is powered by @lukeed’s popular clsx helper library.

`class:list` takes an array of several different possible value kinds:

- `string`: Added to the element `class`

- `Object`: All truthy keys are added to the element `class`

- `Array`: flattened

- `false`, `null`, or `undefined`: skipped

 ` &#x3C;!-- This --> &#x3C; span class:list = { [ ' hello goodbye ' , { world: true }, [ ' friend ' ] ] } /> &#x3C;!-- Becomes --> &#x3C; span class = " hello goodbye world friend " >&#x3C;/ span > `  ">

### `set:html`
 Section titled “set:html”
 `set:html={string}` injects an HTML string into an element, similar to setting `el.innerHTML`.

 The value is not automatically escaped by Astro! Be sure that you trust the value, or that you have escaped it manually before passing it to the template. Forgetting to do this will open you up to Cross Site Scripting (XSS) attacks.

 ` --- const rawHTMLString = " Hello &#x3C;strong>World&#x3C;/strong> " --- &#x3C; h1 > { rawHTMLString } &#x3C;/ h1 > &#x3C;!-- Output: &#x3C;h1>Hello &#x26;lt;strong&#x26;gt;World&#x26;lt;/strong&#x26;gt;&#x3C;/h1> --> &#x3C; h1 set:html = { rawHTMLString } /> &#x3C;!-- Output: &#x3C;h1>Hello &#x3C;strong>World&#x3C;/strong>&#x3C;/h1> --> ` World &#x22;---
# {rawHTMLString}
   ">
 You can also use `set:html` on a `&#x3C;Fragment>` to avoid adding an unnecessary wrapper element. This can be especially useful when fetching HTML from a CMS.

 ` --- const cmsContent = await fetchHTMLFromMyCMS (); --- &#x3C; Fragment set:html = { cmsContent } > ` ">
 `set:html={Promise&#x3C;string>}` injects an HTML string into an element that is wrapped in a Promise.

This can be used to inject HTML stored externally, such as in a database.

 ` --- import api from ' ../db/api.js ' ; --- &#x3C; article set:html = { api . getArticle (Astro . props . id ) } >&#x3C;/ article > ` ">
 `set:html={Promise&#x3C;Response>}` injects a Response into an element.

This is most helpful when using `fetch()`. For example, fetching old posts from a previous static-site generator.

 ` &#x3C; article set:html = { fetch ( ' http://example/old-posts/making-soup.html ' ) } >&#x3C;/ article > ` ">
 `set:html` can be used on any tag and does not have to include HTML. For example, use with `JSON.stringify()` on a `&#x3C;script>` tag to add a JSON-LD schema to your page.

 ` &#x3C; script type = " application/ld+json " set:html = { JSON . stringify ( { " @context " : " https://schema.org/ " , " @type " : " Person " , name: " Houston " , hasOccupation: { " @type " : " Occupation " , name: " Astronaut " } } ) } /> `

 See how client-side scripts work in Astro components.

### `define:vars`
 Section titled “define:vars”
 `define:vars={...}` can pass server-side variables from your component frontmatter into the client `&#x3C;script>` or `&#x3C;style>` tags. Any JSON-serializable frontmatter variable is supported, including `props` passed to your component through `Astro.props`. Values are serialized with `JSON.stringify()` .

 ` --- const foregroundColor = " rgb(221 243 228) " ; const backgroundColor = " rgb(24 121 78) " ; const message = " Astro is awesome! " ; --- &#x3C; style define:vars = { { textColor: foregroundColor , backgroundColor } } > h1 { background-color : var ( --backgroundColor ); color : var ( --textColor ); } &#x3C;/ style >
 &#x3C; script define:vars = { { message } } > alert ( message ); &#x3C;/ script > `

## Advanced Directives
 Section titled “Advanced Directives”

### `is:raw`
 Section titled “is:raw”
 `is:raw` instructs the Astro compiler to treat any children of that element as text. This means that all special Astro templating syntax will be ignored inside of this component.

For example, if you had a custom Katex component that converted some text to HTML, you could have users do this:

```
` --- import Katex from ' ../components/Katex.astro ' ; --- &#x3C; Katex is:raw > Some conflicting {syntax} here &#x3C;/ Katex > `
```
 Some conflicting {syntax} here ">

 Reference

 Contribute

 Community

 Sponsor