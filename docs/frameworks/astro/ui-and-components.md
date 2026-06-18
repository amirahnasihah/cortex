# Astro - UI & Components


## Astro Components

# Components

 Astro components are the basic building blocks of any Astro project. They are HTML-only templating components with no client-side runtime and use the `.astro` file extension.

Astro components are extremely flexible. An Astro component can be as small as a snippet of HTML, like a collection of common `&#x3C;meta>` tags that make SEO easy to work with. Components can be reusable UI elements, like a header or a profile card. Astro components can even contain an entire page layout or, when located in the special `src/pages/` folder, be an entire page itself.

The most important thing to know about Astro components is that they don’t render on the client . They render to HTML either at build-time or on-demand. You can include JavaScript code inside of your component frontmatter, and all of it will be stripped from the final page sent to your users’ browsers. The result is a faster site, with zero JavaScript footprint added by default.

When your Astro component does need client-side interactivity, you can add standard HTML `&#x3C;script>` tags or UI Framework components as “client islands”.

For components that need to render personalized or dynamic content, you can defer their server rendering by adding a server directive . These “server islands” will render their content when it is available, without delaying the entire page load.

## Component Structure
 Section titled “Component Structure”
 An Astro component is made up of two main parts: the Component Script and the Component Template . Each part performs a different job, but together they provide a framework that is both easy to use and expressive enough to handle whatever you might want to build.

 - src/components/EmptyComponent.astro ` --- // Component Script (JavaScript) --- &#x3C;!-- Component Template (HTML + JS Expressions) --> `

### The Component Script
 Section titled “The Component Script”
 Astro uses a code fence (`---`) to identify the component script in your Astro component. If you’ve ever written Markdown before, you may already be familiar with a similar concept called frontmatter. Astro’s idea of a component script was directly inspired by this concept.

You can use the component script to write any JavaScript code that you need to render your template. This can include:

 importing other Astro components

- importing other framework components, like React

- importing data, like a JSON file

- fetching content from an API or database

- creating variables that you will reference in your template

 src/components/MyComponent.astro ` --- import SomeAstroComponent from ' ../components/SomeAstroComponent.astro ' ; import SomeReactComponent from ' ../components/SomeReactComponent.jsx ' ; import someData from ' ../data/pokemon.json ' ;
 // Access passed-in component props, like `&#x3C;X title="Hello, World" />` const { title } = Astro . props ;
 // Fetch external data, even from a private API or database const data = await fetch ( ' SOME_SECRET_API_URL/users ' ) . then ( r => r . json ()); --- &#x3C;!-- Your template here! --> ` &#x60;const { title } = Astro.props;// Fetch external data, even from a private API or databaseconst data = await fetch(&#x27;SOME_SECRET_API_URL/users&#x27;).then(r => r.json());---">
 The code fence is designed to guarantee that the JavaScript that you write in it is “fenced in.” It won’t escape into your frontend application, or fall into your user’s hands. You can safely write code here that is expensive or sensitive (like a call to your private database) without worrying about it ever ending up in your user’s browser.

### The Component Template
 Section titled “The Component Template”
 The component template is below the code fence and determines the HTML output of your component.

If you write plain HTML here, your component will render that HTML in any Astro page it is imported and used.

However, Astro’s component template syntax also supports JavaScript expressions , Astro `&#x3C;style>` and `&#x3C;script>` tags, imported components , and special Astro directives . Data and values defined in the component script can be used in the component template to produce dynamically-created HTML.

 src/components/MyFavoritePokemon.astro ` --- // Your component script here! import Banner from ' ../components/Banner.astro ' ; import Avatar from ' ../components/Avatar.astro ' ; import ReactPokemonComponent from ' ../components/ReactPokemonComponent.jsx ' ; const myFavoritePokemon = [ /* ... */ ]; const { title } = Astro . props ; --- &#x3C;!-- HTML comments supported! --> { /* JS comment syntax is also valid! */ }
 &#x3C; Banner /> &#x3C; h1 > Hello, world! &#x3C;/ h1 >
 &#x3C;!-- Use props and other variables from the component script: --> &#x3C; p > { title } &#x3C;/ p >
 &#x3C;!-- Delay component rendering and provide fallback loading content: --> &#x3C; Avatar server:defer > &#x3C; svg slot = " fallback " class = " generic-avatar " transition:name = " avatar " > ... &#x3C;/ svg > &#x3C;/ Avatar >
 &#x3C;!-- Include other UI framework components with a `client:` directive to hydrate: --> &#x3C; ReactPokemonComponent client:visible />
 &#x3C;!-- Mix HTML with JavaScript expressions, similar to JSX: --> &#x3C; ul > { myFavoritePokemon . map ( ( data ) => &#x3C; li > { data . name } &#x3C;/ li > ) } &#x3C;/ ul >
 &#x3C;!-- Use a template directive to build class names from multiple strings or even objects! --> &#x3C; p class:list = { [ " add " , " dynamic " , { classNames: true }] } /> ` 
# Hello, world!
 {title}
  ...     {myFavoritePokemon.map((data) => - {data.name}
)} ">

## Component-based design
 Section titled “Component-based design”
 Components are designed to be reusable and composable . You can use components inside of other components to build more and more advanced UI. For example, a `Button` component could be used to create a `ButtonGroup` component:

 src/components/ButtonGroup.astro ` --- import Button from ' ./Button.astro ' ; --- &#x3C; div > &#x3C; Button title = " Button 1 " /> &#x3C; Button title = " Button 2 " /> &#x3C; Button title = " Button 3 " /> &#x3C;/ div > `     ">

## Component Props
 Section titled “Component Props”
 An Astro component can define and accept props. These props then become available to the component template for rendering HTML. Props are available on the `Astro.props` global in your frontmatter script.

Here is an example of a component that receives a `greeting` prop and a `name` prop. Notice that the props to be received are destructured from the global `Astro.props` object.

 src/components/GreetingHeadline.astro ` --- // Usage: &#x3C;GreetingHeadline greeting="Howdy" name="Partner" /> const { greeting , name } = Astro . props ; --- &#x3C; h2 > { greeting } , { name } ! &#x3C;/ h2 > ` const { greeting, name } = Astro.props;---
## {greeting}, {name}!
">
 This component, when imported and rendered in other Astro components, layouts or pages, can pass these props as attributes:

 src/components/GreetingCard.astro ` --- import GreetingHeadline from ' ./GreetingHeadline.astro ' ; const name = ' Astro ' ; --- &#x3C; h1 > Greeting Card &#x3C;/ h1 > &#x3C; GreetingHeadline greeting = " Hi " name = { name } /> &#x3C; p > I hope you have a wonderful day! &#x3C;/ p > `  I hope you have a wonderful day!
">
You can also define your props with TypeScript with a `Props` type interface. Astro will automatically pick up the `Props` interface in your frontmatter and give type warnings/errors. These props can also be given default values when destructured from `Astro.props`.

 src/components/GreetingHeadline.astro ` --- interface Props { name : string ; greeting ?: string ; }
 const { greeting = " Hello " , name } = Astro . props ; --- &#x3C; h2 > { greeting } , { name } ! &#x3C;/ h2 > `
 Component props can be given default values to use when none are provided.

 src/components/GreetingHeadline.astro ` --- const { greeting = " Hello " , name = " Astronaut " } = Astro . props ; --- &#x3C; h2 > { greeting } , { name } ! &#x3C;/ h2 > `

## Slots
 Section titled “Slots”
 The `&#x3C;slot />` element is a placeholder for external HTML content, allowing you to inject (or “slot”) child elements from other files into your component template.

By default, all child elements passed to a component will be rendered in its `&#x3C;slot />`.

 src/components/Wrapper.astro
```
` --- import Header from ' ./Header.astro ' ; import Logo from ' ./Logo.astro ' ; import Footer from ' ./Footer.astro ' ;
 const { title } = Astro . props ; --- &#x3C; div id = " content-wrapper " > &#x3C; Header /> &#x3C; Logo /> &#x3C; h1 > { title } &#x3C;/ h1 > &#x3C; slot /> &#x3C;!-- children will go here --> &#x3C; Footer /> &#x3C;/ div > `
```
   
# {title}
 

 Contribute

 Community

 Sponsor

## Layouts

# Layouts

 Layouts are Astro components used to provide a reusable UI structure, such as a page template.

We conventionally use the term “layout” for Astro components that provide common UI elements shared across pages such as headers, navigation bars, and footers. A typical Astro layout component provides Astro, Markdown or MDX pages with:

- a page shell (`&#x3C;html>`, `&#x3C;head>` and `&#x3C;body>` tags)

- a `&#x3C;slot />` to specify where individual page content should be injected.

But, there is nothing special about a layout component! They can accept props and import and use other components like any other Astro component. They can include UI frameworks components and client-side scripts . They do not even have to provide a full page shell, and can instead be used as partial UI templates.

However, if a layout component does contain a page shell, its `&#x3C;html>` element must be the parent of all other elements in the component.

Layout components are commonly placed in a `src/layouts` directory in your project for organization, but this is not a requirement; you can choose to place them anywhere in your project. You can even colocate layout components alongside your pages by prefixing the layout names with `_` .

## Sample Layout
 Section titled “Sample Layout”
 src/layouts/MySiteLayout.astro
