# Astro - Content


## Markdown Content

# Markdown in Astro

 Markdown is commonly used to author text-heavy content like blog posts and documentation. Astro includes built-in support for Markdown files that can also include frontmatter YAML (or TOML ) to define custom properties such as a title, description, and tags.

In Astro, you can author content in GitHub Flavored Markdown , then render it in `.astro` components. This combines a familiar writing format designed for content with the flexibility of Astro’s component syntax and architecture.

## Organizing Markdown files
 Section titled “Organizing Markdown files”
 Your local Markdown files can be kept anywhere within your `src/` directory. Markdown files located within `src/pages/` will automatically generate Markdown pages on your site .

Your Markdown content and frontmatter properties are available to use in components through local file imports or when queried and rendered from data fetched by a content collections helper function .

### File imports vs content collections queries
 Section titled “File imports vs content collections queries”
 Local Markdown can be imported into `.astro` components using an `import` statement for a single file and Vite’s `import.meta.glob()` to query multiple files at once. The exported data from these Markdown files can then be used in the `.astro` component.

If you have groups of related Markdown files, consider defining them as collections . This gives you several advantages, including the ability to store Markdown files anywhere on your filesystem or remotely.

Collections use content-specific, optimized APIs for querying and rendering your Markdown content instead of file imports. Collections are intended for sets of data that share the same structure, such as blog posts or product items. When you define that shape in a schema, you additionally get validation, type safety, and Intellisense in your editor.

 See more about when to use content collections instead of file imports.

## Dynamic JSX-like expressions
 Section titled “Dynamic JSX-like expressions”
 After importing or querying Markdown files, you can write dynamic HTML templates in your `.astro` components that include frontmatter data and body content.

 - src/pages/posts/great-post.md ` --- title : ' The greatest post of all time ' author : ' Ben ' ---
 Here is my _ great _ post! `
 src/pages/my-posts.astro
```
` --- import * as greatPost from ' ./posts/great-post.md ' ; const compiled = await greatPost . compiledContent (); const posts = Object . values ( import. meta . glob ( ' ./posts/*.md ' , { eager: true } )); ---
 &#x3C; p > { greatPost . frontmatter . title } &#x3C;/ p > &#x3C; p > Written by: { greatPost . frontmatter . author } &#x3C;/ p >
 &#x3C; Fragment set:html = { compiled } />
 &#x3C; p > Post Archive: &#x3C;/ p > &#x3C; ul > { posts . map ( post => &#x3C; li >&#x3C; a href = { post . url } > { post . frontmatter . title } &#x3C;/ a >&#x3C;/ li > ) } &#x3C;/ ul > `
```
 {greatPost.frontmatter.title}
Written by: {greatPost.frontmatter.author}
 Post Archive:
  {posts.map(post => {post.frontmatter.title}
)} ">

### Available Properties
 Section titled “Available Properties”

#### Markdown from content collections queries
 Section titled “Markdown from content collections queries”
 When fetching data from your collections with the helper functions `getCollection()` or `getEntry()`, your Markdown’s frontmatter properties are available on a `data` object (e.g. `post.data.title`). Additionally, `body` contains the raw, uncompiled body content as a string.

The `render()` function returns your Markdown body content, a generated list of headings, as well as a modified frontmatter object after any remark or rehype plugins have been applied.

 Read more about using content returned by a collections query .

#### Importing Markdown
 Section titled “Importing Markdown”
 The following exported properties are available in your `.astro` component when importing Markdown using `import` or `import.meta.glob()`:

- `file` - The absolute file path (e.g. `/home/user/projects/.../file.md`).

- `url` - The URL of the page (e.g. `/en/guides/markdown-content`).

- `frontmatter` - Contains any data specified in the file’s YAML (or TOML) frontmatter.

- `&#x3C;Content />` - A component that returns the full, rendered contents of the file.

- `rawContent()` - A function that returns the raw Markdown document as a string.

- `compiledContent()` - An async function that returns the Markdown document compiled to an HTML string.

- `getHeadings()` - An async function that returns an array of all headings (`&#x3C;h1>` to `&#x3C;h6>`) in the file with the type: `{ depth: number; slug: string; text: string }[]`. Each heading’s `slug` corresponds to the generated ID for a given heading and can be used for anchor links.

