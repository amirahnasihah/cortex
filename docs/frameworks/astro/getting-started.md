# Astro - Getting Started


## Install And Setup

# Install Astro

 The `create astro` CLI command is the fastest way to start a new Astro project from scratch. It will walk you through every step of setting up your new Astro project and allow you to choose from a few different official starter templates.

You can also run the CLI command with the `template` flag to begin your project using any existing theme or starter template. Explore our themes and starters showcase where you can browse themes for blogs, portfolios, documentation sites, landing pages, and more!

To install Astro manually instead, see our step-by-step manual installation guide .

## Prerequisites
 Section titled “Prerequisites”

- Node.js - `v22.12.0` or higher. Odd-numbered versions like `v23` are not supported.

- Text editor - We recommend VS Code with our Official Astro extension .

- Terminal - Astro is accessed through its command-line interface (CLI).

## Browser compatibility
 Section titled “Browser compatibility”
 Astro is built with Vite which targets browsers with modern JavaScript support by default. For a complete reference, you can see the list of currently supported browser versions in Vite .

## Install from the CLI wizard
 Section titled “Install from the CLI wizard”
 You can run `create astro` anywhere on your machine, so there’s no need to create a new empty directory for your project before you begin. If you don’t have an empty directory yet for your new project, the wizard will help create one for you automatically.

-
Run the following command in your terminal to start the install wizard:

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` # create a new project with npm npm create astro@latest `

 Terminal window
```
` # create a new project with pnpm pnpm create astro@latest `
```

 Terminal window
```
` # create a new project with yarn yarn create astro `
```

 If all goes well, you will see a success message followed by some recommended next steps.

-
Now that your project has been created, you can `cd` into your new project directory to begin using Astro.

-
If you skipped the “Install dependencies?” step during the CLI wizard, then be sure to install your dependencies before continuing.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install `

 Terminal window
```
` pnpm install `
```

 Terminal window
```
` yarn install `
```

-
 You can now start the Astro dev server and see a live preview of your project while you build!

## CLI installation flags
 Section titled “CLI installation flags”
 You can run the `create astro` command with additional flags to customize the setup process (e.g. answering “yes” to all questions, skipping the Houston animation) or your new project (e.g. install git or not, add integrations).

 See all the available `create astro` command flags .

### Add integrations
 Section titled “Add integrations”
 You can start a new Astro project and install any official integrations or community integrations that support the `astro add` command at the same time by passing the `--add` argument to the `create astro` command.

Run the following command in your terminal, substituting any integration that supports the `astro add` command:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` # create a new project with React and Partytown npm create astro@latest -- --add react --add partytown `

 Terminal window
```
` # create a new project with React and Partytown pnpm create astro@latest --add react --add partytown `
```

 Terminal window
```
` # create a new project with React and Partytown yarn create astro --add react --add partytown `
```

### Use a theme or starter template
 Section titled “Use a theme or starter template”
 You can start a new Astro project based on an official example or the `main` branch of any GitHub repository by passing a `--template` argument to the `create astro` command.

Run the following command in your terminal, substituting the official Astro starter template name, or the GitHub username and repository of the theme you want to use:

 -

 npm

-

 pnpm

-

 Yarn

 Terminal window ` # create a new project with an official example npm create astro@latest -- --template &#x3C;example-name>
 # create a new project based on a GitHub repository’s main branch npm create astro@latest -- --template &#x3C;github-username>/&#x3C;github-repo> ` npm create astro@latest -- --template / ">

 Terminal window
```
` # create a new project with an official example pnpm create astro@latest --template &#x3C;example-name>
 # create a new project based on a GitHub repository’s main branch pnpm create astro@latest --template &#x3C;github-username>/&#x3C;github-repo> `
```
 pnpm create astro@latest --template / ">

 Terminal window
```
` # create a new project with an official example yarn create astro --template &#x3C;example-name>
 # create a new project based on a GitHub repository’s main branch yarn create astro --template &#x3C;github-username>/&#x3C;github-repo> `
