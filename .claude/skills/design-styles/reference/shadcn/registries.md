# shadcn Registries — Where to Pull Components From

> Agent instruction: This is the **map of sources** for component research. Read it alongside
> `../inspo/design-refs.md` (taste/motion) and `shadcn-patterns.md` (how we re-own what we pull). When you need
> a component pattern, look here for *which registry* to mine before reaching for a generic default.
> Re-own what you pull (semantic tokens, `cn()`, `data-slot`) — see `shadcn-patterns.md`.

**Important — pulling ≠ installing.** We use the shadcn **manual** pattern (no `components.json`, no
CLI install into the build). A registry is a **research source**: read its component, learn the
pattern, then hand-rewrite it into your `ui/` components dir to these conventions (semantic tokens,
`cn()`, `data-slot`, etc. — see `shadcn-patterns.md`). Never paste a registry component verbatim; it
will carry foreign tokens, radii, and deps that break your token contract.

---

## How to drive the shadcn MCP

The repo has the shadcn MCP server wired in `.mcp.json` (`shadcn@latest mcp`, secret-free). Tools:

| Tool | Use for |
| --- | --- |
| `search_items_in_registries` | fuzzy-find a component by name/description across registries |
| `list_items_in_registries` | enumerate everything in a registry (filter by `types`: ui, block, hook, theme…) |
| `view_items_in_registries` | read a specific item's source to learn the pattern |
| `get_item_examples_from_registries` | see usage examples for an item |
| `get_add_command_for_items` | get the `npx shadcn add …` command (reference only — we re-own by hand) |
| `get_project_registries` | list registries configured in `components.json` |

**Caveat:** all of these require a `components.json`, which we intentionally don't ship. To *research*
a third-party registry via the MCP you can scaffold a throwaway `components.json` (e.g. in `/tmp`) that
declares the registry under `registries`, point the MCP at it, read what you need, then discard it —
**do not** commit `components.json` into an app. For most cases, reading the registry's own docs/site
(URLs below) is simpler than the MCP dance.

Registry namespaces look like `@name` and resolve to a `registry.json` URL. To add one to a throwaway
config:
```json
{ "registries": { "@magicui": "https://magicui.design/r/{name}.json" } }
```

---

## Registries — start here (verified)

Grouped by what you'd reach for; scope to the project's taste profile (see
`../inspo/design-refs.md`). URLs are the canonical project sites; treat the `@handle` as indicative —
confirm the exact namespace from the site before configuring.

### AI / chat (conversational UI)
| Registry | Site | Use for |
| --- | --- | --- |
| AI Elements (Vercel) | <https://ai-sdk.dev/elements> | message lists, prompt input, streaming, tool calls |
| prompt-kit | <https://www.prompt-kit.com/> | chat composer, message, markdown rendering, scroll-to-bottom |
| kibo-ui | <https://www.kibo-ui.com/> | AI + general blocks (some chat primitives) |

### Motion & "wow" (hero, reveals, micro-interactions)
| Registry | Site | Use for |
| --- | --- | --- |
| Magic UI | <https://magicui.design/> | shimmer, bento, animated gradients, marquee |
| Aceternity UI | <https://ui.aceternity.com/> | spotlight, parallax, text reveal |
| cult-ui | <https://www.cult-ui.com/> | polished animated components |
| React Bits | <https://www.reactbits.dev/> | small animated React interactions |
| Animata | <https://animata.design/> | copy-paste micro-animations, Tailwind-native |

### Baseline primitives & layout
| Registry | Site | Use for |
| --- | --- | --- |
| shadcn/ui (`@shadcn`) | <https://ui.shadcn.com/> | the canonical primitive patterns we mirror manually |
| Origin UI | <https://originui.com/> | clean Tailwind + React baseline variants |
| 21st.dev | <https://21st.dev/> | registry-style components from design engineers; creative nav/hero |
| Skiper UI | <https://skiper-ui.com/> | modern layout patterns |

### Theming / tokens (for `[data-theme]` hi-fi wireframes)
| Registry | Site | Use for |
| --- | --- | --- |
| tweakcn | <https://tweakcn.com/> | visual theme editor → OKLCH token sets to drop into a `[data-theme]` block |

> Niche accents (e.g. terminal/mono): often no single dominant registry — build by hand from your own
> tokens + the chosen typeface. Mine Magic UI / Aceternity for the *motion*, not the palette.

---

## Full registry directory (~250)

> **Not yet populated.** The full directory you pasted earlier was lost when the conversation
> compacted, and it is not recoverable from any transcript. Rather than fabricate registry names into
> a harness doc (which would mislead future sessions), this section is left as a deliberate slot.
>
> **To fill it:** re-paste the directory JSON (or its source URL) and it gets formatted here, grouped
> by category, in one pass. Until then, the verified shortlist above is the source of truth, and the
> shadcn MCP (`list_items_in_registries`) is the live fallback for anything not listed.
