/**
 * Standard SEO layer — one composable for canonical, og:image, hreflang, title.
 * No custom SEO per page unless passed as param.
 */

export interface UseSeoOptions {
  title?: string
  description?: string
  image?: string
}

export function useSeo(options?: UseSeoOptions) {
  const route = useRoute()
  const config = useRuntimeConfig()
  const siteName = config.public.siteName as string
  const siteDomain = config.public.siteDomain as string

  const title = computed(() => options?.title ?? siteName)
  const description = computed(() => options?.description ?? '')
  const image = computed(() => options?.image ?? '')

  const canonicalUrl = computed(() => {
    const path = route.path
    return `${siteDomain}${path}`
  })

  useSeoMeta({
    title,
    description,
    ogTitle: title,
    ogDescription: description,
    ogImage: image,
    ogUrl: canonicalUrl,
  })

  useHead({
    link: [{ rel: 'canonical', href: canonicalUrl }],
  })

  return { title, description, image, canonicalUrl }
}
