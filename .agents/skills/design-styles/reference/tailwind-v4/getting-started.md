# Tailwind CSS - Getting Started


## Installation

### Installing Tailwind CSS as a Vite plugin
Installing Tailwind CSS as a Vite plugin is the most seamless way to integrate it with frameworks like Laravel, SvelteKit, React Router, Nuxt, and SolidJS.

## Editor Setup

## Syntax support

Tailwind CSS uses custom CSS syntax like `@theme`, `@variant`, and `@source`, and in some editors this can trigger warnings or errors where these rules aren&#x27;t recognized.

If you&#x27;re using VS Code, our official Tailwind CSS IntelliSense plugin includes a dedicated Tailwind CSS language mode that has support for all of the custom at-rules and functions Tailwind uses.

In some cases, you may need to disable native CSS linting/validations if your editor is very strict about the syntax it expects in your CSS files.

## Cursor

 Cursor is an AI-native code editor with features like context-aware autocomplete and built-in coding agents. Since it supports VS Code extensions, all of the Tailwind CSS tooling you&#x27;re already familiar with works out of the box – including our official Tailwind CSS IntelliSense extension and the Prettier plugin for class sorting.

Check out and download Cursor .

## Zed

 Zed is a fast, modern code editor, designed from the ground-up for cutting-edge development workflows, including agentic editing with AI. It has built-in support for Tailwind CSS autocompletions, linting, and hover previews, without the need to install and configure a separate extension. It also integrates tightly with Prettier, so our official Prettier plugin works seamlessly with Zed when installed.

Check out Zed and learn more about how it works with Tailwind CSS .

## IntelliSense for VS Code

The official Tailwind CSS IntelliSense extension for Visual Studio Code enhances the Tailwind development experience by providing users with advanced features such as autocomplete, syntax highlighting, and linting.

- Autocomplete — providing intelligent suggestions for utility classes, as well as CSS functions and directives .

- Linting — highlighting errors and potential bugs in both your CSS and your markup.

- Hover previews — revealing the complete CSS for utility classes when you hover over them.

- Syntax highlighting — so that Tailwind features that use custom CSS syntax are highlighted correctly.

Check out the project on GitHub to learn more, or add it to Visual Studio Code to get started now.

## Class sorting with Prettier

We maintain an official Prettier plugin for Tailwind CSS that automatically sorts your classes following our recommended class order .

It works seamlessly with custom Tailwind configurations, and because it’s just a Prettier plugin, it works anywhere Prettier works — including every popular editor and IDE, and of course on the command line.

 HTML

## Compatibility

## Browser support

Tailwind CSS v4.0 is designed for and tested on modern browsers, and the core functionality of the framework specifically depends on these browser versions:

- Chrome 111 (released March 2023)

- Safari 16.4 (released March 2023)

- Firefox 128 (released July 2024)

Tailwind also includes support for many bleeding-edge platform features like `field-sizing: content`, `@starting-style`, and `text-wrap: balance` that have limited browser support. It&#x27;s up to you if you want to use these modern features in your projects — if the browsers you&#x27;re targeting don&#x27;t support them, simply don&#x27;t use those utilities and variants.

If you&#x27;re unsure about the support for a modern platform feature, the Can I use database is a great resource.

## Sass, Less, and Stylus

Tailwind CSS v4.0 is a full-featured CSS build tool designed for a specific workflow, and is not designed to be used with CSS preprocessors like Sass, Less, or Stylus.

 Think of Tailwind CSS itself as your preprocessor — you shouldn&#x27;t use Tailwind with Sass for the same reason you wouldn&#x27;t use Sass with Stylus.

Since Tailwind is designed for modern browsers, you actually don&#x27;t need a preprocessor for things like nesting or variables, and Tailwind itself will do things like bundle your imports and add vendor prefixes.

### Build-time imports

Tailwind will automatically bundle other CSS files you include with `@import`, without the need for a separate preprocessing tool.

 app.css

## Upgrade Guide

Tailwind CSS v4.0 is a new major version of the framework, so while we&#x27;ve worked really hard to minimize breaking changes, some updates are necessary. This guide outlines all the steps required to upgrade your projects from v3 to v4.

 Tailwind CSS v4.0 is designed for Safari 16.4+, Chrome 111+, and Firefox 128+. If you need to support older browsers, stick with v3.4 until your browser support requirements change.

## Using the upgrade tool

If you&#x27;d like to upgrade a project from v3 to v4, you can use our upgrade tool to do the vast majority of the heavy lifting for you:

 Terminal