```
 yarn create astro --template / ">

 By default, this command will use the template repository’s `main` branch. To use a different branch name, pass it as part of the `--template` argument: `&#x3C;github-username>/&#x3C;github-repo>#&#x3C;branch>`.

## Manual Setup
 Section titled “Manual Setup”
 This guide will walk you through the steps to manually install and configure a new Astro project.

If you prefer not to use our automatic `create astro` CLI tool, you can set up your project yourself by following the guide below.

-
Create your directory

Create an empty directory with the name of your project, and then navigate into it.

 Terminal window ` mkdir my-astro-project cd my-astro-project `
 Once you are in your new directory, create your project `package.json` file. This is how you will manage your project dependencies, including Astro. If you aren’t familiar with this file format, run the following command to create one.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm init --yes `

 Terminal window
```
` pnpm init `
```

 Terminal window
```
` yarn init --yes `
```

-
 Install Astro

First, install the Astro project dependencies inside your project.

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm install astro `

 Terminal window
```
` pnpm add astro `
```

 Terminal window
```
` yarn add astro `
```

 Then, replace any placeholder “scripts” section of your `package.json` with the following:

 package.json ` { "scripts" : { "test" : " echo \" Error: no test specified \" &#x26;&#x26; exit 1 " , "dev" : " astro dev " , "build" : " astro build " , "preview" : " astro preview " }, } `
 You’ll use these scripts later in the guide to start Astro and run its different commands.

-
Create your first page

In your text editor, create a new file in your directory at `src/pages/index.astro`. This will be your first Astro page in the project.

For this guide, copy and paste the following code snippet (including `---` dashes) into your new file:

 src/pages/index.astro ` --- // Welcome to Astro! Everything between these triple-dash code fences // is your "component frontmatter". It never runs in the browser. console . log ( ' This runs in your terminal, not the browser! ' ); --- &#x3C;!-- Below is your "component template." It's just HTML, but with some magic sprinkled in to help you build great templates. --> &#x3C; html > &#x3C; body > &#x3C; h1 > Hello, World! &#x3C;/ h1 > &#x3C;/ body > &#x3C;/ html > &#x3C; style > h1 { color : orange ; } &#x3C;/ style > `  
# Hello, World!
  ">

-
 Create your first static asset

You will also want to create a `public/` directory to store your static assets. Astro will always include these assets in your final build, so you can safely reference them from inside your component templates.

In your text editor, create a new file in your directory at `public/robots.txt`. `robots.txt` is a simple file that most sites will include to tell search bots like Google how to treat your site.

For this guide, copy and paste the following code snippet into your new file:

 public/robots.txt ` # Example: Allow all bots to scan and index your site. # Full syntax: https://developers.google.com/search/docs/advanced/robots/create-robots-txt User-agent: * Allow: / `

-
 Create `astro.config.mjs`

Astro is configured using `astro.config.mjs`. This file is optional if you do not need to configure Astro, but you may wish to create it now.

Create `astro.config.mjs` at the root of your project, and copy the code below into it:

 astro.config.mjs ` import { defineConfig } from " astro/config " ;
 // https://astro.build/config export default defineConfig ({}); `
 If you want to include UI framework components such as React, Svelte, etc. or use other tools such as MDX or Partytown in your project, here is where you will manually import and configure integrations .

 Read Astro’s API configuration reference for more information.

-
 Add TypeScript support

TypeScript is configured using `tsconfig.json`. Even if you don’t write TypeScript code, this file is important so that tools like Astro and VS Code know how to understand your project. Some features (like npm package imports) aren’t fully supported in the editor without a `tsconfig.json` file.

If you do intend to write TypeScript code, using Astro’s `strict` or `strictest` template is recommended. You can view and compare the three template configurations at astro/tsconfigs/ .

