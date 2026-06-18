# TypeScript - Tutorials


## Asp Net Core

Was this page helpful?

# ASP.NET Core

## Install ASP.NET Core and TypeScript

 First, install ASP.NET Core if you need it. This quick-start guide requires Visual Studio 2015 or 2017.

Next, if your version of Visual Studio does not already have the latest TypeScript, you can install it .

## Create a new project

- Choose File

- Choose New Project (Ctrl + Shift + N)

- Search for .NET Core in the project search bar

- Select ASP.NET Core Web Application and press the Next button

- Name your project and solution. After select the Create button

- In the last window, select the Empty template and press the Create button

Run the application and make sure that it works.

### Set up the server

 Open Dependencies > Manage NuGet Packages > Browse. Search and install `Microsoft.AspNetCore.StaticFiles` and `Microsoft.TypeScript.MSBuild`:

Open up your `Startup.cs` file and edit your `Configure` function to look like this:

 `public void Configure(IApplicationBuilder app, IHostEnvironment env)
{
 if (env.IsDevelopment())
 {
 app.UseDeveloperExceptionPage();
 }

 app.UseDefaultFiles();
 app.UseStaticFiles();
}`
 You may need to restart VS for the red squiggly lines below `UseDefaultFiles` and `UseStaticFiles` to disappear.

## Add TypeScript

 Next we will add a new folder and call it `scripts`.

## Add TypeScript code

 Right click on `scripts` and click New Item . Then choose TypeScript File and name the file `app.ts`

### Add example code

 Add the following code to the `app.ts` file.

 ts ` function sayHello () { const compiler = ( document . getElementById ( "compiler" ) as HTMLInputElement ) . value ; const framework = ( document . getElementById ( "framework" ) as HTMLInputElement ) . value ; return `Hello from ${ compiler } and ${ framework } !` ; } `

## Set up the build

 Configure the TypeScript compiler

First we need to tell TypeScript how to build. Right click on `scripts` and click New Item . Then choose TypeScript Configuration File and use the default name of `tsconfig.json`

Replace the contents of the `tsconfig.json` file with:

 ` { " compilerOptions " : { " noEmitOnError " : true , " noImplicitAny " : true , " sourceMap " : true , " target " : "es6" }, " files " : [ "./app.ts" ], "compileOnSave" : true } `

- `noEmitOnError` : Do not emit outputs if any errors were reported.

- `noImplicitAny` : Raise error on expressions and declarations with an implied `any` type.

- `sourceMap` : Generates corresponding `.map` file.

- `target` : Specify ECMAScript target version.

 Note: `"ESNext"` targets latest supported

 `noImplicitAny` is good idea whenever you’re writing new code — you can make sure that you don’t write any untyped code by mistake. `"compileOnSave"` makes it easy to update your code in a running web app.

#### Set up NPM

 We need to setup NPM so that JavaScript packages can be downloaded. Right click on the project and select New Item . Then choose NPM Configuration File and use the default name of `package.json`.

Inside the `"devDependencies"` section of the `package.json` file, add gulp and del

 ` "devDependencies" : { "gulp" : "4.0.2" , "del" : "5.1.0" } `
 Visual Studio should start installing gulp and del as soon as you save the file. If not, right-click package.json and then Restore Packages.

After you should see an `npm` folder in your solution explorer

#### Set up gulp

 Right click on the project and click New Item . Then choose JavaScript File and use the name of `gulpfile.js`

 js ` /// <binding AfterBuild='default' Clean='clean' /> /* This file is the main entry point for defining Gulp tasks and using Gulp plugins. Click here to learn more. http://go.microsoft.com/fwlink/?LinkId=518007 */ var gulp = require ( "gulp" ); var del = require ( "del" ); var paths = { scripts: [ "scripts/**/*.js" , "scripts/**/*.ts" , "scripts/**/*.map" ], }; gulp . task ( "clean" , function () { return del ([ "wwwroot/scripts/**/*" ]); }); gulp . task ( "default" , function ( done ) { gulp . src ( paths . scripts ). pipe ( gulp . dest ( "wwwroot/scripts" )); done (); }); `
 The first line tells Visual Studio to run the task ‘default’ after the build finishes. It will also run the ‘clean’ task when you ask Visual Studio to clean the build.

Now right-click on `gulpfile.js` and click Task Runner Explorer.

If ‘default’ and ‘clean’ tasks don’t show up, refresh the explorer:

## Write a HTML page

 Right click on the `wwwroot` folder (if you don’t see the folder try building the project) and add a New Item named `index.html` inside. Use the following code for `index.html`

 ` <!DOCTYPE html> <html> <head> <meta charset="utf-8" /> <script src="scripts/app.js"></script> <title></title> </head> <body> <div id="message"></div> <div> Compiler: <input id="compiler" value="TypeScript" onkeyup="document.getElementById('message').innerText = sayHello()" /><br /> Framework: <input id="framework" value="ASP.NET" onkeyup="document.getElementById('message').innerText = sayHello()" /> </div> </body> </html> `

## Test

- Run the project

- As you type on the boxes you should see the message appear/change!

## Debug

- In Edge, press F12 and click the Debugger tab.

- Look in the first localhost folder, then scripts/app.ts

- Put a breakpoint on the line with return.

- Type in the boxes and confirm that the breakpoint hits in TypeScript code and that inspection works correctly.

Congrats you’ve built your own .NET Core project with a TypeScript frontend.
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: BK OT GC DR LZ 14+ Last updated: Jun 15, 2026

