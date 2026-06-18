# Nuxt - API - Kit


## Modules

# Modules

> Nuxt Kit provides a set of utilities to help you create and use modules. You can use these utilities to create your own modules or to reuse existing modules.

Modules are the building blocks of Nuxt. Kit provides a set of utilities to help you create and use modules. You can use these utilities to create your own modules or to reuse existing modules. For example, you can use the `defineNuxtModule` function to define a module and specify dependencies using the `moduleDependencies` option.

## `defineNuxtModule`

Define a Nuxt module, automatically merging defaults with user provided options, installing any hooks that are provided, and calling an optional setup function for full control.

### Usage

```tstwoslash
import { defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'my-module',
    configKey: 'myModule',
  },
  defaults: {
    enabled: true,
  },
  setup (options) {
    if (options.enabled) {
      console.log('My Nuxt module is enabled!')
    }
  },
})
```

### Type

```tstwoslash
// @errors: 2391
import type { ModuleDefinition, ModuleOptions, NuxtModule } from '@nuxt/schema'
// ---cut---
export function defineNuxtModule<TOptions extends ModuleOptions> (
  definition?: ModuleDefinition<TOptions, Partial<TOptions>, false> | NuxtModule<TOptions, Partial<TOptions>, false>,
): NuxtModule<TOptions, TOptions, false>

export function defineNuxtModule<TOptions extends ModuleOptions> (): {
  with: <TOptionsDefaults extends Partial<TOptions>> (
    definition: ModuleDefinition<TOptions, TOptionsDefaults, true> | NuxtModule<TOptions, TOptionsDefaults, true>,
  ) => NuxtModule<TOptions, TOptionsDefaults, true>
}
```

### Parameters

**definition**: A module definition object or a module function. The module definition object should contain the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        meta
      </code>
    </td>
    
    <td>
      <code>
        ModuleMeta
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Metadata of the module. It defines the module name, version, config key and compatibility.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        defaults
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          T
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sZSNi">
          (
        </span>
        
        <span class="sDfIl">
          (
        </span>
        
        <span class="s1nJG">
          nuxt
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          Nuxt
        </span>
        
        <span class="sDfIl">
          )
        </span>
        
        <span class="smZ93">
          =>
        </span>
        
        <span class="sZSNi">
          T)
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Default options for the module. If a function is provided, it will be called with the Nuxt instance as the first argument.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        schema
      </code>
    </td>
    
    <td>
      <code>
        T
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Schema for the module options. If provided, options will be applied to the schema.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        hooks
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          Partial
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          NuxtHooks
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Hooks to be installed for the module. If provided, the module will install the hooks.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        moduleDependencies
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          Record
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          ,
        </span>
        
        <span class="sZSNi">
          ModuleDependency
        </span>
        
        <span class="sDfIl">
          >
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sZSNi">
          (
        </span>
        
        <span class="sDfIl">
          (
        </span>
        
        <span class="s1nJG">
          nuxt
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          Nuxt
        </span>
        
        <span class="sDfIl">
          )
        </span>
        
        <span class="smZ93">
          =>
        </span>
        
        <span class="sZSNi">
          Record
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          ,
        </span>
        
        <span class="sZSNi">
          ModuleDependency
        </span>
        
        <span class="sDfIl">
          >
        </span>
        
        <span class="sZSNi">
          )
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Dependencies on other modules with version constraints and configuration. Can be an object or a function that receives the Nuxt instance. See <a href="/docs/4.x/api/kit/modules#specifying-module-dependencies">
        example
      </a>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        onInstall
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          (
        </span>
        
        <span class="s1nJG">
          nuxt
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          Nuxt
        </span>
        
        <span class="sDfIl">
          )
        </span>
        
        <span class="smZ93">
          =>
        </span>
        
        <span class="sZSNi">
          Awaitable
        </span>
        
        <span class="sDfIl">
          <void>
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Lifecycle hook called when the module is first installed. Requires <code>
        meta.name
      </code>
      
       and <code>
        meta.version
      </code>
      
       to be defined.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        onUpgrade
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          (
        </span>
        
        <span class="s1nJG">
          nuxt
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          Nuxt
        </span>
        
        <span class="sDfIl">
          ,
        </span>
        
        <span class="s1nJG">
          options
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          T
        </span>
        
        <span class="sDfIl">
          ,
        </span>
        
        <span class="s1nJG">
          previousVersion
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          string
        </span>
        
        <span class="sDfIl">
          )
        </span>
        
        <span class="smZ93">
          =>
        </span>
        
        <span class="sZSNi">
          Awaitable
        </span>
        
        <span class="sDfIl">
          <void>
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Lifecycle hook called when the module is upgraded to a newer version. Requires <code>
        meta.name
      </code>
      
       and <code>
        meta.version
      </code>
      
       to be defined.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setup
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          (
        </span>
        
        <span class="s8R28">
          this
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          void
        </span>
        
        <span class="sDfIl">
          ,
        </span>
        
        <span class="s1nJG">
          resolvedOptions
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          T
        </span>
        
        <span class="sDfIl">
          ,
        </span>
        
        <span class="s1nJG">
          nuxt
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          Nuxt
        </span>
        
        <span class="sDfIl">
          )
        </span>
        
        <span class="smZ93">
          =>
        </span>
        
        <span class="sZSNi">
          Awaitable
        </span>
        
        <span class="sDfIl">
          <void
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sbKd-">
          false
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sZSNi">
          ModuleSetupInstallResult
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Setup function for the module. If provided, the module will call the setup function.
    </td>
  </tr>
</tbody>
</table>

### Examples

#### Using `configKey` to Make Your Module Configurable

When defining a Nuxt module, you can set a `configKey` to specify how users should configure the module in their `nuxt.config`.

```ts
import { defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'my-module',
    configKey: 'myModule',
  },
  defaults: {
    // Module options
    enabled: true,
  },
  setup (options) {
    if (options.enabled) {
      console.log('My Nuxt module is enabled!')
    }
  },
})
```

Users can provide options for this module under the corresponding key in `nuxt.config`.

```ts
export default defineNuxtConfig({
  myModule: {
    enabled: false,
  },
})
```

Users can also completely disable a module by setting the config key to `false`. This prevents the module's setup function from running while still generating types for module options.

```ts
export default defineNuxtConfig({
  // Disable the module entirely
  myModule: false,
})
```

<tip>

