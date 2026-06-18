# TypeScript - What's New


## Typescript 6 0

Was this page helpful?

# TypeScript 6.0

## Less Context-Sensitivity on `this`-less Functions

 When parameters don’t have explicit types written out, TypeScript can usually infer them based on an expected type, or even through other arguments in the same function call.

 ts ` declare function callIt < T >( obj : { produce : ( x : number ) => T , consume : ( y : T ) => void , }): void ; // Works, no issues. callIt ({ produce : ( x : number ) => x * 2 , consume : y => y . toFixed (), }); // Works, no issues even though the order of the properties is flipped. callIt ({ consume : y => y . toFixed (), produce : ( x : number ) => x * 2 , }); `
 Here, TypeScript can infer the type of `y` in the `consume` function based on the inferred `T` from the `produce` function, regardless of the order of the properties.
But what about if these functions were written using method syntax instead of arrow function syntax?

 ts ` declare function callIt < T >( obj : { produce : ( x : number ) => T , consume : ( y : T ) => void , }): void ; // Works fine, `x` is inferred to be a number. callIt ({ produce ( x : number ) { return x * 2 ; }, consume ( y ) { return y . toFixed (); }, }); callIt ({ consume ( y ) { return y . toFixed (); }, // ~ // error: 'y' is of type 'unknown'. produce ( x : number ) { return x * 2 ; }, }); `
 Strangely enough, the second call to `callIt` results in an error because TypeScript is not able to infer the type of `y` in the `consume` method.
What’s happening here is that when TypeScript is trying to find candidates for `T`, it will first skip over functions whose parameters don’t have explicit types.
It does this because certain functions may need the inferred type of `T` to be correctly checked - in our case, we need to know the type of `T` to analyze our `consume` function.

These functions are called contextually sensitive functions - basically, functions that have parameters without explicit types.
Eventually the type system will need to figure out types for these parameters - but this is a bit at odds with how inference works in generic functions because the two “pull” on types in different directions.

 ts ` function callFunc < T >( callback : ( x : T ) => void , value : T ) { return callback ( value ); } callFunc ( x => x . toFixed (), 42 ); // ^ // We need to figure out the type of `x` here, // but we also need to figure out the type of `T` to check the callback. `
 To solve this, TypeScript skips over contextually sensitive functions during type argument inference, and instead checks and infers from other arguments first.
If skipping over contextually sensitive functions doesn’t work, inference just continues across any unchecked arguments, going left-to-right in the argument list.
In the example immediately above, TypeScript will skip over the callback during inference for `T`, but will then look at the second argument, `42`, and infer that `T` is `number`.
Then, when it comes back to check the callback, it will have a contextual type of `(x: number) => void`, which allows it to infer that `x` is a `number` as well.

So what’s going on in our earlier examples?

 ts ` // Arrow syntax - no errors. callIt ({ consume : y => y . toFixed (), produce : ( x : number ) => x * 2 , }); // Method syntax - errors! callIt ({ consume ( y ) { return y . toFixed (); }, // ~ // error: 'y' is of type 'unknown'. produce ( x : number ) { return x * 2 ; }, }); `
 In both examples, `produce` is assigned a function with an explicitly-typed `x` parameter.
Shouldn’t they be checked identically?

The issue is subtle: most functions (like the ones using method syntax) have an implicit `this` parameter, but arrow functions do not.
Any usage of `this` could require “pulling” on the type of `T` - for example, knowing the type of the containing object literal could in turn require the type of `consume`, which uses `T`.

But we’re not using `this`!
Sure, the function might have a `this` value at runtime, but it’s never used!

TypeScript 6.0 takes this into account when it decides if a function is contextually sensitive or not.
If `this` is never actually used in a function, then it is not considered contextually sensitive.
That means these functions will be seen as higher-priority when it comes to type inference, and all of our examples above now work!

 This change was provided thanks to the work of Mateusz Burzyński .

## Subpath Imports Starting with `#/`

 When Node.js added support for modules, it added a feature called “subpath imports” .
This is basically a field called `imports` which allows packages to create internal aliases for modules within their package.

 json ` { "name" : "my-package" , "type" : "module" , "imports" : { "#root/*" : "./dist/*" } } `
 This allows modules in `my-package` to import from paths starting with `#root/`

 js ` import * as utils from "#root/utils.js" ; `
 instead of using a relative path like the following.

 js ` import * as utils from "../../utils.js" ; `
 One minor annoyance with this feature has been that developers always had to write something after the `#` when specifying a subpath import.
Here, we used `root`, but it is a bit useless since there is no directory we’re mapping over other than `./dist/`

Developers who have used bundlers are also accustomed to using path-mapping to avoid long relative paths.
A familiar convention with bundlers has been to use a simple `@/` as the prefix.
Unfortunately, subpath imports could not start with `#/` at all, leading to a lot of confusion for developers trying to adopt them in their projects.

But more recently, Node.js added support for subpath imports starting with `#/` .
This allows packages to use a simple `#/` prefix for their subpath imports without needing to add an extra segment.

 json ` { "name" : "my-package" , "type" : "module" , "imports" : { "#/*" : "./dist/*" } } `
 This is supported in newer Node.js 20 releases, and so TypeScript now supports it under the options `nodenext` and `bundler` for the `--moduleResolution` setting.

This work was done thanks to magic-akari , and the implementing pull request can be found here .

## Combining `--moduleResolution bundler` with `--module commonjs`

 TypeScript’s `--moduleResolution bundler` setting was previously only allowed to be used with `--module esnext` or `--module preserve`;
however, with the deprecation of `--moduleResolution node` (a.k.a. `--moduleResolution node10`), this new combination is often the most suitable upgrade path for many projects.

Projects will often want to instead plan out a migration towards either

- `--module preserve` and `--moduleResolution bundler`

- `--module nodenext`

depending on your project type (e.g. bundled web app, Bun app, or Node.js app).

More information can be found at this implementing pull request .

## The `--stableTypeOrdering` Flag

 As part of our ongoing work on TypeScript’s native port , we’ve introduced a new flag called `--stableTypeOrdering` intended to assist with 6.0-to-7.0 migrations.

Today, TypeScript assigns type IDs (internal tracking numbers) to types in the order they are encountered, and uses these IDs to sort union types in a consistent manner.
A similar process occurs for properties.
As a result, the order in which things are declared in a program can have possibly surprising effects on things like declaration emit.

For example, consider the declaration emit from this file:

 ts ` // Input: some-file.ts export function foo ( condition : boolean ) { return condition ? 100 : 500 ; } // Output: some-file.d.ts export declare function foo ( condition : boolean ): 100 | 500 ; // ^^^^^^^^^ // Note the order of this union: 100, then 500. `
 If we add an unrelated `const` above `foo`, the declaration emit changes:

 ts ` // Input: some-file.ts const x = 500 ; export function foo ( condition : boolean ) { return condition ? 100 : 500 ; } // Output: some-file.d.ts export declare function foo ( condition : boolean ): 500 | 100 ; // ^^^^^^^^^ // Note the change in order here. `
 This happens because the literal type `500` gets a lower type ID than `100` because it was processed first when analyzing the `const x` declaration.
In very rare cases this change in ordering can even cause errors to appear or disappear based on program processing order, but in general, the main place you might notice this ordering is in the emitted declaration files, or in the way types are displayed in your editor.

One of the major architectural improvements in TypeScript 7 is parallel type checking, which dramatically improves overall check time.
However, parallelism introduces a challenge: when different type-checkers visit nodes, types, and symbols in different orders, the internal IDs assigned to these constructs become non-deterministic.
This in turn leads to confusing non-deterministic output, where two files with identical contents in the same program can produce different declaration files, or even calculate different errors when analyzing the same file.
To fix this, TypeScript 7.0 sorts its internal objects (e.g. types and symbols) according to a deterministic algorithm based on the content of the object.
This ensures that all checkers encounter the same object order regardless of how and when they were created.
As a consequence, in the given example, TypeScript 7 will always print `100 | 500`, removing the ordering instability entirely.

This means that TypeScript 6 and 7 can and do sometimes display different ordering.
While these ordering changes are almost always benign, if you’re comparing compiler outputs between runs (for example, checking emitted declaration files in 6.0 vs 7.0), these different orderings can produce a lot of noise that makes it difficult to assess correctness.
Occasionally though, you may witness a change in ordering that causes a type error to appear or disappear, which can be even more confusing.

To help with this situation, in 6.0, you can specify the new `--stableTypeOrdering` flag.
This makes 6.0’s type ordering behavior match 7.0’s, reducing the number of differences between the two codebases.
Note that we don’t necessarily encourage using this flag all the time as it can add a substantial slowdown to type-checking (up to 25% depending on codebase).

If you encounter a type error using `--stableTypeOrdering`, this is typically due to inference differences.
The previous inference without `--stableTypeOrdering` happened to work based on the current ordering of types in your program.
To help with this, you’ll often benefit from providing an explicit type somewhere.
Often, this will be a type argument

 diff ` - someFunctionCall(/*...*/); + someFunctionCall<SomeExplicitType>(/*...*/); `
 or a variable annotation for an argument you intend to pass into a call.

 diff ` - const someVariable = { /*... some complex object ...*/ }; + const someVariable: SomeExplicitType = { /*... some complex object ...*/ }; someFunctionCall(someVariable); `
 Note that this flag is only intended to help diagnose differences between 6.0 and 7.0 - it is not intended to be used as a long-term feature

 See more at this pull-request .

## `es2025` option for `target` and `lib`

 TypeScript 6.0 adds support for the `es2025` option for both `target` and `lib`.
While there are no new JavaScript language features in ES2025, this new target adds new types for built-in APIs (e.g. `RegExp.escape`), and moves a few declarations from `esnext` into `es2025` (e.g. `Promise.try`, `Iterator` methods, and `Set` methods).
Work to enable the new target was contributed thanks to Kenta Moriuchi .

## New Types for `Temporal`

 The long-awaited Temporal proposal has reached stage 4 and will be part of a future ECMAScript standard.
TypeScript 6.0 now includes built-in types for the Temporal API, so you can start using it in your TypeScript code today via `--target esnext` or `"lib": ["esnext"]` (or the more-granular `esnext.temporal`).

 ts ` let yesterday = Temporal . Now . instant (). subtract ({ hours: 24 , }); let tomorrow = Temporal . Now . instant (). add ({ hours: 24 , }); console . log ( `Yesterday: ${ yesterday } ` ); console . log ( `Tomorrow: ${ tomorrow } ` ); `
 Temporal is already usable in several runtimes, and with stage 4 status it is now officially part of the JavaScript language.
 Documentation on the Temporal APIs is available on MDN .

 This work was contributed thanks to GitHub user Renegade334 .

## New Types for “upsert” Methods (a.k.a. `getOrInsert`)

 A common pattern with `Map`s is to check if a key exists, and if not, set and fetch a default value.

 ts ` function processOptions ( compilerOptions : Map < string , unknown >) { let strictValue : unknown ; if ( compilerOptions . has ( "strict" )) { strictValue = compilerOptions . get ( "strict" ); } else { strictValue = true ; compilerOptions . set ( "strict" , strictValue ); } // ... } `
 This pattern can be tedious.
 ECMAScript’s “upsert” proposal recently reached stage 4, and introduces 2 new methods on `Map` and `WeakMap`:

- `getOrInsert`

- `getOrInsertComputed`

These methods have been added to the `esnext` lib so that you can start using them immediately in TypeScript 6.0.

With `getOrInsert`, we can replace our code above with the following:

 ts ` function processOptions ( compilerOptions : Map < string , unknown >) { let strictValue = compilerOptions . getOrInsert ( "strict" , true ); // ... } `
 `getOrInsertComputed` works similarly, but is for cases where the default value may be expensive to compute (e.g. requires lots of computations, allocations, or does long-running synchronous I/O).
Instead, it takes a callback that will only be called if the key is not already present.

 ts ` someMap . getOrInsertComputed ( "someKey" , () => { return computeSomeExpensiveValue ( /*...*/ ); }); `
 This callback is also given the key as an argument, which can be useful for cases where the default value is based on the key.

 ts ` someMap . getOrInsertComputed ( someKey , computeSomeExpensiveDefaultValue ); function computeSomeExpensiveValue ( key : string ) { // ... } `
 This update was contributed thanks to GitHub user Renegade334 .

## `RegExp.escape`

 When constructing some literal string to match within a regular expression, it is important to escape special regular expression characters like `*`, `+`, `?`, `(`, `)`, etc.
The RegExp Escaping ECMAScript proposal has reached stage 4, and introduces a new `RegExp.escape` function that takes care of this for you.

 ts ` function matchWholeWord ( word : string , text : string ) { const escapedWord = RegExp . escape ( word ); const regex = new RegExp ( ` \\ b ${ escapedWord } \\ b` , "g" ); return text . match ( regex ); } `
 `RegExp.escape` is available in the `es2025` lib, so you can start using it in TypeScript 6.0 today.

 This work was contributed thanks Kenta Moriuchi .

## The `dom` lib Now Contains `dom.iterable` and `dom.asynciterable`

 TypeScript’s `lib` option allows you to specify which global declarations your target runtime has.
One option is `dom` to represent web environments (i.e. browsers, who implement the DOM APIs ).
Previously, the DOM APIs were partially split out into `dom.iterable` and `dom.asynciterable` for environments that didn’t support `Iterable`s and `AsyncIterable`s.
This meant that you had to explicitly add `dom.iterable` to use iteration methods on DOM collections like `NodeList` or `HTMLCollection`.

In TypeScript 6.0, the contents of `lib.dom.iterable.d.ts` and `lib.dom.asynciterable.d.ts` are fully included in `lib.dom.d.ts`.
You can still reference `dom.iterable` and `dom.asynciterable` in your configuration file’s `"lib"` array, but they are now just empty files.

 ts ` // Before TypeScript 6.0, this required "lib": ["dom", "dom.iterable"] // Now it works with just "lib": ["dom"] for ( const element of document . querySelectorAll ( "div" )) { console . log ( element . textContent ); } `
 This is a quality-of-life improvement that eliminates a common point of confusion, since no major modern browser lacks these capabilities.
If you were already including both `dom` and `dom.iterable`, you can now simplify to just `dom`.

See more at this issue and its corresponding pull request .

## Breaking Changes and Deprecations in TypeScript 6.0

 TypeScript 6.0 arrives as a significant transition release, designed to prepare developers for TypeScript 7.0, the upcoming native port of the TypeScript compiler.
While TypeScript 6.0 maintains full compatibility with your existing TypeScript knowledge and continues to be API compatible with TypeScript 5.9, this release introduces a number of breaking changes and deprecations that reflect the evolving JavaScript ecosystem and set the stage for TypeScript 7.0.

In the two years since TypeScript 5.0, we’ve seen ongoing shifts in how developers write and ship JavaScript:

- Virtually every runtime environment is now “evergreen”. True legacy environments (ES5) are vanishingly rare.

- Bundlers and ESM have become the most common module targets for new projects, though CommonJS remains a major target. AMD and other in-browser userland module systems are much rarer than they were in 2012.

- Almost all packages can be consumed through some module system. UMD packages still exist, but virtually no new code is available only as a global variable.

- `tsconfig.json` is nearly universal as a configuration mechanism.

- Appetite for “stricter” typing continues to grow.

- TypeScript build performance is top of mind. Despite the gains of TypeScript 7, performance must always remain a key goal, and options which can’t be supported in a performant way need to be more strongly justified.

So TypeScript 6.0 and 7.0 are designed with these realities in mind.
For TypeScript 6.0, these deprecations can be ignored by setting `"ignoreDeprecations": "6.0"` in your tsconfig; however, note that TypeScript 7.0 will not support any of these deprecated options.

Some necessary adjustments can be automatically performed with a codemod or tool.
For example, the experimental `ts5to6` tool can automatically adjust `baseUrl` and `rootDir` across your codebase.

### Up-Front Adjustments

 We’ll cover specific adjustments below, but we have to note that some deprecations and behavior changes do not necessarily have an error message that directly points to the underlying issue.
So we’ll note up-front that many projects will need to do at least one of the following :

-
Set the `"types"` array in tsconfig, typically to `"types": ["node"]`.

`"types": ["*"]` will restore the 5.9 behavior, but we recommend using an explicit array to improve build performance and predictability.

You’ll typically know this is the issue if you see a lot of type errors related to missing identifiers or unresolved built-in modules.

-
Set `"rootDir": "./src"` if you were previously relying on this being inferred

You’ll often know this is the issue if you see files being written to `./dist/src/index.js` instead of `./dist/index.js`.

### Simple Default Changes

 Several compiler options now have updated default values that better reflect modern development practices.

-
 `strict` is now `true` by default :
The appetite for stricter typing continues to grow, and we’ve found that most new projects want `strict` mode enabled.
If you were already using `"strict": true`, nothing changes for you.
If you were relying on the previous default of `false`, you’ll need to explicitly set `"strict": false` in your `tsconfig.json`.

-
 `module` defaults to `esnext` :
Similarly, the new default `module` is `esnext`, acknowledging that ESM is now the dominant module format.

-
 `target` defaults to current-year ES version :
The new default `target` is the most recent supported ECMAScript spec version (effectively a floating target).
Right now, that target is `es2025`.
This reflects the reality that most developers are shipping to evergreen runtimes and don’t need to compile down to older ECMAScript versions.

-
 `noUncheckedSideEffectImports` is now `true` by default :
This helps catch issues with typos in side-effect-only imports.

-
 `libReplacement` is now `false` by default :
This flag previously incurred a large number of failed module resolutions for every run, which in turn increased the number of locations we needed to watch under `--watch` and editor scenarios.
In a new project, `libReplacement` never does anything until other explicit configuration takes place, so it makes sense to turn this off by default for the sake of better performance by default.

If these new defaults break your project, you can specify the previous values explicitly in your `tsconfig.json`.

### `rootDir` now defaults to `.`

 `rootDir` controls the directory structure of your output files relative to the output directory.
Previously, if you did not specify a `rootDir`, it was inferred based on the common directory of all non-declaration input files.
But this often meant that it was impossible to know if a file belonged to a project without trying to load and parse that project.
It also meant that TypeScript had to spend more time inferring that common source directory by analyzing every file path in the program.

In TypeScript 6.0, the default `rootDir` will always be the directory containing the `tsconfig.json` file.
`rootDir` will only be inferred when using `tsc` from the command line without a `tsconfig.json` file.

If you have source files any level deeper than your `tsconfig.json` directory and were relying on TypeScript to infer a common root directory for source files, you’ll need to explicitly set `rootDir`:

 diff ` { "compilerOptions": { // ... + "rootDir": "./src" }, "include": ["./src"] } `
 Likewise, if your `tsconfig.json` referenced files outside of the containing `tsconfig.json`, you would need to adjust your `rootDir` to include those files.

 diff ` { "compilerOptions": { // ... + "rootDir": "../src" }, "include": ["../src/**/*.tests.ts"] } `
 See more at the discussion here and the implementation here .

### `types` now defaults to `[]`

 In a `tsconfig.json`, the `types` field of `compilerOptions` specifies a list of package names to be included in the global scope during compilation.
Typically, packages in `node_modules` are automatically included via imports in your source code;
but for convenience, TypeScript would also include all packages in `node_modules/@types` by default, so that you can get global declarations like `process` or the `"fs"` module from `@types/node`, or `describe` and `it` from `@types/jest`, without needing to import them directly.

In a sense, the `types` value previously defaulted to “enumerate everything in `node_modules/@types`”.
This can be very expensive, as a normal repository setup these days might transitively pull in hundreds of `@types` packages, especially in multi-project workspaces with flattened `node_modules`.
Modern projects almost always need only `@types/node`, `@types/jest`, or a handful of other common global-affecting packages.

In TypeScript 6.0, the default `types` value will be `[]` (an empty array).
This change prevents projects from unintentionally pulling in hundreds or even thousands of unneeded declaration files at build time.
Many projects we’ve looked at have improved their build time anywhere from 20-50% just by setting `types` appropriately.

 This will affect many projects. You will likely need to add `"types": ["node"]` or a few others:

 diff ` { "compilerOptions": { // Explicitly list the @types packages you need + "types": ["node", "jest"] } } `
 You can also specify a `*` entry to re-enable the old enumeration behavior:

 diff ` { "compilerOptions": { // Load ALL the types - the default from TypeScript 5.9 and before. + "types": ["*"] } } `
 If you end up with new error messages like the following:

 ` Cannot find module '...' or its corresponding type declarations. Cannot find name 'fs'. Do you need to install type definitions for node? Try `npm i --save-dev @types/node` and then add 'node' to the types field in your tsconfig. Cannot find name 'path'. Do you need to install type definitions for node? Try `npm i --save-dev @types/node` and then add 'node' to the types field in your tsconfig. Cannot find name 'process'. Do you need to install type definitions for node? Try `npm i --save-dev @types/node` and then add 'node' to the types field in your tsconfig. Cannot find name 'Bun'. Do you need to install type definitions for Bun? Try `npm i --save-dev @types/bun` and then add 'bun' to the types field in your tsconfig. Cannot find name 'describe'. Do you need to install type definitions for a test runner? Try `npm i --save-dev @types/jest` or `npm i --save-dev @types/mocha` and then add 'jest' or 'mocha' to the types field in your tsconfig. `
 it’s likely that you need to add some entries to your `types` field.

See more at the proposal here along with the implementing pull request here .

### Deprecated: `target: es5`

 The ECMAScript 5 target was important for a long time to support legacy browsers; but its successor, ECMAScript 2015 (ES6), was released over a decade ago, and all modern browsers have supported it for many years.
With Internet Explorer’s retirement, and the universality of evergreen browsers, there are very few use cases for ES5 output today.

TypeScript’s lowest target will now be ES2015, and the `target: es5` option is deprecated. If you were using `target: es5`, you’ll need to migrate to a newer target or use an external compiler.
If you still need ES5 output, we recommend using an external compiler to either directly compile your TypeScript source, or to post-process TypeScript’s outputs.

 See more about this deprecation here along with its implementing pull request .

### Deprecated: `--downlevelIteration`

 `--downlevelIteration` only has effects on ES5 emit, and since `--target es5` has been deprecated, `--downlevelIteration` no longer serves a purpose.

Subtly, using `--downlevelIteration false` with `--target es2015` did not error in TypeScript 5.9 and earlier, even though it had no effect.
In TypeScript 6.0, setting `--downlevelIteration` at all will lead to a deprecation error.

See the implementation here .

### Deprecated: `--moduleResolution node` (a.k.a. `--moduleResolution node10`)

 `--moduleResolution node` encoded a specific version of Node.js’s module resolution algorithm that most-accurately reflected the behavior of Node.js 10.
Unfortunately, this target (and its name) ignores many updates to Node.js’s resolution algorithm that have occurred since then, and it is no longer a good representation of the behavior of modern Node.js versions.

In TypeScript 6.0, `--moduleResolution node` (specifically, `--moduleResolution node10`) is deprecated.
Users who were using `--moduleResolution node` should usually migrate to `--moduleResolution nodenext` if they plan on targeting Node.js directly, or `--moduleResolution bundler` if they plan on using a bundler or Bun.

See more at this issue and its corresponding pull request .

### Deprecated: `amd`, `umd`, and `systemjs` values of `module`

 The following flag values are no longer supported

- `--module amd`

- `--module umd`

- `--module systemjs`

- `--module none`

AMD, UMD, and SystemJS were important during the early days of JavaScript modules when browsers lacked native module support.
The semantics of “none” were never well-defined and often led to confusion.
Today, ESM is universally supported in browsers and Node.js, and both import maps and bundlers have become favored ways for filling in the gaps.
If you’re still targeting these module systems, consider migrating to an appropriate ECMAScript module-emitting target, adopt a bundler or different compiler, or stay on TypeScript 5.x until you can migrate.

This also implies dropped support for the `amd-module` directive, which will no longer have any effect.

See more at the proposal issue along with the implementing pull request .

### Deprecated: `--baseUrl`

 The `baseUrl` option is most-commonly used in conjunction with `paths`, and is typically used as a prefix for every value in `paths`.
Unfortunately, `baseUrl` is also considered a look-up root for module resolution.

For example, given the following `tsconfig.json`

 json ` { "compilerOptions" : { // ... "baseUrl" : "./src" , "paths" : { "@app/*" : [ "app/*" ], "@lib/*" : [ "lib/*" ] } } } `
 and an import like

 ts ` import * as someModule from "someModule.js" ; `
 TypeScript will probably resolve this to `src/someModule.js`, even if the developer only intended to add mappings for modules starting with `@app/` and `@lib/`.

In the best case, this also often leads to “worse-looking” paths that bundlers would ignore;
but it often meant that that many import paths that would never have worked at runtime are considered “just fine” by TypeScript.

`path` mappings have not required specifying `baseUrl` for a long time, and in practice, most projects that use `baseUrl` only use it as a prefix for their `paths` entries.
In TypeScript 6.0, `baseUrl` is deprecated and will no longer be considered a look-up root for module resolution.

Developers who used `baseUrl` as a prefix for path-mapping entries can simply remove `baseUrl` and add the prefix to their `paths` entries:

 diff ` { "compilerOptions": { // ... - "baseUrl": "./src", "paths": { - "@app/*": ["app/*"], - "@lib/*": ["lib/*"] + "@app/*": ["./src/app/*"], + "@lib/*": ["./src/lib/*"] } } } `
 Developers who actually did use `baseUrl` as a look-up root can also add an explicit path mapping to preserve the old behavior:

 json ` { "compilerOptions" : { // ... "paths" : { // A new catch-all that replaces the baseUrl: "*" : [ "./src/*" ], // Every other path now has an explicit common prefix: "@app/*" : [ "./src/app/*" ], "@lib/*" : [ "./src/lib/*" ], } } } `
 However, this is extremely rare.
We recommend most developers simply remove `baseUrl` and add the appropriate prefixes to their `paths` entries.

See more at this issue and the corresponding pull request .

### Deprecated: `--moduleResolution classic`

 The `moduleResolution: classic` setting has been removed.
The `classic` resolution strategy was TypeScript’s original module resolution algorithm, and predates Node.js’s resolution algorithm becoming a de facto standard.
Today, all practical use cases are served by `nodenext` or `bundler`.
If you were using `classic`, migrate to one of these modern resolution strategies.

See more at this issue and the implementing pull request .

### Deprecated: `--esModuleInterop false` and `--allowSyntheticDefaultImports false`

 The following settings can no longer be set to `false`:

- `esModuleInterop`

- `allowSyntheticDefaultImports`

`esModuleInterop` and `allowSyntheticDefaultImports` were originally opt-in to avoid breaking existing projects.
However, the behavior they enable has been the recommended default for years.
Setting them to `false` often led to subtle runtime issues when consuming CommonJS modules from ESM.
In TypeScript 6.0, the safer interop behavior is always enabled.

If you have imports that rely on the old behavior, you may need to adjust them:

 ts ` // Before (with esModuleInterop: false) import * as express from "express" ; // After (with esModuleInterop always enabled) import express from "express" ; `
 See more at this issue and its implementing pull request .

### Deprecated: `--alwaysStrict false`

 The `alwaysStrict` flag refers to inference and emit of the `"use strict";` directive.
In TypeScript 6.0, all code will be assumed to be in JavaScript strict mode , which is a set of JS semantics that most-noticeably affects syntactic corner cases around reserved words.
If you have “sloppy mode” code that uses reserved words like `await`, `static`, `private`, or `public` as regular identifiers, you’ll need to rename them.
If you relied on subtle semantics around the meaning of `this` in non-strict code, you may need to adjust your code as well.

See more at this issue and its corresponding pull request .

### Deprecated: `outFile`

 The `--outFile` option has been removed from TypeScript 6.0. This option was originally designed to concatenate multiple input files into a single output file. However, external bundlers like Webpack, Rollup, esbuild, Vite, Parcel, and others now do this job faster, better, and with far more configurability. Removing this option simplifies the implementation and allows us to focus on what TypeScript does best: type-checking and declaration emit. If you’re currently using `--outFile`, you’ll need to migrate to an external bundler. Most modern bundlers have excellent TypeScript support out of the box.

### Deprecated: legacy `module` Syntax for namespaces

 Early versions of TypeScript used the `module` keyword to declare namespaces:

 ts ` // ❌ Deprecated syntax - now an error module Foo { export const bar = 10 ; } `
 This syntax was later aliased to the modern preferred form using the `namespace` keyword:

 ts ` // ✅ The correct syntax namespace Foo { export const bar = 10 ; } `
 When `namespace` was introduced, the `module` syntax was simply discouraged.
A few years ago, the TypeScript language service started marking the keyword as deprecated, suggesting `namespace` in its place.

In TypeScript 6.0, using `module` where `namespace` is expected is now a hard deprecation.
This change is necessary because `module` blocks are a potential ECMAScript proposal that would conflict with the legacy TypeScript syntax.

The ambient module declaration form remains fully supported:

 ts ` // ✅ Still works perfectly declare module "some-module" { export function doSomething (): void ; } `
 See this issue and its corresponding pull request for more details.

### Deprecated: `asserts` Keyword on Imports

 The `asserts` keyword was proposed to the JavaScript language via the import assertions proposal;
however, the proposal eventually morphed into the import attributes proposal , which uses the `with` keyword instead of `asserts`.

Thus, the `asserts` syntax is now deprecated in TypeScript 6.0, and using it will lead to an error:

 ts ` // ❌ Deprecated syntax - now an error. import blob from "./blahb.json" asserts { type : " json " } // ~~~~~~~ // error: Import assertions have been replaced by import attributes. Use 'with' instead of 'asserts'. `
 Instead, use the `with` syntax for import attributes:

 ts ` // ✅ Works with the new import attributes syntax. import blob from "./blahb.json" with { type : " json " } `
 See more at this issue and its corresponding pull request .

