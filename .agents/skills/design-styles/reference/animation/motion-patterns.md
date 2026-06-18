# Motion patterns — the awwwards-tier toolkit

Motion is what separates awwwards/cutting-edge sites from templated slop. **GSAP**
(+ ScrollTrigger) drives scroll/timeline work; **Motion** (Framer Motion,
`motion/react`) drives component/spring/gesture; **Lenis** smooths the scroll they
ride on. Keep static layout in Tailwind — see `gsap-and-lenis.md` for setup.

Rules that keep it tasteful, not gimmicky:
- **Spring/eased, not linear.** `ease: "power3.out"` / spring physics — never `linear`.
- **Stagger** list & grid children (0.05–0.1s) — nothing enters all at once.
- **Scroll-triggered, not autoplay.** Motion responds to the user.
- **Transform + opacity only** (GPU); avoid animating layout props. `will-change` sparingly.
- **Respect `prefers-reduced-motion`** — gate or reduce every effect.
- **Clean up** on unmount / route change (kill triggers); `ScrollTrigger.refresh()` on layout change.

## GSAP — scroll toolkit

```ts
// 1. Scrub — tie progress to scroll position
gsap.to(el, {
  xPercent: -100,
  scrollTrigger: { trigger: el, start: "top top", end: "+=2000", scrub: 1, pin: true },
})

// 2. Reveal on enter (with stagger)
gsap.from(items, {
  opacity: 0, y: 60, duration: 0.9, ease: "power3.out", stagger: 0.08,
  scrollTrigger: { trigger: container, start: "top 75%" },
})

// 3. Parallax depth — layers move at different speeds
gsap.to(".bg-layer", { yPercent: -30, ease: "none",
  scrollTrigger: { trigger: section, start: "top bottom", end: "bottom top", scrub: true } })

// 4. Text reveal — split into lines/words, stagger up (needs SplitText or a split util)
const split = new SplitText(heading, { type: "lines" })
gsap.from(split.lines, { yPercent: 100, opacity: 0, duration: 1, ease: "power4.out", stagger: 0.1,
  scrollTrigger: { trigger: heading, start: "top 80%" } })

// 5. Horizontal scroll section
gsap.to(track, { x: () => -(track.scrollWidth - innerWidth), ease: "none",
  scrollTrigger: { trigger: track, pin: true, scrub: 1, end: () => "+=" + track.scrollWidth } })
```

Named techniques worth reaching for: **pinned sections**, **scrub timelines**,
**parallax depth**, **split-text reveals**, **horizontal scroll**, **marquee /
infinite loop**, **magnetic buttons + custom cursor**, **image-trail / hover
distortion** (WebGL — heavy, use sparingly), **page transitions**.

## Motion (Framer) — component & gesture

```tsx
import { motion, useScroll, useTransform } from "motion/react"

// spring entrance + viewport trigger + stagger via parent variants
<motion.ul initial="hidden" whileInView="show" viewport={{ once: true, margin: "-15%" }}
  variants={{ show: { transition: { staggerChildren: 0.08 } } }}>
  {items.map((it) => (
    <motion.li key={it.id}
      variants={{ hidden: { opacity: 0, y: 40 }, show: { opacity: 1, y: 0 } }}
      transition={{ type: "spring", stiffness: 120, damping: 18 }}>
      {it.label}
    </motion.li>
  ))}
</motion.ul>

// scroll-linked transform
const { scrollYProgress } = useScroll({ target: ref, offset: ["start end", "end start"] })
const y = useTransform(scrollYProgress, [0, 1], [0, -120])
<motion.div style={{ y }} />
```

Use Motion for: `whileHover` / `whileTap` micro-interactions, `layout` animations,
`AnimatePresence` for enter/exit + **page transitions**, drag. Use GSAP for the
heavy scroll-driven sequences above. Don't run both on the same property.

## Reduced motion

```ts
const mq = window.matchMedia("(prefers-reduced-motion: reduce)")
if (!mq.matches) { /* run the full motion */ } else { /* set final state instantly */ }
```

References for *what* to build: `../inspo/design-refs.md` (motion language +
awwwards-style site list). Mine Magic UI / Aceternity (`../shadcn/registries.md`)
for ready motion components — re-own them to the project's tokens.
