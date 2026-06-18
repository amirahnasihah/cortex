# Nuxt Client Templates

These are reusable starting points for new client projects.

---

## Available Templates

### 1. `nuxt-client-base/`
**Single-locale Nuxt 4 template** (no i18n)

Use when:
- Client has one language only (e.g., English-only US startup)
- No need for locale routing or multi-language support

**Stack:**
- Nuxt 4 (app/, server/ at root)
- Tailwind v4
- @nuxtjs/sitemap
- SEO setup (useSeoMeta, canonical, schema.org in layout)
- Folder structure: app/pages, app/components, app/composables, shared/types

---

### 2. `nuxt-client-i18n/`
**Multi-locale Nuxt 4 template** (with @nuxtjs/i18n)

Use when:
- Client needs multiple languages (e.g., en + ja, en + de, etc.)
- Path-based locale routing (`/`, `/ja`, `/de`)
- Locale-aware canonical, hreflang, and SEO

**Stack:**
- Nuxt 4 (app/, server/ at root)
- Tailwind v4
- @nuxtjs/i18n (path prefix strategy)
- @nuxtjs/sitemap
- SEO setup (canonical, hreflang, useSeoMeta, schema.org in layout)
- Locale JSON files in `i18n/locales/{locale}.json`
- Folder structure: app/pages, app/components, app/composables, shared/types, i18n/

---

## How to Use

1. **Clone the template:**
   ```bash
   cp -r templates/nuxt-client-base ~/projects/CLIENT_NAME
   # or
   cp -r templates/nuxt-client-i18n ~/projects/CLIENT_NAME
   ```

2. **Update project details:**
   - `package.json`: name, description
   - `nuxt.config.ts`: site name, domain, locales (if i18n)
   - `i18n/locales/*.json`: add/remove locales as needed (i18n template only)

3. **Fill the design spec:**
   - Copy `docs/design-spec-template.md` to `PROJECT_NAME-design-spec.md`
   - Fill in from Figma or client brief

4. **Generate with AI:**
   - Paste the design spec into Cursor
   - Use the global rule + project structure
   - Generate pages, components, sections

---

## Template Structure (both)

```
app/
├── components/      # Reusable components
├── composables/     # Vue composables
├── layouts/
│   └── default.vue  # SEO (canonical, hreflang), schema.org
├── pages/
│   └── index.vue    # Home page
└── public/
    └── images/

i18n/               # (i18n template only)
├── locales/
│   ├── en.json
│   └── ja.json     # Add more as needed
└── config.ts

server/
├── api/            # API routes
└── routes/         # Server routes

shared/
└── types/          # Shared TypeScript types

nuxt.config.ts      # Nuxt config (SEO, i18n, Tailwind)
package.json
tsconfig.json
tailwind.config.ts
```

---

## Next Steps

- See `../docs/design-spec-template.md` for per-project design spec
- See `../rules/global-cursor-rule.md` for Cursor global rule
- For workflow, see the main README