### Deprecated: `no-default-lib` Directives

 The `/// &#x3C;reference no-default-lib="true"/>` directive has been largely misunderstood and misused.
In TypeScript 6.0, this directive is no longer supported.
If you were using it, consider using `--noLib` or `--libReplacement` instead.

 See more here and at the corresponding pull request .

### Specifying Command-Line Files When `tsconfig.json` Exists is Now an Error

 Currently, if you run `tsc foo.ts` in a folder where a `tsconfig.json` exists, the config file is completely ignored.
This was often very confusing if you expected checking and emit options to apply to the input file.

In TypeScript 6.0, if you run `tsc` with file arguments in a directory containing a `tsconfig.json`, an error will be issued to make this behavior explicit:

 ` error TS5112: tsconfig.json is present but will not be loaded if files are specified on commandline. Use '--ignoreConfig' to skip this error. `
 If it is the case that you wanted to ignore the `tsconfig.json` and just compile `foo.ts` with TypeScript’s defaults, you can use the new `--ignoreConfig` flag.

 sh ` tsc --ignoreConfig foo.ts `
 See more at this issue and its corresponding pull request .

## Preparing for TypeScript 7.0

 TypeScript 6.0 is designed as a transition release.
While options deprecated in TypeScript 6.0 will continue to work without errors when `"ignoreDeprecations": "6.0"` is set, those options will be removed entirely in TypeScript 7.0 (the native TypeScript port).
If you’re seeing deprecation warnings after upgrading to TypeScript 6.0, we strongly recommend addressing them before adopting TypeScript 7.0 (or trying native previews ) in your project.
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: JB Last updated: Jun 15, 2026

## Typescript 5 9

Was this page helpful?

# TypeScript 5.9

## Minimal and Updated `tsc --init`

 For a while, the TypeScript compiler has supported an `--init` flag that can create a `tsconfig.json` within the current directory.
In the last few years, running `tsc --init` created a very “full” `tsconfig.json`, filled with commented-out settings and their descriptions.
We designed this with the intent of making options discoverable and easy to toggle.

However, given external feedback (and our own experience), we found it’s common to immediately delete most of the contents of these new `tsconfig.json` files.
When users want to discover new options, we find they rely on auto-complete from their editor, or navigate to the tsconfig reference on our website (which the generated `tsconfig.json` links to!).
What each setting does is also documented on that same page, and can be seen via editor hovers/tooltips/quick info.
While surfacing some commented-out settings might be helpful, the generated `tsconfig.json` was often considered overkill.

We also felt that it was time that `tsc --init` initialized with a few more prescriptive settings than we already enable.
We looked at some common pain points and papercuts users have when they create a new TypeScript project.
For example, most users write in modules (not global scripts), and `--moduleDetection` can force TypeScript to treat every implementation file as a module.
Developers also often want to use the latest ECMAScript features directly in their runtime, so `--target` can typically be set to `esnext`.
JSX users often find that going back to set `--jsx` is needless friction, and its options are slightly confusing.
And often, projects end up loading more declaration files from `node_modules/@types` than TypeScript actually needs; but specifying an empty `types` array can help limit this.

In TypeScript 5.9, a plain `tsc --init` with no other flags will generate the following `tsconfig.json`:

 json ` { // Visit https://aka.ms/tsconfig to read more about this file "compilerOptions" : { // File Layout // "rootDir": "./src", // "outDir": "./dist", // Environment Settings // See also https://aka.ms/tsconfig_modules "module" : "nodenext" , "target" : "esnext" , "types" : [], // For nodejs: // "lib": ["esnext"], // "types": ["node"], // and npm install -D @types/node // Other Outputs "sourceMap" : true , "declaration" : true , "declarationMap" : true , // Stricter Typechecking Options "noUncheckedIndexedAccess" : true , "exactOptionalPropertyTypes" : true , // Style Options // "noImplicitReturns": true, // "noImplicitOverride": true, // "noUnusedLocals": true, // "noUnusedParameters": true, // "noFallthroughCasesInSwitch": true, // "noPropertyAccessFromIndexSignature": true, // Recommended Options "strict" : true , "jsx" : "react-jsx" , "verbatimModuleSyntax" : true , "isolatedModules" : true , "noUncheckedSideEffectImports" : true , "moduleDetection" : "force" , "skipLibCheck" : true , } } `
 For more details, see the implementing pull request and discussion issue .

## Support for `import defer`

 TypeScript 5.9 introduces support for ECMAScript’s deferred module evaluation proposal using the new `import defer` syntax.
This feature allows you to import a module without immediately executing the module and its dependencies, providing better control over when work and side-effects occur.

The syntax only permits namespace imports:

 ts ` import defer * as feature from "./some-feature.js" ; `
 The key benefit of `import defer` is that the module is only evaluated when one of its exports is first accessed.
Consider this example:

 ts ` // ./some-feature.ts initializationWithSideEffects (); function initializationWithSideEffects () { // ... specialConstant = 42 ; console . log ( "Side effects have occurred!" ); } export let specialConstant : number ; `
 When using `import defer`, the `initializationWithSideEffects()` function will not be called until you actually access a property of the imported namespace:

 ts ` import defer * as feature from "./some-feature.js" ; // No side effects have occurred yet // ... // As soon as `specialConstant` is accessed, the contents of the `feature` // module are run and side effects have taken place. console . log ( feature . specialConstant ); // 42 `
 Because evaluation of the module is deferred until you access a member off of the module, you cannot use named imports or default imports with `import defer`:

 ts ` // ❌ Not allowed import defer { doSomething } from "some-module" ; // ❌ Not allowed import defer defaultExport from "some-module" ; // ✅ Only this syntax is supported import defer * as feature from "some-module" ; `
 Note that when you write `import defer`, the module and its dependencies are fully loaded and ready for execution.
That means that the module will need to exist, and will be loaded from the file system or a network resource.
The key difference between a regular `import` and `import defer` is that the execution of statements and declarations is deferred until you access a property of the imported namespace.

This feature is particularly useful for conditionally loading modules with expensive or platform-specific initialization. It can also improve startup performance by deferring module evaluation for app features until they are actually needed.

Note that `import defer` is not transformed or “downleveled” at all by TypeScript.
It is intended to be used in runtimes that support the feature natively, or by tools such as bundlers that can apply the appropriate transformation.
That means that `import defer` will only work under the `--module` modes `preserve` and `esnext`.

We’d like to extend our thanks to Nicolò Ribaudo who championed the proposal in TC39 and also provided the implementation for this feature .

## Support for `--module node20`

 TypeScript provides several `node*` options for the `--module` and `--moduleResolution` settings.
Most recently, `--module nodenext` has supported the ability to `require()` ECMAScript modules from CommonJS modules, and correctly rejects import assertions (in favor of the standards-bound import attributes ).

TypeScript 5.9 brings a stable option for these settings called `node20`, intended to model the behavior of Node.js v20.
This option is unlikely to have new behaviors in the future, unlike `--module nodenext` or `--moduleResolution nodenext`.
Also unlike `nodenext`, specifying `--module node20` will imply `--target es2023` unless otherwise configured.
`--module nodenext`, on the other hand, implies the floating `--target esnext`.

For more information, take a look at the implementation here .

## Summary Descriptions in DOM APIs

 Previously, many of the DOM APIs in TypeScript only linked to the MDN documentation for the API.
These links were useful, but they didn’t provide a quick summary of what the API does.
Thanks to a few changes from Adam Naji , TypeScript now includes summary descriptions for many DOM APIs based on the MDN documentation.
You can see more of these changes here and here .

## Expandable Hovers (Preview)

 Quick Info (also called “editor tooltips” and “hovers”) can be very useful for peeking at variables to see their types, or at type aliases to see what they actually refer to.
Still, it’s common for people to want to go deeper and get details from whatever’s displayed within the quick info tooltip.
For example, if we hover our mouse over the parameter `options` in the following example:

 ts ` export function drawButton ( options : Options ): void `
 We’re left with `(parameter) options: Options`.

Do we really need to jump to the definition of the type `Options` just to see what members this value has?

Previously, that was actually the case.
To help here, TypeScript 5.9 is now previewing a feature called expandable hovers , or “quick info verbosity”.
If you use an editor like VS Code, you’ll now see a `+` and `-` button on the left of these hover tooltips.
Clicking on the `+` button will expand out types more deeply, while clicking on the `-` button will collapse to the last view.

This feature is currently in preview, and we are seeking feedback for both TypeScript and our partners on Visual Studio Code.
For more details, see the PR for this feature here .

## Configurable Maximum Hover Length

 Occasionally, quick info tooltips can become so long that TypeScript will truncate them to make them more readable.
The downside here is that often the most important information will be omitted from the hover tooltip, which can be frustrating.
To help with this, TypeScript 5.9’s language server supports a configurable hover length, which can be configured in VS Code via the `js/ts.hover.maximumLength` setting.

Additionally, the new default hover length is substantially larger than the previous default.
This means that in TypeScript 5.9, you should see more information in your hover tooltips by default.
For more details, see the PR for this feature here and the corresponding change to Visual Studio Code here .

## Optimizations

### Cache Instantiations on Mappers

 When TypeScript replaces type parameters with specific type arguments, it can end up instantiating many of the same intermediate types over and over again.
In complex libraries like Zod and tRPC, this could lead to both performance issues and errors reported around excessive type instantiation depth.
Thanks to a change from Mateusz Burzyński , TypeScript 5.9 is able to cache many intermediate instantiations when work has already begun on a specific type instantiation.
This in turn avoids lots of unnecessary work and allocations.

### Avoiding Closure Creation in `fileOrDirectoryExistsUsingSource`

 In JavaScript, a function expression will typically allocate a new function object, even if the wrapper function is just passing through arguments to another function with no captured variables.
In code paths around file existence checks, Vincent Bailly found examples of these pass-through function calls, even though the underlying functions only took single arguments.
Given the number of existence checks that could take place in larger projects, he cited a speed-up of around 11%.
 See more on this change here .

## Notable Behavioral Changes

### `lib.d.ts` Changes

 Types generated for the DOM may have an impact on type-checking your codebase.

Additionally, one notable change is that `ArrayBuffer` has been changed in such a way that it is no longer a supertype of several different `TypedArray` types.
This also includes subtypes of `UInt8Array`, such as `Buffer` from Node.js.
As a result, you’ll see new error messages such as:

 ` error TS2345: Argument of type 'ArrayBufferLike' is not assignable to parameter of type 'BufferSource'. error TS2322: Type 'ArrayBufferLike' is not assignable to type 'ArrayBuffer'. error TS2322: Type 'Buffer' is not assignable to type 'Uint8Array<ArrayBufferLike>'. error TS2322: Type 'Buffer' is not assignable to type 'ArrayBuffer'. error TS2345: Argument of type 'Buffer' is not assignable to parameter of type 'string | Uint8Array<ArrayBufferLike>'. `
 If you encounter issues with `Buffer`, you may first want to check that you are using the latest version of the `@types/node` package.
This might include running

 ` npm update @types/node --save-dev `
 Much of the time, the solution is to specify a more specific underlying buffer type instead of using the default `ArrayBufferLike` (i.e. explicitly writing out `Uint8Array&#x3C;ArrayBuffer>` rather than a plain `Uint8Array`).
In instances where some `TypedArray` (like `Uint8Array`) is passed to a function expecting an `ArrayBuffer` or `SharedArrayBuffer`, you can also try accessing the `buffer` property of that `TypedArray` like in the following example:

 diff ` let data = new Uint8Array([0, 1, 2, 3, 4]); - someFunc(data) + someFunc(data.buffer) `

## Type Argument Inference Changes

 In an effort to fix “leaks” of type variables during inference, TypeScript 5.9 may introduce changes in types and possibly new errors in some codebases.
These are hard to predict, but can often be fixed by adding type arguments to generic functions calls.
 See more details here .
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: JB Last updated: Jun 15, 2026

## Typescript 5 8

Was this page helpful?

# TypeScript 5.8

## Granular Checks for Branches in Return Expressions

 Consider some code like the following:

 ts ` declare const untypedCache : Map < any , any >; function getUrlObject ( urlString : string ): URL { return untypedCache . has ( urlString ) ? untypedCache . get ( urlString ) : urlString ; } `
 The intent of this code is to retrieve a URL object from a cache if it exists, or to create a new URL object if it doesn’t.
However, there’s a bug: we forgot to actually construct a new URL object with the input.
Unfortunately, TypeScript generally didn’t catch this sort of bug.

When TypeScript checks conditional expressions like `cond ? trueBranch : falseBranch`, its type is treated as a union of the types of the two branches.
In other words, it gets the type of `trueBranch` and `falseBranch`, and combines them into a union type.
In this case, the type of `untypedCache.get(urlString)` is `any`, and the type of `urlString` is `string`.
This is where things go wrong because `any` is so infectious in how it interacts with other types.
The union `any | string` is simplified to `any`, so by the time TypeScript starts checking whether the expression in our `return` statement is compatible with the expected return type of `URL`, the type system has lost any information that would have caught the bug in this code.

In TypeScript 5.8, the type system special-cases conditional expressions directly inside `return` statements.
Each branch of the conditional is checked against the declared return type of the containing functions (if one exists), so the type system can catch the bug in the example above.

 ts ` declare const untypedCache : Map < any , any >; function getUrlObject ( urlString : string ): URL { return untypedCache . has ( urlString ) ? untypedCache . get ( urlString ) : urlString ; // ~~~~~~~~~ // error! Type 'string' is not assignable to type 'URL'. } `
 This change was made within this pull request , as part of a broader set of future improvements for TypeScript.

## Support for `require()` of ECMAScript Modules in `--module nodenext`

 For years, Node.js supported ECMAScript modules (ESM) alongside CommonJS modules.
Unfortunately, the interoperability between the two had some challenges.

- ESM files could `import` CommonJS files

- CommonJS files could not `require()` ESM files

In other words, consuming CommonJS files from ESM files was possible, but not the other way around.
This introduced many challenges for library authors who wanted to provide ESM support.
These library authors would either have to break compatibility with CommonJS users, “dual-publish” their libraries (providing separate entry-points for ESM and CommonJS), or just stay on CommonJS indefinitely.
While dual-publishing might sound like a good middle-ground, it is a complex and error-prone process that also roughly doubles the amount of code within a package.

Node.js 22 relaxes some of these restrictions and permits `require("esm")` calls from CommonJS modules to ECMAScript modules.
Node.js still does not permit `require()` on ESM files that contain a top-level `await`, but most other ESM files are now consumable from CommonJS files.
This presents a major opportunity for library authors to provide ESM support without having to dual-publish their libraries.

TypeScript 5.8 supports this behavior under the `--module nodenext` flag.
When `--module nodenext` is enabled, TypeScript will avoid issuing errors on these `require()` calls to ESM files.

Because this feature may be back-ported to older versions of Node.js, there is currently no stable `--module nodeXXXX` option that enables this behavior;
however, we predict future versions of TypeScript may be able to stabilize the feature under `node20`.
In the meantime, we encourage users of Node.js 22 and newer to use `--module nodenext`, while library authors and users of older Node.js versions should remain on `--module node16` (or make the minor update to `--module node18` ).

For more information, see our support for require(“esm”) here .

## `--module node18`

 TypeScript 5.8 introduces a stable `--module node18` flag.
For users who are fixed on using Node.js 18, this flag provides a stable point of reference that does not incorporate certain behaviors that are in `--module nodenext`.
Specifically:

- `require()` of ECMAScript modules is disallowed under `node18`, but allowed under `nodenext`

- import assertions (deprecated in favor of import attributes) are allowed under `node18`, but are disallowed under `nodenext`

See more at both the `--module node18` pull request and changes made to `--module nodenext` .

## The `--erasableSyntaxOnly` Option

 Recently, Node.js 23.6 unflagged experimental support for running TypeScript files directly ;
however, only certain constructs are supported under this mode.
Node.js has unflagged a mode called `--experimental-strip-types` which requires that any TypeScript-specific syntax cannot have runtime semantics.
Phrased differently, it must be possible to easily erase or “strip out” any TypeScript-specific syntax from a file, leaving behind a valid JavaScript file.

That means constructs like the following are not supported:

- `enum` declarations

- `namespace`s and `module`s with runtime code

- parameter properties in classes

- Non-ECMAScript `import =` and `export =` assignments

Here are some examples of what does not work:

 ts ` // ❌ error: An `import ... = require(...)` alias import foo = require ( "foo" ); // ❌ error: A namespace with runtime code. namespace container { } // ❌ error: An `import =` alias import Bar = container . Bar ; class Point { // ❌ error: Parameter properties constructor ( public x : number , public y : number ) { } } // ❌ error: An `export =` assignment. export = Point ; // ❌ error: An enum declaration. enum Direction { Up , Down , Left , Right , } `
 Similar tools like ts-blank-space or Amaro (the underlying library for type-stripping in Node.js) have the same limitations.
These tools will provide helpful error messages if they encounter code that doesn’t meet these requirements, but you still won’t find out your code doesn’t work until you actually try to run it.

That’s why TypeScript 5.8 introduces the `--erasableSyntaxOnly` flag.
When this flag is enabled, TypeScript will error on most TypeScript-specific constructs that have runtime behavior.

 ts ` class C { constructor ( public x : number ) { } // ~~~~~~~~~~~~~~~~ // error! This syntax is not allowed when 'erasableSyntaxOnly' is enabled. } } `
 Typically, you will want to combine this flag with the `--verbatimModuleSyntax`, which ensures that a module contains the appropriate import syntax, and that import elision does not take place.

For more information, see the implementation here .

## The `--libReplacement` Flag

 In TypeScript 4.5, we introduced the possibility of substituting the default `lib` files with custom ones.
This was based on the possibility of resolving a library file from packages named `@typescript/lib-*`.
For example, you could lock your `dom` libraries onto a specific version of the `@types/web` package with the following `package.json`:

 json ` { "devDependencies" : { "@typescript/lib-dom" : "npm:@types/web@0.0.199" } } `
 When installed, a package called `@typescript/lib-dom` should exist, and TypeScript will currently always look it up when `dom` is implied by your settings.

This is a powerful feature, but it also incurs a bit of extra work.
Even if you’re not using this feature, TypeScript always performs this lookup, and has to watch for changes in `node_modules` in case a `lib`-replacement package begins to exist.

TypeScript 5.8 introduces the `--libReplacement` flag, which allows you to disable this behavior.
If you’re not using `--libReplacement`, you can now disable it with `--libReplacement false`.
In the future `--libReplacement false` may become the default, so if you currently rely on the behavior you should consider explicitly enabling it with `--libReplacement true`.

For more information, see the change here .

## Preserved Computed Property Names in Declaration Files

 In an effort to make computed properties have more predictable emit in declaration files, TypeScript 5.8 will consistently preserve entity names (`bareVariables` and `dotted.names.that.look.like.this`) in computed property names in classes.

For example, consider the following code:

 ts ` export let propName = "theAnswer" ; export class MyClass { [ propName ] = 42 ; // ~~~~~~~~~~ // error! // A computed property name in a class property declaration must have a simple literal type or a 'unique symbol' type. } `
 Previous versions of TypeScript would issue an error when generating a declaration file for this module, and a best-effort declaration file would generate an index signature.

 ts ` export declare let propName : string ; export declare class MyClass { [ x : string ]: number ; } `
 In TypeScript 5.8, the example code is now allowed, and the emitted declaration file will match what you wrote:

 ts ` export declare let propName : string ; export declare class MyClass { [ propName ]: number ; } `
 Note that this does not create statically-named properties on the class.
You’ll still end up with what is effectively an index signature like `[x: string]: number`, so for that use case, you’d need to use `unique symbol`s or literal types.

Note that writing this code was and currently is an error under the `--isolatedDeclarations` flag;
but we expect that thanks to this change, computed property names will generally be permitted in declaration emit.

Note that it’s possible (though unlikely) that a file compiled in TypeScript 5.8 may generate a declaration file that is not backward compatible in TypeScript 5.7 or earlier.

For more information, see the implementing PR .

## Optimizations on Program Loads and Updates

 TypeScript 5.8 introduces a number of optimizations that can both improve the time to build up a program, and also to update a program based on a file change in either `--watch` mode or editor scenarios.

First, TypeScript now avoids array allocations that would be involved while normalizing paths .
Typically, path normalization would involve segmenting each portion of a path into an array of strings, normalizing the resulting path based on relative segments, and then joining them back together using a canonical separator.
For projects with many files, this can be a significant and repetitive amount of work.
TypeScript now avoids allocating an array, and operates more directly on indexes of the original path.

Additionally, when edits are made that don’t change the fundamental structure of a project, TypeScript now avoids re-validating the options provided to it (e.g. the contents of a `tsconfig.json`).
This means, for example, that a simple edit might not require checking that the output paths of a project don’t conflict with the input paths.
Instead, the results of the last check can be used.
This should make edits in large projects feel more responsive.

## Notable Behavioral Changes

 This section highlights a set of noteworthy changes that should be acknowledged and understood as part of any upgrade.
Sometimes it will highlight deprecations, removals, and new restrictions.
It can also contain bug fixes that are functionally improvements, but which can also affect an existing build by introducing new errors.

### `lib.d.ts`

 Types generated for the DOM may have an impact on type-checking your codebase.
For more information, see linked issues related to DOM and `lib.d.ts` updates for this version of TypeScript .

### Restrictions on Import Assertions Under `--module nodenext`

 Import assertions were a proposed addition to ECMAScript to ensure certain properties of an import (e.g. “this module is JSON, and is not intended to be executable JavaScript code”).
They were reinvented as a proposal called import attributes .
As part of the transition, they swapped from using the `assert` keyword to using the `with` keyword.

 ts ` // An import assertion ❌ - not future-compatible with most runtimes. import data from "./data.json" assert { type : " json " }; // An import attribute ✅ - the preferred way to import a JSON file. import data from "./data.json" with { type : " json " }; `
 Node.js 22 no longer accepts import assertions using the `assert` syntax.
In turn when `--module nodenext` is enabled in TypeScript 5.8, TypeScript will issue an error if it encounters an import assertion.

 ts ` import data from "./data.json" assert { type : " json " }; // ~~~~~~ // error! Import assertions have been replaced by import attributes. Use 'with' instead of 'assert' `
 For more information, see the change here
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: AB Last updated: Jun 15, 2026

## Typescript 5 7

Was this page helpful?

# TypeScript 5.7

## Checks for Never-Initialized Variables

 For a long time, TypeScript has been able to catch issues when a variable has not yet been initialized in all prior branches.

 ts ` let result : number if ( someCondition ()) { result = doSomeWork (); } else { let temporaryWork = doSomeWork (); temporaryWork *= 2 ; // forgot to assign to 'result' } console . log ( result ); // error: Variable 'result' is used before being assigned. `
 Unfortunately, there are some places where this analysis doesn’t work.
For example, if the variable is accessed in a separate function, the type system doesn’t know when the function will be called, and instead takes an “optimistic” view that the variable will be initialized.

 ts ` function foo () { let result : number if ( someCondition ()) { result = doSomeWork (); } else { let temporaryWork = doSomeWork (); temporaryWork *= 2 ; // forgot to assign to 'result' } printResult (); function printResult () { console . log ( result ); // no error here. } } `
 While TypeScript 5.7 is still lenient on variables that have possibly been initialized, the type system is able to report errors when variables have never been initialized at all.

 ts ` function foo () { let result : number // do work, but forget to assign to 'result' function printResult () { console . log ( result ); // error: Variable 'result' is used before being assigned. } } `
 This change was contributed thanks to the work of GitHub user Zzzen !

## Path Rewriting for Relative Paths

 There are several tools and runtimes that allow you to run TypeScript code “in-place”, meaning they do not require a build step which generates output JavaScript files.
For example, ts-node, tsx, Deno, and Bun all support running `.ts` files directly.
More recently, Node.js has been investigating such support with `--experimental-strip-types` (soon to be unflagged!) and `--experimental-transform-types`.
This is extremely convenient because it allows us to iterate faster without worrying about re-running a build task.

There is some complexity to be aware of when using these modes though.
To be maximally compatible with all these tools, a TypeScript file that’s imported “in-place” must be imported with the appropriate TypeScript extension at runtime.
For example, to import a file called `foo.ts`, we have to write the following in Node’s new experimental support:

 ts ` // main.ts import * as foo from "./foo.ts" ; // <- we need foo.ts here, not foo.js `
 Typically, TypeScript would issue an error if we did this, because it expects us to import the output file .
Because some tools do allow `.ts` imports, TypeScript has supported this import style with an option called `--allowImportingTsExtensions` for a while now.
This works fine, but what happens if we need to actually generate `.js` files out of these `.ts` files?
This is a requirement for library authors who will need to be able to distribute just `.js` files, but up until now TypeScript has avoided rewriting any paths.

To support this scenario, we’ve added a new compiler option called `--rewriteRelativeImportExtensions`.
When an import path is relative (starts with `./` or `../`), ends in a TypeScript extension (`.ts`, `.tsx`, `.mts`, `.cts`), and is a non-declaration file, the compiler will rewrite the path to the corresponding JavaScript extension (`.js`, `.jsx`, `.mjs`, `.cjs`).

 ts ` // Under --rewriteRelativeImportExtensions... // these will be rewritten. import * as foo from "./foo.ts" ; import * as bar from "../someFolder/bar.mts" ; // these will NOT be rewritten in any way. import * as a from "./foo" ; import * as b from "some-package/file.ts" ; import * as c from "@some-scope/some-package/file.ts" ; import * as d from "#/file.ts" ; import * as e from "./file.js" ; `
 This allows us to write TypeScript code that can be run in-place and then compiled into JavaScript when we’re ready.

Now, we noted that TypeScript generally avoided rewriting paths.
There are several reasons for this, but the most obvious one is dynamic imports.
If a developer writes the following, it’s not trivial to handle the path that `import` receives.
In fact, it’s impossible to override the behavior of `import` within any dependencies.

 ts ` function getPath () { if ( Math . random () < 0.5 ) { return "./foo.ts" ; } else { return "./foo.js" ; } } let myImport = await import ( getPath ()); `
 Another issue is that (as we saw above) only relative paths are rewritten, and they are written “naively”.
This means that any path that relies on TypeScript’s `baseUrl` and `paths` will not get rewritten:

 json ` // tsconfig.json { "compilerOptions" : { "module" : "nodenext" , // ... "paths" : { "@/*" : [ "./src/*" ] } } } `

```
 ts ` // Won't be transformed, won't work. import * as utilities from "@/utilities.ts" ; `
```

 Nor will any path that might resolve through the `exports` and `imports` fields of a `package.json`.

 json ` // package.json { "name" : "my-package" , "imports" : { "#root/*" : "./dist/*" } } `

```
 ts ` // Won't be transformed, won't work. import * as utilities from "#root/utilities.ts" ; `
```

 As a result, if you’ve been using a workspace-style layout with multiple packages referencing each other, you might need to use conditional exports with scoped custom conditions to make this work:

 json ` // my-package/package.json { "name" : "my-package" , "exports" : { "." : { "@my-package/development" : "./src/index.ts" , "import" : "./lib/index.js" }, "./*" : { "@my-package/development" : "./src/*.ts" , "import" : "./lib/*.js" } } } `
 Any time you want to import the `.ts` files, you can run it with `node --conditions=@my-package/development`.

Note the “namespace” or “scope” we used for the condition `@my-package/development`.
This is a bit of a makeshift solution to avoid conflicts from dependencies that might also use the `development` condition.
If everyone ships a `development` in their package, then resolution may try to resolve to a `.ts` file which will not necessarily work.
This idea is similar to what’s described in Colin McDonnell’s essay Live types in a TypeScript monorepo , along with tshy’s guidance for loading from source .

For more specifics on how this feature works, read up on the change here .

## Support for `--target es2024` and `--lib es2024`

 TypeScript 5.7 now supports `--target es2024`, which allows users to target ECMAScript 2024 runtimes.
This target primarily enables specifying the new `--lib es2024` which contains many features for `SharedArrayBuffer` and `ArrayBuffer`, `Object.groupBy`, `Map.groupBy`, `Promise.withResolvers`, and more.
It also moves `Atomics.waitAsync` from `--lib es2022` to `--lib es2024`.

Note that as part of the changes to `SharedArrayBuffer` and `ArrayBuffer`, the two now diverge a bit.
To bridge the gap and preserve the underlying buffer type, all `TypedArrays` (like `Uint8Array` and others) are now also generic .

 ts ` interface Uint8Array < TArrayBuffer extends ArrayBufferLike = ArrayBufferLike > { // ... } `
 Each `TypedArray` now contains a type parameter named `TArrayBuffer`, though that type parameter has a default type argument so that we can continue to refer to `Int32Array` without explicitly writing out `Int32Array&#x3C;ArrayBufferLike>`.

If you encounter any issues as part of this update, you may need to update `@types/node`.

 This work was primarily provided thanks to Kenta Moriuchi !

## Searching Ancestor Configuration Files for Project Ownership

 When a TypeScript file is loaded in an editor using TSServer (like Visual Studio or VS Code), the editor will try to find the relevant `tsconfig.json` file that “owns” the file.
To do this, it walks up the directory tree from the file being edited, looking for any file named `tsconfig.json`.

Previously, this search would stop at the first `tsconfig.json` file found;
however, imagine a project structure like the following:

 ` project/ ├── src/ │ ├── foo.ts │ ├── foo-test.ts │ ├── tsconfig.json │ └── tsconfig.test.json └── tsconfig.json `
 Here, the idea is that `src/tsconfig.json` is the “main” configuration file for the project, and `src/tsconfig.test.json` is a configuration file for running tests.

 json ` // src/tsconfig.json { "compilerOptions" : { "outDir" : "../dist" }, "exclude" : [ "**/*.test.ts" ] } `

