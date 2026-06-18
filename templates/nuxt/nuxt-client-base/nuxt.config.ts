// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  future: {
    compatibilityVersion: 4,
  },

  app: {
    head: {
      htmlAttrs: {
        lang: 'en',
      },
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      ],
    },
  },

  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/image',
    '@nuxtjs/sitemap',
  ],

  site: {
    url: 'https://example.com', // TODO: Update per project
    name: 'Site Name', // TODO: Update per project
    description: 'Site description', // TODO: Update per project
    defaultLocale: 'en',
    identity: {
      type: 'Organization',
    },
    indexable: true,
  },

  sitemap: {
    strictNuxtContentPaths: true,
  },

  routeRules: {
    '/': { prerender: true },
    // Add more prerender/ISR rules per project
  },

  runtimeConfig: {
    public: {
      siteName: 'Site Name', // TODO: Update per project
      siteDomain: 'https://example.com', // TODO: Update per project
    },
  },
})
