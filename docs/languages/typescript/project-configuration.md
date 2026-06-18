# TypeScript - Project Configuration


## Tsconfig Json

Was this page helpful?

# What is a tsconfig.json

## Overview

 The presence of a `tsconfig.json` file in a directory indicates that the directory is the root of a TypeScript project.
The `tsconfig.json` file specifies the root files and the compiler options required to compile the project.

JavaScript projects can use a `jsconfig.json` file instead, which acts almost the same but has some JavaScript-related compiler flags enabled by default.

A project is compiled in one of the following ways:

## Using `tsconfig.json` or `jsconfig.json`

- By invoking tsc with no input files, in which case the compiler searches for the `tsconfig.json` file starting in the current directory and continuing up the parent directory chain.

- By invoking tsc with no input files and a `--project` (or just `-p`) command line option that specifies the path of a directory containing a `tsconfig.json` file, or a path to a valid `.json` file containing the configurations.

 When input files are specified on the command line, `tsconfig.json` files are ignored.

## Examples

 Example `tsconfig.json` files:

-
Using the `files` property

 ` { " compilerOptions " : { " module " : "commonjs" , " noImplicitAny " : true , " removeComments " : true , " preserveConstEnums " : true , " sourceMap " : true }, " files " : [ "core.ts" , "sys.ts" , "types.ts" , "scanner.ts" , "parser.ts" , "utilities.ts" , "binder.ts" , "checker.ts" , "emitter.ts" , "program.ts" , "commandLineParser.ts" , "tsc.ts" , "diagnosticInformationMap.generated.ts" ] } `

-
 Using the `include` and `exclude` properties

 ` { " compilerOptions " : { " module " : "system" , " noImplicitAny " : true , " removeComments " : true , " preserveConstEnums " : true , " outFile " : "../../built/local/tsc.js" , " sourceMap " : true }, " include " : [ "src/**/*" ], " exclude " : [ "**/*.spec.ts" ] } `

## TSConfig Bases

 Depending on the JavaScript runtime environment which you intend to run your code in, there may be a base configuration which you can use at github.com/tsconfig/bases .
These are `tsconfig.json` files which your project extends from which simplifies your `tsconfig.json` by handling the runtime support.

For example, if you were writing a project which uses Node.js version 12 and above, then you could use the npm module `@tsconfig/node12` :

 ` { " extends " : "@tsconfig/node12/tsconfig.json" , " compilerOptions " : { " preserveConstEnums " : true }, " include " : [ "src/**/*" ], " exclude " : [ "**/*.spec.ts" ] } `
 This lets your `tsconfig.json` focus on the unique choices for your project, and not all of the runtime mechanics. There are a few tsconfig bases already, and we’re hoping the community can add more for different environments.

## Details

 The `"compilerOptions"` property can be omitted, in which case the compiler’s defaults are used. See our full list of supported Compiler Options .

## TSConfig Reference

 To learn more about the hundreds of configuration options in the TSConfig Reference .

## Schema

 The `tsconfig.json` Schema can be found at the JSON Schema Store .
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: OT LG JB L☺ AG 4+ Last updated: Jun 15, 2026

## Compiler Options In Msbuild

Was this page helpful?

# Compiler Options in MSBuild

## Overview

 When you have an MSBuild based project which utilizes TypeScript such as an ASP.NET Core project, you can configure TypeScript in two ways. Either via a `tsconfig.json` or via the project settings.

## Using a `tsconfig.json`

 We recommend using a `tsconfig.json` for your project when possible. To add one to an existing project, add a new item to your project which is called a “TypeScript JSON Configuration File” in modern versions of Visual Studio.

The new `tsconfig.json` will then be used as the source of truth for TypeScript-specific build information like files and configuration. You can learn about how TSConfigs works here and there is a comprehensive reference here .

## Using Project Settings

 You can also define the configuration for TypeScript inside you project’s settings. This is done by editing the XML in your `.csproj` to define `PropertyGroups` which describe how the build can work:

 xml ` <PropertyGroup> <TypeScriptNoEmitOnError> true </TypeScriptNoEmitOnError> <TypeScriptNoImplicitReturns> true </TypeScriptNoImplicitReturns> </PropertyGroup> `
 There is a series of mappings for common TypeScript settings, these are settings which map directly to TypeScript cli options and are used to help you write a more understandable project file. You can use the TSConfig reference to get more information on what values and defaults are for each mapping.

### CLI Mappings

 | **

 MSBuild Config Name**
 | **TSC Flag**
 |

| `&#x3C;TypeScriptAllowJS&#x3E;`
| ` --allowJs `
|

|
Allow JavaScript files to be a part of your program. Use the `checkJS` option to get errors from these files.

|

| `&#x3C;TypeScriptRemoveComments&#x3E;`
| ` --removeComments `
|

|
Disable emitting comments.

|

| `&#x3C;TypeScriptNoImplicitAny&#x3E;`
| ` --noImplicitAny `
|

|
Enable error reporting for expressions and declarations with an implied `any` type..

|

| `&#x3C;TypeScriptGeneratesDeclarations&#x3E;`
| ` --declaration `
|

|
Generate .d.ts files from TypeScript and JavaScript files in your project.

|

| `&#x3C;TypeScriptModuleKind&#x3E;`
| ` --module `
|

|
Specify what module code is generated.

|

| `&#x3C;TypeScriptJSXEmit&#x3E;`
| ` --jsx `
|

|
Specify what JSX code is generated.

|

| `&#x3C;TypeScriptOutDir&#x3E;`
| ` --outDir `
|

|
Specify an output folder for all emitted files.

|

| `&#x3C;TypeScriptSourceMap&#x3E;`
| ` --sourcemap `
|

|
Create source map files for emitted JavaScript files.

|

| `&#x3C;TypeScriptTarget&#x3E;`
| ` --target `
|

|
Set the JavaScript language version for emitted JavaScript and include compatible library declarations.

|

| `&#x3C;TypeScriptNoResolve&#x3E;`
| ` --noResolve `
|

|
Disallow `import`s, `require`s or `&#x3C;reference>`s from expanding the number of files TypeScript should add to a project.

|

| `&#x3C;TypeScriptMapRoot&#x3E;`
| ` --mapRoot `
|

|
Specify the location where debugger should locate map files instead of generated locations.

|

| `&#x3C;TypeScriptSourceRoot&#x3E;`
| ` --sourceRoot `
|

|
Specify the root path for debuggers to find the reference source code.

|

| `&#x3C;TypeScriptCharset&#x3E;`
| ` --charset `
|

|
No longer supported. In early versions, manually set the text encoding for reading files.

|

| `&#x3C;TypeScriptEmitBOM&#x3E;`
| ` --emitBOM `
|

|
Emit a UTF-8 Byte Order Mark (BOM) in the beginning of output files.

|

| `&#x3C;TypeScriptNoLib&#x3E;`
| ` --noLib `
|

|
Disable including any library files, including the default lib.d.ts.

|

| `&#x3C;TypeScriptPreserveConstEnums&#x3E;`
| ` --preserveConstEnums `
|

|
Disable erasing `const enum` declarations in generated code.

|

| `&#x3C;TypeScriptSuppressImplicitAnyIndexErrors&#x3E;`
| ` --suppressImplicitAnyIndexErrors `
|

|
Suppress `noImplicitAny` errors when indexing objects that lack index signatures.

|

| `&#x3C;TypeScriptNoEmitHelpers&#x3E;`
| ` --noEmitHelpers `
|

|
Disable generating custom helper functions like `__extends` in compiled output.

|

| `&#x3C;TypeScriptInlineSourceMap&#x3E;`
| ` --inlineSourceMap `
|

|
Include sourcemap files inside the emitted JavaScript.

|

| `&#x3C;TypeScriptInlineSources&#x3E;`
| ` --inlineSources `
|

|
Include source code in the sourcemaps inside the emitted JavaScript.

|

