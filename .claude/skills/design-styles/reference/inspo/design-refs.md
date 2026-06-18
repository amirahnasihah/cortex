# Design References & Taste Profile

> Agent instruction: Read this file before generating any hi-fi wireframe, page design, or component. The starred sections are the primary references — match the motion language and aesthetic direction described here.
>
> Companion docs: `../shadcn/registries.md` (where to pull components from + the shadcn MCP) · `../shadcn/shadcn-patterns.md` (how we build `ui/` primitives). This file is **taste & motion**; those two are **sources & mechanics**.

---

## Taste Profile

> **Fill per project.** Describe this project's aesthetic direction — type style,
> color approach, motion language, overall vibe — from the brand / Figma / brief.
> This is what makes a given project distinct; the starred references below are
> the shared toolbox, the taste profile is the steer.
>
> Develop it with `/impeccable` + `/taste-skill` (or the `frontend-design` skill)
> when starting from scratch. Keep it short — a few lines of intent, not an essay.

---

## ⭐ Primary UI Libraries — Use These First

These are the starred picks. When generating components, pull patterns from these before reaching for generic shadcn defaults.

| Library                                     | What to use it for                              | Notes                                       |
| ------------------------------------------- | ----------------------------------------------- | ------------------------------------------- |
| [Magic UI](https://magicui.design/)         | Orbit, shimmer, bento grid, animated gradients  | Best for hero sections and feature grids    |
| [Animata](https://animata.design/)          | Copy-paste micro-animations, hover effects      | Open source, Tailwind-native                |
| [Aceternity UI](https://ui.aceternity.com/) | Spotlight cards, parallax, text reveal          | The reference for "wow" scroll effects      |
| [Eldora UI](https://www.eldoraui.site/)     | Lazy-load reveals, staggered lists              | Good for content-heavy pages                |
| [21st.dev](https://21st.dev/)               | Registry-style components from design engineers | Check here for creative nav + hero variants |
| [Skiper UI](https://skiper-ui.com/)         | Modern component patterns                       | Check for layout ideas                      |
| [React Bits](https://www.reactbits.dev/)    | Animated React components                       | Good for small interactions                 |
| [Animate UI](https://animate-ui.com/)       | Animation-first components                      | —                                           |
| [Origin UI](https://originui.com/)          | Clean open-source Tailwind + React              | Good baseline components                    |

---

## Motion & Animation

### Libraries

- **`motion/react`** (Framer Motion) — use for page transitions, stagger, spring physics, scroll-triggered reveals.
- **anime.js** → [`animejs.com`](https://animejs.com/documentation/getting-started/) — DOM-level animation sequences (GSAP alternative, lighter).
- **Rive** → [`rive.app`](https://rive.app/) + [React runtime](https://rive.app/docs/runtimes/react/react) — interactive vector animations.

### Motion language to follow

- **Spring physics** for entrances (not ease-in-out linear)
- **Stagger** on list/grid items (0.05–0.1s delay between items)
- **Scroll-triggered** opacity + Y translate reveals (not autoplay)
- **Drag interactions** → reference: [Framer Motion drag slider](https://codesandbox.io/s/framer-motion-drag-slider-3mggu)
- **Sidebar slide-in on scroll** → reference: [`scalar.com`](https://scalar.com/)
- **Scroll card effect** → reference: [`mymind.com/adhd`](https://mymind.com/adhd)

### Animation references

- [60fps.design](https://60fps.design/) — curated motion references
- [App Motion](http://appmotion.design) — mobile + web animation ideas
- [Shakuro Framer Motion tutorial](https://shakuro.com/blog/framer-motion-tutorials-make-more-advanced-animations) — advanced patterns

---

## ⭐ Visual Inspiration — Primary References

Sites that define the target look. Check these when deciding layout, spacing, and visual language.

| Site                                                             | What to reference                                    |
| ---------------------------------------------------------------- | ---------------------------------------------------- |
| [largo.studio](https://largo.studio/)                            | Overall vibe — layout boldness, type scale           |
| [plant-blog-rive.vercel.app](https://plant-blog-rive.vercel.app) | Rive animation integration in web UI                 |
| [davidhaz.com](https://davidhaz.com/)                            | Personal portfolio aesthetic, type-led               |
| [mymind.com/adhd](https://mymind.com/adhd)                       | Scroll card stacking effect                          |
| [scalar.com](https://scalar.com/)                                | Sidebar slide-in on scroll, developer tool aesthetic |
| [posthog.com](https://posthog.com)                               | OS/terminal-inspired design language                 |
| [firecrawl.dev](https://www.firecrawl.dev/)                      | Clean developer tool landing                         |
| [mistral.ai](https://mistral.ai/)                                | AI product minimal direction                         |
| [raindrop.ai](https://www.raindrop.ai/)                          | Dark-mode developer tool aesthetic, monochromatic palette with teal/blue CTA accents, workflow visualization showing progression through UI states |
| [ona.com](https://ona.com/)                                      | Enterprise-grade polish — full-bleed video hero, asymmetric image+text grid modules, sticky minimal nav, restrained motion (fade/reveal only, no flash) |

---

## Design Curation Sites

Browse these when looking for section ideas or layout patterns.

### Awards & Galleries (highest signal)

1. [impeccable.style](https://impeccable.style/) — **start here for out-of-box taste**
2. [curated.design](https://curated.design) — personal fav
3. [awwwards.com](https://www.awwwards.com/) — industry standard for cutting-edge web design
4. [siteinspire.com](https://www.siteinspire.com/websites) — highly curated, editorial quality
5. [admiretheweb.com](https://admiretheweb.com) — unique picks

### UI / App Patterns

6. [mobbin.com](https://mobbin.com/) — web + mobile app UI pattern library (real screenshots)
7. [component.gallery](http://component.gallery) — design systems
8. [refero.design](https://refero.design/) — references across multiple sites
9. [uncoverlab.co](https://uncoverlab.co/web-design-website-sections) — sections only
10. [devmeetsdevs.com](https://devmeetsdevs.com/) — 1000+ ideas by section

### Landing Pages

11. [land-book.com](https://land-book.com) — large selection
12. [landing.gallery](https://landing.gallery) — all niches
13. [saaslandingpage.com](https://saaslandingpage.com) — SaaS-specific
14. [onepagelove.com](http://onepagelove.com) — single-page focus

### Motion-specific

15. [60fps.design](https://60fps.design/) — motion-focused curation

### Other

16. [inspo.page](https://www.inspo.page/) — general library
17. [craftwork.design/curated/websites](https://craftwork.design/curated/websites/)

### Taste & Skill Reference

- [tasteskill.dev](https://www.tasteskill.dev/) — design taste + skill development
- [open-design.ai](https://open-design.ai/) — AI-assisted design exploration

---

## Design Theory & Education

Read-for-vocabulary references — name the styles and principles, and stay current on where the field is heading. Useful when deciding *which* direction a page should commit to (the Playground theme lab is where we feel those directions on real components).

- [Web design styles](https://tilda.education/en/web-design-styles) — the named-style taxonomy (brutalism, swiss, editorial, etc.); shared vocabulary for the theme-lab directions
- [Web design trends 2025](https://tilda.education/en/web-design-trends-2025) — what's current
- [Web design trends 2026](https://tilda.education/en/web-design-trends-2026) — what's next
- [Web design principles](https://tilda.education/en/web-design-principles) — fundamentals (hierarchy, contrast, rhythm, whitespace)

---

## Icons & Assets

| Resource                                                  | Type                                  |
| --------------------------------------------------------- | ------------------------------------- |
| [Animate Icons](https://animateicons.vercel.app/) ✨      | Animated SVG icons for React          |
| [Lucide](https://lucide.dev/)                             | Default icon set                      |
| [SVGL](https://svgl.app/)                                 | Brand logos / company SVGs            |
| [SVG Repo](https://www.svgrepo.com/)                      | General SVGs                          |
| [React Icons](https://react-icons.github.io/react-icons/) | Multi-library icon set                |
| [Flagpack](https://flagpack.xyz/)                         | Country flag icons                    |
| [Dicebear](https://www.dicebear.com/)                     | Avatar generation                     |
| [unDraw](https://undraw.co/)                              | Open-source illustrations             |

---

## Fonts

- [Google Fonts](https://fonts.google.com/) — primary source for web typefaces (pairs with `@nuxt/fonts` / `next/font`)
- [Best Free Fonts](https://bestfreefonts.com/) — curated free typefaces
- **Typography guidance** (offline) → `../typography/` — pairing, readability, accessible
  & responsive type, variable fonts. Highest-value: `nngroup-pairing-typefaces.md`,
  `nngroup-best-font-reading.md`, `webdev-accessible-typography.md`, `designers-guide-choosing-fonts.md`.

---

## Useful Extras

- [uicolors.app](https://uicolors.app/create) — Tailwind CSS color palette generator
- [Skeleton Generator](https://skeletongenerator.com/) — Tailwind loading skeleton generator
- [ui.jln.dev](https://ui.jln.dev/) — shadcn/ui CSS variable theme generator
- [Navbar Gallery](https://www.navbar.gallery/) — nav pattern ideas
- [Hamburger React](https://hamburger-react.netlify.app/) — mobile nav toggle
- [Huemint](https://huemint.com/) — ML color scheme generation
- [Remotion](https://www.remotion.dev/) — video with React (for animated exports)
- [Rive Editor](https://editor.rive.app/home) — create Rive animations