## Gulp

Was this page helpful?

# Gulp
 This quick start guide will teach you how to build TypeScript with gulp and then add Browserify , terser , or Watchify to the gulp pipeline.
This guide also shows how to add Babel functionality using Babelify .

We assume that you’re already using Node.js with npm .

## Minimal project

 Let’s start out with a new directory.
We’ll name it `proj` for now, but you can change it to whatever you want.

 shell ` mkdir proj cd proj `
 To start, we’re going to structure our project in the following way:

 ` proj/ ├─ src/ └─ dist/ `
 TypeScript files will start out in your `src` folder, run through the TypeScript compiler and end up in `dist`.

Let’s scaffold this out:

 shell ` mkdir src mkdir dist `

### Initialize the project

 Now we’ll turn this folder into an npm package.

 shell ` npm init `
 You’ll be given a series of prompts.
You can use the defaults except for your entry point.
For your entry point, use `./dist/main.js`.
You can always go back and change these in the `package.json` file that’s been generated for you.

### Install our dependencies

 Now we can use `npm install` to install packages.
First install `gulp-cli` globally (if you use a Unix system, you may need to prefix the `npm install` commands in this guide with `sudo`).

 shell ` npm install -g gulp-cli `
 Then install `typescript`, `gulp` and `gulp-typescript` in your project’s dev dependencies.
 Gulp-typescript is a gulp plugin for TypeScript.

 shell ` npm install --save-dev typescript gulp@4.0.0 gulp-typescript `

### Write a simple example

 Let’s write a Hello World program.
In `src`, create the file `main.ts`:

 ts ` function hello ( compiler : string ) { console . log ( `Hello from ${ compiler } ` ); } hello ( "TypeScript" ); `
 In the project root, `proj`, create the file `tsconfig.json`:

 ` { " files " : [ "src/main.ts" ], " compilerOptions " : { " noImplicitAny " : true , " target " : "es5" } } `

### Create a `gulpfile.js`

 In the project root, create the file `gulpfile.js`:

 js ` var gulp = require ( "gulp" ); var ts = require ( "gulp-typescript" ); var tsProject = ts . createProject ( "tsconfig.json" ); gulp . task ( "default" , function () { return tsProject . src (). pipe ( tsProject ()). js . pipe ( gulp . dest ( "dist" )); }); `

### Test the resulting app

```
 shell ` gulp node dist/main.js `
```

 The program should print “Hello from TypeScript!“.

## Add modules to the code

 Before we get to Browserify, let’s build our code out and add modules to the mix.
This is the structure you’re more likely to use for a real app.

Create a file called `src/greet.ts`:

 ts ` export function sayHello ( name : string ) { return `Hello from ${ name } ` ; } `
 Now change the code in `src/main.ts` to import `sayHello` from `greet.ts`:

 ts ` import { sayHello } from "./greet" ; console . log ( sayHello ( "TypeScript" )); `
 Finally, add `src/greet.ts` to `tsconfig.json`:

 ` { " files " : [ "src/main.ts" , "src/greet.ts" ], " compilerOptions " : { " noImplicitAny " : true , " target " : "es5" } } `
 Make sure that the modules work by running `gulp` and then testing in Node:

 shell ` gulp node dist/main.js `
 Notice that even though we used ES2015 module syntax, TypeScript emitted CommonJS modules that Node uses.
We’ll stick with CommonJS for this tutorial, but you could set `module` in the options object to change this.

## Browserify

 Now let’s move this project from Node to the browser.
To do this, we’d like to bundle all our modules into one JavaScript file.
Fortunately, that’s exactly what Browserify does.
Even better, it lets us use the CommonJS module system used by Node, which is the default TypeScript emit.
That means our TypeScript and Node setup will transfer to the browser basically unchanged.

First, install browserify, tsify , and vinyl-source-stream.
tsify is a Browserify plugin that, like gulp-typescript, gives access to the TypeScript compiler.
vinyl-source-stream lets us adapt the file output of Browserify back into a format that gulp understands called vinyl .

 shell ` npm install --save-dev browserify tsify vinyl-source-stream `

### Create a page

 Create a file in `src` named `index.html`:

 html ` <!DOCTYPE html > <html> <head> <meta charset = "UTF-8" /> <title> Hello World! </title> </head> <body> <p id = "greeting" > Loading ... </p> <script src = "bundle.js" ></script> </body> </html> `
 Now change `main.ts` to update the page:

 ts ` import { sayHello } from "./greet" ; function showHello ( divName : string , name : string ) { const elt = document . getElementById ( divName ); elt . innerText = sayHello ( name ); } showHello ( "greeting" , "TypeScript" ); `
 Calling `showHello` calls `sayHello` to change the paragraph’s text.
Now change your gulpfile to the following:

 js ` var gulp = require ( "gulp" ); var browserify = require ( "browserify" ); var source = require ( "vinyl-source-stream" ); var tsify = require ( "tsify" ); var paths = { pages: [ "src/*.html" ], }; gulp . task ( "copy-html" , function () { return gulp . src ( paths . pages ). pipe ( gulp . dest ( "dist" )); }); gulp . task ( "default" , gulp . series ( gulp . parallel ( "copy-html" ), function () { return browserify ({ basedir: "." , debug: true , entries: [ "src/main.ts" ], cache: {}, packageCache: {}, }) . plugin ( tsify ) . bundle () . pipe ( source ( "bundle.js" )) . pipe ( gulp . dest ( "dist" )); }) ); `
 This adds the `copy-html` task and adds it as a dependency of `default`.
