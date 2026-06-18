<script setup lang="ts">
/**
 * Default layout — canonical, hreflang, schema.org.
 * SEO and locale logic live in useSeo / i18n; no duplicated head logic.
 */
const config = useRuntimeConfig()
const siteName = config.public.siteName as string
const siteDomain = config.public.siteDomain as string

const schemaOrg = {
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'Organization',
      '@id': `${siteDomain}/#organization`,
      name: siteName,
      url: siteDomain,
    },
    {
      '@type': 'WebSite',
      '@id': `${siteDomain}/#website`,
      url: siteDomain,
      name: siteName,
      publisher: { '@id': `${siteDomain}/#organization` },
    },
  ],
}

useHead({
  script: [{ type: 'application/ld+json', children: () => JSON.stringify(schemaOrg) }],
})
</script>

<template>
  <div>
    <slot />
  </div>
</template>
