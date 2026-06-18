// https://nuxt.com/docs/api/configuration/nuxt-config
// nuxt-client-i18n scaffold — change only per-project values (site, domain, microCMS, locales).
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  future: {
    compatibilityVersion: 4,
  },

  app: {
    head: {
      htmlAttrs: { lang: 'en' },
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    },
  },

  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/image',
    '@nuxt/fonts',
    '@nuxtjs/i18n',
    '@nuxtjs/seo',
    '@nuxt/test-utils/module',
  ],

  i18n: {
    locales: [
      { code: 'en', language: 'en-US', name: 'English', file: 'en.json' },
      { code: 'ja', language: 'ja-JP', name: '日本語', file: 'ja.json' },
    ],
    lazy: true,
    langDir: 'i18n/locales',
    defaultLocale: 'en',
    strategy: 'prefix_except_default',
    detectBrowserLanguage: {
      useCookie: true,
      cookieKey: 'i18n_redirected',
      redirectOn: 'root',
    },
  },

  site: {
    url: 'https://example.com',
    name: 'Site Name',
    description: 'Site description',
    defaultLocale: 'en',
    identity: { type: 'Organization' },
    indexable: true,
  },

  sitemap: { strictNuxtContentPaths: true },

  routeRules: {
    '/': { prerender: true },
  },

  runtimeConfig: {
    public: {
      siteName: 'Site Name',
      siteDomain: 'https://example.com',
      microcmsApiKey: '',
    },
  },
})
