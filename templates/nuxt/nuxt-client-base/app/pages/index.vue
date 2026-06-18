<script setup lang="ts">
/**
 * Home Page
 */

const config = useRuntimeConfig()

useSeoMeta({
  title: config.public.siteName,
  description: 'Home page description', // TODO: Update per project
  ogTitle: config.public.siteName,
  ogDescription: 'Home page description', // TODO: Update per project
  ogImage: `${config.public.siteDomain}/images/og-image.png`,
  ogUrl: config.public.siteDomain,
  twitterCard: 'summary_large_image',
})
</script>

<template>
  <NuxtLayout>
    <div class="min-h-screen flex items-center justify-center">
      <div class="text-center">
        <h1 class="text-4xl font-bold mb-4">
          Welcome to {{ config.public.siteName }}
        </h1>
        <p class="text-lg text-gray-600">
          Nuxt Client Base Template (No i18n)
        </p>
        <p class="mt-8 text-sm text-gray-500">
          Edit <code class="bg-gray-100 px-2 py-1 rounded">app/pages/index.vue</code> to get started
        </p>
      </div>
    </div>
  </NuxtLayout>
</template>
