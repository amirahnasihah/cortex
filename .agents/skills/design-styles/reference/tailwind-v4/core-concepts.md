# Tailwind CSS - Core Concepts


## Styling With Utility Classes

## Overview

You style things with Tailwind by combining many single-purpose presentational classes (utility classes) directly in your markup:

 ChitChat

## Hover Focus And Other States

Every utility class in Tailwind can be applied conditionally by adding a variant to the beginning of the class name that describes the condition you want to target.

For example, to apply the `bg-sky-700` class on hover, use the `hover:bg-sky-700` class:

 Hover over this button to see the background color change

## Responsive Design

## Overview

Every utility class in Tailwind can be applied conditionally at different breakpoints, which makes it a piece of cake to build complex responsive interfaces without ever leaving your HTML.

First, make sure you&#x27;ve added the viewport meta tag to the `<head>` of your document:

 index.html

## Dark Mode

## Overview

Now that dark mode is a first-class feature of many operating systems, it&#x27;s becoming more and more common to design a dark version of your website to go along with the default design.

To make this as easy as possible, Tailwind includes a `dark` variant that lets you style your site differently when dark mode is enabled:

 Light mode

## Theme

## Overview

Tailwind is a framework for building custom designs, and different designs need different typography, colors, shadows, breakpoints, and more.

These low-level design decisions are often called design tokens , and in Tailwind projects you store those values in theme variables .

### What are theme variables?

Theme variables are special CSS variables defined using the `@theme` directive that influence which utility classes exist in your project.

For example, you can add a new color to your project by defining a theme variable like `--color-mint-500`:

 app.css

## Colors

Tailwind CSS includes a vast, beautiful color palette out of the box, carefully crafted by expert designers and suitable for a wide range of different design styles.

## Adding Custom Styles

Often the biggest challenge when working with a framework is figuring out what you’re supposed to do when there’s something you need that the framework doesn’t handle for you.

Tailwind has been designed from the ground up to be extensible and customizable, so that no matter what you’re building you never feel like you’re fighting the framework.

This guide covers topics like customizing your design tokens, how to break out of those constraints when necessary, adding your own custom CSS, and extending the framework with plugins.

## Customizing your theme

If you want to change things like your color palette, spacing scale, typography scale, or breakpoints, add your customizations using the `@theme` directive in your CSS:

 CSS

## Detecting Classes In Source Files

## Overview

Tailwind works by scanning your project for utility classes, then generating all of the necessary CSS based on the classes you&#x27;ve actually used.

This makes sure your CSS is as small as possible, and is also what makes features like arbitrary values possible.

### How classes are detected

Tailwind treats all of your source files as plain text, and doesn&#x27;t attempt to actually parse your files as code in any way.

Instead it just looks for any tokens in your file that could be classes based on which characters Tailwind is expecting in class names:

 JSX

## Functions And Directives

## Directives

Directives are custom Tailwind-specific at-rules you can use in your CSS that offer special functionality for Tailwind CSS projects.

### @import

Use the `@import` directive to inline import CSS files, including Tailwind itself:

 CSS