| `&#x3C;TypeScriptNewLine&#x3E;`
| ` --newLine `
|

|
Set the newline character for emitting files.

|

| `&#x3C;TypeScriptIsolatedModules&#x3E;`
| ` --isolatedModules `
|

|
Ensure that each file can be safely transpiled without relying on other imports.

|

| `&#x3C;TypeScriptEmitDecoratorMetadata&#x3E;`
| ` --emitDecoratorMetadata `
|

|
Emit design-type metadata for decorated declarations in source files.

|

| `&#x3C;TypeScriptRootDir&#x3E;`
| ` --rootDir `
|

|
Specify the root folder within your source files.

|

| `&#x3C;TypeScriptExperimentalDecorators&#x3E;`
| ` --experimentalDecorators `
|

|
Enable experimental support for TC39 stage 2 draft decorators.

|

| `&#x3C;TypeScriptModuleResolution&#x3E;`
| ` --moduleResolution `
|

|
Specify how TypeScript looks up a file from a given module specifier.

|

| `&#x3C;TypeScriptSuppressExcessPropertyErrors&#x3E;`
| ` --suppressExcessPropertyErrors `
|

|
Disable reporting of excess property errors during the creation of object literals.

|

| `&#x3C;TypeScriptReactNamespace&#x3E;`
| ` --reactNamespace `
|

|
Specify the object invoked for `createElement`. This only applies when targeting `react` JSX emit.

|

| `&#x3C;TypeScriptSkipDefaultLibCheck&#x3E;`
| ` --skipDefaultLibCheck `
|

|
Skip type checking .d.ts files that are included with TypeScript.

|

| `&#x3C;TypeScriptAllowUnusedLabels&#x3E;`
| ` --allowUnusedLabels `
|

|
Disable error reporting for unused labels.

|

| `&#x3C;TypeScriptNoImplicitReturns&#x3E;`
| ` --noImplicitReturns `
|

|
Enable error reporting for codepaths that do not explicitly return in a function.

|

| `&#x3C;TypeScriptNoFallthroughCasesInSwitch&#x3E;`
| ` --noFallthroughCasesInSwitch `
|

|
Enable error reporting for fallthrough cases in switch statements.

|

| `&#x3C;TypeScriptAllowUnreachableCode&#x3E;`
| ` --allowUnreachableCode `
|

|
Disable error reporting for unreachable code.

|

| `&#x3C;TypeScriptForceConsistentCasingInFileNames&#x3E;`
| ` --forceConsistentCasingInFileNames `
|

|
Ensure that casing is correct in imports.

|

| `&#x3C;TypeScriptAllowSyntheticDefaultImports&#x3E;`
| ` --allowSyntheticDefaultImports `
|

|
Allow 'import x from y' when a module doesn't have a default export.

|

| `&#x3C;TypeScriptNoImplicitUseStrict&#x3E;`
| ` --noImplicitUseStrict `
|

|
Disable adding 'use strict' directives in emitted JavaScript files.

|

| `&#x3C;TypeScriptLib&#x3E;`
| ` --lib `
|

|
Specify a set of bundled library declaration files that describe the target runtime environment.

|

| `&#x3C;TypeScriptBaseUrl&#x3E;`
| ` --baseUrl `
|

|
Specify the base directory to resolve bare specifier module names.

|

| `&#x3C;TypeScriptDeclarationDir&#x3E;`
| ` --declarationDir `
|

|
Specify the output directory for generated declaration files.

|

| `&#x3C;TypeScriptNoImplicitThis&#x3E;`
| ` --noImplicitThis `
|

|
Enable error reporting when `this` is given the type `any`.

|

| `&#x3C;TypeScriptSkipLibCheck&#x3E;`
| ` --skipLibCheck `
|

|
Skip type checking all .d.ts files.

|

| `&#x3C;TypeScriptStrictNullChecks&#x3E;`
| ` --strictNullChecks `
|

|
When type checking, take into account `null` and `undefined`.

|

| `&#x3C;TypeScriptNoUnusedLocals&#x3E;`
| ` --noUnusedLocals `
|

|
Enable error reporting when a local variables aren't read.

|

| `&#x3C;TypeScriptNoUnusedParameters&#x3E;`
| ` --noUnusedParameters `
|

|
Raise an error when a function parameter isn't read

|

| `&#x3C;TypeScriptAlwaysStrict&#x3E;`
| ` --alwaysStrict `
|

|
Ensure 'use strict' is always emitted.

|

| `&#x3C;TypeScriptImportHelpers&#x3E;`
| ` --importHelpers `
|

|
Allow importing helper functions from tslib once per project, instead of including them per-file.

|

| `&#x3C;TypeScriptJSXFactory&#x3E;`
| ` --jsxFactory `
|

|
Specify the JSX factory function used when targeting React JSX emit, e.g. 'React.createElement' or 'h'

|

| `&#x3C;TypeScriptStripInternal&#x3E;`
| ` --stripInternal `
|

|
Disable emitting declarations that have `@internal` in their JSDoc comments.

|

| `&#x3C;TypeScriptCheckJs&#x3E;`
| ` --checkJs `
|

|
Enable error reporting in type-checked JavaScript files.

|

| `&#x3C;TypeScriptDownlevelIteration&#x3E;`
| ` --downlevelIteration `
|

|
Emit more compliant, but verbose and less performant JavaScript for iteration.

|

| `&#x3C;TypeScriptStrict&#x3E;`
| ` --strict `
|

|
Enable all strict type checking options.

|

| `&#x3C;TypeScriptNoStrictGenericChecks&#x3E;`
| ` --noStrictGenericChecks `
|

|
Disable strict checking of generic signatures in function types.

|

| `&#x3C;TypeScriptPreserveSymlinks&#x3E;`
| ` --preserveSymlinks `
|

|
Disable resolving symlinks to their realpath. This correlates to the same flag in node.

|

| `&#x3C;TypeScriptStrictFunctionTypes&#x3E;`
| ` --strictFunctionTypes `
|

|
When assigning functions, check to ensure parameters and the return values are subtype-compatible.

|

| `&#x3C;TypeScriptStrictPropertyInitialization&#x3E;`
| ` --strictPropertyInitialization `
|

|
Check for class properties that are declared but not set in the constructor.

|

| `&#x3C;TypeScriptESModuleInterop&#x3E;`
| ` --esModuleInterop `
|

|
Emit additional JavaScript to ease support for importing CommonJS modules. This enables `allowSyntheticDefaultImports` for type compatibility.

|

| `&#x3C;TypeScriptEmitDeclarationOnly&#x3E;`
| ` --emitDeclarationOnly `
|

|
Only output d.ts files and not JavaScript files.

|

| `&#x3C;TypeScriptKeyofStringsOnly&#x3E;`
| ` --keyofStringsOnly `
|

|
Make keyof only return strings instead of string, numbers or symbols. Legacy option.

|

| `&#x3C;TypeScriptUseDefineForClassFields&#x3E;`
| ` --useDefineForClassFields `
|

|
Emit ECMAScript-standard-compliant class fields.

|

| `&#x3C;TypeScriptDeclarationMap&#x3E;`
| ` --declarationMap `
|

|
Create sourcemaps for d.ts files.

|

| `&#x3C;TypeScriptResolveJsonModule&#x3E;`
| ` --resolveJsonModule `
|

|
Enable importing .json files

|

| `&#x3C;TypeScriptStrictBindCallApply&#x3E;`
| ` --strictBindCallApply `
|

|
Check that the arguments for `bind`, `call`, and `apply` methods match the original function.

|

| `&#x3C;TypeScriptNoEmitOnError&#x3E;`
| ` --noEmitOnError `
|

|
Disable emitting files if any type checking errors are reported.

|

### Additional Flags

 Because the MSBuild system passes arguments directly to the TypeScript CLI, you can use the option `TypeScriptAdditionalFlags` to provide specific flags which don’t have a mapping above.

