# TypeScript - Modules Reference


## Introduction

Was this page helpful?

# Modules - Introduction
 This document is divided into four sections:

- The first section develops the theory behind how TypeScript approaches modules. If you want to be able to write the correct module-related compiler options for any situation, reason about how to integrate TypeScript with other tools, or understand how TypeScript processes dependency packages, this is the place to start. While there are guides and reference pages on these topics, building an understanding of these fundamentals will make reading the guides easier, and give you a mental framework for dealing with real-world problems not specifically covered here.

- The guides show how to accomplish specific real-world tasks, starting with picking the right compilation settings for a new project. The guides are a good place to start both for beginners who want to get up and running as quickly as possible and for experts who already have a good grasp of the theory but want concrete guidance on a complicated task.

- The reference section provides a more detailed look at the syntaxes and configurations presented in previous sections.

- The appendices cover complicated topics that deserve additional explanation in more detail than the theory or reference sections allow.

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: AB Last updated: Jun 15, 2026

## Theory

Was this page helpful?

# Modules - Theory

## Scripts and modules in JavaScript

 In the early days of JavaScript, when the language only ran in browsers, there were no modules, but it was still possible to split the JavaScript for a web page into multiple files by using multiple `script` tags in HTML:

 html ` <html> <head> <script src = "a.js" ></script> <script src = "b.js" ></script> </head> <body></body> </html> `
 This approach had some downsides, especially as web pages grew larger and more complex. In particular, all scripts loaded onto the same page share the same scope—appropriately called the “global scope”—meaning the scripts had to be very careful not to overwrite each others’ variables and functions.

Any system that solves this problem by giving files their own scope while still providing a way to make bits of code available to other files can be called a “module system.” (It may sound obvious to say that each file in a module system is called a “module,” but the term is often used to contrast with script files, which run outside a module system, in a global scope.)

There are many module systems , and TypeScript supports emitting several , but this documentation will focus on the two most important systems today: ECMAScript modules (ESM) and CommonJS (CJS).

ECMAScript Modules (ESM) is the module system built into the language, supported in modern browsers and in Node.js since v12. It uses dedicated `import` and `export` syntax:

 js ` // a.js export default "Hello from a.js" ; `

```
 js ` // b.js import a from "./a.js" ; console . log ( a ); // 'Hello from a.js' `
```

 CommonJS (CJS) is the module system that originally shipped in Node.js, before ESM was part of the language specification. It’s still supported in Node.js alongside ESM. It uses plain JavaScript objects and functions named `exports` and `require`:

 js ` // a.js exports . message = "Hello from a.js" ; `

```
 js ` // b.js const a = require ( "./a" ); console . log ( a . message ); // 'Hello from a.js' `
```

 Accordingly, when TypeScript detects that a file is a CommonJS or ECMAScript module, it starts by assuming that file will have its own scope. Beyond that, though, the compiler’s job gets a little more complicated.

## TypeScript’s job concerning modules

 The TypeScript compiler’s chief goal is to prevent certain kinds of runtime errors by catching them at compile time. With or without modules involved, the compiler needs to know about the code’s intended runtime environment—what globals are available, for example. When modules are involved, there are several additional questions the compiler needs to answer in order to do its job. Let’s use a few lines of input code as an example to think about all the information needed to analyze it:

 ts ` import sayHello from "greetings" ; sayHello ( "world" ); `
 To check this file, the compiler needs to know the type of `sayHello` (is it a function that can accept one string argument?), which opens quite a few additional questions:

- Will the module system load this TypeScript file directly, or will it load a JavaScript file that I (or another compiler) generate from this TypeScript file?

- What kind of module does the module system expect to find, given the file name it will load and its location on disk?

- If output JavaScript is being emitted, how will the module syntax present in this file be transformed in the output code?

- Where will the module system look to find the module specified by `"greetings"`? Will the lookup succeed?

- What kind of module is the file resolved by that lookup?

- Does the module system allow the kind of module detected in (2) to reference the kind of module detected in (5) with the syntax decided in (3)?

- Once the `"greetings"` module has been analyzed, what piece of that module is bound to `sayHello`?

Notice that all of these questions depend on characteristics of the host —the system that ultimately consumes the output JavaScript (or raw TypeScript, as the case may be) to direct its module loading behavior, typically either a runtime (like Node.js) or bundler (like Webpack).

The ECMAScript specification defines how ESM imports and exports link up with each other, but it doesn’t specify how the file lookup in (4), known as module resolution , happens, and it doesn’t say anything about other module systems like CommonJS. So runtimes and bundlers, especially those that want to support both ESM and CJS, have a lot of freedom to design their own rules. Consequently, the way TypeScript should answer the questions above can vary dramatically depending on where the code is intended to run. There’s no single right answer, so the compiler must be told the rules through configuration options.

The other key idea to keep in mind is that TypeScript almost always thinks about these questions in terms of its output JavaScript files, not its input TypeScript (or JavaScript!) files. Today, some runtimes and bundlers support loading TypeScript files directly, and in those cases, it doesn’t make sense to think about separate input and output files. Most of this document discusses cases where TypeScript files are compiled to JavaScript files, which in turn are loaded by the runtime module system. Examining these cases is essential for building an understanding of the compiler’s options and behavior—it’s easier to start there and simplify when thinking about esbuild, Bun, and other TypeScript-first runtimes and bundlers . So for now, we can summarize TypeScript’s job when it comes to modules in terms of output files:

Understand the rules of the host enough

- to compile files into a valid output module format ,

- to ensure that imports in those outputs will resolve successfully , and

- to know what type to assign to imported names .

## Who is the host?

 Before we move on, it’s worth making sure we’re on the same page about the term host , because it will come up frequently. We defined it before as “the system that ultimately consumes the output code to direct its module loading behavior.” In other words, it’s the system outside of TypeScript that TypeScript’s module analysis tries to model:

- When the output code (whether produced by `tsc` or a third-party transpiler) is run directly in a runtime like Node.js, the runtime is the host.

- When there is no “output code” because a runtime consumes TypeScript files directly, the runtime is still the host.

- When a bundler consumes TypeScript inputs or outputs and produces a bundle, the bundler is the host, because it looked at the original set of imports/requires, looked up what files they referenced, and produced a new file or set of files where the original imports and requires are erased or transformed beyond recognition. (That bundle itself might comprise modules, and the runtime that runs it will be its host, but TypeScript doesn’t know about anything that happens post-bundler.)

- If another transpiler, optimizer, or formatter runs on TypeScript’s outputs, it’s not a host that TypeScript cares about, as long as it leaves the imports and exports it sees alone.

- When loading modules in a web browser, the behaviors TypeScript needs to model are actually split between the web server and the module system running in the browser. The browser’s JavaScript engine (or a script-based module-loading framework like RequireJS) controls what module formats are accepted, while the web server decides what file to send when one module triggers a request to load another.

- The TypeScript compiler itself is not a host, because it does not provide any behavior related to modules beyond trying to model other hosts.

## The module output format

 In any project, the first question about modules we need to answer is what kinds of modules the host expects, so TypeScript can set its output format for each file to match. Sometimes, the host only supports one kind of module—ESM in the browser, or CJS in Node.js v11 and earlier, for example. Node.js v12 and later accepts both CJS and ES modules, but uses file extensions and `package.json` files to determine what format each file should be, and throws an error if the file’s contents don’t match the expected format.

The `module` compiler option provides this information to the compiler. Its primary purpose is to control the module format of any JavaScript that gets emitted during compilation, but it also serves to inform the compiler about how the module kind of each file should be detected, how different module kinds are allowed to import each other, and whether features like `import.meta` and top-level `await` are available. So, even if a TypeScript project is using `noEmit`, choosing the right setting for `module` still matters. As we established earlier, the compiler needs an accurate understanding of the module system so it can type check (and provide IntelliSense for) imports. See Choosing compiler options for guidance on choosing the right `module` setting for your project.

The available `module` settings are

- `node16` : Reflects the module system of Node.js v16+, which supports ES modules and CJS modules side-by-side with particular interoperability and detection rules.

- `node18` : Reflects the module system of Node.js v18+, which adds support for import attributes.

- `nodenext` : A moving target reflecting the latest Node.js versions as Node.js’s module system evolves. As of TypeScript 5.8, `nodenext` supports `require` of ECMAScript modules.

- `es2015` : Reflects the ES2015 language specification for JavaScript modules (the version that first introduced `import` and `export` to the language).

- `es2020` : Adds support for `import.meta` and `export * as ns from "mod"` to `es2015`.

- `es2022` : Adds support for top-level `await` to `es2020`.

- `esnext` : Currently identical to `es2022`, but will be a moving target reflecting the latest ECMAScript specifications, as well as module-related Stage 3+ proposals that are expected to be included in upcoming specification versions.

- `commonjs` , `system` , `amd` , and `umd` : Each emits everything in the module system named, and assumes everything can be successfully imported into that module system. These are no longer recommended for new projects and will not be covered in detail by this documentation.

Node.js’s rules for module format detection and interoperability make it incorrect to specify `module` as `esnext` or `commonjs` for projects that run in Node.js, even if all files emitted by `tsc` are ESM or CJS, respectively. The only correct `module` settings for projects that intend to run in Node.js are `node16` and `nodenext`. While the emitted JavaScript for an all-ESM Node.js project might look identical between compilations using `esnext` and `nodenext`, the type checking can differ. See the reference section on `nodenext` for more details.

### Module format detection

 Node.js understands both ES modules and CJS modules, but the format of each file is determined by its file extension and the `type` field of the first `package.json` file found in a search of the file’s directory and all ancestor directories:

- `.mjs` and `.cjs` files are always interpreted as ES modules and CJS modules, respectively.

- `.js` files are interpreted as ES modules if the nearest `package.json` file contains a `type` field with the value `"module"`. If there is no `package.json` file, or if the `type` field is missing or has any other value, `.js` files are interpreted as CJS modules.

If a file is determined to be an ES module by these rules, Node.js will not inject the CommonJS `module` and `require` objects into the file’s scope during evaluation, so a file that tries to use them will cause a crash. Conversely, if a file is determined to be a CJS module, `import` and `export` declarations in the file will cause a syntax error crash.

When the `module` compiler option is set to `node16`, `node18`, or `nodenext`, TypeScript applies this same algorithm to the project’s input files to determine the module kind of each corresponding output file. Let’s look at how module formats are detected in an example project that uses `--module nodenext`:

| **

 Input file name**
| **Contents**
| **Output file name**
| **Module kind**
| **Reason**
|

| `/package.json`
| `{}`
|
|
|
|

| `/main.mts`
|
| `/main.mjs`
| ESM
| File extension
|

| `/utils.cts`
|
| `/utils.cjs`
| CJS
| File extension
|

| `/example.ts`
|
| `/example.js`
| CJS
| No `"type": "module"` in `package.json`
|

| `/node_modules/pkg/package.json`
| `{ "type": "module" }`
|
|
|
|

| `/node_modules/pkg/index.d.ts`
|
|
| ESM
| `"type": "module"` in `package.json`
|

| `/node_modules/pkg/index.d.cts`
|
|
| CJS
| File extension
|

When the input file extension is `.mts` or `.cts`, TypeScript knows to treat that file as an ES module or CJS module, respectively, because Node.js will treat the output `.mjs` file as an ES module or the output `.cjs` file as a CJS module. When the input file extension is `.ts`, TypeScript has to consult the nearest `package.json` file to determine the module format, because this is what Node.js will do when it encounters the output `.js` file. (Notice that the same rules apply to the `.d.cts` and `.d.ts` declaration files in the `pkg` dependency: though they will not produce an output file as part of this compilation, the presence of a `.d.ts` file implies the existence of a corresponding `.js` file—perhaps created when the author of the `pkg` library ran `tsc` on an input `.ts` file of their own—which Node.js must interpret as an ES module, due to its `.js` extension and the presence of the `"type": "module"` field in `/node_modules/pkg/package.json`. Declaration files are covered in more detail in a later section .)

The detected module format of input files is used by TypeScript to ensure it emits the output syntax that Node.js expects in each output file. If TypeScript were to emit `/example.js` with `import` and `export` statements in it, Node.js would crash when parsing the file. If TypeScript were to emit `/main.mjs` with `require` calls, Node.js would crash during evaluation. Beyond emit, the module format is also used to determine rules for type checking and module resolution, which we’ll discuss in the following sections.

As of TypeScript 5.6, other `--module` modes (like `esnext` and `commonjs`) also respect format-specific file extensions (`.mts` and `.cts`) as a file-level override for the emit format. For example, a file named `main.mts` will emit ESM syntax into `main.mjs` even if `--module` is set to `commonjs`.

It’s worth mentioning again that TypeScript’s behavior in `--module node16`, `--module node18`, and `--module nodenext` is entirely motivated by Node.js’s behavior. Since TypeScript’s goal is to catch potential runtime errors at compile time, it needs a very accurate model of what will happen at runtime. This fairly complex set of rules for module kind detection is necessary for checking code that will run in Node.js, but may be overly strict or just incorrect if applied to non-Node.js hosts.

### Input module syntax

 It’s important to note that the input module syntax seen in input source files is somewhat decoupled from the output module syntax emitted to JS files. That is, a file with an ESM import:

 ts ` import { sayHello } from "greetings" ; sayHello ( "world" ); `
 might be emitted in ESM format exactly as-is, or might be emitted as CommonJS:

 ts ` Object . defineProperty ( exports , "__esModule" , { value: true }); const greetings_1 = require ( "greetings" ); ( 0 , greetings_1 . sayHello )( "world" ); `
 depending on the `module` compiler option (and any applicable module format detection rules, if the `module` option supports more than one kind of module). In general, this means that looking at the contents of an input file isn’t enough to determine whether it’s an ES module or a CJS module.

Today, most TypeScript files are authored using ESM syntax (`import` and `export` statements) regardless of the output format. This is largely a legacy of the long road ESM has taken to widespread support. ECMAScript modules were standardized in 2015, were supported in most browsers by 2017, and landed in Node.js v12 in 2019. During much of this window, it was clear that ESM was the future of JavaScript modules, but very few runtimes could consume it. Tools like Babel made it possible for JavaScript to be authored in ESM and downleveled to another module format that could be used in Node.js or browsers. TypeScript followed suit, adding support for ES module syntax and softly discouraging the use of the original CommonJS-inspired `import fs = require("fs")` syntax in the 1.5 release .

The upside of this “author ESM, output anything” strategy was that TypeScript could use standard JavaScript syntax, making the authoring experience familiar to newcomers, and (theoretically) making it easy for projects to start targeting ESM outputs in the future. There are three significant downsides, which became fully apparent only after ESM and CJS modules were allowed to coexist and interoperate in Node.js:

- Early assumptions about how ESM/CJS interoperability would work in Node.js turned out to be wrong, and today, interoperability rules differ between Node.js and bundlers. Consequently, the configuration space for modules in TypeScript is large.

- When the syntax in input files all looks like ESM, it’s easy for an author or code reviewer to lose track of what kind of module a file is at runtime. And because of Node.js’s interoperability rules, what kind of module each file is became very important.

- When input files are written in ESM, the syntax in type declaration outputs (`.d.ts` files) looks like ESM too. But because the corresponding JavaScript files could have been emitted in any module format, TypeScript can’t tell what kind of module a file is just by looking at the contents of its type declarations. And again, because of the nature of ESM/CJS interoperability, TypeScript has to know what kind of module everything is in order to provide correct types and prevent imports that will crash.

In TypeScript 5.0, a new compiler option called `verbatimModuleSyntax` was introduced to help TypeScript authors know exactly how their `import` and `export` statements will be emitted. When enabled, the flag requires imports and exports in input files to be written in the form that will undergo the least amount of transformation before emit. So if a file will be emitted as ESM, imports and exports must be written in ESM syntax; if a file will be emitted as CJS, it must be written in the CommonJS-inspired TypeScript syntax (`import fs = require("fs")` and `export = {}`). This setting is particularly recommended for Node.js projects that use mostly ESM, but have a select few CJS files. It is not recommended for projects that currently target CJS, but may want to target ESM in the future.

### ESM and CJS interoperability

 Can an ES module `import` a CommonJS module? If so, does a default import link to `exports` or `exports.default`? Can a CommonJS module `require` an ES module? CommonJS isn’t part of the ECMAScript specification, so runtimes, bundlers, and transpilers have been free to make up their own answers to these questions since ESM was standardized in 2015, and as such no standard set of interoperability rules exist. Today, most runtimes and bundlers broadly fall into one of three categories:

- ESM-only. Some runtimes, like browser engines, only support what’s actually a part of the language: ECMAScript Modules.

- Bundler-like. Before any major JavaScript engine could run ES modules, Babel allowed developers to write them by transpiling them to CommonJS. The way these ESM-transpiled-to-CJS files interacted with hand-written-CJS files implied a set of permissive interoperability rules that have become the de facto standard for bundlers and transpilers.

- Node.js. Until Node.js v20.19.0, CommonJS modules could not load ES modules synchronously (with `require`); they could only load them asynchronously with dynamic `import()` calls. ES modules can default-import CJS modules, which always binds to `exports`. (This means that a default import of a Babel-like CJS output with `__esModule` behaves differently between Node.js and some bundlers.)

TypeScript needs to know which of these rule sets to assume in order to provide correct types on (particularly `default`) imports and to error on imports that will crash at runtime. When the `module` compiler option is set to `node16`, `node18`, or `nodenext`, Node.js’s version-specific rules are enforced. 1 All other `module` settings, combined with the `esModuleInterop` option, result in bundler-like interop in TypeScript. (While using `--module esnext` does prevent you from writing CommonJS modules, it does not prevent you from importing them as dependencies. There’s currently no TypeScript setting that can guard against an ES module importing a CommonJS module, as would be appropriate for direct-to-browser code.)

### Module specifiers are not transformed by default

 While the `module` compiler option can transform imports and exports in input files to different module formats in output files, the module specifier (the string `from` which you `import`, or pass to `require`) is emitted as-written. For example, an input like:

 ts ` import { add } from "./math.mjs" ; add ( 1 , 2 ); `
 might be emitted as either:

 ts ` import { add } from "./math.mjs" ; add ( 1 , 2 ); `
 or:

 ts ` const math_1 = require ( "./math.mjs" ); math_1 . add ( 1 , 2 ); `
 depending on the `module` compiler option, but the module specifier will be `"./math.mjs"` either way. By default, module specifiers must be written in a way that works for the code’s target runtime or bundler, and it’s TypeScript’s job to understand those output -relative specifiers. The process of finding the file referenced by a module specifier is called module resolution .

TypeScript 5.7 introduced the `--rewriteRelativeImportExtensions` option , which transforms relative module specifiers with `.ts`, `.tsx`, `.mts`, or `.cts` extensions to their JavaScript equivalents in output files. This option is useful for creating TypeScript files that can be run directly in Node.js during development and still be compiled to JavaScript outputs for distribution or production use.

This documentation was written before the introduction of `--rewriteRelativeImportExtensions`, and the mental model it presents is built around modeling the behavior of the host module system operating on its input files, whether that’s a bundler operating on TypeScript files or a runtime operating on `.js` outputs. With `--rewriteRelativeImportExtensions`, the way to apply that mental model is to apply it twice : once to the runtime or bundler processing the TypeScript input files directly, and once again to the runtime or bundler processing the transformed outputs. Most of this documentation assumes that only the input files or only the output files will be loaded, but the principles it presents can be extended to the case where both are loaded.

## Module resolution

 Let’s return to our first example and review what we’ve learned about it so far:

 ts ` import sayHello from "greetings" ; sayHello ( "world" ); `
 So far, we’ve discussed how the host’s module system and TypeScript’s `module` compiler option might impact this code. We know that the input syntax looks like ESM, but the output format depends on the `module` compiler option, potentially the file extension, and `package.json` `"type"` field. We also know that what `sayHello` gets bound to, and even whether the import is even allowed, may vary depending on the module kinds of this file and the target file. But we haven’t yet discussed how to find the target file.

### Module resolution is host-defined

 While the ECMAScript specification defines how to parse and interpret `import` and `export` statements, it leaves module resolution up to the host. If you’re creating a hot new JavaScript runtime, you’re free to create a module resolution scheme like:

 ts ` import monkey from "🐒" ; // Looks for './eats/bananas.js' import cow from "🐄" ; // Looks for './eats/grass.js' import lion from "🦁" ; // Looks for './eats/you.js' `
 and still claim to implement “standards-compliant ESM.” Needless to say, TypeScript would have no idea what types to assign to `monkey`, `cow`, and `lion` without built-in knowledge of this runtime’s module resolution algorithm. Just as `module` informs the compiler about the host’s expected module format, `moduleResolution`, along with a few customization options, specify the algorithm the host uses to resolve module specifiers to files. This also clarifies why TypeScript doesn’t modify import specifiers during emit: the relationship between an import specifier and a file on disk (if one even exists) is host-defined, and TypeScript is not a host.