```
 json ` // src/tsconfig.test.json { "compilerOptions" : { "outDir" : "../dist/test" }, "include" : [ "**/*.test.ts" ], "references" : [ { "path" : "./tsconfig.json" } ] } `
```

```
 json ` // tsconfig.json { // This is a "workspace-style" or "solution-style" tsconfig. // Instead of specifying any files, it just references all the actual projects. "files" : [], "references" : [ { "path" : "./src/tsconfig.json" }, { "path" : "./src/tsconfig.test.json" }, ] } `
```

 The problem here is that when editing `foo-test.ts`, the editor would find `project/src/tsconfig.json` as the “owning” configuration file - but that’s not the one we want!
If the walk stops at this point, that might not be desirable.
The only way to avoid this previously was to rename `src/tsconfig.json` to something like `src/tsconfig.src.json`, and then all files would hit the top-level `tsconfig.json` which references every possible project.

 ` project/ ├── src/ │ ├── foo.ts │ ├── foo-test.ts │ ├── tsconfig.src.json │ └── tsconfig.test.json └── tsconfig.json `
 Instead of forcing developers to do this, TypeScript 5.7 now continues walking up the directory tree to find other appropriate `tsconfig.json` files for editor scenarios.
This can provide more flexibility in how projects are organized and how configuration files are structured.

You can get more specifics on the implementation on GitHub here and here .

## Faster Project Ownership Checks in Editors for Composite Projects

 Imagine a large codebase with the following structure:

 ` packages ├── graphics/ │ ├── tsconfig.json │ └── src/ │ └── ... ├── sound/ │ ├── tsconfig.json │ └── src/ │ └── ... ├── networking/ │ ├── tsconfig.json │ └── src/ │ └── ... ├── input/ │ ├── tsconfig.json │ └── src/ │ └── ... └── app/ ├── tsconfig.json ├── some-script.js └── src/ └── ... `
 Each directory in `packages` is a separate TypeScript project, and the `app` directory is the main project that depends on all the other projects.

 json ` // app/tsconfig.json { "compilerOptions" : { // ... }, "include" : [ "src" ], "references" : [ { "path" : "../graphics/tsconfig.json" }, { "path" : "../sound/tsconfig.json" }, { "path" : "../networking/tsconfig.json" }, { "path" : "../input/tsconfig.json" } ] } `
 Now notice we have the file `some-script.js` in the `app` directory.
When we open `some-script.js` in the editor, the TypeScript language service (which also handles the editor experience for JavaScript files!) has to figure out which project the file belongs to so it can apply the right settings.

In this case, the nearest `tsconfig.json` does not include `some-script.js`, but TypeScript will proceed to ask “could one of the projects referenced by `app/tsconfig.json` include `some-script.js`?“.
To do so, TypeScript would previously load up each project, one-by-one, and stop as soon as it found a project which contained `some-script.js`.
Even if `some-script.js` isn’t included in the root set of files, TypeScript would still parse all the files within a project because some of the root set of files can still transitively reference `some-script.js`.

What we found over time was that this behavior caused extreme and unpredictable behavior in larger codebases.
Developers would open up stray script files and find themselves waiting for their entire codebase to be opened up.

Thankfully, every project that can be referenced by another (non-workspace) project must enable a flag called `composite`, which enforces a rule that all input source files must be known up-front.
So when probing a `composite` project, TypeScript 5.7 will only check if a file belongs to the root set of files of that project.
This should avoid this common worst-case behavior.

For more information, see the change here .

### Validated JSON Imports in `--module nodenext`

 When importing from a `.json` file under `--module nodenext`, TypeScript will now enforce certain rules to prevent runtime errors.

For one, an import attribute containing `type: "json"` needs to be present for any JSON file import.

 ts ` import myConfig from "./myConfig.json" ; // ~~~~~~~~~~~~~~~~~ // ❌ error: Importing a JSON file into an ECMAScript module requires a 'type: "json"' import attribute when 'module' is set to 'NodeNext'. import myConfig from "./myConfig.json" with { type : " json " }; // ^^^^^^^^^^^^^^^^ // ✅ This is fine because we provided `type: "json"` `
 On top of this validation, TypeScript will not generate “named” exports, and the contents of a JSON import will only be accessible via a default.

 ts ` // ✅ This is okay: import myConfigA from "./myConfig.json" with { type : " json " }; let version = myConfigA . version ; /////////// import * as myConfigB from "./myConfig.json" with { type : " json " }; // ❌ This is not: let version = myConfig . version ; // ✅ This is okay: let version = myConfig . default . version ; `
 See here for more information on this change.

## Support for V8 Compile Caching in Node.js

 Node.js 22 supports a new API called `module.enableCompileCache()` .
This API allows the runtime to reuse some of the parsing and compilation work done after the first run of a tool.

TypeScript 5.7 now leverages the API so that it can start doing useful work sooner.
In some of our own testing, we’ve witnessed about a 2.5x speed-up in running `tsc --version`.

 ` Benchmark 1: node ./built/local/_tsc.js --version (*without* caching) Time (mean ± σ): 122.2 ms ± 1.5 ms [User: 101.7 ms, System: 13.0 ms] Range (min … max): 119.3 ms … 132.3 ms 200 runs Benchmark 2: node ./built/local/tsc.js --version (*with* caching) Time (mean ± σ): 48.4 ms ± 1.0 ms [User: 34.0 ms, System: 11.1 ms] Range (min … max): 45.7 ms … 52.8 ms 200 runs Summary node ./built/local/tsc.js --version ran 2.52 ± 0.06 times faster than node ./built/local/_tsc.js --version `
 For more information, see the pull request here .

## Notable Behavioral Changes

 This section highlights a set of noteworthy changes that should be acknowledged and understood as part of any upgrade.
Sometimes it will highlight deprecations, removals, and new restrictions.
It can also contain bug fixes that are functionally improvements, but which can also affect an existing build by introducing new errors.

### `lib.d.ts`

 Types generated for the DOM may have an impact on type-checking your codebase.
For more information, see linked issues related to DOM and `lib.d.ts` updates for this version of TypeScript .

### `TypedArray`s Are Now Generic Over `ArrayBufferLike`

 In ECMAScript 2024, `SharedArrayBuffer` and `ArrayBuffer` have types that slightly diverge.
To bridge the gap and preserve the underlying buffer type, all `TypedArrays` (like `Uint8Array` and others) are now also generic .

 ts ` interface Uint8Array < TArrayBuffer extends ArrayBufferLike = ArrayBufferLike > { // ... } `
 Each `TypedArray` now contains a type parameter named `TArrayBuffer`, though that type parameter has a default type argument so that users can continue to refer to `Int32Array` without explicitly writing out `Int32Array&#x3C;ArrayBufferLike>`.

If you encounter any issues as part of this update, such as

 ` error TS2322: Type 'Buffer' is not assignable to type 'Uint8Array<ArrayBufferLike>'. error TS2345: Argument of type 'Buffer' is not assignable to parameter of type 'Uint8Array<ArrayBufferLike>'. error TS2345: Argument of type 'ArrayBufferLike' is not assignable to parameter of type 'ArrayBuffer'. error TS2345: Argument of type 'Buffer' is not assignable to parameter of type 'string | ArrayBufferView | Stream | Iterable<string | ArrayBufferView> | AsyncIterable<string | ArrayBufferView>'. `
 then you may need to update `@types/node`.

You can read the specifics about this change on GitHub .

### Creating Index Signatures from Non-Literal Method Names in Classes

 TypeScript now has a more consistent behavior for methods in classes when they are declared with non-literal computed property names.
For example, in the following:

 ts ` declare const symbolMethodName : symbol ; export class A { [ symbolMethodName ]() { return 1 }; } `
 Previously TypeScript just viewed the class in a way like the following:

 ts ` export class A { } `
 In other words, from the type system’s perspective, `[symbolMethodName]` contributed nothing to the type of `A`

TypeScript 5.7 now views the method `[symbolMethodName]() {}` more meaningfully, and generates an index signature.
As a result, the code above is interpreted as something like the following code:

 ts ` export class A { [ x : symbol ]: () => number ; } `
 This provides behavior that is consistent with properties and methods in object literals.

 Read up more on this change here .

### More Implicit `any` Errors on Functions Returning `null` and `undefined`

 When a function expression is contextually typed by a signature returning a generic type, TypeScript now appropriately provides an implicit `any` error under `noImplicitAny`, but outside of `strictNullChecks`.

 ts ` declare var p : Promise < number >; const p2 = p . catch (() => null ); // ~~~~~~~~~~ // error TS7011: Function expression, which lacks return-type annotation, implicitly has an 'any' return type. `
 See this change for more details .
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: N Last updated: Jun 15, 2026

## Typescript 5 6

Was this page helpful?

# TypeScript 5.6

## Disallowed Nullish and Truthy Checks

 Maybe you’ve written a regex and forgotten to call `.test(...)` on it:

 ts ` if ( /0x [ 0-9a-f ] / ) { // Oops! This block always runs. // ... } `
 or maybe you’ve accidentally written `=>` (which creates an arrow function) instead of `>=` (the greater-than-or-equal-to operator):

 ts ` if ( x => 0 ) { // Oops! This block always runs. // ... } `
 or maybe you’ve tried to use a default value with `??`, but mixed up the precedence of `??` and a comparison operator like `&#x3C;`:

 ts ` function isValid ( value : string | number , options : any , strictness : "strict" | "loose" ) { if ( strictness === "loose" ) { value = + value } return value < options . max ?? 100 ; // Oops! This is parsed as (value < options.max) ?? 100 } `
 or maybe you’ve misplaced a parenthesis in a complex expression:

 ts ` if ( isValid ( primaryValue , "strict" ) || isValid ( secondaryValue , "strict" ) || isValid ( primaryValue , "loose" || isValid ( secondaryValue , "loose" )) ) { // ^^^^ 👀 Did we forget a closing ')'? } `
 None of these examples do what the author intended, but they’re all valid JavaScript code.
Previously TypeScript also quietly accepted these examples.

But with a little bit of experimentation, we found that many many bugs could be caught from flagging down suspicious examples like above.
In TypeScript 5.6, the compiler now errors when it can syntactically determine a truthy or nullish check will always evaluate in a specific way.
So in the above examples, you’ll start to see errors:

 ts ` if ( /0x [ 0-9a-f ] / ) { // ~~~~~~~~~~~~ // error: This kind of expression is always truthy. } if ( x => 0 ) { // ~~~~~~ // error: This kind of expression is always truthy. } function isValid ( value : string | number , options : any , strictness : "strict" | "loose" ) { if ( strictness === "loose" ) { value = + value } return value < options . max ?? 100 ; // ~~~~~~~~~~~~~~~~~~~ // error: Right operand of ?? is unreachable because the left operand is never nullish. } if ( isValid ( primaryValue , "strict" ) || isValid ( secondaryValue , "strict" ) || isValid ( primaryValue , "loose" || isValid ( secondaryValue , "loose" )) ) { // ~~~~~~~ // error: This kind of expression is always truthy. } `
 Similar results can be achieved by enabling the ESLint `no-constant-binary-expression` rule, and you can see some of the results they achieved in their blog post ;
but the new checks TypeScript performs does not have perfect overlap with the ESLint rule, and we also believe there is a lot of value in having these checks built into TypeScript itself.

Note that certain expressions are still allowed, even if they are always truthy or nullish.
Specifically, `true`, `false`, `0`, and `1` are all still allowed despite always being truthy or falsy, since code like the following:

 ts ` while ( true ) { doStuff (); if ( something ()) { break ; } doOtherStuff (); } `
 is still idiomatic and useful, and code like the following:

 ts ` if ( true || inDebuggingOrDevelopmentEnvironment ()) { // ... } `
 is useful while iterating/debugging code.

If you’re curious about the implementation or the sorts of bugs it catches, take a look at the pull request that implemented this feature .

## Iterator Helper Methods

 JavaScript has a notion of iterables (things which we can iterate over by calling a `[Symbol.iterator]()` and getting an iterator) and iterators (things which have a `next()` method which we can call to try to get the next value as we iterate).
By and large, you don’t typically have to think about these things when you toss them into a `for`/`of` loop, or `[...spread]` them into a new array.
But TypeScript does model these with the types `Iterable` and `Iterator` (and even `IterableIterator` which acts as both!), and these types describe the minimal set of members you need for constructs like `for`/`of` to work on them.

`Iterable`s (and `IterableIterator`s) are nice because they can be used in all sorts of places in JavaScript - but a lot of people found themselves missing methods on `Array`s like `map`, `filter`, and for some reason `reduce`.
That’s why a recent proposal was brought forward in ECMAScript to add many methods (and more) from `Array` onto most of the `IterableIterator`s that are produced in JavaScript.

For example, every generator now produces an object that also has a `map` method and a `take` method.

 ts ` function* positiveIntegers () { let i = 1 ; while ( true ) { yield i ; i ++; } } const evenNumbers = positiveIntegers (). map ( x => x * 2 ); // Output: // 2 // 4 // 6 // 8 // 10 for ( const value of evenNumbers . take ( 5 )) { console . log ( value ); } `
 The same is true for methods like `keys()`, `values()`, and `entries()` on `Map`s and `Set`s.

 ts ` function invertKeysAndValues < K , V >( map : Map < K , V >): Map < V , K > { return new Map ( map . entries (). map (([ k , v ]) => [ v , k ]) ); } `
 You can also extend the new `Iterator` object:

 ts ` /** * Provides an endless stream of `0`s. */ class Zeroes extends Iterator < number > { next () { return { value: 0 , done: false } as const ; } } const zeroes = new Zeroes (); // Transform into an endless stream of `1`s. const ones = zeroes . map ( x => x + 1 ); `
 And you can adapt any existing `Iterable`s or `Iterator`s into this new type with `Iterator.from`:

 ts ` Iterator . from (...). filter ( someFunction ); `
 Now, we have to talk about naming.

Earlier we mentioned that TypeScript has types for `Iterable` and `Iterator`;
however, like we mentioned, these act sort of like “protocols” to ensure certain operations work.
 That means that not every value that is declared `Iterable` or `Iterator` in TypeScript will have those methods we mentioned above.

But there is still a new runtime value called `Iterator`.
You can reference `Iterator`, as well as `Iterator.prototype`, as actual values in JavaScript.
This is a bit awkward since TypeScript already defines its own thing called `Iterator` purely for type-checking.
So due to this unfortunate name clash, TypeScript needs to introduce a separate type to describe these native/built-in iterable iterators.

TypeScript 5.6 introduces a new type called `IteratorObject`.
It is defined as follows:

 ts ` interface IteratorObject < T , TReturn = unknown , TNext = unknown > extends Iterator < T , TReturn , TNext > { [ Symbol . iterator ](): IteratorObject < T , TReturn , TNext >; } `
 Lots of built-in collections and methods produce subtypes of `IteratorObject`s (like `ArrayIterator`, `SetIterator`, `MapIterator`, and more), and both the core JavaScript and DOM types in `lib.d.ts`, along with `@types/node`, have been updated to use this new type.

Similarly, there is a `AsyncIteratorObject` type for parity.
`AsyncIterator` does not yet exist as a runtime value in JavaScript that brings the same methods for `AsyncIterable`s, but it is an active proposal and this new type prepares for it.

We’d like to thank Kevin Gibbons who contributed the changes for these types , and who is one of the co-authors of the proposal .

## Strict Builtin Iterator Checks (and `--strictBuiltinIteratorReturn`)

 When you call the `next()` method on an `Iterator&#x3C;T, TReturn>`, it returns an object with a `value` and a `done` property.
This is modeled with the type `IteratorResult`.

 ts ` type IteratorResult < T , TReturn = any > = IteratorYieldResult < T > | IteratorReturnResult < TReturn >; interface IteratorYieldResult < TYield > { done ?: false ; value : TYield ; } interface IteratorReturnResult < TReturn > { done : true ; value : TReturn ; } `
 The naming here is inspired by the way a generator function works.
Generator functions can `yield` values, and then `return` a final value - but the types between the two can be unrelated.

 ts ` function abc123 () { yield "a" ; yield "b" ; yield "c" ; return 123 ; } const iter = abc123 (); iter . next (); // { value: "a", done: false } iter . next (); // { value: "b", done: false } iter . next (); // { value: "c", done: false } iter . next (); // { value: 123, done: true } `
 With the new `IteratorObject` type, we discovered some difficulties in allowing safe implementations of `IteratorObject`s.
At the same time, there’s been a long standing unsafety with `IteratorResult` in cases where `TReturn` was `any` (the default!).
For example, let’s say we have an `IteratorResult&#x3C;string, any>`.
If we end up reaching for the `value` of this type, we’ll end up with `string | any`, which is just `any`.

 ts ` function* uppercase ( iter : Iterator < string , any >) { while ( true ) { const { value , done } = iter . next (); yield value . toUppercase (); // oops! forgot to check for `done` first and misspelled `toUpperCase` if ( done ) { return ; } } } `
 It would be hard to fix this on every `Iterator` today without introducing a lot of breaks, but we can at least fix it with most `IteratorObject`s that get created.

TypeScript 5.6 introduces a new intrinsic type called `BuiltinIteratorReturn` and a new `--strict`-mode flag called `--strictBuiltinIteratorReturn`.
Whenever `IteratorObject`s are used in places like `lib.d.ts`, they are always written with `BuiltinIteratorReturn` type for `TReturn` (though you’ll see the more-specific `MapIterator`, `ArrayIterator`, `SetIterator` more often).

 ts ` interface MapIterator < T > extends IteratorObject < T , BuiltinIteratorReturn , unknown > { [ Symbol . iterator ](): MapIterator < T >; } // ... interface Map < K , V > { // ... /** * Returns an iterable of key, value pairs for every entry in the map. */ entries (): MapIterator <[ K , V ]>; /** * Returns an iterable of keys in the map */ keys (): MapIterator < K >; /** * Returns an iterable of values in the map */ values (): MapIterator < V >; } `
 By default, `BuiltinIteratorReturn` is `any`, but when `--strictBuiltinIteratorReturn` is enabled (possibly via `--strict`), it is `undefined`.
Under this new mode, if we use `BuiltinIteratorReturn`, our earlier example now correctly errors:

 ts ` function* uppercase ( iter : Iterator < string , BuiltinIteratorReturn >) { while ( true ) { const { value , done } = iter . next (); yield value . toUppercase (); // ~~~~~ ~~~~~~~~~~~ // error! ┃ ┃ // ┃ ┗━ Property 'toUppercase' does not exist on type 'string'. Did you mean 'toUpperCase'? // ┃ // ┗━ 'value' is possibly 'undefined'. if ( done ) { return ; } } } `
 You’ll typically see `BuiltinIteratorReturn` paired up with `IteratorObject` throughout `lib.d.ts`.
In general, we recommend being more explicit around the `TReturn` in your own code when possible.

For more information, you can read up on the feature here .

## Support for Arbitrary Module Identifiers

 JavaScript allows modules to export bindings with invalid identifier names as string literals:

 ts ` const banana = "🍌" ; export { banana as "🍌" }; `
 Likewise, it allows modules to grab imports with these arbitrary names and bind them to valid identifiers:

 ts ` import { "🍌" as banana } from "./foo" /** * om nom nom */ function eat ( food : string ) { console . log ( "Eating" , food ); }; eat ( banana ); `
 This seems like a cute party trick (if you’re as fun as we are at parties), but it has its uses for interoperability with other languages (typically via JavaScript/WebAssembly boundaries), since other languages may have different rules for what constitutes a valid identifier.
It can also be useful for tools that generate code, like esbuild with its `inject` feature .

TypeScript 5.6 now allows you to use these arbitrary module identifiers in your code!
We’d like to thank Evan Wallace who contributed this change to TypeScript !

## The `--noUncheckedSideEffectImports` Option

 In JavaScript it’s possible to `import` a module without actually importing any values from it.

 ts ` import "some-module" ; `
 These imports are often called side effect imports because the only useful behavior they can provide is by executing some side effect (like registering a global variable, or adding a polyfill to a prototype).

In TypeScript, this syntax has had a pretty strange quirk: if the `import` could be resolved to a valid source file, then TypeScript would load and check the file.
On the other hand, if no source file could be found, TypeScript would silently ignore the `import`!

This is surprising behavior, but it partially stems from modeling patterns in the JavaScript ecosystem.
For example, this syntax has also been used with special loaders in bundlers to load CSS or other assets.
Your bundler might be configured in such a way where you can include specific `.css` files by writing something like the following:

 tsx ` import "./button-component.css" ; export function Button () { // ... } `
 Still, this masks potential typos on side effect imports.
That’s why TypeScript 5.6 introduces a new compiler option called `--noUncheckedSideEffectImports`, to catch these cases.
When `--noUncheckedSideEffectImports` is enabled, TypeScript will now error if it can’t find a source file for a side effect import.

 ts ` import "oops-this-module-does-not-exist" ; // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ // error: Cannot find module 'oops-this-module-does-not-exist' or its corresponding type declarations. `
 When enabling this option, some working code may now receive an error, like in the CSS example above.
To work around this, users who want to just write side effect `import`s for assets might be better served by writing what’s called an ambient module declaration with a wildcard specifier.
It would go in a global file and look something like the following:

 ts ` // ./src/globals.d.ts // Recognize all CSS files as module imports. declare module "*.css" {} `
 In fact, you might already have a file like this in your project!
For example, running something like `vite init` might create a similar `vite-env.d.ts`.

While this option is currently off by default, we encourage users to give it a try!

For more information, check out the implementation here .

## The `--noCheck` Option

 TypeScript 5.6 introduces a new compiler option, `--noCheck`, which allows you to skip type checking for all input files.
This avoids unnecessary type-checking when performing any semantic analysis necessary for emitting output files.

One scenario for this is to separate JavaScript file generation from type-checking so that the two can be run as separate phases.
For example, you could run `tsc --noCheck` while iterating, and then `tsc --noEmit` for a thorough type check.
You could also run the two tasks in parallel, even in `--watch` mode, though note you’d probably want to specify a separate `--tsBuildInfoFile` path if you’re truly running them at the same time.

`--noCheck` is also useful for emitting declaration files in a similar fashion.
In a project where `--noCheck` is specified on a project that conforms to `--isolatedDeclarations`, TypeScript can quickly generate declaration files without a type-checking pass.
The generated declaration files will rely purely on quick syntactic transformations.

Note that in cases where `--noCheck` is specified, but a project does not use `--isolatedDeclarations`, TypeScript may still perform as much type-checking as necessary to generate `.d.ts` files.
In this sense, `--noCheck` is a bit of a misnomer; however, the process will be lazier than a full type-check, only calculating the types of unannotated declarations.
This should be much faster than a full type-check.

`noCheck` is also available via the TypeScript API as a standard option.
Internally, `transpileModule` and `transpileDeclaration` already used `noCheck` to speed things up (at least as of TypeScript 5.5).
Now any build tool should be able to leverage the flag, taking a variety of custom strategies to coordinate and speed up builds.

For more information, see the work done in TypeScript 5.5 to power up `noCheck` internally , along with the relevant work to make it publicly available on the command line and

## Allow `--build` with Intermediate Errors

 TypeScript’s concept of project references allows you to organize your codebase into multiple projects and create dependencies between them.
Running the TypeScript compiler in `--build` mode (or `tsc -b` for short) is the built-in way of actually conducting that build across projects and figuring out which projects and files need to be compiled.

Previously, using `--build` mode would assume `--noEmitOnError` and immediately stop the build if any errors were encountered.
This meant that “downstream” projects could never be checked and built if any of their “upstream” dependencies had build errors.
In theory, this is a very cromulent approach - if a project has errors, it is not necessarily in a coherent state for its dependencies.

In reality, this sort of rigidity made things like upgrades a pain.
For example, if `projectB` depends on `projectA`, then people more familiar with `projectB` can’t proactively upgrade their code until their dependencies are upgraded.
They are blocked by work on upgrading `projectA` first.

As of TypeScript 5.6, `--build` mode will continue to build projects even if there are intermediate errors in dependencies.
In the face of intermediate errors, they will be reported consistently and output files will be generated on a best-effort basis;
however, the build will continue to completion on the specified project.

If you want to stop the build on the first project with errors, you can use a new flag called `--stopOnBuildErrors`.
This can be useful when running in a CI environment, or when iterating on a project that’s heavily depended upon by other projects.

Note that to accomplish this, TypeScript now always emits a `.tsbuildinfo` file for any project in a `--build` invocation (even if `--incremental`/`--composite` is not specified).
This is to keep track of the state of how `--build` was invoked and what work needs to be performed in the future.

You can read more about this change here on the implementation .

## Region-Prioritized Diagnostics in Editors

 When TypeScript’s language service is asked for the diagnostics for a file (things like errors, suggestions, and deprecations), it would typically require checking the entire file .
Most of the time this is fine, but in extremely large files it can incur a delay.
That can be frustrating because fixing a typo should feel like a quick operation, but can take seconds in a big-enough file.

To address this, TypeScript 5.6 introduces a new feature called region-prioritized diagnostics or region-prioritized checking .
Instead of just requesting diagnostics for a set of files, editors can now also provide a relevant region of a given file - and the intent is that this will typically be the region of the file that is currently visible to a user.
The TypeScript language server can then choose to provide two sets of diagnostics: one for the region, and one for the file in its entirety.
This allows editing to feel way more responsive in large files so you’re not waiting as long for thoes red squiggles to disappear.

For some specific numbers, in our testing on TypeScript’s own `checker.ts` , a full semantic diagnostics response took 3330ms.
In contrast, the response for the first region-based diagnostics response took 143ms!
While the remaining whole-file response took about 3200ms, this can make a huge difference for quick edits.

This feature also includes quite a bit of work to also make diagnostics report more consistently throughout your experience.
Due the way our type-checker leverages caching to avoid work, subsequent checks between the same types could often have a different (typically shorter) error message.
Technically, lazy out-of-order checking could cause diagnostics to report differently between two locations in an editor - even before this feature - but we didn’t want to exacerbate the issue.
With recent work, we’ve ironed out many of these error inconsistencies.

Currently, this functionality is available in Visual Studio Code for TypeScript 5.6 and later.

For more detailed information, take a look at the implementation and write-up here .

## Granular Commit Characters

 TypeScript’s language service now provides its own commit characters for each completion item.
Commit characters are specific characters that, when typed, will automatically commit the currently-suggested completion item.

What this means is that over time your editor will now more frequently commit to the currently-suggested completion item when you type certain characters.
For example, take the following code:

 ts ` declare let food : { eat (): any ; } let f = ( foo /**/ `
 If our cursor is at `/**/`, it’s unclear if the code we’re writing is going to be something like `let f = (food.eat())` or `let f = (foo, bar) => foo + bar`.
You could imagine that the editor might be able to auto-complete differently depending on which character we type out next.
For instance, if we type in the period/dot character (`.`), we probably want the editor to complete with the variable `food`;
but if we type the comma character (`,`), we might be writing out a parameter in an arrow function.

Unfortunately, previously TypeScript just signaled to editors that the current text might define a new parameter name so that no commit characters were safe.
So hitting a `.` wouldn’t do anything even if it was “obvious” that the editor should auto-complete with the word `food`.

TypeScript now explicitly lists which characters are safe to commit for each completion item.
While this won’t immediately change your day-to-day experience, editors that support these commit characters should see behavioral improvements over time.
To see those improvements right now, you can now use the TypeScript nightly extension with Visual Studio Code Insiders .
Hitting `.` in the code above correctly auto-completes with `food`.

For more information, see the pull request that added commit characters along with our adjustments to commit characters depending on context .

## Exclude Patterns for Auto-Imports

 TypeScript’s language service now allows you to specify a list of regular expression patterns which will filter away auto-import suggestions from certain specifiers.
For example, if you want to exclude all “deep” imports from a package like `lodash`, you could configure the following preference in Visual Studio Code:

 json ` { "typescript.preferences.autoImportSpecifierExcludeRegexes" : [ "^lodash/.*$" ] } `
 Or going the other way, you might want to disallow importing from the entry-point of a package:

 json ` { "typescript.preferences.autoImportSpecifierExcludeRegexes" : [ "^lodash$" ] } `
 One could even avoid `node:` imports by using the following setting:

 json ` { "typescript.preferences.autoImportSpecifierExcludeRegexes" : [ "^node:" ] } `
 Note that if you want to specify certain flags like `i` or `u`, you will need to surround your regular expression with slashes.
When providing surrounding slashes, you’ll need to escape other inner slashes.

 json ` { "typescript.preferences.autoImportSpecifierExcludeRegexes" : [ "^./lib/internal" , // no escaping needed "/^. \\ /lib \\ /internal/" , // escaping needed - note the leading and trailing slashes "/^. \\ /lib \\ /internal/i" // escaping needed - we needed slashes to provide the 'i' regex flag ] } `
 In Visual Studio Code, the same settings can be applied for JavaScript through `javascript.preferences.autoImportSpecifierExcludeRegexes`.

For more information, see the implementation here .

## Notable Behavioral Changes

 This section highlights a set of noteworthy changes that should be acknowledged and understood as part of any upgrade.
Sometimes it will highlight deprecations, removals, and new restrictions.
It can also contain bug fixes that are functionally improvements, but which can also affect an existing build by introducing new errors.

### `lib.d.ts`

 Types generated for the DOM may have an impact on type-checking your codebase.
For more information, see linked issues related to DOM and `lib.d.ts` updates for this version of TypeScript .

### `.tsbuildinfo` is Always Written

 To enable `--build` to continue building projects even if there are intermediate errors in dependencies, and to support `--noCheck` on the command line, TypeScript now always emits a `.tsbuildinfo` file for any project in a `--build` invocation.
This happens regardless of whether `--incremental` is actually on.
 See more information here .