An example Markdown blog post may pass the following `Astro.props` object:

 ` Astro . props = { file: " /home/user/projects/.../file.md " , url: " /en/guides/markdown-content/ " , frontmatter: { /** Frontmatter from a blog post */ title: " Astro 0.18 Release " , date: " Tuesday, July 27 2021 " , author: " Matthew Phillips " , description: " Astro 0.18 is our biggest release since Astro launch. " , }, getHeadings : () => [ { " depth " : 1 , " text " : " Astro 0.18 Release " , " slug " : " astro-018-release " }, { " depth " : 2 , " text " : " Responsive partial hydration " , " slug " : " responsive-partial-hydration " } /* ... */ ], rawContent : () => " # Astro 0.18 Release \n A little over a month ago, the first public beta [...] " , compiledContent : () => " &#x3C;h1>Astro 0.18 Release&#x3C;/h1> \n &#x3C;p>A little over a month ago, the first public beta [...]&#x3C;/p> " , } ` [ {&#x22;depth&#x22;: 1, &#x22;text&#x22;: &#x22;Astro 0.18 Release&#x22;, &#x22;slug&#x22;: &#x22;astro-018-release&#x22;}, {&#x22;depth&#x22;: 2, &#x22;text&#x22;: &#x22;Responsive partial hydration&#x22;, &#x22;slug&#x22;: &#x22;responsive-partial-hydration&#x22;} /* ... */ ], rawContent: () => &#x22;# Astro 0.18 Release\nA little over a month ago, the first public beta [...]&#x22;, compiledContent: () => &#x22;
# Astro 0.18 Release
\n A little over a month ago, the first public beta [...]
&#x22;,}">

## The `&#x3C;Content />` Component
 Section titled “The &#x3C;Content /> Component”
 The `&#x3C;Content />` component is available by importing `Content` from a Markdown file. This component returns the file’s full body content, rendered to HTML. You can optionally rename `Content` to any component name you prefer.

You can similarly render the HTML content of a Markdown collection entry by rendering a `&#x3C;Content />` component.

 src/pages/content.astro ` --- // Import statement import { Content as PromoBanner} from ' ../components/promoBanner.md ' ;
 // Collections query import { getEntry, render } from ' astro:content ' ;
 const product = await getEntry ( ' products ' , ' shirt ' ); const { Content } = await render (product); --- &#x3C; h2 > Today's promo &#x3C;/ h2 > &#x3C; PromoBanner />
 &#x3C; p > Sale Ends: { product . data . saleEndDate . toDateString () } &#x3C;/ p > &#x3C; Content /> `  Sale Ends: {product.data.saleEndDate.toDateString()}
 ">

## Heading IDs
 Section titled “Heading IDs”
 Writing headings in Markdown will automatically give you anchor links so you can link directly to certain sections of your page.

 src/pages/page-1.md ` --- title : My page of content --- ## Introduction
 I can link internally to [ my conclusion ] ( #conclusion ) on the same page when writing Markdown.
 ## Conclusion
 I can visit `https://example.com/page-1/#introduction` in a browser to navigate directly to my Introduction. `
 Astro generates heading `id`s based on `github-slugger`. You can find more examples in the github-slugger documentation .

### Heading IDs and plugins
 Section titled “Heading IDs and plugins”
 Astro injects an `id` attribute into all heading elements (`&#x3C;h1>` to `&#x3C;h6>`) in Markdown and MDX files. You can retrieve this data from the `getHeadings()` utility available as a Markdown exported property from an imported file, or from the `render()` function when using Markdown returned from a content collections query .

You can customize these heading IDs with a Markdown processor plugin that injects `id` attributes (e.g. `rehype-slug`). Your custom IDs, instead of Astro’s defaults, will be reflected in the HTML output and the items returned by `getHeadings()`.

Astro injects `id` attributes after your custom plugins have run, so any ID set by a plugin is preserved. If one of your custom plugins needs to access the IDs injected by Astro, you can import Astro’s heading ids plugin and place it before any plugins that rely on it:

 -

 Unified

-

 Sätteri

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { unified, rehypeHeadingIds } from ' @astrojs/markdown-remark ' ; import { otherPluginThatReliesOnHeadingIDs } from ' some/plugin/source ' ;
 export default defineConfig ({ markdown: { processor: unified ({ rehypePlugins: [ rehypeHeadingIds , otherPluginThatReliesOnHeadingIDs , ], }), }, }); `

 astro.config.mjs
```
` import { defineConfig } from ' astro/config ' ; import { satteri, satteriHeadingIdsPlugin } from ' @astrojs/markdown-satteri ' ; import { otherPluginThatReliesOnHeadingIDs } from ' some/plugin/source ' ;
 export default defineConfig ({ markdown: { processor: satteri ({ hastPlugins: [ satteriHeadingIdsPlugin (), otherPluginThatReliesOnHeadingIDs , ], }), }, }); `
```

## Markdown Plugins
 Section titled “Markdown Plugins”
 Astro renders Markdown using a configurable Markdown processor . By default, this is the unified pipeline of remark and rehype , with an active plugin ecosystem.

Astro applies GitHub-Flavored Markdown and SmartyPants automatically. This brings some niceties like generating clickable links from text, and formatting for quotations and em-dashes.

You can extend Markdown processing with plugins, enable additional parser features, or switch to a different processor entirely . See the full list of Markdown configuration options .

### Choosing a Markdown processor
 Section titled “Choosing a Markdown processor”
 The `markdown.processor` option controls which engine renders your `.md` and `.mdx` files. Astro provides two official options:

- `unified()` (default): the remark and rehype pipeline, with its large plugin ecosystem.

- `satteri()` : the native Sätteri pipeline, a faster Markdown and MDX compiler with its own plugin model. Provided by `@astrojs/markdown-satteri`, which you install separately.

### Using remark and rehype plugins
 Section titled “Using remark and rehype plugins”
 The default `unified()` processor accepts third-party remark and rehype plugins. These plugins allow you to extend your Markdown with new capabilities, like auto-generating a table of contents , applying accessible emoji labels , and styling your Markdown .

We encourage you to browse awesome-remark and awesome-rehype for popular plugins! See each plugin’s own README for specific installation instructions.

Import `unified` from `@astrojs/markdown-remark` and pass your plugins to it through `markdown.processor`. This example applies `remark-toc` and `rehype-accessible-emojis` to Markdown files:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { unified } from ' @astrojs/markdown-remark ' ; import remarkToc from ' remark-toc ' ; import { rehypeAccessibleEmojis } from ' rehype-accessible-emojis ' ;
 export default defineConfig ({ markdown: { processor: unified ({ remarkPlugins: [[ remarkToc , { heading: ' toc ' , maxDepth: 3 }]], rehypePlugins: [ rehypeAccessibleEmojis ], }), }, }); `

### Customizing a remark or rehype plugin
 Section titled “Customizing a remark or rehype plugin”
 In order to customize a plugin, provide an options object after it in a nested array.

The example below adds the heading option to the `remarkToc` plugin to change where the table of contents is placed, and the `behavior` option to the `rehype-autolink-headings` plugin in order to add the anchor tag after the headline text.

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { unified } from ' @astrojs/markdown-remark ' ; import remarkToc from ' remark-toc ' ; import rehypeSlug from ' rehype-slug ' ; import rehypeAutolinkHeadings from ' rehype-autolink-headings ' ;
 export default defineConfig ({ markdown: { processor: unified ({ remarkPlugins: [[ remarkToc , { heading: ' contents ' }]], rehypePlugins: [ rehypeSlug , [ rehypeAutolinkHeadings , { behavior: ' append ' }]], }), }, }); `

### Switching to the Sätteri processor
 Section titled “Switching to the Sätteri processor”
 To use Sätteri instead of remark and rehype, install `@astrojs/markdown-satteri`, then import `satteri` and pass it to `markdown.processor`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { satteri } from ' @astrojs/markdown-satteri ' ; import { myMdastPlugin } from ' ./my-satteri-plugin.mjs ' ;
 export default defineConfig ({ markdown: { processor: satteri ({ mdastPlugins: [ myMdastPlugin ()], features: { directive: true }, }), }, }); `
 The Sätteri processor accepts its own plugins through `mdastPlugins` and `hastPlugins`, and toggles optional parser features through `features`. See the Sätteri documentation for the available plugins and features.

Switching processors replaces remark and rehype for both `.md` and `.mdx` files. Any remark or rehype plugins in your config will not apply. To use Sätteri only for `.mdx` files, set the `processor` option on the MDX integration instead.

### Modifying frontmatter programmatically
 Section titled “Modifying frontmatter programmatically”
 When using the remark/rehype processor , you can add frontmatter properties to all of your Markdown and MDX files with a remark or rehype plugin.

-
Append a `customProperty` to the `data.astro.frontmatter` property from your plugin’s `file` argument:

 example-remark-plugin.mjs ` export function exampleRemarkPlugin () { // All remark and rehype plugins return a separate function return function ( tree , file ) { file . data . astro . frontmatter . customProperty = ' Generated property ' ; } } `

-
 Apply this plugin to your `markdown` or `mdx` integration config:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { unified } from ' @astrojs/markdown-remark ' ; import { exampleRemarkPlugin } from ' ./example-remark-plugin.mjs ' ;
 export default defineConfig ({ markdown: { processor: unified ({ remarkPlugins: [ exampleRemarkPlugin ] }), }, }); `
 or

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import mdx from ' @astrojs/mdx ' ; import { unified } from ' @astrojs/markdown-remark ' ; import { exampleRemarkPlugin } from ' ./example-remark-plugin.mjs ' ;
 export default defineConfig ({ integrations: [ mdx ({ processor: unified ({ remarkPlugins: [ exampleRemarkPlugin ] }), }), ], }); `

 Now, every Markdown or MDX file will have `customProperty` in its frontmatter, making it available when importing your markdown and from the `Astro.props.frontmatter` property in your layouts .

 Related recipe:

 Add reading time

### Extending Markdown config from MDX
 Section titled “Extending Markdown config from MDX”
 Astro’s MDX integration will extend your project’s existing Markdown configuration by default, including the Markdown processor . To override individual options, you can specify their equivalent in your MDX configuration.

The following example uses a different syntax highlighter and a different set of plugins for `.mdx` files than for `.md` files:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { unified } from ' @astrojs/markdown-remark ' ; import mdx from ' @astrojs/mdx ' ;
 export default defineConfig ({ markdown: { syntaxHighlight: ' prism ' , processor: unified ({ remarkPlugins: [remarkPlugin1] }), }, integrations: [ mdx ({ // `markdown.syntaxHighlight` gets overridden for `.mdx` files by this option syntaxHighlight: ' shiki ' ,
 // `markdown.processor` gets overridden for `.mdx` files with a different remark plugin processor: unified ({ remarkPlugins: [remarkPlugin2] }), }) ] }); `
 To avoid extending your Markdown config from MDX, set the `extendMarkdownConfig` option (enabled by default) to `false`:

 astro.config.mjs ` import { defineConfig } from ' astro/config ' ; import { unified } from ' @astrojs/markdown-remark ' ; import mdx from ' @astrojs/mdx ' ;
 export default defineConfig ({ markdown: { processor: unified ({ remarkPlugins: [remarkPlugin] }), }, integrations: [ mdx ({ // Markdown config now ignored extendMarkdownConfig: false , // Default `unified()` processor used with no plugins }) ] }); `

## Individual Markdown pages
 Section titled “Individual Markdown pages”

 Astro treats any supported file inside of the `/src/pages/` directory as a page, including `.md` and other Markdown file types.

Placing a file in this directory, or any sub-directory, will automatically build a page route using the pathname of the file and display the Markdown content rendered to HTML. Astro will automatically add a `&#x3C;meta charset="utf-8">` tag to your page to allow easier authoring of non-ASCII content.

 src/pages/page-1.md ` --- title : Hello, World ---
 # Hi there!
 This Markdown file creates a page at `your-domain.com/page-1/`
 It probably isn't styled much, but Markdown does support: - ** bold ** and _ italics. _ - lists - [ links ] ( https://astro.build ) - &#x3C; p > HTML elements &#x3C;/ p > - and more! ` HTML elements
- and more!">

### Frontmatter `layout` property
 Section titled “Frontmatter layout property”
 To help with the limited functionality of individual Markdown pages, Astro provides a special frontmatter `layout` property which is a relative path to an Astro Markdown layout component . `layout` is not a special property when using content collections to query and render your Markdown content, and is not guaranteed to be supported outside of its intended use case.

If your Markdown file is located within `src/pages/`, create a layout component and add it in this layout property to provide a page shell around your Markdown content.

 src/pages/posts/post-1.md ` --- layout : ../../layouts/BlogPostLayout.astro title : Astro in brief author : Himanshu description : Find out what makes Astro awesome! --- This is a post written in Markdown. `
 This layout component is a regular Astro component with specific properties automatically available through `Astro.props` for your Astro template. For example, you can access your Markdown file’s frontmatter properties through `Astro.props.frontmatter`:

 src/layouts/BlogPostLayout.astro ` --- const { frontmatter } = Astro . props ; --- &#x3C; html > &#x3C; head > &#x3C;!-- ... --> &#x3C; meta charset = " utf-8 " > // no longer added by default &#x3C;/ head > &#x3C;!-- ... --> &#x3C; h1 > { frontmatter . title } &#x3C;/ h1 > &#x3C; h2 > Post author: { frontmatter . author } &#x3C;/ h2 > &#x3C; p > { frontmatter . description } &#x3C;/ p > &#x3C; slot /> &#x3C;!-- Markdown content is injected here --> &#x3C;!-- ... --> &#x3C;/ html > `    // no longer added by default  
# {frontmatter.title}

## Post author: {frontmatter.author}
 {frontmatter.description}
   ">
When using the frontmatter `layout` property, you must include the `&#x3C;meta charset="utf-8">` tag in your layout as Astro will no longer add it automatically. You can now also style your Markdown in your layout component.

 Learn more about Markdown Layouts .

## Fetching Remote Markdown
 Section titled “Fetching Remote Markdown”
 Astro’s internal Markdown processor is not available for processing remote Markdown.

To fetch remote Markdown for use in content collections , you can build a custom loader with access to a `renderMarkdown()` function .

To fetch remote Markdown directly and render it to HTML, you will need to install and configure your own Markdown parser from NPM. This will not inherit from any of Astro’s built-in Markdown settings that you have configured.

Be sure that you understand these limitations before implementing this in your project, and consider fetching your remote Markdown using a content collections loader instead.

 src/pages/remote-example.astro
```
` --- // Example: Fetch Markdown from a remote API // and render it to HTML, at runtime. // Using "marked" (https://github.com/markedjs/marked) import { marked } from ' marked ' ; const response = await fetch ( ' https://raw.githubusercontent.com/wiki/adam-p/markdown-here/Markdown-Cheatsheet.md ' ); const markdown = await response . text (); const content = marked . parse (markdown); --- &#x3C; article set:html = { content } /> `
```
 ">

 Learn

 Contribute

 Community

 Sponsor

## Content Collections

# Content collections

 Added in:
 `astro@2.0.0`

 Content collections are the best way to manage sets of content in any Astro project: blog posts, product descriptions, character profiles, recipes, or any structured content. Collections help to organize and query your documents, enable Intellisense and type checking in your editor, and provide automatic TypeScript type-safety for all of your content.

Astro provides performant, scalable APIs to load, query, and render content from anywhere: stored locally in your project, hosted remotely, or fetched live from frequently-updating sources.

## What are Content Collections?
 Section titled “What are Content Collections?”
 A content collection is a set of related, structurally identical data. This data can be stored in one or several files locally (e.g. a folder of individual Markdown files of blog posts, a single JSON file of product descriptions) or fetched from remote sources such as a database, CMS, or API endpoint. Each member of the collection is called an entry.

 - Directory src/ …
 - Directory newsletter/ the “newsletter” collection
 week-1.md a collection entry
- week-2.md a collection entry
- week-3.md a collection entry
 - Directory authors/ the “author” collection
 authors.json a single file containing all collection entries

 Collections are defined by the location and shape of its entries and provide a convenient way to query and render your content and associated metadata. You can create a collection any time you have a group of related data or content, stored in the same location, that shares a common structure.

 Two types of content collections are available to allow you to work with data fetched either at build time or at request time. Both build-time collections and live updating collections use:

- A required `loader` to retrieve your content and metadata from wherever it is stored and make it available to your project through content-focused APIs.

- An optional collection `schema` that allows you to define the expected shape of each entry for type safety, autocomplete, and validation in your editor.

Collections stored locally in your project or on your filesystem can use one of Astro’s provided build-time loaders to fetch data from Markdown, MDX, Markdoc, YAML, TOML, or JSON files. Point Astro to the location of your content, define your data shape, and you’re good to go with a blog or similarly content-heavy, mostly static site in no time!

With community-built loaders or by building a custom build-time collection loader or live loader yourself, you can fetch remote data from any external source, such as a CMS, database, or headless payment system, either at build time or live on demand.

### Types of collections
 Section titled “Types of collections”
 Build-time content collections are updated at build time, and data is saved to a storage layer. This provides excellent performance for most content, but may not be suitable for frequently updating data sources requiring up-to-the-moment data freshness, such as live stock prices.

For the best performance and scalability, use build-time content collections when one or more of these is true:

- Performance is critical and you want to prerender data at build time.

- Your data is relatively static (e.g., blog posts, documentation, product descriptions).

- You want to benefit from build-time optimization and caching.

- You need to process MDX or perform image optimization .

- Your data can be fetched once and reused across multiple builds.

 Live content collections fetch their data at runtime rather than build time. This allows you to access frequently updated data from CMSs, APIs, databases, or other sources using a unified API, without needing to rebuild your site when the data changes. However, this can come at a performance cost since data is fetched at each request and returned directly with no data store persistence.

Live content collections are designed for data that changes frequently and needs to be up-to-date when a page is requested. Consider using them when one or more of these is true:

- You need real-time information (e.g. user-specific data, current stock levels).

- You want to avoid constant rebuilds for content that changes often.

- Your data updates frequently (e.g. up-to-the-minute product inventory, prices, availability).

- You need to pass dynamic filters to your data source based on user input or request parameters.

- You’re building preview functionality for a CMS where editors need to see draft content immediately.

Both kinds of collections can exist in the same project, so you can always choose the best type of collection for each individual data source. For example, a build-time collection can manage product descriptions, while a live collection can manage content inventory.

Both types of collections use similar APIs (e.g. `getCollection()` and `getLiveCollection()`), so that working with collections will feel familiar no matter which one you choose, while still ensuring that you always know which type of collection you are working with.

We suggest using build-time content collections whenever possible, and using live collections when your content needs updating in real time and the performance tradeoffs are acceptable. Additionally, live content collections have some limitations compared to build-time collections:

- No MDX support : MDX cannot be rendered at runtime

- No image optimization : Images cannot be processed at runtime

- Performance considerations : Data is fetched on each request (unless cached)

- No data store persistence : Data is not saved to the content layer data store

### When to create a collection
 Section titled “When to create a collection”
 Define your data as a collection when:

- You have multiple files or data to organize that share the same overall structure (e.g. a directory of blog posts written in Markdown which all have the same frontmatter properties).

- You have existing content stored remotely, such as in a CMS, and want to take advantage of the collections helper functions instead of using `fetch()` or SDKs.

- You need to fetch (tens of) thousands of related pieces of data at build time, and need a querying and caching method that handles at scale.

Much of the benefit of using collections comes from:

- Defining a common data shape to validate that an individual entry is “correct” or “complete”, avoiding errors in production.

- Content-focused APIs designed to make querying intuitive (e.g. `getCollection()` instead of `import.meta.glob()`) when importing and rendering content on your pages.

- Access to both built-in loaders and access to the low-level Content Loader API for retrieving your content. There are additionally several third-party and community-built loaders available, and you can build your own custom loader to fetch data from anywhere.

- Performance and scalability. Build-time content collections data can be cached between builds and is suitable for tens of thousands of content entries.

### When not to create a collection
 Section titled “When not to create a collection”
 Collections provide excellent structure, safety, and organization when you have multiple pieces of content that must share the same properties.

Collections may not be your solution if:

- You have only one or a small number of different content pages. Consider making individual page components such as `src/pages/about.astro` with your content directly instead.

- You are displaying files that are not processed by Astro, such as PDFs. Place these static assets in the `public/` directory of your project instead.

- Your data source has its own SDK/client library for imports that is incompatible with or does not offer a content loader, and you prefer to use it directly.

## TypeScript configuration for collections
 Section titled “TypeScript configuration for collections”
 Content collections rely on TypeScript to provide Zod validation, Intellisense, and type checking in your editor. By default, Astro configures a `strict` TypeScript template when you create a new project using the `create astro` CLI command. Both of Astro’s `strict` and `strictest` templates include the TypeScript settings your project needs for content collections.

If you changed this setting to `base` because you are not writing TypeScript in your project, or are not using any of Astro’s built-in templates, you will need to also add the following `compilerOptions` in your `tsconfig.json` to use content collections:

 - tsconfig.json ` { "extends" : " astro/tsconfigs/base " , // not needed for `strict` or `strictest` "compilerOptions" : { "strictNullChecks" : true , "allowJs" : true } } `

## Defining build-time content collections
 Section titled “Defining build-time content collections”
 All of your build-time content collections are defined in a special `src/content.config.ts` file (`.js` and `.mjs` extensions are also supported) using `defineCollection()`, and then a single collections object is exported for use in your project.

Each individual collection configures:

 a build-time `loader` for a data source (required)

- a build-time `schema` for type safety (optional, but highly recommended!)

 src/content.config.ts ` // 1. Import utilities from `astro:content` import { defineCollection } from ' astro:content ' ;
 // 2. Import loader(s) import { glob, file } from ' astro/loaders ' ;
 // 3. Import Zod import { z } from ' astro/zod ' ;
 // 4. Define a `loader` and `schema` for each collection const blog = defineCollection ( { loader: glob ( { base: ' ./src/content/blog ' , pattern: ' **/*.{md,mdx} ' } ) , schema: z . object ( { title: z . string () , description: z . string () , pubDate: z . coerce . date () , updatedDate: z . coerce . date () . optional () , } ) , } );
 // 5. Export a single `collections` object to register your collection(s) export const collections = { blog } ; `
 You can then use the dedicated `getCollection()` and `getEntry()` functions to query your content collections data and render your content.

You can choose to generate page routes from your build-time collection entries at build time for an entirely static, prerendered site. Or, you can render your build-time collections on demand, choosing to delay building your page until it is first requested. This is useful when you have a large number of pages (e.g. thousands or tens of thousands) and want to delay building a static page until it is needed.

## Build-time collection loaders
 Section titled “Build-time collection loaders”
 Astro provides two built-in loaders (`glob()` and `file()`) for fetching your local content at build time. Pass the location of your data in your project or on your filesystem, and these loaders will automatically handle your data and update the persistent data store content layer.

To fetch remote data at build time, you can build a custom loader to retrieve your data and update the data store. Or, you can use any third-party or community-published loader integration . Several already exist for popular content management systems as well as common data sources such as Obsidian vaults, GitHub repositories, or Bluesky posts.

### The `glob()` loader
 Section titled “The glob() loader”
 The `glob()` loader fetches entries from directories of Markdown, MDX, Markdoc, JSON, YAML, or TOML files from anywhere on the filesystem. If you store your content entries locally as separate files, such as a directory of blog posts, then the `glob()` loader is all you need to access your content.

This loader requires a `pattern` of entry files to match using glob patterns supported by micromatch , and a `base` file path of where your files are located. A unique `id` for each entry will be automatically generated from its file name, but you can define custom IDs if needed.

 src/content.config.ts ` import { defineCollection } from ' astro:content ' ; import { glob } from ' astro/loaders ' ;
 const blog = defineCollection ( { loader: glob ( { pattern: " **/*.md " , base: " ./src/data/blog " } ) , } );
 export const collections = { blog } ; `

#### Defining custom IDs
 Section titled “Defining custom IDs”
 When using the `glob()` loader with Markdown, MDX, Markdoc, JSON, or TOML files, every content entry `id` is automatically generated in an URL-friendly format based on the content filename. This unique `id` is used to query the entry directly from your collection. It is also useful when creating new pages and URLs from your content .

You can override a single entry’s generated `id` by adding your own `slug` property to the file frontmatter or data object for JSON files. This is similar to the “permalink” feature of other web frameworks.

 src/blog/1.md ` --- title : My Blog Post slug : my-custom-id/supports/slashes --- Your blog post content here. `
 src/categories/1.json
```
` { "title" : " My Category " , "slug" : " my-custom-id/supports/slashes " , "description" : " Your category description here. " } `
```

 You can also pass options to the `glob()` loader’s `generateID()` helper function when you define your build-time collection to adjust how `id`s are generated. For example, you may wish to revert the default behavior of converting uppercase letters to lowercase for each collection entry:

 src/content.config.ts ` const authors = defineCollection ( { /* Retrieve all JSON files in your authors directory while retaining * uppercase letters in the ID. */ loader: glob ( { pattern: ' **/*.json ' , base: " ./src/data/authors " , generateId : ( { entry } ) => entry . replace ( / \. json $ / , '' ) , } ) , } ); ` entry.replace(/\.json$/, &#x27;&#x27;), }),});">

### The `file()` loader
 Section titled “The file() loader”
 The `file()` loader fetches multiple entries from a single local file defined in your collection. The `file()` loader will automatically detect and parse (based on the file extension) a single array of objects from JSON and YAML files, and will treat each top-level table as an independent entry in TOML files.

 src/content.config.ts ` import { defineCollection } from ' astro:content ' ; import { file } from ' astro/loaders ' ;
 const dogs = defineCollection ( { loader: file ( " src/data/dogs.json " ) , } );
 export const collections = { dogs } ; `
 Each entry object in the file must have a unique `id` key property so that the entry can be identified and queried. Unlike the `glob()` loader, the `file()` loader will not automatically generate IDs for each entry.

You can provide your entries as an array of objects with an `id` property, or in object form where the unique `id` is the key:

 src/data/dogs.json ` // Specify an `id` property in each object of an array [ { "id" : " poodle " , "coat" : " curly " , "shedding" : " low " }, { "id" : " afghan " , "coat" : " short " , "shedding" : " low " } ] `
 src/data/dogs.json
```
` // Each key will be used as the `id` { "poodle" : { "coat" : " curly " , "shedding" : " low " }, "afghan" : { "coat" : " silky " , "shedding" : " low " } } `
```

#### Parsing other data formats
 Section titled “Parsing other data formats”
 Support for parsing single JSON, YAML, and TOML files into collection entries with the `file()` loader is built-in (unless you have a nested JSON document ). To load your collection from unsupported file types, such as `.csv`, you will need to create a parser function . This function can be made async if required (e.g. to fetch files from the web, or if your parser is asynchronous).

The following example shows importing a third-party CSV parser then passing a custom `parser` function to the `file()` loader:

 src/content.config.ts ` import { defineCollection } from " astro:content " ; import { file } from " astro/loaders " ; import { parse as parseCsv } from " csv-parse/sync " ;
 const cats = defineCollection ( { loader: file ( " src/data/cats.csv " , { parser : ( text ) => parseCsv (text , { columns: true , skipEmptyLines: true } ) , } ) , } ); ` parseCsv(text, { columns: true, skipEmptyLines: true }), }),});">
 Nested `.json` documents Section titled “Nested .json documents”
 The `parser()` argument can be used to load a single collection from a nested JSON document. For example, this JSON file contains multiple collections:

 src/data/pets.json ` { "dogs" : [{}], "cats" : [{}]} `
 You can separate these collections by passing a custom `parser()` function to the `file()` loader for each collection, using Astro’s built-in JSON parsing:

 src/content.config.ts ` import { file } from " astro/loaders " ; import { defineCollection } from " astro:content " ;
 const dogs = defineCollection ( { loader: file ( " src/data/pets.json " , { parser : ( text ) => JSON . parse (text) . dogs } ) } ); const cats = defineCollection ( { loader: file ( " src/data/pets.json " , { parser : ( text ) => JSON . parse (text) . cats } ) } ); ` JSON.parse(text).dogs })});const cats = defineCollection({ loader: file(&#x22;src/data/pets.json&#x22;, { parser: (text) => JSON.parse(text).cats })});">

### Custom build-time loaders
 Section titled “Custom build-time loaders”
 You can build a custom loader using the Content Loader API to fetch remote content from any data source, such as a CMS, a database, or an API endpoint.

Then you can import and define your custom loader in your collections config, passing any required values:

 src/content.config.ts ` import { defineCollection } from ' astro:content ' ; import { myLoader } from ' ./loader.ts ' ;
 const blog = defineCollection ( { loader: myLoader ( { url: " https://api.example.com/posts " , apiKey: " my-secret " , } ) , } ); `

 Using a custom loader to fetch your data will automatically create a collection from your remote data. This gives you all the benefits of local collections, including collection-specific API helpers such as `getCollection()` and `render()` to query and display your data , as well as schema validation.

Similar to creating an Astro integration or Vite plugin, you can distribute your loader as an npm package that others can use in their projects.

 See the full Content Loader API for examples of how to build your own loader.

## Defining the collection schema
 Section titled “Defining the collection schema”
 Schemas enforce consistent frontmatter or entry data within a collection through Zod validation. A schema guarantees that this data exists in a predictable form when you need to reference or query it. If any file violates its collection schema, Astro will provide a helpful error to let you know.

Schemas also power Astro’s automatic TypeScript typings for your content. When you define a schema for your collection, Astro will automatically generate and apply a TypeScript interface to it. The result is full TypeScript support when you query your collection, including property autocompletion and type-checking.

Providing a `schema` is optional, but highly recommended! If you choose to use a schema, then every frontmatter or data property of your collection entries must be defined using a Zod data type :

 src/content.config.ts ` import { defineCollection } from ' astro:content ' ; import { z } from ' astro/zod ' ; import { glob, file } from ' astro/loaders ' ;
 const blog = defineCollection ( { loader: glob ( { pattern: " **/*.md " , base: " ./src/data/blog " } ) , schema: z . object ( { title: z . string () , description: z . string () , pubDate: z . coerce . date () , updatedDate: z . coerce . date () . optional () , } ) } ); const dogs = defineCollection ( { loader: file ( " src/data/dogs.json " ) , schema: z . object ( { id: z . string () , breed: z . string () , temperament: z . array (z . string ()) , } ) , } );
 export const collections = { blog , dogs } ; `

### Defining datatypes with Zod
 Section titled “Defining datatypes with Zod”
 Astro uses Zod to power its content schemas. With Zod, Astro is able to validate every file’s data within a collection and provide automatic TypeScript types when you query content from inside your project.

To use Zod in Astro, import the `z` utility from `"astro/zod"`. This is a re-export of the Zod library, and it supports all of the features of Zod 4.

 See the `z` utility reference for a cheatsheet of common datatypes and to learn how Zod works and what features are available.

#### Zod schema methods
 Section titled “Zod schema methods”
 All Zod schema methods (e.g. `.parse()`, `.transform()`) are available, with some limitations. Notably, performing custom validation checks on images using `image().refine()` is unsupported.

### Defining collection references
 Section titled “Defining collection references”
 Collection entries can also “reference” other related entries.

With the `reference()` function , you can define a property in a collection schema as an entry from another collection. For example, you can require that every `space-shuttle` entry includes a `pilot` property which uses the `pilot` collection’s own schema for type checking, autocomplete, and validation.

A common example is a blog post that references reusable author profiles stored as JSON, or related post URLs stored in the same collection:

 src/content.config.ts ` import { defineCollection, reference } from ' astro:content ' ; import { glob } from ' astro/loaders ' ; import { z } from ' astro/zod ' ;
 const blog = defineCollection ( { loader: glob ( { base: ' ./src/content/blog ' , pattern: ' **/*.{md,mdx} ' } ) , schema: z . object ( { title: z . string () , // Reference a single author from the `authors` collection by `id` author: reference ( ' authors ' ) , // Reference an array of related posts from the `blog` collection by `id` relatedPosts: z . array ( reference ( ' blog ' )) , } ) } );
 const authors = defineCollection ( { loader: glob ( { pattern: ' **/*.json ' , base: " ./src/data/authors " } ) , schema: z . object ( { name: z . string () , portfolio: z . url () , } ) } );
 export const collections = { blog , authors } ; `
 This example blog post specifies the `id`s of related posts and the `id` of the post author:

 src/content/blog/welcome.md ` --- title : " Welcome to my blog " author : ben-holmes # references `src/data/authors/ben-holmes.json` relatedPosts : - about-me # references `src/content/blog/about-me.md` - my-year-in-review # references `src/content/blog/my-year-in-review.md` --- `
 These references will be transformed into objects containing a `collection` key and an `id` key, allowing you to easily query them in your templates .

## Querying build-time collections
 Section titled “Querying build-time collections”
 Astro provides helper functions to query a build-time collection and return one or more content entries.

- `getCollection()` fetches an entire collection and returns an array of entries.

- `getEntry()` fetches a single entry from a collection.

These return entries with a unique `id`, a `data` object with all defined properties, and will also return a `body` containing the raw, uncompiled body of a Markdown, MDX, or Markdoc document.

 src/pages/index.astro ` --- import { getCollection, getEntry } from ' astro:content ' ;
 // Get all entries from a collection. // Requires the name of the collection as an argument. const allBlogPosts = await getCollection ( ' blog ' );
 // Get a single entry from a collection. // Requires the name of the collection and `id` const poodleData = await getEntry ( ' dogs ' , ' poodle ' ); --- `
 The sort order of generated collections is non-deterministic and platform-dependent. This means that if you are calling `getCollection()` and need your entries returned in a specific order (e.g. blog posts sorted by date), you must sort the collection entries yourself:

 src/pages/blog.astro ` --- import { getCollection } from ' astro:content ' ;
 const posts = ( await getCollection ( ' blog ' )) . sort ( ( a , b ) => b . data . pubDate . valueOf () - a . data . pubDate . valueOf () , ); --- ` b.data.pubDate.valueOf() - a.data.pubDate.valueOf(),);---">

 See the full list of properties returned by the `CollectionEntry` type .

### Using content in Astro templates
 Section titled “Using content in Astro templates”
 After querying your collections, you can access each entry’s content and metadata directly inside of your Astro component template.

For example, you can create a list of links to your blog posts, displaying information from your entry’s frontmatter using the `data` property:

 src/pages/index.astro ` --- import { getCollection } from ' astro:content ' ; const posts = await getCollection ( ' blog ' ); --- &#x3C; h1 > My posts &#x3C;/ h1 > &#x3C; ul > { posts . map ( post => ( &#x3C; li >&#x3C; a href = { ` /blog/ ${ post . id } ` } > { post . data . title } &#x3C;/ a >&#x3C;/ li > )) } &#x3C;/ ul > `  {posts.map(post => ( - {post.data.title}
 ))} ">

### Rendering body content
 Section titled “Rendering body content”
 Once queried, you can render Markdown and MDX entries to HTML using the `render()` function from `astro:content`. Calling this function gives you access to rendered HTML content, including both a `&#x3C;Content />` component and a list of all rendered headings.

 src/pages/blog/post-1.astro ` --- import { getEntry, render } from ' astro:content ' ;
 const entry = await getEntry ( ' blog ' , ' post-1 ' );
 const { Content } = await render (entry); --- &#x3C; h1 > { entry . data . title } &#x3C;/ h1 > &#x3C; p > Published on: { entry . data . published . toDateString () } &#x3C;/ p > &#x3C; Content /> ` Published on: {entry.data.published.toDateString()}
 ">

 When working with MDX entries, you can also pass your own components to `&#x3C;Content />` to replace HTML elements with custom alternatives.

#### Passing content as props
 Section titled “Passing content as props”
 A component can also pass an entire collection entry as a prop.

You can use the `CollectionEntry` utility to correctly type your component’s props using TypeScript. This utility takes a string argument that matches the name of your collection schema and will inherit all of the properties of that collection’s schema.

 src/components/BlogCard.astro ` --- import type { CollectionEntry } from ' astro:content ' ; interface Props { post : CollectionEntry &#x3C; ' blog ' > ; }
 // `post` will match your 'blog' collection schema type const { post } = Astro . props ; --- ` ;}// &#x60;post&#x60; will match your &#x27;blog&#x27; collection schema typeconst { post } = Astro.props;---">

### Filtering collection queries
 Section titled “Filtering collection queries”
 `getCollection()` takes an optional “filter” callback that allows you to filter your query based on an entry’s `id` or `data` properties.

You can use this to filter by any content criteria you like. For example, you can filter by properties like `draft` to prevent any draft blog posts from publishing to your blog:

 src/pages/blog.astro ` --- // Example: Filter out content entries with `draft: true` import { getCollection } from ' astro:content ' ; const publishedBlogEntries = await getCollection ( ' blog ' , ( { data } ) => { return data . draft !== true ; } ); --- ` { return data.draft !== true;});---">
 You can also create draft pages that are available when running the dev server, but not built in production:

 src/pages/blog.astro ` --- // Example: Filter out content entries with `draft: true` only when building for production import { getCollection } from ' astro:content ' ; const blogEntries = await getCollection ( ' blog ' , ( { data } ) => { return import. meta . env . PROD ? data . draft !== true : true ; } ); --- ` { return import.meta.env.PROD ? data.draft !== true : true;});---">
 The filter argument also supports filtering by nested directories within a collection. Since the `id` includes the full nested path, you can filter by the start of each `id` to only return items from a specific nested directory:

 src/pages/blog.astro ` --- // Example: Filter entries by sub-directory in the collection import { getCollection } from ' astro:content ' ; const englishDocsEntries = await getCollection ( ' docs ' , ( { id } ) => { return id . startsWith ( ' en/ ' ) ; } ); --- ` { return id.startsWith(&#x27;en/&#x27;);});---">

### Accessing referenced data
 Section titled “Accessing referenced data”
 To access references defined in your schema , first query your collection entry. Your references will be available on the returned `data` object. (e.g. `entry.data.author` and `entry.data.relatedPosts`)

Then, you can use the `getEntry()` function again (or `getEntries()` to retrieve multiple referenced entries) by passing those returned values. The `reference()` function in your schema transforms those values into one or more `collection` and `id` objects as a convenient way to query this related data.

 src/pages/blog/adventures-in-space.astro ` --- import { getEntry, getEntries } from ' astro:content ' ;
 // First, query a blog post const blogPost = await getEntry ( ' blog ' , ' Adventures in Space ' );
 // Retrieve a single reference item: the blog post's author // Equivalent to querying `{collection: "authors", id: "ben-holmes"}` const author = await getEntry (blogPost . data . author );
 // Retrieve an array of referenced items: all the related posts // Equivalent to querying `[{collection: "blog", id: "visiting-mars"}, {collection: "blog", id: "leaving-earth-for-the-first-time"}]` const relatedPosts = await getEntries (blogPost . data . relatedPosts ); ---
 &#x3C; h1 > { blogPost . data . title } &#x3C;/ h1 > &#x3C; p > Author: { author . data . name } &#x3C;/ p >
 &#x3C;!-- ... -->
 &#x3C; h2 > You might also like: &#x3C;/ h2 > { relatedPosts . map ( post => ( &#x3C; a href = { post . id } > { post . data . title } &#x3C;/ a > )) } ` Author: {author.data.name}

## You might also like:
{relatedPosts.map(post => ( {post.data.title} ))}">

## Generating Routes from Content
 Section titled “Generating Routes from Content”
 Content collections are stored outside of the `src/pages/` directory. This means that no pages or routes are generated for your collection items by default by Astro’s file-based routing .

You will need to manually create a new dynamic route if you want to generate HTML pages for each of your collection entries, such as individual blog posts. Your dynamic route will map the incoming request param (e.g. `Astro.params.id` in `src/pages/blog/[...id].astro`) to fetch the correct entry for each page.

The exact method for generating routes will depend on whether your pages are prerendered (default) or rendered on demand by a server.

### Building for static output (default)
 Section titled “Building for static output (default)”
 If you are building a static website (Astro’s default behavior) with build-time collections, use the `getStaticPaths()` function to create multiple pages from a single page component (e.g. `src/pages/[id].astro`) during your build.

Call `getCollection()` inside of `getStaticPaths()` to have your collection data available for building static routes. Then, create the individual URL paths using the `id` property of each content entry. Each page receives the entire collection entry as a prop for use in your page template .

 src/pages/posts/[id].astro ` --- import { getCollection, render } from ' astro:content ' ; // 1. Generate a new path for every collection entry export async function getStaticPaths () { const posts = await getCollection ( ' blog ' ); return posts . map ( post => ({ params: { id: post . id } , props: { post } , })); } // 2. For your template, you can get the entry directly from the prop const { post } = Astro . props ; const { Content } = await render (post); --- &#x3C; h1 > { post . data . title } &#x3C;/ h1 > &#x3C; Content /> ` ({ params: { id: post.id }, props: { post }, }));}// 2. For your template, you can get the entry directly from the propconst { post } = Astro.props;const { Content } = await render(post);---
# {post.data.title}
 ">
 This will generate a page route for every entry in the `blog` collection. For example, an entry at `src/blog/hello-world.md` will have an `id` of `hello-world`, and therefore its final URL will be `/posts/hello-world/`.

### Building routes on demand at request time
 Section titled “Building routes on demand at request time”
 With an adapter installed for on-demand rendering , you can generate your dynamic page routes at request time. First, examine the request (using `Astro.request` or `Astro.params`) to find the slug on demand, and then fetch it using one of Astro’s content collection helper functions:

- `getEntry()` for build-time collection pages that are generated once, upon first request.

- `getLiveEntry()` for live collection pages where data is (re)fetched at each request time.

 src/pages/posts/[id].astro ` --- export const prerender = false ; // Not needed in 'server' mode
 import { getEntry, render } from " astro:content " ;
 // 1. Get the slug from the incoming server request const { id } = Astro . params ; if (id === undefined ) { return Astro . redirect ( " /404 " ); }
 // 2. Query for the entry directly using the request slug const post = await getEntry ( " blog " , id);
 // 3. Redirect if the entry does not exist if (post === undefined ) { return Astro . redirect ( " /404 " ); }
 // 4. Render the entry to HTML in the template const { Content } = await render (post); --- &#x3C; h1 > { post . data . title } &#x3C;/ h1 > &#x3C; Content /> ` ">

## Live content collections
 Section titled “Live content collections”
 Live collections use a different API than build-time content collections, although the configuration and helper functions are designed to feel familiar.

Key differences include:

- Execution time : Run at request time instead of build time

- Configuration file : Use `src/live.config.ts` instead of `src/content.config.ts`

- Collection definition : Use `defineLiveCollection()` instead of `defineCollection()`

- Loader API : Implement `loadCollection` and `loadEntry` methods instead of the `load` method

- Data return : Return data directly instead of storing in the data store

- User-facing functions : Use `getLiveCollection()`/`getLiveEntry()` instead of `getCollection()`/`getEntry()`

Additionally, you must have an adapter configured for on-demand rendering of live collection data.

Define your live collections in the special file `src/live.config.ts` (separate from your `src/content.config.ts` for build-time collections, if you have one).

Each individual collection configures:

- a live `loader` for your data source, and optionally for type safety (required)

- a live collection `schema` for type safety (optional)

Unlike for build-time collections, there are no built-in live loaders available. You will need to create a custom live loader for your specific data source or find a third-party loader to pass to your live collection’s `loader` property.

You can optionally include type safety in your live loaders . Therefore, defining a Zod `schema` for live collections is optional. However, if you provide one, it will take precedence over the live loader’s types.

 src/live.config.ts ` // Define live collections for accessing real-time data import { defineLiveCollection } from ' astro:content ' ; import { storeLoader } from ' @mystore/astro-loader ' ;
 const products = defineLiveCollection ( { loader: storeLoader ( { apiKey: process . env . STORE_API_KEY , endpoint: ' https://api.mystore.com/v1 ' , } ) , } );
 // Export a single `collections` object to register your collection(s) export const collections = { products } ; `
 You can then use the dedicated `getLiveCollection()` and `getLiveEntry()` functions to access your live data and render your content.

You can generate page routes from your live collection entries on demand, fetching your data fresh at runtime upon each request without needing a rebuild of your site like build-time collections do. This is useful when accessing live, up-to-the-moment data is more important than having your content available in a performant data storage layer that persists between site builds.

### Creating a live loader
 Section titled “Creating a live loader”
 You can build a custom live loader using the Live Loader API to fetch remote content fresh upon request from any data source, such as a CMS, a database or an API endpoint. You will have to tell your live loader how to fetch and return content entries from your desired data source, as well as provide error handling for unsuccessful data requests.

Using a live loader to fetch your data will automatically create a collection from your remote data. This gives you all the benefits of Astro’s content collections, including collection-specific API helpers such as `getLiveCollection()` and `render()` to query and display your data , as well as helpful error handling.

 See the basics of building a live loader using the Live Loader API

### Using Zod schemas with live collections
 Section titled “Using Zod schemas with live collections”
 You can use Zod schemas with live collections to validate and transform data at runtime. This Zod validation works the same way as schemas for build-time collections .

When you define a schema for a live collection, it takes precedence over the live loader’s types when you query the collection:

 src/live.config.ts ` import { defineLiveCollection } from ' astro:content ' ; import { z } from ' astro/zod ' ; import { apiLoader } from ' ./loaders/api-loader ' ;
 const products = defineLiveCollection ( { loader: apiLoader ( { endpoint: process . env . API_URL } ) , schema: z . object ( { id: z . string () , name: z . string () , price: z . number () , // Transform the API's category format category: z . string () . transform ( ( str ) => str . toLowerCase () . replace ( / \s + / g , ' - ' )) , // Coerce the date to a Date object createdAt: z . coerce . date () , } ) . transform ( ( data ) => ( { ... data , // Add a formatted price field displayPrice: ` $ ${ data . price . toFixed ( 2 ) } ` , } )) , } );
 export const collections = { products } ; ` str.toLowerCase().replace(/\s+/g, &#x27;-&#x27;)), // Coerce the date to a Date object createdAt: z.coerce.date(), }) .transform((data) => ({ ...data, // Add a formatted price field displayPrice: &#x60;$${data.price.toFixed(2)}&#x60;, })),});export const collections = { products };">
 When using Zod schemas with live collections, validation errors are automatically caught and returned as `AstroError` objects:

 src/pages/store/index.astro ` --- export const prerender = false ; // Not needed in 'server' mode
 import { LiveCollectionValidationError } from ' astro/content/runtime ' ; import { getLiveEntry } from ' astro:content ' ;
 const { entry , error } = await getLiveEntry ( ' products ' , ' 123 ' );
 // You can handle validation errors specifically if (LiveCollectionValidationError . is (error)) { console . error (error . message ); return Astro . rewrite ( ' /500 ' ); }
 // TypeScript knows entry.data matches your Zod schema, not the loader's type console . log (entry ?. data . displayPrice ); // e.g., "$29.99" --- `

 See Zod’s README for complete documentation on how Zod works and what features are available.

### Accessing live data
 Section titled “Accessing live data”
 Astro provides live collection helper functions to access live data on each request and return one (or more) content entries. These can be used similarly to their build-time collection counterparts .

- `getLiveCollection()` fetches an entire collection and returns an array of entries.

- `getLiveEntry()` fetches a single entry from a collection.

These return entries with a unique `id`, and `data` object with all defined properties from the live loader. When using third-party or community loaders distributed as npm packages, check their own documentation for the expected shape of data returned.

You can use these functions to access your live data, passing the name of the collection and optionally filtering conditions.

 src/pages/store/[slug].astro ` --- export const prerender = false ; // Not needed in 'server' mode
 import { getLiveCollection, getLiveEntry } from ' astro:content ' ;
 // Use loader-specific filters const { entries : draftArticles } = await getLiveCollection ( ' articles ' , { status: ' draft ' , author: ' john-doe ' , } );
 // Get a specific product by ID const { entry : product } = await getLiveEntry ( ' products ' , Astro . params . slug ); --- `

#### Rendering content
 Section titled “Rendering content”
 If your live loader returns a `rendered` property , you can use the `render()` function and `&#x3C;Content />` component to render your content directly in your pages, using the same method as build-time collections.

You also have access to any error returned by the live loader , for example, to rewrite to a 404 page when content cannot be displayed:

 src/pages/store/[id].astro ` --- export const prerender = false ; // Not needed in 'server' mode
 import { getLiveEntry, render } from ' astro:content ' ; const { entry , error } = await getLiveEntry ( ' articles ' , Astro . params . id ); if (error) { return Astro . rewrite ( ' /404 ' ); }
 const { Content } = await render (entry) ; ---
 &#x3C; h1 > { entry . data . title } &#x3C;/ h1 > &#x3C; Content /> ` ">

#### Error handling
 Section titled “Error handling”
 Live loaders can fail due to network issues, API errors, or validation problems. The API is designed to make error handling explicit.

When you call `getLiveCollection()` or `getLiveEntry()`, the error will be one of:

- The error type defined by the loader (if it returned an error)

- A `LiveEntryNotFoundError` if the entry was not found

- A `LiveCollectionValidationError` if the collection data does not match the expected schema

- A `LiveCollectionCacheHintError` if the cache hint is invalid

- A `LiveCollectionError` for other errors, such as uncaught errors thrown in the loader

You can use `instanceof` to check the type of an error at runtime:

 src/pages/store/[id].astro ` --- export const prerender = false ; // Not needed in 'server' mode
 import { LiveEntryNotFoundError } from ' astro/content/runtime ' ; import { getLiveEntry } from ' astro:content ' ;
 const { entry , error } = await getLiveEntry ( ' products ' , Astro . params . id );
 if (error) { if (error instanceof LiveEntryNotFoundError ) { console . error ( ` Product not found: ${ error . message } ` ); Astro . response . status = 404 ; } else { console . error ( ` Error loading product: ${ error . message } ` ); return Astro . redirect ( ' /500 ' ); } } --- `

## Using JSON Schema files in your editor
 Section titled “Using JSON Schema files in your editor”

 Added in:
 `astro@4.13.0`

Astro auto-generates JSON Schema files for collections, which you can use in your editor to get IntelliSense and type-checking for data files.

A JSON Schema file is generated for each collection in your project and output to the `.astro/collections/` directory.
For example, if you have two collections, one named `authors` and another named `posts`, Astro will generate `.astro/collections/authors.schema.json` and `.astro/collections/posts.schema.json`.

### Use JSON Schemas in JSON files

You can manually point to an Astro-generated schema by setting the `$schema` field in your JSON file.
The value should be a relative file path from the data file to the schema.
In the following example, a data file in `src/data/authors/` uses the schema generated for the `authors` collection:

 src/data/authors/armand.json ` { "$schema" : " ../../../.astro/collections/authors.schema.json " , "name" : " Armand " , "skills" : [ " Astro " , " Starlight " ] } `

#### Use a schema for a group of JSON files in VS Code

 In VS Code, you can configure a schema to apply to all files in a collection using the `json.schemas` setting .
In the following example, all files in the `src/data/authors/` directory will use the schema generated for the `authors` collection:

 ` { "json.schemas" : [ { "fileMatch" : [ " /src/data/authors/** " ], "url" : " ./.astro/collections/authors.schema.json " } ] } `

### Use schemas in YAML files in VS Code

 In VS Code, you can add support for using JSON schemas in YAML files using the Red Hat YAML extension.
With this extension installed, you can reference a schema in a YAML file using a special comment syntax:

 src/data/authors/armand.yml ` # yaml-language-server: $schema=../../../.astro/collections/authors.schema.json name : Armand skills : - Astro - Starlight `

#### Use schemas for a group of YAML files in VS Code

 With the Red Hat YAML extension, you can configure a schema to apply to all YAML files in a collection using the `yaml.schemas` setting.
In the following example, all YAML files in the `src/data/authors/` directory will use the schema generated for the `authors` collection:

 ` { "yaml.schemas" : { "./.astro/collections/authors.schema.json" : [ " /src/content/authors/*.yml " ] } } `
 See “Associating schemas” in the Red Hat YAML extension documentation for more details.

 Learn

 Contribute

 Community

 Sponsor

## Images

# Images

 Astro provides several ways for you to use images on your site, whether they are stored locally inside your project, linked to from an external URL, or managed in a CMS or CDN.

Astro provides built-in `&#x3C;Image />` and `&#x3C;Picture />` Astro components, Markdown image syntax (`![]()`) processing, SVG components , and an image generating function to optimize and/or transform your images. Additionally, you can configure automatically resizing responsive images by default, or set responsive properties on individual image and picture components.

You can always choose to use images and SVG files using native HTML elements in `.astro` or Markdown files, or the standard way for your file type (e.g. `&#x3C;img />` in MDX and JSX). However, Astro does not perform any processing or optimization of these images.

There is also no native video support in Astro, and we recommend choosing a hosted video service to handle the demands of optimizing and streaming video content.

 See the full API reference for the `&#x3C;Image />` and `&#x3C;Picture />` components.

## Where to store images
 Section titled “Where to store images”

### `src/` vs `public/`
 Section titled “src/ vs public/”
 We recommend that local images are kept in `src/` when possible so that Astro can transform, optimize, and bundle them. Files in the `public/` directory are always served or copied into the build folder as-is, with no processing.

Your local images stored in `src/` can be used by all files in your project: `.astro`, `.md`, `.mdx`, `.mdoc`, and other UI frameworks as file imports. Images can be stored in any folder, including alongside your content.

Store your images in the `public/` folder if you want to avoid any processing. These images are available to your project files as URL paths on your domain and allow you to have a direct public link to them. For example, your site favicon will commonly be placed in the root of this folder where browsers can identify it.

### Remote images
 Section titled “Remote images”
 You can also choose to store your images remotely, in a content management system (CMS) or digital asset management (DAM) platform. Astro can fetch your data remotely using APIs or display images from their full URL path.

For extra protection when dealing with external sources, Astro’s image components and helper function will only process (e.g. optimize, transform) images from authorized image sources specified in your configuration . Remote images from other sources will be displayed with no processing.

## Images in `.astro` files
 Section titled “Images in .astro files”
 Options: `&#x3C;Image />`, `&#x3C;Picture />`, `&#x3C;img>`, `&#x3C;svg>`, SVG components

Astro’s templating language allows you to render optimized images with the Astro `&#x3C;Image />` component and generate multiple sizes and formats with the Astro `&#x3C;Picture />` component. Both components also accept responsive image properties for resizing based on container size and responding to device screen size and resolution.

Additionally, you can import and use SVG files as Astro components in `.astro` components.

All native HTML tags, including `&#x3C;img>` and `&#x3C;svg>`, are also available in `.astro` components. Images rendered with HTML tags will not be processed (e.g. optimized, transformed) and will be copied into your build folder as-is.

For all images in `.astro` files, the value of the image `src` attribute is determined by the location of your image file :

-
A local image from your project `src/` folder uses an import from the file’s relative path.

The image and picture components use the named import directly (e.g. `src={rocket}`), while the `&#x3C;img>` tag uses the `src` object property of the import (e.g. `src={rocket.src}`).

-
Remote and `public/` images use a URL path.

Provide a full URL for remote images (e.g. `src="https://www.example.com/images/my-remote-image.jpg"`), or a relative URL path on your site that corresponds to your file’s location in your `public/` folder (e.g. `src="/images/my-public-image.jpg"` for an image located in `public/images/my-public-image.jpg`).

 - src/pages/blog/my-images.astro ` --- import { Image } from ' astro:assets ' ; import localBirdImage from ' ../../images/subfolder/localBirdImage.png ' ; --- &#x3C; Image src = { localBirdImage } alt = " A bird sitting on a nest of eggs. " /> &#x3C; Image src = " /images/bird-in-public-folder.jpg " alt = " A bird. " width = " 50 " height = " 50 " /> &#x3C; Image src = " https://example.com/remote-bird.jpg " alt = " A bird. " width = " 50 " height = " 50 " />
 &#x3C; img src = { localBirdImage . src } alt = " A bird sitting on a nest of eggs. " > &#x3C; img src = " /images/bird-in-public-folder.jpg " alt = " A bird. " > &#x3C; img src = " https://example.com/remote-bird.jpg " alt = " A bird. " > `      ">

 See the full API reference for the `&#x3C;Image />` and `&#x3C;Picture />` components including required and optional properties.

 Related recipe:

 Dynamically import images

## Images in Markdown files
 Section titled “Images in Markdown files”
 Options: `![]()`, `&#x3C;img>` (with public or remote images)

Use standard Markdown `![alt](src)` syntax in your `.md` files. Your local images stored in `src/` and remote images will be processed and optimized. When you configure responsive images globally , these images will also be responsive .

Images stored in the `public/` folder are never optimized.

 src/pages/post-1.md ` # My Markdown Page
 &#x3C;!-- Local image stored in src/assets/ --> &#x3C;!-- Use a relative file path or import alias --> ![ A starry night sky. ] ( ../assets/stars.png )
 &#x3C;!-- Image stored in public/images/ --> &#x3C;!-- Use the file path relative to public/ --> ![ A starry night sky. ] ( /images/stars.png )
 &#x3C;!-- Remote image on another server --> &#x3C;!-- Use the full URL of the image --> ![ Astro ] ( https://example.com/images/remote-image.png ) `
 The HTML `&#x3C;img>` tag can also be used to display images stored in `public/` or remote images without any image optimization or processing. However, `&#x3C;img>` is not supported for your local images in `src`.

The `&#x3C;Image />` and `&#x3C;Picture />` components are unavailable in `.md` files. If you require more control over your image attributes, we recommend using Astro’s MDX integration to add support for `.mdx` file format. MDX allows additional image options available in MDX , including combining components with Markdown syntax.

## Images in MDX files
 Section titled “Images in MDX files”
 Options: `&#x3C;Image />`, `&#x3C;Picture />`, `&#x3C;img />`, `![]()`, SVG components

You can use Astro’s `&#x3C;Image />` and `&#x3C;Picture />` components in your `.mdx` files by importing both the component and your image. Use them just as they are used in `.astro` files . The JSX `&#x3C;img />` tag is also supported for unprocessed images and uses the same image import as the HTML `&#x3C;img>` tag .

Additionally, there is support for standard Markdown `![alt](src)` syntax with no import required.

 src/pages/post-1.mdx ` --- title : My Page title --- import { Image } from ' astro:assets ' ; import rocket from ' ../assets/rocket.png ' ;
 # My MDX Page
 // Local image stored in the same folder ![ Houston in the wild ](houston.png)
 // Local image stored in src/assets/ &#x3C; Image src = { rocket } alt = " A rocketship in space. " /> &#x3C; img src = { rocket . src } alt = " A rocketship in space. " /> ![ A rocketship in space ](../assets/rocket.png)
 // Image stored in public/images/ &#x3C; Image src = " /images/stars.png " alt = " A starry night sky. " /> &#x3C; img src = " /images/stars.png " alt = " A starry night sky. " /> ![ A starry night sky. ](/images/stars.png)
 // Remote image on another server &#x3C; Image src = " https://example.com/images/remote-image.png " /> &#x3C; img src = " https://example.com/images/remote-image.png " /> ![ Astro ](https://example.com/images/remote-image.png) `  ![A rocketship in space](../assets/rocket.png)// Image stored in public/images/  ![A starry night sky.](/images/stars.png)// Remote image on another server  ![Astro](https://example.com/images/remote-image.png)">

 See the full API reference for the `&#x3C;Image />` and `&#x3C;Picture />` components.

## Images in UI framework components
 Section titled “Images in UI framework components”
 Image options: the framework’s own image syntax (e.g. `&#x3C;img />` in JSX, `&#x3C;img>` in Svelte)

 Local images must first be imported to access their image properties such as `src`. Then, they can be rendered as you normally would in that framework’s own image syntax:

 src/components/ReactImage.jsx ` import stars from " ../assets/stars.png " ;
 export default function ReactImage () { return ( &#x3C; img src = { stars . src } alt = " A starry night sky. " /> ) } `  )}">
 src/components/SvelteImage.svelte
```
` &#x3C; script > import stars from ' ../assets/stars.png ' ; &#x3C;/ script >
 &#x3C; img src = { stars . src } alt = " A starry night sky. " /> `
```
 ">
 Astro components (e.g. `&#x3C;Image />`, `&#x3C;Picture />`, SVG components) are unavailable inside UI framework components because a client island must contain only valid code for its own framework .

But, you can pass the static content generated by these components to a framework component inside a `.astro` file as children or using a named `&#x3C;slot/>` :

 src/components/ImageWrapper.astro ` --- import ReactComponent from ' ./ReactComponent.jsx ' ; import { Image } from ' astro:assets ' ; import stars from ' ~/stars/docline.png ' ; ---
 &#x3C; ReactComponent > &#x3C; Image src = { stars } alt = " A starry night sky. " /> &#x3C;/ ReactComponent > `   ">

## Astro components for images
 Section titled “Astro components for images”
 Astro provides two built-in Astro components for images (`&#x3C;Image />` and `&#x3C;Picture />`) and also allows you to import SVG files and use them as Astro components. These components may be used in any files that can import and render `.astro` components.

### `&#x3C;Image />`
 Section titled “&#x3C;Image />”
 Use the built-in `&#x3C;Image />` Astro component to display optimized versions of:

 your local images located within the `src/` folder

- configured remote images from authorized sources

`&#x3C;Image />` can transform a local or authorized remote image’s dimensions, file type, and quality for control over your displayed image. This transformation happens at build time for prerendered pages. When your page is rendered on demand, this transformation will occur on the fly when the page is viewed. The resulting `&#x3C;img>` tag includes `alt`, `loading`, and `decoding` attributes and infers image dimensions to avoid Cumulative Layout Shift (CLS).

 src/components/MyComponent.astro ` --- // import the Image component and the image import { Image } from ' astro:assets ' ; import myImage from ' ../assets/my_image.png ' ; // Image is 1600x900 ---
 &#x3C;!-- `alt` is mandatory on the Image component --> &#x3C; Image src = { myImage } alt = " A description of my image. " /> ` ">

```
` &#x3C;!-- Prerendered output --> &#x3C;!-- Image is optimized, proper attributes are enforced --> &#x3C; img src = " /_astro/my_image.hash.webp " width = " 1600 " height = " 900 " decoding = " async " loading = " lazy " alt = " A description of my image. " />
 &#x3C;!-- Output rendered on demand--> &#x3C;!-- src will use an endpoint generated on demand--> &#x3C; img src = " /_image?href=%2F_astro%2Fmy_image.hash.webp &#x26;amp; w=1600 &#x26;amp; h=900 &#x26;amp; f=webp " &#x3C;!-- ... -- > /> `
```
  ">
 The `&#x3C;Image />` component accepts several component properties as well as any attributes accepted by the HTML `&#x3C;img>` tag.

The following example provides a `class` to the image component which will apply to the final `&#x3C;img>` element.

 src/pages/index.astro ` --- import { Image } from ' astro:assets ' ; import myImage from ' ../assets/my_image.png ' ; ---
 &#x3C;!-- `alt` is mandatory on the Image component --> &#x3C; Image src = { myImage } alt = "" class = " my-class " /> ` ">

```
` &#x3C;!-- Prerendered output --> &#x3C; img src = " /_astro/my_image.hash.webp " width = " 1600 " height = " 900 " decoding = " async " loading = " lazy " class = " my-class " alt = "" /> `
```
 ">

### `&#x3C;Picture />`
 Section titled “&#x3C;Picture />”

 Added in:
 `astro@3.3.0`

Use the built-in `&#x3C;Picture />` Astro component to generate a `&#x3C;picture>` tag with multiple formats and/or sizes of your image. This allows you to specify preferred file formats to display and at the same time, provide a fallback format. Like the `&#x3C;Image />` component , images will be processed at build time for prerendered pages. When your page is rendered on demand, processing will occur on the fly when the page is viewed.

The following example uses the `&#x3C;Picture />` component to transform a local `.png` file into a web-friendly `avif` and `webp` format as well as the `.png` `&#x3C;img>` that can be displayed as a fallback when needed:

 src/pages/index.astro ` --- import { Picture } from ' astro:assets ' ; import myImage from ' ../assets/my_image.png ' ; // Image is 1600x900 ---
 &#x3C;!-- `alt` is mandatory on the Picture component --> &#x3C; Picture src = { myImage } formats = { [ ' avif ' , ' webp ' ] } alt = " A description of my image. " /> ` ">

```
` &#x3C;!-- Prerendered output --> &#x3C; picture > &#x3C; source srcset = " /_astro/my_image.hash.avif " type = " image/avif " /> &#x3C; source srcset = " /_astro/my_image.hash.webp " type = " image/webp " /> &#x3C; img src = " /_astro/my_image.hash.png " width = " 1600 " height = " 900 " decoding = " async " loading = " lazy " alt = " A description of my image. " /> &#x3C;/ picture > `
```
     ">

 See details about the `&#x3C;Picture />` component properties in the `astro:assets` reference.

### Responsive image behavior
 Section titled “Responsive image behavior”

 Added in:
 `astro@5.10.0`

Responsive images are images that adjust to improve performance across different devices. These images can resize to fit their container, and can be served in different sizes depending on your visitor’s screen size and resolution.

With the layout property applied to the `&#x3C;Image />` or `&#x3C;Picture />` components, Astro will automatically generate the required `srcset` and `sizes` values for your images, and apply the necessary styles to ensure they resize correctly .

When this responsive behavior is configured globally with `image.layout` , it will apply to all image components and also to any local and remote images using the Markdown `![]()` syntax .

Images in your `public/` folder are never optimized, and responsive images are not supported.

 Read more about responsive images on MDN web docs .

#### Generated HTML output for responsive images
 Section titled “Generated HTML output for responsive images”
 When a layout is set, either by default or on an individual component, images have automatically generated `srcset` and `sizes` attributes based on the image’s dimensions and the layout type. Images with `constrained` and `full-width` layouts will have styles applied to ensure they resize according to their container.

 src/components/MyComponent.astro ` --- import { Image } from ' astro:assets ' ; import myImage from ' ../assets/my_image.png ' ; --- &#x3C; Image src = { myImage } alt = " A description of my image. " layout = ' constrained ' width = { 800 } height = { 600 } /> ` ">
 This `&#x3C;Image />` component will generate the following HTML output on a prerendered page:

 ` &#x3C; img src = " /_astro/my_image.hash3.webp " srcset = " /_astro/my_image.hash1.webp 640w, /_astro/my_image.hash2.webp 750w, /_astro/my_image.hash3.webp 800w, /_astro/my_image.hash4.webp 828w, /_astro/my_image.hash5.webp 1080w, /_astro/my_image.hash6.webp 1280w, /_astro/my_image.hash7.webp 1600w " alt = " A description of my image " sizes = " (min-width: 800px) 800px, 100vw " loading = " lazy " decoding = " async " fetchpriority = " auto " width = " 800 " height = " 600 " style = " --fit: cover; --pos: center; " data-astro-image = " constrained " > ` ">

#### Responsive image styles
 Section titled “Responsive image styles”
 Setting `image.responsiveStyles: true` applies a small number of global styles to ensure that your images resize correctly. In most cases, you will want to enable these as a default; your images will not be responsive without additional styles.

However, if you prefer to handle responsive image styling yourself, or need to override these defaults when using Tailwind 4 , leave the default `false` value configured.

The global styles applied by Astro will depend on the layout type, and are designed to produce the best result for the generated `srcset` and `sizes` attributes. These are the default styles:

 Responsive Image Styles ` :where ([ data-astro-image ]) { object-fit : var ( --fit ); object-position : var ( --pos ); } :where ([ data-astro-image = ' full-width ' ]) { width : 100 % ; } :where ([ data-astro-image = ' constrained ' ]) { max-width : 100 % ; } `
 The styles use the `:where()` pseudo-class , which has a specificity of 0, meaning that it is easy to override with your own styles. Any CSS selector will have a higher specificity than `:where()`, so you can easily override the styles by adding your own styles to target the image.

You can override the `object-fit` and `object-position` styles on a per-image basis by setting the `fit` and `position` props on the `&#x3C;Image />` or `&#x3C;Picture />` component.

#### Responsive images with Tailwind 4
 Section titled “Responsive images with Tailwind 4”
 Tailwind 4 is compatible with Astro’s default responsive styles. However, Tailwind uses cascade layers , meaning that its rules are always lower specificity than rules that don’t use layers, including Astro’s responsive styles. Therefore, Astro’s styling will take precedence over Tailwind styling. To use Tailwind rules instead of Astro’s default styling, do not enable Astro’s default responsive styles .

### SVG components
 Section titled “SVG components”

 Added in:
 `astro@5.7.0`

Astro allows you to import SVG files and use them as Astro components. Astro will inline the SVG content into your HTML output.

Reference the default import of any local `.svg` file. Since this import is treated as an Astro component, you must use the same conventions (e.g. capitalization) as when using dynamic tags .

 src/components/MyAstroComponent.astro ` --- import Logo from ' ./path/to/svg/file.svg ' ; ---
 &#x3C; Logo /> ` ">
 Your SVG component, like `&#x3C;Image />` or any other Astro component, is unavailable inside UI framework components, but can be passed to a framework component inside a `.astro` component.

#### SVG component attributes
 Section titled “SVG component attributes”
 You can pass props such as `width`, `height`, `fill`, `stroke`, and any other attribute accepted by the native `&#x3C;svg>` element . These attributes will automatically be applied to the underlying `&#x3C;svg>` element. If a property is present in the original `.svg` file and is passed to the component, the value passed to the component will override the original value.

 src/components/MyAstroComponent.astro ` --- import Logo from ' ../assets/logo.svg ' ; ---
 &#x3C; Logo width = { 64 } height = { 64 } fill = " currentColor " /> ` ">

#### `SvgComponent` Type
 Section titled “SvgComponent Type”

 Added in:
 `astro@5.14.0`

 You can also enforce type safety for your `.svg` assets using the `SvgComponent` type:

 src/components/Logo.astro ` --- import type { SvgComponent } from " astro/types " ; import HomeIcon from " ./Home.svg " ;
 interface Link { url : string ; text : string ; icon : SvgComponent ; }
 const links : Link [] = [ { url: " / " , text: " Home " , icon: HomeIcon, }, ]; --- `

### Creating custom image components
 Section titled “Creating custom image components”
 You can create a custom, reusable image component by wrapping the `&#x3C;Image />` or `&#x3C;Picture/>` component in another Astro component. This allows you to set default attributes and styles only once.

For example, you could create a component for your blog post images that receives attributes as props and applies consistent styles to each image:

 src/components/BlogPostImage.astro ` --- import { Image } from ' astro:assets ' ;
 const { src , ... attrs } = Astro . props ; --- &#x3C; Image src = { src } { ... attrs } />
 &#x3C; style > img { margin-block : 2.5 rem ; border-radius : 0.75 rem ; } &#x3C;/ style > ` ">

## Display unprocessed images with the HTML `&#x3C;img>` tag
 Section titled “Display unprocessed images with the HTML &#x3C;img> tag”
 The Astro template syntax also supports writing an `&#x3C;img>` tag directly, with full control over its final output. These images will not be processed and optimized. It accepts all HTML `&#x3C;img>` tag properties, and the only required property is `src`. However, it is strongly recommended to include the `alt` property for accessibility .

### images in `src/`
 Section titled “images in src/”
 Local images must be imported from the relative path from the existing `.astro` file, or you can configure and use an import alias . Then, you can access the image’s `src` and other properties to use in the `&#x3C;img>` tag.

Imported image assets match the `ImageMetadata` type and have the following signature:

 ` interface ImageMetadata { src : string ; width : number ; height : number ; format : string ; } `
 The following example uses the image’s own `height` and `width` properties to avoid Cumulative Layout Shift (CLS) and improve Core Web Vitals:

 src/pages/posts/post-1.astro ` --- // import local images import myDog from ' ../../images/pets/local-dog.jpg ' ; --- // access the image properties &#x3C; img src = { myDog . src } width = { myDog . width } height = { myDog . height } alt = " A barking dog. " /> ` ">

### Images in `public/`
 Section titled “Images in public/”
 For images located within `public/` use the image’s file path relative to the public folder as the `src` value:

 ` &#x3C; img src = " /images/public-cat.jpg " alt = " A sleeping cat. " > ` ">

### Remote images
 Section titled “Remote images”
 For remote images, use the image’s full URL as the `src` value:

 ` &#x3C; img src = " https://example.com/remote-cat.jpg " alt = " A sleeping cat. " > ` ">

### Choosing `&#x3C;Image />` vs `&#x3C;img>`
 Section titled “Choosing &#x3C;Image /> vs &#x3C;img>”
 The `&#x3C;Image />` component optimizes your image and infers width and height (for images it can process) based on the original aspect ratio to avoid CLS. It is the preferred way to use images in `.astro` files whenever possible.

Use the HTML `&#x3C;img>` element when you cannot use the `&#x3C;Image />` component, for example:

- for unsupported image formats

- when you do not want your image optimized by Astro

- to access and change the `src` attribute dynamically client-side

## Using Images from a CMS or CDN
 Section titled “Using Images from a CMS or CDN”
 Image CDNs work with all Astro image options . Use an image’s full URL as the `src` attribute in the `&#x3C;Image />` component, an `&#x3C;img>` tag, or in Markdown notation. For image optimization with remote images, also configure your authorized domains or URL patterns .

Alternatively, the CDN may provide its own SDKs to more easily integrate in an Astro project. For example:

- Cloudinary supports an Astro SDK which allows you to easily drop in images with their `CldImage` component or a Node.js SDK that can generate URLs to use with an `&#x3C;img>` tag in a Node.js environment.

- ImageKit provides an Astro integration that registers an image service. This means Astro’s built-in `&#x3C;Image />` and `&#x3C;Picture />` components, along with Markdown `![]()` and MDX images, are all routed through ImageKit automatically. It adds CDN delivery, automatic AVIF/WebP conversion, responsive `srcset`, and on-the-fly transformations without changing your existing image syntax.

 See the full API reference for the `&#x3C;Image />` and `&#x3C;Picture />` components.

## Authorizing remote images
 Section titled “Authorizing remote images”
 You can configure lists of authorized image source URL domains and patterns for image optimization using `image.domains` and `image.remotePatterns` . This configuration is an extra layer of safety to protect your site when showing images from an external source.

Remote images from other sources will not be optimized, but using the `&#x3C;Image />` component for these images will prevent Cumulative Layout Shift (CLS).

For example, the following configuration will only allow remote images from `astro.build` to be optimized:

 astro.config.mjs ` export default defineConfig ({ image: { domains: [ " astro.build " ], } }); `
 The following configuration will only allow remote images from HTTPS hosts:

 astro.config.mjs ` export default defineConfig ({ image: { remotePatterns: [{ protocol: " https " }], } }); `

## Images in content collections
 Section titled “Images in content collections”
 You can declare an associated image for a content collections entry, such as a blog post’s cover image, in your frontmatter using its path relative to the current folder:

 src/content/blog/my-post.md ` --- title : " My first blog post " cover : " ./firstpostcover.jpeg " # will resolve to "src/content/blog/firstpostcover.jpeg" coverAlt : " A photograph of a sunset behind a mountain range. " ---
 This is a blog post `
 The `image` helper for the content collections schema lets you validate and import the image.

 src/content.config.ts ` import { defineCollection } from ' astro:content ' ; import { z } from ' astro/zod ' ;
 const blogCollection = defineCollection ( { schema : ( { image } ) => z . object ( { title: z . string () , cover: image () , coverAlt: z . string () , } ) , } );
 export const collections = { blog: blogCollection , } ; ` z.object({ title: z.string(), cover: image(), coverAlt: z.string(), }),});export const collections = { blog: blogCollection,};">
 The image will be imported and transformed into metadata, allowing you to pass it as a `src` to `&#x3C;Image/>`, `&#x3C;img>`, or `getImage()` in an Astro component.

The example below shows a blog index page that renders the cover photo and title of each blog post from the previous schema:

 src/pages/blog.astro ` --- import { Image } from " astro:assets " ; import { getCollection } from " astro:content " ; const allBlogPosts = await getCollection ( " blog " ); ---
 { allBlogPosts . map ( ( post ) => ( &#x3C; div > &#x3C; Image src = { post . data . cover } alt = { post . data . coverAlt } /> &#x3C; h2 > &#x3C; a href = { " /blog/ " + post . id } > { post . data . title } &#x3C;/ a > &#x3C;/ h2 > &#x3C;/ div > )) } ` (  
##  {post.data.title} 
  ))}">

## Generating images with `getImage()`
 Section titled “Generating images with getImage()”
 The `getImage()` function is intended for generating images destined to be used somewhere else than directly in HTML, for example in an API Route . When you need options that the `&#x3C;Picture>` and `&#x3C;Image>` components do not currently support, you can use the `getImage()` function to create your own custom `&#x3C;Image />` component.

`getImage()` can only be used on the server. If you need to use the resulting image URL on the client (e.g. in a client-side script or framework component), call `getImage()` inside the frontmatter and pass the resulting `src` to the client:

 src/components/ClientImage.astro ` --- import { getImage } from " astro:assets " ; import myBackground from " ../background.png " ;
 const optimizedBackground = await getImage ( { src: myBackground , format: " avif " } ); ---
 &#x3C; div id = " background " data-src = { optimizedBackground . src } >&#x3C;/ div >
 &#x3C; script > const src = document . getElementById ( " background " ) . dataset . src ; // use src client-side as needed &#x3C;/ script > ` ">

 See more in the `getImage()` reference .

 Related recipe:

 Build a custom image component

## Alt Text
 Section titled “Alt Text”
 Not all users can see images in the same way, so accessibility is an especially important concern when using images. Use the `alt` attribute to provide descriptive alt text for images.

This attribute is required for both the `&#x3C;Image />` and `&#x3C;Picture />` components. If no alt text is provided, a helpful error message will be provided reminding you to include the `alt` attribute.

If the image is merely decorative (i.e. doesn’t contribute to the understanding of the page), set `alt=""` so that screen readers know to ignore the image.

## Default image service
 Section titled “Default image service”
 Sharp is the default image service used for `astro:assets`. You can further configure the image service using the `image.service` option.

### Configure no-op passthrough service
 Section titled “Configure no-op passthrough service”
 If your adapter does not support Astro’s built-in Sharp image optimization (e.g. Cloudflare), you can configure a no-op image service to allow you to use the `&#x3C;Image />` and `&#x3C;Picture />` components. Note that Astro does not perform any image transformation and processing in these environments. However, you can still enjoy the other benefits of using `astro:assets`, including no Cumulative Layout Shift (CLS), the enforced `alt` attribute, and a consistent authoring experience.

Configure the `passthroughImageService()` to avoid Sharp image processing:

 astro.config.mjs ` import { defineConfig, passthroughImageService } from ' astro/config ' ;
 export default defineConfig ({ image: { service: passthroughImageService () } }); `

## Asset Caching
 Section titled “Asset Caching”
 Astro stores processed image assets in a cache directory during site builds for both local and remote images from authorized sources . By preserving the cache directory between builds, processed assets are reused, improving build time and bandwidth usage.

The default cache directory is `./node_modules/.astro`, however this can be changed using the `cacheDir` configuration setting.

### Remote Images
 Section titled “Remote Images”
 Remote images in the asset cache are managed based on HTTP Caching , and respect the Cache-Control header returned by the remote server.
Images are cached if the Cache-Control header allows, and will be used until they are no longer fresh .

#### Revalidation
 Section titled “Revalidation”

 Added in:
 `astro@5.1.0`

 Revalidation reduces bandwidth usage and build time by checking with the remote server whether an expired cached image is still up-to-date. If the server indicates that the image is still fresh, the cached version is reused, otherwise the image is redownloaded.

Revalidation requires that the remote server send Last-Modified and/or Etag (entity tag) headers with its responses. This feature is available for remote servers that support the If-Modified-Since and If-None-Match headers.

## Community Integrations
 Section titled “Community Integrations”
 There are several third-party community image integrations for optimizing and working with images in your Astro project.

 Learn

 Contribute

 Community

 Sponsor

## Data Fetching

# Data fetching

 `.astro` files can fetch remote data to help you generate your pages.

## `fetch()` in Astro
 Section titled “fetch() in Astro”
 All Astro components have access to the global `fetch()` function in their component script to make HTTP requests to APIs using the full URL (e.g. `https://example.com/api`).
Additionally, you can construct a URL to your project’s pages and endpoints that are rendered on demand on the server using `new URL("/api", Astro.url)` .

This fetch call will be executed at build time, and the data will be available to the component template for generating dynamic HTML. If SSR mode is enabled, any fetch calls will be executed at runtime.

💡 Take advantage of top-level `await` inside of your Astro component script.

💡 Pass fetched data to both Astro and framework components, as props.

 - src/components/User.astro ` --- import Contact from " ../components/Contact.jsx " ; import Location from " ../components/Location.astro " ;
 const response = await fetch ( " https://randomuser.me/api/ " ); const data = await response . json (); const randomUser = data . results [ 0 ]; --- &#x3C;!-- Data fetched at build can be rendered in HTML --> &#x3C; h1 > User &#x3C;/ h1 > &#x3C; h2 > { randomUser . name . first } { randomUser . name . last } &#x3C;/ h2 >
 &#x3C;!-- Data fetched at build can be passed to components as props --> &#x3C; Contact client:load email = { randomUser . email } /> &#x3C; Location city = { randomUser . location . city } /> `  ">

## `fetch()` in Framework Components
 Section titled “fetch() in Framework Components”
 The `fetch()` function is also globally available to any framework components :

 src/components/Movies.tsx ` import type { FunctionalComponent } from ' preact ' ;
 const data = await fetch ( ' https://example.com/movies.json ' ) . then ( ( response ) => response . json ());
 // Components that are build-time rendered also log to the CLI. // When rendered with a `client:*` directive, they also log to the browser console. console . log (data);
 const Movies : FunctionalComponent = () => { // Output the result to the page return &#x3C; div > { JSON . stringify (data) } &#x3C;/ div > ; } ;
 export default Movies; ` response.json());// Components that are build-time rendered also log to the CLI.// When rendered with a &#x60;client:*&#x60; directive, they also log to the browser console.console.log(data);const Movies: FunctionalComponent = () => { // Output the result to the page return {JSON.stringify(data)} ;};export default Movies;">

## GraphQL queries
 Section titled “GraphQL queries”
 Astro can also use `fetch()` to query a GraphQL server with any valid GraphQL query.

 src/components/Film.astro ` --- const response = await fetch ( " https://swapi-graphql.netlify.app/.netlify/functions/index " , { method: " POST " , headers: { " Content-Type " : " application/json " }, body: JSON . stringify ( { query: ` query getFilm ($id:ID!) { film(id: $id) { title releaseDate } } ` , variables: { id: " ZmlsbXM6MQ== " , }, } ) , } );

 const json = await response . json (); const { film } = json . data ; --- &#x3C; h1 > Fetching information about Star Wars: A New Hope &#x3C;/ h1 > &#x3C; h2 > Title: { film . title } &#x3C;/ h2 > &#x3C; p > Year: { film . releaseDate } &#x3C;/ p > ` Year: {film.releaseDate}
">

## Fetch from a Headless CMS
 Section titled “Fetch from a Headless CMS”
 Astro components can fetch data from your favorite CMS and then render it as your page content. Using dynamic routes , components can even generate pages based on your CMS content.

See our CMS Guides for full details on integrating Astro with headless CMSes including Storyblok, Contentful, and WordPress.

## Community resources
 Section titled “Community resources”

 Creating a fullstack app with Astro + GraphQL

 Learn

 Contribute

 Community

 Sponsor

## Astro Db

# Astro DB

Astro DB is a fully-managed SQL database designed for the Astro ecosystem. Develop locally in Astro and deploy to any libSQL-compatible database.

Astro DB is a complete solution to configuring, developing, and querying your data. A local database is created in `.astro/content.db` whenever you run `astro dev` to manage your data without the need for Docker or a network connection.

## Installation
 Section titled “Installation”
 Install the `@astrojs/db` integration using the built-in `astro add` command:

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

## Define your database
 Section titled “Define your database”
 Installing `@astrojs/db` with the `astro add` command will automatically create a `db/config.ts` file in your project where you will define your database tables:

 db/config.ts ` import { defineDb } from ' astro:db ' ;
 export default defineDb ({ tables: { }, }) `

### Tables
 Section titled “Tables”
 Data in Astro DB is stored using SQL tables. Tables structure your data into rows and columns, where columns enforce the type of each row value.

Define your tables in your `db/config.ts` file by providing the structure of the data in your existing libSQL database, or the data you will collect in a new database. This will allow Astro to generate a TypeScript interface to query that table from your project. The result is full TypeScript support when you access your data with property autocompletion and type-checking.

To configure a database table, import and use the `defineTable()` and `column` utilities from `astro:db`. Then, define a name (case-sensitive) for your table and the type of data in each column.

This example configures a `Comment` table with required text columns for `author` and `body`. Then, makes it available to your project through the `defineDb()` export.

 db/config.ts ` import { defineDb, defineTable, column } from ' astro:db ' ;
 const Comment = defineTable ( { columns: { author: column . text () , body: column . text () , } } )
 export default defineDb ({ tables: { Comment }, }) `

 See the table configuration reference for a complete reference of table options.

### Columns
 Section titled “Columns”
 Astro DB supports the following column types:

 db/config.ts ` import { defineTable, column } from ' astro:db ' ;
 const Comment = defineTable ( { columns: { // A string of text. author: column . text () , // A whole integer value. likes: column . number () , // A true or false value. flagged: column . boolean () , // Date/time values queried as JavaScript Date objects. published: column . date () , // An untyped JSON object. metadata: column . json () , } } ); `

 See the table columns reference for more details.

### Table References
 Section titled “Table References”
 Relationships between tables are a common pattern in database design. For example, a `Blog` table may be closely related to other tables of `Comment`, `Author`, and `Category`.

You can define these relations between tables and save them into your database schema using reference columns . To establish a relationship, you will need:

 An identifier column on the referenced table. This is usually an `id` column with the `primaryKey` property.

- A column on the base table to store the referenced `id` . This uses the `references` property to establish a relationship.

This example shows a `Comment` table’s `authorId` column referencing an `Author` table’s `id` column.

 db/config.ts ` const Author = defineTable ( { columns: { id: column . number ( { primaryKey: true } ) , name: column . text () , } } );
 const Comment = defineTable ( { columns: { authorId: column . number ( { references : () => Author . columns . id } ) , body: column . text () , } } ); ` Author.columns.id }), body: column.text(), }});">