Create `tsconfig.json` at the root of your project, and copy the code below into it. (You can use `base`, `strict`, or `strictest` for your TypeScript template):

 tsconfig.json ` { "extends" : " astro/tsconfigs/ base " } `

 Read Astro’s TypeScript setup guide for more information.

-
 Next Steps

If you have followed the steps above, your project directory should now look like this:

 Directory node_modules/ …
 - Directory public/
 robots.txt
 - Directory src/
 Directory pages/
 index.astro
 - astro.config.mjs
- package-lock.json or `yarn.lock`, `pnpm-lock.yaml`, etc.
- package.json
- tsconfig.json

-
 You can now start the Astro dev server and see a live preview of your project while you build!

 Learn

 Contribute

 Community

 Sponsor

## Why Astro

# Why Astro?

 Astro is the web framework for building content-driven websites like blogs, marketing, and e-commerce. Astro is best-known for pioneering a new frontend architecture to reduce JavaScript overhead and complexity compared to other frameworks. If you need a website that loads fast and has great SEO, then Astro is for you.

## Features
 Section titled “Features”
 Astro is an all-in-one web framework. It includes everything you need to create a website, built-in. There are also hundreds of different integrations and API hooks available to customize a project to your exact use case and needs.

Some highlights include:

- Islands : A component-based web architecture optimized for content-driven websites.

- UI-agnostic : Supports React, Preact, Svelte, Vue, Solid, HTMX, web components, and more.

- Server-first : Moves expensive rendering off of your visitors’ devices.

- Zero JS, by default : Less client-side JavaScript to slow your site down.

- Content collections : Organize, validate, and provide TypeScript type-safety for your Markdown content.

- Customizable : Partytown, MDX, and hundreds of integrations to choose from.

## Design Principles
 Section titled “Design Principles”
 Here are five core design principles to help explain why we built Astro, the problems that it exists to solve, and why Astro may be the best choice for your project or team.

Astro is…

- Content-driven : Astro was designed to showcase your content.

- Server-first : Websites run faster when they render HTML on the server.

- Fast by default : It should be impossible to build a slow website in Astro.

- Easy to use : You don’t need to be an expert to build something with Astro.

- Developer-focused : You should have the resources you need to be successful.

### Content-driven
 Section titled “Content-driven”
 Astro was designed for building content-rich websites. This includes marketing sites, publishing sites, documentation sites, blogs, portfolios, landing pages, community sites, and e-commerce sites. If you have content to show, it needs to reach your reader quickly.

By contrast, most modern web frameworks were designed for building web applications . These frameworks excel at building more complex, application-like experiences in the browser: logged-in admin dashboards, inboxes, social networks, todo lists, and even native-like applications like Figma and Ping . However with that complexity, they can struggle to provide great performance when delivering your content.

Astro’s focus on content from its beginnings as a static site builder have allowed Astro to sensibly scale up to performant, powerful, dynamic web applications that still respect your content and your audience. Astro’s unique focus on content lets Astro make tradeoffs and deliver unmatched performance features that wouldn’t make sense for more application-focused web frameworks to implement.

### Server-first
 Section titled “Server-first”
 Astro leverages server rendering over client-side rendering in the browser as much as possible. This is the same approach that traditional server-side frameworks -- PHP, WordPress, Laravel, Ruby on Rails, etc. -- have been using for decades. But you don’t need to learn a second server-side language to unlock it. With Astro, everything is still just HTML, CSS, and JavaScript (or TypeScript, if you prefer).

This approach stands in contrast to other modern JavaScript web frameworks like Next.js, SvelteKit, Nuxt, Remix, and others. These frameworks were built for client-side rendering of your entire website and include server-side rendering mainly to address performance concerns. This approach has been dubbed the Single-Page App (SPA) , in contrast with Astro’s Multi-Page App (MPA) approach.

The SPA model has its benefits. However, these come at the expense of additional complexity and performance tradeoffs. These tradeoffs harm page performance -- critical metrics like Time to Interactive (TTI) -- which doesn’t make much sense for content-focused websites where first-load performance is essential.