### Respecting File Extensions and `package.json` from within `node_modules`

 Before Node.js implemented support for ECMAScript modules in v12, there was never a good way for TypeScript to know whether `.d.ts` files it found in `node_modules` represented JavaScript files authored as CommonJS or ECMAScript modules.
When the vast majority of npm was CommonJS-only, this didn’t cause many problems - if in doubt, TypeScript could just assume that everything behaved like CommonJS.
Unfortunately, if that assumption was wrong it could allow unsafe imports:

 ts ` // node_modules/dep/index.d.ts export declare function doSomething (): void ; // index.ts // Okay if "dep" is a CommonJS module, but fails if // it's an ECMAScript module - even in bundlers! import dep from "dep" ; dep . doSomething (); `
 In practice, this didn’t come up very often.
But in the years since Node.js started supporting ECMAScript modules, the share of ESM on npm has grown.
Fortunately, Node.js also introduced a mechanism that can help TypeScript determine if a file is an ECMAScript module or a CommonJS module: the `.mjs` and `.cjs` file extensions and the `package.json` `"type"` field.
TypeScript 4.7 added support for understanding these indicators, as well as authoring `.mts` and `.cts` files;
however, TypeScript would only read those indicators under `--module node16` and `--module nodenext`, so the unsafe import above was still a problem for anyone using `--module esnext` and `--moduleResolution bundler`, for example.

To solve this, TypeScript 5.6 collects module format information and uses it to resolve ambiguities like the one in the example above in all `module` modes (except `amd`, `umd`, and `system`).
Format-specific file extensions (`.mts` and `.cts`) are respected anywhere they’re found, and the `package.json` `"type"` field is consulted inside `node_modules` dependencies, regardless of the `module` setting.
Previously, it was technically possible to produce CommonJS output into a `.mjs` file or vice versa:

 ts ` // main.mts export default "oops" ; // $ tsc --module commonjs main.mts // main.mjs Object . defineProperty ( exports , "__esModule" , { value: true }); exports . default = "oops" ; `
 Now, `.mts` files never emit CommonJS output, and `.cts` files never emit ESM output.

Note that much of this behavior was provided in pre-release versions of TypeScript 5.5 ( implementation details here ), but in 5.6 this behavior is only extended to files within `node_modules`.

More details are available on the change here .

### Correct `override` Checks on Computed Properties

 Previously, computed properties marked with `override` did not correctly check for the existence of a base class member.
Similarly, if you used `noImplicitOverride`, you would not get an error if you forgot to add an `override` modifier to a computed property.

TypeScript 5.6 now correctly checks computed properties in both cases.

 ts ` const foo = Symbol ( "foo" ); const bar = Symbol ( "bar" ); class Base { [ bar ]() {} } class Derived extends Base { override [ foo ]() {} // ~~~~~ // error: This member cannot have an 'override' modifier because it is not declared in the base class 'Base'. [ bar ]() {} // ~~~~~ // error under noImplicitOverride: This member must have an 'override' modifier because it overrides a member in the base class 'Base'. } `
 This fix was contributed thanks to Oleksandr Tarasiuk in this pull request .
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: N Last updated: Jun 15, 2026

## Typescript 5 5

Was this page helpful?

# TypeScript 5.5

## Inferred Type Predicates

 This section was written by Dan Vanderkam , who implemented this feature in TypeScript 5.5 . Thanks Dan!

TypeScript’s control flow analysis does a great job of tracking how the type of a variable changes as it moves through your code:

 tsx ` interface Bird { commonName : string ; scientificName : string ; sing (): void ; } // Maps country names -> national bird. // Not all nations have official birds (looking at you, Canada!) declare const nationalBirds : Map < string , Bird >; function makeNationalBirdCall ( country : string ) { const bird = nationalBirds . get ( country ); // bird has a declared type of Bird | undefined if ( bird ) { bird . sing (); // bird has type Bird inside the if statement } else { // bird has type undefined here. } } `
 By making you handle the `undefined` case, TypeScript pushes you to write more robust code.

In the past, this sort of type refinement was more difficult to apply to arrays. This would have been an error in all previous versions of TypeScript:

 tsx ` function makeBirdCalls ( countries : string []) { // birds: (Bird | undefined)[] const birds = countries . map ( country => nationalBirds . get ( country )) . filter ( bird => bird !== undefined ); for ( const bird of birds ) { bird . sing (); // error: 'bird' is possibly 'undefined'. } } `
 This code is perfectly fine: we’ve filtered all the `undefined` values out of the list.
But TypeScript hasn’t been able to follow along.

With TypeScript 5.5, the type checker is fine with this code:

 tsx ` function makeBirdCalls ( countries : string []) { // birds: Bird[] const birds = countries . map ( country => nationalBirds . get ( country )) . filter ( bird => bird !== undefined ); for ( const bird of birds ) { bird . sing (); // ok! } } `
 Note the more precise type for `birds`.

This works because TypeScript now infers a type predicate for the `filter` function.
You can see what’s going on more clearly by pulling it out into a standalone function:

 tsx ` // function isBirdReal(bird: Bird | undefined): bird is Bird function isBirdReal ( bird : Bird | undefined ) { return bird !== undefined ; } `
 `bird is Bird` is the type predicate.
It means that, if the function returns `true`, then it’s a `Bird` (if the function returns `false` then it’s `undefined`).
The type declarations for `Array.prototype.filter` know about type predicates, so the net result is that you get a more precise type and the code passes the type checker.

TypeScript will infer that a function returns a type predicate if these conditions hold:

- The function does not have an explicit return type or type predicate annotation.

- The function has a single `return` statement and no implicit returns.

- The function does not mutate its parameter.

- The function returns a `boolean` expression that’s tied to a refinement on the parameter.

Generally this works how you’d expect.
Here’s a few more examples of inferred type predicates:

 tsx ` // const isNumber: (x: unknown) => x is number const isNumber = ( x : unknown ) => typeof x === 'number' ; // const isNonNullish: <T>(x: T) => x is NonNullable<T> const isNonNullish = < T ,>( x : T ) => x != null ; `
 Previously, TypeScript would have just inferred that these functions return `boolean`.
It now infers signatures with type predicates like `x is number` or `x is NonNullable&#x3C;T>`.

Type predicates have “if and only if” semantics.
If a function returns `x is T`, then it means that:

- If the function returns `true` then `x` has the type `T`.

- If the function returns `false` then `x` does not have type `T`.

If you’re expecting a type predicate to be inferred but it’s not, then you may be running afoul of the second rule. This often comes up with “truthiness” checks:

 tsx ` function getClassroomAverage ( students : string [], allScores : Map < string , number >) { const studentScores = students . map ( student => allScores . get ( student )) . filter ( score => !! score ); return studentScores . reduce (( a , b ) => a + b ) / studentScores . length ; // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ // error: Object is possibly 'undefined'. } `
 TypeScript did not infer a type predicate for `score => !!score`, and rightly so: if this returns `true` then `score` is a `number`.
But if it returns `false`, then `score` could be either `undefined` or a `number` (specifically, `0`).
This is a real bug: if any student got a zero on the test, then filtering out their score will skew the average upwards.
Fewer will be above average and more will be sad!

As with the first example, it’s better to explicitly filter out `undefined` values:

 tsx ` function getClassroomAverage ( students : string [], allScores : Map < string , number >) { const studentScores = students . map ( student => allScores . get ( student )) . filter ( score => score !== undefined ); return studentScores . reduce (( a , b ) => a + b ) / studentScores . length ; // ok! } `
 A truthiness check will infer a type predicate for object types, where there’s no ambiguity.
Remember that functions must return a `boolean` to be a candidate for an inferred type predicate: `x => !!x` might infer a type predicate, but `x => x` definitely won’t.

Explicit type predicates continue to work exactly as before.
TypeScript will not check whether it would infer the same type predicate.
Explicit type predicates (“is”) are no safer than a type assertion (“as”).

It’s possible that this feature will break existing code if TypeScript now infers a more precise type than you want. For example:

 tsx ` // Previously, nums: (number | null)[] // Now, nums: number[] const nums = [ 1 , 2 , 3 , null , 5 ]. filter ( x => x !== null ); nums . push ( null ); // ok in TS 5.4, error in TS 5.5 `
 The fix is to tell TypeScript the type that you want using an explicit type annotation:

 tsx ` const nums : ( number | null )[] = [ 1 , 2 , 3 , null , 5 ]. filter ( x => x !== null ); nums . push ( null ); // ok in all versions `
 For more information, check out the implementing pull request and Dan’s blog post about implementing this feature .

## Control Flow Narrowing for Constant Indexed Accesses

 TypeScript is now able to narrow expressions of the form `obj[key]` when both `obj` and `key` are effectively constant.

 ts ` function f1 ( obj : Record < string , unknown >, key : string ) { if ( typeof obj [ key ] === "string" ) { // Now okay, previously was error obj [ key ]. toUpperCase (); } } `
 In the above, neither `obj` nor `key` are ever mutated, so TypeScript can narrow the type of `obj[key]` to `string` after the `typeof` check.
For more information, see the implementing pull request here .

## The JSDoc `@import` Tag

 Today, if you want to import something only for type-checking in a JavaScript file, it is cumbersome.
JavaScript developers can’t simply import a type named `SomeType` if it’s not there at runtime.

 js ` // ./some-module.d.ts export interface SomeType { // ... } // ./index.js import { SomeType } from "./some-module" ; // ❌ runtime error! /** * @param {SomeType} myValue */ function doSomething ( myValue ) { // ... } `
 `SomeType` won’t exist at runtime, so the import will fail.
Developers can instead use a namespace import instead.

 js ` import * as someModule from "./some-module" ; /** * @param {someModule.SomeType} myValue */ function doSomething ( myValue ) { // ... } `
 But `./some-module` is still imported at runtime - which might also not be desirable.

To avoid this, developers typically had to use `import(...)` types in JSDoc comments.

 js ` /** * @param {import("./some-module").SomeType} myValue */ function doSomething ( myValue ) { // ... } `
 If you wanted to reuse the same type in multiple places, you could use a `typedef` to avoid repeating the import.

 js ` /** * @typedef {import("./some-module").SomeType} SomeType */ /** * @param {SomeType} myValue */ function doSomething ( myValue ) { // ... } `
 This helps with local uses of `SomeType`, but it gets repetitive for many imports and can be a bit verbose.

That’s why TypeScript now supports a new `@import` comment tag that has the same syntax as ECMAScript imports.

 js ` /** @import { SomeType } from "some-module" */ /** * @param {SomeType} myValue */ function doSomething ( myValue ) { // ... } `
 Here, we used named imports.
We could also have written our import as a namespace import.

 js ` /** @import * as someModule from "some-module" */ /** * @param {someModule.SomeType} myValue */ function doSomething ( myValue ) { // ... } `
 Because these are just JSDoc comments, they don’t affect runtime behavior at all.

We would like to extend a big thanks to Oleksandr Tarasiuk who contributed this change !

## Regular Expression Syntax Checking

 Until now, TypeScript has typically skipped over most regular expressions in code.
This is because regular expressions technically have an extensible grammar and TypeScript never made any effort to compile regular expressions to earlier versions of JavaScript.
Still, this meant that lots of common problems would go undiscovered in regular expressions, and they would either turn into errors at runtime, or silently fail.

But TypeScript now does basic syntax checking on regular expressions!

 ts ` let myRegex = /@robot ( \s + ( please | immediately )) ) ? do some task/ ; // ~ // error! // Unexpected ')'. Did you mean to escape it with backslash? `
 This is a simple example, but this checking can catch a lot of common mistakes.
In fact, TypeScript’s checking goes slightly beyond syntactic checks.
For instance, TypeScript can now catch issues around backreferences that don’t exist.

 ts ` let myRegex = /@typedef \{ import \( ( . + ) \)\. ([ a-zA-Z_ ] + ) \} \3 / u ; // ~ // error! // This backreference refers to a group that does not exist. // There are only 2 capturing groups in this regular expression. `
 The same applies to named capturing groups.

 ts ` let myRegex = /@typedef \{ import \( (?< importPath > . + ) \)\. (?< importedEntity >[ a-zA-Z_ ] + ) \} \k< namedImport > / ; // ~~~~~~~~~~~ // error! // There is no capturing group named 'namedImport' in this regular expression. `
 TypeScript’s checking is now also aware of when certain RegExp features are used when newer than your target version of ECMAScript.
For example, if we use named capturing groups like the above in an ES5 target, we’ll get an error.

 ts ` let myRegex = /@typedef \{ import \( (?< importPath > . + ) \)\. (?< importedEntity >[ a-zA-Z_ ] + ) \} \k< importedEntity > / ; // ~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~ // error! // Named capturing groups are only available when targeting 'ES2018' or later. `
 The same is true for certain regular expression flags as well.

Note that TypeScript’s regular expression support is limited to regular expression literals .
If you try calling `new RegExp` with a string literal, TypeScript will not check the provided string.

We would like to thank GitHub user graphemecluster who iterated a ton with us to get this feature into TypeScript .

## Support for New ECMAScript `Set` Methods

 TypeScript 5.5 declares new proposed methods for the ECMAScript `Set` type .

Some of these methods, like `union`, `intersection`, `difference`, and `symmetricDifference`, take another `Set` and return a new `Set` as the result.
The other methods, `isSubsetOf`, `isSupersetOf`, and `isDisjointFrom`, take another `Set` and return a `boolean`.
None of these methods mutate the original `Set`s.

Here’s a quick example of how you might use these methods and how they behave:

 ts ` let fruits = new Set ([ "apples" , "bananas" , "pears" , "oranges" ]); let applesAndBananas = new Set ([ "apples" , "bananas" ]); let applesAndOranges = new Set ([ "apples" , "oranges" ]); let oranges = new Set ([ "oranges" ]); let emptySet = new Set (); //// // union //// // Set(4) {'apples', 'bananas', 'pears', 'oranges'} console . log ( fruits . union ( oranges )); // Set(3) {'apples', 'bananas', 'oranges'} console . log ( applesAndBananas . union ( oranges )); //// // intersection //// // Set(2) {'apples', 'bananas'} console . log ( fruits . intersection ( applesAndBananas )); // Set(0) {} console . log ( applesAndBananas . intersection ( oranges )); // Set(1) {'apples'} console . log ( applesAndBananas . intersection ( applesAndOranges )); //// // difference //// // Set(3) {'apples', 'bananas', 'pears'} console . log ( fruits . difference ( oranges )); // Set(2) {'pears', 'oranges'} console . log ( fruits . difference ( applesAndBananas )); // Set(1) {'bananas'} console . log ( applesAndBananas . difference ( applesAndOranges )); //// // symmetricDifference //// // Set(2) {'bananas', 'oranges'} console . log ( applesAndBananas . symmetricDifference ( applesAndOranges )); // no apples //// // isDisjointFrom //// // true console . log ( applesAndBananas . isDisjointFrom ( oranges )); // false console . log ( applesAndBananas . isDisjointFrom ( applesAndOranges )); // true console . log ( fruits . isDisjointFrom ( emptySet )); // true console . log ( emptySet . isDisjointFrom ( emptySet )); //// // isSubsetOf //// // true console . log ( applesAndBananas . isSubsetOf ( fruits )); // false console . log ( fruits . isSubsetOf ( applesAndBananas )); // false console . log ( applesAndBananas . isSubsetOf ( oranges )); // true console . log ( fruits . isSubsetOf ( fruits )); // true console . log ( emptySet . isSubsetOf ( fruits )); //// // isSupersetOf //// // true console . log ( fruits . isSupersetOf ( applesAndBananas )); // false console . log ( applesAndBananas . isSupersetOf ( fruits )); // false console . log ( applesAndBananas . isSupersetOf ( oranges )); // true console . log ( fruits . isSupersetOf ( fruits )); // false console . log ( emptySet . isSupersetOf ( fruits )); `
 We’d like to thank Kevin Gibbons who not only co-championed the feature in ECMAScript, but also provided the declarations for `Set`, `ReadonlySet`, and `ReadonlySetLike` in TypeScript !

## Isolated Declarations

 This section was co-authored by Rob Palmer who supported the design of isolated declarations.

Declaration files (a.k.a. `.d.ts` files) describe the shape of existing libraries and modules to TypeScript.
This lightweight description includes the library’s type signatures and excludes implementation details such as the function bodies.
They are published so that TypeScript can efficiently check your usage of a library without needing to analyse the library itself.
Whilst it is possible to handwrite declaration files, if you are authoring typed code, it’s much safer and simpler to let TypeScript generate them automatically from source files using `--declaration`.

The TypeScript compiler and its APIs have always had the job of generating declaration files;
however, there are some use-cases where you might want to use other tools, or where the traditional build process doesn’t scale.

### Use-case: Faster Declaration Emit Tools

 Imagine if you wanted to create a faster tool to generate declaration files, perhaps as part of a publishing service or a new bundler.
Whilst there is a thriving ecosystem of blazing fast tools that can turn TypeScript into JavaScript, the same is not true for turning TypeScript into declaration files.
The reason is that TypeScript’s inference allows us to write code without explicitly declaring types, meaning declaration emit can be complex.

Let’s consider a simple example of a function that adds two imported variables.

 ts ` // util.ts export let one = "1" ; export let two = "2" ; // add.ts import { one , two } from "./util" ; export function add () { return one + two ; } `
 Even if the only thing we want to do is generate `add.d.ts`, TypeScript needs to crawl into another imported file (`util.ts`), infer that the type of `one` and `two` are strings, and then calculate that the `+` operator on two strings will lead to a `string` return type.

 ts ` // add.d.ts export declare function add (): string ; `
 While this inference is important for the developer experience, it means that tools that want to generate declaration files would need to replicate parts of the type-checker including inference and the ability to resolve module specifiers to follow the imports.

### Use-case: Parallel Declaration Emit and Parallel Checking

 Imagine if you had a monorepo containing many projects and a multi-core CPU that just wished it could help you check your code faster.
Wouldn’t it be great if we could check all those projects at the same time by running each project on a different core?

Unfortunately we don’t have the freedom to do all the work in parallel.
The reason is that we have to build those projects in dependency order, because each project is checking against the declaration files of their dependencies.
So we must build the dependency first to generate the declaration files.
TypeScript’s project references feature works the same way, building the set of projects in “topological” dependency order.

As an example, if we have two projects called `backend` and `frontend`, and they both depend on a project called `core`, TypeScript can’t start type-checking either `frontend` or `backend` until `core` has been built and its declaration files have been generated.

In the above graph, you can see that we have a bottleneck.
Whilst we can build `frontend` and `backend` in parallel, we need to first wait for `core` to finish building before either can start.

How could we improve upon this?
Well, if a fast tool could generate all those declaration files for `core` in parallel , TypeScript then could immediately follow that by type-checking `core`, `frontend`, and `backend` also in parallel .

### Solution: Explicit Types!

 The common requirement in both use-cases is that we need a cross-file type-checker to generate declaration files.
Which is a lot to ask from the tooling community.

As a more complex example, if we want a declaration file for the following code…

 ts ` import { add } from "./add" ; const x = add (); export function foo () { return x ; } `
 …we would need to generate a signature for `foo`.
Well that requires looking at the implementation of `foo`.
`foo` just returns `x`, so getting the type of `x` requires looking at the implementation of `add`.
But that might require looking at the implementation of `add`’s dependencies, and so on.
What we’re seeing here is that generating declaration files requires a whole lot of logic to figure out the types of different places that might not even be local to the current file.

Still, for developers looking for fast iteration time and fully parallel builds, there is another way of thinking about this problem.
A declaration file only requires the types of the public API of a module - in other words, the types of the things that are exported.
If, controversially, developers are willing to explicitly write out the types of the things they export, tools could generate declaration files without needing to look at the implementation of the module - and without reimplementing a full type-checker.

This is where the new `--isolatedDeclarations` option comes in.
`--isolatedDeclarations` reports errors when a module can’t be reliably transformed without a type-checker.
More plainly, it makes TypeScript report errors if you have a file that isn’t sufficiently annotated on its exports.

That means in the above example, we would see an error like the following:

 ts ` export function foo () { // ~~~ // error! Function must have an explicit // return type annotation with --isolatedDeclarations. return x ; } `

### Why are errors desirable?

 Because it means that TypeScript can

- Tell us up-front whether other tools will have issues with generating declaration files

- Provide a quick fix to help add these missing annotations.

This mode doesn’t require annotations everywhere though.
For locals, these can be ignored, since they don’t affect the public API.
For example, the following code would not produce an error:

 ts ` import { add } from "./add" ; const x = add ( "1" , "2" ); // no error on 'x', it's not exported. export function foo (): string { return x ; } `
 There are also certain expressions where the type is “trivial” to calculate.

 ts ` // No error on 'x'. // It's trivial to calculate the type is 'number' export let x = 10 ; // No error on 'y'. // We can get the type from the return expression. export function y () { return 20 ; } // No error on 'z'. // The type assertion makes it clear what the type is. export function z () { return Math . max ( x , y ()) as number ; } `

### Using `isolatedDeclarations`

 `isolatedDeclarations` requires that either the `declaration` or `composite` flags are also set.

Note that `isolatedDeclarations` does not change how TypeScript performs emit - just how it reports errors.
Importantly, and similar to `isolatedModules`, enabling the feature in TypeScript won’t immediately bring about the potential benefits discussed here.
So please be patient and look forward to future developments in this space.
Keeping tool authors in mind, we should also recognize that today, not all of TypeScript’s declaration emit can be easily replicated by other tools wanting to use it as a guide.
That’s something we’re actively working on improving.

On top of this, isolated declarations are still a new feature, and we’re actively working on improving the experience.
Some scenarios, like using computed property declarations in classes and object literals, are not yet supported under `isolatedDeclarations`.
Keep an eye on this space, and feel free to provide us with feedback.

We also feel it is worth calling out that `isolatedDeclarations` should be adopted on a case-by-case basis.
There are some developer ergonomics that are lost when using `isolatedDeclarations`, and thus it may not be the right choice if your setup is not leveraging the two scenarios mentioned earlier.
For others, the work on `isolatedDeclarations` has already uncovered many optimizations and opportunities to unlock different parallel build strategies.
In the meantime, if you’re willing to make the trade-offs, we believe `isolatedDeclarations` can be a powerful tool to speed up your build process as external tooling becomes more widely available.

For more information, read up on the Isolated Declarations: State of the Feature discussion on the TypeScript issue tracker.

### Credit

 Work on `isolatedDeclarations` has been a long-time collaborative effort between the TypeScript team and the infrastructure and tooling teams within Bloomberg and Google.
Individuals like Hana Joo from Google who implemented the quick fix for isolated declaration errors (more on that soon), as well as Ashley Claymore, Jan Kühle, Lisa Velden, Rob Palmer, and Thomas Chetwin have been involved in discussion, specification, and implementation for many months.
But we feel it is specifically worth calling out the tremendous amount of work provided by Titian Cernicova-Dragomir from Bloomberg.
Titian has been instrumental in driving the implementation of `isolatedDeclarations` and has been a contributor to the TypeScript project for years prior.

While the feature involved many changes, you can see the core work for Isolated Declarations here .

## The `${configDir}` Template Variable for Configuration Files

 It’s common in many codebases to reuse a shared `tsconfig.json` file that acts as a “base” for other configuration files.
This is done by using the `extends` field in a `tsconfig.json` file.

 json ` { "extends" : "../../tsconfig.base.json" , "compilerOptions" : { "outDir" : "./dist" } } `
 One of the issues with this is that all paths in the `tsconfig.json` file are relative to the location of the file itself.
This means that if you have a shared `tsconfig.base.json` file that is used by multiple projects, relative paths often won’t be useful in the derived projects.
For example, imagine the following `tsconfig.base.json`:

 json ` { "compilerOptions" : { "typeRoots" : [ "./node_modules/@types" , "./custom-types" ], "outDir" : "dist" } } `
 If author’s intent was that every `tsconfig.json` that extends this file should

- output to a `dist` directory relative to the derived `tsconfig.json` , and

- have a `custom-types` directory relative to the derived `tsconfig.json`,

then this would not work.
The `typeRoots` paths would be relative to the location of the shared `tsconfig.base.json` file, not the project that extends it.
Each project that extends this shared file would need to declare its own `outDir` and `typeRoots` with identical contents.
This could be frustrating and hard to keep in sync between projects, and while the example above is using `typeRoots`, this is a common problem for `paths` and other options.

To solve this, TypeScript 5.5 introduces a new template variable `${configDir}`.
When `${configDir}` is written in certain path fields of a `tsconfig.json` or `jsconfig.json` files, this variable is substituted with the containing directory of the configuration file in a given compilation.
This means that the above `tsconfig.base.json` could be rewritten as:

 json ` { "compilerOptions" : { "typeRoots" : [ "${configDir}/node_modules/@types" , "${configDir}/custom-types" ], "outDir" : "${configDir}/dist" } } `
 Now, when a project extends this file, the paths will be relative to the derived `tsconfig.json`, not the shared `tsconfig.base.json` file.
This makes it easier to share configuration files across projects and ensures that the configuration files are more portable.

If you intend to make a `tsconfig.json` file extendable, consider if a `./` should instead be written with `${configDir}`.

For more information, see the proposal issue and the implementing pull request .

## Consulting `package.json` Dependencies for Declaration File Generation

 Previously, TypeScript would often issue an error message like

 ` The inferred type of "X" cannot be named without a reference to "Y". This is likely not portable. A type annotation is necessary. `
 This was often due to TypeScript’s declaration file generation finding itself in the contents of files that were never explicitly imported in a program.
Generating an import to such a file could be risky if the path ended up being relative.
Still, for codebases with explicit dependencies in the `dependencies` (or `peerDependencies` and `optionalDependencies`) of a `package.json`, generating such an import should be safe under certain resolution modes.
So in TypeScript 5.5, we’re more lenient when that’s the case, and many occurrences of this error should disappear.

 See this pull request for more details on the change.

## Editor and Watch-Mode Reliability Improvements

 TypeScript has either added some new functionality or fixed existing logic that makes `--watch` mode and TypeScript’s editor integration feel more reliable.
That should hopefully translate to fewer TSServer/editor restarts.

### Correctly Refresh Editor Errors in Configuration Files

 TypeScript can generate errors for `tsconfig.json` files;
however, those errors are actually generated from loading a project, and editors typically don’t directly request those errors for `tsconfig.json` files.
While this sounds like a technical detail, it means that when all errors issued in a `tsconfig.json` are fixed, TypeScript doesn’t issue a new fresh empty set of errors, and users are left with stale errors unless they reload their editor.

TypeScript 5.5 now intentionally issues an event to clear these out.
 See more here .

### Better Handling for Deletes Followed by Immediate Writes

 Instead of overwriting files, some tools will opt to delete them and then create new files from scratch.
This is the case when running `npm ci`, for instance.

While this can be efficient for those tools, it can be problematic for TypeScript’s editor scenarios where deleting a watched might dispose of it and all of its transitive dependencies.
Deleting and creating a file in quick succession could lead to TypeScript tearing down an entire project and then rebuilding it from scratch.

TypeScript 5.5 now has a more nuanced approach by keeping parts of a deleted project around until it picks up on a new creation event.
This should make operations like `npm ci` work a lot better with TypeScript.
See more information on the approach here .

### Symlinks are Tracked in Failed Resolutions

 When TypeScript fails to resolve a module, it will still need to watch for any failed lookup paths in case the module is added later.
Previously this was not done for symlinked directories, which could cause reliability issues in monorepo-like scenarios when a build occurred in one project but was not witnessed in the other.
This should be fixed in TypeScript 5.5, and means you won’t need to restart your editor as often.

 See more information here .

### Project References Contribute to Auto-Imports

 Auto-imports no longer requires at least one explicit import to dependent projects in a project reference setup.
Instead, auto-import completions should just work across anything you’ve listed in the `references` field of your `tsconfig.json`.

 See more on the implementing pull request .

## Performance and Size Optimizations

### Monomorphized Objects in Language Service and Public API

 In TypeScript 5.0, we ensured that our `Node` and `Symbol` objects had a consistent set of properties with a consistent initialization order.
Doing so helps reduce polymorphism in different operations, which allows runtimes to fetch properties more quickly.

By making this change, we witnessed impressive speed wins in the compiler;
however, most of these changes were performed on internal allocators for our data structures.
The language service, along with TypeScript’s public API, uses a different set of allocators for certain objects.
This allowed the TypeScript compiler to be a bit leaner, as data used only for the language service would never be used in the compiler.

In TypeScript 5.5, the same monomorphization work has been done for the language service and public API.
What this means is that your editor experience, and any build tools that use the TypeScript API, will get a decent amount faster.
In fact, in our benchmarks, we’ve seen a 5-8% speedup in build times when using the public TypeScript API’s allocators, and language service operations getting 10-20% faster .
While this does imply an increase in memory, we believe that tradeoff is worth it and hope to find ways to reduce that memory overhead.
Things should feel a lot snappier now.

For more information, see the change here .

### Monomorphized Control Flow Nodes

 In TypeScript 5.5, nodes of the control flow graph have been monomorphized so that they always hold a consistent shape.
By doing so, check times will often be reduced by about 1%.

 See this change here .

### Optimizations on our Control Flow Graph

 In many cases, control flow analysis will traverse nodes that don’t provide any new information.
We observed that in the absence of any early termination or effects in the antecedents (or “dominators”) of certain nodes meant that those nodes could always be skipped over.
As such, TypeScript now constructs its control flow graphs to take advantage of this by linking to an earlier node that does provide interesting information for control flow analysis.
This yields a flatter control flow graph, which can be more efficient to traverse.
This optimization has yielded modest gains, but with up to 2% reductions in build time on certain codebases.

You can read more here .

### Skipped Checking in `transpileModule` and `transpileDeclaration`

 TypeScript’s `transpileModule` API can be used for compiling a single TypeScript file’s contents into JavaScript.