```
` --- import BaseHead from ' ../components/BaseHead.astro ' ; import Footer from ' ../components/Footer.astro ' ; const { title } = Astro . props ; --- &#x3C; html lang = " en " > &#x3C; head > &#x3C; meta charset = " utf-8 " > &#x3C; meta name = " viewport " content = " width=device-width, initial-scale=1 " > &#x3C; BaseHead title = { title } /> &#x3C;/ head > &#x3C; body > &#x3C; nav > &#x3C; a href = " # " > Home &#x3C;/ a > &#x3C; a href = " # " > Posts &#x3C;/ a > &#x3C; a href = " # " > Contact &#x3C;/ a > &#x3C;/ nav > &#x3C; h1 > { title } &#x3C;/ h1 > &#x3C; article > &#x3C; slot /> &#x3C;!-- your content is injected here --> &#x3C;/ article > &#x3C; Footer /> &#x3C;/ body > &#x3C; style > h1 { font-size : 2 rem ; } &#x3C;/ style > &#x3C;/ html > `
```
        
# {title}
   

 Contribute

 Community

 Sponsor

## Styling

# Styles and CSS

 Astro was designed to make styling and writing CSS a breeze. Write your own CSS directly inside of an Astro component or import your favorite CSS library like Tailwind . Advanced styling languages like Sass and Less are also supported.

## Styling in Astro
 Section titled “Styling in Astro”
 Styling an Astro component is as easy as adding a `&#x3C;style>` tag to your component or page template. When you place a `&#x3C;style>` tag inside of an Astro component, Astro will detect the CSS and handle your styles for you, automatically.

 - src/components/MyComponent.astro ` &#x3C; style > h1 { color : red ; } &#x3C;/ style > `

### Scoped Styles
 Section titled “Scoped Styles”
 Astro `&#x3C;style>` CSS rules are automatically scoped by default . Scoped styles are compiled behind-the-scenes to only apply to HTML written inside of that same component. The CSS that you write inside of an Astro component is automatically encapsulated inside of that component.

This CSS:

 src/pages/index.astro ` &#x3C; style > h1 { color : red ; }
 .text { color : blue ; } &#x3C;/ style > `
 Compiles to this:

 ` &#x3C; style > h1 [ data-astro-cid-hhnqfkh6 ] { color : red ; }
 .text [ data-astro-cid-hhnqfkh6 ] { color : blue ; } &#x3C;/ style > `
 Scoped styles don’t leak and won’t impact the rest of your site. In Astro, it is okay to use low-specificity selectors like `h1 {}` or `p {}` because they will be compiled with scopes in the final output.

Scoped styles also won’t apply to other Astro components contained inside of your template. If you need to style a child component, consider wrapping that component in a `&#x3C;div>` (or other element) that you can then style.

The specificity of scoped styles is preserved, allowing them to work consistently alongside other CSS files or CSS libraries while still preserving the exclusive boundaries that prevent styles from applying outside the component.

### Global Styles
 Section titled “Global Styles”
 While we recommend scoped styles for most components, you may eventually find a valid reason to write global, unscoped CSS. You can opt-out of automatic CSS scoping with the `&#x3C;style is:global>` attribute.

 src/components/GlobalStyles.astro ` &#x3C; style is:global > /* Unscoped, delivered as-is to the browser. Applies to all &#x3C;h1> tags on your site. */ h1 { color : red ; } &#x3C;/ style > `
 You can also mix global &#x26; scoped CSS rules together in the same `&#x3C;style>` tag using the `:global()` selector. This becomes a powerful pattern for applying CSS styles to children of your component.

 src/components/MixedStyles.astro ` &#x3C; style > /* Scoped to this component, only. */ h1 { color : red ; } /* Mixed: Applies to child `h1` elements only. */ article :global( h1 ) { color : blue ; } &#x3C;/ style > &#x3C; h1 > Title &#x3C;/ h1 > &#x3C; article >&#x3C; slot />&#x3C;/ article > ` ">
 This is a great way to style things like blog posts, or documents with CMS-powered content where the contents live outside of Astro. But be careful: components whose appearance differs based on whether or not they have a certain parent component can become difficult to troubleshoot.

Scoped styles should be used as often as possible. Global styles should be used only as-needed.

### Combining classes with `class:list`
 Section titled “Combining classes with class:list”
 If you need to combine classes on an element dynamically, you can use the `class:list` utility attribute in `.astro` files.

 src/components/ClassList.astro ` --- const { isRed } = Astro . props ; --- &#x3C;!-- If `isRed` is truthy, class will be "box red". --> &#x3C;!-- If `isRed` is falsy, class will be "box". --> &#x3C; div class:list = { [ ' box ' , { red: isRed }] } >&#x3C; slot />&#x3C;/ div >
 &#x3C; style > .box { border : 1 px solid blue ; } .red { border-color : red ; } &#x3C;/ style > ` ">

 See our directives reference page to learn more about `class:list`.

### CSS Variables
 Section titled “CSS Variables”

 Added in:
 `astro@0.21.0`

The Astro `&#x3C;style>` can reference any CSS variables available on the page. You can also pass CSS variables directly from your component frontmatter using the `define:vars` directive.

 src/components/DefineVars.astro ` --- const foregroundColor = " rgb(221 243 228) " ; const backgroundColor = " rgb(24 121 78) " ; --- &#x3C; style define:vars = { { foregroundColor , backgroundColor } } > h1 { background-color : var ( --backgroundColor ) ; color : var ( --foregroundColor ) ; } &#x3C;/ style > &#x3C; h1 > Hello &#x3C;/ h1 > `

 See our directives reference page to learn more about `define:vars`.

### Passing a `class` to a child component
 Section titled “Passing a class to a child component”
 In Astro, HTML attributes like `class` do not automatically pass through to child components.

Instead, accept a `class` prop in the child component and apply it to the root element. When destructuring, you must rename it, because `class` is a reserved word in JavaScript.

Using the default scoped style strategy, you must also pass the `data-astro-cid-*` attribute. You can do this by passing the `...rest` of the props to the component. If you have changed `scopedStyleStrategy` to `'class'` or `'where'`, the `...rest` prop is not necessary.

 src/components/MyComponent.astro ` --- const { class : className , ... rest } = Astro . props ; --- &#x3C; div class = { className } { ... rest }> &#x3C; slot /> &#x3C;/ div > `   ">
 src/pages/index.astro
```
` --- import MyComponent from " ../components/MyComponent.astro " --- &#x3C; style > .red { color : red ; } &#x3C;/ style > &#x3C; MyComponent class = " red " > This will be red! &#x3C;/ MyComponent > `
```
 This will be red! ">

### Inline styles
 Section titled “Inline styles”
 You can style HTML elements inline using the `style` attribute. This can be a CSS string or an object of CSS properties:

 src/pages/index.astro ` // These are equivalent: &#x3C; p style = { { color: " brown " , textDecoration: " underline " } } > My text &#x3C;/ p > &#x3C; p style = " color: brown; text-decoration: underline; " > My text &#x3C;/ p > ` My text
My text
">

## External Styles
 Section titled “External Styles”
 There are two ways to resolve external global stylesheets: an ESM import for files located within your project source, and an absolute URL link for files in your `public/` directory, or hosted outside of your project.

 Read more about using static assets located in `public/` or `src/`.

### Import a local stylesheet
 Section titled “Import a local stylesheet”

 You can import stylesheets in your Astro component frontmatter using ESM import syntax. CSS imports work like any other ESM import in an Astro component , which should be referenced as relative to the component and must be written at the top of your component script, with any other imports.

 src/pages/index.astro ` --- // Astro will bundle and optimize this CSS for you automatically // This also works for preprocessor files like .scss, .styl, etc. import ' ../styles/utils.css ' ; --- &#x3C; html > &#x3C;!-- Your page here --> &#x3C;/ html > ` ">
 CSS `import` via ESM are supported inside of any JavaScript file, including JSX components like React &#x26; Preact. This can be useful for writing granular, per-component styles for your React components.

### Import a stylesheet from an npm package
 Section titled “Import a stylesheet from an npm package”
 You may also need to load stylesheets from an external npm package. This is especially common for utilities like Open Props . If your package recommends using a file extension (i.e. `package-name/styles.css` instead of `package-name/styles`), this should work like any local stylesheet:

 src/pages/random-page.astro ` --- import ' package-name/styles.css ' ; --- &#x3C; html > &#x3C;!-- Your page here --> &#x3C;/ html > ` ">
 If your package does not suggest using a file extension (i.e. `package-name/styles`), you’ll need to update your Astro config first!

Say you are importing a CSS file from `package-name` called `normalize` (with the file extension omitted). To ensure we can prerender your page correctly, add `package-name` to the `vite.ssr.noExternal` array :

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ vite: { ssr: { noExternal: [ ' package-name ' ], } } }) `

 Now, you are free to import `package-name/normalize`. This will be bundled and optimized by Astro like any other local stylesheet.

 src/pages/random-page.astro ` --- import ' package-name/normalize ' ; --- &#x3C; html > &#x3C;!-- Your page here --> &#x3C;/ html > ` ">