For example, this would turn on `noPropertyAccessFromIndexSignature` :

 xml ` <TypeScriptAdditionalFlags> $(TypeScriptAdditionalFlags) --noPropertyAccessFromIndexSignature </TypeScriptAdditionalFlags> `

### Debug and Release Builds

 You can use PropertyGroup conditions to define different sets of configurations. For example, a common task is stripping comments and sourcemaps in production. In this example, we define a debug and release property group which have different TypeScript configurations:

 xml ` <PropertyGroup Condition = "'$(Configuration)' == 'Debug'" > <TypeScriptRemoveComments> false </TypeScriptRemoveComments> <TypeScriptSourceMap> true </TypeScriptSourceMap> </PropertyGroup> <PropertyGroup Condition = "'$(Configuration)' == 'Release'" > <TypeScriptRemoveComments> true </TypeScriptRemoveComments> <TypeScriptSourceMap> false </TypeScriptSourceMap> </PropertyGroup> <Import Project = "$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v$(VisualStudioVersion)\TypeScript\Microsoft.TypeScript.targets" Condition = "Exists('$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v$(VisualStudioVersion)\TypeScript\Microsoft.TypeScript.targets')" /> `

### ToolsVersion

 The value of `&#x3C;TypeScriptToolsVersion>1.7&#x3C;/TypeScriptToolsVersion>` property in the project file identifies the compiler version to use to build (1.7 in this example).
This allows a project to build against the same versions of the compiler on different machines.

If `TypeScriptToolsVersion` is not specified, the latest compiler version installed on the machine will be used to build.

Users using newer versions of TS, will see a prompt to upgrade their project on first load.

### TypeScriptCompileBlocked

 If you are using a different build tool to build your project (e.g. gulp, grunt , etc.) and VS for the development and debugging experience, set `&#x3C;TypeScriptCompileBlocked>true&#x3C;/TypeScriptCompileBlocked>` in your project.
This should give you all the editing support, but not the build when you hit F5.

### TypeScriptEnableIncrementalMSBuild (TypeScript 4.2 Beta and later)

 By default, MSBuild will attempt to only run the TypeScript compiler when the project’s source files have been updated since the last compilation.
However, if this behavior is causing issues, such as when TypeScript’s `incremental` option is enabled, set `&#x3C;TypeScriptEnableIncrementalMSBuild>false&#x3C;/TypeScriptEnableIncrementalMSBuild>` to ensure the TypeScript compiler is invoked with every run of MSBuild.
 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: MH OT Y DR BL 13+ Last updated: Jun 15, 2026

## Compiler Options

Was this page helpful?

# tsc CLI Options

## Using the CLI

 Running `tsc` locally will compile the closest project defined by a `tsconfig.json`, or you can compile a set of TypeScript
files by passing in a glob of files you want. When input files are specified on the command line, `tsconfig.json` files are
ignored.

 sh ` # Run a compile based on a backwards look through the fs for a tsconfig.json tsc # Emit JS for just the index.ts with the compiler defaults tsc index.ts # Emit JS for any .ts files in the folder src, with the default settings tsc src/*.ts # Emit files referenced in with the compiler settings from tsconfig.production.json tsc --project tsconfig.production.json # Emit d.ts files for a js file with showing compiler options which are booleans tsc index.js --declaration --emitDeclarationOnly # Emit a single .js file from two files via compiler options which take string arguments tsc app.ts util.ts --target esnext --outfile index.js `

## Compiler Options

 If you’re looking for more information about the compiler options in a tsconfig, check out the TSConfig Reference

### CLI Commands

 | **

 Flag**
 | **Type**
 |

 | `--all`
 | `boolean`

|

|
Show all compiler options.

 |

 | `--help`
 | `boolean`

|

|
Gives local information for help on the CLI.

 |

 | `--ignoreConfig`
 | `boolean`

|

|
Ignore the tsconfig found and build with commandline options and files.

 |

 | `--init`
 | `boolean`

|

|
Initializes a TypeScript project and creates a tsconfig.json file.

 |

 | `--listFilesOnly`
 | `boolean`

|

|
Print names of files that are part of the compilation and then stop processing.

 |

 | `--locale`
 | `string`

|

|
Set the language of the messaging from TypeScript. This does not affect emit.

 |

 | `--project`
 | `string`

|

|
Compile the project given the path to its configuration file, or to a folder with a 'tsconfig.json'.

 |

 | `--showConfig`
 | `boolean`

|

|
Print the final configuration instead of building.

 |

 | `--version`
 | `boolean`

|

|
Print the compiler's version.

 |

### Build Options

 | **

 Flag**
 | **Type**
 |

 | `--build`
 | `boolean`

|

|
Build one or more projects and their dependencies, if out of date

 |

 | `--clean`
 | `boolean`

|

|
Delete the outputs of all projects.

 |

 | `--dry`
 | `boolean`

|

|
Show what would be built (or deleted, if specified with '--clean')

 |

 | ` --force `
 | `boolean`

|

|
Build all projects, including those that appear to be up to date.

 |

 | ` --verbose `
 | `boolean`

|

|
Enable verbose logging.

 |

### Watch Options

 | **

 Flag**
 | **Type**
 |

 | ` --excludeDirectories `
 | `list`

|

|
Remove a list of directories from the watch process.

 |

 | ` --excludeFiles `
 | `list`

|

|
Remove a list of files from the watch mode's processing.

 |

 | ` --fallbackPolling `
 | `fixedinterval`, `priorityinterval`, `dynamicpriority`, or `fixedchunksize`

|

|
Specify what approach the watcher should use if the system runs out of native file watchers.

 |

 | ` --synchronousWatchDirectory `
 | `boolean`

|