The available `moduleResolution` options are:

- `classic` : TypeScript’s oldest module resolution mode, this is unfortunately the default when `module` is set to anything other than `commonjs`, `node16`, or `nodenext`. It was probably made to provide best-effort resolution for a wide range of RequireJS configurations. It should not be used for new projects (or even old projects that don’t use RequireJS or another AMD module loader), and is scheduled for deprecation in TypeScript 6.0.

- `node10` : Formerly known as `node`, this is the unfortunate default when `module` is set to `commonjs`. It’s a pretty good model of Node.js versions older than v12, and sometimes it’s a passable approximation of how most bundlers do module resolution. It supports looking up packages from `node_modules`, loading directory `index.js` files, and omitting `.js` extensions in relative module specifiers. Because Node.js v12 introduced different module resolution rules for ES modules, though, it’s a very bad model of modern versions of Node.js. It should not be used for new projects.

- `node16` : This is the counterpart of `--module node16` and `--module node18` and is set by default with that `module` setting. Node.js v12 and later support both ESM and CJS, each of which uses its own module resolution algorithm. In Node.js, module specifiers in import statements and dynamic `import()` calls are not allowed to omit file extensions or `/index.js` suffixes, while module specifiers in `require` calls are. This module resolution mode understands and enforces this restriction where necessary, as determined by the module format detection rules instated by `--module node16`/`node18`. (For `node16` and `nodenext`, `module` and `moduleResolution` go hand-in-hand: setting one to `node16` or `nodenext` while setting the other to something else is an error.)

- `nodenext` : Currently identical to `node16`, this is the counterpart of `--module nodenext` and is set by default with that `module` setting. It’s intended to be a forward-looking mode that will support new Node.js module resolution features as they’re added.

- `bundler` : Node.js v12 introduced some new module resolution features for importing npm packages—the `"exports"` and `"imports"` fields of `package.json`—and many bundlers adopted those features without also adopting the stricter rules for ESM imports. This module resolution mode provides a base algorithm for code targeting a bundler. It supports `package.json` `"exports"` and `"imports"` by default, but can be configured to ignore them. It requires setting `module` to `esnext`.

### TypeScript imitates the host’s module resolution, but with types

 Remember the three components of TypeScript’s job concerning modules?

- Compile files into a valid output module format

- Ensure that imports in those outputs will resolve successfully

- Know what type to assign to imported names .

Module resolution is needed to accomplish last two. But when we spend most of our time working in input files, it can be easy to forget about (2)—that a key component of module resolution is validating that the imports or `require` calls in the output files, containing the same module specifiers as the input files , will actually work at runtime. Let’s look at a new example with multiple files:

 ts ` // @Filename: math.ts export function add ( a : number , b : number ) { return a + b ; } // @Filename: main.ts import { add } from "./math" ; add ( 1 , 2 ); `
 When we see the import from `"./math"`, it might be tempting to think, “This is how one TypeScript file refers to another. The compiler follows this (extensionless) path in order to assign a type to `add`.”

This isn’t entirely wrong, but the reality is deeper. The resolution of `"./math"` (and subsequently, the type of `add`) need to reflect the reality of what happens at runtime to the output files. A more robust way to think about this process would look like this:

This model makes it clear that for TypeScript, module resolution is mostly a matter of accurately modeling the host’s module resolution algorithm between output files, with a little bit of remapping applied to find type information. Let’s look at another example that appears unintuitive through the lens of the simple model, but makes perfect sense with the robust model:

 ts ` // @moduleResolution: node16 // @rootDir: src // @outDir: dist // @Filename: src/math.mts export function add ( a : number , b : number ) { return a + b ; } // @Filename: src/main.mts import { add } from "./math.mjs" ; add ( 1 , 2 ); `
 Node.js ESM `import` declarations use a strict module resolution algorithm that requires relative paths to include file extensions. When we only think about input files, it’s a little strange that `"./math.mjs"` seems to resolve to `math.mts`. Since we’re using an `outDir` to put compiled outputs in a different directory, `math.mjs` doesn’t even exist next to `main.mts`! Why should this resolve? With our new mental model, it’s no problem:

Understanding this mental model may not immediately eliminate the strangeness of seeing output file extensions in input files, and it’s natural to think in terms of shortcuts: `"./math.mjs"` refers to the input file `math.mts`. I have to write the output extension, but the compiler knows to look for `.mts` when I write `.mjs`. This shortcut is even how the compiler works internally, but the more robust mental model explains why module resolution in TypeScript works this way: given the constraint that the module specifier in the output file will be the same as the module specifier in the input file, this is the only process that accomplishes our two goals of validating output files and assigning types.

### The role of declaration files

 In the previous example, we saw the “remapping” part of module resolution working between input and output files. But what happens when we import library code? Even if the library was written in TypeScript, it may not have published its source code. If we can’t rely on mapping the library’s JavaScript files back to a TypeScript file, we can verify that our import works at runtime, but how do we accomplish our second goal of assigning types?

This is where declaration files (`.d.ts`, `.d.mts`, etc.) come into play. The best way to understand how declaration files are interpreted is to understand where they come from. When you run `tsc --declaration` on an input file, you get one output JavaScript file and one output declaration file:

Because of this relationship, the compiler assumes that wherever it sees a declaration file, there is a corresponding JavaScript file that is perfectly described by the type information in the declaration file. For performance reasons, in every module resolution mode, the compiler always looks for TypeScript and declaration files first, and if it finds one, it doesn’t continue looking for the corresponding JavaScript file. If it finds a TypeScript input file, it knows a JavaScript file will exist after compilation, and if it finds a declaration file, it knows a compilation (perhaps someone else’s) already happened and created a JavaScript file at the same time as the declaration file.

The declaration file tells the compiler not only that a JavaScript file exists, but also what its name and extension are:

| **

 Declaration file extension**
| **JavaScript file extension**
| **TypeScript file extension**
|

| `.d.ts`
| `.js`
| `.ts`
|

| `.d.ts`
| `.js`
| `.tsx`
|

| `.d.mts`
| `.mjs`
| `.mts`
|

| `.d.cts`
| `.cjs`
| `.cts`
|

| `.d.*.ts`
| `.*`
|
|

The last row expresses that non-JS files can be typed with the `allowArbitraryExtensions` compiler option to support cases where the module system supports importing non-JS files as JavaScript objects. For example, a file named `styles.css` can be represented by a declaration file named `styles.d.css.ts`.

“But wait! Plenty of declaration files are written by hand, not generated by `tsc`. Ever heard of DefinitelyTyped?” you might object. And it’s true—hand-writing declaration files, or even moving/copying/renaming them to represent outputs of an external build tool, is a dangerous, error-prone venture. DefinitelyTyped contributors and authors of typed libraries not using `tsc` to generate both JavaScript and declaration files should ensure that every JavaScript file has a sibling declaration file with the same name and matching extension. Breaking from this structure can lead to false-positive TypeScript errors for end users. The npm package `@arethetypeswrong/cli` can help catch and explain these errors before they’re published.

### Module resolution for bundlers, TypeScript runtimes, and Node.js loaders

 So far, we’ve really emphasized the distinction between input files and output files . Recall that when specifying a file extension on a relative module specifier, TypeScript typically makes you use the output file extension :

 ts ` // @Filename: src/math.ts export function add ( a : number , b : number ) { return a + b ; } // @Filename: src/main.ts import { add } from "./math.ts" ; // ^^^^^^^^^^^ // An import path can only end with a '.ts' extension when 'allowImportingTsExtensions' is enabled. `
 This restriction applies since TypeScript won’t rewrite the extension to `.js`, and if `"./math.ts"` appears in an output JS file, that import won’t resolve to another JS file at runtime. TypeScript really wants to prevent you from generating an unsafe output JS file. But what if there is no output JS file? What if you’re in one of these situations:

- You’re bundling this code, the bundler is configured to transpile TypeScript files in-memory, and it will eventually consume and erase all the imports you’ve written to produce a bundle.

- You’re running this code directly in a TypeScript runtime like Node, Deno or Bun.

- You’re using `ts-node`, `tsx`, or another transpiling loader for Node.

In these cases, you can turn on `noEmit` (or `emitDeclarationOnly`) and `allowImportingTsExtensions` to disable emitting unsafe JavaScript files and silence the error on `.ts`-extensioned imports.

With or without `allowImportingTsExtensions`, it’s still important to pick the most appropriate `moduleResolution` setting for the module resolution host. For bundlers and the Bun runtime, it’s `bundler`. These module resolvers were inspired by Node.js, but didn’t adopt the strict ESM resolution algorithm that disables extension searching that Node.js applies to imports. The `bundler` module resolution setting reflects this, enabling `package.json` `"exports"` support like `node16`—`nodenext`, while always allowing extensionless imports. See Choosing compiler options for more guidance.