This is particularly useful when you want to disable modules inherited from [Nuxt layers](/docs/4.x/guide/going-further/layers#disabling-modules-from-layers).

</tip>

#### Defining Module Compatibility Requirements

If you're developing a Nuxt module and using APIs that are only supported in specific Nuxt versions, it's highly recommended to include `compatibility.nuxt`.

```ts
export default defineNuxtModule({
  meta: {
    name: '@nuxt/icon',
    configKey: 'icon',
    compatibility: {
      // Required nuxt version in semver format.
      nuxt: '>=3.0.0', // or use '^3.0.0'
    },
  },
  setup () {
    const resolver = createResolver(import.meta.url)
    // Implement
  },
})
```

If the user tries to use your module with an incompatible Nuxt version, they will receive a warning in the console.

```terminal
WARN  Module @nuxt/icon is disabled due to incompatibility issues:
 - [nuxt] Nuxt version ^3.1.0 is required but currently using 3.0.0
```

#### Type Safety for Resolved Options with `.with()`

When you need type safety for your resolved/merged module options, you can use the `.with()` method. This enables TypeScript to properly infer the relationship between your module's defaults and the final resolved options that your setup function receives.

```ts
import { defineNuxtModule } from '@nuxt/kit'

// Define your module options interface
interface ModuleOptions {
  apiKey: string
  baseURL: string
  timeout?: number
  retries?: number
}

export default defineNuxtModule<ModuleOptions>().with({
  meta: {
    name: '@nuxtjs/my-api',
    configKey: 'myApi',
  },
  defaults: {
    baseURL: 'https://api.example.com',
    timeout: 5000,
    retries: 3,
  },
  setup (resolvedOptions, nuxt) {
    // resolvedOptions is properly typed as:
    // {
    //   apiKey: string          // Required, no default provided
    //   baseURL: string         // Required, has default value
    //   timeout: number         // Optional, has default value
    //   retries: number         // Optional, has default value
    // }

    console.log(resolvedOptions.baseURL) // ✅ TypeScript knows this is always defined
    console.log(resolvedOptions.timeout) // ✅ TypeScript knows this is always defined
    console.log(resolvedOptions.retries) // ✅ TypeScript knows this is always defined
  },
})
```

Without using `.with()`, the `resolvedOptions` parameter would be typed as the raw `ModuleOptions` interface, where `timeout` and `retries` could be `undefined` even when defaults are provided. The `.with()` method enables TypeScript to understand that default values make those properties non-optional in the resolved options.

#### Using Lifecycle Hooks for Module Installation and Upgrade

You can define lifecycle hooks that run when your module is first installed or upgraded to a new version. These hooks are useful for performing one-time setup tasks, database migrations, or cleanup operations.

<important>

For lifecycle hooks to work, you **must** provide both `meta.name` and `meta.version` in your module definition. The hooks use these values to track the module's installation state in the project's `.nuxtrc` file.

</important>

Lifecycle hooks run before the main `setup` function, and if a hook throws an error, it's logged but doesn't stop the build process.

**onInstall** runs only once when the module is first added to a project.

**onUpgrade** runs each time the module version increases (using semver comparison) — but only once for each version bump.

##### Example

```ts
import { defineNuxtModule } from '@nuxt/kit'
import semver from 'semver'

export default defineNuxtModule({
  meta: {
    name: 'my-awesome-module',
    version: '1.2.0', // Required for lifecycle hooks
    configKey: 'myAwesomeModule',
  },
  defaults: {
    apiKey: '',
    enabled: true,
  },

  onInstall (nuxt) {
    // This runs only when the module is first installed
    console.log('Setting up my-awesome-module for the first time!')

    // You might want to:
    // - Create initial configuration files
    // - Set up database schemas
    // - Display welcome messages
    // - Perform initial data migration
  },

  onUpgrade (nuxt, options, previousVersion) {
    // This runs when the module is upgraded to a newer version
    console.log(`Upgrading my-awesome-module from ${previousVersion} to 1.2.0`)

    // You might want to:
    // - Migrate configuration files
    // - Update database schemas
    // - Clean up deprecated files
    // - Display upgrade notes

    if (semver.lt(previousVersion, '1.1.0')) {
      console.log('⚠️  Breaking changes in 1.1.0 - please check the migration guide')
    }
  },

  setup (options, nuxt) {
    // Regular setup logic runs on every build
    if (options.enabled) {
      // Configure the module
    }
  },
})
```

#### Specifying Module Dependencies

You can use the `moduleDependencies` option to declare dependencies on other modules. This provides a robust way to ensure proper setup order, version compatibility, and configuration management.

The `moduleDependencies` option can be either an object or a function that receives the Nuxt instance:

##### Example

```ts
import { defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'my-module',
  },
  moduleDependencies: {
    '@nuxtjs/tailwindcss': {
      // Specify a version constraint (semver format)
      version: '>=6.0.0',
      // Configuration that overrides user settings
      overrides: {
        exposeConfig: true,
      },
      // Configuration that sets defaults but respects user settings
      defaults: {
        config: {
          darkMode: 'class',
        },
      },
    },
    '@nuxtjs/fontaine': {
      // Optional dependencies won't be installed but ensure that options
      // can be set if they _are_ installed
      optional: true,
      defaults: {
        fonts: [
          {
            family: 'Roboto',
            fallbacks: ['Impact'],
          },
        ],
      },
    },
  },
  setup (options, nuxt) {

  },
})
```

You can also use a function to dynamically determine dependencies based on the Nuxt configuration:

```ts
import { defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'my-module',
  },
  moduleDependencies (nuxt) {
    const dependencies: Record<string, any> = {
      '@nuxtjs/tailwindcss': {
        version: '>=6.0.0',
      },
    }

    // Conditionally add dependencies based on Nuxt config
    if (nuxt.options.experimental?.someFeature) {
      dependencies['@nuxtjs/fontaine'] = {
        optional: true,
      }
    }

    return dependencies
  },
  setup (options, nuxt) {
    // Your setup logic runs after all dependencies are initialized
  },
})
```

## `installModule`

<callout type="warning">

**Deprecated:** Use the [`moduleDependencies`](/docs/4.x/api/kit/modules#specifying-module-dependencies) option in `defineNuxtModule` instead. The `installModule` function will be removed (or may become non-blocking) in a future version.

</callout>

Install specified Nuxt module programmatically. This is helpful when your module depends on other modules. You can pass the module options as an object to `inlineOptions` and they will be passed to the module's `setup` function.

### Usage

```tstwoslash
import { defineNuxtModule, installModule } from '@nuxt/kit'

export default defineNuxtModule({
  async setup () {
    // will install @nuxtjs/fontaine with Roboto font and Impact fallback
    await installModule('@nuxtjs/fontaine', {
      // module configuration
      fonts: [
        {
          family: 'Roboto',
          fallbacks: ['Impact'],
          fallbackName: 'fallback-a',
        },
      ],
    })
  },
})
```

### Type

```ts
async function installModule (moduleToInstall: string | NuxtModule, inlineOptions?: any, nuxt?: Nuxt)
```

### Parameters

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        moduleToInstall
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sZSNi">
          NuxtModule
        </span>
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      The module to install. Can be either a string with the module name or a module object itself.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        inlineOptions
      </code>
    </td>
    
    <td>
      <code>
        any
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      An object with the module options to be passed to the module's <code>
        setup
      </code>
      
       function.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        nuxt
      </code>
    </td>
    
    <td>
      <code>
        Nuxt
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Nuxt instance. If not provided, it will be retrieved from the context via <code>
        useNuxt()
      </code>
      
       call.
    </td>
  </tr>
</tbody>
</table>

### Examples

```ts
import { defineNuxtModule, installModule } from '@nuxt/kit'

export default defineNuxtModule({
  async setup (options, nuxt) {
    // will install @nuxtjs/fontaine with Roboto font and Impact fallback
    await installModule('@nuxtjs/fontaine', {
      // module configuration
      fonts: [
        {
          family: 'Roboto',
          fallbacks: ['Impact'],
          fallbackName: 'fallback-a',
        },
      ],
    })
  },
})
```

<style>

html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}

</style>

---

- [Source](https://github.com/nuxt/nuxt/tree/main/packages/kit/src/module)

## Runtime Config

# Runtime Config

> Nuxt Kit provides a set of utilities to help you access and modify Nuxt runtime configuration.

## `useRuntimeConfig`

At build-time, it is possible to access the resolved Nuxt [runtime config](/docs/4.x/guide/going-further/runtime-config).

### Type

```ts
function useRuntimeConfig (): Record<string, unknown>
```

## `updateRuntimeConfig`

It is also possible to update runtime configuration. This will be merged with the existing runtime configuration, and if Nitro has already been initialized it will trigger an HMR event to reload the Nitro runtime config.

### Type

```ts
function updateRuntimeConfig (config: Record<string, unknown>): void | Promise<void>
```

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/runtime-config.ts)

## Templates

# Templates

> Nuxt Kit provides a set of utilities to help you work with templates. These functions allow you to generate extra files during development and build time.

Templates allow you to generate extra files during development and build time. These files will be available in virtual filesystem and can be used in plugins, layouts, components, etc. `addTemplate` and `addTypeTemplate` allow you to add templates to the Nuxt application. `updateTemplates` allows you to regenerate templates that match the filter.

## `addTemplate`

Renders given template during build into the virtual file system, and optionally to disk in the project `buildDir`

### Usage

```tstwoslash
import { addTemplate, defineNuxtModule } from '@nuxt/kit'
import { defu } from 'defu'

export default defineNuxtModule({
  setup (options, nuxt) {
    const globalMeta = defu(nuxt.options.app.head, {
      charset: options.charset,
      viewport: options.viewport,
    })

    addTemplate({
      filename: 'meta.config.mjs',
      getContents: () => 'export default ' + JSON.stringify({ globalMeta, mixinKey: 'setup' }),
    })
  },
})
```

### Type

```tstwoslash
// @errors: 2391
import type { NuxtTemplate, ResolvedNuxtTemplate } from '@nuxt/schema'
// ---cut---
function addTemplate (template: NuxtTemplate | string): ResolvedNuxtTemplate
```

### Parameters

**template**: A template object or a string with the path to the template. If a string is provided, it will be converted to a template object with `src` set to the string value. If a template object is provided, it must have the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        src
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Path to the template. If <code>
        src
      </code>
      
       is not provided, <code>
        getContents
      </code>
      
       must be provided instead.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        filename
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Filename of the template. If <code>
        filename
      </code>
      
       is not provided, it will be generated from the <code>
        src
      </code>
      
       path. In this case, the <code>
        src
      </code>
      
       option is required.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        dst
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Path to the destination file. If <code>
        dst
      </code>
      
       is not provided, it will be generated from the <code>
        filename
      </code>
      
       path and nuxt <code>
        buildDir
      </code>
      
       option.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        options
      </code>
    </td>
    
    <td>
      <code>
        Options
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Options to pass to the template.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        getContents
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          (
        </span>
        
        <span class="s1nJG">
          data
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          Options
        </span>
        
        <span class="sDfIl">
          )
        </span>
        
        <span class="smZ93">
          =>
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="s52Pk">
          Promise
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      A function that will be called with the <code>
        options
      </code>
      
       object. It should return a string or a promise that resolves to a string. If <code>
        src
      </code>
      
       is provided, this function will be ignored.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        write
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the template will be written to the destination file. Otherwise, the template will be used only in virtual filesystem.
    </td>
  </tr>
</tbody>
</table>

### Examples

#### Creating a Virtual File for Runtime Plugin

In this example, we merge an object inside a module and consume the result in a runtime plugin.

```ts [module.ts]twoslash
import { addTemplate, defineNuxtModule } from '@nuxt/kit'
import { defu } from 'defu'

export default defineNuxtModule({
  setup (options, nuxt) {
    const globalMeta = defu(nuxt.options.app.head, {
      charset: options.charset,
      viewport: options.viewport,
    })

    addTemplate({
      filename: 'meta.config.mjs',
      getContents: () => 'export default ' + JSON.stringify({ globalMeta, mixinKey: 'setup' }),
    })
  },
})
```

In the module above, we generate a virtual file named `meta.config.mjs`. In the runtime plugin, we can import it using the `#build` alias:

```ts [runtime/plugin.ts]
import { createHead as createServerHead } from '@unhead/vue/server'
import { createHead as createClientHead } from '@unhead/vue/client'
import { defineNuxtPlugin } from '#imports'
// @ts-expect-error - virtual file
import metaConfig from '#build/meta.config.mjs'

export default defineNuxtPlugin((nuxtApp) => {
  const createHead = import.meta.server ? createServerHead : createClientHead
  const head = createHead()
  head.push(metaConfig.globalMeta)

  nuxtApp.vueApp.use(head)
})
```

## `addTypeTemplate`

Renders given template during build into the project buildDir, then registers it as types.

### Usage

```tstwoslash
import { addTypeTemplate, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    addTypeTemplate({
      filename: 'types/markdown.d.ts',
      getContents: () => `declare module '*.md' {
  import type { ComponentOptions } from 'vue'
  const Component: ComponentOptions
  export default Component
}`,
    })
  },
})
```

### Type

```ts
function addTypeTemplate (template: NuxtTypeTemplate | string, context?: { nitro?: boolean, nuxt?: boolean }): ResolvedNuxtTemplate
```

### Parameters

**template**: A template object or a string with the path to the template. If a string is provided, it will be converted to a template object with `src` set to the string value. If a template object is provided, it must have the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        src
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Path to the template. If <code>
        src
      </code>
      
       is not provided, <code>
        getContents
      </code>
      
       must be provided instead.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        filename
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Filename of the template. If <code>
        filename
      </code>
      
       is not provided, it will be generated from the <code>
        src
      </code>
      
       path. In this case, the <code>
        src
      </code>
      
       option is required.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        dst
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Path to the destination file. If <code>
        dst
      </code>
      
       is not provided, it will be generated from the <code>
        filename
      </code>
      
       path and nuxt <code>
        buildDir
      </code>
      
       option.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        options
      </code>
    </td>
    
    <td>
      <code>
        Options
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Options to pass to the template.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        getContents
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          (
        </span>
        
        <span class="s1nJG">
          data
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          Options
        </span>
        
        <span class="sDfIl">
          )
        </span>
        
        <span class="smZ93">
          =>
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="s52Pk">
          Promise
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      A function that will be called with the <code>
        options
      </code>
      
       object. It should return a string or a promise that resolves to a string. If <code>
        src
      </code>
      
       is provided, this function will be ignored.
    </td>
  </tr>
</tbody>
</table>

**context**: An optional context object can be passed to control where the type is added. If omitted, the type will only be added to the Nuxt context. This object supports the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        nuxt
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the type will be added to the Nuxt context.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        nitro
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the type will be added to the Nitro context.
    </td>
  </tr>
</tbody>
</table>

### Examples

#### Adding Type Templates to the Nitro Context

By default, －－ only adds the type declarations to the Nuxt context. To also add them to the Nitro context, set nitro to true.

```tstwoslash
import { addTypeTemplate, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    addTypeTemplate({
      filename: 'types/auth.d.ts',
      getContents: () => `declare module '#auth-utils' {
  interface User {
    id: string;
    name: string;
  }

}`,
    }, {
      nitro: true,
    })
  },
})
```

This allows the `#auth-utils` module to be used within the Nitro context.

```ts [server/api/auth.ts]
import type { User } from '#auth-utils'

export default eventHandler(() => {
  const user: User = {
    id: '123',
    name: 'John Doe',
  }

  // do something with the user

  return user
})
```

## `addServerTemplate`

Adds a virtual file that can be used within the Nuxt Nitro server build.

### Usage

```tstwoslash
import { addServerTemplate, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    addServerTemplate({
      filename: '#my-module/test.mjs',
      getContents () {
        return 'export const test = 123'
      },
    })
  },
})
```

### Type

```tstwoslash
// @errors: 2391
import type { NuxtServerTemplate } from '@nuxt/schema'
// ---cut---
function addServerTemplate (template: NuxtServerTemplate): NuxtServerTemplate
```

### Parameters

**template**: A template object. It must have the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        filename
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Filename of the template.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        getContents
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          ()
        </span>
        
        <span class="smZ93">
          =>
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="s52Pk">
          Promise
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      A function that will be called with the <code>
        options
      </code>
      
       object. It should return a string or a promise that resolves to a string.
    </td>
  </tr>
</tbody>
</table>

### Examples

### Creating a Virtual File for Nitro

In this example, we create a virtual file that can be used within the Nuxt Nitro server build.

```tstwoslash
import { addServerTemplate, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    addServerTemplate({
      filename: '#my-module/test.mjs',
      getContents () {
        return 'export const test = 123'
      },
    })
  },
})
```

And then in a runtime file

```ts [server/api/test.ts]
import { test } from '#my-module/test.js'

export default eventHandler(() => {
  return test
})
```

## `updateTemplates`

Regenerate templates that match the filter. If no filter is provided, all templates will be regenerated.

### Usage

```ts
import { defineNuxtModule, updateTemplates } from '@nuxt/kit'
import { resolve } from 'pathe'

export default defineNuxtModule({
  setup (options, nuxt) {
    const updateTemplatePaths = [
      resolve(nuxt.options.srcDir, 'pages'),
    ]
    // watch and rebuild routes template list when one of the pages changes
    nuxt.hook('builder:watch', async (event, relativePath) => {
      if (event === 'change') {
        return
      }

      const path = resolve(nuxt.options.srcDir, relativePath)
      if (updateTemplatePaths.some(dir => path.startsWith(dir))) {
        await updateTemplates({
          filter: template => template.filename === 'routes.mjs',
        })
      }
    })
  },
})
```

### Type

```ts
async function updateTemplates (options: UpdateTemplatesOptions): void
```

### Parameters

**options**: Options to pass to the template. This object can have the following property:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        filter
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          (
        </span>
        
        <span class="s1nJG">
          template
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          ResolvedNuxtTemplate
        </span>
        
        <span class="sDfIl">
          )
        </span>
        
        <span class="smZ93">
          =>
        </span>
        
        <span class="sZSNi">
          boolean
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      A function that will be called with the <code>
        template
      </code>
      
       object. It should return a boolean indicating whether the template should be regenerated. If <code>
        filter
      </code>
      
       is not provided, all templates will be regenerated.
    </td>
  </tr>
</tbody>
</table>

<style>

html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/template.ts)

## Nitro

# Nitro

> Nuxt Kit provides a set of utilities to help you work with Nitro. These functions allow you to add server handlers, plugins, and prerender routes.

Nitro is an open source TypeScript framework to build ultra-fast web servers. Nuxt uses Nitro as its server engine. You can use `useNitro` to access the Nitro instance, `addServerHandler` to add a server handler, `addDevServerHandler` to add a server handler to be used only in development mode, `addServerPlugin` to add a plugin to extend Nitro's runtime behavior, and `addPrerenderRoutes` to add routes to be prerendered by Nitro.

## `addServerHandler`

Adds a Nitro server handler. Use this if you want to create server middleware or a custom route.

### Usage

```tstwoslash
import { addServerHandler, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options) {
    const { resolve } = createResolver(import.meta.url)

    addServerHandler({
      route: '/robots.txt',
      handler: resolve('./runtime/robots.get'),
    })
  },
})
```

### Type

```ts
function addServerHandler (handler: NitroEventHandler): void
```

### Parameters

**handler**: A handler object with the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        handler
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Path to event handler.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        route
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Path prefix or route. If an empty string used, will be used as a middleware.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        middleware
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Specifies this is a middleware handler. Middleware are called on every route and should normally return nothing to pass to the next handlers.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        lazy
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Use lazy loading to import the handler. This is useful when you only want to load the handler on demand.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        method
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Router method matcher. If handler name contains method name, it will be used as a default value.
    </td>
  </tr>
</tbody>
</table>

### Examples

#### Basic Usage

You can use `addServerHandler` to add a server handler from your module.

<code-group>

```ts [module.ts]twoslash
import { addServerHandler, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options) {
    const { resolve } = createResolver(import.meta.url)

    addServerHandler({
      route: '/robots.txt',
      handler: resolve('./runtime/robots.get'),
    })
  },
})
```

```ts [runtime/robots.get.ts]twoslash
export default defineEventHandler(() => {
  return {
    body: `User-agent: *\nDisallow: /`,
  }
})
```

</code-group>

When you access `/robots.txt`, it will return the following response:

```txt
User-agent: *
Disallow: /
```

## `addDevServerHandler`

Adds a Nitro server handler to be used only in development mode. This handler will be excluded from production build.

### Usage

```tstwoslash
import { defineEventHandler } from 'h3'
import { addDevServerHandler, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    addDevServerHandler({
      handler: defineEventHandler(() => {
        return {
          body: `Response generated at ${new Date().toISOString()}`,
        }
      }),
      route: '/_handler',
    })
  },
})
```

### Type

```tstwoslash
// @errors: 2391
import type { NitroDevEventHandler } from 'nitropack/types'
// ---cut---
function addDevServerHandler (handler: NitroDevEventHandler): void
```

### Parameters

**handler**: A handler object with the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        handler
      </code>
    </td>
    
    <td>
      <code>
        EventHandler
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Event handler.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        route
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Path prefix or route. If an empty string used, will be used as a middleware.
    </td>
  </tr>
</tbody>
</table>

### Examples

#### Basic Usage

In some cases, you may want to create a server handler specifically for development purposes, such as a Tailwind config viewer.