### Load a static stylesheet via “link” tags
 Section titled “Load a static stylesheet via “link” tags”
 You can also use the `&#x3C;link>` element to load a stylesheet on the page. This should be an absolute URL path to a CSS file located in your `/public` directory, or an URL to an external website. Relative `&#x3C;link>` href values are not supported.

 src/pages/index.astro ` &#x3C; head > &#x3C;!-- Local: /public/styles/global.css --> &#x3C; link rel = " stylesheet " href = " /styles/global.css " /> &#x3C;!-- External --> &#x3C; link rel = " stylesheet " href = " https://cdn.jsdelivr.net/npm/prismjs@1.24.1/themes/prism-tomorrow.css " /> &#x3C;/ head > `      ">
 Because this approach uses the `public/` directory, it skips the normal CSS processing, bundling and optimizations that are provided by Astro. If you need these transformations, use the Import a Stylesheet method above.

## Cascading Order
 Section titled “Cascading Order”
 Astro components will sometimes have to evaluate multiple sources of CSS. For example, your component might import a CSS stylesheet, include its own `&#x3C;style>` tag, and be rendered inside a layout that imports CSS.

When conflicting CSS rules apply to the same element, browsers first use specificity and then order of appearance to determine which value to show.

If one rule is more specific than another, no matter where the CSS rule appears, its value will take precedence:

 src/components/MyComponent.astro ` &#x3C; style > h1 { color : red } div > h1 { color : purple } &#x3C;/ style > &#x3C; div > &#x3C; h1 > This header will be purple! &#x3C;/ h1 > &#x3C;/ div > ` 
#  This header will be purple!
 ">
 If two rules have the same specificity, then the order of appearance is evaluated, and the last rule’s value will take precedence:

 src/components/MyComponent.astro ` &#x3C; style > h1 { color : purple } h1 { color : red } &#x3C;/ style > &#x3C; div > &#x3C; h1 > This header will be red! &#x3C;/ h1 > &#x3C;/ div > ` 
#  This header will be red!
 ">
 Astro CSS rules are evaluated in this order of appearance:

 `&#x3C;link>` tags in the head (lowest precedence)

- imported styles

- scoped styles (highest precedence)

### Scoped Styles
 Section titled “Scoped Styles”
 Depending on your chosen value for `scopedStyleStrategy` , scoped styles may or may not increase the CLASS column specificity .

However, scoped styles will always come last in the order of appearance. These styles will therefore take precedence over other styles of the same specificity. For example, if you import a stylesheet that conflicts with a scoped style, the scoped style’s value will apply:

 src/components/make-it-purple.css ` h1 { color : purple ; } `
 src/components/MyComponent.astro
```
` --- import " ./make-it-purple.css " --- &#x3C; style > h1 { color : red } &#x3C;/ style > &#x3C; div > &#x3C; h1 > This header will be red! &#x3C;/ h1 > &#x3C;/ div > `
```
 
#  This header will be red!
 ">
 Scoped styles will be overwritten if the imported style is more specific. The style with a higher specificity will take precedence over the scoped style:

 src/components/make-it-purple.css ` #intro { color : purple ; } `
 src/components/MyComponent.astro
```
` --- import " ./make-it-purple.css " --- &#x3C; style > h1 { color : red } &#x3C;/ style > &#x3C; div > &#x3C; h1 id = " intro " > This header will be purple! &#x3C;/ h1 > &#x3C;/ div > `
```
 
#  This header will be purple!
 ">

### Import Order
 Section titled “Import Order”
 When importing multiple stylesheets in an Astro component, the CSS rules are evaluated in the order that they are imported. A higher specificity will always determine which styles to show, no matter when the CSS is evaluated. But, when conflicting styles have the same specificity, the last one imported wins:

 src/components/make-it-purple.css ` div > h1 { color : purple ; } ` h1 { color: purple;}">
 src/components/make-it-green.css
```
` div > h1 { color : green ; } `
```
 h1 { color: green;}">
 src/components/MyComponent.astro
```
` --- import " ./make-it-green.css " import " ./make-it-purple.css " --- &#x3C; style > h1 { color : red } &#x3C;/ style > &#x3C; div > &#x3C; h1 > This header will be purple! &#x3C;/ h1 > &#x3C;/ div > `
```
 
#  This header will be purple!
 ">
 While `&#x3C;style>` tags are scoped and only apply to the component that declares them, imported CSS can “leak”. Importing a component applies any CSS it imports, even if the component is never used:

 src/components/PurpleComponent.astro ` --- import " ./make-it-purple.css " --- &#x3C; div > &#x3C; h1 > I import purple CSS. &#x3C;/ h1 > &#x3C;/ div > ` 
# I import purple CSS.
 ">
 src/components/MyComponent.astro
```
` --- import " ./make-it-green.css " import PurpleComponent from " ./PurpleComponent.astro " ; --- &#x3C; style > h1 { color : red } &#x3C;/ style > &#x3C; div > &#x3C; h1 > This header will be purple! &#x3C;/ h1 > &#x3C;/ div > `
```
 
#  This header will be purple!
 ">

### Link Tags
 Section titled “Link Tags”
 Style sheets loaded via link tags are evaluated in order, before any other styles in an Astro file. Therefore, these styles will have lower precedence than imported stylesheets and scoped styles:

 src/pages/index.astro ` --- import " ../components/make-it-purple.css " ---
 &#x3C; html lang = " en " > &#x3C; head > &#x3C; meta charset = " utf-8 " /> &#x3C; link rel = " icon " type = " image/svg+xml " href = " /favicon.svg " /> &#x3C; meta name = " viewport " content = " width=device-width " /> &#x3C; meta name = " generator " content = { Astro . generator } /> &#x3C; title > Astro &#x3C;/ title > &#x3C; link rel = " stylesheet " href = " /styles/make-it-blue.css " /> &#x3C;/ head > &#x3C; body > &#x3C; div > &#x3C; h1 > This will be purple &#x3C;/ h1 > &#x3C;/ div > &#x3C;/ body > &#x3C;/ html > `    -    Astro     
# This will be purple
   ">

## Tailwind
 Section titled “Tailwind”
 Astro comes with support for adding popular CSS libraries, tools, and frameworks to your project like Tailwind and more!

Astro supports both Tailwind 3 and 4. You can add Tailwind 4 support through a Vite plugin to your project with a CLI command, or install legacy dependencies manually to add Tailwind 3 support through an Astro integration .

To upgrade your Astro project from Tailwind 3 to 4 you will need to both add Tailwind 4 support, and remove legacy Tailwind 3 support.

### Add Tailwind 4
 Section titled “Add Tailwind 4”
 In Astro `>=5.2.0`, use the `astro add tailwind` command for your package manager to install the official Vite Tailwind plugin. To add Tailwind 4 support to earlier versions of Astro, follow the instructions in the Tailwind docs to add the `@tailwindcss/vite` Vite plugin manually.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npx astro add tailwind `

 Terminal window
```
` pnpm astro add tailwind `
```

 Terminal window
```
` yarn astro add tailwind `
```

 Then, import `tailwindcss` into `src/styles/global.css` (or another CSS file of your choosing) to make Tailwind classes available to your Astro project. This file including the import will be created by default if you used the `astro add tailwind` command to install the Vite plugin.

 src/styles/global.css ` @import " tailwindcss " ; `
 Import this file in the pages where you want Tailwind to apply. This is often done in a layout component so that Tailwind styles can be used on all pages sharing that layout:

 src/layouts/Layout.astro ` --- import " ../styles/global.css " ; --- `

### Upgrade from Tailwind 3
 Section titled “Upgrade from Tailwind 3”
 Follow the steps to update an existing Astro project using Tailwind v3 (using the `@astrojs/tailwind` integration) to Tailwind 4 (using the `@tailwindcss/vite` plugin ).

-
 Add Tailwind 4 support to your project through the CLI for the latest version of Astro, or by adding the Vite plugin manually.

-
Uninstall the `@astrojs/tailwind` integration from your project:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm uninstall @astrojs/tailwind `

 Terminal window
```
` pnpm remove @astrojs/tailwind `
```

 Terminal window
```
` yarn remove @astrojs/tailwind `
```