## Seed your database for development
 Section titled “Seed your database for development”
 In development, Astro will use your DB config to generate local types according to your schemas. These will be generated fresh from your seed file each time the dev server is started, and will allow you to query and work with the shape of your data with type safety and autocompletion.

You will not have access to production data during development unless you connect to a remote database during development. This protects your data while allowing you to test and develop with a working database with type-safety.

To seed development data for testing and debugging into your Astro project, create a `db/seed.ts` file. Import both the `db` object and your tables defined in `astro:db`. `insert` some initial data into each table. This development data should match the form of both your database schema and production data.

The following example defines two rows of development data for a `Comment` table, and an `Author` table:

 db/seed.ts ` import { db, Comment, Author } from ' astro:db ' ;
 export default async function () { await db . insert (Author) . values ([ { id: 1 , name: " Kasim " } , { id: 2 , name: " Mina " } , ]);
 await db . insert (Comment) . values ([ { authorId: 1 , body: ' Hope you like Astro DB! ' } , { authorId: 2 , body: ' Enjoy! ' } , ]) } `
 Your development server will automatically restart your database whenever this file changes, regenerating your types and seeding this development data from `seed.ts` fresh each time.

## Connect a libSQL database for production
 Section titled “Connect a libSQL database for production”
 Astro DB can connect to any local libSQL database or to any server that exposes the libSQL remote protocol, whether managed or self-hosted.