|
Synchronously call callbacks and update the state of directory watchers on platforms that don`t support recursive watching natively.

 |

 | `--watch`
 | `boolean`

|

|
Watch input files.

 |

 | ` --watchDirectory `
 | `usefsevents`, `fixedpollinginterval`, `dynamicprioritypolling`, or `fixedchunksizepolling`

|

|
Specify how directories are watched on systems that lack recursive file-watching functionality.

 |

 | ` --watchFile `
 | `fixedpollinginterval`, `prioritypollinginterval`, `dynamicprioritypolling`, `fixedchunksizepolling`, `usefsevents`, or `usefseventsonparentdirectory`

|

|
Specify how the TypeScript watch mode works.

 |

### Compiler Flags

 | **

 Flag**
 | **Type**
 | **Default**
 |

 | ` --allowArbitraryExtensions `
 | `boolean`

 | `false`

|

|
Enable importing files with any extension, provided a declaration file is present.

 |

 | ` --allowImportingTsExtensions `
 | `boolean`

 | `true` if `rewriteRelativeImportExtensions` ; `false` otherwise.

|

|
Allow imports to include TypeScript file extensions.

 |

 | ` --allowJs `
 | `boolean`

 | `false`, unless `checkJs` is set

|

|
Allow JavaScript files to be a part of your program. Use the `checkJS` option to get errors from these files.

 |

 | ` --allowSyntheticDefaultImports `
 | `boolean`

 | `true` if `esModuleInterop` is enabled, `module` is `system`, or `moduleResolution` is `bundler`; `false` otherwise.

|

|
Allow 'import x from y' when a module doesn't have a default export.

 |

 | ` --allowUmdGlobalAccess `
 | `boolean`

 | `false`

|

|
Allow accessing UMD globals from modules.

 |

 | ` --allowUnreachableCode `
 | `boolean`

 |
|

|
Disable error reporting for unreachable code.

 |

 | ` --allowUnusedLabels `
 | `boolean`

 |
|

|
Disable error reporting for unused labels.

 |

 | ` --alwaysStrict `
 | `boolean`

 | `true` if `strict` ; `false` otherwise.

|

|
Ensure 'use strict' is always emitted.

 |

 | ` --assumeChangesOnlyAffectDirectDependencies `
 | `boolean`

 | `false`

|

|
Have recompiles in projects that use `incremental` and `watch` mode assume that changes within a file will only affect files directly depending on it.

 |

 | ` --baseUrl `
 | `string`

 |
|

|
Specify the base directory to resolve bare specifier module names.

 |

 | ` --charset `
 | `string`

 | `utf8`

|

|
No longer supported. In early versions, manually set the text encoding for reading files.

 |

 | ` --checkJs `
 | `boolean`

 | `false`

|

|
Enable error reporting in type-checked JavaScript files.

 |

 | ` --composite `
 | `boolean`

 | `false`

|

|
Enable constraints that allow a TypeScript project to be used with project references.

 |

 | ` --customConditions `
 | `list`

 |
|

|
Conditions to set in addition to the resolver-specific defaults when resolving imports.

 |

 | ` --declaration `
 | `boolean`

 | `true` if `composite` ; `false` otherwise.

|

|
Generate .d.ts files from TypeScript and JavaScript files in your project.

 |

 | ` --declarationDir `
 | `string`

 |
|

|
Specify the output directory for generated declaration files.

 |

 | ` --declarationMap `
 | `boolean`

 | `false`

|

|
Create sourcemaps for d.ts files.

 |

 | ` --diagnostics `
 | `boolean`

 | `false`

|

|
Output compiler performance information after building.

 |

 | ` --disableReferencedProjectLoad `
 | `boolean`

 | `false`

|

|
Reduce the number of projects loaded automatically by TypeScript.

 |

 | ` --disableSizeLimit `
 | `boolean`

 | `false`

|

|
Remove the 20mb cap on total source code size for JavaScript files in the TypeScript language server.

 |

 | ` --disableSolutionSearching `
 | `boolean`

 | `false`

|

|
Opt a project out of multi-project reference checking when editing.

 |

 | ` --disableSourceOfProjectReferenceRedirect `
 | `boolean`

 | `false`

|

|
Disable preferring source files instead of declaration files when referencing composite projects.

 |

 | ` --downlevelIteration `
 | `boolean`

 | `false`

|

|
Emit more compliant, but verbose and less performant JavaScript for iteration.

 |

 | ` --emitBOM `
 | `boolean`

 | `false`

|

|
Emit a UTF-8 Byte Order Mark (BOM) in the beginning of output files.

 |

 | ` --emitDeclarationOnly `
 | `boolean`

 | `false`

|

|
Only output d.ts files and not JavaScript files.

 |

 | ` --emitDecoratorMetadata `
 | `boolean`

 | `false`

|

|
Emit design-type metadata for decorated declarations in source files.

 |

 | ` --erasableSyntaxOnly `
 | `boolean`

 | `false`

|

|
Do not allow runtime constructs that are not part of ECMAScript.

 |

 | ` --esModuleInterop `
 | `boolean`

 | `true` if `module` is `node16`, `nodenext`, or `preserve`; `false` otherwise.

|

|
Emit additional JavaScript to ease support for importing CommonJS modules. This enables `allowSyntheticDefaultImports` for type compatibility.

 |

 | ` --exactOptionalPropertyTypes `
 | `boolean`

 | `false`

|

|
Interpret optional property types as written, rather than adding `undefined`.

 |

 | ` --experimentalDecorators `
 | `boolean`

 | `false`

|

|
Enable experimental support for TC39 stage 2 draft decorators.

 |

 | ` --explainFiles `
 | `boolean`

 | `false`

|

|
Print files read during the compilation including why it was included.

 |

 | ` --extendedDiagnostics `
 | `boolean`

 | `false`

|

|
Output more detailed compiler performance information after building.

 |

 | ` --forceConsistentCasingInFileNames `
 | `boolean`

 | `true`

|

|
Ensure that casing is correct in imports.

 |

 | ` --generateCpuProfile `
 | `string`

 | `profile.cpuprofile`

|

|
Emit a v8 CPU profile of the compiler run for debugging.

 |

 | ` --generateTrace `
 | `string`

 |
|

|
Generates an event trace and a list of types.

 |

 | ` --importHelpers `
 | `boolean`

 | `false`

|

|
Allow importing helper functions from tslib once per project, instead of including them per-file.

 |

 | ` --importsNotUsedAsValues `
 | `remove`, `preserve`, or `error`

 | `remove`

|

|
Specify emit/checking behavior for imports that are only used for types.

 |

 | ` --incremental `
 | `boolean`

 | `true` if `composite` ; `false` otherwise.

|

|
Save .tsbuildinfo files to allow for incremental compilation of projects.

 |

 | ` --inlineSourceMap `
 | `boolean`

 | `false`

|

|
Include sourcemap files inside the emitted JavaScript.

 |

 | ` --inlineSources `
 | `boolean`

 | `false`

|

|
Include source code in the sourcemaps inside the emitted JavaScript.

 |

 | ` --isolatedDeclarations `
 | `boolean`

 | `false`

|

|
Require sufficient annotation on exports so other tools can trivially generate declaration files.

 |

 | ` --isolatedModules `
 | `boolean`

 | `true` if `verbatimModuleSyntax` ; `false` otherwise.

|

|
Ensure that each file can be safely transpiled without relying on other imports.

 |

 | ` --jsx `
 | `preserve`, `react`, `react-native`, `react-jsx`, or `react-jsxdev`

 |
|

|
Specify what JSX code is generated.

 |

 | ` --jsxFactory `
 | `string`

 | `React.createElement`

|

|
Specify the JSX factory function used when targeting React JSX emit, e.g. 'React.createElement' or 'h'.

 |

 | ` --jsxFragmentFactory `
 | `string`

 | `React.Fragment`

|

|
Specify the JSX Fragment reference used for fragments when targeting React JSX emit e.g. 'React.Fragment' or 'Fragment'.

 |

 | ` --jsxImportSource `
 | `string`

 | `react`

|

|
Specify module specifier used to import the JSX factory functions when using `jsx: react-jsx*`.

 |

 | ` --keyofStringsOnly `
 | `boolean`

 | `false`

|

|
Make keyof only return strings instead of string, numbers or symbols. Legacy option.

 |

 | ` --lib `
 | `list`

 |
|

|
Specify a set of bundled library declaration files that describe the target runtime environment.

 |

 | ` --libReplacement `
 | `boolean`

 | `false`

|

|
Enable substitution of default `lib` files with custom ones.

 |

 | ` --listEmittedFiles `
 | `boolean`

 | `false`

|

|
Print the names of emitted files after a compilation.

 |

 | ` --listFiles `
 | `boolean`

 | `false`

|

|
Print all of the files read during the compilation.

 |

 | ` --mapRoot `
 | `string`

 |
|

|
Specify the location where debugger should locate map files instead of generated locations.

 |

 | ` --maxNodeModuleJsDepth `
 | `number`

 | `0`

|

|
Specify the maximum folder depth used for checking JavaScript files from `node_modules`. Only applicable with `allowJs` .

 |

 | ` --module `
 | `none`, `commonjs`, `amd`, `umd`, `system`, `es6`/`es2015`, `es2020`, `es2022`, `esnext`, `node16`, `node18`, `node20`, `nodenext`, or `preserve`

 | `CommonJS` if `target` is `ES5`; `ES6`/`ES2015` otherwise.

|

|
Specify what module code is generated.

 |

 | ` --moduleDetection `
 | `legacy`, `auto`, or `force`

 | "auto": Treat files with imports, exports, import.meta, jsx (with jsx: react-jsx), or esm format (with module: node16+) as modules.

|

|
Specify what method is used to detect whether a file is a script or a module.

 |

 | ` --moduleResolution `
 | `classic`, `node10`/`node`, `node16`, `nodenext`, or `bundler`

 | `Node10` if `module` is `CommonJS`; `Node16` if `module` is `Node16`, `Node18`, or `Node20`; `NodeNext` if `module` is `NodeNext`; `Bundler` if `module` is `Preserve`; `Classic` otherwise.

|

|
Specify how TypeScript looks up a file from a given module specifier.

 |

 | ` --moduleSuffixes `
 | `list`

 |
|

|
List of file name suffixes to search when resolving a module.

 |

 | ` --newLine `
 | `crlf` or `lf`

 | `lf`

|

|
Set the newline character for emitting files.

 |

 | ` --noCheck `
 | `boolean`

 | `false`

|

|
Disable full type checking (only critical parse and emit errors will be reported).

 |

 | ` --noEmit `
 | `boolean`

 | `false`

|

|
Disable emitting files from a compilation.

 |

 | ` --noEmitHelpers `
 | `boolean`

 | `false`

|

|
Disable generating custom helper functions like `__extends` in compiled output.

 |

 | ` --noEmitOnError `
 | `boolean`

 | `false`

|

|
Disable emitting files if any type checking errors are reported.

 |

 | ` --noErrorTruncation `
 | `boolean`

 | `false`

|

|
Disable truncating types in error messages.

 |

 | ` --noFallthroughCasesInSwitch `
 | `boolean`

 | `false`

|

|
Enable error reporting for fallthrough cases in switch statements.

 |

 | ` --noImplicitAny `
 | `boolean`

 | `true` if `strict` ; `false` otherwise.

|

|
Enable error reporting for expressions and declarations with an implied `any` type.

 |

 | ` --noImplicitOverride `
 | `boolean`

 | `false`

|

|
Ensure overriding members in derived classes are marked with an override modifier.

 |

 | ` --noImplicitReturns `
 | `boolean`

 | `false`

|

|
Enable error reporting for codepaths that do not explicitly return in a function.

 |

 | ` --noImplicitThis `
 | `boolean`

 | `true` if `strict` ; `false` otherwise.

|

|
Enable error reporting when `this` is given the type `any`.

 |

 | ` --noImplicitUseStrict `
 | `boolean`

 | `false`

|

|
Disable adding 'use strict' directives in emitted JavaScript files.

 |

 | ` --noLib `
 | `boolean`

 | `false`

|

|
Disable including any library files, including the default lib.d.ts.

 |

 | ` --noPropertyAccessFromIndexSignature `
 | `boolean`

 | `false`

|

|
Enforces using indexed accessors for keys declared using an indexed type.

 |

 | ` --noResolve `
 | `boolean`

 | `false`

|

|
Disallow `import`s, `require`s or `&#x3C;reference>`s from expanding the number of files TypeScript should add to a project.

 |

 | ` --noStrictGenericChecks `
 | `boolean`

 | `false`