That means any time `default` is run, `copy-html` has to run first.
We’ve also changed `default` to call Browserify with the tsify plugin instead of gulp-typescript.
Conveniently, they both allow us to pass the same options object to the TypeScript compiler.

After calling `bundle` we use `source` (our alias for vinyl-source-stream) to name our output bundle `bundle.js`.

Test the page by running gulp and then opening `dist/index.html` in a browser.
You should see “Hello from TypeScript” on the page.

Notice that we specified `debug: true` to Browserify.
This causes tsify to emit source maps inside the bundled JavaScript file.
Source maps let you debug your original TypeScript code in the browser instead of the bundled JavaScript.
You can test that source maps are working by opening the debugger for your browser and putting a breakpoint inside `main.ts`.
When you refresh the page the breakpoint should pause the page and let you debug `greet.ts`.

## Watchify, Babel, and Terser

 Now that we are bundling our code with Browserify and tsify, we can add various features to our build with browserify plugins.

-
Watchify starts gulp and keeps it running, incrementally compiling whenever you save a file.
This lets you keep an edit-save-refresh cycle going in the browser.

-
Babel is a hugely flexible compiler that converts ES2015 and beyond into ES5 and ES3.
This lets you add extensive and customized transformations that TypeScript doesn’t support.

-
Terser compacts your code so that it takes less time to download.

### Watchify

 We’ll start with Watchify to provide background compilation:

 shell ` npm install --save-dev watchify fancy-log `
 Now change your gulpfile to the following:

 js ` var gulp = require ( "gulp" ); var browserify = require ( "browserify" ); var source = require ( "vinyl-source-stream" ); var watchify = require ( "watchify" ); var tsify = require ( "tsify" ); var fancy_log = require ( "fancy-log" ); var paths = { pages: [ "src/*.html" ], }; var watchedBrowserify = watchify ( browserify ({ basedir: "." , debug: true , entries: [ "src/main.ts" ], cache: {}, packageCache: {}, }). plugin ( tsify ) ); gulp . task ( "copy-html" , function () { return gulp . src ( paths . pages ). pipe ( gulp . dest ( "dist" )); }); function bundle () { return watchedBrowserify . bundle () . on ( "error" , fancy_log ) . pipe ( source ( "bundle.js" )) . pipe ( gulp . dest ( "dist" )); } gulp . task ( "default" , gulp . series ( gulp . parallel ( "copy-html" ), bundle )); watchedBrowserify . on ( "update" , bundle ); watchedBrowserify . on ( "log" , fancy_log ); `
 There are basically three changes here, but they require you to refactor your code a bit.

- We wrapped our `browserify` instance in a call to `watchify`, and then held on to the result.

- We called `watchedBrowserify.on('update', bundle);` so that Browserify will run the `bundle` function every time one of your TypeScript files changes.

- We called `watchedBrowserify.on('log', fancy_log);` to log to the console.

Together (1) and (2) mean that we have to move our call to `browserify` out of the `default` task.
And we have to give the function for `default` a name since both Watchify and Gulp need to call it.
Adding logging with (3) is optional but very useful for debugging your setup.

Now when you run Gulp, it should start and stay running.
Try changing the code for `showHello` in `main.ts` and saving it.
You should see output that looks like this:

 shell ` proj$ gulp [10:34:20] Using gulpfile ~/src/proj/gulpfile.js [10:34:20] Starting 'copy-html' ... [10:34:20] Finished 'copy-html' after 26 ms [10:34:20] Starting 'default' ... [10:34:21] 2824 bytes written (0.13 seconds) [10:34:21] Finished 'default' after 1.36 s [10:35:22] 2261 bytes written (0.02 seconds) [10:35:24] 2808 bytes written (0.05 seconds) `

### Terser

 First install Terser.
Since the point of Terser is to mangle your code, we also need to install vinyl-buffer and gulp-sourcemaps to keep sourcemaps working.

 shell ` npm install --save-dev gulp-terser vinyl-buffer gulp-sourcemaps `
 Now change your gulpfile to the following:

 js ` var gulp = require ( "gulp" ); var browserify = require ( "browserify" ); var source = require ( "vinyl-source-stream" ); var terser = require ( "gulp-terser" ); var tsify = require ( "tsify" ); var sourcemaps = require ( "gulp-sourcemaps" ); var buffer = require ( "vinyl-buffer" ); var paths = { pages: [ "src/*.html" ], }; gulp . task ( "copy-html" , function () { return gulp . src ( paths . pages ). pipe ( gulp . dest ( "dist" )); }); gulp . task ( "default" , gulp . series ( gulp . parallel ( "copy-html" ), function () { return browserify ({ basedir: "." , debug: true , entries: [ "src/main.ts" ], cache: {}, packageCache: {}, }) . plugin ( tsify ) . bundle () . pipe ( source ( "bundle.js" )) . pipe ( buffer ()) . pipe ( sourcemaps . init ({ loadMaps: true })) . pipe ( terser ()) . pipe ( sourcemaps . write ( "./" )) . pipe ( gulp . dest ( "dist" )); }) ); `
 Notice that `terser` itself has just one call — the calls to `buffer` and `sourcemaps` exist to make sure sourcemaps keep working.
These calls give us a separate sourcemap file instead of using inline sourcemaps like before.
Now you can run Gulp and check that `bundle.js` does get minified into an unreadable mess:

 shell ` gulp cat dist/bundle.js `

### Babel

 First install Babelify and the Babel preset for ES2015.
