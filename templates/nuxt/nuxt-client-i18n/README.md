# nuxt-client-i18n

**Scaffold template** for starting a new Nuxt 4 + i18n project.

This is the clone-me starting point for international (multi-locale) client work — an opinionated,
controlled base with a fixed structure, standard composables, SEO/CMS/i18n/animation systems, and
tests, so every new i18n project starts the same way.

---

## Stack

- Nuxt 4, TypeScript (strict)
- microCMS, `@nuxtjs/seo`, `@nuxt/fonts`, `@nuxtjs/i18n`, Tailwind v4
- GSAP optional (plugin + `useGsap`)
- **Testing:** Vitest + `@nuxt/test-utils` (unit + Nuxt env). Run: `npm run test`, `npm run test:run`.

Core systems (do not change the pattern, only per-project values):

- One `useMicrocms` for all CMS access — no direct `$fetch` in components.
- One `useSeo` for canonical / og / title.
- i18n strategy locked (`prefix_except_default`, en default, `/ja` prefixed).
- `useSanitize` (+ `shared/utils/sanitize`) for CMS rich text.
- GSAP isolated in `plugins/gsap.client.ts` + `useGsap`.

---

## New project from this scaffold

1. Copy this folder to the new project directory.
2. Update `package.json` name, and `nuxt.config.ts` `site` / `runtimeConfig` (siteName, siteDomain, `microcmsApiKey`).
3. Add env (e.g. `.env` with `NUXT_PUBLIC_MICROCMS_API_KEY`).
4. Add/remove locales in `nuxt.config.ts` `i18n.locales` and matching `i18n/locales/*.json`.
5. Fill design tokens in `tailwind.config.ts` from the design spec.
6. Do **not** change folder structure or naming conventions.

```bash
npm install
npm run dev      # http://localhost:3000 (en) and /ja (ja)
npm run test     # unit + Nuxt env tests
npm run build && npm run preview
```

---

## Folder structure

```
app/
├── app.vue
├── composables/        # useMicrocms, useSeo, useSanitize, useLocalePath, useGsap
├── layouts/default.vue # canonical, hreflang, schema.org
├── pages/index.vue
└── plugins/gsap.client.ts

i18n/locales/           # en.json, ja.json (add de.json, fr.json, ...)
shared/
├── types/schema.org.ts
└── utils/sanitize.ts
test/
├── unit/               # node env
└── nuxt/               # nuxt env

nuxt.config.ts  package.json  tailwind.config.ts  tsconfig.json  vitest.config.ts
```

See `docs/nuxt-client-i18n.md`, `docs/rules.md`, and `docs/testing.md` in the dotclaude repo for the
full structure, project rules (v2), and testing conventions.
