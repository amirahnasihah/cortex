# cortex

Portable AI harness — conventions, skills, and templates for AI-powered development.

Clone anywhere, run `skills.sh`, start working.

## What's inside

```
cortex/
├── CLAUDE.md          # Harness brain — Claude Code reads this
├── skills.sh          # One-command skill installer
├── docs/              # Conventions, specs, rules
├── rules/             # Cursor / AI rules
├── templates/         # Project starters (Nuxt 4)
├── .claude/           # Claude Code shared settings
└── .cursor/rules/     # Cursor project rules
```

## Quick start

```bash
git clone git@github.com:amirahnasihah/cortex.git
cd cortex
bash skills.sh          # install all skills
# or
bash skills.sh design   # design & frontend only
bash skills.sh dev      # dev tools only
bash skills.sh util     # utilities only
```

## Skills manifest

Skills are **not bundled** — `skills.sh` installs them fresh on demand.

| Category | Skills |
|----------|--------|
| Design | impeccable, taste-skill, frontend-design, web-design-guidelines |
| Dev | remotion-best-practices, remotion-render |
| Util | find-skills, skill-creator |

## Templates

| Template | Description |
|----------|-------------|
| `nuxt-client-base` | Nuxt 4 starter — no i18n |
| `nuxt-client-i18n` | Nuxt 4 + i18n, microCMS, multi-locale |

## Roadmap

See [TODO.md](TODO.md) for planned additions (backend, cloud, IoT templates).

## License

[Apache-2.0](LICENSE)