Astro’s server-first approach allows you to opt in to client-side rendering only if, and exactly as, necessary. You can choose to add UI framework components that run on the client. You can take advantage of Astro’s view transitions router for finer control over select page transitions and animations. Astro’s server-first rendering, either pre-rendered or on-demand, provides performant defaults that you can enhance and extend.

### Fast by default
 Section titled “Fast by default”
 Good performance is always important, but it is especially critical for websites whose success depends on displaying your content. It has been well-proven that poor performance loses you engagement, conversions, and money. For example:

- Every 100ms faster → 1% more conversions ( Mobify , earning +$380,000/yr)

- 50% faster → 12% more sales ( AutoAnything )

- 20% faster → 10% more conversions ( Furniture Village )

- 40% faster → 15% more sign-ups ( Pinterest )

- 850ms faster → 7% more conversions ( COOK )

- Every 1 second slower → 10% fewer users ( BBC )

In many web frameworks, it is easy to build a website that looks great during development only to load painfully slow once deployed. JavaScript is often the culprit, since many phones and lower-powered devices rarely match the speed of a developer’s laptop.

Astro’s magic is in how it combines the two values explained above -- a content focus with a server-first architecture -- to make tradeoffs and deliver features that other frameworks cannot. The result is amazing web performance for every website, out of the box. Our goal: It should be nearly impossible to build a slow website with Astro.

An Astro website can load 40% faster with 90% less JavaScript than the same site built with the most popular React web framework. But don’t take our word for it: watch Astro’s performance leave Ryan Carniato (creator of Solid.js and Marko) speechless .

### Easy to use
 Section titled “Easy to use”
 Astro’s goal is to be accessible to every web developer. Astro was designed to feel familiar and approachable regardless of skill level or past experience with web development.

The `.astro` UI language is a superset of HTML: any valid HTML is valid Astro templating syntax! So, if you can write HTML, you can write Astro components! But, it also combines some of our favorite features borrowed from other component languages like JSX expressions (React) and CSS scoping by default (Svelte and Vue). This closeness to HTML also makes it easier to use progressive enhancement and common accessibility patterns without any overhead.

We then made sure that you could also use your favorite UI component languages that you already know, and even reuse components you might already have. React, Preact, Svelte, Vue, Solid, and others, including web components, are all supported for authoring UI components in an Astro project.

Astro was designed to be less complex than other UI frameworks and languages. One big reason for this is that Astro was designed to render on the server, not in the browser. That means that you don’t need to worry about hooks (React), stale closures (also React), refs (Vue), observables (Svelte), atoms, selectors, reactions, or derivations. There is no reactivity on the server, so all of that complexity melts away.

One of our favorite sayings is opt in to complexity. We designed Astro to remove as much “required complexity” as possible from the developer experience, especially as you onboard for the first time. You can build a “Hello World” example website in Astro with just HTML and CSS. Then, when you need to build something more powerful, you can incrementally reach for new features and APIs as you go.

### Developer-focused
 Section titled “Developer-focused”
 We strongly believe that Astro is only a successful project if people love using it. Astro has everything you need to support you as you build with Astro.

Astro invests in developer tools like a great CLI experience from the moment you open your terminal, an official VS Code extension for syntax highlighting, TypeScript and Intellisense, and documentation actively maintained by hundreds of community contributors and available in 14 languages.

Our welcoming, respectful, inclusive community on Discord is ready to provide support, motivation, and encouragement. Open a `#support` thread to get help with your project. Visit our dedicated `#showcase` channel for sharing your Astro sites, blog posts, videos, and even work-in-progress for safe feedback and constructive criticism. Participate in regular live events such as our weekly community call, “Talking and Doc’ing,” and API/bug bashes.

As an open-source project, we welcome contributions of all types and sizes from community members of all experience levels. You are invited to join in roadmap discussions to shape the future of Astro, and we hope you’ll contribute fixes and features to the core codebase, compiler, docs, language tools, websites, and other projects.

 Learn

 Contribute

 Community

 Sponsor