-
 Remove the `@astrojs/tailwind` integration from your `astro.config.mjs`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import tailwind from ' @astrojs/tailwind ' ;
 export default defineConfig ({ // ... integrations: [ tailwind () ], // ... }); `

-
 Then, upgrade your project according to Tailwind’s v4 upgrade guide .

### Legacy Tailwind 3 support
 Section titled “Legacy Tailwind 3 support”
 To add (or keep) support for Tailwind 3, you will need to have both `tailwindcss@3` and the official Astro Tailwind integration `@astrojs/tailwind` installed. Installing these dependencies manually is only used for legacy Tailwind 3 compatibility, and is not required for Tailwind 4. You will also need a legacy Tailwind configuration :

-
Install Tailwind and the Astro Tailwind integration to your project dependencies using your preferred package manager:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install tailwindcss@3 @astrojs/tailwind `

 Terminal window
```
` pnpm add tailwindcss@3 @astrojs/tailwind `
```

 Terminal window
```
` yarn add tailwindcss@3 @astrojs/tailwind `
```

-
 Import the integration to your `astro.config.mjs` file, and add it to your `integrations[]` array:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import tailwind from ' @astrojs/tailwind ' ;
 export default defineConfig ({ // ... integrations: [ tailwind () ], // ... }); `

-
 Create a `tailwind.config.mjs` file in your project’s root directory. You can use the following command to generate a basic configuration file for you:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npx tailwindcss init `

 Terminal window
```
` pnpm dlx tailwindcss init `
```

 Terminal window
```
` yarn dlx tailwindcss init `
```

-
 Add the following basic configuration to your `tailwind.config.mjs` file:

 tailwind.config.mjs ` /** @type {import('tailwindcss').Config} */ export default { content: [ ' ./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue} ' ], theme: { extend: {}, }, plugins: [], }; `

 Related recipe:

 Style rendered Markdown with Tailwind Typography

## CSS Preprocessors
 Section titled “CSS Preprocessors”
 Astro supports CSS preprocessors such as Sass , Stylus , and Less through Vite .

### Sass and SCSS
 Section titled “Sass and SCSS”
 Terminal window
```
` npm install sass `
```

 Use `&#x3C;style lang="scss">` or `&#x3C;style lang="sass">` in `.astro` files.

### Stylus
 Section titled “Stylus”
 Terminal window
```
` npm install stylus `
```

 Use `&#x3C;style lang="styl">` or `&#x3C;style lang="stylus">` in `.astro` files.

### Less
 Section titled “Less”
 Terminal window
```
` npm install less `
```

 Use `&#x3C;style lang="less">` in `.astro` files.

### LightningCSS
 Section titled “LightningCSS”
 Terminal window
```
` npm install lightningcss `
```

 Update your `vite` configuration in `astro.config.mjs`:

 astro.config.mjs ` import { defineConfig } from ' astro/config '
 export default defineConfig ({ vite: { css: { transformer: " lightningcss " , }, }, }) `

### In framework components
 Section titled “In framework components”
 You can also use all of the above CSS preprocessors within JS frameworks as well! Be sure to follow the patterns each framework recommends:

- React / Preact : `import Styles from './styles.module.scss';`

- Vue : `&#x3C;style lang="scss">`

- Svelte : `&#x3C;style lang="scss">`

## PostCSS
 Section titled “PostCSS”
 Astro comes with PostCSS included as part of Vite . To configure PostCSS for your project, create a `postcss.config.cjs` file in the project root. You can import plugins using `require()` after installing them (for example `npm install autoprefixer`).

 postcss.config.cjs ` module . exports = { plugins: [ require ( ' autoprefixer ' ), require ( ' cssnano ' ), ], }; `

## Frameworks and Libraries
 Section titled “Frameworks and Libraries”

### 📘 React / Preact
 Section titled “📘 React / Preact”
 `.jsx` files support both global CSS and CSS Modules. To enable the latter, use the `.module.css` extension (or `.module.scss`/`.module.sass` if using Sass).

 src/components/MyReactComponent.jsx ` import ' ./global.css ' ; // include global CSS import Styles from ' ./styles .module.css ' ; // Use CSS Modules (must end in `.module.css`, `.module.scss`, or `.module.sass`!) `

### 📗 Vue
 Section titled “📗 Vue”
 Vue in Astro supports the same methods as `vue-loader` does:

- vue-loader - Scoped CSS

- vue-loader - CSS Modules

### 📕 Svelte
 Section titled “📕 Svelte”
 Svelte in Astro also works exactly as expected: Svelte Styling Docs .

## Markdown Styling
 Section titled “Markdown Styling”
 Any Astro styling methods are available to a Markdown layout component , but different methods will have different styling effects on your page.

You can apply global styles to your Markdown content by adding imported stylesheets to the layout that wraps your page content. It is also possible to style your Markdown with `&#x3C;style is:global>` tags in the layout component. Note that any styles added are subject to Astro’s cascading order , and you should check your rendered page carefully to ensure your styles are being applied as intended.

You can also add CSS integrations including Tailwind . If you are using Tailwind, the typography plugin can be useful for styling Markdown.

## Production
 Section titled “Production”

### Bundle control
 Section titled “Bundle control”
 When Astro builds your site for production deployment, it minifies and combines your CSS into chunks. Each page on your site gets its own chunk, and additionally, CSS that is shared between multiple pages is further split off into their own chunks for reuse.

However, when you have several pages sharing styles, some shared chunks can become really small. If all of them were sent separately, it would lead to many stylesheets requests and affect site performance. Therefore, by default Astro will link only those in your HTML above 4kB in size as `&#x3C;link rel="stylesheet">` tags, while inlining smaller ones into `&#x3C;style type="text/css">`. This approach provides a balance between the number of additional requests and the volume of CSS that can be cached between pages.

You can configure the size at which stylesheets will be linked externally (in bytes) using the `assetsInlineLimit` vite build option. Note that this option affects script and image inlining as well.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ vite: { build: { assetsInlineLimit: 1024 , } } }); `
 If you would rather all project styles remain external, you can configure the `inlineStylesheets` build option.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ build: { inlineStylesheets: ' never ' } }); `
 You can also set this option to `'always'` which will inline all stylesheets.

## Advanced
 Section titled “Advanced”

### `?raw` CSS Imports
 Section titled “?raw CSS Imports”
 For advanced use cases, CSS can be read directly from disk without being bundled or optimized by Astro. This can be useful when you need complete control over some snippet of CSS, and need to bypass Astro’s automatic CSS handling.

This is not recommended for most users.

 src/components/RawInlineStyles.astro ` --- // Advanced example! Not recommended for most users. import rawStylesCSS from ' ../styles/main.css ?raw ' ; --- &#x3C; style is:inline set:html = { rawStylesCSS } >&#x3C;/ style > `
 See Vite’s docs for full details.

### `?url` CSS Imports
 Section titled “?url CSS Imports”
 For advanced use cases, you can import a direct URL reference for a CSS file inside of your project `src/` directory. This can be useful when you need complete control over how a CSS file is loaded on the page. However, this will prevent the optimization of that CSS file with the rest of your page CSS .

This is not recommended for most users. Instead, place your CSS files inside of `public/` to get a consistent URL reference.

 src/components/RawStylesUrl.astro ` --- // Advanced example! Not recommended for most users. import stylesUrl from ' ../styles/main.css ?url ' ; --- &#x3C; link rel = " preload " href = { stylesUrl } as = " style " > &#x3C; link rel = " stylesheet " href = { stylesUrl } > `  ">
 See Vite’s docs for full details.

 Learn

 Contribute

 Community

 Sponsor

## Fonts

# Using custom fonts

 This guide will show you how to add web fonts to your project and use them in your components.

Astro provides a way to use fonts from your filesystem and various font providers (e.g. Fontsource, Google) through a unified, fully customizable , and type-safe API.

Web fonts can impact page performance at both load time and rendering time. This API helps you keep your site performant with automatic web font optimizations including preload links, optimized fallbacks, and opinionated defaults. See common usage examples .

The Fonts API focuses on performance and privacy by downloading and caching fonts so they’re served from your site. This can avoid sending user data to third-party sites, and also ensures that a consistent set of fonts is available to all your visitors.

## Configuring custom fonts
 Section titled “Configuring custom fonts”
 Registering custom fonts for your Astro project is done through the `fonts` option in your Astro config.

For each font you want to use, you must specify its name , a CSS variable , and an Astro font provider.

Astro provides built-in support for the most popular font providers : Adobe, Bunny, Fontshare, Fontsource, Google, Google Icons and NPM, as well as for using your own local font files. Additionally, you can further customize your font configuration to optimize performance and visitor experience.

### Using a local font file
 Section titled “Using a local font file”
 This example will demonstrate adding a custom font using the font file `DistantGalaxy.woff2`.

-
Add your font file inside the `src/` directory , for example `src/assets/fonts/`.

-
Create a new font family in your Astro config file using the local font provider and specify the variants to be included:

 astro.config.mjs ` import { defineConfig, fontProviders } from " astro/config " ;
 export default defineConfig ({ fonts: [{ provider: fontProviders . local (), name: " DistantGalaxy " , cssVariable: " --font-distant-galaxy " , options: { variants: [{ src: [ ' ./src/assets/fonts/DistantGalaxy.woff2 ' ], weight: ' normal ' , style: ' normal ' }] } }] }); `

-
 Your font is now configured and ready to be added to your page head so that it can be used in your project.

### Using Fontsource
 Section titled “Using Fontsource”
 Astro supports several font providers out of the box, including support for Fontsource that simplifies using Google Fonts and other open-source fonts.

The following example will use Fontsource to add custom font support, but the process is similar for any of Astro’s built-in font providers (e.g. Adobe , Bunny ).

-
Find the font you want to use in Fontsource’s catalog . This example will use Roboto .

-
Create a new font family in your Astro config file using the Fontsource provider :

 astro.config.mjs ` import { defineConfig, fontProviders } from " astro/config " ;
 export default defineConfig ({ fonts: [{ provider: fontProviders . fontsource (), name: " Roboto " , cssVariable: " --font-roboto " , }] }); `

-
 Your font is now configured and ready to be added to your page head so that it can be used in your project.

## Applying custom fonts
 Section titled “Applying custom fonts”
 After a font is configured , it must be added to your page head with an identifying CSS variable. Then, you can use this variable when defining your page styles.

-
Import and include the `&#x3C;Font />` component with the required `cssVariable` property in the head of your page, usually in a dedicated `Head.astro` component or in a layout component directly:

 src/layouts/Layout.astro ` --- import { Font } from " astro:assets " ; ---
 &#x3C; html > &#x3C; head > &#x3C; Font cssVariable = " --font-distant-galaxy " /> &#x3C;/ head > &#x3C; body > &#x3C; slot /> &#x3C;/ body > &#x3C;/ html > `        ">