Like Terser, Babelify mangles code, so we’ll need vinyl-buffer and gulp-sourcemaps.
By default Babelify will only process files with extensions of `.js`, `.es`, `.es6` and `.jsx` so we need to add the `.ts` extension as an option to Babelify.

 shell ` npm install --save-dev babelify@8 babel-core babel-preset-es2015 vinyl-buffer gulp-sourcemaps `
 Now change your gulpfile to the following:

 js ` var gulp = require ( "gulp" ); var browserify = require ( "browserify" ); var source = require ( "vinyl-source-stream" ); var tsify = require ( "tsify" ); var sourcemaps = require ( "gulp-sourcemaps" ); var buffer = require ( "vinyl-buffer" ); var paths = { pages: [ "src/*.html" ], }; gulp . task ( "copy-html" , function () { return gulp . src ( paths . pages ). pipe ( gulp . dest ( "dist" )); }); gulp . task ( "default" , gulp . series ( gulp . parallel ( "copy-html" ), function () { return browserify ({ basedir: "." , debug: true , entries: [ "src/main.ts" ], cache: {}, packageCache: {}, }) . plugin ( tsify ) . transform ( "babelify" , { presets: [ "es2015" ], extensions: [ ".ts" ], }) . bundle () . pipe ( source ( "bundle.js" )) . pipe ( buffer ()) . pipe ( sourcemaps . init ({ loadMaps: true })) . pipe ( sourcemaps . write ( "./" )) . pipe ( gulp . dest ( "dist" )); }) ); `
 We also need to have TypeScript target ES2015.
Babel will then produce ES5 from the ES2015 code that TypeScript emits.
Let’s modify `tsconfig.json`:

 ` { " files " : [ "src/main.ts" ], " compilerOptions " : { " noImplicitAny " : true , " target " : "es2015" } } `
 Babel’s ES5 output should be very similar to TypeScript’s output for such a simple script.
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: BK OT DR RC MF 19+ Last updated: Jun 15, 2026

## Dom Manipulation

Was this page helpful?

# DOM Manipulation

## DOM Manipulation

### An exploration into the `HTMLElement` type

 In the 20+ years since its standardization, JavaScript has come a very long way. While in 2020, JavaScript can be used on servers, in data science, and even on IoT devices, it is important to remember its most popular use case: web browsers.

Websites are made up of HTML and/or XML documents. These documents are static, they do not change. The Document Object Model (DOM) is a programming interface implemented by browsers to make static websites functional. The DOM API can be used to change the document structure, style, and content. The API is so powerful that countless frontend frameworks (jQuery, React, Angular, etc.) have been developed around it to make dynamic websites even easier to develop.

TypeScript is a typed superset of JavaScript, and it ships type definitions for the DOM API. These definitions are readily available in any default TypeScript project. Of the 20,000+ lines of definitions in lib.dom.d.ts , one stands out among the rest: `HTMLElement`. This type is the backbone for DOM manipulation with TypeScript.

You can explore the source code for the DOM type definitions

## Basic Example

 Given a simplified index.html file:

 html ` <!DOCTYPE html > <html lang = "en" > <head><title> TypeScript Dom Manipulation </title></head> <body> <div id = "app" ></div> <!-- Assume index.js is the compiled output of index.ts --> <script src = "index.js" ></script> </body> </html> `
 Let’s explore a TypeScript script that adds a `&#x3C;p>Hello, World!&#x3C;/p>` element to the `#app` element.

 ts ` // 1. Select the div element using the id property const app = document . getElementById ( "app" ); // 2. Create a new <p></p> element programmatically const p = document . createElement ( "p" ); // 3. Add the text content p . textContent = "Hello, World!" ; // 4. Append the p element to the div element app ?. appendChild ( p ); `
 After compiling and running the index.html page, the resulting HTML will be:

 html ` <div id = "app" > <p> Hello, World! </p> </div> `

## The `Document` Interface

 The first line of the TypeScript code uses a global variable `document`. Inspecting the variable shows it is defined by the `Document` interface from the lib.dom.d.ts file. The code snippet contains calls to two methods, `getElementById` and `createElement`.

### `Document.getElementById`

 The definition for this method is as follows:

 ts ` getElementById ( elementId : string ): HTMLElement | null ; `
 Pass it an element id string and it will return either `HTMLElement` or `null`. This method introduces one of the most important types, `HTMLElement`. It serves as the base interface for every other element interface. For example, the `p` variable in the code example is of type `HTMLParagraphElement`. Also, take note that this method can return `null`. This is because the method can’t be certain pre-runtime if it will be able to actually find the specified element or not. In the last line of the code snippet, the new optional chaining operator is used to call `appendChild`.

### `Document.createElement`

 The definition for this method is (I have omitted the deprecated definition):

 ts ` createElement < K extends keyof HTMLElementTagNameMap >( tagName : K , options ?: ElementCreationOptions ): HTMLElementTagNameMap [ K ]; createElement ( tagName : string , options ?: ElementCreationOptions ): HTMLElement ; `
 This is an overloaded function definition. The second overload is simplest and works a lot like the `getElementById` method does. Pass it any `string` and it will return a standard HTMLElement. This definition is what enables developers to create unique HTML element tags.

For example `document.createElement('xyz')` returns a `&#x3C;xyz>&#x3C;/xyz>` element, clearly not an element that is specified by the HTML specification.

For those interested, you can interact with custom tag elements using the `document.getElementsByTagName`

