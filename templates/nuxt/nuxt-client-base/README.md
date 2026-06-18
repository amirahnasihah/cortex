# Nuxt Client Base Template (No i18n)

Single-locale Nuxt 4 starter for clients with one language only.

## Stack

- **Nuxt 4** (SSR, hybrid rendering)
- **Tailwind v4** (custom per project)
- **@nuxtjs/sitemap** (auto sitemap generation)
- **TypeScript** (strict mode)
- **SEO ready** (useSeoMeta, canonical, schema.org in layout)

## Quick Start

1. **Install dependencies:**
   ```bash
   pnpm install
   ```

2. **Update config:**
   - `nuxt.config.ts`: site name, domain
   - `package.json`: name, description

3. **Fill design spec:**
   - Copy `../../docs/design-spec-template.md` to `PROJECT_NAME-design-spec.md`
   - Fill in from Figma or client brief

4. **Dev:**
   ```bash
   pnpm dev
   ```

5. **Build:**
   ```bash
   pnpm build
   pnpm preview
   ```

## Folder Structure

```
app/
├── components/      # Reusable components
├── composables/     # Vue composables
├── layouts/
│   └── default.vue  # SEO (canonical), schema.org (Organization, WebSite)
├── pages/
│   └── index.vue    # Home page
└── public/
    └── images/

server/
├── api/            # API routes
└── routes/         # Server routes

shared/
└── types/          # Shared TypeScript types (schema.org, etc.)

nuxt.config.ts
package.json
tailwind.config.ts
```

## SEO Setup

- **Canonical URL** in layout (`route.path`, no query params)
- **useSeoMeta** in pages (title, description, og*, twitter)
- **Schema.org** in layout (Organization, WebSite)
- **Sitemap** auto-generated via `@nuxtjs/sitemap`

## Adding Pages

1. Create `app/pages/PAGENAME.vue`
2. Add SEO meta in page:
   ```vue
   <script setup lang="ts">
   useSeoMeta({
     title: 'Page Title | Site Name',
     description: 'Page description',
     ogTitle: 'Page Title',
     ogDescription: 'Page description',
     ogImage: '/images/og-image.png',
   })
   </script>
   ```

## Tailwind Customization

Edit `tailwind.config.ts` per project (colors, fonts, spacing from design spec).

## Next Steps

- Add CMS integration (microCMS, Contentful, etc.) if needed
- Add animations (GSAP, etc.) if needed
- Extend schema.org in layout or per page
