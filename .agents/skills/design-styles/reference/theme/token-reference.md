# Token reference

Semantic tokens (shadcn set). **Reference these, never hardcode oklch/hex.**
Names stay constant across clients; only values in `theme.css` change.

| Token | Role | Tailwind utility |
|-------|------|------------------|
| `--background` / `--foreground` | Page base + default text | `bg-background`, `text-foreground` |
| `--card` / `--card-foreground` | Surfaces (cards, panels) | `bg-card`, `text-card-foreground` |
| `--popover` / `--popover-foreground` | Floating layers (menus, tooltips) | `bg-popover`, `text-popover-foreground` |
| `--primary` / `--primary-foreground` | Brand actions, primary CTAs | `bg-primary`, `text-primary-foreground` |
| `--secondary` / `--secondary-foreground` | Secondary actions | `bg-secondary`, `text-secondary-foreground` |
| `--muted` / `--muted-foreground` | Subtle backgrounds, meta text | `bg-muted`, `text-muted-foreground` |
| `--accent` / `--accent-foreground` | Hover/active highlights | `bg-accent`, `text-accent-foreground` |
| `--destructive` / `--destructive-foreground` | Errors, delete actions | `bg-destructive`, `text-destructive-foreground` |
| `--border` | Borders, dividers | `border-border` |
| `--input` | Form control borders | `border-input` |
| `--ring` | Focus ring (match `--primary`) | `ring-ring` |
| `--chart-1..5` | Data viz series | `fill-chart-1`, `stroke-chart-2`, … |
| `--font-sans` / `--font-serif` / `--font-mono` | Typography slots — per-project font families (name ≠ a constraint) | `font-sans`, `font-serif`, `font-mono` |
| `--radius` | Corner radius base | `rounded-lg` (+ `-sm`/`-md`/`-xl`) |

The above is the **always-present core**. A full tweakcn export also carries:
`--sidebar*` (8 tokens), `--shadow-*` scale (+ raw `--shadow-x/y/blur/spread/opacity/color`),
`--tracking-*`, and `--spacing`. Keep whatever tweakcn emits and map it in
`@theme inline` — see `theme.css`.

## Why oklch

`L` (lightness) is perceptually uniform, so tint/shade/hover steps are
predictable: adjust `L`, keep chroma + hue. Also unlocks wider-gamut (P3).

```css
--primary:       oklch(0.62 0.19 27);   /* base */
--primary-hover: oklch(0.56 0.19 27);   /* darker = lower L, same C/H */
```

## Per-client workflow

1. Pull brand hex from Figma → convert (see `hex-to-oklch.md`).
2. Overwrite values in `theme/theme.css` `:root` + `.dark`. Keep hex comments.
3. Components don't change — they reference token names.
