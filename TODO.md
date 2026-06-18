# TODO

## Domain Expansion
- [ ] Cloud skill — Cloudflare Workers, AWS patterns, deployment conventions
- [ ] Backend skill — Node/Bun, Hono, Drizzle, API conventions
- [ ] IoT skill — ESP32, MQTT, embedded patterns

## Harness Improvements
- [ ] Add domain-specific CLAUDE.md partials (backend, cloud, iot)
- [ ] Regenerate llms.txt for frameworks (Next, Nuxt, Astro) — scripts in `scripts/frameworks/`
- [ ] Make conventions.md framework-agnostic (currently has Nuxt-specific folder structure)

## Testing the Harness
- [ ] Test in cloud-labs with Next.js — verify skills work cross-framework
- [ ] Test `/design-styles` generates correct oklch tokens for a fresh project
- [ ] Test `/code-rules` generates correct AGENTS.md scaffold

## catat.exe Integration

Bridge between cortex (harness) and catat.exe (knowledge base).

### Level 1 — Local skill (works today, same machine only)
- [ ] Create `catat` skill in cortex — writes `.md` to `catat.exe/content/`
- [ ] Auto-format content frontmatter (title, description, date)
- [ ] Support target folders: `docs/ai/`, `docs/sop/`, `docs/guides/`, `repos/[name]/`

### Level 2 — Remote API (works anywhere)
- [ ] Add API route in catat.exe: `POST /api/catat` — creates content file + commits to GitHub
- [ ] MCP server or skill that POSTs to `catat.amrhnshh.com/api/catat`
- [ ] Auth (API key or GitHub token) so only kau boleh write