Similarly, the `transpileDeclaration` API (see below) can be used to generate a declaration file for a single TypeScript file.
One of the issues with these APIs is that TypeScript internally would perform a full type-checking pass over the entire contents of the file before emitting the output.
This was necessary to collect certain information which would later be used for the emit phase.

In TypeScript 5.5, we’ve found a way to avoid performing a full check, only lazily collecting this information as necessary, and `transpileModule` and `transpileDeclaration` both enable this functionality by default.
As a result, tools that integrate with these APIs, like ts-loader with `transpileOnly` and ts-jest , should see a noticeable speedup.
In our testing, we generally witness around a 2x speed-up in build time using `transpileModule` .

### TypeScript Package Size Reduction

 Further leveraging our transition to modules in 5.0 , we’ve significantly reduced TypeScript’s overall package size by making `tsserver.js` and `typingsInstaller.js` import from a common API library instead of having each of them produce standalone bundles .

This reduces TypeScript’s size on disk from 30.2 MB to 20.4 MB, and reduces its packed size from 5.5 MB to 3.7 MB!

### Node Reuse in Declaration Emit

 As part of the work to enable `isolatedDeclarations`, we’ve substantially improved how often TypeScript can directly copy your input source code when producing declaration files.

For example, let’s say you wrote

 ts ` export const strBool : string | boolean = "hello" ; export const boolStr : boolean | string = "world" ; `
 Note that the union types are equivalent, but the order of the union is different.
When emitting the declaration file, TypeScript has two equivalent output possibilities.

The first is to use a consistent canonical representation for each type:

 ts ` export const strBool : string | boolean ; export const boolStr : string | boolean ; `
 The second is to re-use the type annotations exactly as written:

 ts ` export const strBool : string | boolean ; export const boolStr : boolean | string ; `
 The second approach is generally preferable for a few reasons:

- Many equivalent representations still encode some level of intent that is better to preserve in the declaration file

- Producing a fresh representation of a type can be somewhat expensive, so avoiding is better

- User-written types are usually shorter than generated type representations

In 5.5, we’ve greatly improved the number of places where TypeScript can correctly identify places where it’s safe and correct to print back types exactly as they were written in the input file.
Many of these cases are invisible performance improvements - TypeScript would generate fresh sets of syntax nodes and serialize them into a string.
Instead, TypeScript can now operate over the original syntax nodes directly, which is much cheaper and faster.

### Caching Contextual Types from Discriminated Unions

 When TypeScript asks for the contextual type of an expression like an object literal, it will often encounter a union type.
In those cases, TypeScript tries to filter out members of the union based on known properties with well known values (i.e. discriminant properties).
This work can be fairly expensive, especially if you end up with an object consisting of many many properties.
In TypeScript 5.5, much of the computation is cached once so that TypeScript doesn’t need to recompute it for every property in the object literal .
Performing this optimization shaved 250ms off of compiling the TypeScript compiler itself.

## Easier API Consumption from ECMAScript Modules

 Previously, if you were writing an ECMAScript module in Node.js, named imports were not available from the `typescript` package.

 ts ` import { createSourceFile } from "typescript" ; // ❌ error import * as ts from "typescript" ; ts . createSourceFile // ❌ undefined??? ts . default . createSourceFile // ✅ works - but ugh! `
 This is because cjs-module-lexer did not recognize the pattern of TypeScript’s generated CommonJS code.
This has been fixed, and users can now use named imports from the TypeScript npm package with ECMAScript modules in Node.js.

 ts ` import { createSourceFile } from "typescript" ; // ✅ works now! import * as ts from "typescript" ; ts . createSourceFile // ✅ works now! `
 For more information, see the change here .

## The `transpileDeclaration` API

 TypeScript’s API exposes a function called `transpileModule`.
It’s intended to make it easy to compile a single file of TypeScript code.
Because it doesn’t have access to an entire program , the caveat is that it may not produce the right output if the code violates any errors under the `isolatedModules` option.

In TypeScript 5.5, we’ve added a new similar API called `transpileDeclaration`.
This API is similar to `transpileModule`, but it’s specifically designed to generate a single declaration file based on some input source text.
Just like `transpileModule`, it doesn’t have access to a full program, and a similar caveat applies: it only generates an accurate declaration file if the input code is free of errors under the new `isolatedDeclarations` option.

If desired, this function can be used to parallelize declaration emit across all files under `isolatedDeclarations` mode.

For more information, see the implementation here .

## Notable Behavioral Changes

 This section highlights a set of noteworthy changes that should be acknowledged and understood as part of any upgrade.
Sometimes it will highlight deprecations, removals, and new restrictions.
It can also contain bug fixes that are functionally improvements, but which can also affect an existing build by introducing new errors.

### Disabling Features Deprecated in TypeScript 5.0

 TypeScript 5.0 deprecated the following options and behaviors:

- `charset`

- `target: ES3`

- `importsNotUsedAsValues`

- `noImplicitUseStrict`

- `noStrictGenericChecks`

- `keyofStringsOnly`

- `suppressExcessPropertyErrors`

- `suppressImplicitAnyIndexErrors`

- `out`

- `preserveValueImports`

- `prepend` in project references

- implicitly OS-specific `newLine`

To continue using the deprecated options above, developers using TypeScript 5.0 and other more recent versions have had to specify a new option called `ignoreDeprecations` with the value `"5.0"`.

In TypeScript 5.5, these options no longer have any effect.
To help with a smooth upgrade path, you may still specify them in your tsconfig, but these will be an error to specify in TypeScript 6.0.
See also the Flag Deprecation Plan which outlines our deprecation strategy.

 More information around these deprecation plans is available on GitHub , which contains suggestions in how to best adapt your codebase.

### `lib.d.ts` Changes

 Types generated for the DOM may have an impact on type-checking your codebase.
For more information, see the DOM updates for TypeScript 5.5 .

### Stricter Parsing for Decorators

 Since TypeScript originally introduced support for decorators, the specified grammar for the proposal has been tightened up.
TypeScript is now stricter about what forms it allows.
While rare, existing decorators may need to be parenthesized to avoid errors.

 ts ` class DecoratorProvider { decorate (... args : any []) { } } class D extends DecoratorProvider { m () { class C { @ super . decorate // ❌ error method1 () { } @( super . decorate ) // ✅ okay method2 () { } } } } `
 See more information on the change here .

### `undefined` is No Longer a Definable Type Name

 TypeScript has always disallowed type alias names that conflict with built-in types:

 ts ` // Illegal type null = any ; // Illegal type number = any ; // Illegal type object = any ; // Illegal type any = any ; `
 Due to a bug, this logic didn’t also apply to the built-in type `undefined`.
In 5.5, this is now correctly identified as an error:

 ts ` // Now also illegal type undefined = any ; `
 Bare references to type aliases named `undefined` never actually worked in the first place.
You could define them, but you couldn’t use them as an unqualified type name.

 ts ` export type undefined = string ; export const m : undefined = "" ; // ^ // Errors in 5.4 and earlier - the local definition of 'undefined' was not even consulted. `
 For more information, see the change here .

### Simplified Reference Directive Declaration Emit

 When producing a declaration file, TypeScript would synthesize a reference directive when it believed one was required.
For example, all Node.js modules are declared ambiently, so cannot be loaded by module resolution alone.
A file like:

 tsx ` import path from "path" ; export const myPath = path . parse ( __filename ); `
 Would emit a declaration file like:

 tsx ` /// <reference types = "node" /> import path from "path" ; export declare const myPath : path . ParsedPath ; `
 Even though the reference directive never appeared in the original source.

Similarly, TypeScript also removed reference directives that it did not believe needed to be a part of the output.
For example, let’s imagine we had a reference directive to `jest`;
however, imagine the reference directive isn’t necessary to generate the declaration file.
TypeScript would simply drop it.
So in the following example:

 tsx ` /// <reference types = "jest" /> import path from "path" ; export const myPath = path . parse ( __filename ); `
 TypeScript would still emit:

 tsx ` /// <reference types = "node" /> import path from "path" ; export declare const myPath : path . ParsedPath ; `
 In the course of working on `isolatedDeclarations`, we realized that this logic was untenable for anyone attempting to implement a declaration emitter without type checking or using more than a single file’s context.
This behavior is also hard to understand from a user’s perspective; whether or not a reference directive appeared in the emitted file seems inconsistent and difficult to predict unless you understand exactly what’s going on during typechecking.
To prevent declaration emit from being different when `isolatedDeclarations` was enabled, we knew that our emit needed to change.

Through experimentation , we found that nearly all cases where TypeScript synthesized reference directives were just to pull in `node` or `react`.
These are cases where the expectation is that a downstream user already references those types through tsconfig.json `"types"` or library imports, so no longer synthesizing these reference directives would be unlikely to break anyone.
It’s worth noting that this is already how it works for `lib.d.ts`; TypeScript doesn’t synthesize a reference to `lib="es2015"` when a module exports a `WeakMap`, instead assuming that a downstream user will have included that as part of their environment.

For reference directives that had been written by library authors (not synthesized), further experimentation showed that nearly all were removed, never showing up in the output.
Most reference directives that were preserved were broken and likely not intended to be preserved.

Given those results, we decided to greatly simplfy reference directives in declaration emit in TypeScript 5.5.
A more consistent strategy will help library authors and consumers have better control of their declaration files.

Reference directives are no longer synthesized.
User-written reference directives are no longer preserved, unless annotated with a new `preserve="true"` attribute.
Concretely, an input file like:

 tsx ` /// <reference types="some-lib" preserve="true" /> /// <reference types = "jest" /> import path from "path" ; export const myPath = path . parse ( __filename ); `
 will emit:

 tsx ` /// <reference types="some-lib" preserve="true" /> import path from "path" ; export declare const myPath : path . ParsedPath ; `
 Adding `preserve="true"` is backwards compatible with older versions of TypeScript as unknown attributes are ignored.

This change also improved performance; in our benchmarks, the emit stage saw a 1-4% improvement in projects with declaration emit enabled.
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: N BS DR Last updated: Jun 15, 2026

## Typescript 5 4

Was this page helpful?

# TypeScript 5.4

## Preserved Narrowing in Closures Following Last Assignments

 TypeScript can usually figure out a more specific type for a variable based on checks that you might perform.
This process is called narrowing.

 ts ` function uppercaseStrings ( x : string | number ) { if ( typeof x === "string" ) { // TypeScript knows 'x' is a 'string' here. return x . toUpperCase (); } } `
 One common pain point was that these narrowed types weren’t always preserved within function closures.

 ts ` function getUrls ( url : string | URL , names : string []) { if ( typeof url === "string" ) { url = new URL ( url ); } return names . map ( name => { url . searchParams . set ( "name" , name ) // ~~~~~~~~~~~~ // error! // Property 'searchParams' does not exist on type 'string | URL'. return url . toString (); }); } `
 Here, TypeScript decided that it wasn’t “safe” to assume that `url` was actually a `URL` object in our callback function because it was mutated elsewhere;
however, in this instance, that arrow function is always created after that assignment to `url`, and it’s also the last assignment to `url`.

TypeScript 5.4 takes advantage of this to make narrowing a little smarter.
When parameters and `let` variables are used in non- hoisted functions, the type-checker will look for a last assignment point.
If one is found, TypeScript can safely narrow from outside the containing function.
What that means is the above example just works now.

Note that narrowing analysis doesn’t kick in if the variable is assigned anywhere in a nested function.
This is because there’s no way to know for sure whether the function will be called later.

 ts ` function printValueLater ( value : string | undefined ) { if ( value === undefined ) { value = "missing!" ; } setTimeout (() => { // Modifying 'value', even in a way that shouldn't affect // its type, will invalidate type refinements in closures. value = value ; }, 500 ); setTimeout (() => { console . log ( value . toUpperCase ()); // ~~~~~ // error! 'value' is possibly 'undefined'. }, 1000 ); } `
 This should make lots of typical JavaScript code easier to express.
You can read more about the change on GitHub .

## The `NoInfer` Utility Type

 When calling generic functions, TypeScript is able to infer type arguments from whatever you pass in.

 ts ` function doSomething < T >( arg : T ) { // ... } // We can explicitly say that 'T' should be 'string'. doSomething < string >( "hello!" ); // We can also just let the type of 'T' get inferred. doSomething ( "hello!" ); `
 One challenge, however, is that it is not always clear what the “best” type is to infer.
This might lead to TypeScript rejecting valid calls, accepting questionable calls, or just reporting worse error messages when it catches a bug.

For example, let’s imagine a `createStreetLight` function that takes a list of color names, along with an optional default color.

 ts ` function createStreetLight < C extends string >( colors : C [], defaultColor ?: C ) { // ... } createStreetLight ([ "red" , "yellow" , "green" ], "red" ); `
 What happens when we pass in a `defaultColor` that wasn’t in the original `colors` array?
In this function, `colors` is supposed to be the “source of truth” and describe what can be passed to `defaultColor`.

 ts ` // Oops! This is undesirable, but is allowed! createStreetLight ([ "red" , "yellow" , "green" ], "blue" ); `
 In this call, type inference decided that `"blue"` was just as valid of a type as `"red"` or `"yellow"` or `"green"`.
So instead of rejecting the call, TypeScript infers the type of `C` as `"red" | "yellow" | "green" | "blue"`.
You might say that inference just blue up in our faces!

One way people currently deal with this is to add a separate type parameter that’s bounded by the existing type parameter.

 ts ` function createStreetLight < C extends string , D extends C >( colors : C [], defaultColor ?: D ) { } createStreetLight ([ "red" , "yellow" , "green" ], "blue" ); // ~~~~~~ // error! // Argument of type '"blue"' is not assignable to parameter of type '"red" | "yellow" | "green" | undefined'. `
 This works, but is a little bit awkward because `D` probably won’t be used anywhere else in the signature for `createStreetLight`.
While not bad in this case , using a type parameter only once in a signature is often a code smell.

That’s why TypeScript 5.4 introduces a new `NoInfer&#x3C;T>` utility type.
Surrounding a type in `NoInfer&#x3C;...>` gives a signal to TypeScript not to dig in and match against the inner types to find candidates for type inference.

Using `NoInfer`, we can rewrite `createStreetLight` as something like this:

 ts ` function createStreetLight < C extends string >( colors : C [], defaultColor ?: NoInfer < C >) { // ... } createStreetLight ([ "red" , "yellow" , "green" ], "blue" ); // ~~~~~~ // error! // Argument of type '"blue"' is not assignable to parameter of type '"red" | "yellow" | "green" | undefined'. `
 Excluding the type of `defaultColor` from being explored for inference means that `"blue"` never ends up as an inference candidate, and the type-checker can reject it.

You can see the specific changes in the implementing pull request , along with the initial implementation provided thanks to Mateusz Burzyński !

## `Object.groupBy` and `Map.groupBy`

 TypeScript 5.4 adds declarations for JavaScript’s new `Object.groupBy` and `Map.groupBy` static methods.

`Object.groupBy` takes an iterable, and a function that decides which “group” each element should be placed in.
The function needs to make a “key” for each distinct group, and `Object.groupBy` uses that key to make an object where every key maps to an array with the original element in it.

So the following JavaScript:

 js ` const array = [ 0 , 1 , 2 , 3 , 4 , 5 ]; const myObj = Object . groupBy ( array , ( num , index ) => { return num % 2 === 0 ? "even" : "odd" ; }); `
 is basically equivalent to writing this:

 js ` const myObj = { even: [ 0 , 2 , 4 ], odd: [ 1 , 3 , 5 ], }; `
 `Map.groupBy` is similar, but produces a `Map` instead of a plain object.
This might be more desirable if you need the guarantees of `Map`s, you’re dealing with APIs that expect `Map`s, or you need to use any kind of key for grouping - not just keys that can be used as property names in JavaScript.

 js ` const myObj = Map . groupBy ( array , ( num , index ) => { return num % 2 === 0 ? "even" : "odd" ; }); `
 and just as before, you could have created `myObj` in an equivalent way:

 js ` const myObj = new Map (); myObj . set ( "even" , [ 0 , 2 , 4 ]); myObj . set ( "odd" , [ 1 , 3 , 5 ]); `
 Note that in the above example of `Object.groupBy`, the object produced uses all optional properties.

 ts ` interface EvenOdds { even ?: number []; odd ?: number []; } const myObj : EvenOdds = Object . groupBy (...); myObj . even ; // ~~~~ // Error to access this under 'strictNullChecks'. `
 This is because there’s no way to guarantee in a general way that all the keys were produced by `groupBy`.

Note also that these methods are only accessible by configuring your `target` to `esnext` or adjusting your `lib` settings.
We expect they will eventually be available under a stable `es2024` target.

We’d like to extend a thanks to Kevin Gibbons for adding the declarations to these `groupBy` methods .

## Support for `require()` calls in `--moduleResolution bundler` and `--module preserve`

 TypeScript has a `moduleResolution` option called `bundler` that is meant to model the way modern bundlers figure out which file an import path refers to.
One of the limitations of the option is that it had to be paired with `--module esnext`, making it impossible to use the `import ... = require(...)` syntax.

 ts ` // previously errored import myModule = require ( "module/path" ); `
 That might not seem like a big deal if you’re planning on just writing standard ECMAScript `import`s, but there’s a difference when using a package with conditional exports .

In TypeScript 5.4, `require()` can now be used when setting the `module` setting to a new option called `preserve`.

Between `--module preserve` and `--moduleResolution bundler`, the two more accurately model what bundlers and runtimes like Bun will allow, and how they’ll perform module lookups.
In fact, when using `--module preserve`, the `bundler` option will be implicitly set for `--moduleResolution` (along with `--esModuleInterop` and `--resolveJsonModule`)

 json ` { "compilerOptions" : { "module" : "preserve" , // ^ also implies: // "moduleResolution": "bundler", // "esModuleInterop": true, // "resolveJsonModule": true, // ... } } `
 Under `--module preserve`, an ECMAScript `import` will always be emitted as-is, and `import ... = require(...)` will be emitted as a `require()` call (though in practice you may not even use TypeScript for emit, since it’s likely you’ll be using a bundler for your code).
This holds true regardless of the file extension of the containing file.
So the output of this code:

 ts ` import * as foo from "some-package/foo" ; import bar = require ( "some-package/bar" ); `
 should look something like this:

 js ` import * as foo from "some-package/foo" ; var bar = require ( "some-package/bar" ); `
 What this also means is that the syntax you choose directs how conditional exports are matched.
So in the above example, if the `package.json` of `some-package` looks like this:

 json ` { "name" : "some-package" , "version" : "0.0.1" , "exports" : { "./foo" : { "import" : "./esm/foo-from-import.mjs" , "require" : "./cjs/foo-from-require.cjs" }, "./bar" : { "import" : "./esm/bar-from-import.mjs" , "require" : "./cjs/bar-from-require.cjs" } } } `
 TypeScript will resolve these paths to `[...]/some-package/esm/foo-from-import.mjs` and `[...]/some-package/cjs/bar-from-require.cjs`.

For more information, you can read up on these new settings here .

## Checked Import Attributes and Assertions

 Import attributes and assertions are now checked against the global `ImportAttributes` type.
This means that runtimes can now more accurately describe the import attributes

 ts ` // In some global file. interface ImportAttributes { type : "json" ; } // In some other module import * as ns from "foo" with { type : " not - json " }; // ~~~~~~~~~~ // error! // // Type '{ type: "not-json"; }' is not assignable to type 'ImportAttributes'. // Types of property 'type' are incompatible. // Type '"not-json"' is not assignable to type '"json"'. `
 This change was provided thanks to Oleksandr Tarasiuk .

## Quick Fix for Adding Missing Parameters

 TypeScript now has a quick fix to add a new parameter to functions that are called with too many arguments.

This can be useful when threading a new argument through several existing functions, which can be cumbersome today.

 This quick fix was provided courtsey of Oleksandr Tarasiuk .

## Upcoming Changes from TypeScript 5.0 Deprecations

 TypeScript 5.0 deprecated the following options and behaviors:

- `charset`

- `target: ES3`

- `importsNotUsedAsValues`

- `noImplicitUseStrict`

- `noStrictGenericChecks`

- `keyofStringsOnly`

- `suppressExcessPropertyErrors`

- `suppressImplicitAnyIndexErrors`

- `out`

- `preserveValueImports`

- `prepend` in project references

- implicitly OS-specific `newLine`

To continue using them, developers using TypeScript 5.0 and other more recent versions have had to specify a new option called `ignoreDeprecations` with the value `"5.0"`.

However, TypScript 5.4 will be the last version in which these will continue to function as normal.
By TypeScript 5.5 (likely June 2024), these will become hard errors, and code using them will need to be migrated away.

For more information, you can read up on this plan on GitHub , which contains suggestions in how to best adapt your codebase.

## Notable Behavioral Changes

 This section highlights a set of noteworthy changes that should be acknowledged and understood as part of any upgrade.
Sometimes it will highlight deprecations, removals, and new restrictions.
It can also contain bug fixes that are functionally improvements, but which can also affect an existing build by introducing new errors.

### `lib.d.ts` Changes

 Types generated for the DOM may have an impact on type-checking your codebase.
For more information, see the DOM updates for TypeScript 5.4 .

### More Accurate Conditional Type Constraints

 The following code no longer allows the second variable declaration in the function `foo`.

 ts ` type IsArray < T > = T extends any [] ? true : false ; function foo < U extends object >( x : IsArray < U >) { let first : true = x ; // Error let second : false = x ; // Error, but previously wasn't } `
 Previously, when TypeScript checked the initializer for `second`, it needed to determine whether `IsArray&#x3C;U>` was assignable to the unit type `false`.
While `IsArray&#x3C;U>` isn’t compatible any obvious way, TypeScript looks at the constraint of that type as well.
In a conditional type like `T extends Foo ? TrueBranch : FalseBranch`, where `T` is generic, the type system would look at the constraint of `T`, substitute it in for `T` itself, and decide on either the true or false branch.

But this behavior was inaccurate because it was overly eager.
Even if the constraint of `T` isn’t assignable to `Foo`, that doesn’t mean that it won’t be instantiated with something that is.
And so the more correct behavior is to produce a union type for the constraint of the conditional type in cases where it can’t be proven that `T` never or always extends `Foo.`

TypeScript 5.4 adopts this more accurate behavior.
What this means in practice is that you may begin to find that some conditional type instances are no longer compatible with their branches.

 You can read about the specific changes here .

### More Aggressive Reduction of Intersections Between Type Variables and Primitive Types

 TypeScript now reduces intersections with type variables and primitives more aggressively, depending on how the type variable’s constraint overlaps with those primitives.

 ts ` declare function intersect < T , U >( x : T , y : U ): T & U ; function foo < T extends "abc" | "def" >( x : T , str : string , num : number ) { // Was 'T & string', now is just 'T' let a = intersect ( x , str ); // Was 'T & number', now is just 'never' let b = intersect ( x , num ) // Was '(T & "abc") | (T & "def")', now is just 'T' let c = Math . random () < 0.5 ? intersect ( x , "abc" ) : intersect ( x , "def" ); } `
 For more information, see the change here .

### Improved Checking Against Template Strings with Interpolations

 TypeScript now more accurately checks whether or not strings are assignable to the placeholder slots of a template string type.

 ts ` function a < T extends { id : string }>() { let x : `- ${ keyof T & string } ` ; // Used to error, now doesn't. x = "-id" ; } `
 This behavior is more desirable, but may cause breaks in code using constructs like conditional types, where these rule changes are easy to witness.

 See this change for more details.

### Errors When Type-Only Imports Conflict with Local Values

 Previously, TypeScript would permit the following code under `isolatedModules` if the import to `Something` only referred to a type.

 ts ` import { Something } from "./some/path" ; let Something = 123 ; `
 However, it’s not safe for single-file compilers to assume whether it’s “safe” to drop the `import`, even if the code is guaranteed to fail at runtime.
In TypeScript 5.4, this code will trigger an error like the following:

 ` Import 'Something' conflicts with local value, so must be declared with a type-only import when 'isolatedModules' is enabled. `
 The fix should be to either make a local rename, or, as the error states, add the `type` modifier to the import:

 ts ` import type { Something } from "./some/path" ; // or import { type Something } from "./some/path" ; `
 See more information on the change itself .

### New Enum Assignability Restrictions

 When two enums have the same declared names and enum member names, they were previously always considered compatible;
however, when the values were known, TypeScript would silently allow them to have differing values.

TypeScript 5.4 tightens this restriction by requiring the values to be identical when they are known.

 ts ` namespace First { export enum SomeEnum { A = 0 , B = 1 , } } namespace Second { export enum SomeEnum { A = 0 , B = 2 , } } function foo ( x : First . SomeEnum , y : Second . SomeEnum ) { // Both used to be compatible - no longer the case, // TypeScript errors with something like: // // Each declaration of 'SomeEnum.B' differs in its value, where '1' was expected but '2' was given. x = y ; y = x ; } `
 Additionally, there are new restrictions for when one of the enum members does not have a statically known value.
In these cases, the other enum must at least be implicitly numeric (e.g. it has no statically resolved initializer), or it is explicitly numeric (meaning TypeScript could resolve the value to something numeric).
Practically speaking, what this means is that string enum members are only ever compatible with other string enums of the same value.

 ts ` namespace First { export declare enum SomeEnum { A , B , } } namespace Second { export declare enum SomeEnum { A , B = "some known string" , } } function foo ( x : First . SomeEnum , y : Second . SomeEnum ) { // Both used to be compatible - no longer the case, // TypeScript errors with something like: // // One value of 'SomeEnum.B' is the string '"some known string"', and the other is assumed to be an unknown numeric value. x = y ; y = x ; } `
 For more information, see the pull request that introduced this change .

### Name Restrictions on Enum Members

 TypeScript no longer allows enum members to use the names `Infinity`, `-Infinity`, or `NaN`.

 ts ` // Errors on all of these: // // An enum member cannot have a numeric name. enum E { Infinity = 0 , "-Infinity" = 1 , NaN = 2 , } `
 See more details here .

### Better Mapped Type Preservation Over Tuples with `any` Rest Elements

 Previously, applying a mapped type with `any` into a tuple would create an `any` element type.
This is undesirable and is now fixed.

 ts ` Promise . all ([ "" , ...([] as any )]) . then (( result ) => { const head = result [ 0 ]; // 5.3: any, 5.4: string const tail = result . slice ( 1 ); // 5.3 any, 5.4: any[] }); `
 For more information, see the fix along with the follow-on discussion around behavioral changes and further tweaks .

### Emit Changes

 While not a breaking change per se, developers may have implicitly taken dependencies on TypeScript’s JavaScript or declaration emit outputs.
The following are notable changes.

- Preserve type parameter names more often when shadowed

- Move complex parameter lists of async function into downlevel generator body

- Do not remove binding alias in function declarations

- ImportAttributes should go through the same emit phases when in an ImportTypeNode

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: N I Last updated: Jun 15, 2026

## Typescript 5 3

Was this page helpful?

# TypeScript 5.3

## Import Attributes

 TypeScript 5.3 supports the latest updates to the import attributes proposal.

One use-case of import attributes is to provide information about the expected format of a module to the runtime.

 ts ` // We only want this to be interpreted as JSON, // not a runnable/malicious JavaScript file with a `.json` extension. import obj from "./something.json" with { type : " json " }; `
 The contents of these attributes are not checked by TypeScript since they’re host-specific, and are simply left alone so that browsers and runtimes can handle them (and possibly error).

 ts ` // TypeScript is fine with this. // But your browser? Probably not. import * as foo from "./foo.js" with { type : " fluffy bunny " }; `
 Dynamic `import()` calls can also use import attributes through a second argument.

 ts ` const obj = await import ( "./something.json" , { with: { type: "json" } }); `
 The expected type of that second argument is defined by a type called `ImportCallOptions`, which by default just expects a property called `with`.

Note that import attributes are an evolution of an earlier proposal called “import assertions”, which were implemented in TypeScript 4.5 .
The most obvious difference is the use of the `with` keyword over the `assert` keyword.
But the less-visible difference is that runtimes are now free to use attributes to guide the resolution and interpretation of import paths, whereas import assertions could only assert some characteristics after loading a module.

Over time, TypeScript will be deprecating the old syntax for import assertions in favor of the proposed syntax for import attributes.
Existing code using `assert` should migrate towards the `with` keyword.
New code that needs an import attribute should use `with` exclusively.

We’d like to thank Oleksandr Tarasiuk for implementing this proposal !
And we’d also like to call out Wenlu Wang for their implementation of import assertions !

## Stable Support `resolution-mode` in Import Types

 In TypeScript 4.7, TypeScript added support for a `resolution-mode` attribute in `/// &#x3C;reference types="..." />` to control whether a specifier should be resolved via `import` or `require` semantics.

 ts ` /// <reference types="pkg" resolution-mode="require" /> // or /// <reference types="pkg" resolution-mode="import" /> `
 A corresponding field was added to import assertions on type-only imports as well;
however, it was only supported in nightly versions of TypeScript.
The rationale was that in spirit, import assertions were not intended to guide module resolution.
So this feature was shipped experimentally in a nightly-only mode to get more feedback.

But given that import attributes can guide resolution, and that we’ve seen reasonable use-cases, TypeScript 5.3 now supports the `resolution-mode` attribute for `import type`.

 ts ` // Resolve `pkg` as if we were importing with a `require()` import type { TypeFromRequire } from "pkg" with { " resolution - mode ": " require " }; // Resolve `pkg` as if we were importing with an `import` import type { TypeFromImport } from "pkg" with { " resolution - mode ": " import " }; export interface MergedType extends TypeFromRequire , TypeFromImport {} `
 These import attributes can also be used on `import()` types.

 ts ` export type TypeFromRequire = import ( "pkg" , { with: { "resolution-mode" : "require" } }). TypeFromRequire ; export type TypeFromImport = import ( "pkg" , { with: { "resolution-mode" : "import" } }). TypeFromImport ; export interface MergedType extends TypeFromRequire , TypeFromImport {} `
 For more information, check out the change here