For the first definition of `createElement`, it is using some advanced generic patterns. It is best understood broken down into chunks, starting with the generic expression: `&#x3C;K extends keyof HTMLElementTagNameMap>`. This expression defines a generic parameter `K` that is constrained to the keys of the interface `HTMLElementTagNameMap`. The map interface contains every specified HTML tag name and its corresponding type interface. For example here are the first 5 mapped values:

 ts ` interface HTMLElementTagNameMap { "a" : HTMLAnchorElement ; "abbr" : HTMLElement ; "address" : HTMLElement ; "applet" : HTMLAppletElement ; "area" : HTMLAreaElement ; ... } `
 Some elements do not exhibit unique properties and so they just return `HTMLElement`, but other types do have unique properties and methods so they return their specific interface (which will extend from or implement `HTMLElement`).

Now, for the remainder of the `createElement` definition: `(tagName: K, options?: ElementCreationOptions): HTMLElementTagNameMap[K]`. The first argument `tagName` is defined as the generic parameter `K`. The TypeScript interpreter is smart enough to infer the generic parameter from this argument. This means that the developer does not have to specify the generic parameter when using the method; whatever value is passed to the `tagName` argument will be inferred as `K` and thus can be used throughout the remainder of the definition. This is exactly what happens; the return value `HTMLElementTagNameMap[K]` takes the `tagName` argument and uses it to return the corresponding type. This definition is how the `p` variable from the code snippet gets a type of `HTMLParagraphElement`. And if the code was `document.createElement('a')`, then it would be an element of type `HTMLAnchorElement`.

## The `Node` interface

 The `document.getElementById` function returns an `HTMLElement`. `HTMLElement` interface extends the `Element` interface which extends the `Node` interface. This prototypal extension allows for all `HTMLElements` to utilize a subset of standard methods. In the code snippet, we use a property defined on the `Node` interface to append the new `p` element to the website.

### `Node.appendChild`

 The last line of the code snippet is `app?.appendChild(p)`. The previous, `document.getElementById`, section detailed that the optional chaining operator is used here because `app` can potentially be null at runtime. The `appendChild` method is defined by:

 ts ` appendChild < T extends Node >( newChild : T ): T ; `
 This method works similarly to the `createElement` method as the generic parameter `T` is inferred from the `newChild` argument. `T` is constrained to another base interface `Node`.

## Difference between `children` and `childNodes`

 Previously, this document details the `HTMLElement` interface extends from `Element` which extends from `Node`. In the DOM API there is a concept of children elements. For example in the following HTML, the `p` tags are children of the `div` element

 tsx ` <div> <p> Hello, World </p> <p> TypeScript! </p> </div> ; const div = document . getElementsByTagName ( "div" )[ 0 ]; div . children ; // HTMLCollection(2) [p, p] div . childNodes ; // NodeList(2) [p, p] `
 After capturing the `div` element, the `children` prop will return an `HTMLCollection` list containing the `HTMLParagraphElements`. The `childNodes` property will return a similar `NodeList` list of nodes. Each `p` tag will still be of type `HTMLParagraphElements`, but the `NodeList` can contain additional HTML nodes that the `HTMLCollection` list cannot.

Modify the HTML by removing one of the `p` tags, but keep the text.

 tsx ` <div> <p> Hello, World </p> TypeScript! </div> ; const div = document . getElementsByTagName ( "div" )[ 0 ]; div . children ; // HTMLCollection(1) [p] div . childNodes ; // NodeList(2) [p, text] `
 See how both lists change. `children` now only contains the `&#x3C;p>Hello, World&#x3C;/p>` element, and the `childNodes` contains a `text` node rather than two `p` nodes. The `text` part of the `NodeList` is the literal `Node` containing the text `TypeScript!`. The `children` list does not contain this `Node` because it is not considered an `HTMLElement`.

## The `querySelector` and `querySelectorAll` methods

 Both of these methods are great tools for getting lists of dom elements that fit a more unique set of constraints. They are defined in lib.dom.d.ts as:

 ts ` /** * Returns the first element that is a descendant of node that matches selectors. */ querySelector < K extends keyof HTMLElementTagNameMap >( selectors : K ): HTMLElementTagNameMap [ K ] | null ; querySelector < K extends keyof SVGElementTagNameMap >( selectors : K ): SVGElementTagNameMap [ K ] | null ; querySelector < E extends Element = Element >( selectors : string ): E | null ; /** * Returns all element descendants of node that match selectors. */ querySelectorAll < K extends keyof HTMLElementTagNameMap >( selectors : K ): NodeListOf < HTMLElementTagNameMap [ K ]>; querySelectorAll < K extends keyof SVGElementTagNameMap >( selectors : K ): NodeListOf < SVGElementTagNameMap [ K ]>; querySelectorAll < E extends Element = Element >( selectors : string ): NodeListOf < E >; `
 The `querySelectorAll` definition is similar to `getElementsByTagName`, except it returns a new type: `NodeListOf`. This return type is essentially a custom implementation of the standard JavaScript list element. Arguably, replacing `NodeListOf&#x3C;E>` with `E[]` would result in a very similar user experience. `NodeListOf` only implements the following properties and methods: `length`, `item(index)`, `forEach((value, key, parent) => void)`, and numeric indexing. Additionally, this method returns a list of elements , not nodes , which is what `NodeList` was returning from the `.childNodes` method. While this may appear as a discrepancy, take note that interface `Element` extends from `Node`.