|

|
Disable strict checking of generic signatures in function types.

 |

 | ` --noUncheckedIndexedAccess `
 | `boolean`

 | `false`

|

|
Add `undefined` to a type when accessed using an index.

 |

 | ` --noUncheckedSideEffectImports `
 | `boolean`

 | `true`

|

|
Check side effect imports.

 |

 | ` --noUnusedLocals `
 | `boolean`

 | `false`

|

|
Enable error reporting when local variables aren't read.

 |

 | ` --noUnusedParameters `
 | `boolean`

 | `false`

|

|
Raise an error when a function parameter isn't read.

 |

 | ` --out `
 | `string`

 |
|

|
Deprecated setting. Use `outFile` instead.

 |

 | ` --outDir `
 | `string`

 |
|

|
Specify an output folder for all emitted files.

 |

 | ` --outFile `
 | `string`

 |
|

|
Specify a file that bundles all outputs into one JavaScript file. If `declaration` is true, also designates a file that bundles all .d.ts output.

 |

 | ` --paths `
 | `object`

 |
|

|
Specify a set of entries that re-map imports to additional lookup locations.

 |

 | ` --plugins `
 | `list`

 |
|

|
Specify a list of language service plugins to include.

 |

 | ` --preserveConstEnums `
 | `boolean`

 | `true` if `isolatedModules` ; `false` otherwise.

|

|
Disable erasing `const enum` declarations in generated code.

 |

 | ` --preserveSymlinks `
 | `boolean`

 | `false`

|

|
Disable resolving symlinks to their realpath. This correlates to the same flag in node.

 |

 | ` --preserveValueImports `
 | `boolean`

 | `false`

|

|
Preserve unused imported values in the JavaScript output that would otherwise be removed.

 |

 | ` --preserveWatchOutput `
 | `boolean`

 | `false`

|

|
Disable wiping the console in watch mode.

 |

 | ` --pretty `
 | `boolean`

 | `true`

|

|
Enable color and formatting in TypeScript's output to make compiler errors easier to read.

 |

 | ` --reactNamespace `
 | `string`

 | `React`

|

|
Specify the object invoked for `createElement`. This only applies when targeting `react` JSX emit.

 |

 | ` --removeComments `
 | `boolean`

 | `false`

|

|
Disable emitting comments.

 |

 | ` --resolveJsonModule `
 | `boolean`

 | `false`

|

|
Enable importing .json files.

 |

 | ` --resolvePackageJsonExports `
 | `boolean`

 | `true` when `moduleResolution` is `node16`, `nodenext`, or `bundler`; otherwise `false`

|

|
Use the package.json 'exports' field when resolving package imports.

 |

 | ` --resolvePackageJsonImports `
 | `boolean`

 | `true` when `moduleResolution` is `node16`, `nodenext`, or `bundler`; otherwise `false`

|

|
Use the package.json 'imports' field when resolving imports.

 |

 | ` --rewriteRelativeImportExtensions `
 | `boolean`

 | `false`

|

|
Rewrite `.ts`, `.tsx`, `.mts`, and `.cts` file extensions in relative import paths to their JavaScript equivalent in output files.

 |

 | ` --rootDir `
 | `string`

 | Computed from the list of input files.

|

|
Specify the root folder within your source files.

 |

 | ` --rootDirs `
 | `list`

 | Computed from the list of input files.

|

|
Allow multiple folders to be treated as one when resolving modules.

 |

 | ` --skipDefaultLibCheck `
 | `boolean`

 | `false`

|

|
Skip type checking .d.ts files that are included with TypeScript.

 |

 | ` --skipLibCheck `
 | `boolean`

 | `false`

|

|
Skip type checking all .d.ts files.

 |

 | ` --sourceMap `
 | `boolean`

 | `false`

|

|
Create source map files for emitted JavaScript files.

 |

 | ` --sourceRoot `
 | `string`

 |
|

|
Specify the root path for debuggers to find the reference source code.

 |

 | ` --stableTypeOrdering `
 | `boolean`

 | `false`

|

|
Ensure types are ordered stably and deterministically across compilations.

 |

 | ` --stopBuildOnErrors `
 | `boolean`

 |
|

|
Skip building downstream projects on error in upstream project.

 |

 | ` --strict `
 | `boolean`

 | `true`

|

|
Enable all strict type-checking options.

 |

 | ` --strictBindCallApply `
 | `boolean`

 | `true` if `strict` ; `false` otherwise.

|

|
Check that the arguments for `bind`, `call`, and `apply` methods match the original function.

 |

 | ` --strictBuiltinIteratorReturn `
 | `boolean`

 | `true` if `strict` ; `false` otherwise.

|

|
Built-in iterators are instantiated with a TReturn type of undefined instead of any.

 |

 | ` --strictFunctionTypes `
 | `boolean`

 | `true` if `strict` ; `false` otherwise.

|

|
When assigning functions, check to ensure parameters and the return values are subtype-compatible.

 |

 | ` --strictNullChecks `
 | `boolean`

 | `true` if `strict` ; `false` otherwise.

|

|
When type checking, take into account `null` and `undefined`.

 |

 | ` --strictPropertyInitialization `
 | `boolean`

 | `true` if `strict` ; `false` otherwise.

|

|
Check for class properties that are declared but not set in the constructor.

 |

 | ` --stripInternal `
 | `boolean`

 | `false`

|

|
Disable emitting declarations that have `@internal` in their JSDoc comments.

 |

 | ` --suppressExcessPropertyErrors `
 | `boolean`

 | `false`

