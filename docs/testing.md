# Testing — nuxt-client-i18n and Nuxt projects

Vitest + @nuxt/test-utils. Unit tests (Node) for pure logic; Nuxt-environment tests for composables that use Nuxt (useRuntimeConfig, $fetch, etc.).

---

## Setup (in template)

- **Vitest** + **@nuxt/test-utils**, **@vue/test-utils**, **happy-dom**
- **vitest.config.ts** with two projects:
  - **unit** — `test/unit/**/*.{test,spec}.ts` — `environment: 'node'` (fast, no Nuxt)
  - **nuxt** — `test/nuxt/**/*.{test,spec}.ts` — Nuxt runtime (composables, auto-imports)
- Optional: **@nuxt/test-utils/module** in nuxt.config for DevTools integration

Commands: `npm run test` (watch), `npm run test:run` (CI).

---

## What to test

### microCMS

- **useMicrocms** (or `composables/cms/`): mock `$fetch` with `mockNuxtImport('$fetch', () => vi.fn())`. Assert correct URL, headers (`X-MICROCMS-API-KEY`), query params, and return value.
- **Shared types** (e.g. from microCMS): unit test pure transformers/normalizers in `test/unit/`.
- Do **not** call the real microCMS API in tests; keep tests fast and deterministic.

### CMS rich editor → frontend output

- **Sanitization:** Rich text from microCMS (or any CMS) must be sanitized before rendering to avoid XSS. Test the sanitizer in **unit** (no Nuxt):
  - Strip `<script>` tags.
  - Strip event handlers (`onclick`, `onerror`, etc.).
  - Preserve safe tags (e.g. `p`, `a`, `strong`, `ul`, `li`) and attributes (e.g. `href`).
- Put pure sanitize logic in **shared/utils/** (e.g. `sanitize.ts`) and a thin **useSanitize** composable in `app/composables/`. Unit test the pure function; use the composable in components.
- For stricter sanitization in production, use a library (e.g. isomorphic-dompurify) and still cover behavior with unit tests.

### SEO

- **useSeo** or layout meta: test in **nuxt** environment or with `mountSuspended` and assert `useHead` / `useSeoMeta` usage or resulting meta in the DOM.
- Canonical, hreflang, title template: consider E2E or snapshot tests if you need full page output.

### Composables

- **Need Nuxt (useRuntimeConfig, $fetch, useRoute, etc.):** `test/nuxt/**` and mock with `mockNuxtImport`.
- **Pure logic (no Nuxt):** `test/unit/**`, import from `shared/utils` or the composable’s inner helper.

---

## Naming and layout

- Test files: **`*.test.ts`** or **`*.spec.ts`** next to the code or under `test/unit/` and `test/nuxt/`.
- Composable tests: e.g. `test/nuxt/composables/useMicrocms.test.ts`, `test/unit/sanitize.test.ts` for shared utils.
- Follow project naming: **camelCase** inside tests; **PascalCase** for types/describe blocks as needed.

---

## Best practices

1. **Unit tests** for pure functions (sanitize, formatters, type guards) — fast, no Nuxt.
2. **Nuxt tests** only when the code uses Nuxt context; mock `$fetch`, `useRuntimeConfig`, etc., via `mockNuxtImport`.
3. **CMS content:** Always mock API; test “CMS rich editor → safe HTML” with unit tests on the sanitizer.
4. **No real API or secrets** in tests; use `.env.test` for test-time config if needed.
5. Run `test:run` in CI; use `test` (watch) during development.

---

## Reference

- [Nuxt 4 — Testing](https://nuxt.com/docs/getting-started/testing)
- [@nuxt/test-utils](https://nuxt.com/modules/test-utils) — `mockNuxtImport`, `mountSuspended`, Nuxt environment
- [Vitest](https://vitest.dev/) — projects, mocking, coverage
