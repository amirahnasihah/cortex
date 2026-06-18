# cortex

Portable AI harness — conventions, skills, and templates for AI-powered development.

## What's inside

```
cortex/
├── CLAUDE.md              # Harness brain — Claude Code reads this
├── install-skills.sh      # Installs third-party skills
├── .agents/skills/        # Custom skills (cross-platform, committed)
│   ├── design-styles/     # Tailwind v4 oklch theme + shadcn
│   └── code-rules/        # TypeScript/engineering conventions
├── docs/                  # Conventions, specs, rules
├── rules/                 # Cursor / AI rules
├── templates/             # Project starters (Nuxt 4)
└── .claude/settings.json  # Claude Code shared settings
```

## Quick start

```bash
git clone git@github.com:amirahnasihah/cortex.git
cd cortex
bash install-skills.sh    # installs third-party skills (impeccable, taste-skill)
```

Custom skills (`design-styles`, `code-rules`) are already in the repo — no install needed.

## Skills

| Type | Skills | Location |
|------|--------|----------|
| Custom (committed) | design-styles, code-rules | `.agents/skills/` |
| Third-party (install) | impeccable, taste-skill | via `install-skills.sh` |

`.agents/skills/` is cross-platform — works with Claude Code, Cursor, Copilot, Gemini CLI.

Browse more skills at [skills.sh](https://www.skills.sh/).

## Templates

| Template | Description |
|----------|-------------|
| `nuxt-client-base` | Nuxt 4 starter — no i18n |
| `nuxt-client-i18n` | Nuxt 4 + i18n, microCMS, multi-locale |

## Roadmap

See [TODO.md](TODO.md) for planned additions (backend, cloud, IoT templates).

## License

[Apache-2.0](LICENSE)