To see these methods in action modify the existing code to:

 tsx ` <ul> <li> First :) </li> <li> Second! </li> <li> Third times a charm. </li> </ul> ; const first = document . querySelector ( "li" ); // returns the first li element const all = document . querySelectorAll ( "li" ); // returns the list of all li elements `

## Interested in learning more?

 The best part about the lib.dom.d.ts type definitions is that they are reflective of the types annotated in the Mozilla Developer Network (MDN) documentation site. For example, the `HTMLElement` interface is documented by this HTMLElement page on MDN. These pages list all available properties, methods, and sometimes even examples. Another great aspect of the pages is that they provide links to the corresponding standard documents. Here is the link to the W3C Recommendation for HTMLElement .

Sources:

- ECMA-262 Standard

- Introduction to the DOM

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: EA OT SA M IO 6+ Last updated: Jun 15, 2026

## Migrating From Javascript

Was this page helpful?

# Migrating from JavaScript
 TypeScript doesn’t exist in a vacuum.
It was built with the JavaScript ecosystem in mind, and a lot of JavaScript exists today.
Converting a JavaScript codebase over to TypeScript is, while somewhat tedious, usually not challenging.
In this tutorial, we’re going to look at how you might start out.
We assume you’ve read enough of the handbook to write new TypeScript code.

If you’re looking to convert a React project, we recommend looking at the React Conversion Guide first.

## Setting up your Directories

 If you’re writing in plain JavaScript, it’s likely that you’re running your JavaScript directly,
where your `.js` files are in a `src`, `lib`, or `dist` directory, and then run as desired.

If that’s the case, the files that you’ve written are going to be used as inputs to TypeScript, and you’ll run the outputs it produces.
During our JS to TS migration, we’ll need to separate our input files to prevent TypeScript from overwriting them.
If your output files need to reside in a specific directory, then that will be your output directory.

You might also be running some intermediate steps on your JavaScript, such as bundling or using another transpiler like Babel.
In this case, you might already have a folder structure like this set up.

From this point on, we’re going to assume that your directory is set up something like this:

 ` projectRoot ├── src │ ├── file1.js │ └── file2.js ├── built └── tsconfig.json `
 If you have a `tests` folder outside of your `src` directory, you might have one `tsconfig.json` in `src`, and one in `tests` as well.

## Writing a Configuration File

 TypeScript uses a file called `tsconfig.json` for managing your project’s options, such as which files you want to include, and what sorts of checking you want to perform.
Let’s create a bare-bones one for our project:

 json ` { "compilerOptions" : { "outDir" : "./built" , "allowJs" : true , "target" : "es5" }, "include" : [ "./src/**/*" ] } `
 Here we’re specifying a few things to TypeScript:

- Read in any files it understands in the `src` directory (with `include` ).

- Accept JavaScript files as inputs (with `allowJs` ).

- Emit all of the output files in `built` (with `outDir` ).

- Translate newer JavaScript constructs down to an older version like ECMAScript 5 (using `target` ).

At this point, if you try running `tsc` at the root of your project, you should see output files in the `built` directory.
The layout of files in `built` should look identical to the layout of `src`.
You should now have TypeScript working with your project.

## Early Benefits

 Even at this point you can get some great benefits from TypeScript understanding your project.
If you open up an editor like VS Code or Visual Studio , you’ll see that you can often get some tooling support like completion.
You can also catch certain bugs with options like:

- `noImplicitReturns` which prevents you from forgetting to return at the end of a function.

- `noFallthroughCasesInSwitch` which is helpful if you never want to forget a `break` statement between `case`s in a `switch` block.

TypeScript will also warn about unreachable code and labels, which you can disable with `allowUnreachableCode` and `allowUnusedLabels` respectively.

## Integrating with Build Tools

 You might have some more build steps in your pipeline.
Perhaps you concatenate something to each of your files.
Each build tool is different, but we’ll do our best to cover the gist of things.

### Gulp

 If you’re using Gulp in some fashion, we have a tutorial on using Gulp with TypeScript, and integrating with common build tools like Browserify, Babelify, and Uglify.
You can read more there.

### Webpack

 Webpack integration is pretty simple.
You can use `ts-loader`, a TypeScript loader, combined with `source-map-loader` for easier debugging.
Simply run

 shell ` npm install ts-loader source-map-loader `
 and merge in options from the following into your `webpack.config.js` file:

 js ` module . exports = { entry: "./src/index.ts" , output: { filename: "./dist/bundle.js" , }, // Enable sourcemaps for debugging webpack's output. devtool: "source-map" , resolve: { // Add '.ts' and '.tsx' as resolvable extensions. extensions: [ "" , ".webpack.js" , ".web.js" , ".ts" , ".tsx" , ".js" ], }, module: { rules: [ // All files with a '.ts' or '.tsx' extension will be handled by 'ts-loader'. { test: / \. tsx ? $ / , loader: "ts-loader" }, // All output '.js' files will have any sourcemaps re-processed by 'source-map-loader'. { test: / \. js $ / , loader: "source-map-loader" }, ], }, // Other options... }; `
 It’s important to note that ts-loader will need to run before any other loader that deals with `.js` files.

You can see an example of using Webpack in our tutorial on React and Webpack .

## Moving to TypeScript Files

 At this point, you’re probably ready to start using TypeScript files.
The first step is to rename one of your `.js` files to `.ts`.
If your file uses JSX, you’ll need to rename it to `.tsx`.

Finished with that step?
Great!
You’ve successfully migrated a file from JavaScript to TypeScript!

