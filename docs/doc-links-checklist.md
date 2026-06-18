# Doc links checklist — quick reference for indexing and context

Use this list when you need to point the AI (or yourself) at official docs. Cursor indexes **your repo**; external sites are not indexed. Keep this file in the repo so you can @-mention it or paste links into chat when relevant.

---

## In-repo (dotclaude)

| Resource | Path | Use when |
|----------|------|----------|
| **Conventions** (stack, naming, structure, reuse) | `docs/conventions.md` | New projects, onboarding, PR review, AI rules; single source of truth for camelCase/PascalCase/kebab-case and folder layout |
| **nuxt-client-i18n** definition | `docs/nuxt-client-i18n.md` | What the internal framework is; locked stack, structure, naming, core systems |
| **nuxt-client-i18n v2 project rules** | `docs/rules.md` | Strict structure, dependency direction, CMS/SEO/i18n/animation; follow when editing nuxt-client-i18n or projects built from it |
| **Testing** (Vitest, microCMS, rich editor sanitize) | `docs/testing.md` | Unit vs Nuxt env, what to test for CMS/SEO, sanitization best practices |
| Design spec template | `docs/design-spec-template.md` | Copy per project; fill from Figma |
| Client Cursor rule snippet | `rules/nuxt-client-conventions.mdc` | Copy into client projects’ `.cursor/rules/` so Cursor follows same naming and structure |

---

## Core stack

| Resource | Link | Use when |
|----------|------|----------|
| Nuxt 4 | https://nuxt.com/docs/4.x/getting-started | Setup, directory structure, config |
| Nuxt SEO | https://nuxtseo.com/ | useSeoMeta, canonical, hreflang, sitemap |
| Nuxt i18n | https://i18n.nuxtjs.org/ | Locales, routing, useLocaleHead, SEO |
| Tailwind v4 | https://tailwindcss.com/docs | @import "tailwindcss", Vite plugin, Nuxt guide |
| Vue 3 | https://vuejs.org/guide/ | Composition API, SFC, reactivity |
| VueUse | https://vueuse.org/ | useMediaQuery, useStorage, etc. |
| Nitro | https://nitro.build/guide | Server, route rules, deploy |
| Pinia (if used) | https://pinia.vuejs.org/ | State, @pinia/nuxt |
| VeeValidate (if used) | https://vee-validate.logaretm.com/v4/ | Forms, validation |

---

## CMS & assets

| Resource | Link | Use when |
|----------|------|----------|
| MicroCMS | https://document.microcms.io/ | API, Nuxt, schema |
| Nuxt Image | https://image.nuxt.com/ | NuxtImg, providers, presets |
| Nuxt Fonts | https://nuxt.com/docs/getting-started/styling#working-with-fonts | Fonts, preload |

---

## Hosting & deployment

| Resource | Link | Use when |
|----------|------|----------|
| NuxtHub | https://hub.nuxt.com/ | Cloudflare deploy, cache |
| Vercel (Nitro) | https://nitro.build/deploy/providers/vercel | Deploy, ISR |

---

## SEO and i18n (deep links)

- **Nuxt SEO – hreflang:** https://nuxtseo.com/learn-seo/nuxt/routes-and-rendering/i18n  
- **Nuxt SEO – meta:** https://nuxtseo.com/learn-seo/nuxt/mastering-meta  
- **i18n SEO:** https://i18n.nuxtjs.org/docs/guide/seo  

---

## How to use this for “indexing”

- **In-repo:** Cursor indexes files in your project. This checklist is in the repo, so you can say e.g. “See docs/doc-links-checklist.md for our stack links.”
- **External docs:** Not indexed by Cursor. When you need a specific doc, open the link above or paste the URL into chat and ask the AI to use it.
- **Quick start:** For a new project or new teammate, share this repo (or copy this file); all important links are in one place.