## Islands

# Islands architecture

 Astro helped pioneer and popularize a new frontend architecture pattern called Islands Architecture. Islands architecture works by rendering the majority of your page to fast, static HTML with smaller “islands” of JavaScript added when interactivity or personalization is needed on the page (an image carousel, for example). This avoids the monolithic JavaScript payloads that slow down the responsiveness of many other, modern JavaScript web frameworks.

## A brief history
 Section titled “A brief history”
 The term “component island” was first coined by Etsy’s frontend architect Katie Sylor-Miller in 2019. This idea was then expanded on and documented in this post by Preact creator Jason Miller on August 11, 2020.

The general idea of an “Islands” architecture is deceptively simple: render HTML pages on the server, and inject placeholders or slots around highly dynamic regions […] that can then be “hydrated” on the client into small self-contained widgets, reusing their server-rendered initial HTML.
— Jason Miller, Creator of Preact

The technique that this architectural pattern builds on is also known as partial or selective hydration.

In contrast, most JavaScript-based web frameworks hydrate &#x26; render an entire website as one large JavaScript application (also known as a single-page application, or SPA). SPAs provide simplicity and power but suffer from page-load performance problems due to heavy client-side JavaScript usage.

SPAs have their place, even embedded inside an Astro page . But, SPAs lack the native ability to selectively and strategically hydrate, making them a heavy-handed choice for most projects on the web today.

Astro became popular as the first mainstream JavaScript web framework with selective hydration built-in, using that same component islands pattern first coined by Sylor-Miller. We’ve since expanded and evolved on Sylor-Miller’s original work, which helped to inspire a similar component island approach to dynamically server-rendered content.

## What is an island?
 Section titled “What is an island?”
 In Astro, an island is an enhanced UI component on an otherwise static page of HTML.

A client island is an interactive JavaScript UI component that is hydrated separately from the rest of the page, while a server island is a UI component that server-renders its dynamic content separately from the rest of the page.

Both islands run expensive or slower processes independently, on a per-component basis, for optimized page loads.

## Island components
 Section titled “Island components”
 Astro components are the building blocks of your page template. They render to static HTML with no client-side runtime.

Think of a client island as an interactive widget floating in a sea of otherwise static, lightweight, server-rendered HTML. Server islands can be added for personalized or dynamic server-rendered elements, such as a logged in visitor’s profile picture.

 Header (interactive island)
 Sidebar (static HTML)
 Static content like text, images, etc.

 Image carousel (interactive island)
 Footer (static HTML)

Source: Islands Architecture: Jason Miller

An island always runs in isolation from other islands on the page, and multiple islands can exist on a page. Client islands can still share state and communicate with each other, even though they run in different component contexts.

This flexibility allows Astro to support multiple UI frameworks like React , Preact , Svelte , Vue , and SolidJS . Because they are independent, you can even mix several frameworks on each page.

## Client Islands
 Section titled “Client Islands”
 By default, Astro will automatically render every UI component to just HTML &#x26; CSS, stripping out all client-side JavaScript automatically.

 - src/pages/index.astro ` &#x3C; MyReactComponent /> ` ">
 This may sound strict, but this behavior is what keeps Astro websites fast by default and protects developers from accidentally sending unnecessary or unwanted JavaScript that might slow down their website.

Turning any static UI component into an interactive island requires only a `client:*` directive. Astro then automatically builds and bundles your client-side JavaScript for optimized performance.

 src/pages/index.astro ` &#x3C;!-- This component is now interactive on the page! The rest of your website remains static. --> &#x3C; MyReactComponent client:load /> ` ">
 With islands, client-side JavaScript is only loaded for the explicit interactive components that you mark using `client:*` directives.

And because interaction is configured at the component-level, you can handle different loading priorities for each component based on its usage. For example, `client:idle` tells a component to load when the browser becomes idle, and `client:visible` tells a component to load only once it enters the viewport.