### Module resolution for libraries

 When compiling an app, you choose the `moduleResolution` option for a TypeScript project based on who the module resolution host is. When compiling a library, you don’t know where the output code will run, but you’d like it to run in as many places as possible. Using `"module": "node18"` (along with the implied `"moduleResolution": "node16"` ) is the best bet for maximizing the compatibility of the output JavaScript’s module specifiers, since it will force you to comply with Node.js’s stricter rules for `import` module resolution. Let’s look at what would happen if a library were to compile with `"moduleResolution": "bundler"` (or worse, `"node10"`):

 ts ` export * from "./utils" ; `
 Assuming `./utils.ts` (or `./utils/index.ts`) exists, a bundler would be fine with this code, so `"moduleResolution": "bundler"` doesn’t complain. Compiled with `"module": "esnext"`, the output JavaScript for this export statement will look exactly the same as the input. If that JavaScript were published to npm, it would be usable by projects that use a bundler, but it would cause an error when run in Node.js:

 ` Error [ERR_MODULE_NOT_FOUND]: Cannot find module '.../node_modules/dependency/utils' imported from .../node_modules/dependency/index.js Did you mean to import ./utils.js? `
 On the other hand, if we had written:

 ts ` export * from "./utils.js" ; `
 This would produce output that works both in Node.js and in bundlers.

In short, `"moduleResolution": "bundler"` is infectious, allowing code that only works in bundlers to be produced. Likewise, `"moduleResolution": "nodenext"` is only checking that the output works in Node.js, but in most cases, module code that works in Node.js will work in other runtimes and in bundlers.

Of course, this guidance can only apply in cases where the library ships outputs from `tsc`. If the library is being bundled before shipping, `"moduleResolution": "bundler"` may be acceptable. Any build tool that changes the module format or module specifiers to produce the final build of the library bears the responsibility of ensuring the safety and compatibility of the product’s module code, and `tsc` can no longer contribute to that task, since it can’t know what module code will exist at runtime.

- In Node.js v20.19.0 and later, a `require` of an ES module is allowed, but only if the resolved module and its top-level imports don’t use top-level `await`. TypeScript does not try to enforce this rule, as it lacks the ability to tell from a declaration file whether the corresponding JavaScript file contains top-level `await`. ↩

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: AB RP MS FS Last updated: Jun 15, 2026

## Choosing Compiler Options

Was this page helpful?

# Modules - Choosing Compiler Options

## I’m writing an app

 A single tsconfig.json can only represent a single environment, both in terms of what globals are available and in terms of how modules behave. If your app contains server code, DOM code, web worker code, test code, and code to be shared by all of those, each of those should have its own tsconfig.json, connected with project references . Then, use this guide once for each tsconfig.json. For library-like projects within an app, especially ones that need to run in multiple runtime environments, use the “ I’m writing a library ” section.

### I’m using a bundler

 In addition to adopting the following settings, it’s also recommended not to set `{ "type": "module" }` or use `.mts` files in bundler projects for now. Some bundlers adopt different ESM/CJS interop behavior under these circumstances, which TypeScript cannot currently analyze with `"moduleResolution": "bundler"`. See issue #54102 for more information.

 json ` { "compilerOptions" : { // This is not a complete template; it only // shows relevant module-related settings. // Be sure to set other important options // like `target`, `lib`, and `strict`. // Required "module" : "esnext" , "moduleResolution" : "bundler" , "esModuleInterop" : true , // Consult your bundler’s documentation "customConditions" : [ "module" ], // Recommended "noEmit" : true , // or `emitDeclarationOnly` "allowImportingTsExtensions" : true , "allowArbitraryExtensions" : true , "verbatimModuleSyntax" : true , // or `isolatedModules` } } `

### I’m compiling and running the outputs in Node.js

 Remember to set `"type": "module"` or use `.mts` files if you intend to emit ES modules.

 json ` { "compilerOptions" : { // This is not a complete template; it only // shows relevant module-related settings. // Be sure to set other important options // like `target`, `lib`, and `strict`. // Required "module" : "nodenext" , // Implied by `"module": "nodenext"`: // "moduleResolution": "nodenext", // "esModuleInterop": true, // "target": "esnext", // Recommended "verbatimModuleSyntax" : true , } } `

### I’m using ts-node

 ts-node attempts to be compatible with the same code and the same tsconfig.json settings that can be used to compile and run the JS outputs in Node.js . Refer to ts-node documentation for more details.

### I’m using tsx

 Whereas ts-node makes minimal modifications to Node.js’s module system by default, tsx behaves more like a bundler, allowing extensionless/index module specifiers and arbitrary mixing of ESM and CJS. Use the same settings for tsx as you would for a bundler .

### I’m writing ES modules for the browser, with no bundler or module compiler

 TypeScript does not currently have options dedicated to this scenario, but you can approximate them by using a combination of the `nodenext` ESM module resolution algorithm and `paths` as a substitute for URL and import map support.

 json ` // tsconfig.json { "compilerOptions" : { // This is not a complete template; it only // shows relevant module-related settings. // Be sure to set other important options // like `target`, `lib`, and `strict`. // Combined with `"type": "module"` in a local package.json, // this enforces including file extensions on relative path imports. "module" : "nodenext" , "paths" : { // Point TS to local types for remote URLs: "https://esm.sh/lodash@4.17.21" : [ "./node_modules/@types/lodash/index.d.ts" ], // Optional: point bare specifier imports to an empty file // to prohibit importing from node_modules specifiers not listed here: "*" : [ "./empty-file.ts" ] } } } `
 This setup allows explicitly listed HTTPS imports to use locally-installed type declaration files, while erroring on imports that would normally resolve in node_modules:

 ts ` import {} from "lodash" ; // ^^^^^^^^ // File '/project/empty-file.ts' is not a module. ts(2306) `
 Alternatively, you can use import maps to explicitly map a list of bare specifiers to URLs in the browser, while relying on `nodenext`’s default node_modules lookups, or on `paths`, to direct TypeScript to type declaration files for those bare specifier imports:

 html ` <script type = "importmap" > { "imports": { "lodash": "https://esm.sh/lodash@4.17.21" } } </script> `

```
 ts ` import {} from "lodash" ; // Browser: https://esm.sh/lodash@4.17.21 // TypeScript: ./node_modules/@types/lodash/index.d.ts `