-
 In any page rendered with that layout, including the layout component itself, you can now define styles with your font’s `cssVariable` to apply your custom font.

In the following example, the `&#x3C;h1>` heading will have the custom font applied, while the paragraph `&#x3C;p>` will not.

 src/pages/example.astro ` --- import Layout from " ../layouts/Layout.astro " ; --- &#x3C; Layout > &#x3C; h1 > In a galaxy far, far away... &#x3C;/ h1 >
 &#x3C; p > Custom fonts make my headings much cooler! &#x3C;/ p >
 &#x3C; style > h1 { font-family : var ( --font-distant-galaxy ); } &#x3C;/ style > &#x3C;/ Layout > ` 
# In a galaxy far, far away...
 Custom fonts make my headings much cooler!
  ">

## Preloading fonts
 Section titled “Preloading fonts”
 Font preloading should be done sparingly, as it can block the loading of other important resources or download fonts that are unnecessary for the current page. Consider preloading only the most essential fonts, necessary for displaying content visible above the fold.

To preload a font, pass the `preload` property to the corresponding `&#x3C;Font />` component. If multiple files correspond to a font, you can also specify which one to preload by passing an array.

 src/layouts/Layout.astro ` --- import { Font } from " astro:assets " ; ---
 &#x3C; html > &#x3C; head > &#x3C; Font cssVariable = " --font-distant-galaxy " preload /> &#x3C;/ head > &#x3C; body > &#x3C; slot /> &#x3C;/ body > &#x3C;/ html > `        ">

## Register fonts in Tailwind
 Section titled “Register fonts in Tailwind”
 If you are using Tailwind for styling, you will not apply your styles with the `font-face` CSS property.

Instead, after configuring your custom font and adding it to your page head , you will need to update your Tailwind configuration to register your font:

 -

 Tailwind CSS 4.0

-

 Tailwind CSS 3.0

 src/styles/global.css ` @import " tailwindcss " ;
 @theme inline { --font-sans: var(--font-roboto ); } `

 tailwind.config.mjs
```
` /** @type {import("tailwindcss").Config} */ export default { content: [ " ./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue} " ], theme: { extend: {}, fontFamily: { sans: [ " var(--font-roboto) " ] } }, plugins: [] }; `
```

 See Tailwind’s docs on adding custom font families for more information.

## Using variable fonts
 Section titled “Using variable fonts”
 To use variable fonts in your project, specify the available weight range instead of individual weights in your provider’s configuration.

 -

 Local provider

-

 Other providers

 When using a local font file , you can specify that the font is variable by setting the `weight` property of the variant to a string corresponding to the exact weight range available for the font.
The following example configures Inter as a local variable font with the available weight range:
 astro.config.mjs ` import { defineConfig, fontProviders } from " astro/config " ;
 export default defineConfig ({ fonts: [{ provider: fontProviders . local (), name: " Inter " , cssVariable: " --font-inter " , options: { variants: [ { weight: " 100 900 " , style: " normal " , src: [ " ./src/assets/fonts/InterVariable.woff2 " ], }, ], }, }] }); `

 When using other providers (e.g. Fontsource) , that support variable fonts, you can request the variable version of a font by setting the `weights` property with an array containing the exact range of weights available for the font.
The following example downloads Fira Code from Fontsource as a variable font with the available weight range:
 astro.config.mjs ` import { defineConfig, fontProviders } from " astro/config " ;
 export default defineConfig ({ fonts: [{ cssVariable: " --font-fira-code " , name: " Fira Code " , provider: fontProviders . fontsource (), styles: [ " normal " ], weights: [ " 300 700 " ], }] }); `

## Customizing font fallbacks
 Section titled “Customizing font fallbacks”
 Fallback fonts are used when the primary font has not yet loaded, contains missing characters, or cannot be loaded for any reason. When the fallback font differs significantly from the primary font, layout shifts may occur during page loading.

To avoid this, Astro automatically tries to generate optimized fallback fonts from the last defined fallback if it is a generic font family . It uses `sans-serif` by default, but it may not match the desired appearance of your primary font. You can adjust it in your font configuration:

 astro.config.mjs ` import { defineConfig, fontProviders } from " astro/config " ;
 export default defineConfig ({ fonts: [{ provider: fontProviders . fontsource (), name: " Cousine " , cssVariable: " --font-cousine " , fallbacks: [ " monospace " ] }] }); `
 You can also opt out of the default optimization by setting `font.optimizedFallbacks` to `false` in your font configuration. Astro will then use the fallback fonts specified in your configuration without any additional automatic processing.

## Accessing font data programmatically
 Section titled “Accessing font data programmatically”
 Astro exposes low-level APIs for accessing data programmatically:

- Font family data through the `fontData` object

- Font file URLs with the `experimental_getFontFileURL()` function.

This can be useful for advanced use cases where you need direct access to font files, such as generating OpenGraph images with Satori in an API Route .

The `fontData` object gives you access to all font files downloaded by Astro for your project, along with their metadata. This means that you are responsible for filtering font files to find the specific file you need, and for fetching data after resolving URLs.

The following example generates an OpenGraph image in a static file endpoint, assuming that only one font and its format have been configured with a format supported by Satori :

 src/pages/og.png.ts ` import type { APIRoute } from " astro " ; import { fontData, experimental_getFontFileURL } from " astro:assets " ; import satori from " satori " ; import { html } from " satori-html " ; import sharp from " sharp " ;
 export const GET : APIRoute = async ( context ) => { const fontPath = fontData[ " --font-roboto " ] [ 0 ] ?. src [ 0 ] ?. url ;
 if (fontPath === undefined ) { throw new Error ( " Cannot find the font path. " ) ; }
 const url = experimental_getFontFileURL (fontPath , context . url ) ; const data = await fetch (url) . then ( ( res ) => res . arrayBuffer ()) ;
 const svg = await satori ( html ` &#x3C;div style="color: black;">hello, world&#x3C;/div> ` , { width: 600 , height: 400 , fonts: [ { name: " Roboto " , data, weight: 400 , style: " normal " , }, ] , }, ) ;
 const pngBuffer = await sharp (Buffer . from (svg)) . resize ( 600 , 400 ) . png () . toBuffer () ;
 return new Response ( new Uint8Array (pngBuffer) , { headers: { " Content-Type " : " image/png " , }, } ) ; } ; ` { const fontPath = fontData[&#x22;--font-roboto&#x22;][0]?.src[0]?.url; if (fontPath === undefined) { throw new Error(&#x22;Cannot find the font path.&#x22;); } const url = experimental_getFontFileURL(fontPath, context.url); const data = await fetch(url).then((res) => res.arrayBuffer()); const svg = await satori( html&#x60; hello, world &#x60;, { width: 600, height: 400, fonts: [ { name: &#x22;Roboto&#x22;, data, weight: 400, style: &#x22;normal&#x22;, }, ], }, ); const pngBuffer = await sharp(Buffer.from(svg)) .resize(600, 400) .png() .toBuffer(); return new Response(new Uint8Array(pngBuffer), { headers: { &#x22;Content-Type&#x22;: &#x22;image/png&#x22;, }, });};">

## Granular font configuration
 Section titled “Granular font configuration”
 A font family is defined by a combination of properties such as weights and styles (e.g. `weights: [500, 600]` and `styles: ["normal", "bold"]`), but you may want to download only certain combinations of these.

For greater control over which font files are downloaded, you can specify the same font (ie. with the same `cssVariable`, `name`, and `provider` properties) multiple times with different combinations. Astro will merge the results and download only the required files. For example, it is possible to download normal `500` and `600` while downloading only italic `500`:

 astro.config.mjs ` import { defineConfig, fontProviders } from " astro/config " ;
 export default defineConfig ({ fonts: [ { name: " Roboto " , cssVariable: " --roboto " , provider: fontProviders . google (), weights: [ 500 , 600 ], styles: [ " normal " ] }, { name: " Roboto " , cssVariable: " --roboto " , provider: fontProviders . google (), weights: [ 500 ], styles: [ " italic " ] } ] }); `

## Caching
 Section titled “Caching”
 The Fonts API caching implementation was designed to be practical in development and efficient in production. During builds, font files are copied to the `_astro/fonts` output directory, so they can benefit from HTTP caching of static assets (usually a year).

To clear the cache in development, remove the `.astro/fonts` directory. To clear the build cache, remove the `node_modules/.astro/fonts` directory.

## Examples
 Section titled “Examples”
 Astro’s font feature is based on flexible configuration options. Your own project’s font configuration may look different from simplified examples, so the following are provided to show what various font configurations might look like when used in production.

 astro.config.mjs
```
` import { defineConfig, fontProviders } from " astro/config " ;
 export default defineConfig ({ fonts: [ { name: " Roboto " , cssVariable: " --font-roboto " , provider: fontProviders . google (), // Default included: // weights: [400] , // styles: ["normal", "italic"], // subsets: ["latin"], // fallbacks: ["sans-serif"], // formats: ["woff2"], }, { name: " Inter " , cssVariable: " --font-inter " , provider: fontProviders . fontsource (), // Specify weights that are actually used weights: [ 400 , 500 , 600 , 700 ], // Specify styles that are actually used styles: [ " normal " ], // Download only font files for characters used on the page subsets: [ " latin " , " cyrillic " ], // Download more font formats formats: [ " woff2 " , " woff " ], }, { name: " JetBrains Mono " , cssVariable: " --font-jetbrains-mono " , provider: fontProviders . fontsource (), // Download only font files for characters used on the page subsets: [ " latin " , " latin-ext " ], // Use a fallback font family matching the intended appearance fallbacks: [ " monospace " ], }, { name: " Poppins " , cssVariable: " --font-poppins " , provider: fontProviders . local (), options: { // Weight and style are not specified so Astro // will try to infer them for each variant variants: [ { src: [ " ./src/assets/fonts/Poppins-regular.woff2 " , " ./src/assets/fonts/Poppins-regular.woff " , ] }, { src: [ " ./src/assets/fonts/Poppins-bold.woff2 " , " ./src/assets/fonts/Poppins-bold.woff " , ] }, ] } } ], }); `