### Benefits of client islands

The most obvious benefit of building with Astro Islands is performance: the majority of your website is converted to fast, static HTML and JavaScript is only loaded for the individual components that need it. JavaScript is one of the slowest assets that you can load per-byte, so every byte counts.

Another benefit is parallel loading. In the example illustration above, the low-priority “image carousel” island doesn’t need to block the high-priority “header” island. The two load in parallel and hydrate in isolation, meaning that the header becomes interactive immediately without having to wait for the heavier carousel lower down the page.

Even better, you can tell Astro exactly how and when to render each component. If that image carousel is really expensive to load, you can attach a special client directive that tells Astro to only load the carousel when it becomes visible on the page. If the user never sees it, it never loads.

In Astro, it’s up to you as the developer to explicitly tell Astro which components on the page need to also run in the browser. Astro will only hydrate exactly what’s needed on the page and leave the rest of your site as static HTML.

 Client islands are the secret to Astro’s fast-by-default performance story!

 Read more about using JavaScript framework components in your project.

## Server islands
 Section titled “Server islands”
 Server islands are a way to move expensive or slow server-side code out of the way of the main rendering process, making it easy to combine high-performance static HTML and dynamic server-generated components.

Add the `server:defer` directive to any Astro component on your page to turn it into its own server island:

 src/pages/index.astro ` --- import Avatar from " ../components/Avatar.astro " ; --- &#x3C; Avatar server:defer /> ` ">
 This breaks up your page with smaller areas of server-rendered content that each load in parallel.

Your page’s main content can be rendered immediately with placeholder content, such as a generic avatar, until your island’s own content is available. With server islands, having small components of personalized content does not delay the rendering of an otherwise static page.

This rendering pattern was built to be portable. It does not depend on any server infrastructure so it will work with any host, from a Node.js server in a Docker container to the serverless provider of your choice.

### Benefits of server islands

One benefit of server islands is the ability to render the more highly dynamic parts of your page on the fly. This allows the outer shell and main content to be more aggressively cached, providing faster performance.

Another benefit is providing a great visitor experience. Server islands are optimized and load quickly, often even before the browser has even painted the page. But in the short time it takes for your islands to render, you can display custom fallback content and prevent any layout shift.

An example of a site that benefits from Astro’s server islands is an e-commerce storefront. Although the main content of product pages change infrequently, these pages typically have some dynamic pieces:

 The user’s avatar in the header.

- Special deals and sales for the product.

- User reviews.

Using server islands for these elements, your visitor will see the most important part of the page, your product, immediately. Generic avatars, loading spinners, and store announcements can be displayed as fallback content until the personalized parts are available.

 Read more about using server islands in your project.

 Learn

 Contribute

 Community

 Sponsor

## Project Structure

# Project structure

 Your new Astro project generated from the `create astro` CLI wizard already includes some files and folders. Others, you will create yourself and add to Astro’s existing file structure.

Here’s how an Astro project is organized, and some files you will find in your new project.

## Directories and Files
 Section titled “Directories and Files”
 Astro leverages an opinionated folder layout for your project. Every Astro project root should include the following directories and files:

- `src/*` - Your project source code (components, pages, styles, images, etc.)

- `public/*` - Your non-code, unprocessed assets (fonts, icons, etc.)

- `package.json` - A project manifest.

- `astro.config.mjs` - An Astro configuration file. (recommended)

- `tsconfig.json` - A TypeScript configuration file. (recommended)

### Example Project Tree
 Section titled “Example Project Tree”
 A common Astro project directory might look like this:

 - Directory public/
 robots.txt
- favicon.svg
- my-cv.pdf
 - Directory src/
 Directory blog/
 post1.md
- post2.md
- post3.md
 - Directory components/
 Header.astro
- Button.jsx
 - Directory images/
 image1.jpg
- image2.jpg
- image3.jpg
 - Directory layouts/
 PostLayout.astro
 - Directory pages/
 Directory posts/
 [post].astro
 - about.astro