|

|
Disable reporting of excess property errors during the creation of object literals.

 |

 | ` --suppressImplicitAnyIndexErrors `
 | `boolean`

 | `false`

|

|
Suppress `noImplicitAny` errors when indexing objects that lack index signatures.

 |

 | ` --target `
 | `es3`, `es5`, `es6`/`es2015`, `es2016`, `es2017`, `es2018`, `es2019`, `es2020`, `es2021`, `es2022`, `es2023`, `es2024`, `es2025`, or `esnext`

 | `es2023` if `module` is `node20`; `esnext` if `module` is `nodenext`; `ES5` otherwise.

|

|
Set the JavaScript language version for emitted JavaScript and include compatible library declarations.

 |

 | ` --traceResolution `
 | `boolean`

 | `false`

|

|
Log paths used during the `moduleResolution` process.

 |

 | ` --tsBuildInfoFile `
 | `string`

 | `.tsbuildinfo`

|

|
The file to store `.tsbuildinfo` incremental build information in.

 |

 | ` --typeRoots `
 | `list`

 |
|

|
Specify multiple folders that act like `./node_modules/@types`.

 |

 | ` --types `
 | `list`

 |
|

|
Specify type package names to be included without being referenced in a source file.

 |

 | ` --useDefineForClassFields `
 | `boolean`

 | `true` if `target` is `ES2022` or higher, including `ESNext`; `false` otherwise.

|

|
Emit ECMAScript-standard-compliant class fields.

 |

 | ` --useUnknownInCatchVariables `
 | `boolean`

 | `true` if `strict` ; `false` otherwise.

|

|
Default catch clause variables as `unknown` instead of `any`.

 |

 | ` --verbatimModuleSyntax `
 | `boolean`

 | `false`

|

|
Do not transform or elide any imports or exports not marked as type-only, ensuring they are written in the output file's format based on the 'module' setting.

 |

## Related

- Every option is fully explained in the TSConfig Reference .

- Learn how to use a `tsconfig.json` file.

- Learn how to work in an MSBuild project .

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: MH OT DR AD JB 65+ Last updated: Jun 15, 2026

## Project References

Was this page helpful?

# Project References
 Project references allows you to structure your TypeScript programs into smaller pieces, available in TypeScript 3.0 and newer.

By doing this, you can greatly improve build times, enforce logical separation between components, and organize your code in new and better ways.

We’re also introducing a new mode for `tsc`, the `--build` flag, that works hand in hand with project references to enable faster TypeScript builds.

## An Example Project

 Let’s look at a fairly normal program and see how project references can help us better organize it.
Imagine you have a project with two modules, `converter` and `units`, and a corresponding test file for each:

 ` / ├── src/ │ ├── converter.ts │ └── units.ts ├── test/ │ ├── converter-tests.ts │ └── units-tests.ts └── tsconfig.json `
 The test files import the implementation files and do some testing:

 ts ` // converter-tests.ts import * as converter from "../src/converter" ; assert . areEqual ( converter . celsiusToFahrenheit ( 0 ), 32 ); `
 Previously, this structure was rather awkward to work with if you used a single tsconfig file:

- It was possible for the implementation files to import the test files

- It wasn’t possible to build `test` and `src` at the same time without having `src` appear in the output folder name, which you probably don’t want

- Changing just the internals in the implementation files required typechecking the tests again, even though this wouldn’t ever cause new errors

- Changing just the tests required typechecking the implementation again, even if nothing changed

You could use multiple tsconfig files to solve some of those problems, but new ones would appear:

- There’s no built-in up-to-date checking, so you end up always running `tsc` twice

- Invoking `tsc` twice incurs more startup time overhead

- `tsc -w` can’t run on multiple config files at once

Project references can solve all of these problems and more.

## What is a Project Reference?

 `tsconfig.json` files have a new top-level property, `references` . It’s an array of objects that specifies projects to reference:

 js ` { "compilerOptions" : { // The usual }, "references" : [ { "path" : "../src" } ] } `
 The `path` property of each reference can point to a directory containing a `tsconfig.json` file, or to the config file itself (which may have any name).

When you reference a project, new things happen:

- Importing modules from a referenced project will instead load its output declaration file (`.d.ts`)

- If the referenced project produces an `outFile` , the output file `.d.ts` file’s declarations will be visible in this project

- Build mode (see below) will automatically build the referenced project if needed

By separating into multiple projects, you can greatly improve the speed of typechecking and compiling, reduce memory usage when using an editor, and improve enforcement of the logical groupings of your program.

## `composite`

 Referenced projects must have the new `composite` setting enabled.
This setting is needed to ensure TypeScript can quickly determine where to find the outputs of the referenced project.
Enabling the `composite` flag changes a few things:

- The `rootDir` setting, if not explicitly set, defaults to the directory containing the `tsconfig` file

- All implementation files must be matched by an `include` pattern or listed in the `files` array. If this constraint is violated, `tsc` will inform you which files weren’t specified

- `declaration` must be turned on

## `declarationMap`

 We’ve also added support for declaration source maps .
If you enable `declarationMap` , you’ll be able to use editor features like “Go to Definition” and Rename to transparently navigate and edit code across project boundaries in supported editors.

## Caveats for Project References

 Project references have a few trade-offs you should be aware of.

Because dependent projects make use of `.d.ts` files that are built from their dependencies, you’ll either have to check in certain build outputs or build a project after cloning it before you can navigate the project in an editor without seeing spurious errors.

When using VS Code (since TS 3.7) we have a behind-the-scenes in-memory `.d.ts` generation process that should be able to mitigate this, but it has some perf implications. For very large composite projects you might want to disable this using disableSourceOfProjectReferenceRedirect option .

Additionally, to preserve compatibility with existing build workflows, `tsc` will not automatically build dependencies unless invoked with the `--build` switch.
Let’s learn more about `--build`.

## Build Mode for TypeScript

 A long-awaited feature is smart incremental builds for TypeScript projects.
In 3.0 you can use the `--build` flag with `tsc`.
This is effectively a new entry point for `tsc` that behaves more like a build orchestrator than a simple compiler.

Running `tsc --build` (`tsc -b` for short) will do the following:

- Find all referenced projects

- Detect if they are up-to-date

- Build out-of-date projects in the correct order

You can provide `tsc -b` with multiple config file paths (e.g. `tsc -b src test`).
Just like `tsc -p`, specifying the config file name itself is unnecessary if it’s named `tsconfig.json`.

### `tsc -b` Commandline

 You can specify any number of config files:

 shell ` > tsc -b # Use the tsconfig.json in the current directory > tsc -b src # Use src/tsconfig.json > tsc -b foo/prd.tsconfig.json bar # Use foo/prd.tsconfig.json and bar/tsconfig.json `
 Don’t worry about ordering the files you pass on the commandline - `tsc` will re-order them if needed so that dependencies are always built first.

There are also some flags specific to `tsc -b`:

- `--verbose` : Prints out verbose logging to explain what’s going on (may be combined with any other flag)

- `--dry`: Shows what would be done but doesn’t actually build anything

- `--clean`: Deletes the outputs of the specified projects (may be combined with `--dry`)

- `--force` : Act as if all projects are out of date

- `--watch`: Watch mode (may not be combined with any flag except `--verbose` )

## Caveats

 Normally, `tsc` will produce outputs (`.js` and `.d.ts`) in the presence of syntax or type errors, unless `noEmitOnError` is on.
Doing this in an incremental build system would be very bad - if one of your out-of-date dependencies had a new error, you’d only see it once because a subsequent build would skip building the now up-to-date project.
For this reason, `tsc -b` effectively acts as if `noEmitOnError` is enabled for all projects.

If you check in any build outputs (`.js`, `.d.ts`, `.d.ts.map`, etc.), you may need to run a `--force` build after certain source control operations depending on whether your source control tool preserves timestamps between the local copy and the remote copy.