Of course, that might not feel right.
If you open that file in an editor with TypeScript support (or if you run `tsc --pretty`), you might see red squiggles on certain lines.
You should think of these the same way you’d think of red squiggles in an editor like Microsoft Word.
TypeScript will still translate your code, just like Word will still let you print your documents.

If that sounds too lax for you, you can tighten that behavior up.
If, for instance, you don’t want TypeScript to compile to JavaScript in the face of errors, you can use the `noEmitOnError` option.
In that sense, TypeScript has a dial on its strictness, and you can turn that knob up as high as you want.

If you plan on using the stricter settings that are available, it’s best to turn them on now (see Getting Stricter Checks below).
For instance, if you never want TypeScript to silently infer `any` for a type without you explicitly saying so, you can use `noImplicitAny` before you start modifying your files.
While it might feel somewhat overwhelming, the long-term gains become apparent much more quickly.

### Weeding out Errors

 Like we mentioned, it’s not unexpected to get error messages after conversion.
The important thing is to actually go one by one through these and decide how to deal with the errors.
Often these will be legitimate bugs, but sometimes you’ll have to explain what you’re trying to do a little better to TypeScript.

#### Importing from Modules

 You might start out getting a bunch of errors like `Cannot find name 'require'.`, and `Cannot find name 'define'.`.
In these cases, it’s likely that you’re using modules.
While you can just convince TypeScript that these exist by writing out

 ts ` // For Node/CommonJS declare function require ( path : string ): any ; `
 or

 ts ` // For RequireJS/AMD declare function define (... args : any []): any ; `
 it’s better to get rid of those calls and use TypeScript syntax for imports.

First, you’ll need to enable some module system by setting TypeScript’s `module` option.
Valid options are `commonjs`, `amd`, `system`, and `umd`.

If you had the following Node/CommonJS code:

 js ` var foo = require ( "foo" ); foo . doStuff (); `
 or the following RequireJS/AMD code:

 js ` define ([ "foo" ], function ( foo ) { foo . doStuff (); }); `
 then you would write the following TypeScript code:

 ts ` import foo = require ( "foo" ); foo . doStuff (); `

#### Getting Declaration Files

 If you started converting over to TypeScript imports, you’ll probably run into errors like `Cannot find module 'foo'.`.
The issue here is that you likely don’t have declaration files to describe your library.
Luckily this is pretty easy.
If TypeScript complains about a package like `lodash`, you can just write

 shell ` npm install -S @types/lodash `
 If you’re using a module option other than `commonjs`, you’ll need to set your `moduleResolution` option to `node`.

After that, you’ll be able to import lodash with no issues, and get accurate completions.

#### Exporting from Modules

 Typically, exporting from a module involves adding properties to a value like `exports` or `module.exports`.
TypeScript allows you to use top-level export statements.
For instance, if you exported a function like so:

 js ` module . exports . feedPets = function ( pets ) { // ... }; `
 you could write that out as the following:

 ts ` export function feedPets ( pets ) { // ... } `
 Sometimes you’ll entirely overwrite the exports object.
This is a common pattern people use to make their modules immediately callable like in this snippet:

 js ` var express = require ( "express" ); var app = express (); `
 You might have previously written that like so:

 js ` function foo () { // ... } module . exports = foo ; `
 In TypeScript, you can model this with the `export =` construct.

 ts ` function foo () { // ... } export = foo ; `

#### Too many/too few arguments

 You’ll sometimes find yourself calling a function with too many/few arguments.
Typically, this is a bug, but in some cases, you might have declared a function that uses the `arguments` object instead of writing out any parameters:

 js ` function myCoolFunction () { if ( arguments . length == 2 && ! Array . isArray ( arguments [ 1 ])) { var f = arguments [ 0 ]; var arr = arguments [ 1 ]; // ... } // ... } myCoolFunction ( function ( x ) { console . log ( x ); }, [ 1 , 2 , 3 , 4 ] ); myCoolFunction ( function ( x ) { console . log ( x ); }, 1 , 2 , 3 , 4 ); `
 In this case, we need to use TypeScript to tell any of our callers about the ways `myCoolFunction` can be called using function overloads.

 ts ` function myCoolFunction ( f : ( x : number ) => void , nums : number []): void ; function myCoolFunction ( f : ( x : number ) => void , ... nums : number []): void ; function myCoolFunction () { if ( arguments . length == 2 && ! Array . isArray ( arguments [ 1 ])) { var f = arguments [ 0 ]; var arr = arguments [ 1 ]; // ... } // ... } `
 We added two overload signatures to `myCoolFunction`.
The first checks states that `myCoolFunction` takes a function (which takes a `number`), and then a list of `number`s.
The second one says that it will take a function as well, and then uses a rest parameter (`...nums`) to state that any number of arguments after that need to be `number`s.

#### Sequentially Added Properties

 Some people find it more aesthetically pleasing to create an object and add properties immediately after like so:

 js ` var options = {}; options . color = "red" ; options . volume = 11 ; `
 TypeScript will say that you can’t assign to `color` and `volume` because it first figured out the type of `options` as `{}` which doesn’t have any properties.
If you instead moved the declarations into the object literal themselves, you’d get no errors:

 ts ` let options = { color: "red" , volume: 11 , }; `
 You could also define the type of `options` and add a type assertion on the object literal.

 ts ` interface Options { color : string ; volume : number ; } let options = {} as Options ; options . color = "red" ; options . volume = 11 ; `
 Alternatively, you can just say `options` has the type `any` which is the easiest thing to do, but which will benefit you the least.