- index.astro
- rss.xml.js
 - Directory styles/
 global.css
 - content.config.ts
 - astro.config.mjs
- package.json
- tsconfig.json

### `src/`
 Section titled “src/”
 The `src/` folder is where most of your project source code lives. This includes:

- Pages

- Layouts

- Astro components

- UI framework components (React, etc.)

- Styles (CSS, Sass)

- Markdown

- Images to be optimized and processed by Astro

Astro processes, optimizes, and bundles your `src/` files to create the final website that is shipped to the browser. Unlike the static `public/` directory, your `src/` files are built and handled for you by Astro.

Some files (like Astro components) are not even sent to the browser as written but are instead rendered to static HTML. Other files (like CSS) are sent to the browser but may be optimized or bundled with other CSS files for performance.

### `src/pages`
 Section titled “src/pages”
 Pages routes are created for your site by adding supported file types to this directory.

### `src/components`
 Section titled “src/components”
 Components are reusable units of code for your HTML pages. These could be Astro components , or UI framework components like React or Vue. It is common to group and organize all of your project components together in this folder.

This is a common convention in Astro projects, but it is not required. Feel free to organize your components however you like!

### `src/layouts`
 Section titled “src/layouts”
 Layouts are Astro components that define the UI structure shared by one or more pages .

Just like `src/components`, this directory is a common convention but not required.

### `src/styles`
 Section titled “src/styles”
 It is a common convention to store your CSS or Sass files in a `src/styles` directory, but this is not required. As long as your styles live somewhere in the `src/` directory and are imported correctly, Astro will handle and optimize them.

### `public/`
 Section titled “public/”
 The `public/` directory is for files and assets in your project that do not need to be processed during Astro’s build process. The files in this folder will be copied into the build folder untouched, and then your site will be built.

This behavior makes `public/` ideal for common assets that do not require any processing, like some images and fonts, or special files such as `robots.txt` and `manifest.webmanifest`.

You can place CSS and JavaScript in your `public/` directory, but be aware that those files will not be bundled or optimized in your final build.

### `package.json`
 Section titled “package.json”
 This is a file used by JavaScript package managers to manage your dependencies. It also defines the scripts that are commonly used to run Astro (ex: `npm run dev`, `npm run build`).

There are two kinds of dependencies you can specify in a `package.json`: `dependencies` and `devDependencies`. In most cases, these work the same: Astro needs all dependencies at build time, and your package manager will install both. We recommend putting all of your dependencies in `dependencies` to start, and only use `devDependencies` if you find a specific need to do so.

For help creating a new `package.json` file for your project, check out the manual setup instructions.

### `astro.config.mjs`
 Section titled “astro.config.mjs”
 This file is generated in every starter template and includes configuration options for your Astro project. Here you can specify integrations to use, build options, server options, and more.

Astro supports several file formats for its JavaScript configuration file: `astro.config.js`, `astro.config.mjs` and `astro.config.ts`. We recommend using `.mjs` in most cases or `.ts` if you want to write TypeScript in your config file.

TypeScript config file loading is handled using `tsm` and will respect your project’s `tsconfig` options.

See the configuration reference for complete details.

### `tsconfig.json`
 Section titled “tsconfig.json”
 This file is generated in every starter template and includes TypeScript configuration options for your Astro project. Some features (like npm package imports) aren’t fully supported in the editor without a `tsconfig.json` file.

See the TypeScript Guide for details on setting configurations.

 Learn

 Contribute

 Community

 Sponsor

## Develop And Build

# Develop and build

 Once you have an Astro project, now you’re ready to build with Astro! 🚀

## Edit your project
 Section titled “Edit your project”
 To make changes to your project, open your project folder in your code editor. Working in development mode with the dev server running allows you to see updates to your site as you edit the code.

You can also customize aspects of your development environment such as configuring TypeScript or installing the official Astro editor extensions.