## `resolution-mode` Supported in All Module Modes

 Previously, using `resolution-mode` was only allowed under the `moduleResolution` options `node16` and `nodenext`.
To make it easier to look up modules specifically for type purposes, `resolution-mode` now works appropriately in all other `moduleResolution` options like `bundler`, `node10`, and simply doesn’t error under `classic`.

For more information, see the implementing pull request .

## `switch (true)` Narrowing

 TypeScript 5.3 now can perform narrowing based on conditions in each `case` clause within a `switch (true)`.

 ts ` function f ( x : unknown ) { switch ( true ) { case typeof x === "string" : // 'x' is a 'string' here console . log ( x . toUpperCase ()); // falls through... case Array . isArray ( x ): // 'x' is a 'string | any[]' here. console . log ( x . length ); // falls through... default : // 'x' is 'unknown' here. // ... } } `
 This feature was spearheaded initial work by Mateusz Burzyński
We’d like to extend a “thank you!” for this contribution.

## Narrowing On Comparisons to Booleans

 Occasionally you may find yourself performing a direct comparison with `true` or `false` in a condition.
Usually these are unnecessary comparisons, but you might prefer it as a point of style, or to avoid certain issues around JavaScript truthiness.
Regardless, previously TypeScript just didn’t recognize such forms when performing narrowing.

TypeScript 5.3 now keeps up and understands these expressions when narrowing variables.

 ts ` interface A { a : string ; } interface B { b : string ; } type MyType = A | B ; function isA ( x : MyType ): x is A { return "a" in x ; } function someFn ( x : MyType ) { if ( isA ( x ) === true ) { console . log ( x . a ); // works! } } `
 We’d like to thank Mateusz Burzyński for the pull request that implemented this.

## `instanceof` Narrowing Through `Symbol.hasInstance`

 A slightly esoteric feature of JavaScript is that it is possible to override the behavior of the `instanceof` operator.
To do so, the value on the right side of the `instanceof` operator needs to have a specific method named by `Symbol.hasInstance`.

 js ` class Weirdo { static [ Symbol . hasInstance ]( testedValue ) { // wait, what? return testedValue === undefined ; } } // false console . log ( new Thing () instanceof Weirdo ); // true console . log ( undefined instanceof Weirdo ); `
 To better model this behavior in `instanceof`, TypeScript now checks if such a `[Symbol.hasInstance]` method exists and is declared as a type predicate function.
If it does, the tested value on the left side of the `instanceof` operator will be narrowed appropriately by that type predicate.

 ts ` interface PointLike { x : number ; y : number ; } class Point implements PointLike { x : number ; y : number ; constructor ( x : number , y : number ) { this . x = x ; this . y = y ; } distanceFromOrigin () { return Math . sqrt ( this . x ** 2 + this . y ** 2 ); } static [ Symbol . hasInstance ]( val : unknown ): val is PointLike { return !! val && typeof val === "object" && "x" in val && "y" in val && typeof val . x === "number" && typeof val . y === "number" ; } } function f ( value : unknown ) { if ( value instanceof Point ) { // Can access both of these - correct! value . x ; value . y ; // Can't access this - we have a 'PointLike', // but we don't *actually* have a 'Point'. value . distanceFromOrigin (); } } `
 As you can see in this example, `Point` defines its own `[Symbol.hasInstance]` method.
It actually acts as a custom type guard over a separate type called `PointLike`.
In the function `f`, we were able to narrow `value` down to a `PointLike` with `instanceof`, but not a `Point`.
That means that we can access the properties `x` and `y`, but not the method `distanceFromOrigin`.

For more information, you can read up on this change here .

## Checks for `super` Property Accesses on Instance Fields

 In JavaScript, it’s possible to access a declaration in a base class through the `super` keyword.

 js ` class Base { someMethod () { console . log ( "Base method called!" ); } } class Derived extends Base { someMethod () { console . log ( "Derived method called!" ); super . someMethod (); } } new Derived (). someMethod (); // Prints: // Derived method called! // Base method called! `
 This is different from writing something like `this.someMethod()`, since that could invoke an overridden method.
This is a subtle distinction, made more subtle by the fact that often the two can be interchangeable if a declaration is never overridden at all.

 js ` class Base { someMethod () { console . log ( "someMethod called!" ); } } class Derived extends Base { someOtherMethod () { // These act identically. this . someMethod (); super . someMethod (); } } new Derived (). someOtherMethod (); // Prints: // someMethod called! // someMethod called! `
 The problem is using them interchangeably is that `super` only works on members declared on the prototype — not instance properties.
That means that if you wrote `super.someMethod()`, but `someMethod` was defined as a field, you’d get a runtime error!

 ts ` class Base { someMethod = () => { console . log ( "someMethod called!" ); } } class Derived extends Base { someOtherMethod () { super . someMethod (); } } new Derived (). someOtherMethod (); // 💥 // Doesn't work because 'super.someMethod' is 'undefined'. `
 TypeScript 5.3 now more-closely inspects `super` property accesses/method calls to see if they correspond to class fields.
If they do, we’ll now get a type-checking error.

 This check was contributed thanks to Jack Works !

## Interactive Inlay Hints for Types

 TypeScript’s inlay hints now support jumping to the definition of types!
This makes it easier to casually navigate your code.

See more at the implementation here .

## Settings to Prefer `type` Auto-Imports

 Previously when TypeScript generated auto-imports for something in a type position, it would add a `type` modifier based on your settings.
For example, when getting an auto-import on `Person` in the following:

 ts ` export let p : Person `
 TypeScript’s editing experience would usually add an import for `Person` as:

 ts ` import { Person } from "./types" ; export let p : Person `
 and under certain settings like `verbatimModuleSyntax`, it would add the `type` modifier:

 ts ` import { type Person } from "./types" ; export let p : Person `
 However, maybe your codebase isn’t able to use some of these options; or you just have a preference for explicit `type` imports when possible.

 With a recent change , TypeScript now enables this to be an editor-specific option.
In Visual Studio Code, you can enable it in the UI under “TypeScript › Preferences: Prefer Type Only Auto Imports”, or as the JSON configuration option `typescript.preferences.preferTypeOnlyAutoImports`

## Optimizations by Skipping JSDoc Parsing

 When running TypeScript via `tsc`, the compiler will now avoid parsing JSDoc.
This drops parsing time on its own, but also reduces memory usage to store comments along with time spent in garbage collection.
All-in-all, you should see slightly faster compiles and quicker feedback in `--watch` mode.

 The specific changes can be viewed here .

Because not every tool using TypeScript will need to store JSDoc (e.g. typescript-eslint and Prettier), this parsing strategy has been surfaced as part of the API itself.
This can enable these tools to gain the same memory and speed improvements we’ve brought to the TypeScript compiler.
The new options for comment parsing strategy are described in `JSDocParsingMode`.
More information is available on this pull request .

## Optimizations by Comparing Non-Normalized Intersections

 In TypeScript, unions and intersections always follow a specific form, where intersections can’t contain union types.
That means that when we create an intersection over a union like `A &#x26; (B | C)`, that intersection will be normalized into `(A &#x26; B) | (A &#x26; C)`.
Still, in some cases the type system will maintain the original form for display purposes.

It turns out that the original form can be used for some clever fast-path comparisons between types.

For example, let’s say we have `SomeType &#x26; (Type1 | Type2 | ... | Type99999NINE)` and we want to see if that’s assignable to `SomeType`.
Recall that we don’t really have an intersection as our source type — we have a union that looks like `(SomeType &#x26; Type1) | (SomeType &#x26; Type2) | ... |(SomeType &#x26; Type99999NINE)`.
When checking if a union is assignable to some target type, we have to check if every member of the union is assignable to the target type, and that can be very slow.

In TypeScript 5.3, we peek at the original intersection form that we were able to tuck away.
When we compare the types, we do a quick check to see if the target exists in any constituent of the source intersection.

For more information, see this pull request .

## Consolidation Between `tsserverlibrary.js` and `typescript.js`

 TypeScript itself ships two library files: `tsserverlibrary.js` and `typescript.js`.
There are certain APIs available only in `tsserverlibrary.js` (like the `ProjectService` API), which may be useful to some importers.
Still, the two are distinct bundles with a lot of overlap, duplicating code in the package.
What’s more, it can be challenging to consistently use one over the other due to auto-imports or muscle memory.
Accidentally loading both modules is far too easy, and code may not work properly on a different instance of the API.
Even if it does work, loading a second bundle increases resource usage.

Given this, we’ve decided to consolidate the two.
`typescript.js` now contains what `tsserverlibrary.js` used to contain, and `tsserverlibrary.js` now simply re-exports `typescript.js`.
Comparing the before/after of this consolidation, we saw the following reduction in package size:

| **

 **
| **Before**
| **After**
| **Diff**
| **Diff (percent)**
|

| Packed
| 6.90 MiB
| 5.48 MiB
| -1.42 MiB
| -20.61%
|

| Unpacked
| 38.74 MiB
| 30.41 MiB
| -8.33 MiB
| -21.50%
|

| **

 **
| **Before**
| **After**
| **Diff**
| **Diff (percent)**
|

| `lib/tsserverlibrary.d.ts`
| 570.95 KiB
| 865.00 B
| -570.10 KiB
| -99.85%
|

| `lib/tsserverlibrary.js`
| 8.57 MiB
| 1012.00 B
| -8.57 MiB
| -99.99%
|

| `lib/typescript.d.ts`
| 396.27 KiB
| 570.95 KiB
| +174.68 KiB
| +44.08%
|

| `lib/typescript.js`
| 7.95 MiB
| 8.57 MiB
| +637.53 KiB
| +7.84%
|

In other words, this is over a 20.5% reduction in package size.

For more information, you can see the work involved here .

## Breaking Changes and Correctness Improvements

### `lib.d.ts` Changes

 Types generated for the DOM may have an impact on your codebase.
For more information, see the DOM updates for TypeScript 5.3 .

### Checks for `super` Accesses on Instance Properties

 TypeScript 5.3 now detects when the declaration referenced by a `super.` property access is a class field and issues an error.
This prevents errors that might occur at runtime.

 See more on this change here .
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: AB EL Last updated: Jun 15, 2026

## Typescript 5 2

Was this page helpful?

# TypeScript 5.2

## `using` Declarations and Explicit Resource Management

 TypeScript 5.2 adds support for the upcoming Explicit Resource Management feature in ECMAScript.
Let’s explore some of the motivations and understand what the feature brings us.

It’s common to need to do some sort of “clean-up” after creating an object.
For example, you might need to close network connections, delete temporary files, or just free up some memory.

Let’s imagine a function that creates a temporary file, reads and writes to it for various operations, and then closes and deletes it.

 ts ` import * as fs from "fs" ; export function doSomeWork () { const path = ".some_temp_file" ; const file = fs . openSync ( path , "w+" ); // use file... // Close the file and delete it. fs . closeSync ( file ); fs . unlinkSync ( path ); } `
 This is fine, but what happens if we need to perform an early exit?

 ts ` export function doSomeWork () { const path = ".some_temp_file" ; const file = fs . openSync ( path , "w+" ); // use file... if ( someCondition ()) { // do some more work... // Close the file and delete it. fs . closeSync ( file ); fs . unlinkSync ( path ); return ; } // Close the file and delete it. fs . closeSync ( file ); fs . unlinkSync ( path ); } `
 We’re starting to see some duplication of clean-up which can be easy to forget.
We’re also not guaranteed to close and delete the file if an error gets thrown.
This could be solved by wrapping this all in a `try`/`finally` block.

 ts ` export function doSomeWork () { const path = ".some_temp_file" ; const file = fs . openSync ( path , "w+" ); try { // use file... if ( someCondition ()) { // do some more work... return ; } } finally { // Close the file and delete it. fs . closeSync ( file ); fs . unlinkSync ( path ); } } `
 While this is more robust, it’s added quite a bit of “noise” to our code.
There are also other foot-guns we can run into if we start adding more clean-up logic to our `finally` block — for example, exceptions preventing other resources from being disposed.
This is what the explicit resource management proposal aims to solve.
The key idea of the proposal is to support resource disposal — this clean-up work we’re trying to deal with — as a first class idea in JavaScript.

This starts by adding a new built-in `symbol` called `Symbol.dispose`, and we can create objects with methods named by `Symbol.dispose`.
For convenience, TypeScript defines a new global type called `Disposable` which describes these.

 ts ` class TempFile implements Disposable { #path : string ; #handle : number ; constructor ( path : string ) { this . #path = path ; this . #handle = fs . openSync ( path , "w+" ); } // other methods [ Symbol . dispose ]() { // Close the file and delete it. fs . closeSync ( this . #handle ); fs . unlinkSync ( this . #path ); } } `
 Later on we can call those methods.

 ts ` export function doSomeWork () { const file = new TempFile ( ".some_temp_file" ); try { // ... } finally { file [ Symbol . dispose ](); } } `
 Moving the clean-up logic to `TempFile` itself doesn’t buy us much;
we’ve basically just moved all the clean-up work from the `finally` block into a method, and that’s always been possible.
But having a well-known “name” for this method means that JavaScript can build other features on top of it.

That brings us to the first star of the feature: `using` declarations!
`using` is a new keyword that lets us declare new fixed bindings, kind of like `const`.
The key difference is that variables declared with `using` get their `Symbol.dispose` method called at the end of the scope!

So we could simply have written our code like this:

 ts ` export function doSomeWork () { using file = new TempFile ( ".some_temp_file" ); // use file... if ( someCondition ()) { // do some more work... return ; } } `
 Check it out — no `try`/`finally` blocks!
At least, none that we see.
Functionally, that’s exactly what `using` declarations will do for us, but we don’t have to deal with that.

You might be familiar with `using` declarations in C# , `with` statements in Python , or `try`-with-resource declarations in Java .
These are all similar to JavaScript’s new `using` keyword, and provide a similar explicit way to perform a “tear-down” of an object at the end of a scope.

`using` declarations do this clean-up at the very end of their containing scope or right before an “early return” like a `return` or a `throw`n error.
They also dispose in a first-in-last-out order like a stack.

 ts ` function loggy ( id : string ): Disposable { console . log ( `Creating ${ id } ` ); return { [ Symbol . dispose ]() { console . log ( `Disposing ${ id } ` ); } } } function func () { using a = loggy ( "a" ); using b = loggy ( "b" ); { using c = loggy ( "c" ); using d = loggy ( "d" ); } using e = loggy ( "e" ); return ; // Unreachable. // Never created, never disposed. using f = loggy ( "f" ); } func (); // Creating a // Creating b // Creating c // Creating d // Disposing d // Disposing c // Creating e // Disposing e // Disposing b // Disposing a `
 `using` declarations are supposed to be resilient to exceptions;
if an error is thrown, it’s rethrown after disposal.
On the other hand, the body of your function might execute as expected, but the `Symbol.dispose` might throw.
In that case, that exception is rethrown as well.

But what happens if both the logic before and during disposal throws an error?
For those cases, `SuppressedError` has been introduced as a new subtype of `Error`.
It features a `suppressed` property that holds the last-thrown error, and an `error` property for the most-recently thrown error.

 ts ` class ErrorA extends Error { name = "ErrorA" ; } class ErrorB extends Error { name = "ErrorB" ; } function throwy ( id : string ) { return { [ Symbol . dispose ]() { throw new ErrorA ( `Error from ${ id } ` ); } }; } function func () { using a = throwy ( "a" ); throw new ErrorB ( "oops!" ) } try { func (); } catch ( e : any ) { console . log ( e . name ); // SuppressedError console . log ( e . message ); // An error was suppressed during disposal. console . log ( e . error . name ); // ErrorA console . log ( e . error . message ); // Error from a console . log ( e . suppressed . name ); // ErrorB console . log ( e . suppressed . message ); // oops! } `
 You might have noticed that we’re using synchronous methods in these examples.
However, lots of resource disposal involves asynchronous operations, and we need to wait for those to complete before we continue running any other code.

That’s why there is also a new `Symbol.asyncDispose`, and it brings us to the next star of the show — `await using` declarations.
These are similar to `using` declarations, but the key is that they look up whose disposal must be `await`ed.
They use a different method named by `Symbol.asyncDispose`, though they can operate on anything with a `Symbol.dispose` as well.
For convenience, TypeScript also introduces a global type called `AsyncDisposable` that describes any object with an asynchronous dispose method.

 ts ` async function doWork () { // Do fake work for half a second. await new Promise ( resolve => setTimeout ( resolve , 500 )); } function loggy ( id : string ): AsyncDisposable { console . log ( `Constructing ${ id } ` ); return { async [ Symbol . asyncDispose ]() { console . log ( `Disposing (async) ${ id } ` ); await doWork (); }, } } async function func () { await using a = loggy ( "a" ); await using b = loggy ( "b" ); { await using c = loggy ( "c" ); await using d = loggy ( "d" ); } await using e = loggy ( "e" ); return ; // Unreachable. // Never created, never disposed. await using f = loggy ( "f" ); } func (); // Constructing a // Constructing b // Constructing c // Constructing d // Disposing (async) d // Disposing (async) c // Constructing e // Disposing (async) e // Disposing (async) b // Disposing (async) a `
 Defining types in terms of `Disposable` and `AsyncDisposable` can make your code much easier to work with if you expect others to do tear-down logic consistently.
In fact, lots of existing types exist in the wild which have a `dispose()` or `close()` method.
For example, the Visual Studio Code APIs even define their own `Disposable` interface .
APIs in the browser and in runtimes like Node.js, Deno, and Bun might also choose to use `Symbol.dispose` and `Symbol.asyncDispose` for objects which already have clean-up methods, like file handles, connections, and more.

Now maybe this all sounds great for libraries, but a little bit heavy-weight for your scenarios.
If you’re doing a lot of ad-hoc clean-up, creating a new type might introduce a lot of over-abstraction and questions about best-practices.
For example, take our `TempFile` example again.

 ts ` class TempFile implements Disposable { #path : string ; #handle : number ; constructor ( path : string ) { this . #path = path ; this . #handle = fs . openSync ( path , "w+" ); } // other methods [ Symbol . dispose ]() { // Close the file and delete it. fs . closeSync ( this . #handle ); fs . unlinkSync ( this . #path ); } } export function doSomeWork () { using file = new TempFile ( ".some_temp_file" ); // use file... if ( someCondition ()) { // do some more work... return ; } } `
 All we wanted was to remember to call two functions — but was this the best way to write it?
Should we be calling `openSync` in the constructor, create an `open()` method, or pass in the handle ourselves?
Should we expose a method for every possible operation we need to perform, or should we just make the properties public?

That brings us to the final stars of the feature: `DisposableStack` and `AsyncDisposableStack`.
These objects are useful for doing both one-off clean-up, along with arbitrary amounts of cleanup.
A `DisposableStack` is an object that has several methods for keeping track of `Disposable` objects, and can be given functions for doing arbitrary clean-up work.
We can also assign them to `using` variables because — get this — they’re also `Disposable` !
So here’s how we could’ve written the original example.

 ts ` function doSomeWork () { const path = ".some_temp_file" ; const file = fs . openSync ( path , "w+" ); using cleanup = new DisposableStack (); cleanup . defer (() => { fs . closeSync ( file ); fs . unlinkSync ( path ); }); // use file... if ( someCondition ()) { // do some more work... return ; } // ... } `
 Here, the `defer()` method just takes a callback, and that callback will be run once `cleanup` is disposed of.
Typically, `defer` (and other `DisposableStack` methods like `use` and `adopt`)
should be called immediately after creating a resource.
As the name suggests, `DisposableStack` disposes of everything it keeps track of like a stack, in a first-in-last-out order, so `defer`ing immediately after creating a value helps avoid odd dependency issues.
`AsyncDisposableStack` works similarly, but can keep track of `async` functions and `AsyncDisposable`s, and is itself an `AsyncDisposable.`

The `defer` method is similar in many ways to the `defer` keyword in Go , Swift , Zig , Odin , and others, where the conventions should be similar.

Because this feature is so recent, most runtimes will not support it natively.
To use it, you will need runtime polyfills for the following:

- `Symbol.dispose`

- `Symbol.asyncDispose`

- `DisposableStack`

- `AsyncDisposableStack`

- `SuppressedError`

However, if all you’re interested in is `using` and `await using`, you should be able to get away with only polyfilling the built-in `symbol`s.
Something as simple as the following should work for most cases:

 ts ` Symbol . dispose ??= Symbol ( "Symbol.dispose" ); Symbol . asyncDispose ??= Symbol ( "Symbol.asyncDispose" ); `
 You will also need to set your compilation `target` to `es2022` or below, and configure your `lib` setting to either include `"esnext"` or `"esnext.disposable"`.

 json ` { "compilerOptions" : { "target" : "es2022" , "lib" : [ "es2022" , "esnext.disposable" , "dom" ] } } `
 For more information on this feature, take a look at the work on GitHub !

## Decorator Metadata

 TypeScript 5.2 implements an upcoming ECMAScript feature called decorator metadata .

The key idea of this feature is to make it easy for decorators to create and consume metadata on any class they’re used on or within.

Whenever decorator functions are used, they now have access to a new `metadata` property on their context object.
The `metadata` property just holds a simple object.
Since JavaScript lets us add properties arbitrarily, it can be used as a dictionary that is updated by each decorator.
Alternatively, since every `metadata` object will be identical for each decorated portion of a class, it can be used as a key into a `Map`.
After all decorators on or in a class get run, that object can be accessed on the class via `Symbol.metadata`.

 ts ` interface Context { name : string ; metadata : Record < PropertyKey , unknown >; } function setMetadata ( _target : any , context : Context ) { context . metadata [ context . name ] = true ; } class SomeClass { @ setMetadata foo = 123 ; @ setMetadata accessor bar = "hello!" ; @ setMetadata baz () { } } const ourMetadata = SomeClass [ Symbol . metadata ]; console . log ( JSON . stringify ( ourMetadata )); // { "bar": true, "baz": true, "foo": true } `
 This can be useful in a number of different scenarios.
Metadata could possibly be attached for lots of uses like debugging, serialization, or performing dependency injection with decorators.
Since metadata objects are created per decorated class, frameworks can either privately use them as keys into a `Map` or `WeakMap`, or tack properties on as necessary.

For example, let’s say we wanted to use decorators to keep track of which properties and accessors are serializable when using `JSON.stringify` like so:

 ts ` import { serialize , jsonify } from "./serializer" ; class Person { firstName : string ; lastName : string ; @ serialize age : number @ serialize get fullName () { return ` ${ this . firstName } ${ this . lastName } ` ; } toJSON () { return jsonify ( this ) } constructor ( firstName : string , lastName : string , age : number ) { // ... } } `
 Here, the intent is that only `age` and `fullName` should be serialized because they are marked with the `@serialize` decorator.
We define a `toJSON` method for this purpose, but it just calls out to `jsonify` which uses the metadata that `@serialize` created.

Here’s an example of how the module `./serialize.ts` might be defined:

 ts ` const serializables = Symbol (); type Context = | ClassAccessorDecoratorContext | ClassGetterDecoratorContext | ClassFieldDecoratorContext ; export function serialize ( _target : any , context : Context ): void { if ( context . static || context . private ) { throw new Error ( "Can only serialize public instance members." ) } if ( typeof context . name === "symbol" ) { throw new Error ( "Cannot serialize symbol-named properties." ); } const propNames = ( context . metadata [ serializables ] as string [] | undefined ) ??= []; propNames . push ( context . name ); } export function jsonify ( instance : object ): string { const metadata = instance . constructor [ Symbol . metadata ]; const propNames = metadata ?.[ serializables ] as string [] | undefined ; if (! propNames ) { throw new Error ( "No members marked with @serialize." ); } const pairStrings = propNames . map ( key => { const strKey = JSON . stringify ( key ); const strValue = JSON . stringify (( instance as any )[ key ]); return ` ${ strKey } : ${ strValue } ` ; }); return `{ ${ pairStrings . join ( ", " ) } }` ; } `
 This module has a local `symbol` called `serializables` to store and retrieve the names of properties marked `@serializable`.
It stores a list of these property names on the metadata on each invocation of `@serializable`.
When `jsonify` is called, the list of properties is fetched off of the metadata and used to retrieve the actual values from the instance, eventually serializing those names and values.

Using a `symbol` technically makes this data accessible to others.
An alternative might be to use a `WeakMap` using the metadata object as a key.
This keeps data private and happens to use fewer type assertions in this case, but is otherwise similar.

 ts ` const serializables = new WeakMap < object , string []>(); type Context = | ClassAccessorDecoratorContext | ClassGetterDecoratorContext | ClassFieldDecoratorContext ; export function serialize ( _target : any , context : Context ): void { if ( context . static || context . private ) { throw new Error ( "Can only serialize public instance members." ) } if ( typeof context . name !== "string" ) { throw new Error ( "Can only serialize string properties." ); } let propNames = serializables . get ( context . metadata ); if ( propNames === undefined ) { serializables . set ( context . metadata , propNames = []); } propNames . push ( context . name ); } export function jsonify ( instance : object ): string { const metadata = instance . constructor [ Symbol . metadata ]; const propNames = metadata && serializables . get ( metadata ); if (! propNames ) { throw new Error ( "No members marked with @serialize." ); } const pairStrings = propNames . map ( key => { const strKey = JSON . stringify ( key ); const strValue = JSON . stringify (( instance as any )[ key ]); return ` ${ strKey } : ${ strValue } ` ; }); return `{ ${ pairStrings . join ( ", " ) } }` ; } `
 As a note, these implementations don’t handle subclassing and inheritance.
That’s left as an exercise to you (and you might find that it is easier in one version of the file than the other!).

Because this feature is still fresh, most runtimes will not support it natively.
To use it, you will need a polyfill for `Symbol.metadata`.
Something as simple as the following should work for most cases:

 ts ` Symbol . metadata ??= Symbol ( "Symbol.metadata" ); `
 You will also need to set your compilation `target` to `es2022` or below, and configure your `lib` setting to either include `"esnext"` or `"esnext.decorators"`.

 json ` { "compilerOptions" : { "target" : "es2022" , "lib" : [ "es2022" , "esnext.decorators" , "dom" ] } } `
 We’d like to thank Oleksandr Tarasiuk for contributing the implementation of decorator metadata for TypeScript 5.2!

## Named and Anonymous Tuple Elements

 Tuple types have supported optional labels or names for each element.

 ts ` type Pair < T > = [first: T , second: T ]; `
 These labels don’t change what you’re allowed to do with them — they’re solely to help with readability and tooling.

However, TypeScript previously had a rule that tuples could not mix and match between labeled and unlabeled elements.
In other words, either no element could have a label in a tuple, or all elements needed one.

 ts ` // ✅ fine - no labels type Pair1 < T > = [ T , T ]; // ✅ fine - all fully labeled type Pair2 < T > = [first: T , second: T ]; // ❌ previously an error type Pair3 < T > = [first: T , T ]; // ~ // Tuple members must all have names // or all not have names. `
 This could be annoying for rest elements where we’d be forced to just add a label like `rest` or `tail`.

 ts ` // ❌ previously an error type TwoOrMore_A < T > = [first: T , second: T , ... T []]; // ~~~~~~ // Tuple members must all have names // or all not have names. // ✅ type TwoOrMore_B < T > = [first: T , second: T , rest: ... T []]; `
 It also meant that this restriction had to be enforced internally in the type system, meaning TypeScript would lose labels.

 ts ` type HasLabels = [a: string , b: string ]; type HasNoLabels = [ number , number ]; type Merged = [... HasNoLabels , ... HasLabels ]; // ^ [number, number, string, string] // // 'a' and 'b' were lost in 'Merged' `
 In TypeScript 5.2, the all-or-nothing restriction on tuple labels has been lifted.
The language can now also preserve labels when spreading into an unlabeled tuple.

We’d like to extend our thanks to Josh Goldberg and Mateusz Burzyński who collaborated to lift this restriction .

## Easier Method Usage for Unions of Arrays

 In previous versions of TypeScript, calling a method on a union of arrays could end in pain.

 ts ` declare let array : string [] | number []; array . filter ( x => !! x ); // ~~~~~~ error! // This expression is not callable. // Each member of the union type '...' has signatures, // but none of those signatures are compatible // with each other. `
 In this example, TypeScript would try to see if each version of `filter` is compatible across `string[]` and `number[]`.
Without a coherent strategy, TypeScript threw its hands in the air and said “I can’t make it work”.

In TypeScript 5.2, before giving up in these cases, unions of arrays are treated as a special case.
A new array type is constructed out of each member’s element type, and then the method is invoked on that.

Taking the above example, `string[] | number[]` is transformed into `(string | number)[]` (or `Array&#x3C;string | number>`), and `filter` is invoked on that type.
There is a slight caveat which is that `filter` will produce an `Array&#x3C;string | number>` instead of a `string[] | number[]`;
but for a freshly produced value there is less risk of something “going wrong”.

This means lots of methods like `filter`, `find`, `some`, `every`, and `reduce` should all be invokable on unions of arrays in cases where they were not previously.

You can read up more details on the implementing pull request .

## Type-Only Import Paths with TypeScript Implementation File Extensions

 TypeScript now allows both declaration and implementation file extensions to be included in type-only import paths, regardless of whether `allowImportingTsExtensions` is enabled.

This means that you can now write `import type` statements that use `.ts`, `.mts`, `.cts`, and `.tsx` file extensions.

 ts ` import type { JustAType } from "./justTypes.ts" ; export function f ( param : JustAType ) { // ... } `
 It also means that `import()` types, which can be used in both TypeScript and JavaScript with JSDoc, can use those file extensions.

 js ` /** * @param {import("./justTypes.ts").JustAType} param */ export function f ( param ) { // ... } `
 For more information, see the change here .