To connect Astro DB to a libSQL database, set the following environment variables obtained from your database provider:

- `ASTRO_DB_REMOTE_URL`: the connection URL to the location of your local or remote libSQL DB. This may include URL configuration options such as sync and encryption as parameters.

- `ASTRO_DB_APP_TOKEN`: the auth token to your libSQL server. This is required for remote databases, and not needed for local DBs like files or in-memory databases

Depending on your service, you may have access to a CLI or web UI to retrieve these values. The following section will demonstrate connecting to Turso and setting these values as an example, but you are free to use any provider.

### Getting started with Turso
 Section titled “Getting started with Turso”
 Turso is the company behind libSQL , the open-source fork of SQLite that powers Astro DB. They provide a fully managed libSQL database platform and are fully compatible with Astro.

The steps below will guide you through the process of installing the Turso CLI, logging in (or signing up), creating a new database, getting the required environmental variables, and pushing the schema to the remote database.

-
Install the Turso CLI .

-
 Log in or sign up to Turso.

-
Create a new database. In this example the database name is `andromeda`.

 Terminal window ` turso db create andromeda `

-
 Run the `show` command to see information about the newly created database:

 Terminal window ` turso db show andromeda `
 Copy the `URL` value and set it as the value for `ASTRO_DB_REMOTE_URL`.

 .env ` ASTRO_DB_REMOTE_URL = libsql://andromeda-houston.turso.io `

