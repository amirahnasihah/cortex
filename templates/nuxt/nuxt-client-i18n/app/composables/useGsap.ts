/**
 * GSAP — optional. Register plugin in plugins/gsap.client.ts.
 * Keep animation isolated; never mix with layout logic.
 */
export function useGsap() {
  const nuxtApp = useNuxtApp()
  const gsap = (nuxtApp as unknown as { $gsap?: unknown }).$gsap ?? null
  const ScrollTrigger = (nuxtApp as unknown as { $ScrollTrigger?: unknown }).$ScrollTrigger ?? null
  return { gsap, ScrollTrigger }
}