```

 Learn

 Contribute

 Community

 Sponsor

## Syntax Highlighting

# Syntax Highlighting

 Astro comes with built-in support for Shiki and Prism . This provides syntax highlighting for:

- all code fences (```) used in a Markdown or MDX file.

- content within the built-in `&#x3C;Code />` component (powered by Shiki) in `.astro` files.

- content within the `&#x3C;Prism />` component (powered by Prism) in `.astro` files.

Add community integrations such as Expressive Code for even more text marking and annotation options in your code blocks.

## Markdown code blocks
 Section titled “Markdown code blocks”
 A Markdown code block is indicated by a block with three backticks ``` at the start and end. You can indicate the programming language being used after the opening backticks to indicate how to color and style your code to make it easier to read.

 - ` ```js // JavaScript code with syntax highlighting. var fun = function lang ( l ) { dateformat . i18n = require ( ' ./lang/ ' + l ) ; return true ; } ; ``` `
 Astro’s Markdown code blocks are styled by Shiki by default, preconfigured with the `github-dark` theme. The compiled output will be limited to inline `style`s without any extraneous CSS classes, stylesheets, or client-side JS.

You can add a Prism stylesheet and switch to Prism’s highlighting , or disable Astro’s syntax highlighting entirely, with the `markdown.syntaxHighlight` configuration option.

 See the full `markdown.shikiConfig` reference for the complete set of Markdown syntax highlighting options available when using Shiki.

### Setting a default Shiki theme
 Section titled “Setting a default Shiki theme”
 You can configure any built-in Shiki theme for your Markdown code blocks in your Astro config:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ markdown: { shikiConfig: { theme: ' dracula ' , }, }, }); `

 See the full Shiki config reference for the complete set of Markdown code block options.