-
 Create a new token to authenticate requests to the database:

 Terminal window ` turso db tokens create andromeda `
 Copy the output of the command and set it as the value for `ASTRO_DB_APP_TOKEN`.

 .env ` ASTRO_DB_REMOTE_URL = libsql://andromeda-houston.turso.io ASTRO_DB_APP_TOKEN = eyJhbGciOiJF...3ahJpTkKDw `

-
 Push your DB schema and metadata to the new Turso database.

 Terminal window ` astro db push --remote `

-
 Congratulations, now you have a database connected! Give yourself a break. 👾

 Terminal window ` turso relax `

 To explore more features of Turso, check out the Turso docs .

### Connecting to remote databases
 Section titled “Connecting to remote databases”
 Astro DB allows you to connect to both local and remote databases. By default, Astro uses a local database file for `dev` and `build` commands, recreating tables and inserting development seed data each time.

To connect to a hosted remote database, use the `--remote` flag. This flag enables both readable and writable access to your remote database, allowing you to accept and persist user data in production environments.

Configure your build command to use the `--remote` flag:

 package.json ` { "scripts" : { "build" : " astro build --remote " } } `
 You can also use the flag directly in the command line:

 Terminal window ` # Build with a remote connection astro build --remote
 # Develop with a remote connection astro dev --remote `

 The `--remote` flag uses the connection to the remote DB both locally during the build and on the server. Ensure you set the necessary environment variables in both your local development environment and your deployment platform. Additionally, you may need to configure web mode for non-Node.js runtimes such as Cloudflare Workers or Deno.