## MSBuild

 If you have an msbuild project, you can enable build mode by adding

 xml ` <TypeScriptBuildMode> true </TypeScriptBuildMode> `
 to your proj file. This will enable automatic incremental build as well as cleaning.

Note that as with `tsconfig.json` / `-p`, existing TypeScript project properties will not be respected - all settings should be managed using your tsconfig file.

Some teams have set up msbuild-based workflows wherein tsconfig files have the same implicit graph ordering as the managed projects they are paired with.
If your solution is like this, you can continue to use `msbuild` with `tsc -p` along with project references; these are fully interoperable.

## Guidance

### Overall Structure

 With more `tsconfig.json` files, you’ll usually want to use Configuration file inheritance to centralize your common compiler options.
This way you can change a setting in one file rather than having to edit multiple files.

Another good practice is to have a “solution” `tsconfig.json` file that simply has `references` to all of your leaf-node projects and sets `files` to an empty array (otherwise the solution file will cause double compilation of files). Note that starting with 3.0, it is no longer an error to have an empty `files` array if you have at least one `reference` in a `tsconfig.json` file.

This presents a simple entry point; e.g. in the TypeScript repo we simply run `tsc -b src` to build all endpoints because we list all the subprojects in `src/tsconfig.json`

You can see these patterns in the TypeScript repo - see `src/tsconfig-base.json`, `src/tsconfig.json`, and `src/tsc/tsconfig.json` as key examples.

### Structuring for relative modules

 In general, not much is needed to transition a repo using relative modules.
Simply place a `tsconfig.json` file in each subdirectory of a given parent folder, and add `reference`s to these config files to match the intended layering of the program.
You will need to either set the `outDir` to an explicit subfolder of the output folder, or set the `rootDir` to the common root of all project folders.

### Structuring for outFiles

 Layout for compilations using `outFile` is more flexible because relative paths don’t matter as much.
The TypeScript repo itself is a good reference here - we have some “library” projects and some “endpoint” projects; “endpoint” projects are kept as small as possible and pull in only the libraries they need.

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: MH OT RC T MK 23+ Last updated: Jun 15, 2026

## Integrating With Build Tools

Was this page helpful?

# Integrating with Build Tools

## Babel

### Install

```
 sh ` npm install @babel/cli @babel/core @babel/preset-typescript --save-dev `
```

### .babelrc

```
 js ` { "presets" : [ "@babel/preset-typescript" ] } `
```

### Using Command Line Interface

```
 sh ` ./node_modules/.bin/babel --out-file bundle.js src/index.ts `
```

### package.json

```
 js ` { "scripts" : { "build" : "babel --out-file bundle.js main.ts" }, } `
```

### Execute Babel from the command line

```
 sh ` npm run build `
```

## Browserify

### Install

```
 sh ` npm install tsify `
```

### Using Command Line Interface

```
 sh ` browserify main.ts -p [ tsify --noImplicitAny ] > bundle.js `
```

### Using API

```
 js ` var browserify = require ( "browserify" ); var tsify = require ( "tsify" ); browserify () . add ( "main.ts" ) . plugin ( "tsify" , { noImplicitAny: true }) . bundle () . pipe ( process . stdout ); `
```

 More details: smrq/tsify

## Grunt

### Using `grunt-ts` (no longer maintained)

#### Install

```
 sh ` npm install grunt-ts --save-dev `
```

#### Basic Gruntfile.js

```
 js ` module . exports = function ( grunt ) { grunt . initConfig ({ ts: { default: { src: [ "**/*.ts" , "!node_modules/**/*.ts" ], }, }, }); grunt . loadNpmTasks ( "grunt-ts" ); grunt . registerTask ( "default" , [ "ts" ]); }; `
```

 More details: TypeStrong/grunt-ts

### Using `grunt-browserify` combined with `tsify`

#### Install

```
 sh ` npm install grunt-browserify tsify --save-dev `
```

#### Basic Gruntfile.js

```
 js ` module . exports = function ( grunt ) { grunt . initConfig ({ browserify: { all: { src: "src/main.ts" , dest: "dist/main.js" , options: { plugin: [ "tsify" ], }, }, }, }); grunt . loadNpmTasks ( "grunt-browserify" ); grunt . registerTask ( "default" , [ "browserify" ]); }; `
```

 More details: jmreidy/grunt-browserify , TypeStrong/tsify

## Gulp

### Install

```
 sh ` npm install gulp-typescript `
```

### Basic gulpfile.js

```
 js ` var gulp = require ( "gulp" ); var ts = require ( "gulp-typescript" ); gulp . task ( "default" , function () { var tsResult = gulp . src ( "src/*.ts" ). pipe ( ts ({ noImplicitAny: true , out: "output.js" , }) ); return tsResult . js . pipe ( gulp . dest ( "built/local" )); }); `
```

 More details: ivogabe/gulp-typescript

## Jspm

### Install

```
 sh ` npm install -g jspm@beta `
```

 Note: Currently TypeScript support in jspm is in 0.16beta

More details: TypeScriptSamples/jspm

## MSBuild

 Update project file to include locally installed `Microsoft.TypeScript.Default.props` (at the top) and `Microsoft.TypeScript.targets` (at the bottom) files:

 xml ` <?xml version = "1.0" encoding = "utf-8" ?> <Project ToolsVersion = "4.0" DefaultTargets = "Build" xmlns = "http://schemas.microsoft.com/developer/msbuild/2003" > <!-- Include default props at the top --> <Import Project = "$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v$(VisualStudioVersion)\TypeScript\Microsoft.TypeScript.Default.props" Condition = "Exists('$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v$(VisualStudioVersion)\TypeScript\Microsoft.TypeScript.Default.props')" /> <!-- TypeScript configurations go here --> <PropertyGroup Condition = "'$(Configuration)' == 'Debug'" > <TypeScriptRemoveComments> false </TypeScriptRemoveComments> <TypeScriptSourceMap> true </TypeScriptSourceMap> </PropertyGroup> <PropertyGroup Condition = "'$(Configuration)' == 'Release'" > <TypeScriptRemoveComments> true </TypeScriptRemoveComments> <TypeScriptSourceMap> false </TypeScriptSourceMap> </PropertyGroup> <!-- Include default targets at the bottom --> <Import Project = "$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v$(VisualStudioVersion)\TypeScript\Microsoft.TypeScript.targets" Condition = "Exists('$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v$(VisualStudioVersion)\TypeScript\Microsoft.TypeScript.targets')" /> </Project> `
 More details about defining MSBuild compiler options: Setting Compiler Options in MSBuild projects

## NuGet

- Right-Click -> Manage NuGet Packages

- Search for `Microsoft.TypeScript.MSBuild`

- Hit `Install`

- When install is complete, rebuild!

 More details can be found at Package Manager Dialog and using nightly builds with NuGet

## Rollup

### Install

```
 ` npm install @rollup/plugin-typescript --save-dev `
```

 Note that both `typescript` and `tslib` are peer dependencies of this plugin that need to be installed separately.

### Usage

 Create a `rollup.config.js` configuration file and import the plugin:

 js ` // rollup.config.js import typescript from '@rollup/plugin-typescript' ; export default { input: 'src/index.ts' , output: { dir: 'output' , format: 'cjs' }, plugins: [ typescript ()] }; `

## Svelte Compiler

### Install

```
 ` npm install --save-dev svelte-preprocess `
```

 Note that `typescript` is an optional peer dependencies of this plugin and needs to be installed separately. `tslib` is not provided either.

You may also consider `svelte-check` for CLI type checking.

### Usage

 Create a `svelte.config.js` configuration file and import the plugin:

 js ` // svelte.config.js import preprocess from 'svelte-preprocess' ; const config = { // Consult https://github.com/sveltejs/svelte-preprocess // for more information about preprocessors preprocess: preprocess () }; export default config ; `
 You can now specify that script blocks are written in TypeScript:

 ` <script lang="ts"> `

