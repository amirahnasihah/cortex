# AI-aware development: MCP, indexing, and your stack

Reference for moving from “AI for code help” to “designing an AI-aware dev environment” (MCP, indexing, sharing context).

---

## 1. What MCP is (in practice)

**MCP (Model Context Protocol)** = a structured way to let AI access external tools/data safely.

For you that can mean: microCMS content, Git repo, Figma files, Nuxt project structure, docs, local files. Instead of pasting everything manually, MCP lets the AI query those systems.

---

## 2. Stacks that typically have MCPs

- **Documentation-heavy:** Next.js, Nuxt, React, Vue, Tailwind, AWS — index docs, semantic search, return relevant sections.
- **CMS / API:** microCMS, Contentful, Sanity, Strapi — fetch schema, content models, generate types, inspect entries.
- **Design:** Figma MCP, Notion MCP.
- **Git / code:** Repo indexing, GitHub MCP, local filesystem MCP.

---

## 3. For your stack (Nuxt + microCMS + GSAP + i18n)

### High value

1. **Local repository index (Cursor)** — Already does this. Parses repo, builds embeddings, lets AI reference files. Use for: “Follow same pattern as VisionSection.vue”, “Refactor all SEO usage”, “Find all canonical logic”, “Check duplicated composables.”
2. **microCMS MCP** — Fetch schema, generate TypeScript types, suggest field mappings, check unused fields, generate API composables. High leverage.

### Optional

3. **Nuxt MCP** — Usually not necessary; Cursor indexing + docs search is enough unless you want auto routeRules or Nitro migration suggestions.
4. **Figma MCP** — Useful if you have it; design spec + paste is fine without.

---

## 4. Sharing MCP (3 levels)

- **Level 1 – Personal local:** Install MCP locally, connect Cursor. Just for you. Good for solo/small freelance.
- **Level 2 – Project-level:** Commit `.claude/settings.json` (or equivalent) with allowed tools/endpoints/permissions. Team pulls repo and gets same MCP config. Shareable.
- **Level 3 – Hosted MCP:** Host microCMS proxy, internal docs, deployment MCP. Agency-level; usually not needed yet.

---

## 5. Cursor indexing ≠ MCP

**Index** = local semantic index of your codebase. Enables cross-file reasoning, refactor suggestions, pattern detection, duplicate export detection.

For your workflow (repeating layout patterns, SEO logic, i18n patterns, matching design systems), **indexing is more important than MCP**. You don’t share the index; each dev’s AI builds its own. You share: repo, rules (`.cursor/rules`), `CLAUDE.md`, MCP config (optional).

---

## 6. Priority order for you

1. Clean project rule (`.cursor/rules`)
2. Clean `CLAUDE.md`
3. Good repo indexing (Cursor)
4. Optional microCMS MCP
5. Optional Figma MCP

Anything more is overengineering.

---

## 7. The real power move: structured context

Instead of chasing MCP hype, define in `.claude/` or `.cursor/rules/`:

- Project stack
- Folder conventions
- i18n rules
- SEO pattern
- Design constraints
- Source-of-truth components

That guides generation quality more than extra MCPs.

---

## 8. Next level: microCMS → type generator

Idea: fetch microCMS schema → auto-generate `shared/types/cms.ts`, server API helpers, Zod validation. AI-augmented tooling; high ROI.

---

## 9. Honest advice

You’re already at high-skill frontend (Nuxt 4 + i18n + GSAP + microCMS + SEO + international clients). Don’t chase MCP hype. Use indexing heavily, keep project rules clean, standardize templates, use AI for structure + translation, keep infra flexible. That gives more speed than five extra MCPs.