### Start the Astro dev server
 Section titled “Start the Astro dev server”
 Astro comes with a built-in development server that has everything you need for project development. The `astro dev` CLI command will start the local development server so that you can see your new website in action for the very first time.

Every starter template comes with a pre-configured script that will run `astro dev` for you. After navigating into your project directory, use your favorite package manager to run this command and start the Astro development server.

 -

 npm

-

 pnpm

-

 Yarn

 - Terminal window ` npm run dev `

 Terminal window
```
` pnpm run dev `
```

 Terminal window
```
` yarn run dev `
```

 If all goes well, Astro will now be serving your project on http://localhost:4321/ . Visit that link in your browser and see your new site!

### Work in development mode
 Section titled “Work in development mode”
 Astro will listen for live file changes in your `src/` directory and update your site preview as you build, so you will not need to restart the server as you make changes during development. You will always be able to see an up-to-date version of your site in your browser when the dev server is running.

When viewing your site in the browser, you’ll have access to the Astro dev toolbar . As you build, it will help you inspect your islands , spot accessibility issues, and more.

If you aren’t able to open your project in the browser after starting the dev server, go back to the terminal where you ran the `dev` command and check the message displayed. It should tell you if an error occurred, or if your project is being served at a different URL than http://localhost:4321/ .

## Build and preview your site
 Section titled “Build and preview your site”
 To check the version of your site that will be created at build time, quit the dev server ( Ctrl + C ) and run the appropriate build command for your package manager in your terminal:

 npm

-

 pnpm

-

 Yarn

 Terminal window ` npm run build `

 Terminal window
```
` pnpm build `
```

 Terminal window
```
` yarn run build `
```

 Astro will build a deploy-ready version of your site in a separate folder (`dist/` by default) and you can watch its progress in the terminal. This will alert you to any build errors in your project before you deploy to production. If TypeScript is configured to `strict` or `strictest`, the `build` script will also check your project for type errors.

When the build is finished, run the appropriate `preview` command (e.g. `npm run preview`) in your terminal and you can view the built version of your site locally in the same browser preview window.

Note that this previews your code as it existed when the build command was last run. This is meant to give you a preview of how your site will look when it is deployed to the web. Any later changes you make to your code after building will not be reflected while you preview your site until you run the build command again.

Use ( Ctrl + C ) to quit the preview and run another terminal command, such as restarting the dev server to go back to working in development mode which does update as you edit to show a live preview of your code changes.

 Read more about the Astro CLI and the terminal commands you will use as you build with Astro.

## Next Steps
 Section titled “Next Steps”
 Success! You are now ready to start building with Astro! 🥳

Here are a few things that we recommend exploring next. You can read them in any order. You can even leave our documentation for a bit and go play in your new Astro project codebase, coming back here whenever you run into trouble or have a question.

### Configure your dev environment
 Section titled “Configure your dev environment”
 Explore the guides below to customize your development experience.

 Editor Setup

 Customize your code editor to improve the Astro developer experience and unlock new features.

 Dev Toolbar

 Explore the helpful features of the dev toolbar.

 TypeScript Configuration

 Configure options for type-checking, IntelliSense, and more.

### Explore Astro’s Features
 Section titled “Explore Astro’s Features”

 Understand your codebase

 Learn about Astro’s file structure in our Project Structure guide.

 Create content collections

 Add content to your new site with frontmatter validation and automatic type-safety.

 Add view transitions

 Create seamless page transitions and animations.

 Learn about Islands

 Read about Astro's islands architecture.

### Take the introductory tutorial
 Section titled “Take the introductory tutorial”
 Build a fully functional Astro blog starting from a single blank page in our introductory tutorial .

This is a great way to see how Astro works and walks you through the basics of pages, layouts, components, routing, islands, and more. It also includes an optional, beginner-friendly unit for those newer to web development concepts in general, which will guide you through installing the necessary applications on your computer, creating a GitHub account, and deploying your site.

 Learn

 Contribute

 Community

 Sponsor