## Vite

 Vite supports importing `.ts` files out-of-the-box. It only performs transpilation and not type checking. It also requires that some `compilerOptions` have certain values. See the Vite docs for more details.

## Webpack

### Install

```
 sh ` npm install ts-loader --save-dev `
```

### Basic webpack.config.js when using Webpack 5 or 4

```
 js ` const path = require ( 'path' ); module . exports = { entry: './src/index.ts' , module: { rules: [ { test: / \. tsx ? $ / , use: 'ts-loader' , exclude: /node_modules/ , }, ], }, resolve: { extensions: [ '.tsx' , '.ts' , '.js' ], }, output: { filename: 'bundle.js' , path: path . resolve ( __dirname , 'dist' ), }, }; `
```

 See more details on ts-loader here .

Alternatives:

- awesome-typescript-loader

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: MH OT MDB RC DR 15+ Last updated: Jun 15, 2026

## Configuring Watch

Was this page helpful?

# Configuring Watch
 As of TypeScript 3.8 and onward, the Typescript compiler exposes configuration which controls how it watches files and directories. Prior to this version, configuration required the use of environment variables which are still available.

## Background

 The `--watch` implementation of the compiler relies on Node’s `fs.watch` and `fs.watchFile`. Each of these methods has pros and cons.

`fs.watch` relies on file system events to broadcast changes in the watched files and directories. The implementation of this command is OS dependent and unreliable - on many operating systems, it does not work as expected. Additionally, some operating systems limit the number of watches which can exist simultaneously (e.g. some flavors of Linux ). Heavy use of `fs.watch` in large codebases has the potential to exceed these limits and result in undesirable behavior. However, because this implementation relies on an events-based model, CPU use is comparatively light. The compiler typically uses `fs.watch` to watch directories (e.g. source directories included by compiler configuration files and directories in which module resolution failed, among others). TypeScript uses these to augment potential failures in individual file watchers. However, there is a key limitation of this strategy: recursive watching of directories is supported on Windows and macOS, but not on Linux. This suggested a need for additional strategies for file and directory watching.

`fs.watchFile` uses polling and thus costs CPU cycles. However, `fs.watchFile` is by far the most reliable mechanism available to subscribe to the events from files and directories of interest. Under this strategy, the TypeScript compiler typically uses `fs.watchFile` to watch source files, config files, and files which appear missing based on reference statements. This means that the degree to which CPU usage will be higher when using `fs.watchFile` depends directly on number of files watched in the codebase.

## Configuring file watching using a `tsconfig.json`

 The suggested method of configuring watch behavior is through the new `watchOptions` section of `tsconfig.json`. We provide an example configuration below. See the following section for detailed descriptions of the settings available.

 ` { // Some typical compiler options " compilerOptions " : { " target " : "es2020" , " moduleResolution " : "node" // ... }, // NEW: Options for file/directory watching "watchOptions" : { // Use native file system events for files and directories " watchFile " : "useFsEvents" , " watchDirectory " : "useFsEvents" , // Poll files for updates more frequently // when they're updated a lot. " fallbackPolling " : "dynamicPriority" , // Don't coalesce watch notification " synchronousWatchDirectory " : true , // Finally, two additional settings for reducing the amount of possible // files to track work from these directories " excludeDirectories " : [ "**/node_modules" , "_build" ], " excludeFiles " : [ "build/fileWhichChangesOften.ts" ] } } `
 For further details, see the release notes for Typescript 3.8 .

## Configuring file watching using environment variable `TSC_WATCHFILE`

| **

 Option**
| **Description**
|

| `PriorityPollingInterval`
| Use `fs.watchFile`, but use different polling intervals for source files, config files and missing files
|

| `DynamicPriorityPolling`
| Use a dynamic queue where frequently modified files are polled at shorter intervals, and unchanged files are polled less frequently
|

| `UseFsEvents`
| Use `fs.watch`. On operating systems that limit the number of active watches, fall back to `fs.watchFile` when a watcher fails to be created.
|

| `UseFsEventsWithFallbackDynamicPolling`
| Use `fs.watch`. On operating systems that limit the number of active watches, fall back to dynamic polling queues (as explained in `DynamicPriorityPolling`)
|

| `UseFsEventsOnParentDirectory`
| Use `fs.watch` on the parent directories of included files (yielding a compromise that results in lower CPU usage than pure `fs.watchFile` but potentially lower accuracy).
|

| default (no value specified)
| If environment variable `TSC_NONPOLLING_WATCHER` is set to true, use `UseFsEventsOnParentDirectory`. Otherwise, watch files using `fs.watchFile` with `250ms` as the timeout for any file.
|

## Configuring directory watching using environment variable `TSC_WATCHDIRECTORY`

 For directory watches on platforms which don’t natively allow recursive directory watching (i.e. non macOS and Windows operating systems) is supported through recursively creating directory watchers for each child directory using different options selected by `TSC_WATCHDIRECTORY`.

 NOTE: On platforms which support native recursive directory watching, the value of `TSC_WATCHDIRECTORY` is ignored.

| **

 Option**
| **Description**
|

| `RecursiveDirectoryUsingFsWatchFile`
| Use `fs.watchFile` to watch included directories and child directories.
|

| `RecursiveDirectoryUsingDynamicPriorityPolling`
| Use a dynamic polling queue to poll changes to included directories and child directories.
|

| default (no value specified)
| Use `fs.watch` to watch included directories and child directories.
|

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: SN OT BS JM IO 8+ Last updated: Jun 15, 2026

## Nightly Builds

Was this page helpful?

# Nightly Builds
 A nightly build from the TypeScript’s `main` branch is published by midnight PST to npm.
Here is how you can get it and use it with your tools.

## Using npm

```
 shell ` npm install -D typescript@next `
```

## Updating your IDE to use the nightly builds

 You can also update your editor/IDE to use the nightly drop.
You will typically need to install the package through npm.
The rest of this section mostly assumes `typescript@next` is already installed.

### Visual Studio Code

 The VS Code website has documentation on selecting a workspace version of TypeScript .
After installing a nightly version of TypeScript in your workspace, you can follow directions there, or simply update your workspace settings in the JSON view.
A direct way to do this is to open or create your workspace’s `.vscode/settings.json` and add the following property:

 json ` "typescript.tsdk" : "<path to your folder>/node_modules/typescript/lib" `
 Alternatively, if you simply want to run the nightly editing experience for JavaScript and TypeScript in Visual Studio Code without changing your workspace version, you can run the JavaScript and TypeScript Nightly Extension

### Sublime Text

 Update the `Settings - User` file with the following:

 json ` "typescript_tsdk" : "<path to your folder>/node_modules/typescript/lib" `
 More information is available at the TypeScript Plugin for Sublime Text installation documentation .

### Visual Studio 2013 and 2015

 Note: Most changes do not require you to install a new version of the VS TypeScript plugin.

The nightly build currently does not include the full plugin setup, but we are working on publishing an installer on a nightly basis as well.

-
Download the VSDevMode.ps1 script.

Also see our wiki page on using a custom language service file .

-
From a PowerShell command window, run:

For VS 2015:

 `VSDevMode.ps1 14 -tsScript <path to your folder>/node_modules/typescript/lib`
 For VS 2013:

 `VSDevMode.ps1 12 -tsScript <path to your folder>/node_modules/typescript/lib`

### IntelliJ IDEA (Mac)

 Go to `Preferences` > `Languages &#x26; Frameworks` > `TypeScript`:

TypeScript Version: If you installed with npm: `/usr/local/lib/node_modules/typescript/lib`

### IntelliJ IDEA (Windows)

 Go to `File` > `Settings` > `Languages &#x26; Frameworks` > `TypeScript`:

TypeScript Version: If you installed with npm: `C:\Users\USERNAME\AppData\Roaming\npm\node_modules\typescript\lib`

 The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤
 Contributors to this page: MH OT S DR NS 4+ Last updated: Jun 15, 2026