```

## I’m writing a library

 Choosing compilation settings as a library author is a fundamentally different process from choosing settings as an app author. When writing an app, settings are chosen that reflect the runtime environment or bundler—typically a single entity with known behavior. When writing a library, you would ideally check your code under all possible library consumer compilation settings. Since this is impractical, you can instead use the strictest possible settings, since satisfying those tends to satisfy all others.

 json ` { "compilerOptions" : { "module" : "node18" , "target" : "es2020" , // set to the *lowest* target you support "strict" : true , "verbatimModuleSyntax" : true , "declaration" : true , "sourceMap" : true , "declarationMap" : true , "rootDir" : "src" , "outDir" : "dist" } } `
 Let’s examine why we picked each of these settings:

-
 `module: "node18"` . When a codebase is compatible with Node.js’s module system, it almost always works in bundlers as well. If you’re using a third-party emitter to emit ESM outputs, ensure that you set `"type": "module"` in your package.json so TypeScript checks your code as ESM, which uses a stricter module resolution algorithm in Node.js than CommonJS does. As an example, let’s look at what would happen if a library were to compile with `"moduleResolution": "bundler"`:

 ts ` export * from "./utils" ; `
 Assuming `./utils.ts` (or `./utils/index.ts`) exists, a bundler would be fine with this code, so `"moduleResolution": "bundler"` doesn’t complain. Compiled with `"module": "esnext"`, the output JavaScript for this export statement will look exactly the same as the input. If that JavaScript were published to npm, it would be usable by projects that use a bundler, but it would cause an error when run in Node.js:

 ` Error [ERR_MODULE_NOT_FOUND]: Cannot find module '.../node_modules/dependency/utils' imported from .../node_modules/dependency/index.js Did you mean to import ./utils.js? `
 On the other hand, if we had written:

 ts ` export * from "./utils.js" ; `
 This would produce output that works both in Node.js and in bundlers.

In short, `"moduleResolution": "bundler"` is infectious, allowing code that only works in bundlers to be produced. Likewise, `"moduleResolution": "nodenext"` is only checking that the output works in Node.js, but in most cases, module code that works in Node.js will work in other runtimes and in bundlers.

-
 `target: "es2020"` . Setting this value to the lowest ECMAScript version that you intend to support ensures the emitted code will not use language features introduced in a later version. Since `target` also implies a corresponding value for `lib`, this also ensures you don’t access globals that may not be available in older environments.

-
 `strict: true` . Without this, you may write type-level code that ends up in your output `.d.ts` files and errors when a consumer compiles with `strict` enabled. For example, this `extends` clause:

 ts ` export interface Super { foo : string ; } export interface Sub extends Super { foo : string | undefined ; } `
 is only an error under `strictNullChecks`. On the other hand, it’s very difficult to write code that errors only when `strict` is disabled , so it’s highly recommended for libraries to compile with `strict`.

-
 `verbatimModuleSyntax: true` . This setting protects against a few module-related pitfalls that can cause problems for library consumers. First, it prevents writing any import statements that could be interpreted ambiguously based on the user’s value of `esModuleInterop` or `allowSyntheticDefaultImports`. Previously, it was often suggested that libraries compile without `esModuleInterop`, since its use in libraries could force users to adopt it too. However, it’s also possible to write imports that only work without `esModuleInterop`, so neither value for the setting guarantees portability for libraries. `verbatimModuleSyntax` does provide such a guarantee. 1 Second, it prevents the use of `export default` in modules that will be emitted as CommonJS, which can require bundler users and Node.js ESM users to consume the module differently. See the appendix on ESM/CJS Interop for more details.

-
 `declaration: true` emits type declaration files alongside the output JavaScript. This is needed for consumers of the library to have any type information.

-
 `sourceMap: true` and `declarationMap: true` emit source maps for the output JavaScript and type declaration files, respectively. These are only useful if the library also ships its source (`.ts`) files. By shipping source maps and source files, consumers of the library will be able to debug the library code somewhat more easily. By shipping declaration maps and source files, consumers will be able to see the original TypeScript sources when they run Go To Definition on imports from the libraries. Both of these represent a tradeoff between developer experience and library size, so it’s up to you whether to include them.

-
 `rootDir: "src"` and `outDir: "dist"` . Using a separate output directory is always a good idea, but it’s necessary for libraries that publish their input files. Otherwise, extension substitution will cause the library’s consumers to load the library’s `.ts` files instead of `.d.ts` files, causing type errors and performance problems.

### Considerations for bundling libraries

 If you’re using a bundler to emit your library, then all your (non-externalized) imports will be processed by the bundler with known behavior, not by your users’ unknowable environments. In this case, you can use `"module": "esnext"` and `"moduleResolution": "bundler"`, but only with two caveats:

-
TypeScript cannot model module resolution when some files are bundled and some are externalized. When bundling libraries with dependencies, it’s common to bundle the first-party library source code into a single file, but leave imports of external dependencies as real imports in the bundled output. This essentially means module resolution is split between the bundler and the end user’s environment. To model this in TypeScript, you would want to process bundled imports with `"moduleResolution": "bundler"` and externalized imports with `"moduleResolution": "nodenext"` (or with multiple options to check that everything will work in a range of end-user environments). But TypeScript cannot be configured to use two different module resolution settings in the same compilation. As a consequence, using `"moduleResolution": "bundler"` may allow imports of externalized dependencies that would work in a bundler but are unsafe in Node.js. On the other hand, using `"moduleResolution": "nodenext"` may impose overly strict requirements on bundled imports.

-
You must ensure that your declaration files get bundled as well. Recall the first rule of declaration files : every declaration file represents exactly one JavaScript file. If you use `"moduleResolution": "bundler"` and use a bundler to emit an ESM bundle while using `tsc` to emit many individual declaration files, your declaration files may cause errors when consumed under `"module": "nodenext"`. For example, an input file like:

 ts ` import { Component } from "./extensionless-relative-import" ; `
 will have its import erased by the JS bundler, but produce a declaration file with an identical import statement. That import statement, however, will contain an invalid module specifier in Node.js, since it’s missing a file extension. For Node.js users, TypeScript will error on the declaration file and infect types referencing `Component` with `any`, assuming the dependency will crash at runtime.

If your TypeScript bundler does not produce bundled declaration files, use `"moduleResolution": "nodenext"` to ensure that the imports preserved in your declaration files will be compatible with end-users’ TypeScript settings. Even better, consider not bundling your library.

### Notes on dual-emit solutions

 A single TypeScript compilation (whether emitting or just type checking) assumes that each input file will only produce one output file. Even if `tsc` isn’t emitting anything, the type checking it performs on imported names rely on knowledge about how the output file will behave at runtime, based on the module- and emit-related options set in the tsconfig.json. While third-party emitters are generally safe to use in combination with `tsc` type checking as long as `tsc` can be configured to understand what the other emitter will emit, any solution that emits two different sets of outputs with different module formats while only type checking once leaves (at least) one of the outputs unchecked. Because external dependencies may expose different APIs to CommonJS and ESM consumers, there’s no configuration you can use to guarantee in a single compilation that both outputs will be type-safe. In practice, most dependencies follow best practices and dual-emit outputs work. Running tests and static analysis against all output bundles before publishing significantly reduces the chance of a serious problem going unnoticed.

- `verbatimModuleSyntax` can only work when the JS emitter emits the same module kind as `tsc` would given the tsconfig.json, source file extension, and package.json `"type"`. The option works by enforcing that the `import`/`require` written is identical to the `import`/`require` emitted. Any configuration that produces both an ESM and a CJS output from the same source file is fundamentally incompatible with `verbatimModuleSyntax`, since its whole purpose is to prevent you from writing `import` anywhere that a `require` would be emitted. `verbatimModuleSyntax` can also be defeated by configuring a third-party emitter to emit a different module kind than `tsc` would—for example, by setting `"module": "esnext"` in tsconfig.json while configuring Babel to emit CommonJS. ↩

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: AB TM Last updated: Jun 15, 2026

## Reference

Was this page helpful?

# Modules - Reference

## Module syntax

 The TypeScript compiler recognizes standard ECMAScript module syntax in TypeScript and JavaScript files and many forms of CommonJS syntax in JavaScript files.

There are also a few TypeScript-specific syntax extensions that can be used in TypeScript files and/or JSDoc comments.

### Importing and exporting TypeScript-specific declarations

 Type aliases, interfaces, enums, and namespaces can be exported from a module with an `export` modifier, like any standard JavaScript declaration:

 ts ` // Standard JavaScript syntax... export function f () {} // ...extended to type declarations export type SomeType = /* ... */ ; export interface SomeInterface { /* ... */ } `
 They can also be referenced in named exports, even alongside references to standard JavaScript declarations:

 ts ` export { f , SomeType , SomeInterface }; `
 Exported types (and other TypeScript-specific declarations) can be imported with standard ECMAScript imports:

 ts ` import { f , SomeType , SomeInterface } from "./module.js" ; `
 When using namespace imports or exports, exported types are available on the namespace when referenced in a type position:

 ts ` import * as mod from "./module.js" ; mod . f (); mod . SomeType ; // Property 'SomeType' does not exist on type 'typeof import("./module.js")' let x : mod . SomeType ; // Ok `

### Type-only imports and exports

 When emitting imports and exports to JavaScript, by default, TypeScript automatically elides (does not emit) imports that are only used in type positions and exports that only refer to types. Type-only imports and exports can be used to force this behavior and make the elision explicit. Import declarations written with `import type`, export declarations written with `export type { ... }`, and import or export specifiers prefixed with the `type` keyword are all guaranteed to be elided from the output JavaScript.

 ts ` // @Filename: main.ts import { f , type SomeInterface } from "./module.js" ; import type { SomeType } from "./module.js" ; class C implements SomeInterface { constructor ( p : SomeType ) { f (); } } export type { C }; // @Filename: main.js import { f } from "./module.js" ; class C { constructor ( p ) { f (); } } `
 Even values can be imported with `import type`, but since they won’t exist in the output JavaScript, they can only be used in non-emitting positions:

 ts ` import type { f } from "./module.js" ; f (); // 'f' cannot be used as a value because it was imported using 'import type' let otherFunction : typeof f = () => {}; // Ok `
 A type-only import declaration may not declare both a default import and named bindings, since it appears ambiguous whether `type` applies to the default import or to the entire import declaration. Instead, split the import declaration into two, or use `default` as a named binding:

 ts ` import type fs , { BigIntOptions } from "fs" ; // ^^^^^^^^^^^^^^^^^^^^^ // Error: A type-only import can specify a default import or named bindings, but not both. import type { default as fs , BigIntOptions } from "fs" ; // Ok `

### `import()` types

 TypeScript provides a type syntax similar to JavaScript’s dynamic `import` for referencing the type of a module without writing an import declaration:

 ts ` // Access an exported type: type WriteFileOptions = import ( "fs" ). WriteFileOptions ; // Access the type of an exported value: type WriteFileFunction = typeof import ( "fs" ). writeFile ; `
 This is especially useful in JSDoc comments in JavaScript files, where it’s not possible to import types otherwise:

 ts ` /** @type {import("webpack").Configuration} */ module . exports = { // ... } `

### `export =` and `import = require()`

 When emitting CommonJS modules, TypeScript files can use a direct analog of `module.exports = ...` and `const mod = require("...")` JavaScript syntax:

 ts ` // @Filename: main.ts import fs = require ( "fs" ); export = fs . readFileSync ( "..." ); // @Filename: main.js "use strict" ; const fs = require ( "fs" ); module . exports = fs . readFileSync ( "..." ); `
 This syntax was used over its JavaScript counterparts since variable declarations and property assignments could not refer to TypeScript types, whereas special TypeScript syntax could:

 ts ` // @Filename: a.ts interface Options { /* ... */ } module . exports = Options ; // Error: 'Options' only refers to a type, but is being used as a value here. export = Options ; // Ok // @Filename: b.ts const Options = require ( "./a" ); const options : Options = { /* ... */ }; // Error: 'Options' refers to a value, but is being used as a type here. // @Filename: c.ts import Options = require ( "./a" ); const options : Options = { /* ... */ }; // Ok `

### Ambient modules

 TypeScript supports a syntax in script (non-module) files for declaring a module that exists in the runtime but has no corresponding file. These ambient modules usually represent runtime-provided modules, like `"fs"` or `"path"` in Node.js:

 ts ` declare module "path" { export function normalize ( p : string ): string ; export function join (... paths : any []): string ; export var sep : string ; } `
 Once an ambient module is loaded into a TypeScript program, TypeScript will recognize imports of the declared module in other files:

 ts ` // 👇 Ensure the ambient module is loaded - // may be unnecessary if path.d.ts is included // by the project tsconfig.json somehow. /// <reference path = "path.d.ts" /> import { normalize , join } from "path" ; `
 Ambient module declarations are easy to confuse with module augmentations since they use identical syntax. This module declaration syntax becomes a module augmentation when the file is a module, meaning it has a top-level `import` or `export` statement (or is affected by `--moduleDetection force` or `auto` ):

 ts ` // Not an ambient module declaration anymore! export {}; declare module "path" { export function normalize ( p : string ): string ; export function join (... paths : any []): string ; export var sep : string ; } `
 Ambient modules may use imports inside the module declaration body to refer to other modules without turning the containing file into a module (which would make the ambient module declaration a module augmentation):

 ts ` declare module "m" { // Moving this outside "m" would totally change the meaning of the file! import { SomeType } from "other" ; export function f (): SomeType ; } `
 A pattern ambient module contains a single `*` wildcard character in its name, matching zero or more characters in import paths. This can be useful for declaring modules provided by custom loaders:

 ts ` declare module "*.html" { const content : string ; export default content ; } `

## The `module` compiler option

 This section discusses the details of each `module` compiler option value. See the Module output format theory section for more background on what the option is and how it fits into the overall compilation process. In brief, the `module` compiler option was historically only used to control the output module format of emitted JavaScript files. The more recent `node16`, `node18`, and `nodenext` values, however, describe a wide range of characteristics of Node.js’s module system, including what module formats are supported, how the module format of each file is determined, and how different module formats interoperate.

### `node16`, `node18`, `node20`, `nodenext`

 Node.js supports both CommonJS and ECMAScript modules, with specific rules for which format each file can be and how the two formats are allowed to interoperate. `node16`, `node18`, and `nodenext` describe the full range of behavior for Node.js’s dual-format module system, and emit files in either CommonJS or ESM format . This is different from every other `module` option, which are runtime-agnostic and force all output files into a single format, leaving it to the user to ensure the output is valid for their runtime.

A common misconception is that `node16`—`nodenext` only emit ES modules. In reality, these modes describe versions of Node.js that support ES modules, not just projects that use ES modules. Both ESM and CommonJS emit are supported, based on the detected module format of each file. Because they are the only `module` options that reflect the complexities of Node.js’s dual module system, they are the only correct `module` options for all apps and libraries that are intended to run in Node.js v12 or later, whether they use ES modules or not.

The fixed-version `node16` and `node18` modes represent the module system behavior stabilized in their respective Node.js versions, while the `nodenext` mode changes with the latest stable versions of Node.js. The following table summarizes the current differences between the three modes:

| **

 **
| **`target`**
| **`moduleResolution`**
| **import assertions**
| **import attributes**
| **JSON imports**
| **require(esm)**
|

| node16
| `es2022`
| `node16`
| ❌
| ❌
| no restrictions
| ❌
|

| node18
| `es2022`
| `node16`
| ✅
| ✅
| needs `type "json"`
| ❌
|

| nodenext
| `esnext`
| `nodenext`
| ❌
| ✅
| needs `type "json"`
| ✅
|

#### Module format detection

- `.mts`/`.mjs`/`.d.mts` files are always ES modules.

- `.cts`/`.cjs`/`.d.cts` files are always CommonJS modules.

- `.ts`/`.tsx`/`.js`/`.jsx`/`.d.ts` files are ES modules if the nearest ancestor package.json file contains `"type": "module"`, otherwise CommonJS modules.

 The detected module format of input `.ts`/`.tsx`/`.mts`/`.cts` files determines the module format of the emitted JavaScript files. So, for example, a project consisting entirely of `.ts` files will emit all CommonJS modules by default under `--module nodenext`, and can be made to emit all ES modules by adding `"type": "module"` to the project package.json.

#### Interoperability rules

- When an ES module references a CommonJS module:

 The `module.exports` of the CommonJS module is available as a default import to the ES module.

- Properties (other than `default`) of the CommonJS module’s `module.exports` may or may not be available as named imports to the ES module. Node.js attempts to make them available via static analysis . TypeScript cannot know from a declaration file whether that static analysis will succeed, and optimistically assumes it will. This limits TypeScript’s ability to catch named imports that may crash at runtime. See #54018 for more details.

- When a CommonJS module references an ES module:

 In `node16` and `node18`, `require` cannot reference an ES module. For TypeScript, this includes `import` statements in files that are detected to be CommonJS modules, since those `import` statements will be transformed to `require` calls in the emitted JavaScript.

- In `nodenext`, to reflect the behavior of Node.js v22.12.0 and later, `require` can reference an ES module. In Node.js, an error is thrown if the ES module, or any of its imported modules, uses top-level `await`. TypeScript does not attempt to detect this case and will not emit a compile-time error. The result of the `require` call is the module’s Module Namespace Object, i.e., the same as the result of an `await import()` of the same module (but without the need to `await` anything).

- A dynamic `import()` call can always be used to import an ES module. It returns a Promise of the module’s Module Namespace Object (what you’d get from `import * as ns from "./module.js"` from another ES module).

#### Emit

 The emit format of each file is determined by the detected module format of each file. ESM emit is similar to `--module esnext` , but has a special transformation for `import x = require("...")`, which is not allowed in `--module esnext`:

 ts ` // @Filename: main.ts import x = require ( "mod" ); `

```
 js ` // @Filename: main.js import { createRequire as _createRequire } from "module" ; const __require = _createRequire ( import . meta . url ); const x = __require ( "mod" ); `
```

 CommonJS emit is similar to `--module commonjs` , but dynamic `import()` calls are not transformed. Emit here is shown with `esModuleInterop` enabled:

 ts ` // @Filename: main.ts import fs from "fs" ; // transformed const dynamic = import ( "mod" ); // not transformed `

```
 js ` // @Filename: main.js "use strict" ; var __importDefault = ( this && this . __importDefault ) || function ( mod ) { return ( mod && mod . __esModule ) ? mod : { "default" : mod }; }; Object . defineProperty ( exports , "__esModule" , { value: true }); const fs_1 = __importDefault ( require ( "fs" )); // transformed const dynamic = import ( "mod" ); // not transformed `
```

#### Implied and enforced options

- `--module nodenext` implies and enforces `--moduleResolution nodenext`.

- `--module node18` or `node16` implies and enforces `--moduleResolution node16`.

- `--module nodenext` implies `--target esnext`.

- `--module node18` or `node16` implies `--target es2022`.

- `--module nodenext` or `node18` or `node16` implies `--esModuleInterop`.

#### Summary

- `node16`, `node18`, and `nodenext` are the only correct `module` options for all apps and libraries that are intended to run in Node.js v12 or later, whether they use ES modules or not.

- `node16`, `node18`, and `nodenext` emit files in either CommonJS or ESM format, based on the detected module format of each file.

- Node.js’s interoperability rules between ESM and CJS are reflected in type checking.

- ESM emit transforms `import x = require("...")` to a `require` call constructed from a `createRequire` import.

- CommonJS emit leaves dynamic `import()` calls untransformed, so CommonJS modules can asynchronously import ES modules.

### `preserve`

 In `--module preserve` ( added in TypeScript 5.4), ECMAScript imports and exports written in input files are preserved in the output, and CommonJS-style `import x = require("...")` and `export = ...` statements are emitted as CommonJS `require` and `module.exports`. In other words, the format of each individual import or export statement is preserved, rather than being coerced into a single format for the whole compilation (or even a whole file).

While it’s rare to need to mix imports and require calls in the same file, this `module` mode best reflects the capabilities of most modern bundlers, as well as the Bun runtime.

Why care about TypeScript’s `module` emit with a bundler or with Bun, where you’re likely also setting `noEmit`? TypeScript’s type checking and module resolution behavior are affected by the module format that it would emit. Setting `module` gives TypeScript information about how your bundler or runtime will process imports and exports, which ensures that the types you see on imported values accurately reflect what will happen at runtime or after bundling. See `--moduleResolution bundler` for more discussion.

#### Examples

```
 ts ` // @Filename: main.ts import x , { y , z } from "mod" ; import mod = require ( "mod" ); const dynamic = import ( "mod" ); export const e1 = 0 ; export default "default export" ; `
```

```
 js ` // @Filename: main.js import x , { y , z } from "mod" ; const mod = require ( "mod" ); const dynamic = import ( "mod" ); export const e1 = 0 ; export default "default export" ; `
```

#### Implied and enforced options

- `--module preserve` implies `--moduleResolution bundler`.

- `--module preserve` implies `--esModuleInterop`.

 The option `--esModuleInterop` is enabled by default in `--module preserve` only for its type checking behavior. Since imports never transform into require calls in `--module preserve`, `--esModuleInterop` does not affect the emitted JavaScript.

### `es2015`, `es2020`, `es2022`, `esnext`

#### Summary

- Use `esnext` with `--moduleResolution bundler` for bundlers, Bun, and tsx.

- Do not use for Node.js. Use `node16`, `node18`, or `nodenext` with `"type": "module"` in package.json to emit ES modules for Node.js.

- `import mod = require("mod")` is not allowed in non-declaration files.

- `es2020` adds support for `import.meta` properties.

- `es2022` adds support for top-level `await`.

- `esnext` is a moving target that may include support for Stage 3 proposals to ECMAScript modules.

- Emitted files are ES modules, but dependencies may be any format.

#### Examples

```
 ts ` // @Filename: main.ts import x , { y , z } from "mod" ; import * as mod from "mod" ; const dynamic = import ( "mod" ); console . log ( x , y , z , mod , dynamic ); export const e1 = 0 ; export default "default export" ; `
```

```
 js ` // @Filename: main.js import x , { y , z } from "mod" ; import * as mod from "mod" ; const dynamic = import ( "mod" ); console . log ( x , y , z , mod , dynamic ); export const e1 = 0 ; export default "default export" ; `
```

### `commonjs`

#### Summary

- You probably shouldn’t use this. Use `node16`, `node18`, or `nodenext` to emit CommonJS modules for Node.js.

- Emitted files are CommonJS modules, but dependencies may be any format.

- Dynamic `import()` is transformed to a Promise of a `require()` call.

- `esModuleInterop` affects the output code for default and namespace imports.

#### Examples

 Output is shown with `esModuleInterop: false`.

 ts ` // @Filename: main.ts import x , { y , z } from "mod" ; import * as mod from "mod" ; const dynamic = import ( "mod" ); console . log ( x , y , z , mod , dynamic ); export const e1 = 0 ; export default "default export" ; `

```
 js ` // @Filename: main.js "use strict" ; Object . defineProperty ( exports , "__esModule" , { value: true }); exports . e1 = void 0 ; const mod_1 = require ( "mod" ); const mod = require ( "mod" ); const dynamic = Promise . resolve (). then (() => require ( "mod" )); console . log ( mod_1 . default , mod_1 . y , mod_1 . z , mod ); exports . e1 = 0 ; exports . default = "default export" ; `
```

```
 ts ` // @Filename: main.ts import mod = require ( "mod" ); console . log ( mod ); export = { p1: true , p2: false }; `
```

```
 js ` // @Filename: main.js "use strict" ; const mod = require ( "mod" ); console . log ( mod ); module . exports = { p1: true , p2: false }; `
```

### `system`

#### Summary

- Designed for use with the SystemJS module loader .

#### Examples

```
 ts ` // @Filename: main.ts import x , { y , z } from "mod" ; import * as mod from "mod" ; const dynamic = import ( "mod" ); console . log ( x , y , z , mod , dynamic ); export const e1 = 0 ; export default "default export" ; `
```

```
 js ` // @Filename: main.js System . register ([ "mod" ], function ( exports_1 , context_1 ) { "use strict" ; var mod_1 , mod , dynamic , e1 ; var __moduleName = context_1 && context_1 . id ; return { setters: [ function ( mod_1_1 ) { mod_1 = mod_1_1 ; mod = mod_1_1 ; } ], execute : function () { dynamic = context_1 . import ( "mod" ); console . log ( mod_1 . default , mod_1 . y , mod_1 . z , mod , dynamic ); exports_1 ( "e1" , e1 = 0 ); exports_1 ( "default" , "default export" ); } }; }); `
```

### `amd`

#### Summary

- Designed for AMD loaders like RequireJS.

- You probably shouldn’t use this. Use a bundler instead.

- Emitted files are AMD modules, but dependencies may be any format.

- Supports `outFile`.

#### Examples

```
 ts ` // @Filename: main.ts import x , { y , z } from "mod" ; import * as mod from "mod" ; const dynamic = import ( "mod" ); console . log ( x , y , z , mod , dynamic ); export const e1 = 0 ; export default "default export" ; `
```

```
 js ` // @Filename: main.js define ([ "require" , "exports" , "mod" , "mod" ], function ( require , exports , mod_1 , mod ) { "use strict" ; Object . defineProperty ( exports , "__esModule" , { value: true }); exports . e1 = void 0 ; const dynamic = new Promise (( resolve_1 , reject_1 ) => { require ([ "mod" ], resolve_1 , reject_1 ); }); console . log ( mod_1 . default , mod_1 . y , mod_1 . z , mod , dynamic ); exports . e1 = 0 ; exports . default = "default export" ; }); `
```

### `umd`

#### Summary

- Designed for AMD or CommonJS loaders.

- Does not expose a global variable like most other UMD wrappers.

- You probably shouldn’t use this. Use a bundler instead.

- Emitted files are UMD modules, but dependencies may be any format.

#### Examples

```
 ts ` // @Filename: main.ts import x , { y , z } from "mod" ; import * as mod from "mod" ; const dynamic = import ( "mod" ); console . log ( x , y , z , mod , dynamic ); export const e1 = 0 ; export default "default export" ; `
```

```
 js ` // @Filename: main.js ( function ( factory ) { if ( typeof module === "object" && typeof module . exports === "object" ) { var v = factory ( require , exports ); if ( v !== undefined ) module . exports = v ; } else if ( typeof define === "function" && define . amd ) { define ([ "require" , "exports" , "mod" , "mod" ], factory ); } })( function ( require , exports ) { "use strict" ; var __syncRequire = typeof module === "object" && typeof module . exports === "object" ; Object . defineProperty ( exports , "__esModule" , { value: true }); exports . e1 = void 0 ; const mod_1 = require ( "mod" ); const mod = require ( "mod" ); const dynamic = __syncRequire ? Promise . resolve (). then (() => require ( "mod" )) : new Promise (( resolve_1 , reject_1 ) => { require ([ "mod" ], resolve_1 , reject_1 ); }); console . log ( mod_1 . default , mod_1 . y , mod_1 . z , mod , dynamic ); exports . e1 = 0 ; exports . default = "default export" ; }); `
```

## The `moduleResolution` compiler option

 This section describes module resolution features and processes shared by multiple `moduleResolution` modes, then specifies the details of each mode. See the Module resolution theory section for more background on what the option is and how it fits into the overall compilation process. In brief, `moduleResolution` controls how TypeScript resolves module specifiers (string literals in `import`/`export`/`require` statements) to files on disk, and should be set to match the module resolver used by the target runtime or bundler.

### Common features and processes

#### File extension substitution

 TypeScript always wants to resolve internally to a file that can provide type information, while ensuring that the runtime or bundler can use the same path to resolve to a file that provides a JavaScript implementation. For any module specifier that would, according to the `moduleResolution` algorithm specified, trigger a lookup of a JavaScript file in the runtime or bundler, TypeScript will first try to find a TypeScript implementation file or type declaration file with the same name and analagous file extension.

| **

 Runtime lookup**
| **TypeScript lookup #1**
| **TypeScript lookup #2**
| **TypeScript lookup #3**
| **TypeScript lookup #4**
| **TypeScript lookup #5**
|

| `/mod.js`
| `/mod.ts`
| `/mod.tsx`
| `/mod.d.ts`
| `/mod.js`
| `./mod.jsx`
|

| `/mod.mjs`
| `/mod.mts`
| `/mod.d.mts`
| `/mod.mjs`
|
|
|

| `/mod.cjs`
| `/mod.cts`
| `/mod.d.cts`
| `/mod.cjs`
|
|
|

Note that this behavior is independent of the actual module specifier written in the import. This means that TypeScript can resolve to a `.ts` or `.d.ts` file even if the module specifier explicitly uses a `.js` file extension:

 ts ` import x from "./mod.js" ; // Runtime lookup: "./mod.js" // TypeScript lookup #1: "./mod.ts" // TypeScript lookup #2: "./mod.d.ts" // TypeScript lookup #3: "./mod.js" `
 See TypeScript imitates the host’s module resolution, but with types for an explanation of why TypeScript’s module resolution works this way.

#### Relative file path resolution

 All of TypeScript’s `moduleResolution` algorithms support referencing a module by a relative path that includes a file extension (which will be substituted according to the rules above ):

 ts ` // @Filename: a.ts export {}; // @Filename: b.ts import {} from "./a.js" ; // ✅ Works in every `moduleResolution` `

#### Extensionless relative paths

 In some cases, the runtime or bundler allows omitting a `.js` file extension from a relative path. TypeScript supports this behavior where the `moduleResolution` setting and the context indicate that the runtime or bundler supports it:

 ts ` // @Filename: a.ts export {}; // @Filename: b.ts import {} from "./a" ; `
 If TypeScript determines that the runtime will perform a lookup for `./a.js` given the module specifier `"./a"`, then `./a.js` will undergo extension substitution , and resolve to the file `a.ts` in this example.

Extensionless relative paths are not supported in `import` paths in Node.js, and are not always supported in file paths specified in package.json files. TypeScript currently never supports omitting a `.mjs`/`.mts` or `.cjs`/`.cts` file extension, even though some runtimes and bundlers do.

#### Directory modules (index file resolution)

 In some cases, a directory, rather than a file, can be referenced as a module. In the simplest and most common case, this involves the runtime or bundler looking for an `index.js` file in a directory. TypeScript supports this behavior where the `moduleResolution` setting and the context indicate that the runtime or bundler supports it:

 ts ` // @Filename: dir/index.ts export {}; // @Filename: b.ts import {} from "./dir" ; `
 If TypeScript determines that the runtime will perform a lookup for `./dir/index.js` given the module specifier `"./dir"`, then `./dir/index.js` will undergo extension substitution , and resolve to the file `dir/index.ts` in this example.

Directory modules may also contain a package.json file, where resolution of the `"main"` and `"types"` fields are supported, and take precedence over `index.js` lookups. The `"typesVersions"` field is also supported in directory modules.

Note that directory modules are not the same as `node_modules` packages and only support a subset of the features available to packages, and are not supported at all in some contexts. Node.js considers them a legacy feature .

#### `paths`

 Overview
 TypeScript offers a way to override the compiler’s module resolution for bare specifiers with the `paths` compiler option. While the feature was originally designed to be used with the AMD module loader (a means of running modules in the browser before ESM existed or bundlers were widely used), it still has uses today when a runtime or bundler supports module resolution features that TypeScript does not model. For example, when running Node.js with `--experimental-network-imports`, you can manually specify a local type definition file for a specific `https://` import:

 json ` { "compilerOptions" : { "module" : "nodenext" , "paths" : { "https://esm.sh/lodash@4.17.21" : [ "./node_modules/@types/lodash/index.d.ts" ] } } } `

```
 ts ` // Typed by ./node_modules/@types/lodash/index.d.ts due to `paths` entry import { add } from "https://esm.sh/lodash@4.17.21" ; `
```

 It’s also common for apps built with bundlers to define convenience path aliases in their bundler configuration, and then inform TypeScript of those aliases with `paths`:

 json ` { "compilerOptions" : { "module" : "esnext" , "moduleResolution" : "bundler" , "paths" : { "@app/*" : [ "./src/*" ] } } } `
 `paths` does not affect emit
 The `paths` option does not change the import path in the code emitted by TypeScript. Consequently, it’s very easy to create path aliases that appear to work in TypeScript but will crash at runtime:

 json ` { "compilerOptions" : { "module" : "nodenext" , "paths" : { "node-has-no-idea-what-this-is" : [ "./oops.ts" ] } } } `

```
 ts ` // TypeScript: ✅ // Node.js: 💥 import {} from "node-has-no-idea-what-this-is" ; `
```

 While it’s ok for bundled apps to set up `paths`, it’s very important that published libraries do not , since the emitted JavaScript will not work for consumers of the library without those users setting up the same aliases for both TypeScript and their bundler. Both libraries and apps can consider package.json `"imports"` as a standard replacement for convenience `paths` aliases.

 `paths` should not point to monorepo packages or node_modules packages
 While module specifiers that match `paths` aliases are bare specifiers, once the alias is resolved, module resolution proceeds on the resolved path as a relative path. Consequently, resolution features that happen for `node_modules` package lookups , including package.json `"exports"` field support, do not take effect when a `paths` alias is matched. This can lead to surprising behavior if `paths` is used to point to a `node_modules` package:

 ts ` { "compilerOptions" : { "paths" : { "pkg" : [ "./node_modules/pkg/dist/index.d.ts" ], "pkg/*" : [ "./node_modules/pkg/*" ] } } } `
 While this configuration may simulate some of the behavior of package resolution, it overrides any `main`, `types`, `exports`, and `typesVersions` the package’s `package.json` file defines, and imports from the package may fail at runtime.

The same caveat applies to packages referencing each other in a monorepo. Instead of using `paths` to make TypeScript artificially resolve `"@my-scope/lib"` to a sibling package, it’s best to use workspaces via npm , yarn , or pnpm to symlink your packages into `node_modules`, so both TypeScript and the runtime or bundler perform real `node_modules` package lookups. This is especially important if the monorepo packages will be published to npm—the packages will reference each other via `node_modules` package lookups once installed by users, and using workspaces allows you to test that behavior during local development.

 Relationship to `baseUrl`
 When `baseUrl` is provided, the values in each `paths` array are resolved relative to the `baseUrl`. Otherwise, they are resolved relative to the `tsconfig.json` file that defines them.

 Wildcard substitutions
 `paths` patterns can contain a single `*` wildcard, which matches any string. The `*` token can then be used in the file path values to substitute the matched string:

 json ` { "compilerOptions" : { "paths" : { "@app/*" : [ "./src/*" ] } } } `
 When resolving an import of `"@app/components/Button"`, TypeScript will match on `@app/*`, binding `*` to `components/Button`, and then attempt to resolve the path `./src/components/Button` relative to the `tsconfig.json` path. The remainder of this lookup will follow the same rules as any other relative path lookup according to the `moduleResolution` setting.

When multiple patterns match a module specifier, the pattern with the longest matching prefix before any `*` token is used:

 json ` { "compilerOptions" : { "paths" : { "*" : [ "./src/foo/one.ts" ], "foo/*" : [ "./src/foo/two.ts" ], "foo/bar" : [ "./src/foo/three.ts" ] } } } `
 When resolving an import of `"foo/bar"`, all three `paths` patterns match, but the last is used because `"foo/bar"` is longer than `"foo/"` and `""`.

 Fallbacks
 Multiple file paths can be provided for a path mapping. If resolution fails for one path, the next one in the array will be attempted until resolution succeeds or the end of the array is reached.

 json ` { "compilerOptions" : { "paths" : { "*" : [ "./vendor/*" , "./types/*" ] } } } `

#### `baseUrl`

 `baseUrl` was designed for use with AMD module loaders. If you aren’t using an AMD module loader, you probably shouldn’t use `baseUrl`. Since TypeScript 4.1, `baseUrl` is no longer required to use `paths` and should not be used just to set the directory `paths` values are resolved from.

The `baseUrl` compiler option can be combined with any `moduleResolution` mode and specifies a directory that bare specifiers (module specifiers that don’t begin with `./`, `../`, or `/`) are resolved from. `baseUrl` has a higher precedence than `node_modules` package lookups in `moduleResolution` modes that support them.

When performing a `baseUrl` lookup, resolution proceeds with the same rules as other relative path resolutions. For example, in a `moduleResolution` mode that supports extensionless relative paths a module specifier `"some-file"` may resolve to `/src/some-file.ts` if `baseUrl` is set to `/src`.

Resolution of relative module specifiers are never affected by the `baseUrl` option.

#### `node_modules` package lookups

 Node.js treats module specifiers that aren’t relative paths, absolute paths, or URLs as references to packages that it looks up in `node_modules` subdirectories. Bundlers conveniently adopted this behavior to allow their users to use the same dependency management system, and often even the same dependencies, as they would in Node.js. All of TypeScript’s `moduleResolution` options except `classic` support `node_modules` lookups. (`classic` supports lookups in `node_modules/@types` when other means of resolution fail, but never looks for packages in `node_modules` directly.) Every `node_modules` package lookup has the following structure (beginning after higher precedence bare specifier rules, like `paths`, `baseUrl`, self-name imports, and package.json `"imports"` lookups have been exhausted):

- For each ancestor directory of the importing file, if a `node_modules` directory exists within it:

 If a directory with the same name as the package exists within `node_modules`:

 Attempt to resolve types from the package directory.

- If a result is found, return it and stop the search.

- If a directory with the same name as the package exists within `node_modules/@types`:

 Attempt to resolve types from the `@types` package directory.

- If a result is found, return it and stop the search.

- Repeat the previous search through all `node_modules` directories, but this time, allow JavaScript files as a result, and do not search in `@types` directories.

All `moduleResolution` modes (except `classic`) follow this pattern, while the details of how they resolve from a package directory, once located, differ, and are explained in the following sections.

#### package.json `"exports"`

 When `moduleResolution` is set to `node16`, `nodenext`, or `bundler`, and `resolvePackageJsonExports` is not disabled, TypeScript follows Node.js’s package.json `"exports"` spec when resolving from a package directory triggered by a bare specifier `node_modules` package lookup .

TypeScript’s implementation for resolving a module specifier through `"exports"` to a file path follows Node.js exactly. Once a file path is resolved, however, TypeScript will still try multiple file extensions in order to prioritize finding types.

When resolving through conditional `"exports"` , TypeScript always matches the `"types"` and `"default"` conditions if present. Additionally, TypeScript will match a versioned types condition in the form `"types@{selector}"` (where `{selector}` is a `"typesVersions"`-compatible version selector) according to the same version-matching rules implemented in `"typesVersions"` . Other non-configurable conditions are dependent on the `moduleResolution` mode and specified in the following sections. Additional conditions can be configured to match with the `customConditions` compiler option.

Note that the presence of `"exports"` prevents any subpaths not explicitly listed or matched by a pattern in `"exports"` from being resolved.

 Example: subpaths, conditions, and extension substitution
 Scenario: `"pkg/subpath"` is requested with conditions `["types", "node", "require"]` (determined by `moduleResolution` setting and the context that triggered the module resolution request) in a package directory with the following package.json:

 json ` { "name" : "pkg" , "exports" : { "." : { "import" : "./index.mjs" , "require" : "./index.cjs" }, "./subpath" : { "import" : "./subpath/index.mjs" , "require" : "./subpath/index.cjs" } } } `
 Resolution process within the package directory:

- Does `"exports"` exist? Yes.

- Does `"exports"` have a `"./subpath"` entry? Yes.

- The value at `exports["./subpath"]` is an object—it must be specifying conditions.

- Does the first condition `"import"` match this request? No.

- Does the second condition `"require"` match this request? Yes.

- Does the path `"./subpath/index.cjs"` have a recognized TypeScript file extension? No, so use extension substitution.

- Via extension substitution , try the following paths, returning the first one that exists, or `undefined` otherwise:

 `./subpath/index.cts`

- `./subpath/index.d.cts`

- `./subpath/index.cjs`

If `./subpath/index.cts` or `./subpath.d.cts` exists, resolution is complete. Otherwise, resolution searches `node_modules/@types/pkg` and other `node_modules` directories in an attempt to resolve types, according to the `node_modules` package lookups rules. If no types are found, a second pass through all `node_modules` resolves to `./subpath/index.cjs` (assuming it exists), which counts as a successful resolution, but one that does not provide types, leading to `any`-typed imports and a `noImplicitAny` error if enabled.

 Example: explicit `"types"` condition
 Scenario: `"pkg/subpath"` is requested with conditions `["types", "node", "import"]` (determined by `moduleResolution` setting and the context that triggered the module resolution request) in a package directory with the following package.json:

 json ` { "name" : "pkg" , "exports" : { "./subpath" : { "import" : { "types" : "./types/subpath/index.d.mts" , "default" : "./es/subpath/index.mjs" }, "require" : { "types" : "./types/subpath/index.d.cts" , "default" : "./cjs/subpath/index.cjs" } } } } `
 Resolution process within the package directory:

- Does `"exports"` exist? Yes.

- Does `"exports"` have a `"./subpath"` entry? Yes.

- The value at `exports["./subpath"]` is an object—it must be specifying conditions.

- Does the first condition `"import"` match this request? Yes.

- The value at `exports["./subpath"].import` is an object—it must be specifying conditions.

- Does the first condition `"types"` match this request? Yes.

- Does the path `"./types/subpath/index.d.mts"` have a recognized TypeScript file extension? Yes, so don’t use extension substitution.

- Return the path `"./types/subpath/index.d.mts"` if the file exists, `undefined` otherwise.

 Example: versioned `"types"` condition
 Scenario: using TypeScript 4.7.5, `"pkg/subpath"` is requested with conditions `["types", "node", "import"]` (determined by `moduleResolution` setting and the context that triggered the module resolution request) in a package directory with the following package.json:

 json ` { "name" : "pkg" , "exports" : { "./subpath" : { "types@>=5.2" : "./ts5.2/subpath/index.d.ts" , "types@>=4.6" : "./ts4.6/subpath/index.d.ts" , "types" : "./tsold/subpath/index.d.ts" , "default" : "./dist/subpath/index.js" } } } `
 Resolution process within the package directory:

- Does `"exports"` exist? Yes.

- Does `"exports"` have a `"./subpath"` entry? Yes.

- The value at `exports["./subpath"]` is an object—it must be specifying conditions.

- Does the first condition `"types@>=5.2"` match this request? No, 4.7.5 is not greater than or equal to 5.2.

- Does the second condition `"types@>=4.6"` match this request? Yes, 4.7.5 is greater than or equal to 4.6.

- Does the path `"./ts4.6/subpath/index.d.ts"` have a recognized TypeScript file extension? Yes, so don’t use extension substitution.

- Return the path `"./ts4.6/subpath/index.d.ts"` if the file exists, `undefined` otherwise.

 Example: subpath patterns
 Scenario: `"pkg/wildcard.js"` is requested with conditions `["types", "node", "import"]` (determined by `moduleResolution` setting and the context that triggered the module resolution request) in a package directory with the following package.json:

 json ` { "name" : "pkg" , "type" : "module" , "exports" : { "./*.js" : { "types" : "./types/*.d.ts" , "default" : "./dist/*.js" } } } `
 Resolution process within the package directory:

- Does `"exports"` exist? Yes.

- Does `"exports"` have a `"./wildcard.js"` entry? No.

- Does any key with a `*` in it match `"./wildcard.js"`? Yes, `"./*.js"` matches and sets `wildcard` to be the substitution.

- The value at `exports["./*.js"]` is an object—it must be specifying conditions.

- Does the first condition `"types"` match this request? Yes.

- In `./types/*.d.ts`, replace `*` with the substitution `wildcard`. `./types/wildcard.d.ts`

- Does the path `"./types/wildcard.d.ts"` have a recognized TypeScript file extension? Yes, so don’t use extension substitution.

- Return the path `"./types/wildcard.d.ts"` if the file exists, `undefined` otherwise.

 Example: `"exports"` block other subpaths
 Scenario: `"pkg/dist/index.js"` is requested in a package directory with the following package.json:

 json ` { "name" : "pkg" , "main" : "./dist/index.js" , "exports" : "./dist/index.js" } `
 Resolution process within the package directory:

- Does `"exports"` exist? Yes.

- The value at `exports` is a string—it must be a file path for the package root (`"."`).

- Is the request `"pkg/dist/index.js"` for the package root? No, it has a subpath `dist/index.js`.

- Resolution fails; return `undefined`.

Without `"exports"`, the request could have succeeded, but the presence of `"exports"` prevents resolving any subpaths that cannot be matched through `"exports"`.

#### package.json `"typesVersions"`

 A `node_modules` package or directory module may specify a `"typesVersions"` field in its package.json to redirect TypeScript’s resolution process according to the TypeScript compiler version, and for `node_modules` packages, according to the subpath being resolved. This allows package authors to include new TypeScript syntax in one set of type definitions while providing another set for backward compatibility with older TypeScript versions (through a tool like downlevel-dts ). `"typesVersions"` is supported in all `moduleResolution` modes; however, the field is not read in situations when package.json `"exports"` are read.

 Example: redirect all requests to a subdirectory
 Scenario: a module imports `"pkg"` using TypeScript 5.2, where `node_modules/pkg/package.json` is:

 json ` { "name" : "pkg" , "version" : "1.0.0" , "types" : "./index.d.ts" , "typesVersions" : { ">=3.1" : { "*" : [ "ts3.1/*" ] } } } `
 Resolution process:

- (Depending on compiler options) Does `"exports"` exist? No.

- Does `"typesVersions"` exist? Yes.

- Is the TypeScript version `>=3.1`? Yes. Remember the mapping `"*": ["ts3.1/*"]`.

- Are we resolving a subpath after the package name? No, just the root `"pkg"`.

- Does `"types"` exist? Yes.

- Does any key in `"typesVersions"` match `./index.d.ts`? Yes, `"*"` matches and sets `index.d.ts` to be the substitution.

- In `ts3.1/*`, replace `*` with the substitution `./index.d.ts`: `ts3.1/index.d.ts` .

- Does the path `./ts3.1/index.d.ts` have a recognized TypeScript file extension? Yes, so don’t use extension substitution.

- Return the path `./ts3.1/index.d.ts` if the file exists, `undefined` otherwise.

 Example: redirect requests for a specific file
 Scenario: a module imports `"pkg"` using TypeScript 3.9, where `node_modules/pkg/package.json` is:

 json ` { "name" : "pkg" , "version" : "1.0.0" , "types" : "./index.d.ts" , "typesVersions" : { "<4.0" : { "index.d.ts" : [ "index.v3.d.ts" ] } } } `
 Resolution process:

- (Depending on compiler options) Does `"exports"` exist? No.

- Does `"typesVersions"` exist? Yes.

- Is the TypeScript version `&#x3C;4.0`? Yes. Remember the mapping `"index.d.ts": ["index.v3.d.ts"]`.

- Are we resolving a subpath after the package name? No, just the root `"pkg"`.

- Does `"types"` exist? Yes.

- Does any key in `"typesVersions"` match `./index.d.ts`? Yes, `"index.d.ts"` matches.

- Does the path `./index.v3.d.ts` have a recognized TypeScript file extension? Yes, so don’t use extension substitution.

- Return the path `./index.v3.d.ts` if the file exists, `undefined` otherwise.

#### package.json `"main"` and `"types"`

 If a directory’s package.json `"exports"` field is not read (either due to compiler options, or because it is not present, or because the directory is being resolved as a directory module instead of a `node_modules` package ) and the module specifier does not have a subpath after the package name or package.json-containing directory, TypeScript will attempt to resolve from these package.json fields, in order, in an attempt to find the main module for the package or directory:

- `"types"`

- `"typings"` (legacy)

- `"main"`

The declaration file found at `"types"` is assumed to be an accurate representation of the implementation file found at `"main"`. If `"types"` and `"typings"` are not present or cannot be resolved, TypeScript will read the `"main"` field and perform extension substitution to find a declaration file.

When publishing a typed package to npm, it’s recommended to include a `"types"` field even if extension substitution or package.json `"exports"` make it unnecessary, because npm shows a TS icon on the package registry listing only if the package.json contains a `"types"` field.

#### Package-relative file paths

 If neither package.json `"exports"` nor package.json `"typesVersions"` apply, subpaths of a bare package specifier resolve relative to the package directory, according to applicable relative path resolution rules. In modes that respect [package.json `"exports"`], this behavior is blocked by the mere presence of the `"exports"` field in the package’s package.json, even if the import fails to resolve through `"exports"`, as demonstrated in an example above . On the other hand, if the import fails to resolve through `"typesVersions"`, a package-relative file path resolution is attempted as a fallback.

When package-relative paths are supported, they resolve under the same rules as any other relative path considering the `moduleResolution` mode and context. For example, in `--moduleResolution nodenext` , directory modules and extensionless paths are only supported in `require` calls, not in `import`s:

 ts ` // @Filename: module.mts import "pkg/dist/foo" ; // ❌ import, needs `.js` extension import "pkg/dist/foo.js" ; // ✅ import foo = require ( "pkg/dist/foo" ); // ✅ require, no extension needed `

#### package.json `"imports"` and self-name imports

 When `moduleResolution` is set to `node16`, `nodenext`, or `bundler`, and `resolvePackageJsonImports` is not disabled, TypeScript will attempt to resolve import paths beginning with `#` through the `"imports"` field of the nearest ancestor package.json of the importing file. Similarly, when package.json `"exports"` lookups are enabled, TypeScript will attempt to resolve import paths beginning with the current package name—that is, the value in the `"name"` field of the nearest ancestor package.json of the importing file—through the `"exports"` field of that package.json. Both of these features allow files in a package to import other files in the same package, replacing a relative import path.

TypeScript follows Node.js’s resolution algorithm for `"imports"` and self references exactly up until a file path is resolved. At that point, TypeScript’s resolution algorithm forks based on whether the package.json containing the `"imports"` or `"exports"` being resolved belongs to a `node_modules` dependency or the local project being compiled (i.e., its directory contains the tsconfig.json file for the project that contains the importing file):

- If the package.json is in `node_modules`, TypeScript will apply extension substitution to the file path if it doesn’t already have a recognized TypeScript file extension, and check for the existence of the resulting file paths.

- If the package.json is part of the local project, an additional remapping step is performed in order to find the input TypeScript implementation file that will eventually produce the output JavaScript or declaration file path that was resolved from `"imports"`. Without this step, any compilation that resolves an `"imports"` path would be referencing output files from the previous compilation instead of other input files that are intended to be included in the current compilation. This remapping uses the `outDir`/`declarationDir` and `rootDir` from the tsconfig.json, so using `"imports"` usually requires an explicit `rootDir` to be set.

This variation allows package authors to write `"imports"` and `"exports"` fields that reference only the compilation outputs that will be published to npm, while still allowing local development to use the original TypeScript source files.

 Example: local project with conditions
 Scenario: `"/src/main.mts"` imports `"#utils"` with conditions `["types", "node", "import"]` (determined by `moduleResolution` setting and the context that triggered the module resolution request) in a project directory with a tsconfig.json and package.json:

 json ` // tsconfig.json { "compilerOptions" : { "moduleResolution" : "node16" , "resolvePackageJsonImports" : true , "rootDir" : "./src" , "outDir" : "./dist" } } `

```
 json ` // package.json { "name" : "pkg" , "imports" : { "#utils" : { "import" : "./dist/utils.d.mts" , "require" : "./dist/utils.d.cts" } } } `
```

 Resolution process:

- Import path starts with `#`, try to resolve through `"imports"`.

- Does `"imports"` exist in the nearest ancestor package.json? Yes.

- Does `"#utils"` exist in the `"imports"` object? Yes.

- The value at `imports["#utils"]` is an object—it must be specifying conditions.

- Does the first condition `"import"` match this request? Yes.

- Should we attempt to map the output path to an input path? Yes, because:

 Is the package.json in `node_modules`? No, it’s in the local project.

- Is the tsconfig.json within the package.json directory? Yes.

- In `./dist/utils.d.mts`, replace the `outDir` prefix with `rootDir`. `./src/utils.d.mts`

- Replace the output extension `.d.mts` with the corresponding input extension `.mts`. `./src/utils.mts`

- Return the path `"./src/utils.mts"` if the file exists.

- Otherwise, return the path `"./dist/utils.d.mts"` if the file exists.

 Example: `node_modules` dependency with subpath pattern
 Scenario: `"/node_modules/pkg/main.mts"` imports `"#internal/utils"` with conditions `["types", "node", "import"]` (determined by `moduleResolution` setting and the context that triggered the module resolution request) with the package.json:

 json ` // /node_modules/pkg/package.json { "name" : "pkg" , "imports" : { "#internal/*" : { "import" : "./dist/internal/*.mjs" , "require" : "./dist/internal/*.cjs" } } } `
 Resolution process:

- Import path starts with `#`, try to resolve through `"imports"`.

- Does `"imports"` exist in the nearest ancestor package.json? Yes.

- Does `"#internal/utils"` exist in the `"imports"` object? No, check for pattern matches.

- Does any key with a `*` match `"#internal/utils"`? Yes, `"#internal/*"` matches and sets `utils` to be the substitution.

- The value at `imports["#internal/*"]` is an object—it must be specifying conditions.

- Does the first condition `"import"` match this request? Yes.

- Should we attempt to map the output path to an input path? No, because the package.json is in `node_modules`.

- In `./dist/internal/*.mjs`, replace `*` with the substitution `utils`. `./dist/internal/utils.mjs`

- Does the path `./dist/internal/utils.mjs` have a recognized TypeScript file extension? No, try extension substitution.

- Via extension substitution , try the following paths, returning the first one that exists, or `undefined` otherwise:

 `./dist/internal/utils.mts`

- `./dist/internal/utils.d.mts`

- `./dist/internal/utils.mjs`

### `node16`, `nodenext`

 These modes reflect the module resolution behavior of Node.js v12 and later. (`node16` and `nodenext` are currently identical, but if Node.js makes significant changes to its module system in the future, `node16` will be frozen while `nodenext` will be updated to reflect the new behavior.) In Node.js, the resolution algorithm for ECMAScript imports is significantly different from the algorithm for CommonJS `require` calls. For each module specifier being resolved, the syntax and the module format of the importing file are first used to determine whether the module specifier will be in an `import` or `require` in the emitted JavaScript. That information is then passed into the module resolver to determine which resolution algorithm to use (and whether to use the `"import"` or `"require"` condition for package.json `"exports"` or `"imports"` ).

TypeScript files that are determined to be in CommonJS format may still use `import` and `export` syntax by default, but the emitted JavaScript will use `require` and `module.exports` instead. This means that it’s common to see `import` statements that are resolved using the `require` algorithm. If this causes confusion, the `verbatimModuleSyntax` compiler option can be enabled, which prohibits the use of `import` statements that would be emitted as `require` calls.

Note that dynamic `import()` calls are always resolved using the `import` algorithm, according to Node.js’s behavior. However, `import()` types are resolved according to the format of the importing file (for backward compatibility with existing CommonJS-format type declarations):

 ts ` // @Filename: module.mts import x from "./mod.js" ; // `import` algorithm due to file format (emitted as-written) import ( "./mod.js" ); // `import` algorithm due to syntax (emitted as-written) type Mod = typeof import ( "./mod.js" ); // `import` algorithm due to file format import mod = require ( "./mod" ); // `require` algorithm due to syntax (emitted as `require`) // @Filename: commonjs.cts import x from "./mod" ; // `require` algorithm due to file format (emitted as `require`) import ( "./mod.js" ); // `import` algorithm due to syntax (emitted as-written) type Mod = typeof import ( "./mod" ); // `require` algorithm due to file format import mod = require ( "./mod" ); // `require` algorithm due to syntax (emitted as `require`) `

#### Implied and enforced options

- `--moduleResolution node16` and `nodenext` must be paired with `--module node16`, `node18`, `node20`, or `nodenext` .

#### Supported features

 Features are listed in order of precedence.

| **

 **
| **`import`**
| **`require`**
|

| `paths`
| ✅
| ✅
|

| `baseUrl`
| ✅
| ✅
|

| `node_modules` package lookups
| ✅
| ✅
|

| package.json `"exports"`
| ✅ matches `types`, `node`, `import`
| ✅ matches `types`, `node`, `require`
|

| package.json `"imports"` and self-name imports
| ✅ matches `types`, `node`, `import`
| ✅ matches `types`, `node`, `require`
|

| package.json `"typesVersions"`
| ✅
| ✅
|

| Package-relative paths
| ✅ when `exports` not present
| ✅ when `exports` not present
|

| Full relative paths
| ✅
| ✅
|

| Extensionless relative paths
| ❌
| ✅
|

| Directory modules
| ❌
| ✅
|

### `bundler`

 `--moduleResolution bundler` attempts to model the module resolution behavior common to most JavaScript bundlers. In short, this means supporting all the behaviors traditionally associated with Node.js’s CommonJS `require` resolution algorithm like `node_modules` lookups , directory modules , and extensionless paths , while also supporting newer Node.js resolution features like package.json `"exports"` and package.json `"imports"` .

It’s instructive to think about the similarities and differences between `--moduleResolution bundler` and `--moduleResolution nodenext`, particularly in how they decide what conditions to use when resolving package.json `"exports"` or `"imports"`. Consider an import statement in a `.ts` file:

 ts ` // index.ts import { foo } from "pkg" ; `
 Recall that in `--module nodenext --moduleResolution nodenext`, the `--module` setting first determines whether the import will be emitted to the `.js` file as an `import` or `require` call, then passes that information to TypeScript’s module resolver, which decides whether to match `"import"` or `"require"` conditions in `"pkg"`’s package.json `"exports"` accordingly. Let’s assume that there’s no package.json in scope of this file. The file extension is `.ts`, so the output file extension will be `.js`, which Node.js will interpret as CommonJS, so TypeScript will emit this `import` as a `require` call. So, the module resolver will use the `require` condition as it resolves `"exports"` from `"pkg"`.

The same process happens in `--moduleResolution bundler`, but the rules for deciding whether to emit an `import` or `require` call for this import statement will be different, since `--moduleResolution bundler` necessitates using `--module esnext` or `--module preserve` . In both of those modes, ESM `import` declarations always emit as ESM `import` declarations, so TypeScript’s module resolver will receive that information and use the `"import"` condition as it resolves `"exports"` from `"pkg"`.

This explanation may be somewhat unintuitive, since `--moduleResolution bundler` is usually used in combination with `--noEmit`—bundlers typically process raw `.ts` files and perform module resolution on untransformed `import`s or `require`s. However, for consistency, TypeScript still uses the hypothetical emit decided by `module` to inform module resolution and type checking. This makes `--module preserve` the best choice whenever a runtime or bundler is operating on raw `.ts` files, since it implies no transformation. Under `--module preserve --moduleResolution bundler`, you can write imports and requires in the same file that will resolve with the `import` and `require` conditions, respectively:

 ts ` // index.ts import pkg1 from "pkg" ; // Resolved with "import" condition import pkg2 = require ( "pkg" ); // Resolved with "require" condition `

#### Implied and enforced options

- `--moduleResolution bundler` must be paired with `--module esnext` or `--module preserve`.

- `--moduleResolution bundler` implies `--allowSyntheticDefaultImports`.

#### Supported features

- `paths` ✅

- `baseUrl` ✅

- `node_modules` package lookups ✅

- package.json `"exports"` ✅ matches `types`, `import`/`require` depending on syntax

- package.json `"imports"` and self-name imports ✅ matches `types`, `import`/`require` depending on syntax

- package.json `"typesVersions"` ✅

- Package-relative paths ✅ when `exports` not present

- Full relative paths ✅

- Extensionless relative paths ✅

- Directory modules ✅

### `node10` (formerly known as `node`)

 `--moduleResolution node` was renamed to `node10` (keeping `node` as an alias for backward compatibility) in TypeScript 5.0. It reflects the CommonJS module resolution algorithm as it existed in Node.js versions earlier than v12. It should no longer be used.

#### Supported features

- `paths` ✅

- `baseUrl` ✅

- `node_modules` package lookups ✅

- package.json `"exports"` ❌

- package.json `"imports"` and self-name imports ❌

- package.json `"typesVersions"` ✅

- Package-relative paths ✅

- Full relative paths ✅

- Extensionless relative paths ✅

- Directory modules ✅

### `classic`

 Do not use `classic`.
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: AB MS YP SF SF 2+ Last updated: Jun 15, 2026

## Esm Cjs Interop

Was this page helpful?

# Modules - ESM/CJS Interoperability
 It’s 2015, and you’re writing an ESM-to-CJS transpiler. There’s no specification for how to do this; all you have is a specification of how ES modules are supposed to interact with each other, knowledge of how CommonJS modules interact with each other, and a knack for figuring things out. Consider an exporting ES module:

 ts ` export const A = {}; export const B = {}; export default "Hello, world!" ; `
 How would you turn this into a CommonJS module? Recalling that default exports are just named exports with special syntax, there seems to be only one choice:

 ts ` exports . A = {}; exports . B = {}; exports . default = "Hello, world!" ; `
 This is a nice analog, and it lets you implement a similar on the importing side:

 ts ` import hello , { A , B } from "./module" ; console . log ( hello , A , B ); // transpiles to: const module_1 = require ( "./module" ); console . log ( module_1 . default , module_1 . A , module_1 . B ); `
 So far, everything in CJS-world matches up one-to-one with everything in ESM-world. Extending the equivalence above one step further, we can see that we also have:

 ts ` import * as mod from "./module" ; console . log ( mod . default , mod . A , mod . B ); // transpiles to: const mod = require ( "./module" ); console . log ( mod . default , mod . A , mod . B ); `
 You might notice that in this scheme, there’s no way to write an ESM export that produces an output where `exports` is assigned a function, class, or primitive:

 ts ` // @Filename: exports-function.js module . exports = function hello () { console . log ( "Hello, world!" ); }; `
 But existing CommonJS modules frequently take this form. How might an ESM import, processed with our transpiler, access this module? We just established that a namespace import (`import *`) transpiles to a plain `require` call, so we can support an input like:

 ts ` import * as hello from "./exports-function" ; hello (); // transpiles to: const hello = require ( "./exports-function" ); hello (); `
 Our output works at runtime, but we have a compliance problem: according to the JavaScript specification, a namespace import always resolves to a Module Namespace Object , that is, an object whose members are the exports of the module. In this case, `require` would return the function `hello`, but `import *` can never return a function. The correspondence we assumed appears invalid.

It’s worth taking a step back here and clarifying what the goal is. As soon as modules landed in the ES2015 specification, transpilers emerged with support for downleveling ESM to CJS, allowing users to adopt the new syntax long before runtimes implemented support for it. There was even a sense that writing ESM code was a good way to “future-proof” new projects. For this to be true, there needed to be a seamless migration path from executing the transpilers’ CJS output to executing the ESM input natively once runtimes developed support for it. The goal was to find a way to downlevel ESM to CJS that would allow any or all of those transpiled outputs to be replaced by their true ESM inputs in a future runtime, with no observable change in behavior.

By following the specification, it was easy enough for transpilers to find a set of transformations that made the semantics of their transpiled CommonJS outputs match the specified semantics of their ESM inputs (arrows represent imports):

However, CommonJS modules (written as CommonJS, not as ESM transpiled to CommonJS) were already well-established in the Node.js ecosystem, so it was inevitable that modules written as ESM and transpiled to CJS would start “importing” modules written as CommonJS. The behavior for this interoperability, though, was not specified by ES2015, and didn’t yet exist in any real runtime.

Even if transpiler authors did nothing, a behavior would emerge from the existing semantics between the `require` calls they emitted in transpiled code and the `exports` defined in existing CJS modules. And to allow users to transition seamlessly from transpiled ESM to true ESM once their runtime supported it, that behavior would have to match the one the runtime chose to implement.

Guessing what interop behavior runtimes would support wasn’t limited to ESM importing “true CJS” modules either. Whether ESM would be able to recognize ESM-transpiled-from-CJS as distinct from CJS, and whether CJS would be able to `require` ES modules, were also unspecified. Even whether ESM imports would use the same module resolution algorithm as CJS `require` calls was unknowable. All these variables would have to be predicted correctly in order to give transpiler users a seamless migration path toward native ESM.

## `allowSyntheticDefaultImports` and `esModuleInterop`

 Let’s return to our specification compliance problem, where `import *` transpiles to `require`:

 ts ` // Invalid according to the spec: import * as hello from "./exports-function" ; hello (); // but the transpilation works: const hello = require ( "./exports-function" ); hello (); `
 When TypeScript first added support for writing and transpiling ES modules, the compiler addressed this problem by issuing an error on any namespace import of a module whose `exports` was not a namespace-like object:

 ts ` import * as hello from "./exports-function" ; // TS2497 ^^^^^^^^^^^^^^^^^^^^ // External module '"./exports-function"' resolves to a non-module entity // and cannot be imported using this construct. `
 The only workaround was for users to go back to using the older TypeScript import syntax representing a CommonJS `require`:

 ts ` import hello = require ( "./exports-function" ); `
 Forcing users to revert to non-ESM syntax was essentially an admission that “we don’t know how or if a CJS module like `"./exports-function"` will be accessible with ESM imports in the future, but we know it can’t be with `import *`, even though it will work at runtime in the transpilation scheme we’re using.” It doesn’t meet the goal of allowing this file to be migrated to real ESM without changes, but neither does the alternative of allowing the `import *` to link to a function. This is still the behavior in TypeScript today when `allowSyntheticDefaultImports` and `esModuleInterop` are disabled.

Unfortunately, this is a slight oversimplification—TypeScript didn’t fully avoid the compliance issue with this error, because it allowed namespace imports of functions to work, and retain their call signatures, as long as the function declaration merged with a namespace declaration—even if the namespace was empty. So while a module exporting a bare function was recognized as a “non-module entity”:

 ts ` declare function $ ( selector : string ): any ; export = $ ; // Cannot `import *` this 👍 `
 A should-be-meaningless change allowed the invalid import to type check without errors:

 ts ` declare namespace $ {} declare function $ ( selector : string ): any ; export = $ ; // Allowed to `import *` this and call it 😱 `

 Meanwhile, other transpilers were coming up with a way to solve the same problem. The thought process went something like this:

- To import a CJS module that exports a function or a primitive, we clearly need to use a default import. A namespace import would be illegal, and named imports don’t make sense here.

- Most likely, this means that runtimes implementing ESM/CJS interop will choose to make default imports of CJS modules always link directly to the whole `exports`, rather than only doing so if the `exports` is a function or primitive.

- So, a default import of a true CJS module should work just like a `require` call. But we’ll need a way to disambiguate true CJS modules from our transpiled CJS modules, so we can still transpile `export default "hello"` to `exports.default = "hello"` and have a default import of that module link to `exports.default`. Basically, a default import of one of our own transpiled modules needs to work one way (to simulate ESM-to-ESM imports), while a default import of any other existing CJS module needs to work another way (to simulate how we think ESM-to-CJS imports will work).

- When we transpile an ES module to CJS, let’s add a special extra field to the output:
 ts ` exports . A = {}; exports . B = {}; exports . default = "Hello, world!" ; // Extra special flag! exports . __esModule = true ; `
that we can check for when we transpile a default import:

```
 ts ` // import hello from "./module"; const _mod = require ( "./module" ); const hello = _mod . __esModule ? _mod . default : _mod ; `
```

 The `__esModule` flag first appeared in Traceur, then in Babel, SystemJS, and Webpack shortly after. TypeScript added the `allowSyntheticDefaultImports` in 1.8 to allow the type checker to link default imports directly to the `exports`, rather than the `exports.default`, of any module types that lacked an `export default` declaration. The flag didn’t modify how imports or exports were emitted, but it allowed default imports to reflect how other transpilers would treat them. Namely, it allowed a default import to be used to resolve to “non-module entities,” where `import *` was an error:

 ts ` // Error: import * as hello from "./exports-function" ; // Old workaround: import hello = require ( "./exports-function" ); // New way, with `allowSyntheticDefaultImports`: import hello from "./exports-function" ; `
 This was usually enough to let Babel and Webpack users write code that already worked in those systems without TypeScript complaining, but it was only a partial solution, leaving a few issues unsolved:

- Babel and others varied their default import behavior on whether an `__esModule` property was found on the target module, but `allowSyntheticDefaultImports` only enabled a fallback behavior when no default export was found in the target module’s types. This created an inconsistency if the target module had an `__esModule` flag but no default export. Transpilers and bundlers would still link a default import of such a module to its `exports.default`, which would be `undefined`, and would ideally be an error in TypeScript, since real ESM imports cause errors if they can’t be linked. But with `allowSyntheticDefaultImports`, TypeScript would think a default import of such an import links to the whole `exports` object, allowing named exports to be accessed as its properties.

- `allowSyntheticDefaultImports` didn’t change how namespace imports were typed, creating an odd inconsistency where both could be used and would have the same type:
 ts ` // @Filename: exportEqualsObject.d.ts declare const obj : object ; export = obj ; // @Filename: main.ts import objDefault from "./exportEqualsObject" ; import * as objNamespace from "./exportEqualsObject" ; // This should be true at runtime, but TypeScript gives an error: objNamespace . default === objDefault ; // ^^^^^^^ Property 'default' does not exist on type 'typeof import("./exportEqualsObject")'. `

- Most importantly, `allowSyntheticDefaultImports` did not change the JavaScript emitted by `tsc`. So while the flag enabled more accurate checking as long as the code was fed into another tool like Babel or Webpack, it created a real danger for users who were emitting `--module commonjs` with `tsc` and running in Node.js. If they encountered an error with `import *`, it may have appeared as if enabling `allowSyntheticDefaultImports` would fix it, but in fact it only silenced the build-time error while emitting code that would crash in Node.

 TypeScript introduced the `esModuleInterop` flag in 2.7, which refined the type checking of imports to address the remaining inconsistencies between TypeScript’s analysis and the interop behavior used in existing transpilers and bundlers, and critically, adopted the same `__esModule`-conditional CommonJS emit that transpilers had adopted years before. (Another new emit helper for `import *` ensured the result was always an object, with call signatures stripped, fully resolving the specification compliance issue that the aforementioned “resolves to a non-module entity” error didn’t quite sidestep.) Finally, with the new flag enabled, TypeScript’s type checking, TypeScript’s emit, and the rest of the transpiling and bundling ecosystem were in agreement on a CJS/ESM interop scheme that was spec-legal and, perhaps, plausibly adoptable by Node.

## Interop in Node.js

 Node.js shipped support for ES modules unflagged in v12. Like the bundlers and transpilers began doing years before, Node.js gave CommonJS modules a “synthetic default export” of their `exports` object, allowing the entire module contents to be accessed with a default import from ESM:

 ts ` // @Filename: export.cjs module . exports = { hello: "world" }; // @Filename: import.mjs import greeting from "./export.cjs" ; greeting . hello ; // "world" `
 That’s one win for seamless migration! Unfortunately, the similarities mostly end there.

### No `__esModule` detection (the “double default” problem)

 Node.js wasn’t able to respect the `__esModule` marker to vary its default import behavior. So a transpiled module with a “default export” behaves one way when “imported” by another transpiled module, and another way when imported by a true ES module in Node.js:

 ts ` // @Filename: node_modules/dependency/index.js exports . __esModule = true ; exports . default = function doSomething () { /*...*/ } // @Filename: transpile-vs-run-directly.{js/mjs} import doSomething from "dependency" ; // Works after transpilation, but not a function in Node.js ESM: doSomething (); // Doesn't exist after transpilation, but works in Node.js ESM: doSomething . default (); `
 While the transpiled default import only makes the synthetic default export if the target module lacks an `__esModule` flag, Node.js always synthesizes a default export, creating a “double default” on the transpiled module.

### Unreliable named exports

 In addition to making a CommonJS module’s `exports` object available as a default import, Node.js attempts to find properties of `exports` to make available as named imports. This behavior matches bundlers and transpilers when it works; however, Node.js uses syntactic analysis to synthesize named exports before any code executes, whereas transpiled modules resolve their named imports at runtime. The result is that imports from CJS modules that work in transpiled modules may not work in Node.js:

 ts ` // @Filename: named-exports.cjs exports . hello = "world" ; exports [ "worl" + "d" ] = "hello" ; // @Filename: transpile-vs-run-directly.{js/mjs} import { hello , world } from "./named-exports.cjs" ; // `hello` works, but `world` is missing in Node.js 💥 import mod from "./named-exports.cjs" ; mod . world ; // Accessing properties from the default always works ✅ `

### Cannot `require` a true ES module before Node.js v22

 True CommonJS modules can `require` an ESM-transpiled-to-CJS module, since they’re both CommonJS at runtime. But in Node.js versions older than v22.12.0, `require` crashes if it resolves to an ES module. This means published libraries cannot migrate from transpiled modules to true ESM without breaking their CommonJS (true or transpiled) consumers:

 ts ` // @Filename: node_modules/dependency/index.js export function doSomething () { /* ... */ } // @Filename: dependent.js import { doSomething } from "dependency" ; // ✅ Works if dependent and dependency are both transpiled // ✅ Works if dependent and dependency are both true ESM // ✅ Works if dependent is true ESM and dependency is transpiled // 💥 Crashes if dependent is transpiled and dependency is true ESM `

### Different module resolution algorithms

 Node.js introduced a new module resolution algorithm for resolving ESM imports that differed significantly from the long-standing algorithm for resolving `require` calls. While not directly related to interop between CJS and ES modules, this difference was one more reason why a seamless migration from transpiled modules to true ESM might not be possible:

 ts ` // @Filename: add.js export function add ( a , b ) { return a + b ; } // @Filename: math.js export * from "./add" ; // ^^^^^^^ // Works when transpiled to CJS, // but would have to be "./add.js" // in Node.js ESM. `

## Conclusions

 Clearly, a seamless migration from transpiled modules to ESM isn’t possible, at least in Node.js. Where does this leave us?

### Setting the right `module` compiler option is critical

 Since interoperability rules differ between hosts, TypeScript can’t offer correct checking behavior unless it understands what kind of module is represented by each file it sees, and what set of rules to apply to them. This is the purpose of the `module` compiler option. (In particular, code that is intended to run in Node.js is subject to stricter rules than code that will be processed by a bundler. The compiler’s output is not checked for Node.js compatibility unless `module` is set to `node16`, `node18`, or `nodenext`.)

### Applications with CommonJS code should always enable `esModuleInterop`

 In a TypeScript application (as opposed to a library that others may consume) where `tsc` is used to emit JavaScript files, whether `esModuleInterop` is enabled doesn’t have major consequences. The way you write imports for certain kinds of modules will change, but TypeScript’s checking and emit are in sync, so error-free code should be safe to run in either mode. The downside of leaving `esModuleInterop` disabled in this case is that it allows you to write JavaScript code with semantics that clearly violate the ECMAScript specification, confusing intuitions about namespace imports and making it harder to migrate to running ES modules in the future.

In an application that gets processed by a third-party transpiler or bundler, on the other hand, enabling `esModuleInterop` is more important. All major bundlers and transpilers use an `esModuleInterop`-like emit strategy, so TypeScript needs to adjust its checking to match. (The compiler always reasons about what will happen in the JavaScript files that `tsc` would emit, so even if another tool is being used in place of `tsc`, emit-affecting compiler options should still be set to match the output of that tool as closely as possible.)

`allowSyntheticDefaultImports` without `esModuleInterop` should be avoided. It changes the compiler’s checking behavior without changing the code emitted by `tsc`, allowing potentially unsafe JavaScript to be emitted. Additionally, the checking changes it introduces are an incomplete version of the ones introduced by `esModuleInterop`. Even if `tsc` isn’t being used for emit, it’s better to enable `esModuleInterop` than `allowSyntheticDefaultImports`.

Some people object to the inclusion of the `__importDefault` and `__importStar` helper functions included in `tsc`’s JavaScript output when `esModuleInterop` is enabled, either because it marginally increases the output size on disk or because the interop algorithm employed by the helpers seems to misrepresent Node.js’s interop behavior by checking for `__esModule`, leading to the hazards discussed earlier. Both of these objections can be addressed, at least partially, without accepting the flawed checking behavior exhibited with `esModuleInterop` disabled. First, the `importHelpers` compiler option can be used to import the helper functions from `tslib` rather than inlining them into each file that needs them. To discuss the second objection, let’s look at a final example:

 ts ` // @Filename: node_modules/transpiled-dependency/index.js exports . __esModule = true ; exports . default = function doSomething () { /* ... */ }; exports . something = "something" ; // @Filename: node_modules/true-cjs-dependency/index.js module . exports = function doSomethingElse () { /* ... */ }; // @Filename: src/sayHello.ts export default function sayHello () { /* ... */ } export const hello = "hello" ; // @Filename: src/main.ts import doSomething from "transpiled-dependency" ; import doSomethingElse from "true-cjs-dependency" ; import sayHello from "./sayHello.js" ; `
 Assume we’re compiling `src` to CommonJS for use in Node.js. Without `allowSyntheticDefaultImports` or `esModuleInterop`, the import of `doSomethingElse` from `"true-cjs-dependency"` is an error, and the others are not. To fix the error without changing any compiler options, you could change the import to `import doSomethingElse = require("true-cjs-dependency")`. However, depending on how the types for the module (not shown) are written, you may also be able to write and call a namespace import, which would be a language-level specification violation. With `esModuleInterop`, none of the imports shown are errors (and all are callable), but the invalid namespace import would be caught.

What would change if we decided to migrate `src` to true ESM in Node.js (say, add `"type": "module"` to our root package.json)? The first import, `doSomething` from `"transpiled-dependency"`, would no longer be callable—it exhibits the “double default” problem, where we’d have to call `doSomething.default()` rather than `doSomething()`. (TypeScript understands and catches this under `--module node16`—`nodenext`.) But notably, the second import of `doSomethingElse`, which needed `esModuleInterop` to work when compiling to CommonJS, works fine in true ESM.

If there’s something to complain about here, it’s not what `esModuleInterop` does with the second import. The changes it makes, both allowing the default import and preventing callable namespace imports, are exactly in line with Node.js’s real ESM/CJS interop strategy, and made migration to real ESM easier. The problem, if there is one, is that `esModuleInterop` seems to fail at giving us a seamless migration path for the first import. But this problem was not introduced by enabling `esModuleInterop`; the first import was completely unaffected by it. Unfortunately, this problem cannot be solved without breaking the semantic contract between `main.ts` and `sayHello.ts`, because the CommonJS output of `sayHello.ts` looks structurally identical to `transpiled-dependency/index.js`. If `esModuleInterop` changed the way the transpiled import of `doSomething` works to be identical to the way it would work in Node.js ESM, it would change the behavior of the `sayHello` import in the same way, making the input code violate ESM semantics (thus still preventing the `src` directory from being migrated to ESM without changes).

As we’ve seen, there is no seamless migration path from transpiled modules to true ESM. But `esModuleInterop` is one step in the right direction. For those who still prefer to minimize module syntax transformations and the inclusion of the import helper functions, enabling `verbatimModuleSyntax` is a better choice than disabling `esModuleInterop`. `verbatimModuleSyntax` enforces that the `import mod = require("mod")` and `export = ns` syntax be used in CommonJS-emitting files, avoiding all the kinds of import ambiguity we’ve discussed, at the cost of ease of migration to true ESM.

### Library code needs special considerations

 Libraries that ship as CommonJS should avoid using default exports, since the way those transpiled exports can be accessed varies between different tools and runtimes, and some of those ways will look confusing to users. A default export, transpiled to CommonJS by `tsc`, is accessible in Node.js as the default property of a default import:

 js ` import pkg from "pkg" ; pkg . default (); `
 in most bundlers or transpiled ESM as the default import itself:

 js ` import pkg from "pkg" ; pkg (); `
 and in vanilla CommonJS as the default property of a `require` call:

 js ` const pkg = require ( "pkg" ); pkg . default (); `
 Users will detect a misconfigured module smell if they have to access the `.default` property of a default import, and if they’re trying to write code that will run both in Node.js and a bundler, they might be stuck. Some third-party TypeScript transpilers expose options that change the way default exports are emitted to mitigate this difference, but they don’t produce their own declaration (`.d.ts`) files, so that creates a mismatch between the runtime behavior and the type checking, further confusing and frustrating users. Instead of using default exports, libraries that need to ship as CommonJS should use `export =` for modules that have a single main export, or named exports for modules that have multiple exports:

 diff ` - export default function doSomething() { /* ... */ } + export = function doSomething() { /* ... */ } `
 Libraries (that ship declaration files) should also take extra care to ensure the types they write are error-free under a wide range of compiler options. For example, it’s possible to write one interface that extends another in such a way that it only compiles successfully when `strictNullChecks` is disabled. If a library were to publish types like that, it would force all their users to disable `strictNullChecks` too. `esModuleInterop` can allow type declarations to contain similarly “infectious” default imports:

 ts ` // @Filename: /node_modules/dependency/index.d.ts import express from "express" ; declare function doSomething ( req : express . Request ): any ; export = doSomething ; `
 Suppose this default import only works with `esModuleInterop` enabled, and causes an error when a user without that option references this file. The user should probably enable `esModuleInterop` anyway, but it’s generally seen as bad form for libraries to make their configurations infectious like this. It would be much better for the library to ship a declaration file like:

 ts ` import express = require ( "express" ); // ... `
 Examples like this have led to conventional wisdom that says libraries should not enable `esModuleInterop`. This advice is a reasonable start, but we’ve looked at examples where the type of a namespace import changes, potentially introducing an error, when enabling `esModuleInterop`. So whether libraries compile with or without `esModuleInterop`, they run the risk of writing syntax that makes their choice infectious.

Library authors who want to go above and beyond to ensure maximum compatibility would do well to validate their declaration files against a matrix of compiler options. But using `verbatimModuleSyntax` completely sidesteps the issue with `esModuleInterop` by forcing CommonJS-emitting files to use CommonJS-style import and export syntax. Additionally, since `esModuleInterop` only affects CommonJS, as more libraries move to ESM-only publishing over time, the relevance of this issue will decline.

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: AB XZ DR K Last updated: Jun 15, 2026