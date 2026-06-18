# Animation — GSAP + Lenis

**GSAP** drives motion; **Tailwind** keeps static layout/styling. Keep them
separate — don't animate via Tailwind transition classes for anything complex.

**Lenis** (smooth scroll) is **optional** — add only when the client/design
asks. Not a default.

## GSAP + ScrollTrigger (Nuxt plugin)

```ts
// app/plugins/gsap.client.ts
import gsap from "gsap"
import { ScrollTrigger } from "gsap/ScrollTrigger"

export default defineNuxtPlugin(() => {
  gsap.registerPlugin(ScrollTrigger)
  return { provide: { gsap } }
})
```

```vue
<script setup lang="ts">
const { $gsap } = useNuxtApp()
const el = ref<HTMLElement>()

onMounted(() => {
  $gsap.from(el.value!, {
    opacity: 0, y: 40, duration: 0.8, ease: "power2.out",
    scrollTrigger: { trigger: el.value!, start: "top 80%" },
  })
})
</script>
```

- `.client.ts` plugin — animation is client-only.
- Clean up with `ScrollTrigger.refresh()` on layout change; kill tweens in
  `onUnmounted` for SPA navigation.
- Respect `prefers-reduced-motion`.

## Lenis (optional smooth scroll)

```bash
pnpm add lenis
```

```ts
// app/plugins/lenis.client.ts — only if the design calls for smooth scroll
import Lenis from "lenis"

export default defineNuxtPlugin(() => {
  const lenis = new Lenis({ lerp: 0.1, smoothWheel: true })
  const raf = (time: number) => { lenis.raf(time); requestAnimationFrame(raf) }
  requestAnimationFrame(raf)
  // Sync with ScrollTrigger if both are used:
  // lenis.on("scroll", ScrollTrigger.update)
})
```
