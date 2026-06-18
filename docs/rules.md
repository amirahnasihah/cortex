# nuxt-client-i18n v2 — Project Rules

This project follows a standardized Nuxt 4 architecture. All new files must follow the structure and conventions below.

---

## 1. Core Principles

- Follow Nuxt 4 default structure (`app/`, `server/`, `shared/`).
- Separate UI, layout, features, and logic clearly.
- Avoid duplicated logic and cross-layer pollution.
- One responsibility per file.
- Prefer `unknown` over `any` in TypeScript.
- No client-specific logic in base template.

---

## 2. Folder Structure Rules

### app/

All application code lives inside `app/`.

```
app/
  components/
  composables/
  layouts/
  pages/
  plugins/
  assets/
  constants/
  data/
```

Do NOT create new top-level folders inside `app/` without strong reason.

---

### components/

Structure:

```
components/
  ui/         → reusable UI primitives
  layout/     → Header, Footer, navigation
  features/   → domain-specific sections (About, News, etc.)
  icons/      → SVG-only components
```

Rules:

- Vue components use **PascalCase**.
- One component per file.
- No business logic inside `ui/`.
- `features/` may depend on `ui/`, never the reverse.
- Avoid deeply nested folders (max depth: 3).

---

### composables/

Grouped by responsibility:

```
composables/
  animations/
  cms/
  seo/
  state/
  utils/
```

Rules:

- File names must start with `use`.
- One composable per file.
- No DOM manipulation outside `animations/`.
- CMS API logic belongs in `cms/`.
- SEO meta helpers belong in `seo/`.
- Do not mix reactive logic with pure utilities.

---

### app/lib/

For pure, non-reactive utilities:

```
app/lib/
  seo/
  cms/
  animations/
```

Rules:

- No Vue imports here.
- Pure TypeScript functions only.
- No side effects.

---

### server/

```
server/
  api/
  middleware/
```

Rules:

- Server-only code.
- No imports from `app/`.
- Shared types must come from `shared/`.

---

### shared/

```
shared/
  types/
  utils/
```

Rules:

- Used by both `app/` and `server/`.
- No Vue imports.
- Types must have a single source of export.
- Avoid duplicate type definitions.

---

## 3. Naming Conventions

### Components

- PascalCase: `VisionSection.vue`
- Client-only: `Intro.client.vue`
- No kebab-case component filenames.

### Composables

- `useSomething.ts`
- Lower camel case inside.

### Types

- PascalCase type names.
- One domain per file when possible.

### Pages

- Folder per route.
- `index.vue` for root of section.
- Dynamic routes: `[id]/index.vue`.

---

## 4. i18n Rules

- Locale files live in `i18n/locales/`.
- Keys follow: `page.section.element`.
- No inline hardcoded copy in components.
- All text must come from locale files.

---

## 5. SEO Rules

- SEO handled in `layouts/default.vue` or via `useSeo`.
- Canonical must be locale-aware.
- hreflang must be generated per locale.
- No duplicate meta tags.

---

## 6. CMS Rules

- All CMS API access goes through `composables/cms/`.
- Shared CMS types live in `shared/types/`.
- Type generation script: `scripts/generate-cms-types.ts`.
- Do not access CMS directly inside components.

---

## 7. Animation Rules

- GSAP logic isolated inside `composables/animations/`.
- No timeline logic directly inside page files.
- Always clean up ScrollTrigger on unmount.

---

## 8. Dependency Direction

**Allowed:**

- features → ui
- layout → ui
- pages → features
- composables → shared
- server → shared

**Not allowed:**

- ui → features
- shared → app
- server → app

---

## 9. Deployment Safety

- No filesystem writes.
- No Node-only APIs in client code.
- Runtime config used for secrets.
- Compatible with Vercel and Cloudflare.

---

## 10. When Adding New Feature

1. Add component under `features/`.
2. Add required composable under correct group.
3. Add i18n keys.
4. Add types in `shared/types/` if needed.
5. Do not bypass structure.

---

## 11. Testing Rules

- **Vitest** + **@nuxt/test-utils** for unit and Nuxt-runtime tests.
- **test/unit/** — Node environment; pure logic (e.g. `shared/utils`, sanitize, formatters). No Nuxt.
- **test/nuxt/** — Nuxt environment; composables that use `useRuntimeConfig`, `$fetch`, etc. Use `mockNuxtImport` to mock `$fetch` or other auto-imports.
- **microCMS:** Mock all API calls; do not hit real microCMS in tests. Test `get()` URL, headers, and return value.
- **CMS rich editor output:** Sanitize HTML before render. Put sanitize logic in `shared/utils/` and unit test it (strip script, event handlers; preserve safe tags). Use composable `useSanitize` in components.
- One test file per composable or util; name `useSomething.test.ts` or `sanitize.test.ts`. See **docs/testing.md** for full guidance.

---

This structure is the internal OSBR frontend standard. Deviations must be documented.