```ts
import { joinURL } from 'ufo'
import { addDevServerHandler, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  async setup (options, nuxt) {
    const route = joinURL(nuxt.options.app?.baseURL, '/_tailwind')

    // @ts-expect-error - tailwind-config-viewer does not have correct types
    const createServer = await import('tailwind-config-viewer/server/index.js').then(r => r.default || r) as any
    const viewerDevMiddleware = createServer({ tailwindConfigProvider: () => options, routerPrefix: route }).asMiddleware()

    addDevServerHandler({ route, handler: viewerDevMiddleware })
  },
})
```

## `useNitro`

Returns the Nitro instance.

<warning>

You can call `useNitro()` only after `ready` hook.

</warning>

<note>

Changes to the Nitro instance configuration are not applied.

</note>

### Usage

```ts
import { defineNuxtModule, useNitro } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options, nuxt) {
    const resolver = createResolver(import.meta.url)

    nuxt.hook('ready', () => {
      const nitro = useNitro()
      // Do something with Nitro instance
    })
  },
})
```

### Type

```ts
function useNitro (): Nitro
```

## `addServerPlugin`

Add plugin to extend Nitro's runtime behavior.

<tip>

You can read more about Nitro plugins in the [Nitro documentation](https://nitro.build/guide/plugins).

</tip>

<warning>

It is necessary to explicitly import `defineNitroPlugin` from `nitropack/runtime` within your plugin file. The same requirement applies to utilities such as `useRuntimeConfig`.

</warning>

### Usage

```tstwoslash
import { addServerPlugin, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    const { resolve } = createResolver(import.meta.url)
    addServerPlugin(resolve('./runtime/plugin.ts'))
  },
})
```

### Type

```ts
function addServerPlugin (plugin: string): void
```

### Parameters

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        plugin
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Path to the plugin. The plugin must export a default function that accepts the Nitro instance as an argument.
    </td>
  </tr>
</tbody>
</table>

### Examples

<code-group>

```ts [module.ts]
import { addServerPlugin, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    const { resolve } = createResolver(import.meta.url)
    addServerPlugin(resolve('./runtime/plugin.ts'))
  },
})
```

```ts [runtime/plugin.ts]
export default defineNitroPlugin((nitroApp) => {
  nitroApp.hooks.hook('request', (event) => {
    console.log('on request', event.path)
  })

  nitroApp.hooks.hook('beforeResponse', (event, { body }) => {
    console.log('on response', event.path, { body })
  })

  nitroApp.hooks.hook('afterResponse', (event, { body }) => {
    console.log('on after response', event.path, { body })
  })
})
```

</code-group>

## `addPrerenderRoutes`

Add routes to be prerendered to Nitro.

### Usage

```ts
import { addPrerenderRoutes, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'nuxt-sitemap',
    configKey: 'sitemap',
  },
  defaults: {
    sitemapUrl: '/sitemap.xml',
    prerender: true,
  },
  setup (options) {
    if (options.prerender) {
      addPrerenderRoutes(options.sitemapUrl)
    }
  },
})
```

### Type

```ts
function addPrerenderRoutes (routes: string | string[]): void
```

### Parameters

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        routes
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sZSNi">
          string[]
        </span>
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      A route or an array of routes to prerender.
    </td>
  </tr>
</tbody>
</table>

## `addServerImports`

Add imports to the server. It makes your imports available in Nitro without the need to import them manually.

<warning>

If you want to provide a utility that works in both server and client contexts and is usable in the [`shared/`](/docs/4.x/directory-structure/shared) directory, the function must be imported from the same source file for both [`addImports`](/docs/4.x/api/kit/autoimports#addimports) and `addServerImports` and should have identical signature. That source file should not import anything context-specific (i.e., Nitro context, Nuxt app context) or else it might cause errors during type-checking.

</warning>

### Usage

```tstwoslash
import { addServerImports, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options) {
    const names = [
      'useStoryblok',
      'useStoryblokApi',
      'useStoryblokBridge',
      'renderRichText',
      'RichTextSchema',
    ]

    names.forEach(name =>
      addServerImports({ name, as: name, from: '@storyblok/vue' }),
    )
  },
})
```

### Type

```ts
function addServerImports (dirs: Import | Import[]): void
```

### Parameters

`imports`: An object or an array of objects with the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        name
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Import name to be detected.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        from
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Module specifier to import from.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        priority
      </code>
    </td>
    
    <td>
      <code>
        number
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Priority of the import; if multiple imports have the same name, the one with the highest priority will be used.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        disabled
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If this import is disabled.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        meta
      </code>
    </td>
    
    <td>
      <code>
        Record<string, any>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Metadata of the import.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        type
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If this import is a pure type import.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        typeFrom
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Use this as the <code>
        from
      </code>
      
       value when generating type declarations.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        as
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Import as this name.
    </td>
  </tr>
</tbody>
</table>

## `addServerImportsDir`

Add a directory to be scanned for auto-imports by Nitro.

### Usage

```tstwoslash
import { addServerImportsDir, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'my-module',
    configKey: 'myModule',
  },
  setup (options) {
    const { resolve } = createResolver(import.meta.url)
    addServerImportsDir(resolve('./runtime/server/composables'))
  },
})
```

### Type

```ts
function addServerImportsDir (dirs: string | string[], opts: { prepend?: boolean }): void
```

### Parameters

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        dirs
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sZSNi">
          string[]
        </span>
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      A directory or an array of directories to register to be scanned by Nitro.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        opts
      </code>
    </td>
    
    <td>
      <code>
        { prepend?: boolean }
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Options for the import directory. If <code>
        prepend
      </code>
      
       is <code>
        true
      </code>
      
      , the directory is added to the beginning of the scan list.
    </td>
  </tr>
</tbody>
</table>

### Examples

You can use `addServerImportsDir` to add a directory to be scanned by Nitro. This is useful when you want Nitro to auto-import functions from a custom server directory.

<code-group>

```ts [module.ts]twoslash
import { addServerImportsDir, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'my-module',
    configKey: 'myModule',
  },
  setup (options) {
    const { resolve } = createResolver(import.meta.url)
    addServerImportsDir(resolve('./runtime/server/composables'))
  },
})
```

```ts [runtime/server/composables/index.ts]twoslash
export function useApiSecret () {
  const { apiSecret } = useRuntimeConfig()
  return apiSecret
}
```

</code-group>

You can then use the `useApiSecret` function in your server code:

```ts [runtime/server/api/hello.ts]twoslash
const useApiSecret = (): string => ''
// ---cut---
export default defineEventHandler(() => {
  const apiSecret = useApiSecret()
  // Do something with the apiSecret
})
```

## `addServerScanDir`

Add directories to be scanned by Nitro. It will check for subdirectories, which will be registered
just like the `~~/server` folder is.

<note>

Only `~~/server/api`, `~~/server/routes`, `~~/server/middleware`, and `~~/server/utils` are scanned.

</note>

### Usage

```tstwoslash
import { addServerScanDir, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'my-module',
    configKey: 'myModule',
  },
  setup (options) {
    const { resolve } = createResolver(import.meta.url)
    addServerScanDir(resolve('./runtime/server'))
  },
})
```

### Type

```ts
function addServerScanDir (dirs: string | string[], opts: { prepend?: boolean }): void
```

### Parameters

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        dirs
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sZSNi">
          string[]
        </span>
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      A directory or an array of directories to register to be scanned for by Nitro as server dirs.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        opts
      </code>
    </td>
    
    <td>
      <code>
        { prepend?: boolean }
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Options for the import directory. If <code>
        prepend
      </code>
      
       is <code>
        true
      </code>
      
      , the directory is added to the beginning of the scan list.
    </td>
  </tr>
</tbody>
</table>

### Examples

You can use `addServerScanDir` to add a directory to be scanned by Nitro. This is useful when you want to add a custom server directory.

<code-group>

```ts [module.ts]twoslash
import { addServerScanDir, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'my-module',
    configKey: 'myModule',
  },
  setup (options) {
    const { resolve } = createResolver(import.meta.url)
    addServerScanDir(resolve('./runtime/server'))
  },
})
```

```ts [runtime/server/utils/index.ts]twoslash
export function hello () {
  return 'Hello from server utils!'
}
```

</code-group>

You can then use the `hello` function in your server code.

```ts [runtime/server/api/hello.ts]twoslash
function hello () {
  return 'Hello from server utils!'
}
// ---cut---
export default defineEventHandler(() => {
  return hello() // Hello from server utils!
})
```

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/nitro.ts)

## Resolving

# Resolving

> Nuxt Kit provides a set of utilities to help you resolve paths. These functions allow you to resolve paths relative to the current module, with unknown name or extension.

Sometimes you need to resolve a path relative to the current module without knowing the name or extension. For example, you may want to add a plugin that is located in the same directory as the module. To handle these cases, Nuxt provides a set of utilities to resolve paths. `resolvePath` and `resolveAlias` are used to resolve paths relative to the current module. `findPath` is used to find the first existing file in a given set of paths. `createResolver` is used to create a resolver relative to the base path.

## `resolvePath`

Resolves the full path to a file or directory, respecting Nuxt alias and extensions options. If a path could not be resolved, a normalized input path will be returned.

### Usage

```ts
import { defineNuxtModule, resolvePath } from '@nuxt/kit'

export default defineNuxtModule({
  async setup () {
    const entrypoint = await resolvePath('@unhead/vue')
    console.log(`Unhead entrypoint is ${entrypoint}`)
  },
})
```

### Type

```ts
function resolvePath (path: string, options?: ResolvePathOptions): Promise<string>
```

### Parameters

**path**: A path to resolve.

**options**: Options to pass to the resolver. This object can have the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        cwd
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Base for resolving paths from. Default is Nuxt rootDir.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        alias
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          Record
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          ,
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      An object of aliases. Default is Nuxt configured aliases.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        extensions
      </code>
    </td>
    
    <td>
      <code>
        string[]
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      The file extensions to try. Default is Nuxt configured extensions.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        virtual
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Whether to resolve files that exist in the Nuxt VFS (for example, as a Nuxt template).
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        fallbackToOriginal
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Whether to fallback to the original path if the resolved path does not exist instead of returning the normalized input path.
    </td>
  </tr>
</tbody>
</table>

### Examples

```ts
import { defineNuxtModule, resolvePath } from '@nuxt/kit'
import { join } from 'pathe'

const headlessComponents: ComponentGroup[] = [
  {
    relativePath: 'combobox/combobox.js',
    chunkName: 'headlessui/combobox',
    exports: [
      'Combobox',
      'ComboboxLabel',
      'ComboboxButton',
      'ComboboxInput',
      'ComboboxOptions',
      'ComboboxOption',
    ],
  },
]

export default defineNuxtModule({
  meta: {
    name: 'nuxt-headlessui',
    configKey: 'headlessui',
  },
  defaults: {
    prefix: 'Headless',
  },
  async setup (options) {
    const entrypoint = await resolvePath('@headlessui/vue')
    const root = join(entrypoint, '../components')

    for (const group of headlessComponents) {
      for (const e of group.exports) {
        addComponent(
          {
            name: e,
            export: e,
            filePath: join(root, group.relativePath),
            chunkName: group.chunkName,
            mode: 'all',
          },
        )
      }
    }
  },
})
```

## `resolveAlias`

Resolves path aliases respecting Nuxt alias options.

### Type

```ts
function resolveAlias (path: string, alias?: Record<string, string>): string
```

### Parameters

**path**: A path to resolve.

**alias**: An object of aliases. If not provided, it will be read from `nuxt.options.alias`.

## `findPath`

Try to resolve first existing file in a given set of paths.

### Usage

```ts
import { defineNuxtModule, findPath } from '@nuxt/kit'
import { join } from 'pathe'

export default defineNuxtModule({
  async setup (_, nuxt) {
    // Resolve main (app.vue)
    const mainComponent = await findPath([
      join(nuxt.options.srcDir, 'App'),
      join(nuxt.options.srcDir, 'app'),
    ])
  },
})
```

### Type

```ts
function findPath (paths: string | string[], options?: ResolvePathOptions, pathType: 'file' | 'dir'): Promise<string | null>
```

### Parameters

**paths**: A path or an array of paths to resolve.

**options**: Options to pass to the resolver. This object can have the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        cwd
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Base for resolving paths from. Default is Nuxt rootDir.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        alias
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          Record
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          ,
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      An object of aliases. Default is Nuxt configured aliases.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        extensions
      </code>
    </td>
    
    <td>
      <code>
        string[]
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      The file extensions to try. Default is Nuxt configured extensions.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        virtual
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Whether to resolve files that exist in the Nuxt VFS (for example, as a Nuxt template).
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        fallbackToOriginal
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Whether to fallback to the original path if the resolved path does not exist instead of returning the normalized input path.
    </td>
  </tr>
</tbody>
</table>

## `createResolver`

Creates resolver relative to base path.

<tip icon="i-lucide-video" target="_blank" to="https://vueschool.io/lessons/resolving-paths-and-injecting-assets-to-the-app?friend=nuxt">

Watch Vue School video about createResolver.

</tip>

### Usage

```ts
import { createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup (_, nuxt) {
    const { resolve, resolvePath } = createResolver(import.meta.url)
  },
})
```

### Type

```ts
function createResolver (basePath: string | URL): Resolver
```

### Parameters

**basePath**: A base path to resolve from. It can be a string or a URL.

### Return Value

The `createResolver` function returns an object with the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        resolve
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          (
        </span>
        
        <span class="s1nJG">
          path
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          string
        </span>
        
        <span class="sDfIl">
          )
        </span>
        
        <span class="smZ93">
          =>
        </span>
        
        <span class="sZSNi">
          string
        </span>
      </code>
    </td>
    
    <td>
      A function that resolves a path relative to the base path.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        resolvePath
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          (
        </span>
        
        <span class="s1nJG">
          path
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          string
        </span>
        
        <span class="sDfIl">
          ,
        </span>
        
        <span class="s1nJG">
          options
        </span>
        
        <span class="sDfIl">
          ?:
        </span>
        
        <span class="s52Pk">
          ResolvePathOptions
        </span>
        
        <span class="sDfIl">
          )
        </span>
        
        <span class="smZ93">
          =>
        </span>
        
        <span class="s52Pk">
          Promise
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      A function that resolves a path relative to the base path and respects Nuxt alias and extensions options.
    </td>
  </tr>
</tbody>
</table>

### Examples

```ts
import { createResolver, defineNuxtModule, isNuxt2 } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options, nuxt) {
    const resolver = createResolver(import.meta.url)

    nuxt.hook('modules:done', () => {
      if (isNuxt2()) {
        addPlugin(resolver.resolve('./runtime/plugin.vue2'))
      } else {
        addPlugin(resolver.resolve('./runtime/plugin.vue3'))
      }
    })
  },
})
```

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/resolve.ts)