## Comma Completions for Object Members

 It can be easy to forget to add a comma when adding a new property to an object.
Previously, if you forgot a comma and requested auto-completion, TypeScript would confusingly give poor unrelated completion results.

TypeScript 5.2 now gracefully provides object member completions when you’re missing a comma.
But to just skip past hitting you with a syntax error, it will also auto-insert the missing comma.

For more information, see the implementation here .

## Inline Variable Refactoring

 TypeScript 5.2 now has a refactoring to inline the contents of a variable to all usage sites.

 .

Using the “inline variable” refactoring will eliminate the variable and replace all the variable’s usages with its initializer.
Note that this may cause that initializer’s side-effects to run at a different time, and as many times as the variable has been used.

For more details, see the implementing pull request .

## Optimized Checks for Ongoing Type Compatibility

 Because TypeScript is a structural type system, types occasionally need to be compared in a member-wise fashion;
however, recursive types add some issues here.
For example:

 ts ` interface A { value : A ; other : string ; } interface B { value : B ; other : number ; } `
 When checking whether the type `A` is compatible with the type `B`, TypeScript will end up checking whether the types of `value` in `A` and `B` are respectively compatible.
At this point, the type system needs to stop checking any further and proceed to check other members.
To do this, the type system has to track when any two types are already being related.

Previously TypeScript already kept a stack of type pairs, and iterated through that to determine whether those types are being related.
When this stack is shallow that’s not a problem; but when the stack isn’t shallow, that, uh, is a problem .

In TypeScript 5.3, a simple `Set` helps track this information.
This reduced the time spent on a reported test case that used the drizzle library by over 33%!

 ` Benchmark 1: old Time (mean ± σ): 3.115 s ± 0.067 s [User: 4.403 s, System: 0.124 s] Range (min … max): 3.018 s … 3.196 s 10 runs Benchmark 2: new Time (mean ± σ): 2.072 s ± 0.050 s [User: 3.355 s, System: 0.135 s] Range (min … max): 1.985 s … 2.150 s 10 runs Summary 'new' ran 1.50 ± 0.05 times faster than 'old' `
 Read more on the change here .

## Breaking Changes and Correctness Fixes

 TypeScript strives not to unnecessarily introduce breaks;
however, occasionally we must make corrections and improvements so that code can be better-analyzed.

### `lib.d.ts` Changes

 Types generated for the DOM may have an impact on your codebase.
For more information, see the DOM updates for TypeScript 5.2 .

### `labeledElementDeclarations` May Hold `undefined` Elements

 In order to support a mixture of labeled and unlabeled elements , TypeScript’s API has changed slightly.
The `labeledElementDeclarations` property of `TupleType` may hold `undefined` for at each position where an element is unlabeled.

 diff ` interface TupleType { - labeledElementDeclarations?: readonly (NamedTupleMember | ParameterDeclaration)[]; + labeledElementDeclarations?: readonly (NamedTupleMember | ParameterDeclaration | undefined)[]; } `

### `module` and `moduleResolution` Must Match Under Recent Node.js settings

 The `--module` and `--moduleResolution` options each support a `node16` and `nodenext` setting.
These are effectively “modern Node.js” settings that should be used on any recent Node.js project.
What we’ve found is that when these two options don’t agree on whether they are using Node.js-related settings, projects are effectively misconfigured.

In TypeScript 5.2, when using `node16` or `nodenext` for either of the `--module` and `--moduleResolution` options, TypeScript now requires the other to have a similar Node.js-related setting.
In cases where the settings diverge, you’ll likely get an error message like either

 ` Option 'moduleResolution' must be set to 'NodeNext' (or left unspecified) when option 'module' is set to 'NodeNext'. `
 or

 ` Option 'module' must be set to 'Node16' when option 'moduleResolution' is set to 'Node16'. `
 So for example `--module esnext --moduleResolution node16` will be rejected — but you may be better off just using `--module nodenext` alone, or `--module esnext --moduleResolution bundler`.

For more information, see the change here .

### Consistent Export Checking for Merged Symbols

 When two declarations merge, they must agree on whether they are both exported.
Due to a bug, TypeScript missed specific cases in ambient contexts, like in declaration files or `declare module` blocks.
For example, it would not issue an error on a case like the following, where `replaceInFile` is declared once as an exported function, and one as an un-exported namespace.

 ts ` declare module 'replace-in-file' { export function replaceInFile ( config : unknown ): Promise < unknown []>; export {}; namespace replaceInFile { export function sync ( config : unknown ): unknown []; } } `
 In an ambient module, adding an `export { ... }` or a similar construct like `export default ...` implicitly changes whether all declarations are automatically exported.
TypeScript now recognizes these unfortunately confusing semantics more consistently, and issues an error on the fact that all declarations of `replaceInFile` need to agree in their modifiers, and will issue the following error:

 ` Individual declarations in merged declaration 'replaceInFile' must be all exported or all local. `
 For more information, see the change here .
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: AB EI Last updated: Jun 15, 2026

## Typescript 5 1

Was this page helpful?

# TypeScript 5.1

## Easier Implicit Returns for `undefined`-Returning Functions

 In JavaScript, if a function finishes running without hitting a `return`, it returns the value `undefined`.

 ts ` function foo () { // no return } // x = undefined let x = foo (); `
 However, in previous versions of TypeScript, the only functions that could have absolutely no return statements were `void`- and `any`-returning functions.
That meant that even if you explicitly said “this function returns `undefined`” you were forced to have at least one return statement.

 ts ` // ✅ fine - we inferred that 'f1' returns 'void' function f1 () { // no returns } // ✅ fine - 'void' doesn't need a return statement function f2 (): void { // no returns } // ✅ fine - 'any' doesn't need a return statement function f3 (): any { // no returns } // ❌ error! // A function whose declared type is neither 'void' nor 'any' must return a value. function f4 (): undefined { // no returns } `
 This could be a pain if some API expected a function returning `undefined` - you would need to have either at least one explicit return of `undefined` or a `return` statement and an explicit annotation.

 ts ` declare function takesFunction ( f : () => undefined ): undefined ; // ❌ error! // Argument of type '() => void' is not assignable to parameter of type '() => undefined'. takesFunction (() => { // no returns }); // ❌ error! // A function whose declared type is neither 'void' nor 'any' must return a value. takesFunction ((): undefined => { // no returns }); // ❌ error! // Argument of type '() => void' is not assignable to parameter of type '() => undefined'. takesFunction (() => { return ; }); // ✅ works takesFunction (() => { return undefined ; }); // ✅ works takesFunction ((): undefined => { return ; }); `
 This behavior was frustrating and confusing, especially when calling functions outside of one’s control.
Understanding the interplay between inferring `void` over `undefined`, whether an `undefined`-returning function needs a `return` statement, etc. seems like a distraction.

First, TypeScript 5.1 now allows `undefined`-returning functions to have no return statement.

 ts ` // ✅ Works in TypeScript 5.1! function f4 (): undefined { // no returns } // ✅ Works in TypeScript 5.1! takesFunction ((): undefined => { // no returns }); `
 Second, if a function has no return expressions and is being passed to something expecting a function that returns `undefined`, TypeScript infers `undefined` for that function’s return type.

 ts ` // ✅ Works in TypeScript 5.1! takesFunction ( function f () { // ^ return type is undefined // no returns }); // ✅ Works in TypeScript 5.1! takesFunction ( function f () { // ^ return type is undefined return ; }); `
 To address another similar pain-point, under TypeScript’s `--noImplicitReturns` option, functions returning only `undefined` now have a similar exception to `void`, in that not every single code path must end in an explicit `return`.

 ts ` // ✅ Works in TypeScript 5.1 under '--noImplicitReturns'! function f (): undefined { if ( Math . random ()) { // do some stuff... return ; } } `
 For more information, you can read up on the original issue and the implementing pull request .

## Unrelated Types for Getters and Setters

 TypeScript 4.3 made it possible to say that a `get` and `set` accessor pair might specify two different types.

 ts ` interface Serializer { set value ( v : string | number | boolean ); get value (): string ; } declare let box : Serializer ; // Allows writing a 'boolean' box . value = true ; // Comes out as a 'string' console . log ( box . value . toUpperCase ()); `
 Initially we required that the `get` type had to be a subtype of the `set` type.
This meant that writing

 ts ` box . value = box . value ; `
 would always be valid.

However, there are plenty of existing and proposed APIs that have completely unrelated types between their getters and setters.
For example, consider one of the most common examples - the `style` property in the DOM and `CSSStyleRule` API.
Every style rule has a `style` property that is a `CSSStyleDeclaration` ;
however, if you try to write to that property, it will only work correctly with a string!

TypeScript 5.1 now allows completely unrelated types for `get` and `set` accessor properties, provided that they have explicit type annotations.
And while this version of TypeScript does not yet change the types for these built-in interfaces, `CSSStyleRule` can now be defined in the following way:

 ts ` interface CSSStyleRule { // ... /** Always reads as a `CSSStyleDeclaration` */ get style (): CSSStyleDeclaration ; /** Can only write a `string` here. */ set style ( newValue : string ); // ... } `
 This also allows other patterns like requiring `set` accessors to accept only “valid” data, but specifying that `get` accessors may return `undefined` if some underlying state hasn’t been initialized yet.

 ts ` class SafeBox { #value : string | undefined ; // Only accepts strings! set value ( newValue : string ) { } // Must check for 'undefined'! get value (): string | undefined { return this . #value ; } } `
 In fact, this is similar to how optional properties are checked under `--exactOptionalProperties`.

You can read up more on the implementing pull request .

## Decoupled Type-Checking Between JSX Elements and JSX Tag Types

 One pain point TypeScript had with JSX was its requirements on the type of every JSX element’s tag.

For context, a JSX element is either of the following:

 tsx ` // A self-closing JSX tag < Foo /> // A regular element with an opening/closing tag < Bar ></ Bar > `
 When type-checking `&#x3C;Foo />` or `&#x3C;Bar>&#x3C;/Bar>`, TypeScript always looks up a namespace called `JSX` and fetches a type out of it called `Element` - or more directly, it looks up `JSX.Element`.

But to check whether `Foo` or `Bar` themselves were valid to use as tag names, TypeScript would roughly just grab the types returned or constructed by `Foo` or `Bar` and check for compatibility with `JSX.Element` (or another type called `JSX.ElementClass` if the type is constructable).

The limitations here meant that components could not be used if they returned or “rendered” a more broad type than just `JSX.Element`.
For example, a JSX library might be fine with a component returning `string`s or `Promise`s.

As a more concrete example, React is considering adding limited support for components that return `Promise`s , but existing versions of TypeScript cannot express that without someone drastically loosening the type of `JSX.Element`.

 tsx ` import * as React from "react" ; async function Foo () { return <div></div> ; } let element = < Foo /> ; // ~~~ // 'Foo' cannot be used as a JSX component. // Its return type 'Promise<Element>' is not a valid JSX element. `
 To provide libraries with a way to express this, TypeScript 5.1 now looks up a type called `JSX.ElementType`.
`ElementType` specifies precisely what is valid to use as a tag in a JSX element.
So it might be typed today as something like

 tsx ` namespace JSX { export type ElementType = // All the valid lowercase tags keyof IntrinsicAttributes // Function components ( props : any ) => Element // Class components new ( props : any ) => ElementClass ; export interface IntrinsicAttributes extends /*...*/ {} export type Element = /*...*/ ; export type ElementClass = /*...*/ ; } `
 We’d like to extend our thanks to Sebastian Silbermann who contributed this change !

## Namespaced JSX Attributes

 TypeScript now supports namespaced attribute names when using JSX.

 tsx ` import * as React from "react" ; // Both of these are equivalent: const x = < Foo a : b = "hello" /> ; const y = < Foo a : b = "hello" /> ; interface FooProps { "a:b" : string ; } function Foo ( props : FooProps ) { return <div> { props [ "a:b" ] } </div> ; } `
 Namespaced tag names are looked up in a similar way on `JSX.IntrinsicAttributes` when the first segment of the name is a lowercase name.

 tsx ` // In some library's code or in an augmentation of that library: namespace JSX { interface IntrinsicElements { [ "a:b" ]: { prop : string }; } } // In our code: let x = <a : b prop = "hello!" /> ; `
 This contribution was provided thanks to Oleksandr Tarasiuk .

## `typeRoots` Are Consulted In Module Resolution

 When TypeScript’s specified module lookup strategy is unable to resolve a path, it will now resolve packages relative to the specified `typeRoots`.

See this pull request for more details.

## Move Declarations to Existing Files

 In addition to moving declarations to new files, TypeScript now ships a preview feature for moving declarations to existing files as well.
You can try this functionality out in a recent version of Visual Studio Code.

Keep in mind that this feature is currently in preview, and we are seeking further feedback on it.

 https://github.com/microsoft/TypeScript/pull/53542

## Linked Cursors for JSX Tags

 TypeScript now supports linked editing for JSX tag names.
Linked editing (occasionally called “mirrored cursors”) allows an editor to edit multiple locations at the same time automatically.

This new feature should work in both TypeScript and JavaScript files, and can be enabled in Visual Studio Code Insiders.
In Visual Studio Code, you can either edit the `Editor: Linked Editing` option in the Settings UI:

or configure `editor.linkedEditing` in your JSON settings file:

 jsonc ` { // ... "editor.linkedEditing" : true , } `
 This feature will also be supported by Visual Studio 17.7 Preview 1.

You can take a look at our implementation of linked editing here!

## Snippet Completions for `@param` JSDoc Tags

 TypeScript now provides snippet completions when typing out a `@param` tag in both TypeScript and JavaScript files.
This can help cut down on some typing and jumping around text as you document your code or add JSDoc types in JavaScript.

You can check out how this new feature was implemented on GitHub .

## Optimizations

### Avoiding Unnecessary Type Instantiation

 TypeScript 5.1 now avoids performing type instantiation within object types that are known not to contain references to outer type parameters.
This has the potential to cut down on many unnecessary computations, and reduced the type-checking time of material-ui’s docs directory by over 50%.

You can see the changes involved for this change on GitHub .

### Negative Case Checks for Union Literals

 When checking if a source type is part of a union type, TypeScript will first do a fast look-up using an internal type identifier for that source.
If that look-up fails, then TypeScript checks for compatibility against every type within the union.

When relating a literal type to a union of purely literal types, TypeScript can now avoid that full walk against every other type in the union.
This assumption is safe because TypeScript always interns/caches literal types - though there are some edge cases to handle relating to “fresh” literal types.

 This optimization was able to reduce the type-checking time of the code in this issue from about 45 seconds to about 0.4 seconds.

### Reduced Calls into Scanner for JSDoc Parsing

 When older versions of TypeScript parsed out a JSDoc comment, they would use the scanner/tokenizer to break the comment into fine-grained tokens and piece the contents back together.
This could be helpful for normalizing comment text, so that multiple spaces would just collapse into one;
but it was extremely “chatty” and meant the parser and scanner would jump back and forth very often, adding overhead to JSDoc parsing.

TypeScript 5.1 has moved more logic around breaking down JSDoc comments into the scanner/tokenizer.
The scanner now returns larger chunks of content directly to the parser to do as it needs.

 These changes have brought down the parse time of several 10Mb mostly-prose-comment JavaScript files by about half.
For a more realistic example, our performance suite’s snapshot of xstate dropped about 300ms of parse time, making it faster to load and analyze.

## Breaking Changes

### ES2020 and Node.js 14.17 as Minimum Runtime Requirements

 TypeScript 5.1 now ships JavaScript functionality that was introduced in ECMAScript 2020.
As a result, at minimum TypeScript must be run in a reasonably modern runtime.
For most users, this means TypeScript now only runs on Node.js 14.17 and later.

If you try running TypeScript 5.1 under an older version of Node.js such as Node 10 or 12, you may see an error like the following from running either `tsc.js` or `tsserver.js`:

 ` node_modules/typescript/lib/tsserver.js:2406 for (let i = startIndex ?? 0; i < array.length; i++) { ^ SyntaxError: Unexpected token '?' at wrapSafe (internal/modules/cjs/loader.js:915:16) at Module._compile (internal/modules/cjs/loader.js:963:27) at Object.Module._extensions..js (internal/modules/cjs/loader.js:1027:10) at Module.load (internal/modules/cjs/loader.js:863:32) at Function.Module._load (internal/modules/cjs/loader.js:708:14) at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:60:12) at internal/main/run_main_module.js:17:47 `
 Additionally, if you try installing TypeScript you’ll get something like the following error messages from npm:

 ` npm WARN EBADENGINE Unsupported engine { npm WARN EBADENGINE package: 'typescript@5.1.1-rc', npm WARN EBADENGINE required: { node: '>=14.17' }, npm WARN EBADENGINE current: { node: 'v12.22.12', npm: '8.19.2' } npm WARN EBADENGINE } `
 from Yarn:

 ` error typescript@5.1.1-rc: The engine "node" is incompatible with this module. Expected version ">=14.17". Got "12.22.12" error Found incompatible module. `

 See more information around this change here .

### Explicit `typeRoots` Disables Upward Walks for `node_modules/@types`

 Previously, when the `typeRoots` option was specified in a `tsconfig.json` but resolution to any `typeRoots` directories had failed, TypeScript would still continue walking up parent directories, trying to resolve packages within each parent’s `node_modules/@types` folder.

This behavior could prompt excessive look-ups and has been disabled in TypeScript 5.1.
As a result, you may begin to see errors like the following based on entries in your `tsconfig.json`’s `types` option or `/// &#x3C;reference >` directives

 ` error TS2688: Cannot find type definition file for 'node'. error TS2688: Cannot find type definition file for 'mocha'. error TS2688: Cannot find type definition file for 'jasmine'. error TS2688: Cannot find type definition file for 'chai-http'. error TS2688: Cannot find type definition file for 'webpack-env"'. `
 The solution is typically to add specific entries for `node_modules/@types` to your `typeRoots`:

 jsonc ` { "compilerOptions" : { "types" : [ "node" , "mocha" ], "typeRoots" : [ // Keep whatever you had around before. "./some-custom-types/" , // You might need your local 'node_modules/@types'. "./node_modules/@types" , // You might also need to specify a shared 'node_modules/@types' // if you're using a "monorepo" layout. "../../node_modules/@types" , ] } } `
 More information is available on the original change on our issue tracker .
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: N BT LL Last updated: Jun 15, 2026

## Typescript 5 0

Was this page helpful?

# TypeScript 5.0

## Decorators

 Decorators are an upcoming ECMAScript feature that allow us to customize classes and their members in a reusable way.

Let’s consider the following code:

 ts ` class Person { name : string ; constructor ( name : string ) { this . name = name ; } greet () { console . log ( `Hello, my name is ${ this . name } .` ); } } const p = new Person ( "Ray" ); p . greet (); `
 `greet` is pretty simple here, but let’s imagine it’s something way more complicated - maybe it does some async logic, it’s recursive, it has side effects, etc.
Regardless of what kind of ball-of-mud you’re imagining, let’s say you throw in some `console.log` calls to help debug `greet`.

 ts ` class Person { name : string ; constructor ( name : string ) { this . name = name ; } greet () { console . log ( "LOG: Entering method." ); console . log ( `Hello, my name is ${ this . name } .` ); console . log ( "LOG: Exiting method." ) } } `
 This pattern is fairly common.
It sure would be nice if there was a way we could do this for every method!

This is where decorators come in.
We can write a function called `loggedMethod` that looks like the following:

 ts ` function loggedMethod ( originalMethod : any , _context : any ) { function replacementMethod ( this : any , ... args : any []) { console . log ( "LOG: Entering method." ) const result = originalMethod . call ( this , ... args ); console . log ( "LOG: Exiting method." ) return result ; } return replacementMethod ; } `
 “What’s the deal with all of these `any`s?
What is this, `any`Script!?”

Just be patient - we’re keeping things simple for now so that we can focus on what this function is doing.
Notice that `loggedMethod` takes the original method (`originalMethod`) and returns a function that

- logs an “Entering…” message

- passes along `this` and all of its arguments to the original method

- logs an “Exiting…” message, and

- returns whatever the original method returned.

Now we can use `loggedMethod` to decorate the method `greet`:

 ts ` class Person { name : string ; constructor ( name : string ) { this . name = name ; } @ loggedMethod greet () { console . log ( `Hello, my name is ${ this . name } .` ); } } const p = new Person ( "Ray" ); p . greet (); // Output: // // LOG: Entering method. // Hello, my name is Ray. // LOG: Exiting method. `
 We just used `loggedMethod` as a decorator above `greet` - and notice that we wrote it as `@loggedMethod`.
When we did that, it got called with the method target and a context object .
Because `loggedMethod` returned a new function, that function replaced the original definition of `greet`.

We didn’t mention it yet, but `loggedMethod` was defined with a second parameter.
It’s called a “context object”, and it has some useful information about how the decorated method was declared - like whether it was a `#private` member, or `static`, or what the name of the method was.
Let’s rewrite `loggedMethod` to take advantage of that and print out the name of the method that was decorated.

 ts ` function loggedMethod ( originalMethod : any , context : ClassMethodDecoratorContext ) { const methodName = String ( context . name ); function replacementMethod ( this : any , ... args : any []) { console . log ( `LOG: Entering method ' ${ methodName } '.` ) const result = originalMethod . call ( this , ... args ); console . log ( `LOG: Exiting method ' ${ methodName } '.` ) return result ; } return replacementMethod ; } `
 We’re now using the context parameter - and that it’s the first thing in `loggedMethod` that has a type stricter than `any` and `any[]`.
TypeScript provides a type called `ClassMethodDecoratorContext` that models the context object that method decorators take.

Apart from metadata, the context object for methods also has a useful function called `addInitializer`.
It’s a way to hook into the beginning of the constructor (or the initialization of the class itself if we’re working with `static`s).

As an example - in JavaScript, it’s common to write something like the following pattern:

 ts ` class Person { name : string ; constructor ( name : string ) { this . name = name ; this . greet = this . greet . bind ( this ); } greet () { console . log ( `Hello, my name is ${ this . name } .` ); } } `
 Alternatively, `greet` might be declared as a property initialized to an arrow function.

 ts ` class Person { name : string ; constructor ( name : string ) { this . name = name ; } greet = () => { console . log ( `Hello, my name is ${ this . name } .` ); }; } `
 This code is written to ensure that `this` isn’t re-bound if `greet` is called as a stand-alone function or passed as a callback.

 ts ` const greet = new Person ( "Ray" ). greet ; // We don't want this to fail! greet (); `
 We can write a decorator that uses `addInitializer` to call `bind` in the constructor for us.

 ts ` function bound ( originalMethod : any , context : ClassMethodDecoratorContext ) { const methodName = context . name ; if ( context . private ) { throw new Error ( `'bound' cannot decorate private properties like ${ methodName as string } .` ); } context . addInitializer ( function () { this [ methodName ] = this [ methodName ]. bind ( this ); }); } `
 `bound` isn’t returning anything - so when it decorates a method, it leaves the original alone.
Instead, it will add logic before any other fields are initialized.

 ts ` class Person { name : string ; constructor ( name : string ) { this . name = name ; } @ bound @ loggedMethod greet () { console . log ( `Hello, my name is ${ this . name } .` ); } } const p = new Person ( "Ray" ); const greet = p . greet ; // Works! greet (); `
 Notice that we stacked two decorators - `@bound` and `@loggedMethod`.
These decorations run in “reverse order”.
That is, `@loggedMethod` decorates the original method `greet`, and `@bound` decorates the result of `@loggedMethod`.
In this example, it doesn’t matter - but it could if your decorators have side-effects or expect a certain order.

Also worth noting - if you’d prefer stylistically, you can put these decorators on the same line.

 ts ` @ bound @ loggedMethod greet () { console . log ( `Hello, my name is ${ this . name } .` ); } `
 Something that might not be obvious is that we can even make functions that return decorator functions.
That makes it possible to customize the final decorator just a little.
If we wanted, we could have made `loggedMethod` return a decorator and customize how it logs its messages.

 ts ` function loggedMethod ( headMessage = "LOG:" ) { return function actualDecorator ( originalMethod : any , context : ClassMethodDecoratorContext ) { const methodName = String ( context . name ); function replacementMethod ( this : any , ... args : any []) { console . log ( ` ${ headMessage } Entering method ' ${ methodName } '.` ) const result = originalMethod . call ( this , ... args ); console . log ( ` ${ headMessage } Exiting method ' ${ methodName } '.` ) return result ; } return replacementMethod ; } } `
 If we did that, we’d have to call `loggedMethod` before using it as a decorator.
We could then pass in any string as the prefix for messages that get logged to the console.

 ts ` class Person { name : string ; constructor ( name : string ) { this . name = name ; } @ loggedMethod ( "⚠️" ) greet () { console . log ( `Hello, my name is ${ this . name } .` ); } } const p = new Person ( "Ray" ); p . greet (); // Output: // // ⚠️ Entering method 'greet'. // Hello, my name is Ray. // ⚠️ Exiting method 'greet'. `
 Decorators can be used on more than just methods!
They can be used on properties/fields, getters, setters, and auto-accessors.
Even classes themselves can be decorated for things like subclassing and registration.

To learn more about decorators in-depth, you can read up on Axel Rauschmayer’s extensive summary .

For more information about the changes involved, you can view the original pull request .

### Differences with Experimental Legacy Decorators

 If you’ve been using TypeScript for a while, you might be aware of the fact that it’s had support for “experimental” decorators for years.
While these experimental decorators have been incredibly useful, they modeled a much older version of the decorators proposal, and always required an opt-in compiler flag called `--experimentalDecorators`.
Any attempt to use decorators in TypeScript without this flag used to prompt an error message.

`--experimentalDecorators` will continue to exist for the foreseeable future;
however, without the flag, decorators will now be valid syntax for all new code.
Outside of `--experimentalDecorators`, they will be type-checked and emitted differently.
The type-checking rules and emit are sufficiently different that while decorators can be written to support both the old and new decorators behavior, any existing decorator functions are not likely to do so.

This new decorators proposal is not compatible with `--emitDecoratorMetadata`, and it does not allow decorating parameters.
Future ECMAScript proposals may be able to help bridge that gap.

On a final note: in addition to allowing decorators to be placed before the `export` keyword, the proposal for decorators now provides the option of placing decorators after `export` or `export default`.
The only exception is that mixing the two styles is not allowed.

 js ` // ✅ allowed @ register export default class Foo { // ... } // ✅ also allowed export default @ register class Bar { // ... } // ❌ error - before *and* after is not allowed @ before export @ after class Bar { // ... } `

### Writing Well-Typed Decorators

 The `loggedMethod` and `bound` decorator examples above are intentionally simple and omit lots of details about types.

Typing decorators can be fairly complex.
For example, a well-typed version of `loggedMethod` from above might look something like this:

 ts ` function loggedMethod < This , Args extends any [], Return >( target : ( this : This , ... args : Args ) => Return , context : ClassMethodDecoratorContext < This , ( this : This , ... args : Args ) => Return > ) { const methodName = String ( context . name ); function replacementMethod ( this : This , ... args : Args ): Return { console . log ( `LOG: Entering method ' ${ methodName } '.` ) const result = target . call ( this , ... args ); console . log ( `LOG: Exiting method ' ${ methodName } '.` ) return result ; } return replacementMethod ; } `
 We had to separately model out the type of `this`, the parameters, and the return type of the original method, using the type parameters `This`, `Args`, and `Return`.

Exactly how complex your decorators functions are defined depends on what you want to guarantee.
Just keep in mind, your decorators will be used more than they’re written, so a well-typed version will usually be preferable - but there’s clearly a trade-off with readability, so try to keep things simple.

More documentation on writing decorators will be available in the future - but this post should have a good amount of detail for the mechanics of decorators.

## `const` Type Parameters

 When inferring the type of an object, TypeScript will usually choose a type that’s meant to be general.
For example, in this case, the inferred type of `names` is `string[]`:

 ts ` type HasNames = { names : readonly string [] }; function getNamesExactly < T extends HasNames >( arg : T ): T [ "names" ] { return arg . names ; } // Inferred type: string[] const names = getNamesExactly ({ names: [ "Alice" , "Bob" , "Eve" ]}); `
 Usually the intent of this is to enable mutation down the line.

However, depending on what exactly `getNamesExactly` does and how it’s intended to be used, it can often be the case that a more-specific type is desired.

Up until now, API authors have typically had to recommend adding `as const` in certain places to achieve the desired inference:

 ts ` // The type we wanted: // readonly ["Alice", "Bob", "Eve"] // The type we got: // string[] const names1 = getNamesExactly ({ names: [ "Alice" , "Bob" , "Eve" ]}); // Correctly gets what we wanted: // readonly ["Alice", "Bob", "Eve"] const names2 = getNamesExactly ({ names: [ "Alice" , "Bob" , "Eve" ]} as const ); `
 This can be cumbersome and easy to forget.
In TypeScript 5.0, you can now add a `const` modifier to a type parameter declaration to cause `const`-like inference to be the default:

 ts ` type HasNames = { names : readonly string [] }; function getNamesExactly < const T extends HasNames >( arg : T ): T [ "names" ] { // ^^^^^ return arg . names ; } // Inferred type: readonly ["Alice", "Bob", "Eve"] // Note: Didn't need to write 'as const' here const names = getNamesExactly ({ names: [ "Alice" , "Bob" , "Eve" ] }); `
 Note that the `const` modifier doesn’t reject mutable values, and doesn’t require immutable constraints.