### Setting light and dark mode themes
 Section titled “Setting light and dark mode themes”
 You can specify dual Shiki themes for light and dark mode in your Astro config:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ;
 export default defineConfig ({ markdown: { shikiConfig: { themes: { light: ' github-light ' , dark: ' github-dark ' , }, }, }, }); `
 Then, add Shiki’s dark mode CSS variables via media query or classes to apply to all your Markdown code blocks by default. Replace the `.shiki` class in the examples from Shiki’s documentation with `.astro-code`:

 src/styles/global.css ` @media ( prefers-color-scheme: dark ) { .shiki , .shiki span { . astro-code , . astro-code span { color : var ( --shiki-dark ) !important ; background-color : var ( --shiki-dark-bg ) !important ; /* Optional, if you also want font styles */ font-style : var ( --shiki-dark-font-style ) !important ; font-weight : var ( --shiki-dark-font-weight ) !important ; text-decoration : var ( --shiki-dark-text-decoration ) !important ; } } `

 See the full Shiki config reference for the complete set of Markdown code block options.

### Adding your own Shiki theme
 Section titled “Adding your own Shiki theme”
 Instead of using one of Shiki’s predefined themes, you can import a custom Shiki theme from a local file.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import customTheme from ' ./my-shiki-theme.json ' ;
 export default defineConfig ({ markdown: { shikiConfig: { theme: customTheme , }, }, }); `

### Customizing Shiki themes
 Section titled “Customizing Shiki themes”
 You can follow Shiki’s own theme documentation for more customization options for themes, light vs dark mode toggles , or styling via CSS variables .

You will need to adjust the examples from Shiki’s documentation for your Astro project by making the following substitutions:

 Code blocks are styled using the `.astro-code` class instead of `.shiki`

- When using the `css-variables` theme, custom properties are prefixed with `--astro-code-` instead of `--shiki-`

## Components for code blocks
 Section titled “Components for code blocks”
 There are two Astro components available for `.astro` and `.mdx` files to render code blocks: `&#x3C;Code />` and `&#x3C;Prism />` .

You can reference the `Props` of these components using the `ComponentProps` type utility.

### `&#x3C;Code />`
 Section titled “&#x3C;Code />”
 This component is powered internally by Shiki. It supports all popular Shiki themes and languages as well as several other Shiki options such as custom themes, languages, transformers , and default colors.

These values are passed to the `&#x3C;Code />` component using the `theme`, `lang`, `embeddedLangs` , `transformers` , and `defaultColor` attributes respectively as props. The `&#x3C;Code />` component will not inherit your `shikiConfig` settings for Markdown code blocks.

 ` --- import { Code } from ' astro:components ' ; --- &#x3C;!-- Syntax highlight some JavaScript code. --> &#x3C; Code code = { ` const foo = 'bar'; ` } lang = " js " /> &#x3C;!-- Optional: Customize your theme. --> &#x3C; Code code = { ` const foo = 'bar'; ` } lang = " js " theme = " dark-plus " /> &#x3C;!-- Optional: Enable word wrapping. --> &#x3C; Code code = { ` const foo = 'bar'; ` } lang = " js " wrap /> &#x3C;!-- Optional: Output inline code. --> &#x3C; p > &#x3C; Code code = { ` const foo = 'bar'; ` } lang = " js " inline /> will be rendered inline. &#x3C;/ p > &#x3C;!-- Optional: defaultColor --> &#x3C; Code code = { ` const foo = 'bar'; ` } lang = " js " defaultColor = { false } /> `      will be rendered inline.
 ">

#### `embeddedLangs`
 Section titled “embeddedLangs”
 Type: `string[] | undefined`

 Added in:
 `astro@6.0.0`

Any additional languages to be included for syntax highlighting by Shiki.

A `lang` value may include support for highlighting some additional languages by default (e.g. `lang="svelte"` will also provide highlighting for `ts`).

Use `embeddedLangs` to include support for additional, non-standard language combinations (e.g. `jsx` support when `lang="vue"`).

 src/pages/index.astro ` --- import { Code } from ' astro:components '
 const code = ` &#x3C;script setup lang="tsx"> const Text = ({ text }: { text: string }) => &#x3C;div>{text}&#x3C;/div>; &#x3C;/script>
 &#x3C;template> &#x3C;Text text="Hello world" /> &#x3C;/template> ` --- &#x3C; Code lang = " vue " embeddedLangs = { [ " tsx " ] } code = { code } /> `   &#x60;--- ">

#### `transformers`
 Section titled “transformers”
 Type: `ShikiTransformer[] | undefined`

 Added in:
 `astro@4.11.0`

An array of Shiki transformers to be applied to your `code`. Since Astro v4.14.0, you can also provide a string for Shiki’s `meta` attribute to pass options to transformers.

Note that `transformers` only applies classes and you must provide your own CSS rules to target the elements of your code block.

 src/pages/index.astro ` --- import { transformerNotationFocus, transformerMetaHighlight } from ' @shikijs/transformers ' import { Code } from ' astro:components ' const code = ` const foo = 'hello' const bar = ' world' console.log(foo + bar) // [!code focus] ` --- &#x3C; Code code = { code } lang = " js " transformers = { [ transformerMetaHighlight ()] } meta = " {1,3} " />
 &#x3C; style is:global > pre .has-focused .line:not ( .focused ) { filter : blur ( 1 px ); } &#x3C;/ style > ` ">

### `&#x3C;Prism />`
 Section titled “&#x3C;Prism />”
 This component provides language-specific syntax highlighting for code blocks by applying Prism’s CSS classes. Note that you must provide a Prism CSS stylesheet (or bring your own) to style the classes.

To use the `Prism` highlighter component, you must install the `@astrojs/prism` package:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install @astrojs/prism `

 Terminal window
```
` pnpm add @astrojs/prism `
```

 Terminal window
```
` yarn add @astrojs/prism `
```

 Then, you can import and use the `&#x3C;Prism />` component like any other Astro component, passing a language and the code to render.

 ` --- import { Prism } from ' @astrojs/prism ' ; --- &#x3C; Prism lang = " js " code = { ` const foo = 'bar'; ` } /> ` ">
 In addition to the list of languages supported by Prism , you can also use `lang="astro"` to display Astro code blocks.

## Add a Prism stylesheet
 Section titled “Add a Prism stylesheet”
 If you opt to use Prism (either by configuring `markdown.syntaxHighlight: 'prism'` or with the `&#x3C;Prism />` component), Astro will apply Prism’s CSS classes instead of Shiki’s to your code. You will need to bring your own CSS stylesheet for syntax highlighting to appear.

-
Choose a premade stylesheet from the available Prism Themes .

-
Add this stylesheet to your project’s `public/` directory .

-
Load this into your page’s `&#x3C;head>` in a layout component via a `&#x3C;link>` tag. (See Prism basic usage .)

You can also visit the list of languages supported by Prism for options and usage.

 Learn

 Contribute

 Community

 Sponsor

## Client Side Scripts

# Scripts and event handling

 You can send JavaScript to the browser and add functionality to your Astro components using `&#x3C;script>` tags in the component template.

Scripts add interactivity to your site, such as handling events or updating content dynamically, without the need for a UI framework like React, Svelte, or Vue. This avoids the overhead of shipping framework JavaScript and doesn’t require you to know any additional framework to create a full-featured website or application.

## Client-Side Scripts
 Section titled “Client-Side Scripts”
 Scripts can be used to add event listeners, send analytics data, play animations, and everything else JavaScript can do on the web.

Astro automatically enhances the HTML standard `&#x3C;script>` tag with bundling, TypeScript, and more. See how astro processes scripts for more details.

 - src/components/ConfettiButton.astro ` &#x3C; button data-confetti-button > Celebrate! &#x3C;/ button >
 &#x3C; script > // Import from npm package. import confetti from ' canvas-confetti ' ;
 // Find our component DOM on the page. const buttons = document . querySelectorAll ( ' [data-confetti-button] ' );
 // Add event listeners to fire confetti when a button is clicked. buttons . forEach ( ( button ) => { button . addEventListener ( ' click ' , () => confetti ()); }); &#x3C;/ script > ` Celebrate! ">

 See when your scripts will not be processed to troubleshoot script behavior, or to learn how to opt-out of this processing intentionally.

## Script processing
 Section titled “Script processing”
 By default, Astro processes `&#x3C;script>` tags that contain no attributes (other than `src`) in the following ways:

 TypeScript support: All scripts are TypeScript by default.

- Import bundling: Import local files or npm modules, which will be bundled together.

- Type Module: Processed scripts become `type="module"` automatically.

- Deduplication: If a component that contains a `&#x3C;script>` is used multiple times on a page, the script will only be included once.

- Automatic inlining: If the script is small enough, Astro will inline it directly into the HTML to reduce the number of requests.

 src/components/Example.astro ` &#x3C; script > // Processed! Bundled! TypeScript! // Importing local scripts and from npm packages works. &#x3C;/ script > `

### Unprocessed scripts
 Section titled “Unprocessed scripts”
 Astro will not process a `&#x3C;script>` tag if it has any attribute other than `src`.

You can add the `is:inline` directive to intentionally opt out of processing for a script.

 src/components/InlineScript.astro ` &#x3C; script is:inline > // Will be rendered into the HTML exactly as written! // Not transformed: no TypeScript and no import resolution by Astro. // If used inside a component, this code is duplicated for each instance. &#x3C;/ script > `

### Include JavaScript files on your page
 Section titled “Include JavaScript files on your page”
 You may want to write your scripts as separate `.js`/`.ts` files or need to reference an external script on another server. You can do this by referencing these in a `&#x3C;script>` tag’s `src` attribute.

#### Import local scripts
 Section titled “Import local scripts”
 When to use this: when your script lives inside of `src/`.

Astro will process these scripts according to the script processing rules .

 src/components/LocalScripts.astro ` &#x3C;!-- relative path to script at `src/scripts/local.js` --> &#x3C; script src = " ../scripts/local.js " >&#x3C;/ script >
 &#x3C;!-- also works for local TypeScript files --> &#x3C; script src = " ./script-with-types.ts " >&#x3C;/ script > `

#### Load external scripts
 Section titled “Load external scripts”
 When to use this: when your JavaScript file lives inside of `public/` or on a CDN.

To load scripts outside of your project’s `src/` folder, include the `is:inline` directive. This approach skips the JavaScript processing, bundling, and optimizations that are provided by Astro when you import scripts as described above.

 src/components/ExternalScripts.astro ` &#x3C;!-- absolute path to a script at `public/my-script.js` --> &#x3C; script is:inline src = " /my-script.js " >&#x3C;/ script >
 &#x3C;!-- full URL to a script on a remote server --> &#x3C; script is:inline src = " https://my-analytics.com/script.js " >&#x3C;/ script > `

## Common script patterns
 Section titled “Common script patterns”

### Handle `onclick` and other events
 Section titled “Handle onclick and other events”
 Some UI frameworks use custom syntax for event handling like `onClick={...}` (React/Preact) or `@click="..."` (Vue). Astro follows standard HTML more closely and does not use custom syntax for events.

Instead, you can use `addEventListener` in a `&#x3C;script>` tag to handle user interactions.

 src/components/AlertButton.astro ` &#x3C; button class = " alert " > Click me! &#x3C;/ button >
 &#x3C; script > // Find all buttons with the `alert` class on the page. const buttons = document . querySelectorAll ( ' button.alert ' );
 // Handle clicks on each button. buttons . forEach ( ( button ) => { button . addEventListener ( ' click ' , () => { alert ( ' Button was clicked! ' ); }); }); &#x3C;/ script > ` Click me! ">
 If you have multiple `&#x3C;AlertButton />` components on a page, Astro will not run the script multiple times. Scripts are bundled and only included once per page. Using `querySelectorAll` ensures that this script attaches the event listener to every button with the `alert` class found on the page.

### Web components with custom elements
 Section titled “Web components with custom elements”
 You can create your own HTML elements with custom behavior using the Web Components standard. Defining a custom element in a `.astro` component allows you to build interactive components without needing a UI framework library.

In this example, we define a new `&#x3C;astro-heart>` HTML element that tracks how many times you click the heart button and updates the `&#x3C;span>` with the latest count.

 src/components/AstroHeart.astro ` &#x3C;!-- Wrap the component elements in our custom element “astro-heart”. --> &#x3C; astro-heart > &#x3C; button aria-label = " Heart " > 💜 &#x3C;/ button > × &#x3C; span > 0 &#x3C;/ span > &#x3C;/ astro-heart >
 &#x3C; script > // Define the behaviour for our new type of HTML element. class AstroHeart extends HTMLElement { connectedCallback () { let count = 0 ;
 const heartButton = this . querySelector ( ' button ' ); const countSpan = this . querySelector ( ' span ' );
 // Each time the button is clicked, update the count. heartButton . addEventListener ( ' click ' , () => { count ++ ; countSpan . textContent = count . toString (); }); } }
 // Tell the browser to use our AstroHeart class for &#x3C;astro-heart> elements. customElements . define ( ' astro-heart ' , AstroHeart ); &#x3C;/ script > `  💜 × 0  ">
 There are two advantages to using a custom element here:

-
Instead of searching the whole page using `document.querySelector()`, you can use `this.querySelector()`, which only searches within the current custom element instance. This makes it easier to work with only the children of one component instance at a time.

-
Although a `&#x3C;script>` only runs once, the browser will run our custom element’s `connectedCallback()` method each time it finds `&#x3C;astro-heart>` on the page. This means you can safely write code for one component at a time, even if you intend to use this component multiple times on a page.

 You can learn more about custom elements in web.dev’s Reusable Web Components guide and MDN’s introduction to custom elements .

### Pass frontmatter variables to scripts
 Section titled “Pass frontmatter variables to scripts”
 In Astro components, the code in the frontmatter (between the `---` fences) runs on the server and is not available in the browser.

To pass server-side variables to client-side scripts, store them in `data-*` attributes on HTML elements. Scripts can then access these values using the `dataset` property.

In this example component, a `message` prop is stored in a `data-message` attribute, so the custom element can read `this.dataset.message` and get the value of the prop in the browser.

 src/components/AstroGreet.astro ` --- const { message = ' Welcome, world! ' } = Astro . props ; ---
 &#x3C;!-- Store the message prop as a data attribute. --> &#x3C; astro-greet data-message = { message } > &#x3C; button > Say hi! &#x3C;/ button > &#x3C;/ astro-greet >
 &#x3C; script > class AstroGreet extends HTMLElement { connectedCallback () { // Read the message from the data attribute. const message = this . dataset . message ; const button = this . querySelector ( ' button ' ); button . addEventListener ( ' click ' , () => { alert ( message ); }); } }
 customElements . define ( ' astro-greet ' , AstroGreet ); &#x3C;/ script > `  Say hi!  ">
 Now we can use our component multiple times and be greeted by a different message for each one.

 src/pages/example.astro ` --- import AstroGreet from ' ../components/AstroGreet.astro ' ; ---
 &#x3C;!-- Use the default message: “Welcome, world!” --> &#x3C; AstroGreet />
 &#x3C;!-- Use custom messages passed as a props. --> &#x3C; AstroGreet message = " Lovely day to build components! " /> &#x3C; AstroGreet message = " Glad you made it! 👋 " /> `   ">

### Combining scripts and UI Frameworks
 Section titled “Combining scripts and UI Frameworks”
 Elements rendered by a UI framework may not be available yet when a `&#x3C;script>` tag executes. If your script also needs to handle UI framework components , using a custom element is recommended.

 Learn

 Contribute

 Community

 Sponsor

## Framework Components

# Front-end frameworks

 Build your Astro website without sacrificing your favorite component framework. Create Astro islands with the UI frameworks of your choice.

## Official front-end framework integrations
 Section titled “Official front-end framework integrations”
 Astro supports a variety of popular frameworks including React , Preact , Svelte , Vue , SolidJS , and AlpineJS with official integrations.

Find even more community-maintained framework integrations (e.g. Angular, Qwik, Elm) in our integrations directory.

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

## Installing integrations
 Section titled “Installing integrations”
 One or several of these Astro integrations can be installed and configured in your project.

See the Integrations Guide for more details on installing and configuring Astro integrations.

## Using framework components
 Section titled “Using framework components”
 Use your JavaScript framework components in your Astro pages, layouts and components just like Astro components! All your components can live together in `/src/components`, or can be organized in any way you like.

To use a framework component, import it from its relative path in your Astro component script. Then, use the component alongside other components, HTML elements and JSX-like expressions in the component template.

 - src/pages/static-components.astro ` --- import MyReactComponent from ' ../components/MyReactComponent.jsx ' ; --- &#x3C; html > &#x3C; body > &#x3C; h1 > Use React components directly in Astro! &#x3C;/ h1 > &#x3C; MyReactComponent /> &#x3C;/ body > &#x3C;/ html > `  
# Use React components directly in Astro!
   ">
 By default, your framework components will only render on the server, as static HTML. This is useful for templating components that are not interactive and avoids sending any unnecessary JavaScript to the client.

## Hydrating interactive components
 Section titled “Hydrating interactive components”
 A framework component can be made interactive (hydrated) using a `client:*` directive . These are component attributes that determine when your component’s JavaScript should be sent to the browser.

With all client directives except `client:only`, your component will first render on the server to generate static HTML. Component JavaScript will be sent to the browser according to the directive you chose. The component will then hydrate and become interactive.

 src/pages/interactive-components.astro ` --- // Example: hydrating framework components in the browser. import InteractiveButton from ' ../components/InteractiveButton.jsx ' ; import InteractiveCounter from ' ../components/InteractiveCounter.jsx ' ; import InteractiveModal from ' ../components/InteractiveModal.svelte ' ; --- &#x3C;!-- This component's JS will begin importing when the page loads --> &#x3C; InteractiveButton client:load />
 &#x3C;!-- This component's JS will not be sent to the client until the user scrolls down and the component is visible on the page --> &#x3C; InteractiveCounter client:visible />
 &#x3C;!-- This component won't render on the server, but will render on the client when the page loads --> &#x3C; InteractiveModal client:only = " svelte " /> `   ">
 The JavaScript framework (React, Svelte, etc.) needed to render the component will be sent to the browser along with the component’s own JavaScript. If two or more components on a page use the same framework, the framework will only be sent once.

### Available hydration directives
 Section titled “Available hydration directives”
 There are several hydration directives available for UI framework components: `client:load`, `client:idle`, `client:visible`, `client:media={QUERY}` and `client:only={FRAMEWORK}`.

 See our directives reference page for a full description of these hydration directives, and their usage.

## Mixing frameworks
 Section titled “Mixing frameworks”
 You can import and render components from multiple frameworks in the same Astro component.

 src/pages/mixing-frameworks.astro ` --- // Example: Mixing multiple framework components on the same page. import MyReactComponent from ' ../components/MyReactComponent.jsx ' ; import MySvelteComponent from ' ../components/MySvelteComponent.svelte ' ; import MyVueComponent from ' ../components/MyVueComponent.vue ' ; --- &#x3C; div > &#x3C; MySvelteComponent /> &#x3C; MyReactComponent /> &#x3C; MyVueComponent /> &#x3C;/ div > `     ">
 Astro will recognize and render your component based on its file extension. To distinguish between frameworks that use the same file extension, additional configuration when rendering multiple JSX frameworks (e.g. React and Preact) is required.

## Passing props to framework components
 Section titled “Passing props to framework components”
 You can pass props from Astro components to framework components:

 src/pages/frameworks-props.astro ` --- import TodoList from ' ../components/TodoList.jsx ' ; import Counter from ' ../components/Counter.svelte ' ; --- &#x3C; div > &#x3C; TodoList initialTodos = { [ " learn Astro " , " review PRs " ] } /> &#x3C; Counter startingCount = { 1 } /> &#x3C;/ div > `    ">
 Props that are passed to interactive framework components using a `client:*` directive must be serialized : translated into a format suitable for transfer over a network, or storage. However, Astro does not serialize every type of data structure. Therefore, there are some limitations on what can be passed as props to hydrated components.

The following prop types are supported:
plain object, `number`, `string`, `Array`, `Map`, `Set`, `RegExp`, `Date`, `BigInt`, `URL`, `Uint8Array`, `Uint16Array`, `Uint32Array`, and `Infinity`

Non-supported data structures passed to components, such as functions, can only be used during the component’s server rendering and cannot be used to provide interactivity. For example, passing functions to hydrated components is not supported because Astro cannot pass functions from the server in a way that makes them executable on the client.

## Passing children to framework components
 Section titled “Passing children to framework components”
 Inside of an Astro component, you can pass children to framework components. Each framework has its own patterns for how to reference these children: React, Preact, and Solid all use a special prop named `children`, while Svelte and Vue use the `&#x3C;slot />` element.

 src/pages/component-children.astro ` --- import MyReactSidebar from ' ../components/MyReactSidebar.jsx ' ; --- &#x3C; MyReactSidebar > &#x3C; p > Here is a sidebar with some text and a button. &#x3C;/ p > &#x3C;/ MyReactSidebar > `  Here is a sidebar with some text and a button.
 ">
Additionally, you can use Named Slots to group specific children together.

For React, Preact, and Solid, these slots will be converted to a top-level prop. Slot names using `kebab-case` will be converted to `camelCase`.

 src/pages/named-slots.astro ` --- import MySidebar from ' ../components/MySidebar.jsx ' ; --- &#x3C; MySidebar > &#x3C; h2 slot = " title " > Menu &#x3C;/ h2 > &#x3C; p > Here is a sidebar with some text and a button. &#x3C;/ p > &#x3C; ul slot = " social-links " > &#x3C; li >&#x3C; a href = " https://twitter.com/astrodotbuild " > Twitter &#x3C;/ a >&#x3C;/ li > &#x3C; li >&#x3C; a href = " https://github.com/withastro " > GitHub &#x3C;/ a >&#x3C;/ li > &#x3C;/ ul > &#x3C;/ MySidebar > ` 
## Menu
 Here is a sidebar with some text and a button.
  Twitter
 - GitHub
  ">
 src/components/MySidebar.jsx ` export default function MySidebar ( props ) { return ( &#x3C; aside > &#x3C; header > { props . title } &#x3C;/ header > &#x3C; main > { props . children } &#x3C;/ main > &#x3C; footer > { props . socialLinks } &#x3C;/ footer > &#x3C;/ aside > ) } `
 For Svelte and Vue these slots can be referenced using a `&#x3C;slot>` element with the `name` attribute. Slot names using `kebab-case` will be preserved.

 src/components/MySidebar.svelte ` &#x3C; aside > &#x3C; header >&#x3C; slot name = " title " />&#x3C;/ header > &#x3C; main >&#x3C; slot />&#x3C;/ main > &#x3C; footer >&#x3C; slot name = " social-links " />&#x3C;/ footer > &#x3C;/ aside > `

## Nesting framework components
 Section titled “Nesting framework components”
 Inside of an Astro file, framework component children can also be hydrated components. This means that you can recursively nest components from any of these frameworks.

 src/pages/nested-components.astro ` --- import MyReactSidebar from ' ../components/MyReactSidebar.jsx ' ; import MyReactButton from ' ../components/MyReactButton.jsx ' ; import MySvelteButton from ' ../components/MySvelteButton.svelte ' ; --- &#x3C; MyReactSidebar > &#x3C; p > Here is a sidebar with some text and a button. &#x3C;/ p > &#x3C; div slot = " actions " > &#x3C; MyReactButton client:idle /> &#x3C; MySvelteButton client:idle /> &#x3C;/ div > &#x3C;/ MyReactSidebar > `  Here is a sidebar with some text and a button.
     ">

This allows you to build entire “apps” in your preferred JavaScript framework and render them, via a parent component, to an Astro page.

## Can I use Astro components inside my framework components?
 Section titled “Can I use Astro components inside my framework components?”
 Any UI framework component becomes an “island” of that framework. These components must be written entirely as valid code for that framework, using only its own imports and packages. You cannot import `.astro` components in a UI framework component (e.g. `.jsx` or `.svelte`).

You can, however, use the Astro `&#x3C;slot />` pattern to pass static content generated by Astro components as children to your framework components inside an `.astro` component .

 src/pages/astro-children.astro ` --- import MyReactComponent from ' ../components/MyReactComponent.jsx ' ; import MyAstroComponent from ' ../components/MyAstroComponent.astro ' ; --- &#x3C; MyReactComponent > &#x3C; MyAstroComponent slot = " name " /> &#x3C;/ MyReactComponent > `   ">

## Can I hydrate Astro components?
 Section titled “Can I hydrate Astro components?”
 If you try to hydrate an Astro component with a `client:` modifier, you will get an error.

 Astro components are HTML-only templating components with no client-side runtime. But, you can use a `&#x3C;script>` tag in your Astro component template to send JavaScript to the browser that executes in the global scope.

 Learn more about client-side `&#x3C;script>` tags in Astro components

 Learn

 Contribute

 Community

 Sponsor