## Logging

# Logging

> Nuxt Kit provides a set of utilities to help you work with logging. These functions allow you to log messages with extra features.

Nuxt provides a logger instance that you can use to log messages with extra features. `useLogger` allows you to get a logger instance.

## `useLogger`

Returns a logger instance. It uses [consola](https://github.com/unjs/consola) under the hood.

### Usage

```tstwoslash
import { defineNuxtModule, useLogger } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options, nuxt) {
    const logger = useLogger('my-module')

    logger.info('Hello from my module!')
  },
})
```

### Type

```ts
function useLogger (tag?: string, options?: Partial<ConsolaOptions>): ConsolaInstance
```

### Parameters

**tag**: A tag to suffix all log messages with, displayed on the right near the timestamp.

**options**: Consola configuration options.

### Examples

```tstwoslash
import { defineNuxtModule, useLogger } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options, nuxt) {
    const logger = useLogger('my-module', { level: options.quiet ? 0 : 3 })

    logger.info('Hello from my module!')
  },
})
```

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/logger.ts)

## Builder

# Builder

> Nuxt Kit provides a set of utilities to help you work with the builder. These functions allow you to extend the Vite and webpack configurations.

Nuxt have builders based on [Vite](https://github.com/nuxt/nuxt/tree/main/packages/vite) and [webpack](https://github.com/nuxt/nuxt/tree/main/packages/webpack). You can extend the config passed to each one using `extendViteConfig` and `extendWebpackConfig` functions. You can also add additional plugins via `addVitePlugin`, `addWebpackPlugin` and `addBuildPlugin`.

## `extendViteConfig`

Extends the Vite configuration. Callback function can be called multiple times, when applying to both client and server builds.

<warning>

This hook is now deprecated, and we recommend using a Vite plugin instead with a `config` hook, or — for environment-specific configuration — the `applyToEnvironment` hook.

</warning>

### Usage

```tstwoslash
import { defineNuxtModule, extendViteConfig } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    extendViteConfig((config) => {
      config.optimizeDeps ||= {}
      config.optimizeDeps.include ||= []
      config.optimizeDeps.include.push('cross-fetch')
    })
  },
})
```

For environment-specific configuration in Nuxt 5+, use `addVitePlugin()` instead:

```tstwoslash
import { addVitePlugin, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    // For global configuration (affects all environments)
    addVitePlugin(() => ({
      name: 'my-global-plugin',
      config (config) {
        // This runs before environment setup
        config.optimizeDeps ||= {}
        config.optimizeDeps.include ||= []
        config.optimizeDeps.include.push('cross-fetch')
      },
    }))

    // For environment-specific configuration
    addVitePlugin(() => ({
      name: 'my-client-plugin',
      applyToEnvironment (environment) {
        return environment.name === 'client'
      },
      configEnvironment (name, config) {
        // This only affects the client environment
        config.optimizeDeps ||= {}
        config.optimizeDeps.include ||= []
        config.optimizeDeps.include.push('client-only-package')
      },
    }))
  },
})
```

<warning>

**Important:** The `config` hook runs before `applyToEnvironment` and modifies the global configuration. Use `configEnvironment` for environment-specific configuration changes.

</warning>

### Type

```tstwoslash
// @errors: 2391
import type { UserConfig as ViteConfig } from 'vite'
import type { ExtendViteConfigOptions } from '@nuxt/kit'
// ---cut---
function extendViteConfig (callback: ((config: ViteConfig) => void), options?: ExtendViteConfigOptions): void
```

<read-more icon="i-simple-icons-vite" target="_blank" to="https://vite.dev/config/">

Check out the Vite website for more information about its configuration.

</read-more>

### Parameters

**callback**: A callback function that will be called with the Vite configuration object.

**options**: Options to pass to the callback function. This object can have the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        dev
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building in development mode.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        build
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building in production mode.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        server
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building the server bundle. <strong>
        Deprecated in Nuxt 5+.
      </strong>
      
       Use <code>
        addVitePlugin()
      </code>
      
       with <code>
        applyToEnvironment()
      </code>
      
       instead.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        client
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building the client bundle. <strong>
        Deprecated in Nuxt 5+.
      </strong>
      
       Use <code>
        addVitePlugin()
      </code>
      
       with <code>
        applyToEnvironment()
      </code>
      
       instead.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        prepend
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be prepended to the array with <code>
        unshift()
      </code>
      
       instead of <code>
        push()
      </code>
      
      .
    </td>
  </tr>
</tbody>
</table>

## `extendWebpackConfig`

Extends the webpack configuration. Callback function can be called multiple times, when applying to both client and server builds.

### Usage

```tstwoslash
import { defineNuxtModule, extendWebpackConfig } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    extendWebpackConfig((config) => {
      config.module!.rules!.push({
        test: /\.txt$/,
        use: 'raw-loader',
      })
    })
  },
})
```

### Type

```tstwoslash
// @errors: 2391
import type { Configuration as WebpackConfig } from 'webpack'
import type { ExtendWebpackConfigOptions } from '@nuxt/kit'
// ---cut---
function extendWebpackConfig (callback: ((config: WebpackConfig) => void), options?: ExtendWebpackConfigOptions): void
```

<read-more icon="i-simple-icons-webpack" target="_blank" to="https://webpack.js.org/configuration/">

Check out webpack website for more information about its configuration.

</read-more>

### Parameters

**callback**: A callback function that will be called with the webpack configuration object.

**options**: Options to pass to the callback function. This object can have the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        dev
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building in development mode.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        build
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building in production mode.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        server
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building the server bundle.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        client
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building the client bundle.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        prepend
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be prepended to the array with <code>
        unshift()
      </code>
      
       instead of <code>
        push()
      </code>
      
      .
    </td>
  </tr>
</tbody>
</table>

## `addVitePlugin`

Append Vite plugin to the config.

<warning>

In Nuxt 5+, plugins registered with `server: false` or `client: false` options will not have their `config` or `configResolved` hooks called. Instead, use the `applyToEnvironment()` method instead for environment-specific plugins.

</warning>

### Usage

```tstwoslash
// @errors: 2307
// ---cut---
import { addVitePlugin, defineNuxtModule } from '@nuxt/kit'
import { svg4VuePlugin } from 'vite-plugin-svg4vue'

export default defineNuxtModule({
  meta: {
    name: 'nuxt-svg-icons',
    configKey: 'nuxtSvgIcons',
  },
  defaults: {
    svg4vue: {
      assetsDirName: 'assets/icons',
    },
  },
  setup (options) {
    addVitePlugin(svg4VuePlugin(options.svg4vue))

    // or, to add a vite plugin to only one environment
    addVitePlugin(() => ({
      name: 'my-client-plugin',
      applyToEnvironment (environment) {
        return environment.name === 'client'
      },
      // ... rest of your client-only plugin
    }))
  },
})
```

### Type

```tstwoslash
// @errors: 2391
import type { Plugin as VitePlugin } from 'vite'
import type { ExtendViteConfigOptions } from '@nuxt/kit'
// ---cut---
function addVitePlugin (pluginOrGetter: VitePlugin | VitePlugin[] | (() => VitePlugin | VitePlugin[]), options?: ExtendViteConfigOptions): void
```

<tip>

See [Vite website](https://vite.dev/guide/api-plugin) for more information about Vite plugins. You can also use [this repository](https://github.com/vitejs/awesome-vite#plugins) to find a plugin that suits your needs.

</tip>

### Parameters

**pluginOrGetter**: A Vite plugin instance or an array of Vite plugin instances. If a function is provided, it must return a Vite plugin instance or an array of Vite plugin instances. The function can also be async or return a Promise, which is useful for lazy-loading plugins:

```tstwoslash
// @errors: 2307
import { addVitePlugin, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    // Lazy load the plugin - only imported when the build actually runs
    addVitePlugin(() => import('my-vite-plugin').then(r => r.default()))
  },
})
```

**options**: Options to pass to the callback function. This object can have the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        dev
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building in development mode.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        build
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building in production mode.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        server
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building the server bundle. <strong>
        Deprecated in Nuxt 5+.
      </strong>
      
       Use <code>
        applyToEnvironment()
      </code>
      
       instead.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        client
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building the client bundle. <strong>
        Deprecated in Nuxt 5+.
      </strong>
      
       Use <code>
        applyToEnvironment()
      </code>
      
       instead.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        prepend
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be prepended to the array with <code>
        unshift()
      </code>
      
       instead of <code>
        push()
      </code>
      
      .
    </td>
  </tr>
</tbody>
</table>

## `addWebpackPlugin`

Append webpack plugin to the config.

### Usage

```ts
import EslintWebpackPlugin from 'eslint-webpack-plugin'
import { addWebpackPlugin, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'nuxt-eslint',
    configKey: 'eslint',
  },
  defaults: nuxt => ({
    include: [`${nuxt.options.srcDir}/**/*.{js,jsx,ts,tsx,vue}`],
    lintOnStart: true,
  }),
  setup (options, nuxt) {
    const webpackOptions = {
      ...options,
      context: nuxt.options.srcDir,
      files: options.include,
      lintDirtyModulesOnly: !options.lintOnStart,
    }
    addWebpackPlugin(new EslintWebpackPlugin(webpackOptions), { server: false })
  },
})
```

### Type

```tstwoslash
// @errors: 2391
import type { WebpackPluginInstance } from 'webpack'
import type { ExtendWebpackConfigOptions } from '@nuxt/kit'
// ---cut---
function addWebpackPlugin (pluginOrGetter: WebpackPluginInstance | WebpackPluginInstance[] | (() => WebpackPluginInstance | WebpackPluginInstance[]), options?: ExtendWebpackConfigOptions): void
```

<tip>

See [webpack website](https://webpack.js.org/concepts/plugins/) for more information about webpack plugins. You can also use [this collection](https://webpack.js.org/awesome-webpack/#webpack-plugins) to find a plugin that suits your needs.

</tip>

### Parameters

**pluginOrGetter**: A webpack plugin instance or an array of webpack plugin instances. If a function is provided, it must return a webpack plugin instance or an array of webpack plugin instances. The function can also be async or return a Promise, enabling lazy-loading of plugins.

**options**: Options to pass to the callback function. This object can have the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        dev
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building in development mode.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        build
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building in production mode.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        server
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building the server bundle.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        client
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building the client bundle.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        prepend
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be prepended to the array with <code>
        unshift()
      </code>
      
       instead of <code>
        push()
      </code>
      
      .
    </td>
  </tr>
</tbody>
</table>

## `addBuildPlugin`

Builder-agnostic version of `addVitePlugin` and `addWebpackPlugin`. It will add the plugin to both Vite and webpack configurations if they are present.

### Type

```tstwoslash
// @errors: 2391
import type { ExtendConfigOptions } from '@nuxt/kit'
import type { Plugin as VitePlugin } from 'vite'
import type { WebpackPluginInstance } from 'webpack'
import type { RspackPluginInstance } from '@rspack/core'

interface AddBuildPluginFactory {
  vite?: () => VitePlugin | VitePlugin[]
  webpack?: () => WebpackPluginInstance | WebpackPluginInstance[]
  rspack?: () => RspackPluginInstance | RspackPluginInstance[]
}
// ---cut---
function addBuildPlugin (pluginFactory: AddBuildPluginFactory, options?: ExtendConfigOptions): void
```

### Parameters

**pluginFactory**: A factory function that returns an object with `vite` and/or `webpack` properties. These properties must be functions that return a Vite plugin instance or an array of Vite plugin instances and/or a webpack plugin instance or an array of webpack plugin instances.

**options**: Options to pass to the callback function. This object can have the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        dev
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building in development mode.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        build
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building in production mode.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        server
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building the server bundle.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        client
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be called when building the client bundle.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        prepend
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the callback function will be prepended to the array with <code>
        unshift()
      </code>
      
       instead of <code>
        push()
      </code>
      
      .
    </td>
  </tr>
</tbody>
</table>

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/build.ts)

## Layers

# Layers

> Nuxt Kit provides utilities to help you work with layers and their directory structures.

Nuxt layers provide a powerful way to share and extend functionality across projects. When working with layers in modules, you often need to access directory paths from each layer. Nuxt Kit provides the `getLayerDirectories` utility to access resolved directory paths for all layers in your Nuxt application.

## `getLayerDirectories`

Get the resolved directory paths for all layers in a Nuxt application. This function provides a structured way to access layer directories without directly accessing the private `nuxt.options._layers` property.

### Usage

```tstwoslash
import { defineNuxtModule, getLayerDirectories } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    const layerDirs = getLayerDirectories()

    // Access directories from all layers
    for (const [index, layer] of layerDirs.entries()) {
      console.log(`Layer ${index}:`)
      console.log(`  Root: ${layer.root}`)
      console.log(`  App: ${layer.app}`)
      console.log(`  Server: ${layer.server}`)
      console.log(`  Pages: ${layer.appPages}`)
      // ... other directories
    }
  },
})
```

### Type

```tstwoslash
// @errors: 2391
import type { Nuxt } from '@nuxt/schema'
// ---cut---
function getLayerDirectories (nuxt?: Nuxt): LayerDirectories[]

interface LayerDirectories {
  /** Nuxt rootDir (`/` by default) */
  readonly root: string
  /** Nitro source directory (`/server` by default) */
  readonly server: string
  /** Local modules directory (`/modules` by default) */
  readonly modules: string
  /** Shared directory (`/shared` by default) */
  readonly shared: string
  /** Public directory (`/public` by default) */
  readonly public: string
  /** Nuxt srcDir (`/app/` by default) */
  readonly app: string
  /** Layouts directory (`/app/layouts` by default) */
  readonly appLayouts: string
  /** Middleware directory (`/app/middleware` by default) */
  readonly appMiddleware: string
  /** Pages directory (`/app/pages` by default) */
  readonly appPages: string
  /** Plugins directory (`/app/plugins` by default) */
  readonly appPlugins: string
}
```

### Parameters

**nuxt** (optional): The Nuxt instance to get layers from. If not provided, the function will use the current Nuxt context.

### Return Value

The `getLayerDirectories` function returns an array of `LayerDirectories` objects, one for each layer in the application.

**Layer Priority Ordering**: The layers are ordered by priority, where:

- The **first layer** is the user/project layer (highest priority)
- **Earlier layers override later layers** in the array
- **Base layers appear last** in the array (lowest priority)

This ordering matches Nuxt's layer resolution system, where user-defined configurations and files take precedence over those from base layers.

**LayerDirectories**: An object containing the resolved directory paths for a layer.

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        root
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      The root directory of the layer (equivalent to <code>
        rootDir
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        server
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      The server directory for Nitro server-side code
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        modules
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      The local modules directory
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        shared
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      The shared directory for code used by both client and server
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      The source directory of the layer (equivalent to <code>
        srcDir
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        public
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      The public directory for static assets
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        appLayouts
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      The layouts directory for Vue layout components
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        appMiddleware
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      The middleware directory for route middleware
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        appPages
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      The pages directory for file-based routing
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        appPlugins
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      The plugins directory for Nuxt plugins
    </td>
  </tr>
</tbody>
</table>

### Examples

**Processing files from all layers:**

```tstwoslash
// @errors: 2307
// ---cut---
import { defineNuxtModule, getLayerDirectories } from '@nuxt/kit'
import { resolve } from 'pathe'
import { globby } from 'globby'

export default defineNuxtModule({
  async setup () {
    const layerDirs = getLayerDirectories()

    // Find all component files across layers
    // Note: layerDirs[0] is the user layer (highest priority)
    // Later layers in the array have lower priority
    const componentFiles = []
    for (const [index, layer] of layerDirs.entries()) {
      const files = await globby('**/*.vue', {
        cwd: resolve(layer.app, 'components'),
        absolute: true,
      })
      console.log(`Layer ${index} (${index === 0 ? 'user' : 'base'}):`, files.length, 'components')
      componentFiles.push(...files)
    }
  },
})
```

**Adding templates from multiple layers:**

```tstwoslash
import { addTemplate, defineNuxtModule, getLayerDirectories } from '@nuxt/kit'
import { basename, resolve } from 'pathe'
import { existsSync } from 'node:fs'

export default defineNuxtModule({
  setup () {
    const layerDirs = getLayerDirectories()

    // Add a config file from each layer that has one
    for (const dirs of layerDirs) {
      const configPath = resolve(dirs.app, 'my-module.config.ts')
      if (existsSync(configPath)) {
        addTemplate({
          filename: `my-module-${basename(dirs.root)}.config.ts`,
          src: configPath,
        })
      }
    }
  },
})
```

**Respecting layer priority:**

```tstwoslash
import { defineNuxtModule, getLayerDirectories } from '@nuxt/kit'
import { resolve } from 'pathe'
import { existsSync, readFileSync } from 'node:fs'

export default defineNuxtModule({
  setup () {
    const layerDirs = getLayerDirectories()

    // Find the first (highest priority) layer that has a specific config file
    // This respects the layer priority system
    let configContent = null
    for (const dirs of layerDirs) {
      const configPath = resolve(dirs.app, 'my-config.json')
      if (existsSync(configPath)) {
        configContent = readFileSync(configPath, 'utf-8')
        console.log(`Using config from layer: ${dirs.root}`)
        break // Use the first (highest priority) config found
      }
    }

    // Alternative: Collect configs from all layers, with user layer taking precedence
    const allConfigs = {}
    for (const dirs of layerDirs.reverse()) { // Process from lowest to highest priority
      const configPath = resolve(dirs.app, 'my-config.json')
      if (existsSync(configPath)) {
        const config = JSON.parse(readFileSync(configPath, 'utf-8'))
        Object.assign(allConfigs, config) // Later assignments override earlier ones
      }
    }
  },
})
```

**Checking for layer-specific directories:**

```tstwoslash
import { defineNuxtModule, getLayerDirectories } from '@nuxt/kit'
import { existsSync } from 'node:fs'
import { resolve } from 'pathe'

export default defineNuxtModule({
  setup () {
    const layerDirs = getLayerDirectories()

    // Find layers that have a specific custom directory
    const layersWithAssets = layerDirs.filter((layer) => {
      return existsSync(resolve(layer.app, 'assets'))
    })

    console.log(`Found ${layersWithAssets.length} layers with assets directory`)
  },
})
```

<note>

The `getLayerDirectories` function includes caching via a WeakMap to avoid recomputing directory paths for the same layers repeatedly, improving performance when called multiple times.

</note>

<note>

Directory paths returned by this function always include a trailing slash for consistency.

</note>

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/layers.ts)

## Programmatic

# Programmatic Usage

> Nuxt Kit provides a set of utilities to help you work with Nuxt programmatically. These functions allow you to load Nuxt, build Nuxt, and load Nuxt configuration.

Programmatic usage can be helpful when you want to use Nuxt programmatically, for example, when building a [CLI tool](https://github.com/nuxt/cli) or [test utils](https://github.com/nuxt/test-utils).

## `loadNuxt`

Load Nuxt programmatically. It will load the Nuxt configuration, instantiate and return the promise with Nuxt instance.

### Type

```ts
function loadNuxt (loadOptions?: LoadNuxtOptions): Promise<Nuxt>
```

### Parameters

**loadOptions**: Loading conditions for Nuxt. `loadNuxt` uses [`c12`](https://github.com/unjs/c12) under the hood, so it accepts the same options as `c12.loadConfig` with some additional options:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        dev
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , Nuxt will be loaded in development mode.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ready
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , Nuxt will be ready to use after the <code>
        loadNuxt
      </code>
      
       call. If set to <code>
        false
      </code>
      
      , you will need to call <code>
        nuxt.ready()
      </code>
      
       to make sure Nuxt is ready to use.
    </td>
  </tr>
</tbody>
</table>

## `buildNuxt`

Build Nuxt programmatically. It will invoke the builder (currently [@nuxt/vite-builder](https://github.com/nuxt/nuxt/tree/main/packages/vite) or [@nuxt/webpack-builder](https://github.com/nuxt/nuxt/tree/main/packages/webpack)) to bundle the application.

### Type

```ts
function buildNuxt (nuxt: Nuxt): Promise<any>
```

### Parameters

**nuxt**: Nuxt instance to build. It can be retrieved from the context via `useNuxt()` call.

## `loadNuxtConfig`

Load Nuxt configuration. It will return the promise with the configuration object.

### Type

```ts
function loadNuxtConfig (options: LoadNuxtConfigOptions): Promise<NuxtOptions>
```

### Parameters

**options**: Options to pass in [`c12`](https://github.com/unjs/c12#options) `loadConfig` call.

## `writeTypes`

Generates `tsconfig.json` and writes it to the project buildDir.

### Type

```ts
function writeTypes (nuxt?: Nuxt): void
```

### Parameters

**nuxt**: Nuxt instance to build. It can be retrieved from the context via `useNuxt()` call.

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}

</style>

---

- [Source](https://github.com/nuxt/nuxt/tree/main/packages/kit/src/loader)

## Compatibility

# Compatibility

> Nuxt Kit provides a set of utilities to help you check the compatibility of your modules with different Nuxt versions.

Nuxt Kit utilities can be used in Nuxt 3, Nuxt 2 with Bridge and even Nuxt 2 without Bridge. To make sure your module is compatible with all versions, you can use the `checkNuxtCompatibility`, `assertNuxtCompatibility` and `hasNuxtCompatibility` functions. They will check if the current Nuxt version meets the constraints you provide. Also you can use `isNuxt2`, `isNuxt3` and `getNuxtVersion` functions for more granular checks.

## `checkNuxtCompatibility`

Checks if constraints are met for the current Nuxt version. If not, returns an array of messages. Nuxt 2 version also checks for `bridge` support.

### Usage

```tstwoslash
import { checkNuxtCompatibility, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  async setup (_options, nuxt) {
    const issues = await checkNuxtCompatibility({ nuxt: '^2.16.0' }, nuxt)
    if (issues.length) {
      console.warn('Nuxt compatibility issues found:\n' + issues.toString())
    } else {
      // do something
    }
  },
})
```

### Type

```ts
function checkNuxtCompatibility (constraints: NuxtCompatibility, nuxt?: Nuxt): Promise<NuxtCompatibilityIssues>
```

### Parameters

**constraints**: Version and builder constraints to check against. It accepts the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        nuxt
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Nuxt version in semver format. Versions may be defined in Node.js way, for example: <code>
        >=2.15.0 <3.0.0
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        bridge
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          Record
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          ,
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sbKd-">
          false
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Specifies version constraints or disables compatibility for specific Nuxt builders like <code>
        vite
      </code>
      
      , <code>
        webpack
      </code>
      
      , or <code>
        rspack
      </code>
      
      . Use <code>
        false
      </code>
      
       to disable.
    </td>
  </tr>
</tbody>
</table>

**nuxt**: Nuxt instance. If not provided, it will be retrieved from the context via `useNuxt()` call.

## `assertNuxtCompatibility`

Asserts that constraints are met for the current Nuxt version. If not, throws an error with the list of issues as string.

### Type

```tstwoslash
// @errors: 2391
import type { Nuxt, NuxtCompatibility } from '@nuxt/schema'
// ---cut---
function assertNuxtCompatibility (constraints: NuxtCompatibility, nuxt?: Nuxt): Promise<true>
```

### Parameters

**constraints**: Version and builder constraints to check against. Refer to the [constraints table in `checkNuxtCompatibility`](/docs/4.x/api/kit/compatibility#parameters) for details.

**nuxt**: Nuxt instance. If not provided, it will be retrieved from the context via `useNuxt()` call.

## `hasNuxtCompatibility`

Checks if constraints are met for the current Nuxt version. Return `true` if all constraints are met, otherwise returns `false`. Nuxt 2 version also checks for `bridge` support.

### Usage

```tstwoslash
import { defineNuxtModule, hasNuxtCompatibility } from '@nuxt/kit'

export default defineNuxtModule({
  async setup (_options, nuxt) {
    const usingNewPostcss = await hasNuxtCompatibility({ nuxt: '^2.16.0' }, nuxt)
    if (usingNewPostcss) {
      // do something
    } else {
      // do something else
    }
  },
})
```

### Type

```ts
function hasNuxtCompatibility (constraints: NuxtCompatibility, nuxt?: Nuxt): Promise<boolean>
```

### Parameters

**constraints**: Version and builder constraints to check against. Refer to the [constraints table in `checkNuxtCompatibility`](/docs/4.x/api/kit/compatibility#parameters) for details.

**nuxt**: Nuxt instance. If not provided, it will be retrieved from the context via `useNuxt()` call.

## `isNuxtMajorVersion`

Check if current Nuxt instance is of specified major version

### Usage

```tstwoslash
import { defineNuxtModule, isNuxtMajorVersion } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    if (isNuxtMajorVersion(3)) {
      // do something for Nuxt 3
    } else {
      // do something else for other versions
    }
  },
})
```

### Type

```ts
function isNuxtMajorVersion (major: number, nuxt?: Nuxt): boolean
```

### Parameters

**major**: Major version to check against.

**nuxt**: Nuxt instance. If not provided, it will be retrieved from the context via `useNuxt()` call.

## `isNuxt3`

Checks if the current Nuxt version is 3.x.

<note>

Use `isNuxtMajorVersion(2, nuxt)` instead. This may be removed in @nuxt/kit v5 or a future major version.

</note>

### Type

```ts
function isNuxt3 (nuxt?: Nuxt): boolean
```

### Parameters

**nuxt**: Nuxt instance. If not provided, it will be retrieved from the context via `useNuxt()` call.

## `isNuxt2`

Checks if the current Nuxt version is 2.x.

<note>

Use `isNuxtMajorVersion(2, nuxt)` instead. This may be removed in @nuxt/kit v5 or a future major version.

</note>

### Type

```ts
function isNuxt2 (nuxt?: Nuxt): boolean
```

### Parameters

**nuxt**: Nuxt instance. If not provided, it will be retrieved from the context via `useNuxt()` call.

## `getNuxtVersion`

Returns the current Nuxt version.

### Type

```ts
function getNuxtVersion (nuxt?: Nuxt): string
```

### Parameters

**nuxt**: Nuxt instance. If not provided, it will be retrieved from the context via `useNuxt()` call.

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/compatibility.ts)

## Autoimports

# Auto-imports

> Nuxt Kit provides a set of utilities to help you work with auto-imports. These functions allow you to register your own utils, composables and Vue APIs.

Nuxt auto-imports helper functions, composables and Vue APIs to use across your application without explicitly importing them. Based on the directory structure, every Nuxt application can also use auto-imports for its own composables and plugins.

With Nuxt Kit you can also add your own auto-imports. `addImports` and `addImportsDir` allow you to add imports to the Nuxt application. `addImportsSources` allows you to add listed imports from 3rd party packages to the Nuxt application.

These utilities are powered by [`unimport`](https://github.com/unjs/unimport), which provides the underlying auto-import mechanism used in Nuxt.

<note>

These functions are designed for registering your own utils, composables and Vue APIs. For pages, components and plugins, please refer to the specific sections: [Pages](/docs/4.x/api/kit/pages), [Components](/docs/4.x/api/kit/components), [Plugins](/docs/4.x/api/kit/plugins).

</note>

<tip icon="i-lucide-video" target="_blank" to="https://vueschool.io/lessons/expanding-nuxt-s-auto-imports?friend=nuxt">

Watch Vue School video about Auto-imports Nuxt Kit utilities.

</tip>

## `addImports`

Add imports to the Nuxt application. It makes your imports available in the Nuxt app context without the need to import them manually.

<tip>

To add imports for the Nitro server context, refer to the [`addServerImports`](/docs/4.x/api/kit/nitro#addserverimports) function.

</tip>

### Usage

```tstwoslash
import { addImports, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options, nuxt) {
    const names = [
      'useStoryblok',
      'useStoryblokApi',
      'useStoryblokBridge',
      'renderRichText',
      'RichTextSchema',
    ]

    names.forEach(name =>
      addImports({ name, as: name, from: '@storyblok/vue' }),
    )
  },
})
```

### Type

```ts
function addImports (imports: Import | Import[]): void
```

### Parameters

`imports`: An object or an array of objects with the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        name
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Import name to be detected.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        from
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Module specifier to import from.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        priority
      </code>
    </td>
    
    <td>
      <code>
        number
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Priority of the import; if multiple imports have the same name, the one with the highest priority will be used.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        disabled
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If this import is disabled.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        meta
      </code>
    </td>
    
    <td>
      <code>
        Record<string, any>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Metadata of the import.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        type
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If this import is a pure type import.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        typeFrom
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Use this as the <code>
        from
      </code>
      
       value when generating type declarations.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        as
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Import as this name.
    </td>
  </tr>
</tbody>
</table>

## `addImportsDir`

Add imports from a directory to the Nuxt application. It will automatically import all files from the directory and make them available in the Nuxt application without the need to import them manually.

### Usage

```tstwoslash
import { addImportsDir, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: '@vueuse/motion',
    configKey: 'motion',
  },
  setup (options, nuxt) {
    const resolver = createResolver(import.meta.url)
    addImportsDir(resolver.resolve('./runtime/composables'))
  },
})
```

### Type

```ts
function addImportsDir (dirs: string | string[], options?: { prepend?: boolean }): void
```

### Parameters

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        dirs
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sZSNi">
          string[]
        </span>
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      A string or an array of strings with the path to the directory to import from.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        options
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          {
        </span>
        
        <span class="sZSNi">
          prepend
        </span>
        
        <span class="sDfIl">
          ?:
        </span>
        
        <span class="sZSNi">
          boolean
        </span>
        
        <span class="sDfIl">
          }
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Options to pass to the import. If <code>
        prepend
      </code>
      
       is set to <code>
        true
      </code>
      
      , the imports will be prepended to the list of imports.
    </td>
  </tr>
</tbody>
</table>

## `addImportsSources`

Add listed imports to the Nuxt application.

### Usage

```tstwoslash
import { addImportsSources, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    addImportsSources([
      { package: '@vueuse/core' },
      {
        from: 'h3',
        imports: [
          'defineEventHandler',
          'getQuery',
          'getRouterParams',
          'readBody',
          'sendRedirect',
        ],
      },
    ])
  },
})
```

### Type

```ts
function addImportsSources (importSources: Preset | Preset[]): void
```

### Parameters

**importSources**: An object or an array of objects with the following properties:

- InlinePreset

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        from
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Module specifier to import from.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        imports
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          PresetImport
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sZSNi">
          ImportSource[]
        </span>
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      An object or an array of objects, which can be import names, import objects or import sources.
    </td>
  </tr>
</tbody>
</table>

- PackagePreset

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        package
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Name of the package.
    </td>
  </tr>
</tbody>
</table>

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/imports.ts)

## Components

# Components

> Nuxt Kit provides a set of utilities to help you work with components. You can register components globally or locally, and also add directories to be scanned for components.

Components are the building blocks of your Nuxt application. They are reusable Vue instances that can be used to create a user interface. In Nuxt, components from the components directory are automatically imported by default. However, if you need to import components from an alternative directory or wish to selectively import them as needed, `@nuxt/kit` provides the `addComponentsDir` and `addComponent` methods. These utils allow you to customize the component configuration to better suit your needs.

<tip icon="i-lucide-video" target="_blank" to="https://vueschool.io/lessons/injecting-components-and-component-directories?friend=nuxt">

Watch Vue School video about injecting components.

</tip>

## `addComponentsDir`

Register a directory to be scanned for components and imported only when used. Keep in mind, that this does not register components globally, until you specify `global: true` option.

### Usage

```ts
export default defineNuxtModule({
  meta: {
    name: '@nuxt/ui',
    configKey: 'ui',
  },
  setup () {
    addComponentsDir({
      path: resolve('./runtime/components'),
      prefix: 'U',
      pathPrefix: false,
    })
  },
})
```

### Type

```ts
function addComponentsDir (dir: ComponentsDir, opts: { prepend?: boolean } = {}): void
```

### Parameters

`dir` An object with the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        path
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Path (absolute or relative) to the directory containing your components. You can use Nuxt aliases (~ or @) to refer to directories inside project or directly use an npm package path similar to require.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        pattern
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sZSNi">
          string[]
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Accept Pattern that will be run against specified path.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        ignore
      </code>
    </td>
    
    <td>
      <code>
        string[]
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Ignore patterns that will be run against specified path.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        prefix
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Prefix all matched components with this string.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        pathPrefix
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Prefix component name by its path.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        prefetch
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      These properties (prefetch/preload) are used in production to configure how components with Lazy prefix are handled by webpack via its magic comments. Learn more on <a href="https://webpack.js.org/api/module-methods/#magic-comments" rel="nofollow">
        webpack documentation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        preload
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      These properties (prefetch/preload) are used in production to configure how components with Lazy prefix are handled by webpack via its magic comments. Learn more on <a href="https://webpack.js.org/api/module-methods/#magic-comments" rel="nofollow">
        webpack documentation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        isAsync
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      This flag indicates, component should be loaded async (with a separate chunk) regardless of using Lazy prefix or not.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        extendComponent
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          (
        </span>
        
        <span class="s1nJG">
          component
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          Component
        </span>
        
        <span class="sDfIl">
          )
        </span>
        
        <span class="smZ93">
          =>
        </span>
        
        <span class="s52Pk">
          Promise
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          Component
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sDfIl">
          void>
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sZSNi">
          (Component
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sDfIl">
          void
        </span>
        
        <span class="sZSNi">
          )
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      A function that will be called for each component found in the directory. It accepts a component object and should return a component object or a promise that resolves to a component object.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        global
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If enabled, registers components to be globally available.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        island
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If enabled, registers components as islands. You can read more about islands in <a href="/docs/4.x/api/components/nuxt-island">
        <code>
          <NuxtIsland/>
        </code>
      </a>
      
       component description.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        watch
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Watch specified path for changes, including file additions and file deletions.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        extensions
      </code>
    </td>
    
    <td>
      <code>
        string[]
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Extensions supported by Nuxt builder.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        transpile
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          '
        </span>
        
        <span class="sGFVr">
          auto
        </span>
        
        <span class="sDfIl">
          '
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sZSNi">
          boolean
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Transpile specified path using build.transpile. If set to <code>
        'auto'
      </code>
      
      , it will set <code>
        transpile: true
      </code>
      
       if <code>
        node_modules/
      </code>
      
       is in path.
    </td>
  </tr>
</tbody>
</table>

`opts`

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        prepend
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the directory will be prepended to the array with <code>
        unshift()
      </code>
      
       instead of <code>
        push()
      </code>
      
      .
    </td>
  </tr>
</tbody>
</table>

## `addComponent`

Register a component to be automatically imported.

### Usage

```ts
import { addComponent, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: '@nuxt/image',
    configKey: 'image',
  },
  setup () {
    const resolver = createResolver(import.meta.url)

    addComponent({
      name: 'NuxtImg',
      filePath: resolver.resolve('./runtime/components/NuxtImg.vue'),
    })

    addComponent({
      name: 'NuxtPicture',
      filePath: resolver.resolve('./runtime/components/NuxtPicture.vue'),
    })
  },
})
```

### Type

```ts
function addComponent (options: AddComponentOptions): void
```

### Parameters

`options`: An object with the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        name
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Component name.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        filePath
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Path to the component.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        declarationPath
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Path to component's declaration file. It is used to generate components' <a href="/docs/4.x/api/kit/templates#addtypetemplate">
        type templates
      </a>
      
      ; if not provided, <code>
        filePath
      </code>
      
       is used instead.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        pascalName
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Pascal case component name. If not provided, it will be generated from the component name.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        kebabName
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Kebab case component name. If not provided, it will be generated from the component name.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        export
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Specify named or default export. If not provided, it will be set to <code>
        'default'
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        shortPath
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Short path to the component. If not provided, it will be generated from the component path.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        chunkName
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Chunk name for the component. If not provided, it will be generated from the component name.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        prefetch
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      These properties (prefetch/preload) are used in production to configure how components with Lazy prefix are handled by webpack via its magic comments. Learn more on <a href="https://webpack.js.org/api/module-methods/#magic-comments" rel="nofollow">
        webpack documentation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        preload
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      These properties (prefetch/preload) are used in production to configure how components with Lazy prefix are handled by webpack via its magic comments. Learn more on <a href="https://webpack.js.org/api/module-methods/#magic-comments" rel="nofollow">
        webpack documentation
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        global
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If enabled, registers component to be globally available.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        island
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If enabled, registers component as island. You can read more about islands in <a href="/docs/4.x/api/components/nuxt-island">
        <code>
          <NuxtIsland/>
        </code>
      </a>
      
       component description.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        mode
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          '
        </span>
        
        <span class="sGFVr">
          client
        </span>
        
        <span class="sDfIl">
          '
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sDfIl">
          '
        </span>
        
        <span class="sGFVr">
          server
        </span>
        
        <span class="sDfIl">
          '
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sDfIl">
          '
        </span>
        
        <span class="sGFVr">
          all
        </span>
        
        <span class="sDfIl">
          '
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      This options indicates if component should render on client, server or both. By default, it will render on both client and server.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        priority
      </code>
    </td>
    
    <td>
      <code>
        number
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Priority of the component, if multiple components have the same name, the one with the highest priority will be used.
    </td>
  </tr>
</tbody>
</table>

### Examples

If you want to auto-import a component from an npm package, and the component is a named export (rather than the default), you can use the `export` option to specify it.

```ts
import { addComponent, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    // import { MyComponent as MyAutoImportedComponent } from 'my-npm-package'
    addComponent({
      name: 'MyAutoImportedComponent',
      export: 'MyComponent',
      filePath: 'my-npm-package',
    })
  },
})
```

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/components.ts)

## Context

# Context

> Nuxt Kit provides a set of utilities to help you work with context.

Nuxt modules allow you to enhance Nuxt's capabilities. They offer a structured way to keep your code organized and modular. If you're looking to break down your module into smaller components, Nuxt offers the `useNuxt` and `tryUseNuxt` functions. These functions enable you to conveniently access the Nuxt instance from the context without having to pass it as an argument.

<note>

When you're working with the `setup` function in Nuxt modules, Nuxt is already provided as the second argument. This means you can access it directly without needing to call `useNuxt()`.

</note>

## `useNuxt`

Get the Nuxt instance from the context. It will throw an error if Nuxt is not available.

### Usage

```ts
import { useNuxt } from '@nuxt/kit'

const setupSomeFeature = () => {
  const nuxt = useNuxt()

  // You can now use the nuxt instance
  console.log(nuxt.options)
}
```

### Type

```tstwoslash
// @errors: 2391
import type { Nuxt } from '@nuxt/schema'
// ---cut---
function useNuxt (): Nuxt
```

### Return Value

The `useNuxt` function returns the Nuxt instance, which contains all the options and methods available in Nuxt.

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        options
      </code>
    </td>
    
    <td>
      <code>
        NuxtOptions
      </code>
    </td>
    
    <td>
      The resolved Nuxt configuration.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        hooks
      </code>
    </td>
    
    <td>
      <code>
        Hookable<NuxtHooks>
      </code>
    </td>
    
    <td>
      The Nuxt hook system. Allows registering and listening to lifecycle events.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        hook
      </code>
    </td>
    
    <td>
      <code>
        (name: string, (...args: any[]) => Promise<void> | void) => () => void
      </code>
    </td>
    
    <td>
      Shortcut for <code>
        nuxt.hooks.hook
      </code>
      
      . Registers a single callback for a specific lifecycle hook.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        callHook
      </code>
    </td>
    
    <td>
      <code>
        (name: string, ...args: any[]) => Promise<any>
      </code>
    </td>
    
    <td>
      Shortcut for <code>
        nuxt.hooks.callHook
      </code>
      
      . Triggers a lifecycle hook manually and runs all registered callbacks.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        addHooks
      </code>
    </td>
    
    <td>
      <code>
        (configHooks: NestedHooks) => () => void
      </code>
    </td>
    
    <td>
      Shortcut for <code>
        nuxt.hooks.addHooks
      </code>
      
      . Registers multiple hooks at once.
    </td>
  </tr>
</tbody>
</table>

### Examples

<code-group>

```ts [setupTranspilation.ts]twoslash
import { useNuxt } from '@nuxt/kit'

export const setupTranspilation = () => {
  const nuxt = useNuxt()

  if (nuxt.options.builder === '@nuxt/webpack-builder') {
    nuxt.options.build.transpile ||= []
    nuxt.options.build.transpile.push('xstate')
  }
}
```

```ts [module.ts]twoslash
// @module: esnext
// @filename: setupTranspilation.ts
export const setupTranspilation = () => {}
// @filename: module.ts
import { defineNuxtModule } from '@nuxt/kit'
// ---cut---
import { setupTranspilation } from './setupTranspilation'

export default defineNuxtModule({
  setup () {
    setupTranspilation()
  },
})
```

</code-group>

## `tryUseNuxt`

Get the Nuxt instance from the context. It will return `null` if Nuxt is not available.

### Usage

```tstwoslash
import { tryUseNuxt } from '@nuxt/kit'

function setupSomething () {
  const nuxt = tryUseNuxt()

  if (nuxt) {
    // You can now use the nuxt instance
    console.log(nuxt.options)
  } else {
    console.log('Nuxt is not available')
  }
}
```

### Type

```tstwoslash
// @errors: 2391
import type { Nuxt } from '@nuxt/schema'
// ---cut---
function tryUseNuxt (): Nuxt | null
```

### Return Value

The `tryUseNuxt` function returns the Nuxt instance if available, or `null` if Nuxt is not available.

The Nuxt instance as described in the `useNuxt` section.

### Examples

<code-group>

```ts [requireSiteConfig.ts]twoslash
declare module '@nuxt/schema' {
  interface NuxtOptions {
    siteConfig: SiteConfig
  }
}
// ---cut---
import { tryUseNuxt } from '@nuxt/kit'

interface SiteConfig {
  title?: string
}

export const requireSiteConfig = (): SiteConfig => {
  const nuxt = tryUseNuxt()
  if (!nuxt) {
    return {}
  }
  return nuxt.options.siteConfig
}
```

```ts [module.ts]twoslash
// @module: esnext
// @filename: requireSiteConfig.ts
interface SiteConfig {
  title?: string
}
export const requireSiteConfig = (): SiteConfig => {
  return {}
}
// @filename: module.ts
// ---cut---
import { defineNuxtModule, useNuxt } from '@nuxt/kit'
import { requireSiteConfig } from './requireSiteConfig'

export default defineNuxtModule({
  setup (_, nuxt) {
    const config = requireSiteConfig()
    nuxt.options.app.head.title = config.title
  },
})
```

</code-group>

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/context.ts)

## Pages

# Pages

> Nuxt Kit provides a set of utilities to help you create and use pages. You can use these utilities to manipulate the pages configuration or to define route rules.

## `extendPages`

In Nuxt, routes are automatically generated based on the structure of the files in the `app/pages` directory. However, there may be scenarios where you'd want to customize these routes. For instance, you might need to add a route for a dynamic page not generated by Nuxt, remove an existing route, or modify the configuration of a route. For such customizations, Nuxt offers the `extendPages` feature, which allows you to extend and alter the pages configuration.

<tip icon="i-lucide-video" target="_blank" to="https://vueschool.io/lessons/extend-and-alter-nuxt-pages?friend=nuxt">

Watch Vue School video about extendPages.

</tip>

### Usage

```tstwoslash
import { createResolver, defineNuxtModule, extendPages } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options) {
    const { resolve } = createResolver(import.meta.url)

    extendPages((pages) => {
      pages.unshift({
        name: 'prismic-preview',
        path: '/preview',
        file: resolve('runtime/preview.vue'),
      })
    })
  },
})
```

### Type

```ts
function extendPages (callback: (pages: NuxtPage[]) => void): void
```

### Parameters

**callback**: A function that will be called with the pages configuration. You can alter this array by adding, deleting, or modifying its elements. Note: You should modify the provided pages array directly, as changes made to a copied array will not be reflected in the configuration.

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        name
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      The name of the route. Useful for programmatic navigation and identifying routes.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        path
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      The route URL path. If not set, Nuxt will infer it from the file location.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        file
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Path to the Vue file that should be used as the component for the route.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        meta
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          Record
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          ,
        </span>
        
        <span class="sZSNi">
          any
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Custom metadata for the route. Can be used in layouts, middlewares, or navigation guards.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        alias
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          string[]
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sZSNi">
          string
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      One or more alias paths for the route. Useful for supporting multiple URLs.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        redirect
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          RouteLocationRaw
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Redirect rule for the route. Supports named routes, objects, or string paths.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        children
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          NuxtPage[]
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Nested child routes under this route for layout or view nesting.
    </td>
  </tr>
</tbody>
</table>

## `extendRouteRules`

Nuxt is powered by the [Nitro](https://nitro.build/) server engine. With Nitro, you can incorporate high-level logic directly into your configuration, which is useful for actions like redirects, proxying, caching, and appending headers to routes. This configuration works by associating route patterns with specific route settings.

<tip>

You can read more about Nitro route rules in the [Nitro documentation](https://nitro.build/guide/routing#route-rules).

</tip>

<tip icon="i-lucide-video" target="_blank" to="https://vueschool.io/lessons/adding-route-rules-and-route-middlewares?friend=nuxt">

Watch Vue School video about adding route rules and route middlewares.

</tip>

### Usage

```tstwoslash
import { createResolver, defineNuxtModule, extendPages, extendRouteRules } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options) {
    const { resolve } = createResolver(import.meta.url)

    extendPages((pages) => {
      pages.unshift({
        name: 'preview-new',
        path: '/preview-new',
        file: resolve('runtime/preview.vue'),
      })
    })

    extendRouteRules('/preview', {
      redirect: {
        to: '/preview-new',
        statusCode: 302,
      },
    })

    extendRouteRules('/preview-new', {
      cache: {
        maxAge: 60 * 60 * 24 * 7,
      },
    })
  },
})
```

### Type

```ts
function extendRouteRules (route: string, rule: NitroRouteConfig, options?: ExtendRouteRulesOptions): void
```

### Parameters

**route**: A route pattern to match against.<br />

**rule**: A route rule configuration to apply to the matched route.

<tip>

About route rules configurations, you can get more detail in [Hybrid Rendering > Route Rules](/docs/4.x/guide/concepts/rendering#route-rules).

</tip>

**options**: An object to pass to the route configuration. If `override` is set to `true`, it will override the existing route configuration.

<table>
<thead>
  <tr>
    <th>
      Name
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Default
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        override
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Override route rule config, default is false
    </td>
  </tr>
</tbody>
</table>

## `addRouteMiddleware`

Registers route middlewares to be available for all routes or for specific routes.

Route middlewares can be also defined in plugins via [`addRouteMiddleware`](/docs/4.x/api/utils/add-route-middleware) composable.

<tip>

Read more about route middlewares in the [Route middleware documentation](/docs/4.x/getting-started/routing#route-middleware).

</tip>

<tip icon="i-lucide-video" target="_blank" to="https://vueschool.io/lessons/adding-route-rules-and-route-middlewares?friend=nuxt">

Watch Vue School video about adding route rules and route middlewares.

</tip>

### Usage

<code-group>

```ts [module.ts]twoslash
import { addRouteMiddleware, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    const { resolve } = createResolver(import.meta.url)

    addRouteMiddleware({
      name: 'auth',
      path: resolve('runtime/auth'),
      global: true,
    }, { prepend: true })
  },
})
```

```ts [runtime/auth.ts]twoslash
function isAuthenticated (): boolean { return false }
// ---cut---
export default defineNuxtRouteMiddleware((to, from) => {
  // isAuthenticated() is an example method verifying if a user is authenticated
  if (to.path !== '/login' && isAuthenticated() === false) {
    return navigateTo('/login')
  }
})
```

</code-group>

### Type

```ts
function addRouteMiddleware (input: NuxtMiddleware | NuxtMiddleware[], options?: AddRouteMiddlewareOptions): void
```

### Parameters

**input**: A middleware object or an array of middleware objects with the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        name
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      The name of the middleware.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        path
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      The file path to the middleware.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        global
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , applies middleware to all routes.
    </td>
  </tr>
</tbody>
</table>

**options**: An object with the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Default
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        override
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If <code>
        true
      </code>
      
      , replaces middleware with the same name.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        prepend
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If <code>
        true
      </code>
      
      , prepends middleware before existing middlewares.
    </td>
  </tr>
</tbody>
</table>

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sYRBq, html code.shiki .sYRBq{--shiki-light:#F76D47;--shiki-default:#F76D47;--shiki-dark:#F78C6C}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .sWuyu, html code.shiki .sWuyu{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#676E95;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/pages.ts)

## Layout

# Layout

> Nuxt Kit provides a set of utilities to help you work with layouts.

Layouts is used to be a wrapper around your pages. It can be used to wrap your pages with common components, for example, a header and a footer. Layouts can be registered using `addLayout` utility.

## `addLayout`

Register template as layout and add it to the layouts.

<note>

In Nuxt 2 `error` layout can also be registered using this utility. In Nuxt 3+ `error` layout [replaced](/docs/4.x/getting-started/error-handling#error-page) with `error.vue` page in project root.

</note>

### Usage

```tstwoslash
import { addLayout, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    const { resolve } = createResolver(import.meta.url)

    addLayout({
      src: resolve('templates/custom-layout.ts'),
      filename: 'custom-layout.ts',
    }, 'custom')
  },
})
```

### Type

```ts
function addLayout (layout: NuxtTemplate | string, name: string): void
```

### Parameters

**layout**: A template object or a string with the path to the template. If a string is provided, it will be converted to a template object with `src` set to the string value. If a template object is provided, it must have the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        src
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Path to the template. If <code>
        src
      </code>
      
       is not provided, <code>
        getContents
      </code>
      
       must be provided instead.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        filename
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Filename of the template. If <code>
        filename
      </code>
      
       is not provided, it will be generated from the <code>
        src
      </code>
      
       path. In this case, the <code>
        src
      </code>
      
       option is required.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        dst
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Path to the destination file. If <code>
        dst
      </code>
      
       is not provided, it will be generated from the <code>
        filename
      </code>
      
       path and nuxt <code>
        buildDir
      </code>
      
       option.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        options
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          Record
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          ,
        </span>
        
        <span class="sZSNi">
          any
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Options to pass to the template.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        getContents
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          (
        </span>
        
        <span class="s1nJG">
          data
        </span>
        
        <span class="sDfIl">
          )
        </span>
        
        <span class="smZ93">
          =>
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="s52Pk">
          Promise
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      A function that will be called with the <code>
        options
      </code>
      
       object. It should return a string or a promise that resolves to a string. If <code>
        src
      </code>
      
       is provided, this function will be ignored.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        write
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the template will be written to the destination file. Otherwise, the template will be used only in virtual filesystem.
    </td>
  </tr>
</tbody>
</table>

**name**: The name to register the layout under (e.g., `default`, `custom`, etc.).

### Example

This will register a layout named `custom` that wraps pages with a header and footer.

```tstwoslash
import { addLayout, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    addLayout({
      write: true,
      filename: 'my-layout.vue',
      getContents: () => `<template>
  <div>
    <header>My Header</header>
    <slot />
    <footer>My Footer</footer>
  </div>
</template>`,
    }, 'custom')
  },
})
```

You can then use this layout in your pages:

```vue [app/pages/about.vue]
<script setup lang="ts">
definePageMeta({
  layout: 'custom',
})
</script>

<template>
  <div>About Page</div>
</template>
```

<warning>

Due to the lack of support for virtual `.vue` files by `@vitejs/plugin-vue`, you can work around this limitation by passing `write: true` to the first argument of `addLayout`.

</warning>

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/layout.ts)

## Head

# Head

> Nuxt Kit provides utilities to help you manage head configuration in modules.

## `setGlobalHead`

Sets global head configuration for your Nuxt application. This utility allows modules to programmatically configure meta tags, links, scripts, and other head elements that will be applied across all pages.

The provided head configuration will be merged with any existing head configuration using deep merging, with your provided values taking precedence.

<tip>

This is particularly useful for modules that need to inject global meta tags, stylesheets, or scripts into the application head.

</tip>

### Type

```tstwoslash
// @errors: 2391
// ---cut---
import type { SerializableHead } from '@unhead/vue/types'

interface AppHeadMetaObject extends SerializableHead {
  charset?: string
  viewport?: string
}

function setGlobalHead (head: AppHeadMetaObject): void
```

### Parameters

#### `head`

**Type**: `AppHeadMetaObject`

An object containing head configuration. All properties are optional and will be merged with existing configuration:

- `charset`: Character encoding for the document
- `viewport`: Viewport meta tag configuration
- `meta`: Array of meta tag objects
- `link`: Array of link tag objects (stylesheets, icons, etc.)
- `style`: Array of inline style tag objects
- `script`: Array of script tag objects
- `noscript`: Array of noscript tag objects
- `title`: Default page title
- `titleTemplate`: Template for formatting page titles
- `bodyAttrs`: Attributes to add to the `<body>` tag
- `htmlAttrs`: Attributes to add to the `<html>` tag

### Examples

#### Adding Global Meta Tags

```ts
import { defineNuxtModule, setGlobalHead } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    setGlobalHead({
      meta: [
        { name: 'theme-color', content: '#ffffff' },
        { name: 'author', content: 'Your Name' },
      ],
    })
  },
})
```

#### Injecting Global Stylesheets

```ts
import { defineNuxtModule, setGlobalHead } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    setGlobalHead({
      link: [
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap',
        },
      ],
    })
  },
})
```

#### Adding Global Scripts

```ts
import { defineNuxtModule, setGlobalHead } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    setGlobalHead({
      script: [
        {
          src: 'https://cdn.example.com/analytics.js',
          async: true,
          defer: true,
        },
      ],
    })
  },
})
```

#### Setting HTML Attributes

```ts
import { defineNuxtModule, setGlobalHead } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    setGlobalHead({
      htmlAttrs: {
        lang: 'en',
        dir: 'ltr',
      },
      bodyAttrs: {
        class: 'custom-body-class',
      },
    })
  },
})
```

<style>

html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/head.ts)

## Plugins

# Plugins

> Nuxt Kit provides a set of utilities to help you create and use plugins. You can add plugins or plugin templates to your module using these functions.

Plugins are self-contained code that usually add app-level functionality to Vue. In Nuxt, plugins are automatically imported from the `app/plugins/` directory. However, if you need to ship a plugin with your module, Nuxt Kit provides the `addPlugin` and `addPluginTemplate` methods. These utils allow you to customize the plugin configuration to better suit your needs.

## `addPlugin`

Registers a Nuxt plugin and adds it to the plugins array.

<tip icon="i-lucide-video" target="_blank" to="https://vueschool.io/lessons/injecting-plugins?friend=nuxt">

Watch Vue School video about `addPlugin`.

</tip>

### Usage

```tstwoslash
import { addPlugin, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    const { resolve } = createResolver(import.meta.url)

    addPlugin({
      src: resolve('runtime/plugin.js'),
      mode: 'client',
    })
  },
})
```

### Type

```ts
function addPlugin (plugin: NuxtPlugin | string, options?: AddPluginOptions): NuxtPlugin
```

### Parameters

**plugin**: A plugin object or a string with the path to the plugin. If a string is provided, it will be converted to a plugin object with `src` set to the string value.

If a plugin object is provided, it must have the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        src
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
    
    <td>
      Path to the plugin file.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        mode
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          '
        </span>
        
        <span class="sGFVr">
          all
        </span>
        
        <span class="sDfIl">
          '
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sDfIl">
          '
        </span>
        
        <span class="sGFVr">
          server
        </span>
        
        <span class="sDfIl">
          '
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sDfIl">
          '
        </span>
        
        <span class="sGFVr">
          client
        </span>
        
        <span class="sDfIl">
          '
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        'all'
      </code>
      
      , the plugin will be included in both client and server bundles. If set to <code>
        'server'
      </code>
      
      , the plugin will only be included in the server bundle. If set to <code>
        'client'
      </code>
      
      , the plugin will only be included in the client bundle. You can also use <code>
        .client
      </code>
      
       and <code>
        .server
      </code>
      
       modifiers when specifying <code>
        src
      </code>
      
       option to use plugin only in client or server side.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        order
      </code>
    </td>
    
    <td>
      <code>
        number
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Order of the plugin. This allows more granular control over plugin order and should only be used by advanced users. Lower numbers run first, and user plugins default to <code>
        0
      </code>
      
      . It's recommended to set <code>
        order
      </code>
      
       to a number between <code>
        -20
      </code>
      
       for <code>
        pre
      </code>
      
      -plugins (plugins that run before Nuxt plugins) and <code>
        20
      </code>
      
       for <code>
        post
      </code>
      
      -plugins (plugins that run after Nuxt plugins).
    </td>
  </tr>
</tbody>
</table>

<warning>

Avoid using `order` unless necessary. Use `append` if you simply need to register plugins after Nuxt defaults.

</warning>

**options**: Optional object with the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        append
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If <code>
        true
      </code>
      
      , the plugin will be appended to the plugins array. If <code>
        false
      </code>
      
      , it will be prepended. Defaults to <code>
        false
      </code>
      
      .
    </td>
  </tr>
</tbody>
</table>

### Examples

<code-group>

```ts [module.ts]
import { addPlugin, createResolver, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup () {
    const { resolve } = createResolver(import.meta.url)

    addPlugin({
      src: resolve('runtime/plugin.js'),
      mode: 'client',
    })
  },
})
```

```ts [runtime/plugin.ts]
export default defineNuxtPlugin((nuxtApp) => {
  const colorMode = useColorMode()

  nuxtApp.hook('app:mounted', () => {
    if (colorMode.preference !== 'dark') {
      colorMode.preference = 'dark'
    }
  })
})
```

</code-group>

## `addPluginTemplate`

Adds a template and registers as a nuxt plugin. This is useful for plugins that need to generate code at build time.

<tip icon="i-lucide-video" target="_blank" to="https://vueschool.io/lessons/injecting-plugin-templates?friend=nuxt">

Watch Vue School video about `addPluginTemplate`.

</tip>

### Usage

```tstwoslash
import { addPluginTemplate, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options) {
    addPluginTemplate({
      filename: 'module-plugin.mjs',
      getContents: () => `import { defineNuxtPlugin } from '#app/nuxt'
export default defineNuxtPlugin({
  name: 'module-plugin',
  setup (nuxtApp) {
    ${options.log ? 'console.log("Plugin install")' : ''}
  }
})`,
    })
  },
})
```

### Type

```ts
function addPluginTemplate (pluginOptions: NuxtPluginTemplate, options?: AddPluginOptions): NuxtPlugin
```

### Parameters

**pluginOptions**: A plugin template object with the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        src
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Path to the template. If <code>
        src
      </code>
      
       is not provided, <code>
        getContents
      </code>
      
       must be provided instead.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        filename
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Filename of the template. If <code>
        filename
      </code>
      
       is not provided, it will be generated from the <code>
        src
      </code>
      
       path. In this case, the <code>
        src
      </code>
      
       option is required.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        dst
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Path to the destination file. If <code>
        dst
      </code>
      
       is not provided, it will be generated from the <code>
        filename
      </code>
      
       path and nuxt <code>
        buildDir
      </code>
      
       option.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        mode
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          '
        </span>
        
        <span class="sGFVr">
          all
        </span>
        
        <span class="sDfIl">
          '
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sDfIl">
          '
        </span>
        
        <span class="sGFVr">
          server
        </span>
        
        <span class="sDfIl">
          '
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="sDfIl">
          '
        </span>
        
        <span class="sGFVr">
          client
        </span>
        
        <span class="sDfIl">
          '
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        'all'
      </code>
      
      , the plugin will be included in both client and server bundles. If set to <code>
        'server'
      </code>
      
      , the plugin will only be included in the server bundle. If set to <code>
        'client'
      </code>
      
      , the plugin will only be included in the client bundle. You can also use <code>
        .client
      </code>
      
       and <code>
        .server
      </code>
      
       modifiers when specifying <code>
        src
      </code>
      
       option to use plugin only in client or server side.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        options
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sZSNi">
          Record
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          ,
        </span>
        
        <span class="sZSNi">
          any
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Options to pass to the template.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        getContents
      </code>
    </td>
    
    <td>
      <code className="language-ts shiki shiki-themes material-theme-lighter material-theme-lighter material-theme-palenight" language="ts" style="">
        <span class="sDfIl">
          (
        </span>
        
        <span class="s1nJG">
          data
        </span>
        
        <span class="sDfIl">
          :
        </span>
        
        <span class="s52Pk">
          Record
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="s52Pk">
          string
        </span>
        
        <span class="sDfIl">
          ,
        </span>
        
        <span class="s52Pk">
          any
        </span>
        
        <span class="sDfIl">
          >)
        </span>
        
        <span class="smZ93">
          =>
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          |
        </span>
        
        <span class="s52Pk">
          Promise
        </span>
        
        <span class="sDfIl">
          <
        </span>
        
        <span class="sZSNi">
          string
        </span>
        
        <span class="sDfIl">
          >
        </span>
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      A function that will be called with the <code>
        options
      </code>
      
       object. It should return a string or a promise that resolves to a string. If <code>
        src
      </code>
      
       is provided, this function will be ignored.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        write
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If set to <code>
        true
      </code>
      
      , the template will be written to the destination file. Otherwise, the template will be used only in virtual filesystem.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        order
      </code>
    </td>
    
    <td>
      <code>
        number
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      Order of the plugin. This allows more granular control over plugin order and should only be used by advanced users. Lower numbers run first, and user plugins default to <code>
        0
      </code>
      
      . It's recommended to set <code>
        order
      </code>
      
       to a number between <code>
        -20
      </code>
      
       for <code>
        pre
      </code>
      
      -plugins (plugins that run before Nuxt plugins) and <code>
        20
      </code>
      
       for <code>
        post
      </code>
      
      -plugins (plugins that run after Nuxt plugins).
    </td>
  </tr>
</tbody>
</table>

<warning>

Prefer using `getContents` for dynamic plugin generation. Avoid setting `order` unless necessary.

</warning>

**options**: Optional object with the following properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        append
      </code>
    </td>
    
    <td>
      <code>
        boolean
      </code>
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
    
    <td>
      If <code>
        true
      </code>
      
      , the plugin will be appended to the plugins array. If <code>
        false
      </code>
      
      , it will be prepended. Defaults to <code>
        false
      </code>
      
      .
    </td>
  </tr>
</tbody>
</table>

### Examples

#### Generate a plugin template with different options

Use `addPluginTemplate` when you need to generate plugin code dynamically at build time. This allows you to generate different plugin contents based on the options passed to it. For example, Nuxt internally uses this function to generate Vue app configurations.

```ts [module.ts]twoslash
import { addPluginTemplate, defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup (_, nuxt) {
    if (nuxt.options.vue.config && Object.values(nuxt.options.vue.config).some(v => v !== null && v !== undefined)) {
      addPluginTemplate({
        filename: 'vue-app-config.mjs',
        write: true,
        getContents: () => `import { defineNuxtPlugin } from '#app/nuxt'
export default defineNuxtPlugin({
  name: 'nuxt:vue-app-config',
  enforce: 'pre',
  setup (nuxtApp) {
    ${Object.keys(nuxt.options.vue.config!)
        .map(k => `nuxtApp.vueApp.config[${JSON.stringify(k)}] = ${JSON.stringify(nuxt.options.vue.config![k as 'idPrefix'])}`)
        .join('\n')
    }
  }
})`,
      })
    }
  },
})
```

This generates different plugin code depending on the provided configuration.

<code-group>

```ts [nuxt.config.ts]
export default defineNuxtConfig({
  vue: {
    config: {
      idPrefix: 'nuxt',
    },
  },
})
```

```ts [#build/vue-app-config.mjs]
import { defineNuxtPlugin } from '#app/nuxt'

export default defineNuxtPlugin({
  name: 'nuxt:vue-app-config',
  enforce: 'pre',
  setup (nuxtApp) {
    nuxtApp.vueApp.config.idPrefix = 'nuxt'
  },
})
```

</code-group>

<style>

html pre.shiki code .smZ93, html code.shiki .smZ93{--shiki-light:#9C3EDA;--shiki-default:#9C3EDA;--shiki-dark:#C792EA}html pre.shiki code .s3cPz, html code.shiki .s3cPz{--shiki-light:#6182B8;--shiki-default:#6182B8;--shiki-dark:#82AAFF}html pre.shiki code .sDfIl, html code.shiki .sDfIl{--shiki-light:#39ADB5;--shiki-default:#39ADB5;--shiki-dark:#89DDFF}html pre.shiki code .s1nJG, html code.shiki .s1nJG{--shiki-light:#90A4AE;--shiki-light-font-style:italic;--shiki-default:#90A4AE;--shiki-default-font-style:italic;--shiki-dark:#BABED8;--shiki-dark-font-style:italic}html pre.shiki code .s52Pk, html code.shiki .s52Pk{--shiki-light:#E2931D;--shiki-default:#E2931D;--shiki-dark:#FFCB6B}html .light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html.light .shiki span {color: var(--shiki-light);background: var(--shiki-light-bg);font-style: var(--shiki-light-font-style);font-weight: var(--shiki-light-font-weight);text-decoration: var(--shiki-light-text-decoration);}html .default .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .shiki span {color: var(--shiki-default);background: var(--shiki-default-bg);font-style: var(--shiki-default-font-style);font-weight: var(--shiki-default-font-weight);text-decoration: var(--shiki-default-text-decoration);}html .dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html.dark .shiki span {color: var(--shiki-dark);background: var(--shiki-dark-bg);font-style: var(--shiki-dark-font-style);font-weight: var(--shiki-dark-font-weight);text-decoration: var(--shiki-dark-text-decoration);}html pre.shiki code .sGFVr, html code.shiki .sGFVr{--shiki-light:#91B859;--shiki-default:#91B859;--shiki-dark:#C3E88D}html pre.shiki code .s8R28, html code.shiki .s8R28{--shiki-light:#39ADB5;--shiki-light-font-style:italic;--shiki-default:#39ADB5;--shiki-default-font-style:italic;--shiki-dark:#89DDFF;--shiki-dark-font-style:italic}html pre.shiki code .sZSNi, html code.shiki .sZSNi{--shiki-light:#90A4AE;--shiki-default:#90A4AE;--shiki-dark:#BABED8}html pre.shiki code .sRlkE, html code.shiki .sRlkE{--shiki-light:#E53935;--shiki-default:#E53935;--shiki-dark:#F07178}html pre.shiki code .sbKd-, html code.shiki .sbKd-{--shiki-light:#FF5370;--shiki-default:#FF5370;--shiki-dark:#FF9CAC}

</style>

---

- [Source](https://github.com/nuxt/nuxt/blob/main/packages/kit/src/plugin.ts)

## Examples

# Examples

> Examples of Nuxt Kit utilities in use.

## Accessing Nuxt Vite Config

If you are building an integration that needs access to the runtime Vite or webpack config that Nuxt uses, it is possible to extract this using Kit utilities.

Some examples of projects doing this already:

- [histoire](https://github.com/histoire-dev/histoire/blob/main/packages/histoire-plugin-nuxt/src/index.ts)
- [nuxt-vitest](https://github.com/danielroe/nuxt-vitest/blob/main/packages/nuxt-vitest/src/config.ts)
- [@storybook-vue/nuxt](https://github.com/storybook-vue/storybook-nuxt/blob/main/packages/storybook-nuxt/src/preset.ts)

Here is a brief example of how you might access the Vite config from a project; you could implement a similar approach to get the webpack configuration.

```js
import { buildNuxt, loadNuxt } from '@nuxt/kit'

// https://github.com/nuxt/nuxt/issues/14534
async function getViteConfig () {
  const nuxt = await loadNuxt({ cwd: process.cwd(), dev: false, overrides: { ssr: false } })
  return new Promise((resolve, reject) => {
    nuxt.hook('vite:extend', (config) => {
      resolve(config)
      throw new Error('_stop_')
    })
    buildNuxt(nuxt).catch((err) => {
      if (!err.toString().includes('_stop_')) {
        reject(err)
      }
    })
  }).finally(() => nuxt.close())
}

const viteConfig = await getViteConfig()
console.log(viteConfig)
```