When deploying your Astro DB project, make sure your deployment platform’s build command is set to `npm run build` (or the equivalent for your package manager) to utilize the `--remote` flag configured in your `package.json`.

### Remote URL configuration options
 Section titled “Remote URL configuration options”
 The `ASTRO_DB_REMOTE_URL` environment variable configures the location of your database as well as other options like sync and encryption.

#### URL scheme and host
 Section titled “URL scheme and host”
 libSQL supports both HTTP and WebSockets as the transport protocol for a remote server. It also supports using a local file or an in-memory DB. Those can be configured using the following URL schemes in the connection URL:

- `memory:` will use an in-memory DB. The host must be empty in this case.

- `file:` will use a local file. The host is the path to the file (`file:path/to/file.db`).

- `libsql:` will use a remote server through the protocol preferred by the library (this might be different across versions). The host is the address of the server (`libsql://your.server.io`).

- `http:` will use a remote server through HTTP. `https:` can be used to enable a secure connection. The host is the same as for `libsql:`.

- `ws:` will use a remote server through WebSockets. `wss:` can be used to enable a secure connection. The host is the same as for `libsql:`.

Details of the libSQL connection (e.g. encryption key, replication, sync interval) can be configured as query parameters in the remote connection URL.

For example, to have an encrypted local file work as an embedded replica to a libSQL server, you can set the following environment variables:

 .env ` ASTRO_DB_REMOTE_URL = file://local-copy.db?encryptionKey=your-encryption-key&#x26;syncInterval=60&#x26;syncUrl=libsql%3A%2F%2Fyour.server.io ASTRO_DB_APP_TOKEN = token-to-your-remote-url `

