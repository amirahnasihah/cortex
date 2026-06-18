# Nuxt - API - Advanced


## Hooks

# Lifecycle Hooks

> Nuxt provides a powerful hooking system to expand almost every aspect using hooks.

<read-more to="/docs/4.x/guide/going-further/hooks">



</read-more>

## App Hooks (runtime)

Check the [app source code](https://github.com/nuxt/nuxt/blob/main/packages/nuxt/src/app/nuxt.ts#L37) for all available hooks.

<table>
<thead>
  <tr>
    <th>
      Hook
    </th>
    
    <th>
      Arguments
    </th>
    
    <th>
      Environment
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
        app:created
      </code>
    </td>
    
    <td>
      <code>
        vueApp
      </code>
    </td>
    
    <td>
      Server & Client
    </td>
    
    <td>
      Called when initial <code>
        vueApp
      </code>
      
       instance is created.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app:error
      </code>
    </td>
    
    <td>
      <code>
        err
      </code>
    </td>
    
    <td>
      Server & Client
    </td>
    
    <td>
      Called when a fatal error occurs.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app:error:cleared
      </code>
    </td>
    
    <td>
      <code>
        { redirect? }
      </code>
    </td>
    
    <td>
      Server & Client
    </td>
    
    <td>
      Called when a fatal error occurs.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        vue:setup
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Server & Client
    </td>
    
    <td>
      Called when the setup of Nuxt root is initialized. This callback must be synchronous.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        vue:error
      </code>
    </td>
    
    <td>
      <code>
        err, target, info
      </code>
    </td>
    
    <td>
      Server & Client
    </td>
    
    <td>
      Called when a vue error propagates to the root component. <a href="https://vuejs.org/api/composition-api-lifecycle#onerrorcaptured" rel="nofollow">
        Learn More
      </a>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app:rendered
      </code>
    </td>
    
    <td>
      <code>
        renderContext
      </code>
    </td>
    
    <td>
      Server
    </td>
    
    <td>
      Called when SSR rendering is done.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app:redirected
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Server
    </td>
    
    <td>
      Called before SSR redirection.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app:beforeMount
      </code>
    </td>
    
    <td>
      <code>
        vueApp
      </code>
    </td>
    
    <td>
      Client
    </td>
    
    <td>
      Called before mounting the app, called only on client side.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app:mounted
      </code>
    </td>
    
    <td>
      <code>
        vueApp
      </code>
    </td>
    
    <td>
      Client
    </td>
    
    <td>
      Called when Vue app is initialized and mounted in browser.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app:suspense:resolve
      </code>
    </td>
    
    <td>
      <code>
        appComponent
      </code>
    </td>
    
    <td>
      Client
    </td>
    
    <td>
      On <a href="https://vuejs.org/guide/built-ins/suspense#suspense" rel="nofollow">
        Suspense
      </a>
      
       resolved event.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app:manifest:update
      </code>
    </td>
    
    <td>
      <code>
        { id, timestamp }
      </code>
    </td>
    
    <td>
      Client
    </td>
    
    <td>
      Called when there is a newer version of your app detected.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app:data:refresh
      </code>
    </td>
    
    <td>
      <code>
        keys?
      </code>
    </td>
    
    <td>
      Client
    </td>
    
    <td>
      Called when <code>
        refreshNuxtData
      </code>
      
       is called.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        link:prefetch
      </code>
    </td>
    
    <td>
      <code>
        to
      </code>
    </td>
    
    <td>
      Client
    </td>
    
    <td>
      Called when a <code>
        <NuxtLink>
      </code>
      
       is observed to be prefetched.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        page:start
      </code>
    </td>
    
    <td>
      <code>
        pageComponent?
      </code>
    </td>
    
    <td>
      Client
    </td>
    
    <td>
      Called on <a href="https://vuejs.org/guide/built-ins/suspense#suspense" rel="nofollow">
        Suspense
      </a>
      
       inside of <code>
        NuxtPage
      </code>
      
       pending event.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        page:finish
      </code>
    </td>
    
    <td>
      <code>
        pageComponent?
      </code>
    </td>
    
    <td>
      Client
    </td>
    
    <td>
      Called on <a href="https://vuejs.org/guide/built-ins/suspense#suspense" rel="nofollow">
        Suspense
      </a>
      
       inside of <code>
        NuxtPage
      </code>
      
       resolved event.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        page:loading:start
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Client
    </td>
    
    <td>
      Called when a route navigation begins (before resolution) or when the page key changes. May fire without the page component's <code>
        setup()
      </code>
      
       re-running if the page is reused (e.g. with a static <code>
        key
      </code>
      
       in <code>
        definePageMeta
      </code>
      
      ).
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        page:loading:end
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Client
    </td>
    
    <td>
      Called after <code>
        page:finish
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        page:transition:finish
      </code>
    </td>
    
    <td>
      <code>
        pageComponent?
      </code>
    </td>
    
    <td>
      Client
    </td>
    
    <td>
      After page transition <a href="https://vuejs.org/guide/built-ins/transition#javascript-hooks" rel="nofollow">
        onAfterLeave
      </a>
      
       event.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        dev:ssr-logs
      </code>
    </td>
    
    <td>
      <code>
        logs
      </code>
    </td>
    
    <td>
      Client
    </td>
    
    <td>
      Called with an array of server-side logs that have been passed to the client (if <code>
        features.devLogs
      </code>
      
       is enabled).
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        page:view-transition:start
      </code>
    </td>
    
    <td>
      <code>
        transition
      </code>
    </td>
    
    <td>
      Client
    </td>
    
    <td>
      Called after <code>
        document.startViewTransition
      </code>
      
       is called when <a href="/docs/4.x/getting-started/transitions#view-transitions-api-experimental">
        experimental viewTransition support is enabled
      </a>
      
      . The <code>
        transition
      </code>
      
       argument is a <a href="https://developer.mozilla.org/en-US/docs/Web/API/ViewTransition" rel="nofollow">
        <code>
          ViewTransition
        </code>
      </a>
      
       object with a <code>
        types
      </code>
      
       property (<a href="https://developer.mozilla.org/en-US/docs/Web/API/ViewTransitionTypeSet" rel="nofollow">
        <code>
          ViewTransitionTypeSet
        </code>
      </a>
      
      ) that can be read or modified.
    </td>
  </tr>
</tbody>
</table>

## Nuxt Hooks (build time)

Check the [schema source code](https://github.com/nuxt/nuxt/blob/main/packages/schema/src/types/hooks.ts#L83) for all available hooks.

<table>
<thead>
  <tr>
    <th>
      Hook
    </th>
    
    <th>
      Arguments
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
        kit:compatibility
      </code>
    </td>
    
    <td>
      <code>
        compatibility, issues
      </code>
    </td>
    
    <td>
      Allows extending compatibility checks.
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
        nuxt
      </code>
    </td>
    
    <td>
      Called after Nuxt initialization, when the Nuxt instance is ready to work.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        close
      </code>
    </td>
    
    <td>
      <code>
        nuxt
      </code>
    </td>
    
    <td>
      Called when Nuxt instance is gracefully closing.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        restart
      </code>
    </td>
    
    <td>
      <code>
        { hard?: boolean }
      </code>
    </td>
    
    <td>
      To be called to restart the current Nuxt instance.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        modules:before
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Called during Nuxt initialization, before installing user modules.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        modules:done
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Called during Nuxt initialization, after installing user modules.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app:resolve
      </code>
    </td>
    
    <td>
      <code>
        app
      </code>
    </td>
    
    <td>
      Called after resolving the <code>
        app
      </code>
      
       instance.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app:templates
      </code>
    </td>
    
    <td>
      <code>
        app
      </code>
    </td>
    
    <td>
      Called during <code>
        NuxtApp
      </code>
      
       generation, to allow customizing, modifying or adding new files to the build directory (either virtually or to written to <code>
        .nuxt
      </code>
      
      ).
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        app:templatesGenerated
      </code>
    </td>
    
    <td>
      <code>
        app
      </code>
    </td>
    
    <td>
      Called after templates are compiled into the <a href="/docs/4.x/directory-structure/nuxt">
        virtual file system
      </a>
      
       (vfs).
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        build:before
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Called before Nuxt bundle builder.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        build:done
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Called after Nuxt bundle builder is complete.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        build:manifest
      </code>
    </td>
    
    <td>
      <code>
        manifest
      </code>
    </td>
    
    <td>
      Called during the manifest build by Vite and webpack. This allows customizing the manifest that Nitro will use to render <code>
        <script>
      </code>
      
       and <code>
        <link>
      </code>
      
       tags in the final HTML.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        builder:generateApp
      </code>
    </td>
    
    <td>
      <code>
        options
      </code>
    </td>
    
    <td>
      Called before generating the app.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        builder:watch
      </code>
    </td>
    
    <td>
      <code>
        event, path
      </code>
    </td>
    
    <td>
      Called at build time in development when the watcher spots a change to a file or directory in the project.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        pages:extend
      </code>
    </td>
    
    <td>
      <code>
        pages
      </code>
    </td>
    
    <td>
      Called after page routes are scanned from the file system.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        pages:resolved
      </code>
    </td>
    
    <td>
      <code>
        pages
      </code>
    </td>
    
    <td>
      Called after page routes have been augmented with scanned metadata.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        pages:routerOptions
      </code>
    </td>
    
    <td>
      <code>
        { files: Array<{ path: string, optional?: boolean }> }
      </code>
    </td>
    
    <td>
      Called when resolving <code>
        router.options
      </code>
      
       files. Later items in the array override earlier ones.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        server:devHandler
      </code>
    </td>
    
    <td>
      <code>
        handler
      </code>
    </td>
    
    <td>
      Called when the dev middleware is being registered on the Nitro dev server.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        imports:sources
      </code>
    </td>
    
    <td>
      <code>
        presets
      </code>
    </td>
    
    <td>
      Called at setup allowing modules to extend sources.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        imports:extend
      </code>
    </td>
    
    <td>
      <code>
        imports
      </code>
    </td>
    
    <td>
      Called at setup allowing modules to extend imports.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        imports:context
      </code>
    </td>
    
    <td>
      <code>
        context
      </code>
    </td>
    
    <td>
      Called when the <a href="https://github.com/unjs/unimport" rel="nofollow">
        unimport
      </a>
      
       context is created.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        imports:dirs
      </code>
    </td>
    
    <td>
      <code>
        dirs
      </code>
    </td>
    
    <td>
      Allows extending import directories.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        components:dirs
      </code>
    </td>
    
    <td>
      <code>
        dirs
      </code>
    </td>
    
    <td>
      Called within <code>
        app:resolve
      </code>
      
       allowing to extend the directories that are scanned for auto-importable components.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        components:extend
      </code>
    </td>
    
    <td>
      <code>
        components
      </code>
    </td>
    
    <td>
      Allows extending new components.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        nitro:config
      </code>
    </td>
    
    <td>
      <code>
        nitroConfig
      </code>
    </td>
    
    <td>
      Called before initializing Nitro, allowing customization of Nitro's configuration.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        nitro:init
      </code>
    </td>
    
    <td>
      <code>
        nitro
      </code>
    </td>
    
    <td>
      Called after Nitro is initialized, which allows registering Nitro hooks and interacting directly with Nitro.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        nitro:build:before
      </code>
    </td>
    
    <td>
      <code>
        nitro
      </code>
    </td>
    
    <td>
      Called before building the Nitro instance.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        nitro:build:public-assets
      </code>
    </td>
    
    <td>
      <code>
        nitro
      </code>
    </td>
    
    <td>
      Called after copying public assets. Allows modifying public assets before Nitro server is built.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        prerender:routes
      </code>
    </td>
    
    <td>
      <code>
        ctx
      </code>
    </td>
    
    <td>
      Allows extending the routes to be pre-rendered.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        build:error
      </code>
    </td>
    
    <td>
      <code>
        error
      </code>
    </td>
    
    <td>
      Called when an error occurs at build time.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        prepare:types
      </code>
    </td>
    
    <td>
      <code>
        options
      </code>
    </td>
    
    <td>
      Called before <code>
        @nuxt/cli
      </code>
      
       writes TypeScript configuration files (<code>
        .nuxt/tsconfig.app.json
      </code>
      
      , <code>
        .nuxt/tsconfig.server.json
      </code>
      
      , etc.) and <code>
        .nuxt/nuxt.d.ts
      </code>
      
      , allowing addition of custom references and declarations in <code>
        nuxt.d.ts
      </code>
      
      , or directly modifying the options in generated configurations
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        listen
      </code>
    </td>
    
    <td>
      <code>
        listenerServer, listener
      </code>
    </td>
    
    <td>
      Called when the dev server is loading.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        schema:extend
      </code>
    </td>
    
    <td>
      <code>
        schemas
      </code>
    </td>
    
    <td>
      Allows extending default schemas.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        schema:resolved
      </code>
    </td>
    
    <td>
      <code>
        schema
      </code>
    </td>
    
    <td>
      Allows extending resolved schema.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        schema:beforeWrite
      </code>
    </td>
    
    <td>
      <code>
        schema
      </code>
    </td>
    
    <td>
      Called before writing the given schema.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        schema:written
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Called after the schema is written.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        vite:extend
      </code>
    </td>
    
    <td>
      <code>
        viteBuildContext
      </code>
    </td>
    
    <td>
      Allows extending Vite default context.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        vite:extendConfig
      </code>
    </td>
    
    <td>
      <code>
        viteInlineConfig, env
      </code>
    </td>
    
    <td>
      Allows extending Vite default config. <strong>
        Deprecated in Nuxt 5+.
      </strong>
      
       In Nuxt 5, this operates on a shared configuration rather than separate client/server configs.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        vite:configResolved
      </code>
    </td>
    
    <td>
      <code>
        viteInlineConfig, env
      </code>
    </td>
    
    <td>
      Allows reading the resolved Vite config. <strong>
        Deprecated in Nuxt 5+.
      </strong>
      
       In Nuxt 5, this operates on a shared configuration rather than separate client/server configs.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        vite:serverCreated
      </code>
    </td>
    
    <td>
      <code>
        viteServer, env
      </code>
    </td>
    
    <td>
      Called when the Vite server is created.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        vite:compiled
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Called after Vite server is compiled.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        webpack:config
      </code>
    </td>
    
    <td>
      <code>
        webpackConfigs
      </code>
    </td>
    
    <td>
      Called before configuring the webpack compiler.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        webpack:configResolved
      </code>
    </td>
    
    <td>
      <code>
        webpackConfigs
      </code>
    </td>
    
    <td>
      Allows reading the resolved webpack config.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        webpack:compile
      </code>
    </td>
    
    <td>
      <code>
        options
      </code>
    </td>
    
    <td>
      Called right before compilation.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        webpack:compiled
      </code>
    </td>
    
    <td>
      <code>
        options
      </code>
    </td>
    
    <td>
      Called after resources are loaded.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        webpack:change
      </code>
    </td>
    
    <td>
      <code>
        shortPath
      </code>
    </td>
    
    <td>
      Called on <code>
        change
      </code>
      
       on WebpackBar.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        webpack:error
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Called on <code>
        done
      </code>
      
       if has errors on WebpackBar.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        webpack:done
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Called on <code>
        allDone
      </code>
      
       on WebpackBar.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        webpack:progress
      </code>
    </td>
    
    <td>
      <code>
        statesArray
      </code>
    </td>
    
    <td>
      Called on <code>
        progress
      </code>
      
       on WebpackBar.
    </td>
  </tr>
</tbody>
</table>

## Nitro App Hooks (runtime, server-side)

See [Nitro](https://nitro.build/guide/plugins#available-hooks) for all available hooks.

<table>
<thead>
  <tr>
    <th>
      Hook
    </th>
    
    <th>
      Arguments
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Types
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        dev:ssr-logs
      </code>
    </td>
    
    <td>
      <code>
        { path, logs }
      </code>
    </td>
    
    <td>
      Server
    </td>
    
    <td>
      Called at the end of a request cycle with an array of server-side logs.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        render:response
      </code>
    </td>
    
    <td>
      <code>
        response, { event }
      </code>
    </td>
    
    <td>
      Called before sending the response.
    </td>
    
    <td>
      <a href="https://github.com/nuxt/nuxt/blob/71ef8bd3ff207fd51c2ca18d5a8c7140476780c7/packages/nuxt/src/core/runtime/nitro/renderer.ts#L24" rel="nofollow">
        response
      </a>
      
      , <a href="https://github.com/h3js/h3/blob/f6ceb5581043dc4d8b6eab91e9be4531e0c30f8e/src/types.ts#L38" rel="nofollow">
        event
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        render:html
      </code>
    </td>
    
    <td>
      <code>
        html, { event }
      </code>
    </td>
    
    <td>
      Called before constructing the HTML.
    </td>
    
    <td>
      <a href="https://github.com/nuxt/nuxt/blob/71ef8bd3ff207fd51c2ca18d5a8c7140476780c7/packages/nuxt/src/core/runtime/nitro/renderer.ts#L15" rel="nofollow">
        html
      </a>
      
      , <a href="https://github.com/h3js/h3/blob/f6ceb5581043dc4d8b6eab91e9be4531e0c30f8e/src/types.ts#L38" rel="nofollow">
        event
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        render:island
      </code>
    </td>
    
    <td>
      <code>
        islandResponse, { event, islandContext }
      </code>
    </td>
    
    <td>
      Called before constructing the island HTML.
    </td>
    
    <td>
      <a href="https://github.com/nuxt/nuxt/blob/e50cabfed1984c341af0d0c056a325a8aec26980/packages/nuxt/src/core/runtime/nitro/renderer.ts#L28" rel="nofollow">
        islandResponse
      </a>
      
      , <a href="https://github.com/h3js/h3/blob/f6ceb5581043dc4d8b6eab91e9be4531e0c30f8e/src/types.ts#L38" rel="nofollow">
        event
      </a>
      
      , <a href="https://github.com/nuxt/nuxt/blob/e50cabfed1984c341af0d0c056a325a8aec26980/packages/nuxt/src/core/runtime/nitro/renderer.ts#L38" rel="nofollow">
        islandContext
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        close
      </code>
    </td>
    
    <td>
      -
    </td>
    
    <td>
      Called when Nitro is closed.
    </td>
    
    <td>
      -
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        error
      </code>
    </td>
    
    <td>
      <code>
        error, { event? }
      </code>
    </td>
    
    <td>
      Called when an error occurs.
    </td>
    
    <td>
      <a href="https://github.com/nitrojs/nitro/blob/d20ffcbd16fc4003b774445e1a01e698c2bb078a/src/types/runtime/nitro.ts#L48" rel="nofollow">
        error
      </a>
      
      , <a href="https://github.com/h3js/h3/blob/f6ceb5581043dc4d8b6eab91e9be4531e0c30f8e/src/types.ts#L38" rel="nofollow">
        event
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        request
      </code>
    </td>
    
    <td>
      <code>
        event
      </code>
    </td>
    
    <td>
      Called when a request is received.
    </td>
    
    <td>
      <a href="https://github.com/h3js/h3/blob/f6ceb5581043dc4d8b6eab91e9be4531e0c30f8e/src/types.ts#L38" rel="nofollow">
        event
      </a>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        beforeResponse
      </code>
    </td>
    
    <td>
      <code>
        event, { body }
      </code>
    </td>
    
    <td>
      Called before sending the response.
    </td>
    
    <td>
      <a href="https://github.com/h3js/h3/blob/f6ceb5581043dc4d8b6eab91e9be4531e0c30f8e/src/types.ts#L38" rel="nofollow">
        event
      </a>
      
      , unknown
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        afterResponse
      </code>
    </td>
    
    <td>
      <code>
        event, { body }
      </code>
    </td>
    
    <td>
      Called after sending the response.
    </td>
    
    <td>
      <a href="https://github.com/h3js/h3/blob/f6ceb5581043dc4d8b6eab91e9be4531e0c30f8e/src/types.ts#L38" rel="nofollow">
        event
      </a>
      
      , unknown
    </td>
  </tr>
</tbody>
</table>

## Import Meta

# Import meta

> Understand where your code is running using `import.meta`.

## The `import.meta` object

With ES modules you can obtain some metadata from the code that imports or compiles your ES-module.
This is done through `import.meta`, which is an object that provides your code with this information.
Throughout the Nuxt documentation you may see snippets that use this already to figure out whether the
code is currently running on the client or server side.

<read-more to="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta">

Read more about `import.meta`.

</read-more>

## Runtime (App) Properties

These values are statically injected and can be used for tree-shaking your runtime code.

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
        import.meta.client
      </code>
    </td>
    
    <td>
      boolean
    </td>
    
    <td>
      True when evaluated on the client side.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        import.meta.browser
      </code>
    </td>
    
    <td>
      boolean
    </td>
    
    <td>
      True when evaluated on the client side.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        import.meta.server
      </code>
    </td>
    
    <td>
      boolean
    </td>
    
    <td>
      True when evaluated on the server side.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        import.meta.nitro
      </code>
    </td>
    
    <td>
      boolean
    </td>
    
    <td>
      True when evaluated on the server side.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        import.meta.dev
      </code>
    </td>
    
    <td>
      boolean
    </td>
    
    <td>
      True when running the Nuxt dev server.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        import.meta.envName
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      The current Nuxt environment name, including custom values passed via <code>
        --envName
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        import.meta.test
      </code>
    </td>
    
    <td>
      boolean
    </td>
    
    <td>
      True when running in a test context.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        import.meta.prerender
      </code>
    </td>
    
    <td>
      boolean
    </td>
    
    <td>
      True when rendering HTML on the server in the prerender stage of your build.
    </td>
  </tr>
</tbody>
</table>

## Builder Properties

These values are available both in modules and in your `nuxt.config`.

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
        import.meta.env
      </code>
    </td>
    
    <td>
      object
    </td>
    
    <td>
      Equals <code>
        process.env
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        import.meta.url
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      Resolvable path for the current file.
    </td>
  </tr>
</tbody>
</table>

## Examples

### Using `import.meta.url` to resolve files within modules

```ts [modules/my-module/index.ts]
import { createResolver } from 'nuxt/kit'

// Resolve relative from the current file
const resolver = createResolver(import.meta.url)

export default defineNuxtModule({
  meta: { name: 'myModule' },
  setup () {
    addComponent({
      name: 'MyModuleComponent',
      // Resolves to '/modules/my-module/components/MyModuleComponent.vue'
      filePath: resolver.resolve('./components/MyModuleComponent.vue'),
    })
  },
})
```

## Nuxt Config

# Nuxt Configuration

> Discover all the options you can use in your nuxt.config.ts file.

## alias

You can improve your DX by defining additional aliases to access custom directories within your JavaScript and CSS.

- **Type**: `object`
- **Default**

```json
{
  "~": "/<rootDir>/app",
  "@": "/<rootDir>/app",
  "~~": "/<rootDir>",
  "@@": "/<rootDir>",
  "#shared": "/<rootDir>/shared",
  "#server": "/<rootDir>/server",
  "assets": "/<rootDir>/app/assets",
  "public": "/<rootDir>/public",
  "#build": "/<rootDir>/.nuxt",
  "#internal/nuxt/paths": "/<rootDir>/.nuxt/paths.mjs"
}
```

<callout>

**Note**: Within a webpack context (image sources, CSS - but not JavaScript) you *must* access
your alias by prefixing it with `~`.

</callout>

<callout>

**Note**: These aliases will be automatically added to the generated TypeScript configurations (`.nuxt/tsconfig.app.json`, `.nuxt/tsconfig.server.json`, etc.) so you can get full type support and path auto-complete. In case you need to extend options provided by the generated configurations further, make sure to add them here or within the `typescript.tsConfig` property in `nuxt.config`.

</callout>

**Example**:

```ts
import { fileURLToPath } from 'node:url'

export default defineNuxtConfig({
  alias: {
    'images': fileURLToPath(new URL('./assets/images', import.meta.url)),
    'style': fileURLToPath(new URL('./assets/style', import.meta.url)),
    'data': fileURLToPath(new URL('./assets/other/data', import.meta.url)),
  },
})
```

```html
<template>
  <img src="~images/main-bg.jpg">
</template>

<script>
import data from 'data/test.json'
</script>

<style>
// Uncomment the below
//@import '~style/variables.scss';
//@import '~style/utils.scss';
//@import '~style/base.scss';
body {
  background-image: url('~images/main-bg.jpg');
}
</style>
```

## analyzeDir

The directory where Nuxt will store the generated files when running `nuxt analyze`.

If a relative path is specified, it will be relative to your `rootDir`.

- **Type**: `string`
- **Default:** `"/<rootDir>/.nuxt/analyze"`

## app

Nuxt App configuration.

### `baseURL`

The base path of your Nuxt application.

For example:

- **Type**: `string`
- **Default:** `"/"`

**Example**:

```ts
export default defineNuxtConfig({
  app: {
    baseURL: '/prefix/',
  },
})
```

This can also be set at runtime by setting the NUXT_APP_BASE_URL environment variable.

**Example**:

```bash
NUXT_APP_BASE_URL=/prefix/ node .output/server/index.mjs
```

### `buildAssetsDir`

The folder name for the built site assets, relative to `baseURL` (or `cdnURL` if set). This is set at build time and should not be customized at runtime.

- **Type**: `string`
- **Default:** `"/_nuxt/"`

### `cdnURL`

An absolute URL to serve the public folder from (production-only).

For example:

- **Type**: `string`
- **Default:** `""`

**Example**:

```ts
export default defineNuxtConfig({
  app: {
    cdnURL: 'https://mycdn.org/',
  },
})
```

This can be set to a different value at runtime by setting the `NUXT_APP_CDN_URL` environment variable.

**Example**:

```bash
NUXT_APP_CDN_URL=https://mycdn.org/ node .output/server/index.mjs
```

### `head`

Set default configuration for `<head>` on every page.

- **Type**: `object`
- **Default**

```json
{
  "meta": [
    {
      "name": "viewport",
      "content": "width=device-width, initial-scale=1"
    },
    {
      "charset": "utf-8"
    }
  ],
  "link": [],
  "style": [],
  "script": [],
  "noscript": []
}
```

**Example**:

```ts
export default defineNuxtConfig({
  app: {
    head: {
      meta: [
      // <meta name="viewport" content="width=device-width, initial-scale=1">
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      ],
      script: [
      // <script src="https://myawesome-lib.js"></script>
        { src: 'https://awesome-lib.js' },
      ],
      link: [
      // <link rel="stylesheet" href="https://myawesome-lib.css">
        { rel: 'stylesheet', href: 'https://awesome-lib.css' },
      ],
      // please note that this is an area that is likely to change
      style: [
      // <style>:root { color: red }</style>
        { textContent: ':root { color: red }' },
      ],
      noscript: [
      // <noscript>JavaScript is required</noscript>
        { textContent: 'JavaScript is required' },
      ],
    },
  },
})
```

### `keepalive`

Default values for KeepAlive configuration between pages.

This can be overridden with `definePageMeta` on an individual page. Only JSON-serializable values are allowed.

- **Type**: `boolean`
- **Default:** `false`

**See**: [Vue KeepAlive](https://vuejs.org/api/built-in-components#keepalive)

### `layoutTransition`

Default values for layout transitions.

This can be overridden with `definePageMeta` on an individual page. Only JSON-serializable values are allowed.

- **Type**: `boolean | TransitionProps`
- **Default:** `false`

**See**: [Vue Transition docs](https://vuejs.org/api/built-in-components#transition)

### `pageTransition`

Default values for page transitions.

This can be overridden with `definePageMeta` on an individual page. Only JSON-serializable values are allowed.

- **Type**: `boolean | TransitionProps`
- **Default:** `false`

**See**: [Vue Transition docs](https://vuejs.org/api/built-in-components#transition)

### `rootAttrs`

Customize Nuxt root element id.

- **Type**: `object`
- **Default**

```json
{
  "id": "__nuxt"
}
```

### `rootId`

Customize Nuxt root element id.

- **Type**: `string`
- **Default:** `"__nuxt"`

### `rootTag`

Customize Nuxt root element tag.

- **Type**: `string`
- **Default:** `"div"`

### `spaLoaderAttrs`

Customize Nuxt SPA loading template element attributes.

- **Type**: `object`
- **Default:**

```json
{
"id": "__nuxt-loader"
}
```

#### `id`

- **Type**: `string`
- **Default:** `"__nuxt-loader"`

### `spaLoaderTag`

Customize Nuxt SpaLoader element tag.

- **Type**: `string`
- **Default:** `"div"`

### `teleportAttrs`

Customize Nuxt Teleport element attributes.

- **Type**: `object`
- **Default**

```json
{
  "id": "teleports"
}
```

### `teleportId`

Customize Nuxt Teleport element id.

- **Type**: `string`
- **Default:** `"teleports"`

### `teleportTag`

Customize Nuxt Teleport element tag.

- **Type**: `string`
- **Default:** `"div"`

### `viewTransition`

Default values for view transitions.

This only has an effect when **experimental** support for View Transitions is [enabled in your nuxt.config file](/docs/4.x/getting-started/transitions#view-transitions-api-experimental).
This can be overridden with `definePageMeta` on an individual page.

- **Type**: `boolean`
- **Default:** `false`

**See**: [Nuxt View Transition API docs](/docs/4.x/getting-started/transitions#view-transitions-api-experimental)

## appConfig

Additional app configuration

For programmatic usage and type support, you can directly provide app config with this option. It will be merged with `app.config` file as default value.

### `nuxt`

## appId

For multi-app projects, the unique id of the Nuxt application.

Defaults to `nuxt-app`.

- **Type**: `string`
- **Default:** `"nuxt-app"`

## build

Shared build configuration.

### `analyze`

Nuxt allows visualizing your bundles and how to optimize them.

Set to `true` to enable bundle analysis, or pass an object with options: [for webpack](https://github.com/webpack/webpack-bundle-analyzer#options-for-plugin) or [for vite](https://github.com/btd/rollup-plugin-visualizer#options).

- **Type**: `object`
- **Default**

```json
{
  "template": "treemap",
  "projectRoot": "/<rootDir>",
  "filename": "/<rootDir>/.nuxt/analyze/{name}.html"
}
```

**Example**:

```ts
export default defineNuxtConfig({
  analyze: {
    analyzerMode: 'static',
  },
})
```

### `templates`

It is recommended to use `addTemplate` from `@nuxt/kit` instead of this option.

- **Type**: `array`

**Example**:

```ts
export default defineNuxtConfig({
  build: {
    templates: [
      {
        src: '~~/modules/support/plugin.js', // `src` can be absolute or relative
        dst: 'support.js', // `dst` is relative to project `.nuxt` dir
      },
    ],
  },
})
```

### `transpile`

If you want to transpile specific dependencies with Babel, you can add them here. Each item in transpile can be a package name, a function, a string or regex object matching the dependency's file name.

You can also use a function to conditionally transpile. The function will receive an object ({ isDev, isServer, isClient, isModern, isLegacy }).

- **Type**: `array`

**Example**:

```ts
export default defineNuxtConfig({
  build: {
    transpile: [({ isLegacy }) => isLegacy && 'ky'],
  },
})
```

## buildDir

Define the directory where your built Nuxt files will be placed.

Many tools assume that `.nuxt` is a hidden directory (because it starts with a `.`). If that is a problem, you can use this option to prevent that.

- **Type**: `string`
- **Default:** `"/<rootDir>/.nuxt"`

**Example**:

```ts
export default defineNuxtConfig({
  buildDir: 'nuxt-build',
})
```

## buildId

A unique identifier matching the build. This may contain the hash of the current state of the project.

- **Type**: `string`
- **Default:** `"4a2e2d30-418f-41df-8e58-ed5df06de7fd"`

## builder

The builder to use for bundling the Vue part of your application.

Nuxt supports multiple builders for the client-side application. By default, Vite is used, but you can switch to webpack, Rspack, or even provide a custom builder implementation.

- **Type**: `'vite' | 'webpack' | 'rspack' | string | { bundle: (nuxt: Nuxt) => Promise<void> }`
- **Default:** `"@nuxt/vite-builder"`

**Using supported builders:**

```ts
export default defineNuxtConfig({
  // default - uses @nuxt/vite-builder
  // builder: 'vite',

  // uses @nuxt/webpack-builder
  // builder: 'webpack',

  // uses @nuxt/rspack-builder
  builder: 'rspack',
})
```

If you are using `webpack` or `rspack` you will need to make sure `@nuxt/webpack-builder` or `@nuxt/rspack-builder` is explicitly installed in your project.

**Using a custom builder object:**

You can provide a custom builder by passing an object with a `bundle` function:

```ts
export default defineNuxtConfig({
  builder: {
    async bundle (nuxt) {
      const entry = await resolvePath(resolve(nuxt.options.appDir, 'entry'))

      // Build client and server bundles
      await buildClient(nuxt, entry)
      if (nuxt.options.ssr) {
        await buildServer(nuxt, entry)
      }

      // ... it's a bit more complicated than that, of course!
    },
  },
})
```

**Creating a custom builder package:**

To create a custom builder as a separate package, it should export a `bundle` function. You can then specify the package name in your `nuxt.config.ts`:

```ts
export default defineNuxtConfig({
  builder: 'my-custom-builder',
})
```

## compatibilityDate

Specify a compatibility date for your app.

This is used to control the behavior of presets in Nitro, Nuxt Image and other modules that may change behavior without a major version bump.
We plan to improve the tooling around this feature in the future.

## components

Configure Nuxt component auto-registration.

Any components in the directories configured here can be used throughout your pages, layouts (and other components) without needing to explicitly import them.

- **Type**: `object`
- **Default**

```json
{
  "dirs": [
    {
      "path": "~/components/global",
      "global": true
    },
    "~/components"
  ]
}
```

**See**: [`app/components/` directory documentation](/docs/4.x/directory-structure/app/components)

## css

You can define the CSS files/modules/libraries you want to set globally (included in every page).

Nuxt will automatically guess the file type by its extension and use the appropriate pre-processor. You will still need to install the required loader if you need to use them.

- **Type**: `array`

**Example**:

```ts
export default defineNuxtConfig({
  css: [
  // Load a Node.js module directly (here it's a Sass file).
    'bulma',
    // CSS file in the project
    '~/assets/css/main.css',
    // SCSS file in the project
    '~/assets/css/main.scss',
  ],
})
```

## debug

Set to `true` to enable debug mode.

At the moment, it prints out hook names and timings on the server, and logs hook arguments as well in the browser.
You can also set this to an object to enable specific debug options.

- **Type**: `boolean`
- **Default:** `false`

## dev

Whether Nuxt is running in development mode.

Normally, you should not need to set this.

- **Type**: `boolean`
- **Default:** `false`

## devServer

### `cors`

Set CORS options for the dev server

#### `origin`

- **Type**: `array`
- **Default**

```json
[
  {}
]
```

### `host`

Dev server listening host

### `https`

Whether to enable HTTPS.

- **Type**: `boolean`
- **Default:** `false`

**Example**:

```ts
export default defineNuxtConfig({
  devServer: {
    https: {
      key: './server.key',
      cert: './server.crt',
    },
  },
})
```

### `loadingTemplate`

Template to show a loading screen

- **Type**: `function`

### `port`

Dev server listening port

- **Type**: `number`
- **Default:** `3000`

### `url`

Listening dev server URL.

This should not be set directly as it will always be overridden by the dev server with the full URL (for module and internal use).

- **Type**: `string`
- **Default:** `"http://localhost:3000"`

## devServerHandlers

Nitro development-only server handlers.

- **Type**: `array`

**See**: [Nitro server routes documentation](https://nitro.build/guide/routing)

## devtools

Enable Nuxt DevTools for development.

Breaking changes for devtools might not reflect on the version of Nuxt.

**See**:  [Nuxt DevTools](https://devtools.nuxt.com/) for more information.

## dir

Customize default directory structure used by Nuxt.

It is better to stick with defaults unless needed.

### `app`

- **Type**: `string`
- **Default:** `"app"`

### `assets`

The assets directory (aliased as `~assets` in your build).

- **Type**: `string`
- **Default:** `"app/assets"`

### `layouts`

The layouts directory, each file of which will be auto-registered as a Nuxt layout.

- **Type**: `string`
- **Default:** `"app/layouts"`

### `middleware`

The middleware directory, each file of which will be auto-registered as a Nuxt middleware.

- **Type**: `string`
- **Default:** `"app/middleware"`

### `modules`

The modules directory, each file in which will be auto-registered as a Nuxt module.

- **Type**: `string`
- **Default:** `"modules"`

### `pages`

The directory which will be processed to auto-generate your application page routes.

- **Type**: `string`
- **Default:** `"app/pages"`

### `plugins`

The plugins directory, each file of which will be auto-registered as a Nuxt plugin.

- **Type**: `string`
- **Default:** `"app/plugins"`

### `public`

The directory containing your static files, which will be directly accessible via the Nuxt server and copied across into your `dist` folder when your app is generated.

- **Type**: `string`
- **Default:** `"public"`

### `shared`

The shared directory. This directory is shared between the app and the server.

- **Type**: `string`
- **Default:** `"shared"`

## esbuild

### `options`

Configure shared esbuild options used within Nuxt and passed to other builders, such as Vite or webpack.

#### `jsxFactory`

- **Type**: `string`
- **Default:** `"h"`

#### `jsxFragment`

- **Type**: `string`
- **Default:** `"Fragment"`

#### `target`

- **Type**: `string`
- **Default:** `"esnext"`

#### `tsconfigRaw`

- **Type**: `object`

## experimental

<read-more to="/docs/4.x/guide/going-further/experimental-features">

Learn more about Nuxt's experimental features.

</read-more>

## extends

Extend project from multiple local or remote sources.

Value should be either a string or array of strings pointing to source directories or config path relative to current config.
You can use `github:`, `gh:` `gitlab:` or `bitbucket:`

**See**: [`c12` docs on extending config layers](https://github.com/unjs/c12#extending-config-layer-from-remote-sources)

**See**: [`giget` documentation](https://github.com/unjs/giget)

## extensions

The extensions that should be resolved by the Nuxt resolver.

- **Type**: `array`
- **Default**

```json
[
  ".js",
  ".jsx",
  ".mjs",
  ".ts",
  ".tsx",
  ".vue"
]
```

## features

<read-more to="/docs/4.x/guide/going-further/features#features">

Learn more about Nuxt's opt-in features.

</read-more>

## future

<read-more to="/docs/4.x/guide/going-further/features#features">

Learn more about opting-in to new features that will become default in a future (possibly major) version of the framework.

</read-more>

## hooks

Hooks are listeners to Nuxt events that are typically used in modules, but are also available in `nuxt.config`.

Internally, hooks follow a naming pattern using colons (e.g., build:done).
For ease of configuration, you can also structure them as an hierarchical object in `nuxt.config` (as below).

**Example**:

```ts
import fs from 'node:fs'
import path from 'node:path'

export default defineNuxtConfig({
  hooks: {
    build: {
      done (builder) {
        const extraFilePath = path.join(
          builder.nuxt.options.buildDir,
          'extra-file',
        )
        fs.writeFileSync(extraFilePath, 'Something extra')
      },
    },
  },
})
```

## ignore

More customizable than `ignorePrefix`: all files matching glob patterns specified inside the `ignore` array will be ignored in building.

- **Type**: `array`
- **Default**

```json
[
  "**/*.stories.{js,cts,mts,ts,jsx,tsx}",
  "**/*.{spec,test}.{js,cts,mts,ts,jsx,tsx}",
  "**/*.d.{cts,mts,ts}",
  "**/*.d.vue.{cts,mts,ts}",
  "**/.{pnpm-store,vercel,netlify,output,git,cache,data}",
  "**/*.sock",
  ".nuxt/analyze",
  ".nuxt",
  "**/-*.*"
]
```

## ignoreOptions

Pass options directly to `node-ignore` (which is used by Nuxt to ignore files).

**See**: [node-ignore](https://github.com/kaelzhang/node-ignore)

**Example**:

```ts
export default defineNuxtConfig({
  ignoreOptions: {
    ignorecase: false,
  },
})
```

## ignorePrefix

Any file in `app/pages/`, `app/layouts/`, `app/middleware/`, and `public/` directories will be ignored during the build process if its filename starts with the prefix specified by `ignorePrefix`. This is intended to prevent certain files from being processed or served in the built application. By default, the `ignorePrefix` is set to '-', ignoring any files starting with '-'.

- **Type**: `string`
- **Default:** `"-"`

## imports

Configure how Nuxt auto-imports composables into your application.

**See**: [Nuxt documentation](/docs/4.x/directory-structure/app/composables)

### `dirs`

An array of custom directories that will be auto-imported. Note that this option will not override the default directories (~/composables, ~/utils).

- **Type**: `array`

**Example**:

```ts
export default defineNuxtConfig({
  imports: {
  // Auto-import pinia stores defined in `~/stores`
    dirs: ['stores'],
  },
})
```

### `global`

- **Type**: `boolean`
- **Default:** `false`

### `scan`

Whether to scan your `app/composables/` and `app/utils/` directories for composables to auto-import. Auto-imports registered by Nuxt or other modules, such as imports from `vue` or `nuxt`, will still be enabled.

- **Type**: `boolean`
- **Default:** `true`

## logLevel

Log level when building logs.

Defaults to 'silent' when running in CI or when a TTY is not available. This option is then used as 'silent' in Vite and 'none' in webpack

- **Type**: `string`
- **Default:** `"info"`

## modules

Modules are Nuxt extensions which can extend its core functionality and add endless integrations.

Each module is either a string (which can refer to a package, or be a path to a file), a tuple with the module as first string and the options as a second object, or an inline module function.
Nuxt tries to resolve each item in the modules array using node require path (in `node_modules`) and then will be resolved from project `rootDir` if `~~` alias is used.

- **Type**: `array`

<callout>

**Note**: Modules are executed sequentially so the order is important. First, the modules defined in `nuxt.config.ts` are loaded. Then, modules found in the `modules/`
directory are executed, and they load in alphabetical order.

</callout>

**Example**:

```ts
export default defineNuxtConfig({
  modules: [
  // Using package name
    '@nuxt/scripts',
    // Relative to your project rootDir
    '~~/custom-modules/awesome.js',
    // Providing options
    ['@nuxtjs/google-analytics', { ua: 'X1234567' }],
    // Inline definition
    function () {},
  ],
})
```

## modulesDir

Used to set the modules directories for path resolving (for example, webpack's `resolveLoading`, `nodeExternals` and `postcss`).

The configuration path is relative to `options.rootDir` (default is current working directory).
Setting this field may be necessary if your project is organized as a yarn workspace-styled mono-repository.

- **Type**: `array`
- **Default**

```json
[
  "/<rootDir>/node_modules"
]
```

**Example**:

```ts
export default defineNuxtConfig({
  modulesDir: ['../../node_modules'],
})
```

## nitro

Configuration for Nitro.

**See**: [Nitro configuration docs](https://nitro.build/config)

### `routeRules`

- **Type**: `object`

### `runtimeConfig`

- **Type**: `object`
- **Default**

```json
{
  "public": {},
  "app": {
    "buildId": "4a2e2d30-418f-41df-8e58-ed5df06de7fd",
    "baseURL": "/",
    "buildAssetsDir": "/_nuxt/",
    "cdnURL": ""
  },
  "nitro": {
    "envPrefix": "NUXT_"
  }
}
```

## optimization

Build time optimization configuration.

### `asyncTransforms`

Options passed directly to the transformer from `unctx` that preserves async context after `await`.

#### `asyncFunctions`

- **Type**: `array`
- **Default**

```json
[
  "defineNuxtPlugin",
  "defineNuxtRouteMiddleware"
]
```

#### `objectDefinitions`

##### `defineNuxtComponent`

- **Type**: `array`
- **Default**

```json
[
  "asyncData",
  "setup"
]
```

##### `defineNuxtPlugin`

- **Type**: `array`
- **Default**

```json
[
  "setup"
]
```

##### `definePageMeta`

- **Type**: `array`
- **Default**

```json
[
  "middleware",
  "validate"
]
```

### `keyedComposables`

Functions to inject a key for.

As long as the number of arguments passed to the function is less than `argumentLength`, an additional magic string will be injected as the last argument. This key is stable between SSR and client-side hydration. You will need to take steps to handle this additional key.
The key is unique based on the location of the function being invoked within the file.

<read-more to="/docs/4.x/guide/modules/recipes-basics#add-keyed-functions">

Learn more about keyed functions.

</read-more>

- **Type**: `array`
- **Default**

```json
[
  {
    "name": "callOnce",
    "argumentLength": 3,
    "source": "#app/composables/once"
  },
  {
    "name": "defineNuxtComponent",
    "argumentLength": 2,
    "source": "#app/composables/component"
  },
  {
    "name": "useState",
    "argumentLength": 2,
    "source": "#app/composables/state"
  },
  {
    "name": "useFetch",
    "argumentLength": 3,
    "source": "#app/composables/fetch"
  },
  {
    "name": "useAsyncData",
    "argumentLength": 3,
    "source": "#app/composables/asyncData"
  },
  {
    "name": "useLazyAsyncData",
    "argumentLength": 3,
    "source": "#app/composables/asyncData"
  },
  {
    "name": "useLazyFetch",
    "argumentLength": 3,
    "source": "#app/composables/fetch"
  }
]
```

### `treeShake`

Tree shake code from specific builds.

#### `composables`

Tree shake composables from the server or client builds.

**Example**:

```ts
export default defineNuxtConfig({
  optimization: {
    treeShake: {
      composables: {
        client: { vue: ['onMounted'] },
        server: { vue: ['onServerPrefetch'] },
      },
    },
  },
})
```

##### `client`

- **Type**: `object`
- **Default**

```json
{
  "vue": [
    "onRenderTracked",
    "onRenderTriggered",
    "onServerPrefetch"
  ],
  "#app": [
    "definePayloadReducer",
    "definePageMeta",
    "onPrehydrate"
  ]
}
```

##### `server`

- **Type**: `object`
- **Default**

```json
{
  "vue": [
    "onMounted",
    "onUpdated",
    "onUnmounted",
    "onBeforeMount",
    "onBeforeUpdate",
    "onBeforeUnmount",
    "onRenderTracked",
    "onRenderTriggered",
    "onActivated",
    "onDeactivated"
  ],
  "#app": [
    "definePayloadReviver",
    "definePageMeta"
  ]
}
```

## pages

Whether to use the vue-router integration in Nuxt 3. If you do not provide a value it will be enabled if you have a `app/pages/` directory in your source folder.

Additionally, you can provide a glob pattern or an array of patterns to scan only certain files for pages.

**Example**:

```ts
export default defineNuxtConfig({
  pages: {
    pattern: ['**/*/*.vue', '!**/*.spec.*'],
  },
})
```

## plugins

An array of nuxt app plugins.

Each plugin can be a string (which can be an absolute or relative path to a file). If it ends with `.client` or `.server` then it will be automatically loaded only in the appropriate context.
It can also be an object with `src` and `mode` keys.

- **Type**: `array`

<callout>

**Note**: Plugins are also auto-registered from the `~/plugins` directory
and these plugins do not need to be listed in `nuxt.config` unless you
need to customize their order. All plugins are deduplicated by their src path.

</callout>

**See**: [`app/plugins/` directory documentation](/docs/4.x/directory-structure/app/plugins)

**Example**:

```ts
export default defineNuxtConfig({
  plugins: [
    '~/custom-plugins/foo.client.js', // only in client side
    '~/custom-plugins/bar.server.js', // only in server side
    '~/custom-plugins/baz.js', // both client & server
    { src: '~/custom-plugins/both-sides.js' },
    { src: '~/custom-plugins/client-only.js', mode: 'client' }, // only on client side
    { src: '~/custom-plugins/server-only.js', mode: 'server' }, // only on server side
  ],
})
```

## postcss

### `order`

A strategy for ordering PostCSS plugins.

- **Type**: `function`

### `plugins`

Options for configuring PostCSS plugins.

**See**: [PostCSS docs](https://postcss.org/)

#### `autoprefixer`

Plugin to parse CSS and add vendor prefixes to CSS rules.

**See**: [`autoprefixer`](https://github.com/postcss/autoprefixer)

#### `cssnano`

- **Type**: `object`

**See**: [`cssnano` configuration options](https://cssnano.github.io/cssnano/docs/config-file/#configuration-options)

## rootDir

Define the root directory of your application.

This property can be overwritten (for example, running `nuxt ./my-app/` will set the `rootDir` to the absolute path of `./my-app/` from the current/working directory.
It is normally not needed to configure this option.

- **Type**: `string`
- **Default:** `"/<rootDir>"`

## routeRules

Global route options applied to matching server routes.

**Experimental**: This is an experimental feature and API may change in the future.

**See**: [Nitro route rules documentation](https://nitro.build/config#routerules)

## router

### `options`

Additional router options passed to `vue-router`. On top of the options for `vue-router`, Nuxt offers additional options to customize the router (see below).

<callout>

**Note**: Only JSON serializable options should be passed by Nuxt config.
For more control, you can use an `router.options.ts` file.

</callout>

**See**: [Vue Router documentation](https://router.vuejs.org/api/interfaces/routeroptions)

#### `hashMode`

You can enable hash history in SPA mode. In this mode, router uses a hash character (#) before the actual URL that is internally passed. When enabled, the **URL is never sent to the server** and **SSR is not supported**.

- **Type**: `boolean`
- **Default:** `false`

**Default**: false

#### `scrollBehaviorType`

Customize the scroll behavior for hash links.

- **Type**: `string`
- **Default:** `"auto"`

**Default**: 'auto'

## runtimeConfig

Runtime config allows passing dynamic config and environment variables to the Nuxt app context.

The value of this object is accessible from server only using `useRuntimeConfig`.
It mainly should hold *private* configuration which is not exposed on the frontend. This could include a reference to your API secret tokens.
Anything under `public` and `app` will be exposed to the frontend as well.
Values are automatically replaced by matching env variables at runtime, e.g. setting an environment variable `NUXT_API_KEY=my-api-key NUXT_PUBLIC_BASE_URL=/foo/` would overwrite the two values in the example below.

- **Type**: `object`
- **Default**

```json
{
  "public": {},
  "app": {
    "buildId": "4a2e2d30-418f-41df-8e58-ed5df06de7fd",
    "baseURL": "/",
    "buildAssetsDir": "/_nuxt/",
    "cdnURL": ""
  }
}
```

**Example**:

```ts
export default defineNuxtConfig({
  runtimeConfig: {
    apiKey: '', // Default to an empty string, automatically set at runtime using process.env.NUXT_API_KEY
    public: {
      baseURL: '', // Exposed to the frontend as well.
    },
  },
})
```

## server

Configuration for Nuxt's server builder.

### `builder`

Specify the server builder to use for bundling the server part of your application.

By default, Nuxt uses `@nuxt/nitro-server`, which provides standalone Nitro integration. This architecture allows for different Nitro integration patterns, such as using Nitro as a Vite plugin (with the Vite Environment API).

- **Type**: `string | { bundle: (nuxt: Nuxt) => Promise<void> }`
- **Default:** `"@nuxt/nitro-server"`

<callout type="warning">

This option is intended for internal use and the API is not finalized. Please open an issue before relying on the current implementation.

</callout>

## serverDir

Define the server directory of your Nuxt application, where Nitro routes, middleware and plugins are kept.

If a relative path is specified, it will be relative to your `rootDir`.

- **Type**: `string`
- **Default:** `"/<rootDir>/server"`

## serverHandlers

Nitro server handlers.

Each handler accepts the following options:

- handler: The path to the file defining the handler. - route: The route under which the handler is available. This follows the conventions of [rou3](https://github.com/h3js/rou3). - method: The HTTP method of requests that should be handled. - middleware: Specifies whether it is a middleware handler. - lazy: Specifies whether to use lazy loading to import the handler.
- **Type**: `array`

**See**: [`server/` directory documentation](/docs/4.x/directory-structure/server)

<callout>

**Note**: Files from `server/api`, `server/middleware` and `server/routes` will be automatically registered by Nuxt.

</callout>

**Example**:

```ts
export default defineNuxtConfig({
  serverHandlers: [
    { route: '/path/foo/**:name', handler: '#server/foohandler.ts' },
  ],
})
```

## sourcemap

Configures whether and how sourcemaps are generated for server and/or client bundles.

If set to a single boolean, that value applies to both server and client. Additionally, the `'hidden'` option is also available for both server and client.
Available options for both client and server: - `true`: Generates sourcemaps and includes source references in the final bundle. - `false`: Does not generate any sourcemaps. - `'hidden'`: Generates sourcemaps but does not include references in the final bundle.

- **Type**: `object`
- **Default**

```json
{
  "server": true,
  "client": false
}
```

## spaLoadingTemplate

Boolean or a path to an HTML file with the contents of which will be inserted into any HTML page rendered with `ssr: false`.

- If it is unset, it will use `~/spa-loading-template.html` file in one of your layers, if it exists. - If it is false, no SPA loading indicator will be loaded. - If true, Nuxt will look for `~/spa-loading-template.html` file in one of your layers, or a
default Nuxt image will be used.
Some good sources for spinners are [SpinKit](https://github.com/tobiasahlin/SpinKit) or [SVG Spinners](https://icones.js.org/collection/svg-spinners).
- **Default:** `null`

**Example**: ~/spa-loading-template.html

```html
<!-- https://github.com/barelyhuman/snips/blob/dev/pages/css-loader.md -->
<div class="loader"></div>
<style>
.loader {
  display: block;
  position: fixed;
  z-index: 1031;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 18px;
  height: 18px;
  box-sizing: border-box;
  border: solid 2px transparent;
  border-top-color: #000;
  border-left-color: #000;
  border-bottom-color: #efefef;
  border-right-color: #efefef;
  border-radius: 50%;
  -webkit-animation: loader 400ms linear infinite;
  animation: loader 400ms linear infinite;
}

@-webkit-keyframes loader {
  0% {
    -webkit-transform: translate(-50%, -50%) rotate(0deg);
  }
  100% {
    -webkit-transform: translate(-50%, -50%) rotate(360deg);
  }
}
@keyframes loader {
  0% {
    transform: translate(-50%, -50%) rotate(0deg);
  }
  100% {
    transform: translate(-50%, -50%) rotate(360deg);
  }
}
</style>
```

## srcDir

Define the source directory of your Nuxt application.

If a relative path is specified, it will be relative to the `rootDir`.

- **Type**: `string`
- **Default:** `"app"` (Nuxt 4), `"."` (Nuxt 3 with `compatibilityMode: 3`)

**Example**:

```ts
export default defineNuxtConfig({
  srcDir: 'app/',
})
```

This expects the following folder structure:

```bash
-| app/
---| assets/
---| components/
---| composables/
---| layouts/
---| middleware/
---| pages/
---| plugins/
---| utils/
---| app.config.ts
---| app.vue
---| error.vue
-| server/
-| shared/
-| public/
-| modules/
-| layers/
-| nuxt.config.ts
-| package.json
```

## ssr

Whether to enable rendering of HTML - either dynamically (in server mode) or at generate time. If set to `false` generated pages will have no content.

- **Type**: `boolean`
- **Default:** `true`

## telemetry

Manually disable nuxt telemetry.

**See**: [Nuxt Telemetry](https://github.com/nuxt/telemetry) for more information.

## test

Whether your app is being unit tested.

- **Type**: `boolean`
- **Default:** `false`

## theme

Extend project from a local or remote source.

Value should be a string pointing to source directory or config path relative to current config.
You can use `github:`, `gitlab:`, `bitbucket:` or `https://` to extend from a remote git repository.

- **Type**: `string`

## typescript

Configuration for Nuxt's TypeScript integration.

### `builder`

Which builder types to include for your project.

By default Nuxt infers this based on your `builder` option (defaulting to 'vite') but you can either turn off builder environment types (with `false`) to handle this fully yourself, or opt for a 'shared' option.
The 'shared' option is advised for module authors, who will want to support multiple possible builders.

- **Default:** `null`

### `hoist`

Modules to generate deep aliases for within `compilerOptions.paths`. This does not yet support subpaths. It may be necessary when using Nuxt within a pnpm monorepo with `shamefully-hoist=false`.

- **Type**: `array`
- **Default**

```json
[
  "nitropack/types",
  "nitropack/runtime",
  "nitropack",
  "defu",
  "h3",
  "consola",
  "ofetch",
  "@unhead/vue",
  "@nuxt/devtools",
  "vue",
  "@vue/runtime-core",
  "@vue/compiler-sfc",
  "vue-router",
  "vue-router/auto-routes",
  "unplugin-vue-router/client",
  "@nuxt/schema",
  "nuxt"
]
```

### `includeWorkspace`

Include parent workspace in the Nuxt project. Mostly useful for themes and module authors.

- **Type**: `boolean`
- **Default:** `false`

### `nodeTsConfig`

You can extend the generated `.nuxt/tsconfig.node.json` TypeScript configuration using this option.

**See**: [tsconfig.json information](/docs/4.x/directory-structure/tsconfig)

### `sharedTsConfig`

You can extend the generated `.nuxt/tsconfig.shared.json` TypeScript configuration using this option.

**See**: [tsconfig.json information](/docs/4.x/directory-structure/tsconfig)

### `shim`

Generate a `*.vue` shim.

We recommend instead letting the [official Vue extension](https://marketplace.visualstudio.com/items?itemName=Vue.volar) generate accurate types for your components.
Note that you may wish to set this to `true` if you are using other libraries, such as ESLint, that are unable to understand the type of `.vue` files.

- **Type**: `boolean`
- **Default:** `false`

### `strict`

TypeScript comes with certain checks to give you more safety and analysis of your program. Once you’ve converted your codebase to TypeScript, you can start enabling these checks for greater safety. [Read More](https://www.typescriptlang.org/docs/handbook/migrating-from-javascript.html#getting-stricter-checks)

- **Type**: `boolean`
- **Default:** `true`

### `tsConfig`

You can extend the generated `.nuxt/tsconfig.app.json` TypeScript configuration using this option.

**See**: [tsconfig.json information](/docs/4.x/directory-structure/tsconfig)

### `typeCheck`

Enable build-time type checking.

If set to true, this will type check in development. You can restrict this to build-time type checking by setting it to `build`. Requires to install `typescript` and `vue-tsc` as dev dependencies.

- **Type**: `boolean`
- **Default:** `false`

**See**: [Nuxt TypeScript docs](/docs/4.x/guide/concepts/typescript)

## unhead

An object that allows us to configure the `unhead` nuxt module.

### `legacy`

Enable the legacy compatibility mode for `unhead` module. This applies the following changes: - Disables Capo.js sorting - Adds the `DeprecationsPlugin`: supports `hid`, `vmid`, `children`, `body` - Adds the `PromisesPlugin`: supports promises as input

- **Type**: `boolean`
- **Default:** `false`

**See**: [`unhead` migration documentation](https://unhead.unjs.io/docs/typescript/head/guides/get-started/migration)

**Example**:

```ts
export default defineNuxtConfig({
  unhead: {
    legacy: true,
  },
})
```

### `renderSSRHeadOptions`

An object that will be passed to `renderSSRHead` to customize the output.

- **Type**: `object`
- **Default**

```json
{
  "omitLineBreaks": false
}
```

**Example**:

```ts
export default defineNuxtConfig({
  unhead: {
    renderSSRHeadOptions: {
      omitLineBreaks: true,
    },
  },
})
```

## vite

Configuration that will be passed directly to Vite.

Top-level `vite` options are shared across both client and server environments. Use `$client` and `$server` to provide environment-specific configuration that will be merged into their respective builds.

**Example**:

```ts
export default defineNuxtConfig({
  vite: {
    $client: {
      build: {
        rollupOptions: {
          output: {
            manualChunks: {
              analytics: ['analytics-package'],
            },
          },
        },
      },
    },
    $server: {
      build: {
        sourcemap: 'inline',
      },
    },
  },
})
```

**See**: [Vite configuration docs](https://vite.dev/config/) for more information.
Please note that not all vite options are supported in Nuxt.

### `$client`

Configuration that will be merged into Vite's configuration for the client (browser) build.

- **Type**: `object`

### `$server`

Configuration that will be merged into Vite's configuration for the server build.

- **Type**: `object`

### `build`

#### `assetsDir`

- **Type**: `string`
- **Default:** `"_nuxt/"`

#### `emptyOutDir`

- **Type**: `boolean`
- **Default:** `false`

### `cacheDir`

- **Type**: `string`
- **Default:** `"/<rootDir>/node_modules/.cache/vite"`

### `clearScreen`

- **Type**: `boolean`
- **Default:** `true`

### `define`

- **Type**: `object`
- **Default**

```json
{
  "__VUE_PROD_HYDRATION_MISMATCH_DETAILS__": false,
  "process.dev": false,
  "import.meta.dev": false,
  "process.test": false,
  "import.meta.test": false
}
```

### `esbuild`

- **Type**: `object`
- **Default**

```json
{
  "target": "esnext",
  "jsxFactory": "h",
  "jsxFragment": "Fragment",
  "tsconfigRaw": {}
}
```

### `mode`

- **Type**: `string`
- **Default:** `"production"`

### `optimizeDeps`

#### `esbuildOptions`

- **Type**: `object`
- **Default**

```json
{
  "target": "esnext",
  "jsxFactory": "h",
  "jsxFragment": "Fragment",
  "tsconfigRaw": {}
}
```

#### `exclude`

- **Type**: `array`
- **Default**

```json
[
  "vue-demi"
]
```

### `publicDir`

### `resolve`

#### `extensions`

- **Type**: `array`
- **Default**

```json
[
  ".mjs",
  ".js",
  ".ts",
  ".jsx",
  ".tsx",
  ".json",
  ".vue"
]
```

### `root`

- **Type**: `string`
- **Default:** `"/<rootDir>"`

### `server`

#### `fs`

##### `allow`

- **Type**: `array`
- **Default**

```json
[
  "/<rootDir>/.nuxt",
  "/<rootDir>/app",
  "/<rootDir>",
  "/<workspaceDir>"
]
```

### `vue`

#### `features`

##### `propsDestructure`

- **Type**: `boolean`
- **Default:** `true`

#### `isProduction`

- **Type**: `boolean`
- **Default:** `true`

#### `script`

##### `hoistStatic`

#### `template`

##### `compilerOptions`

- **Type**: `object`

##### `transformAssetUrls`

- **Type**: `object`
- **Default**

```json
{
  "video": [
    "src",
    "poster"
  ],
  "source": [
    "src"
  ],
  "img": [
    "src"
  ],
  "image": [
    "xlink:href",
    "href"
  ],
  "use": [
    "xlink:href",
    "href"
  ]
}
```

### `vueJsx`

- **Type**: `object`
- **Default**

```json
{
  "isCustomElement": {
    "$schema": {
      "title": "",
      "description": "",
      "tags": []
    }
  }
}
```

## vue

Vue.js config

### `compilerOptions`

Options for the Vue compiler that will be passed at build time.

**See**: [Vue documentation](https://vuejs.org/api/application#app-config-compileroptions)

### `config`

It is possible to pass configure the Vue app globally. Only serializable options may be set in your `nuxt.config`. All other options should be set at runtime in a Nuxt plugin.

**See**: [Vue app config documentation](https://vuejs.org/api/application#app-config)

### `propsDestructure`

Enable reactive destructure for `defineProps`

- **Type**: `boolean`
- **Default:** `true`

### `runtimeCompiler`

Include Vue compiler in runtime bundle.

- **Type**: `boolean`
- **Default:** `false`

### `transformAssetUrls`

#### `image`

- **Type**: `array`
- **Default**

```json
[
  "xlink:href",
  "href"
]
```

#### `img`

- **Type**: `array`
- **Default**

```json
[
  "src"
]
```

#### `source`

- **Type**: `array`
- **Default**

```json
[
  "src"
]
```

#### `use`

- **Type**: `array`
- **Default**

```json
[
  "xlink:href",
  "href"
]
```

#### `video`

- **Type**: `array`
- **Default**

```json
[
  "src",
  "poster"
]
```

## watch

The watch property lets you define patterns that will restart the Nuxt dev server when changed.

It is an array of strings or regular expressions. Strings should be either absolute paths or relative to the `srcDir` (and the `srcDir` of any layers). Regular expressions will be matched against the path relative to the project `srcDir` (and the `srcDir` of any layers).

- **Type**: `array`

## watchers

The watchers property lets you overwrite watchers configuration in your `nuxt.config`.

### `chokidar`

Options to pass directly to `chokidar`.

**See**: [chokidar](https://github.com/paulmillr/chokidar#api)

#### `ignoreInitial`

- **Type**: `boolean`
- **Default:** `true`

#### `ignorePermissionErrors`

- **Type**: `boolean`
- **Default:** `true`

### `rewatchOnRawEvents`

An array of event types, which, when received, will cause the watcher to restart.

### `webpack`

`watchOptions` to pass directly to webpack.

**See**: [webpack@4 watch options](https://v4.webpack.js.org/configuration/watch/#watchoptions).

#### `aggregateTimeout`

- **Type**: `number`
- **Default:** `1000`

## webpack

### `aggressiveCodeRemoval`

Hard-replaces `typeof process`, `typeof window` and `typeof document` to tree-shake bundle.

- **Type**: `boolean`
- **Default:** `false`

### `analyze`

If you are using webpack, Nuxt uses `webpack-bundle-analyzer` to visualize your bundles and how to optimize them.

Set to `true` to enable bundle analysis, or pass an object with options: [for webpack](https://github.com/webpack/webpack-bundle-analyzer#options-for-plugin) or [for vite](https://github.com/btd/rollup-plugin-visualizer#options).

- **Type**: `object`
- **Default**

```json
{
  "template": "treemap",
  "projectRoot": "/<rootDir>",
  "filename": "/<rootDir>/.nuxt/analyze/{name}.html"
}
```

**Example**:

```ts
export default defineNuxtConfig({
  webpack: {
    analyze: {
      analyzerMode: 'static',
    },
  },
})
```

### `cssSourceMap`

Enables CSS source map support (defaults to `true` in development).

- **Type**: `boolean`
- **Default:** `false`

### `devMiddleware`

See [webpack-dev-middleware](https://github.com/webpack/webpack-dev-middleware) for available options.

#### `stats`

- **Type**: `string`
- **Default:** `"none"`

### `experiments`

Configure [webpack experiments](https://webpack.js.org/configuration/experiments/)

### `extractCSS`

Enables Common CSS Extraction.

Using [mini-css-extract-plugin](https://github.com/webpack/mini-css-extract-plugin) under the hood, your CSS will be extracted into separate files, usually one per component. This allows caching your CSS and JavaScript separately.

- **Type**: `boolean`
- **Default:** `true`

**Example**:

```ts
export default defineNuxtConfig({
  webpack: {
    extractCSS: true,
    // or
    extractCSS: {
      ignoreOrder: true,
    },
  },
})
```

If you want to extract all your CSS to a single file, there is a workaround for this.
However, note that it is not recommended to extract everything into a single file.
Extracting into multiple CSS files is better for caching and preload isolation. It
can also improve page performance by downloading and resolving only those resources
that are needed.

**Example**:

```ts
export default defineNuxtConfig({
  webpack: {
    extractCSS: true,
    optimization: {
      splitChunks: {
        cacheGroups: {
          styles: {
            name: 'styles',
            test: /\.(css|vue)$/,
            chunks: 'all',
            enforce: true,
          },
        },
      },
    },
  },
})
```

### `filenames`

Customize bundle filenames.

To understand a bit more about the use of manifests, take a look at [webpack documentation](https://webpack.js.org/guides/code-splitting/).

<callout>

**Note**: Be careful when using non-hashed based filenames in production
as most browsers will cache the asset and not detect the changes on first load.

</callout>

This example changes fancy chunk names to numerical ids:

**Example**:

```ts
export default defineNuxtConfig({
  webpack: {
    filenames: {
      chunk: ({ isDev }) => (isDev ? '[name].js' : '[id].[contenthash].js'),
    },
  },
})
```

#### `app`

- **Type**: `function`

#### `chunk`

- **Type**: `function`

#### `css`

- **Type**: `function`

#### `font`

- **Type**: `function`

#### `img`

- **Type**: `function`

#### `video`

- **Type**: `function`

### `friendlyErrors`

Set to `false` to disable the overlay provided by [FriendlyErrorsWebpackPlugin](https://github.com/nuxt/friendly-errors-webpack-plugin).

- **Type**: `boolean`
- **Default:** `true`

### `hotMiddleware`

See [webpack-hot-middleware](https://github.com/webpack/webpack-hot-middleware) for available options.

### `loaders`

Customize the options of Nuxt's integrated webpack loaders.

#### `css`

See [css-loader](https://github.com/webpack/css-loader) for available options.

##### `esModule`

- **Type**: `boolean`
- **Default:** `false`

##### `importLoaders`

- **Type**: `number`
- **Default:** `0`

##### `url`

###### `filter`

- **Type**: `function`

#### `cssModules`

See [css-loader](https://github.com/webpack/css-loader) for available options.

##### `esModule`

- **Type**: `boolean`
- **Default:** `false`

##### `importLoaders`

- **Type**: `number`
- **Default:** `0`

##### `modules`

###### `localIdentName`

- **Type**: `string`
- **Default:** `"[local]_[hash:base64:5]"`

##### `url`

###### `filter`

- **Type**: `function`

#### `esbuild`

- **Type**: `object`
- **Default**

```json
{
  "target": "esnext",
  "jsxFactory": "h",
  "jsxFragment": "Fragment",
  "tsconfigRaw": {}
}
```

**See**: [esbuild loader](https://github.com/privatenumber/esbuild-loader)

#### `file`

**See**: [`file-loader` Options](https://github.com/webpack/file-loader#options)

**Default**:

```json
{ "esModule": false }
```

##### `esModule`

- **Type**: `boolean`
- **Default:** `false`

##### `limit`

- **Type**: `number`
- **Default:** `1000`

#### `fontUrl`

**See**: [`file-loader` Options](https://github.com/webpack/file-loader#options)

**Default**:

```json
{ "esModule": false }
```

##### `esModule`

- **Type**: `boolean`
- **Default:** `false`

##### `limit`

- **Type**: `number`
- **Default:** `1000`

#### `imgUrl`

**See**: [`file-loader` Options](https://github.com/webpack/file-loader#options)

**Default**:

```json
{ "esModule": false }
```

##### `esModule`

- **Type**: `boolean`
- **Default:** `false`

##### `limit`

- **Type**: `number`
- **Default:** `1000`

#### `less`

- **Default**

```json
{
  "sourceMap": false
}
```

**See**: [`less-loader` Options](https://github.com/webpack/less-loader#options)

#### `pugPlain`

**See**: [`pug` options](https://pugjs.org/api/reference.html#options)

#### `sass`

**See**: [`sass-loader` Options](https://github.com/webpack/sass-loader#options)

**Default**:

```json
{
  "sassOptions": {
    "indentedSyntax": true
  }
}
```

##### `sassOptions`

###### `indentedSyntax`

- **Type**: `boolean`
- **Default:** `true`

#### `scss`

- **Default**

```json
{
  "sourceMap": false
}
```

**See**: [`sass-loader` Options](https://github.com/webpack/sass-loader#options)

#### `stylus`

- **Default**

```json
{
  "sourceMap": false
}
```

**See**: [`stylus-loader` Options](https://github.com/webpack/stylus-loader#options)

#### `vue`

See [vue-loader](https://github.com/vuejs/vue-loader) for available options.

##### `compilerOptions`

- **Type**: `object`

##### `propsDestructure`

- **Type**: `boolean`
- **Default:** `true`

##### `transformAssetUrls`

- **Type**: `object`
- **Default**

```json
{
  "video": [
    "src",
    "poster"
  ],
  "source": [
    "src"
  ],
  "img": [
    "src"
  ],
  "image": [
    "xlink:href",
    "href"
  ],
  "use": [
    "xlink:href",
    "href"
  ]
}
```

#### `vueStyle`

- **Default**

```json
{
  "sourceMap": false
}
```

### `optimization`

Configure [webpack optimization](https://webpack.js.org/configuration/optimization/).

#### `minimize`

Set minimize to `false` to disable all minimizers. (It is disabled in development by default).

- **Type**: `boolean`
- **Default:** `true`

#### `minimizer`

You can set minimizer to a customized array of plugins.

#### `runtimeChunk`

- **Type**: `string`
- **Default:** `"single"`

#### `splitChunks`

##### `automaticNameDelimiter`

- **Type**: `string`
- **Default:** `"/"`

##### `cacheGroups`

##### `chunks`

- **Type**: `string`
- **Default:** `"all"`

### `optimizeCSS`

OptimizeCSSAssets plugin options.

Defaults to true when `extractCSS` is enabled.

- **Type**: `boolean`
- **Default:** `false`

**See**: [css-minimizer-webpack-plugin documentation](https://github.com/webpack/css-minimizer-webpack-plugin).

### `plugins`

Add webpack plugins.

- **Type**: `array`

**Example**:

```ts
import webpack from 'webpack'
import { version } from './package.json'

export default defineNuxtConfig({
  webpack: {
    plugins: [
      // ...
      new webpack.DefinePlugin({
        'process.VERSION': version,
      }),
    ],
  },
})
```

### `postcss`

Customize PostCSS Loader. same options as [`postcss-loader` options](https://github.com/webpack/postcss-loader#options)

#### `postcssOptions`

##### `plugins`

- **Type**: `object`
- **Default**

```json
{
  "autoprefixer": {},
  "cssnano": {}
}
```

### `profile`

Enable the profiler in webpackbar.

It is normally enabled by CLI argument `--profile`.

- **Type**: `boolean`
- **Default:** `false`

**See**: [webpackbar](https://github.com/unjs/webpackbar#profile).

### `serverURLPolyfill`

The polyfill library to load to provide URL and URLSearchParams.

Defaults to `'url'` ([see package](https://www.npmjs.com/package/url)).

- **Type**: `string`
- **Default:** `"url"`

### `warningIgnoreFilters`

Filters to hide build warnings.

- **Type**: `array`

## workspaceDir

Define the workspace directory of your application.

Often this is used when in a monorepo setup. Nuxt will attempt to detect your workspace directory automatically, but you can override it here.
It is normally not needed to configure this option.

- **Type**: `string`
- **Default:** `"/<workspaceDir>"`