Using a mutable type constraint might give surprising results.
For example:

 ts ` declare function fnBad < const T extends string []>( args : T ): void ; // 'T' is still 'string[]' since 'readonly ["a", "b", "c"]' is not assignable to 'string[]' fnBad ([ "a" , "b" , "c" ]); `
 Here, the inferred candidate for `T` is `readonly ["a", "b", "c"]`, and a `readonly` array can’t be used where a mutable one is needed.
In this case, inference falls back to the constraint, the array is treated as `string[]`, and the call still proceeds successfully.

A better definition of this function should use `readonly string[]`:

 ts ` declare function fnGood < const T extends readonly string []>( args : T ): void ; // T is readonly ["a", "b", "c"] fnGood ([ "a" , "b" , "c" ]); `
 Similarly, remember to keep in mind that the `const` modifier only affects inference of object, array and primitive expressions that were written within the call, so arguments which wouldn’t (or couldn’t) be modified with `as const` won’t see any change in behavior:

 ts ` declare function fnGood < const T extends readonly string []>( args : T ): void ; const arr = [ "a" , "b" , "c" ]; // 'T' is still 'string[]'-- the 'const' modifier has no effect here fnGood ( arr ); `
 See the pull request and the ( first and second ) motivating issues for more details.

## Supporting Multiple Configuration Files in `extends`

 When managing multiple projects, it can be helpful to have a “base” configuration file that other `tsconfig.json` files can extend from.
That’s why TypeScript supports an `extends` field for copying over fields from `compilerOptions`.

 jsonc ` // packages/front-end/src/tsconfig.json { "extends" : "../../../tsconfig.base.json" , "compilerOptions" : { "outDir" : "../lib" , // ... } } `
 However, there are scenarios where you might want to extend from multiple configuration files.
For example, imagine using a TypeScript base configuration file shipped to npm .
If you want all your projects to also use the options from the `@tsconfig/strictest` package on npm, then there’s a simple solution: have `tsconfig.base.json` extend from `@tsconfig/strictest`:

 jsonc ` // tsconfig.base.json { "extends" : "@tsconfig/strictest/tsconfig.json" , "compilerOptions" : { // ... } } `
 This works to a point.
If you have any projects that don’t want to use `@tsconfig/strictest`, they have to either manually disable the options, or create a separate version of `tsconfig.base.json` that doesn’t extend from `@tsconfig/strictest`.

To give some more flexibility here, Typescript 5.0 now allows the `extends` field to take multiple entries.
For example, in this configuration file:

 jsonc ` { "extends" : [ "a" , "b" , "c" ], "compilerOptions" : { // ... } } `
 Writing this is kind of like extending `c` directly, where `c` extends `b`, and `b` extends `a`.
If any fields “conflict”, the latter entry wins.

So in the following example, both `strictNullChecks` and `noImplicitAny` are enabled in the final `tsconfig.json`.

 jsonc ` // tsconfig1.json { "compilerOptions" : { "strictNullChecks" : true } } // tsconfig2.json { "compilerOptions" : { "noImplicitAny" : true } } // tsconfig.json { "extends" : [ "./tsconfig1.json" , "./tsconfig2.json" ], "files" : [ "./index.ts" ] } `
 As another example, we can rewrite our original example in the following way.

 jsonc ` // packages/front-end/src/tsconfig.json { "extends" : [ "@tsconfig/strictest/tsconfig.json" , "../../../tsconfig.base.json" ], "compilerOptions" : { "outDir" : "../lib" , // ... } } `
 For more details, read more on the original pull request .

## All `enum`s Are Union `enum`s

 When TypeScript originally introduced enums, they were nothing more than a set of numeric constants with the same type.

 ts ` enum E { Foo = 10 , Bar = 20 , } `
 The only thing special about `E.Foo` and `E.Bar` was that they were assignable to anything expecting the type `E`.
Other than that, they were pretty much just `number`s.

 ts ` function takeValue ( e : E ) {} takeValue ( E . Foo ); // works takeValue ( 123 ); // error! `
 It wasn’t until TypeScript 2.0 introduced enum literal types that enums got a bit more special.
Enum literal types gave each enum member its own type, and turned the enum itself into a union of each member type.
They also allowed us to refer to only a subset of the types of an enum, and to narrow away those types.

 ts ` // Color is like a union of Red | Orange | Yellow | Green | Blue | Violet enum Color { Red , Orange , Yellow , Green , Blue , /* Indigo, */ Violet } // Each enum member has its own type that we can refer to! type PrimaryColor = Color . Red | Color . Green | Color . Blue ; function isPrimaryColor ( c : Color ): c is PrimaryColor { // Narrowing literal types can catch bugs. // TypeScript will error here because // we'll end up comparing 'Color.Red' to 'Color.Green'. // We meant to use ||, but accidentally wrote &&. return c === Color . Red && c === Color . Green && c === Color . Blue ; } `
 One issue with giving each enum member its own type was that those types were in some part associated with the actual value of the member.
In some cases it’s not possible to compute that value - for instance, an enum member could be initialized by a function call.

 ts ` enum E { Blah = Math . random () } `
 Whenever TypeScript ran into these issues, it would quietly back out and use the old enum strategy.
That meant giving up all the advantages of unions and literal types.

TypeScript 5.0 manages to make all enums into union enums by creating a unique type for each computed member.
That means that all enums can now be narrowed and have their members referenced as types as well.

For more details on this change, you can read the specifics on GitHub .

## `--moduleResolution bundler`

 TypeScript 4.7 introduced the `node16` and `nodenext` options for its `--module` and `--moduleResolution` settings.
The intent of these options was to better model the precise lookup rules for ECMAScript modules in Node.js;
however, this mode has many restrictions that other tools don’t really enforce.

For example, in an ECMAScript module in Node.js, any relative import needs to include a file extension.

 js ` // entry.mjs import * as utils from "./utils" ; // ❌ wrong - we need to include the file extension. import * as utils from "./utils.mjs" ; // ✅ works `
 There are certain reasons for this in Node.js and the browser - it makes file lookups faster and works better for naive file servers.
But for many developers using tools like bundlers, the `node16`/`nodenext` settings were cumbersome because bundlers don’t have most of these restrictions.
In some ways, the `node` resolution mode was better for anyone using a bundler.

But in some ways, the original `node` resolution mode was already out of date.
Most modern bundlers use a fusion of the ECMAScript module and CommonJS lookup rules in Node.js.
For example, extensionless imports work just fine just like in CommonJS, but when looking through the `export` conditions of a package, they’ll prefer an `import` condition just like in an ECMAScript file.

To model how bundlers work, TypeScript now introduces a new strategy: `--moduleResolution bundler`.

 jsonc ` { "compilerOptions" : { "target" : "esnext" , "moduleResolution" : "bundler" } } `
 If you are using a modern bundler like Vite, esbuild, swc, Webpack, Parcel, and others that implement a hybrid lookup strategy, the new `bundler` option should be a good fit for you.

On the other hand, if you’re writing a library that’s meant to be published on npm, using the `bundler` option can hide compatibility issues that may arise for your users who aren’t using a bundler.
So in these cases, using the `node16` or `nodenext` resolution options is likely to be a better path.

To read more on `--moduleResolution bundler`, take a look at the implementing pull request .

## Resolution Customization Flags

 JavaScript tooling may now model “hybrid” resolution rules, like in the `bundler` mode we described above.
Because tools may differ in their support slightly, TypeScript 5.0 provides ways to enable or disable a few features that may or may not work with your configuration.

### `allowImportingTsExtensions`

 `--allowImportingTsExtensions` allows TypeScript files to import each other with a TypeScript-specific extension like `.ts`, `.mts`, or `.tsx`.

This flag is only allowed when `--noEmit` or `--emitDeclarationOnly` is enabled, since these import paths would not be resolvable at runtime in JavaScript output files.
The expectation here is that your resolver (e.g. your bundler, a runtime, or some other tool) is going to make these imports between `.ts` files work.

### `resolvePackageJsonExports`

 `--resolvePackageJsonExports` forces TypeScript to consult the `exports` field of `package.json` files if it ever reads from a package in `node_modules`.

This option defaults to `true` under the `node16`, `nodenext`, and `bundler` options for `--moduleResolution`.

### `resolvePackageJsonImports`

 `--resolvePackageJsonImports` forces TypeScript to consult the `imports` field of `package.json` files when performing a lookup that starts with `#` from a file whose ancestor directory contains a `package.json`.

This option defaults to `true` under the `node16`, `nodenext`, and `bundler` options for `--moduleResolution`.

### `allowArbitraryExtensions`

 In TypeScript 5.0, when an import path ends in an extension that isn’t a known JavaScript or TypeScript file extension, the compiler will look for a declaration file for that path in the form of `{file basename}.d.{extension}.ts`.
For example, if you are using a CSS loader in a bundler project, you might want to write (or generate) declaration files for those stylesheets:

 css ` /* app.css */ .cookie-banner { display : none ; } `

```
 ts ` // app.d.css.ts declare const css : { cookieBanner : string ; }; export default css ; `
```

```
 ts ` // App.tsx import styles from "./app.css" ; styles . cookieBanner ; // string `
```

 By default, this import will raise an error to let you know that TypeScript doesn’t understand this file type and your runtime might not support importing it.
But if you’ve configured your runtime or bundler to handle it, you can suppress the error with the new `--allowArbitraryExtensions` compiler option.

Note that historically, a similar effect has often been achievable by adding a declaration file named `app.css.d.ts` instead of `app.d.css.ts` - however, this just worked through Node’s `require` resolution rules for CommonJS.
Strictly speaking, the former is interpreted as a declaration file for a JavaScript file named `app.css.js`.
Because relative files imports need to include extensions in Node’s ESM support, TypeScript would error on our example in an ESM file under `--moduleResolution node16` or `nodenext`.

For more information, read up the proposal for this feature and its corresponding pull request .

### `customConditions`

 `--customConditions` takes a list of additional conditions that should succeed when TypeScript resolves from an `exports` or `imports` field of a `package.json`.
These conditions are added to whatever existing conditions a resolver will use by default.

For example, when this field is set in a `tsconfig.json` as so:

 jsonc ` { "compilerOptions" : { "target" : "es2022" , "moduleResolution" : "bundler" , "customConditions" : [ "my-condition" ] } } `
 Any time an `exports` or `imports` field is referenced in `package.json`, TypeScript will consider conditions called `my-condition`.

So when importing from a package with the following `package.json`

 jsonc ` { // ... "exports" : { "." : { "my-condition" : "./foo.mjs" , "node" : "./bar.mjs" , "import" : "./baz.mjs" , "require" : "./biz.mjs" } } } `
 TypeScript will try to look for files corresponding to `foo.mjs`.

This field is only valid under the `node16`, `nodenext`, and `bundler` options for `--moduleResolution`

## `--verbatimModuleSyntax`

 By default, TypeScript does something called import elision .
Basically, if you write something like

 ts ` import { Car } from "./car" ; export function drive ( car : Car ) { // ... } `
 TypeScript detects that you’re only using an import for types and drops the import entirely.
Your output JavaScript might look something like this:

 js ` export function drive ( car ) { // ... } `
 Most of the time this is good, because if `Car` isn’t a value that’s exported from `./car`, we’ll get a runtime error.

But it does add a layer of complexity for certain edge cases.
For example, notice there’s no statement like `import "./car";` - the import was dropped entirely.
That actually makes a difference for modules that have side-effects or not.

TypeScript’s emit strategy for JavaScript also has another few layers of complexity - import elision isn’t always just driven by how an import is used - it often consults how a value is declared as well.
So it’s not always clear whether code like the following

 ts ` export { Car } from "./car" ; `
 should be preserved or dropped.
If `Car` is declared with something like a `class`, then it can be preserved in the resulting JavaScript file.
But if `Car` is only declared as a `type` alias or `interface`, then the JavaScript file shouldn’t export `Car` at all.

While TypeScript might be able to make these emit decisions based on information from across files, not every compiler can.

The `type` modifier on imports and exports helps with these situations a bit.
We can make it explicit whether an import or export is only being used for type analysis, and can be dropped entirely in JavaScript files by using the `type` modifier.

 ts ` // This statement can be dropped entirely in JS output import type * as car from "./car" ; // The named import/export 'Car' can be dropped in JS output import { type Car } from "./car" ; export { type Car } from "./car" ; `
 `type` modifiers are not quite useful on their own - by default, module elision will still drop imports, and nothing forces you to make the distinction between `type` and plain imports and exports.
So TypeScript has the flag `--importsNotUsedAsValues` to make sure you use the `type` modifier, `--preserveValueImports` to prevent some module elision behavior, and `--isolatedModules` to make sure that your TypeScript code works across different compilers.
Unfortunately, understanding the fine details of those 3 flags is hard, and there are still some edge cases with unexpected behavior.

TypeScript 5.0 introduces a new option called `--verbatimModuleSyntax` to simplify the situation.
The rules are much simpler - any imports or exports without a `type` modifier are left around.
Anything that uses the `type` modifier is dropped entirely.

 ts ` // Erased away entirely. import type { A } from "a" ; // Rewritten to 'import { b } from "bcd";' import { b , type c , type d } from "bcd" ; // Rewritten to 'import {} from "xyz";' import { type xyz } from "xyz" ; `
 With this new option, what you see is what you get.

That does have some implications when it comes to module interop though.
Under this flag, ECMAScript `import`s and `export`s won’t be rewritten to `require` calls when your settings or file extension implied a different module system.
Instead, you’ll get an error.
If you need to emit code that uses `require` and `module.exports`, you’ll have to use TypeScript’s module syntax that predates ES2015:

| **

 Input TypeScript**
 | **Output JavaScript**
 |

|
 ts ` import foo = require ( "foo" ); `

|

```
 js ` const foo = require ( "foo" ); `
```

|

|

```
 ts ` function foo () {} function bar () {} function baz () {} export = { foo , bar , baz }; `
```

|

```
 js ` function foo () {} function bar () {} function baz () {} module . exports = { foo , bar , baz }; `
```

|

 While this is a limitation, it does help make some issues more obvious.
For example, it’s very common to forget to set the `type` field in `package.json` under `--module node16`.
As a result, developers would start writing CommonJS modules instead of ES modules without realizing it, giving surprising lookup rules and JavaScript output.
This new flag ensures that you’re intentional about the file type you’re using because the syntax is intentionally different.

Because `--verbatimModuleSyntax` provides a more consistent story than `--importsNotUsedAsValues` and `--preserveValueImports`, those two existing flags are being deprecated in its favor.

For more details, read up on [the original pull request] https://github.com/microsoft/TypeScript/pull/52203 and its proposal issue .

## Support for `export type *`

 When TypeScript 3.8 introduced type-only imports, the new syntax wasn’t allowed on `export * from "module"` or `export * as ns from "module"` re-exports. TypeScript 5.0 adds support for both of these forms:

 ts ` // models/vehicles.ts export class Spaceship { // ... } // models/index.ts export type * as vehicles from "./vehicles" ; // main.ts import { vehicles } from "./models" ; function takeASpaceship ( s : vehicles . Spaceship ) { // ✅ ok - `vehicles` only used in a type position } function makeASpaceship () { return new vehicles . Spaceship (); // ^^^^^^^^ // 'vehicles' cannot be used as a value because it was exported using 'export type'. } `
 You can read more about the implementation here .

## `@satisfies` Support in JSDoc

 TypeScript 4.9 introduced the `satisfies` operator.
It made sure that the type of an expression was compatible, without affecting the type itself.
For example, let’s take the following code:

 ts ` interface CompilerOptions { strict ?: boolean ; outDir ?: string ; // ... } interface ConfigSettings { compilerOptions ?: CompilerOptions ; extends ?: string | string []; // ... } let myConfigSettings = { compilerOptions: { strict: true , outDir: "../lib" , // ... }, extends: [ "@tsconfig/strictest/tsconfig.json" , "../../../tsconfig.base.json" ], } satisfies ConfigSettings ; `
 Here, TypeScript knows that `myConfigSettings.extends` was declared with an array - because while `satisfies` validated the type of our object, it didn’t bluntly change it to `CompilerOptions` and lose information.
So if we want to map over `extends`, that’s fine.

 ts ` declare function resolveConfig ( configPath : string ): CompilerOptions ; let inheritedConfigs = myConfigSettings . extends . map ( resolveConfig ); `
 This was helpful for TypeScript users, but plenty of people use TypeScript to type-check their JavaScript code using JSDoc annotations.
That’s why TypeScript 5.0 is supporting a new JSDoc tag called `@satisfies` that does exactly the same thing.

`/** @satisfies */` can catch type mismatches:

 js ` // @ts-check /** * @typedef CompilerOptions * @prop {boolean} [strict] * @prop {string} [outDir] */ /** * @satisfies {CompilerOptions} */ let myCompilerOptions = { outdir: "../lib" , // ~~~~~~ oops! we meant outDir }; `
 But it will preserve the original type of our expressions, allowing us to use our values more precisely later on in our code.

 js ` // @ts-check /** * @typedef CompilerOptions * @prop {boolean} [strict] * @prop {string} [outDir] */ /** * @typedef ConfigSettings * @prop {CompilerOptions} [compilerOptions] * @prop {string | string[]} [extends] */ /** * @satisfies {ConfigSettings} */ let myConfigSettings = { compilerOptions: { strict: true , outDir: "../lib" , }, extends: [ "@tsconfig/strictest/tsconfig.json" , "../../../tsconfig.base.json" ], }; let inheritedConfigs = myConfigSettings . extends . map ( resolveConfig ); `
 `/** @satisfies */` can also be used inline on any parenthesized expression.
We could have written `myCompilerOptions` like this:

 ts ` let myConfigSettings = /** @satisfies {ConfigSettings} */ ({ compilerOptions: { strict: true , outDir: "../lib" , }, extends: [ "@tsconfig/strictest/tsconfig.json" , "../../../tsconfig.base.json" ], }); `
 Why?
Well, it usually makes more sense when you’re deeper in some other code, like a function call.

 js ` compileCode ( /** @satisfies {CompilerOptions} */ ({ // ... })); `
 This feature was provided thanks to Oleksandr Tarasiuk !

## `@overload` Support in JSDoc

 In TypeScript, you can specify overloads for a function.
Overloads give us a way to say that a function can be called with different arguments, and possibly return different results.
They can restrict how callers can actually use our functions, and refine what results they’ll get back.

 ts ` // Our overloads: function printValue ( str : string ): void ; function printValue ( num : number , maxFractionDigits ?: number ): void ; // Our implementation: function printValue ( value : string | number , maximumFractionDigits ?: number ) { if ( typeof value === "number" ) { const formatter = Intl . NumberFormat ( "en-US" , { maximumFractionDigits , }); value = formatter . format ( value ); } console . log ( value ); } `
 Here, we’ve said that `printValue` takes either a `string` or a `number` as its first argument.
If it takes a `number`, it can take a second argument to determine how many fractional digits we can print.

TypeScript 5.0 now allows JSDoc to declare overloads with a new `@overload` tag.
Each JSDoc comment with an `@overload` tag is treated as a distinct overload for the following function declaration.

 js ` // @ts-check /** * @overload * @param {string} value * @return {void} */ /** * @overload * @param {number} value * @param {number} [maximumFractionDigits] * @return {void} */ /** * @param {string | number} value * @param {number} [maximumFractionDigits] */ function printValue ( value , maximumFractionDigits ) { if ( typeof value === "number" ) { const formatter = Intl . NumberFormat ( "en-US" , { maximumFractionDigits , }); value = formatter . format ( value ); } console . log ( value ); } `
 Now regardless of whether we’re writing in a TypeScript or JavaScript file, TypeScript can let us know if we’ve called our functions incorrectly.

 ts ` // all allowed printValue ( "hello!" ); printValue ( 123.45 ); printValue ( 123.45 , 2 ); printValue ( "hello!" , 123 ); // error! `
 This new tag was implemented thanks to Tomasz Lenarcik .

## Passing Emit-Specific Flags Under `--build`

 TypeScript now allows the following flags to be passed under `--build` mode

- `--declaration`

- `--emitDeclarationOnly`

- `--declarationMap`

- `--sourceMap`

- `--inlineSourceMap`

This makes it way easier to customize certain parts of a build where you might have different development and production builds.

For example, a development build of a library might not need to produce declaration files, but a production build would.
A project can configure declaration emit to be off by default and simply be built with

 sh ` tsc --build -p ./my-project-dir `
 Once you’re done iterating in the inner loop, a “production” build can just pass the `--declaration` flag.

 sh ` tsc --build -p ./my-project-dir --declaration `
 More information on this change is available here .

## Case-Insensitive Import Sorting in Editors

 In editors like Visual Studio and VS Code, TypeScript powers the experience for organizing and sorting imports and exports.
Often though, there can be different interpretations of when a list is “sorted”.

For example, is the following import list sorted?

 ts ` import { Toggle , freeze , toBoolean , } from "./utils" ; `
 The answer might surprisingly be “it depends”.
If we don’t care about case-sensitivity, then this list is clearly not sorted.
The letter `f` comes before both `t` and `T`.

But in most programming languages, sorting defaults to comparing the byte values of strings.
The way JavaScript compares strings means that `"Toggle"` always comes before `"freeze"` because according to the ASCII character encoding , uppercase letters come before lowercase.
So from that perspective, the import list is sorted.

TypeScript previously considered the import list to be sorted because it was doing a basic case-sensitive sort.
This could be a point of frustration for developers who preferred a case- insensitive ordering, or who used tools like ESLint which require case-insensitive ordering by default.

TypeScript now detects case sensitivity by default.
This means that TypeScript and tools like ESLint typically won’t “fight” each other over how to best sort imports.

Our team has also been experimenting with further sorting strategies which you can read about here .
These options may eventually be configurable by editors.
For now, they are still unstable and experimental, and you can opt into them in VS Code today by using the `typescript.unstable` entry in your JSON options.
Below are all of the options you can try out (set to their defaults):

 jsonc ` { "typescript.unstable" : { // Should sorting be case-sensitive? Can be: // - true // - false // - "auto" (auto-detect) "organizeImportsIgnoreCase" : "auto" , // Should sorting be "ordinal" and use code points or consider Unicode rules? Can be: // - "ordinal" // - "unicode" "organizeImportsCollation" : "ordinal" , // Under `"organizeImportsCollation": "unicode"`, // what is the current locale? Can be: // - [any other locale code] // - "auto" (use the editor's locale) "organizeImportsLocale" : "en" , // Under `"organizeImportsCollation": "unicode"`, // should upper-case letters or lower-case letters come first? Can be: // - false (locale-specific) // - "upper" // - "lower" "organizeImportsCaseFirst" : false , // Under `"organizeImportsCollation": "unicode"`, // do runs of numbers get compared numerically (i.e. "a1" < "a2" < "a100")? Can be: // - true // - false "organizeImportsNumericCollation" : true , // Under `"organizeImportsCollation": "unicode"`, // do letters with accent marks/diacritics get sorted distinctly // from their "base" letter (i.e. is é different from e)? Can be // - true // - false "organizeImportsAccentCollation" : true }, "javascript.unstable" : { // same options valid here... }, } `
 You can read more details on the original work for auto-detecting and specifying case-insensitivity , followed by the the broader set of options .

## Exhaustive `switch`/`case` Completions

 When writing a `switch` statement, TypeScript now detects when the value being checked has a literal type.
If so, it will offer a completion that scaffolds out each uncovered `case`.

You can see specifics of the implementation on GitHub .

## Speed, Memory, and Package Size Optimizations

 TypeScript 5.0 contains lots of powerful changes across our code structure, our data structures, and algorithmic implementations.
What these all mean is that your entire experience should be faster - not just running TypeScript, but even installing it.

Here are a few interesting wins in speed and size that we’ve been able to capture relative to TypeScript 4.9.

| **

 Scenario**
| **Time or Size Relative to TS 4.9**
|

| material-ui build time
| 89%
|

| TypeScript Compiler startup time
| 89%
|

| Playwright build time
| 88%
|

| TypeScript Compiler self-build time
| 87%
|

| Outlook Web build time
| 82%
|

| VS Code build time
| 80%
|

| typescript npm Package Size
| 59%
|

How?
There are a few notable improvements we’d like give more details on in the future.
But we won’t make you wait for that blog post.

First off, we recently migrated TypeScript from namespaces to modules, allowing us to leverage modern build tooling that can perform optimizations like scope hoisting.
Using this tooling, revisiting our packaging strategy, and removing some deprecated code has shaved off about 26.4 MB from TypeScript 4.9’s 63.8 MB package size.
It also brought us a notable speed-up through direct function calls.

TypeScript also added more uniformity to internal object types within the compiler, and also slimmed the data stored on some of these object types as well.
This reduced polymorphic and megamorphic use sites, while offsetting most of the necessary memory consumption that was necessary for uniform shapes.

We’ve also performed some caching when serializing information to strings.
Type display, which can happen as part of error reporting, declaration emit, code completions, and more, can end up being fairly expensive.
TypeScript now caches some commonly used machinery to reuse across these operations.

Another notable change we made that improved our parser was leveraging `var` to occasionally side-step the cost of using `let` and `const` across closures.
This improved some of our parsing performance.

Overall, we expect most codebases should see speed improvements from TypeScript 5.0, and have consistently been able to reproduce wins between 10% to 20%.
Of course this will depend on hardware and codebase characteristics, but we encourage you to try it out on your codebase today!

For more information, see some of our notable optimizations:

- Migrate to Modules

- `Node` Monomorphization

- `Symbol` Monomorphization

- `Identifier` Size Reduction

- `Printer` Caching

- Limited Usage of `var`

## Breaking Changes and Deprecations

### Runtime Requirements

 TypeScript now targets ECMAScript 2018.
For Node users, that means a minimum version requirement of at least Node.js 10 and later.

### `lib.d.ts` Changes

 Changes to how types for the DOM are generated might have an impact on existing code.
Notably, certain properties have been converted from `number` to numeric literal types, and properties and methods for cut, copy, and paste event handling have been moved across interfaces.

### API Breaking Changes

 In TypeScript 5.0, we moved to modules, removed some unnecessary interfaces, and made some correctness improvements.
For more details on what’s changed, see our API Breaking Changes page.

### Forbidden Implicit Coercions in Relational Operators

 Certain operations in TypeScript will already warn you if you write code which may cause an implicit string-to-number coercion:

 ts ` function func ( ns : number | string ) { return ns * 4 ; // Error, possible implicit coercion } `
 In 5.0, this will also be applied to the relational operators `>`, `&#x3C;`, `&#x3C;=`, and `>=`:

 ts ` function func ( ns : number | string ) { return ns > 4 ; // Now also an error } `
 To allow this if desired, you can explicitly coerce the operand to a `number` using `+`:

 ts ` function func ( ns : number | string ) { return + ns > 4 ; // OK } `
 This correctness improvement was contributed courtesy of Mateusz Burzyński .

### Enum Overhaul

 TypeScript has had some long-standing oddities around `enum`s ever since its first release.
In 5.0, we’re cleaning up some of these problems, as well as reducing the concept count needed to understand the various kinds of `enum`s you can declare.

There are two main new errors you might see as part of this.
The first is that assigning an out-of-domain literal to an `enum` type will now error as one might expect:

 ts ` enum SomeEvenDigit { Zero = 0 , Two = 2 , Four = 4 } // Now correctly an error let m : SomeEvenDigit = 1 ; `
 The other is that declaration of certain kinds of indirected mixed string/number `enum` forms would, incorrectly, create an all-number `enum`:

 ts ` enum Letters { A = "a" } enum Numbers { one = 1 , two = Letters . A } // Now correctly an error const t : number = Numbers . two ; `
 You can see more details in relevant change .

### More Accurate Type-Checking for Parameter Decorators in Constructors Under `--experimentalDecorators`

 TypeScript 5.0 makes type-checking more accurate for decorators under `--experimentalDecorators`.
One place where this becomes apparent is when using a decorator on a constructor parameter.

 ts ` export declare const inject : ( entity : any ) => ( target : object , key : string | symbol , index ?: number ) => void ; export class Foo {} export class C { constructor (@ inject ( Foo ) private x : any ) { } } `
 This call will fail because `key` expects a `string | symbol`, but constructor parameters receive a key of `undefined`.
The correct fix is to change the type of `key` within `inject`.
A reasonable workaround if you’re using a library that can’t be upgraded is is to wrap `inject` in a more type-safe decorator function, and use a type-assertion on `key`.

For more details, see this issue .

### Deprecations and Default Changes

 In TypeScript 5.0, we’ve deprecated the following settings and setting values:

- `--target: ES3`

- `--out`

- `--noImplicitUseStrict`

- `--keyofStringsOnly`

- `--suppressExcessPropertyErrors`

- `--suppressImplicitAnyIndexErrors`

- `--noStrictGenericChecks`

- `--charset`

- `--importsNotUsedAsValues`

- `--preserveValueImports`

- `prepend` in project references

These configurations will continue to be allowed until TypeScript 5.5, at which point they will be removed entirely, however, you will receive a warning if you are using these settings.
In TypeScript 5.0, as well as future releases 5.1, 5.2, 5.3, and 5.4, you can specify `"ignoreDeprecations": "5.0"` to silence those warnings.
We’ll also shortly be releasing a 4.9 patch to allow specifying `ignoreDeprecations` to allow for smoother upgrades.
Aside from deprecations, we’ve changed some settings to better improve cross-platform behavior in TypeScript.

`--newLine`, which controls the line endings emitted in JavaScript files, used to be inferred based on the current operating system if not specified.
We think builds should be as deterministic as possible, and Windows Notepad supports line-feed line endings now, so the new default setting is `LF`.
The old OS-specific inference behavior is no longer available.

`--forceConsistentCasingInFileNames`, which ensured that all references to the same file name in a project agreed in casing, now defaults to `true`.
This can help catch differences issues with code written on case-insensitive file systems.

You can leave feedback and view more information on the tracking issue for 5.0 deprecations
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: AB B EI M M 2+ Last updated: Jun 15, 2026