#### `encryptionKey`
 Section titled “encryptionKey”
 libSQL has native support for encrypted databases. Passing this search parameter will enable encryption using the given key:

 .env ` ASTRO_DB_REMOTE_URL = file:path/to/file.db?encryptionKey=your-encryption-key `

#### `syncUrl`
 Section titled “syncUrl”
 Embedded replicas are a feature of libSQL clients that creates a full synchronized copy of your database on a local file or in memory for ultra-fast reads. Writes are sent to a remote database defined on the `syncUrl` and synchronized with the local copy.

Use this property to pass a separate connection URL to turn the database into an embedded replica of another database. This should only be used with the schemes `file:` and `memory:`. The parameter must be URL encoded.

For example, to have an in-memory embedded replica of a database on `libsql://your.server.io`, you can set the connection URL as such:

 .env ` ASTRO_DB_REMOTE_URL = memory:?syncUrl=libsql%3A%2F%2Fyour.server.io `

#### `syncInterval`
 Section titled “syncInterval”
 Interval between embedded replica synchronizations in seconds. By default it only synchronizes on startup and after writes.

This property is only used when `syncUrl` is also set. For example, to set an in-memory embedded replica to synchronize every minute set the following environment variable:

 .env ` ASTRO_DB_REMOTE_URL = memory:?syncUrl=libsql%3A%2F%2Fyour.server.io&#x26;syncInterval=60 `