#### `any`, `Object`, and `{}`

 You might be tempted to use `Object` or `{}` to say that a value can have any property on it because `Object` is, for most purposes, the most general type.
However `any` is actually the type you want to use in those situations, since it’s the most flexible type.

For instance, if you have something that’s typed as `Object` you won’t be able to call methods like `toLowerCase()` on it.
Being more general usually means you can do less with a type, but `any` is special in that it is the most general type while still allowing you to do anything with it.
That means you can call it, construct it, access properties on it, etc.
Keep in mind though, whenever you use `any`, you lose out on most of the error checking and editor support that TypeScript gives you.

If a decision ever comes down to `Object` and `{}`, you should prefer `{}`.
While they are mostly the same, technically `{}` is a more general type than `Object` in certain esoteric cases.

### Getting Stricter Checks

 TypeScript comes with certain checks to give you more safety and analysis of your program.
Once you’ve converted your codebase to TypeScript, you can start enabling these checks for greater safety.

#### No Implicit `any`

 There are certain cases where TypeScript can’t figure out what certain types should be.
To be as lenient as possible, it will decide to use the type `any` in its place.
While this is great for migration, using `any` means that you’re not getting any type safety, and you won’t get the same tooling support you’d get elsewhere.
You can tell TypeScript to flag these locations down and give an error with the `noImplicitAny` option.

#### Strict `null` &#x26; `undefined` Checks

 By default, TypeScript assumes that `null` and `undefined` are in the domain of every type.
That means anything declared with the type `number` could be `null` or `undefined`.
Since `null` and `undefined` are such a frequent source of bugs in JavaScript and TypeScript, TypeScript has the `strictNullChecks` option to spare you the stress of worrying about these issues.

When `strictNullChecks` is enabled, `null` and `undefined` get their own types called `null` and `undefined` respectively.
Whenever anything is possibly `null`, you can use a union type with the original type.
So for instance, if something could be a `number` or `null`, you’d write the type out as `number | null`.

If you ever have a value that TypeScript thinks is possibly `null`/`undefined`, but you know better, you can use the postfix `!` operator to tell it otherwise.

 ts ` declare var foo : string [] | null ; foo . length ; // error - 'foo' is possibly 'null' foo !. length ; // okay - 'foo!' just has type 'string[]' `
 As a heads up, when using `strictNullChecks` , your dependencies may need to be updated to use `strictNullChecks` as well.

#### No Implicit `any` for `this`

 When you use the `this` keyword outside of classes, it has the type `any` by default.
For instance, imagine a `Point` class, and imagine a function that we wish to add as a method:

 ts ` class Point { constructor ( public x , public y ) {} getDistance ( p : Point ) { let dx = p . x - this . x ; let dy = p . y - this . y ; return Math . sqrt ( dx ** 2 + dy ** 2 ); } } // ... // Reopen the interface. interface Point { distanceFromOrigin (): number ; } Point . prototype . distanceFromOrigin = function () { return this . getDistance ({ x: 0 , y: 0 }); }; `
 This has the same problems we mentioned above - we could easily have misspelled `getDistance` and not gotten an error.
For this reason, TypeScript has the `noImplicitThis` option.
When that option is set, TypeScript will issue an error when `this` is used without an explicit (or inferred) type.
The fix is to use a `this`-parameter to give an explicit type in the interface or in the function itself:

 ts ` Point . prototype . distanceFromOrigin = function ( this : Point ) { return this . getDistance ({ x: 0 , y: 0 }); }; ` The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: DR OT TA MG MF 19+ Last updated: Jun 15, 2026

## Babel With Typescript

Was this page helpful?

# Using Babel with TypeScript

## Babel vs `tsc` for TypeScript

 When making a modern JavaScript project, you might ask yourself what is the right way to convert files from TypeScript to JavaScript?

A lot of the time the answer is “it depends” , or “someone may have decided for you” depending on the project. If you are building your project with an existing framework like tsdx , Angular , NestJS or any framework mentioned in the Getting Started then this decision is handled for you.

However, a useful heuristic could be:

- Is your build output mostly the same as your source input files? Use `tsc`

- Do you need a build pipeline with multiple potential outputs? Use `babel` for transpiling and `tsc` for type checking

## Babel for transpiling, `tsc` for types

 This is a common pattern for projects with existing build infrastructure which may have been ported from a JavaScript codebase to TypeScript.

This technique is a hybrid approach, using Babel’s preset-typescript to generate your JS files, and then using TypeScript to do type checking and `.d.ts` file generation.

By using babel’s support for TypeScript, you get the ability to work with existing build pipelines and are more likely to have a faster JS emit time because Babel does not type check your code.

#### Type Checking and d.ts file generation

 The downside to using babel is that you don’t get type checking during the transition from TS to JS. This can mean that type errors which you miss in your editor could sneak through into production code.

In addition to that, Babel cannot create `.d.ts` files for your TypeScript which can make it harder to work with your project if it is a library.

To fix these issues, you would probably want to set up a command to type check your project using TSC. This likely means duplicating some of your babel config into a corresponding `tsconfig.json` and ensuring these flags are enabled:

 ` "compilerOptions" : { // Ensure that .d.ts files are created by tsc, but not .js files " declaration " : true , " emitDeclarationOnly " : true , // Ensure that Babel can safely transpile files in the TypeScript project " isolatedModules " : true } `
 For more information on these flags:

- `isolatedModules`

- `declaration` , `emitDeclarationOnly`

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: OT SU R US Last updated: Jun 15, 2026