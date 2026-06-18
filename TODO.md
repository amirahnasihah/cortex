# TODO

## Future Templates
- [ ] Backend (Node/Bun, Hono, Drizzle)
- [ ] Cloud (Cloudflare Workers, AWS)
- [ ] IoT (ESP32, MQTT, embedded)

## Harness Improvements
- [ ] Slim down repo — remove bundled skills, use `skills.sh` for on-demand install
- [ ] Add domain-specific CLAUDE.md partials (backend, cloud, iot)
- [ ] Add `.env.example` files per template

## catat.exe Integration

Bridge between cortex (harness) and catat.exe (knowledge base).

### Level 1 — Local skill (works today, same machine only)
- [ ] Create `catat` skill in cortex — writes `.md` to `catat.exe/content/`
- [ ] Auto-format Nuxt Content frontmatter (title, description, date)
- [ ] Support target folders: `docs/ai/`, `docs/sop/`, `docs/guides/`, `repos/[name]/`

### Level 2 — Remote API (works anywhere)
- [ ] Add API route in catat.exe: `POST /api/catat` — creates content file + commits to GitHub
- [ ] MCP server or skill that POSTs to `catat.amrhnshh.com/api/catat`
- [ ] Auth (API key or GitHub token) so only kau boleh write
