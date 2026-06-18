<script setup lang="ts">
/**
 * Default Layout
 * Sets up canonical URL and Schema.org structured data
 */

const route = useRoute()
const config = useRuntimeConfig()

// Canonical URL (no query params to avoid duplicate content)
const canonicalUrl = computed(() => {
  const baseUrl = config.public.siteDomain
  const path = route.path
  return `${baseUrl}${path}`
})

// Schema.org: Organization + WebSite
const schemaOrg = computed(() => {
  const baseUrl = config.public.siteDomain
  const siteName = config.public.siteName

  return {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'Organization',
        '@id': `${baseUrl}/#organization`,
        name: siteName,
        url: baseUrl,
        // TODO: Add logo, sameAs (social links), etc.
      },
      {
        '@type': 'WebSite',
        '@id': `${baseUrl}/#website`,
        url: baseUrl,
        name: siteName,
        publisher: {
          '@id': `${baseUrl}/#organization`,
        },
      },
    ],
  }
})

useHead({
  link: [
    {
      rel: 'canonical',
      href: canonicalUrl.value,
    },
  ],
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify(schemaOrg.value),
    },
  ],
})
</script>

<template>
  <div>
    <!-- TODO: Add header/nav component here -->
    <slot />
    <!-- TODO: Add footer component here -->
  </div>
</template>