## Query your database
 Section titled “Query your database”
 You can query your database from any Astro page , endpoint , or action in your project using the provided `db` ORM and query builder.

### Drizzle ORM
 Section titled “Drizzle ORM”

```
` import { db } from ' astro:db ' ; `
```

 Astro DB includes a built-in Drizzle ORM client. There is no setup or manual configuration required to use the client. The Astro DB `db` client is automatically configured to communicate with your database (local or remote) when you run Astro. It uses your exact database schema definition for type-safe SQL queries with TypeScript errors when you reference a column or table that doesn’t exist.

### Select
 Section titled “Select”
 The following example selects all rows of a `Comment` table. This returns the complete array of seeded development data from `db/seed.ts` which is then available for use in your page template:

 src/pages/index.astro ` --- import { db, Comment } from ' astro:db ' ;
 const comments = await db . select () . from (Comment); ---
 &#x3C; h2 > Comments &#x3C;/ h2 >
 { comments . map ( ( { author , body } ) => ( &#x3C; article > &#x3C; p > Author: { author } &#x3C;/ p > &#x3C; p > { body } &#x3C;/ p > &#x3C;/ article > )) } ` (  Author: {author}
 {body}
  ))}">

 See the Drizzle `select()` API reference for a complete overview.

### Insert
 Section titled “Insert”
 To accept user input, such as handling form requests and inserting data into your remote hosted database, configure your Astro project for on-demand rendering and add an adapter for your deployment environment.

This example inserts a row into a `Comment` table based on a parsed form POST request:

 src/pages/index.astro ` --- import { db, Comment } from ' astro:db ' ;
 if (Astro . request . method === ' POST ' ) { // Parse form data const formData = await Astro . request . formData (); const author = formData . get ( ' author ' ); const body = formData . get ( ' body ' ); if ( typeof author === ' string ' &#x26;&#x26; typeof body === ' string ' ) { // Insert form data into the Comment table await db . insert (Comment) . values ({ author, body }); } }
 // Render the new list of comments on each request const comments = await db . select () . from (Comment); ---
 &#x3C; form method = " POST " style = " display: grid " > &#x3C; label for = " author " > Author &#x3C;/ label > &#x3C; input id = " author " name = " author " />
 &#x3C; label for = " body " > Body &#x3C;/ label > &#x3C; textarea id = " body " name = " body " >&#x3C;/ textarea >
 &#x3C; button type = " submit " > Submit &#x3C;/ button > &#x3C;/ form >
 &#x3C;!-- Render `comments` --> `  Author   Body   Submit  ">
 You can also use Astro actions to insert data into an Astro DB table. The following example inserts a row into a `Comment` table using an action:

 src/actions/index.ts ` import { db, Comment } from ' astro:db ' ; import { defineAction } from ' astro:actions ' ; import { z } from ' astro/zod ' ;
 export const server = { addComment: defineAction ( { // Actions include type safety with Zod, removing the need // to check if typeof {value} === 'string' in your pages input: z . object ( { author: z . string () , body: z . string () , } ) , handler : async ( input ) => { const updatedComments = await db . insert (Comment) . values (input) . returning () ; // Return the updated comments return updatedComments ; }, } ) , } ; ` { const updatedComments = await db .insert(Comment) .values(input) .returning(); // Return the updated comments return updatedComments; }, }),};">

 See the Drizzle `insert()` API reference for a complete overview.

### Delete
 Section titled “Delete”
 You can also query your database from an API endpoint. This example deletes a row from a `Comment` table by the `id` parameter:

 src/pages/api/comments/[id].ts ` import type { APIRoute } from " astro " ; import { db, Comment, eq } from ' astro:db ' ;
 export const DELETE : APIRoute = async ( ctx ) => { await db . delete (Comment) . where ( eq (Comment . id , ctx . params . id )) ; return new Response ( null , { status: 204 } ) ; } ` { await db.delete(Comment).where(eq(Comment.id, ctx.params.id )); return new Response(null, { status: 204 });}">

 See the Drizzle `delete()` API reference for a complete overview.

### Filtering
 Section titled “Filtering”
 To query for table results by a specific property, use Drizzle options for partial selects . For example, add a `.where()` call to your `select()` query and pass the comparison you want to make.

The following example queries for all rows in a `Comment` table that contain the phrase “Astro DB.” Use the `like()` operator to check if a phrase is present within the `body`:

 src/pages/index.astro ` --- import { db, Comment, like } from ' astro:db ' ;
 const comments = await db . select () . from (Comment) . where ( like (Comment . body , ' %Astro DB% ' ) ); --- `

### Drizzle utilities
 Section titled “Drizzle utilities”
 All Drizzle utilities for building queries are exposed from the `astro:db` module. This includes:

- Filter operators like `eq()` and `gt()`

- Aggregation helpers like `count()`

- The `sql` helper for writing raw SQL queries

 ` import { eq, gt, count, sql } from ' astro:db ' ; `

### Relationships
 Section titled “Relationships”
 You can query related data from multiple tables using a SQL join. To create a join query, extend your `db.select()` statement with a join operator. Each function accepts a table to join with and a condition to match rows between the two tables.

This example uses an `innerJoin()` function to join `Comment` authors with their related `Author` information based on the `authorId` column. This returns an array of objects with each `Author` and `Comment` row as top-level properties:

 src/pages/index.astro ` --- import { db, eq, Comment, Author } from ' astro:db ' ;
 const comments = await db . select () . from (Comment) . innerJoin (Author, eq (Comment . authorId , Author . id )); ---
 &#x3C; h2 > Comments &#x3C;/ h2 >
 { comments . map ( ( { Author , Comment } ) => ( &#x3C; article > &#x3C; p > Author: { Author . name } &#x3C;/ p > &#x3C; p > { Comment . body } &#x3C;/ p > &#x3C;/ article > )) } ` (  Author: {Author.name}
 {Comment.body}
  ))}">

 See the Drizzle join reference for all available join operators and config options.

### Batch Transactions
 Section titled “Batch Transactions”
 All remote database queries are made as a network request. You may need to “batch” queries together into a single transaction when making a large number of queries, or to have automatic rollbacks if any query fails.

This example seeds multiple rows in a single request using the `db.batch()` method:

 db/seed.ts ` import { db, Author, Comment } from ' astro:db ' ;
 export default async function () { const queries = []; // Seed 100 sample comments into your remote database // with a single network request. for ( let i = 0 ; i &#x3C; 100 ; i ++ ) { queries . push (db . insert (Comment) . values ({ body: ` Test comment ${ i } ` })); } await db . batch (queries); } `

 See the Drizzle `db.batch()` docs for more details.

## Pushing changes to your database
 Section titled “Pushing changes to your database”
 You can push changes made during development to your database.

### Pushing table schemas
 Section titled “Pushing table schemas”
 Your table schema may change over time as your project grows. You can safely test configuration changes locally and push to your remote database when you deploy.

You can push your local schema changes to your remote database via the CLI using the `astro db push --remote` command:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm run astro db push --remote `

 Terminal window
```
` pnpm astro db push --remote `
```

 Terminal window
```
` yarn astro db push --remote `
```

 This command will verify that your local changes can be made without data loss and, if necessary, suggest how to safely make changes to your schema in order to resolve conflicts.

#### Pushing breaking schema changes
 Section titled “Pushing breaking schema changes”

 If you must change your table schema in a way that is incompatible with your existing data hosted on your remote database, you will need to reset your production database.

To push a table schema update that includes a breaking change, add the `--force-reset` flag to reset all production data:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm run astro db push --remote --force-reset `

 Terminal window
```
` pnpm astro db push --remote --force-reset `
```

 Terminal window
```
` yarn astro db push --remote --force-reset `
```

### Renaming tables
 Section titled “Renaming tables”
 It is possible to rename a table after pushing your schema to your remote database.

If you do not have any important production data , then you can reset your database using the `--force-reset` flag. This flag will drop all of the tables in the database and create new ones so that it matches your current schema exactly.

To rename a table while preserving your production data, you must perform a series of non-breaking changes to push your local schema to your remote database safely.

The following example renames a table from `Comment` to `Feedback`:

-
In your database config file, add the `deprecated: true` property to the table you want to rename:

 db/config.ts ` const Comment = defineTable ( { deprecated: true , columns: { author: column . text () , body: column . text () , } } ); `

-
 Add a new table schema (matching the existing table’s properties exactly) with the new name:

 db/config.ts ` const Comment = defineTable ( { deprecated: true , columns: { author: column . text () , body: column . text () , } } ); const Feedback = defineTable ( { columns: { author: column . text () , body: column . text () , } } ); `

-
 Push to your remote database with `astro db push --remote`. This will add the new table and mark the old as deprecated.

-
Update any of your local project code to use the new table instead of the old table. You might need to migrate data to the new table as well.

-
Once you are confident that the old table is no longer used in your project, you can remove the schema from your `config.ts`:

 db/config.ts ` const Comment = defineTable ( { deprecated: true , columns: { author: column . text () , body: column . text () , } } );
 const Feedback = defineTable ( { columns: { author: column . text () , body: column . text () , } } ); `

-
 Push to your remote database again with `astro db push --remote`. The old table will be dropped, leaving only the new, renamed table.

### Pushing table data
 Section titled “Pushing table data”
 You may need to push data to your remote database for seeding or data migrations. You can author a `.ts` file with the `astro:db` module to write type-safe queries. Then, execute the file against your remote database using the command `astro db execute &#x3C;file-path> --remote`:

The following Comments can be seeded using the command `astro db execute db/seed.ts --remote`:

 db/seed.ts ` import { Comment } from ' astro:db ' ;
 export default async function () { await db . insert (Comment) . values ([ { authorId: 1 , body: ' Hope you like Astro DB! ' } , { authorId: 2 , body: ' Enjoy! ' } , ]) } `

 See the CLI reference for a complete list of commands.

## Building Astro DB integrations
 Section titled “Building Astro DB integrations”
 Astro integrations can extend user projects with additional Astro DB tables and seed data.

Use the `extendDb()` method in the `astro:db:setup` hook to register additional Astro DB config and seed files.
The `defineDbIntegration()` helper provides TypeScript support and auto-complete for the `astro:db:setup` hook.

 my-integration/index.ts ` import { defineDbIntegration } from ' @astrojs/db/utils ' ;
 export default function MyIntegration () { return defineDbIntegration ({ name: ' my-astro-db-powered-integration ' , hooks: { ' astro:db:setup ' : ( { extendDb } ) => { extendDb ({ configEntrypoint: ' @astronaut/my-package/config ' , seedEntrypoint: ' @astronaut/my-package/seed ' , }); } , // Other integration hooks... } , }); } ` { extendDb({ configEntrypoint: &#x27;@astronaut/my-package/config&#x27;, seedEntrypoint: &#x27;@astronaut/my-package/seed&#x27;, }); }, // Other integration hooks... }, });}">
 Integration config and seed files follow the same format as their user-defined equivalents.

### Type safe operations in integrations
 Section titled “Type safe operations in integrations”
 While working on integrations, you may not be able to benefit from Astro’s generated table types exported from `astro:db`.
For full type safety, use the `asDrizzleTable()` utility to create a table reference object you can use for database operations.

For example, given an integration setting up the following `Pets` database table:

 my-integration/config.ts ` import { defineDb, defineTable, column } from ' astro:db ' ;
 export const Pets = defineTable ( { columns: { name: column . text () , species: column . text () , }, } );
 export default defineDb ({ tables: { Pets } }); `
 The seed file can import `Pets` and use `asDrizzleTable()` to insert rows into your table with type checking:

 my-integration/seed.ts ` import { asDrizzleTable } from ' @astrojs/db/utils ' ; import { db } from ' astro:db ' ; import { Pets } from ' ./config ' ;
 export default async function () { const typeSafePets = asDrizzleTable ( ' Pets ' , Pets );
 await db . insert ( typeSafePets ) . values ([ { name: ' Palomita ' , species: ' cat ' } , { name: ' Pan ' , species: ' dog ' } , ]); } `
 The value returned by `asDrizzleTable('Pets', Pets)` is equivalent to `import { Pets } from 'astro:db'`, but is available even when Astro’s type generation can’t run.
You can use it in any integration code that needs to query or insert into the database.

## Migrate from Astro Studio to Turso
 Section titled “Migrate from Astro Studio to Turso”

- In the Studio dashboard , navigate to the project you wish to migrate. In the settings tab, use the “Export Database” button to download a dump of your database.

- Follow the official instructions to install the Turso CLI and sign up or log in to your Turso account.

- Create a new database on Turso using the `turso db create` command.
 Terminal window
```
` turso db create [database-name] `
```

- Fetch the database URL using the Turso CLI, and use it as the environment variable `ASTRO_DB_REMOTE_URL`.
 Terminal window
```
` turso db show [database-name] `
```

```
` ASTRO_DB_REMOTE_URL = [your-database-url] `
```

- Create a token to access your database, and use it as the environment variable `ASTRO_DB_APP_TOKEN`.
 Terminal window
```
` turso db tokens create [database-name] `
```

```
` ASTRO_DB_APP_TOKEN = [your-app-token] `
```

- Push your DB schema and metadata to the new Turso database.
 Terminal window
```
` astro db push --remote `
```

- Import the database dump from step 1 into your new Turso DB.
 Terminal window
```
` turso db shell [database-name] &#x3C; ./path/to/dump.sql `
```

- Once you have confirmed your project connects to the new database, you can safely delete the project from Astro Studio.

 Learn

 Contribute

 Community

 Sponsor