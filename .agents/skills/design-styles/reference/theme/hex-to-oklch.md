# Figma hex → oklch

Figma authors colors in **hex** (no oklch picker). tweakcn + Tailwind v4 work in
**oklch**. Convert **at the boundary**; keep hex as the design source of truth.

## Rule

- Store **oklch** in tokens (`theme.css`).
- Leave the **original hex as a comment** next to each token — auditable map +
  sign-off value for strict brand guides.

```css
--primary: oklch(0.62 0.19 27);   /* Figma brand #E5484D */
```

## How to convert

Pick any one — they all output the same oklch:

- **tweakcn** (`tweakcn.com`) — paste hex, tune live, copy the full token block.
- **oklch.com** — single-color picker, paste hex, read the oklch string.
- **Tailwind v4** — ships oklch palettes; match Figma to the nearest if close.
- **Code** — `culori`: `formatCss(oklch(parse('#E5484D')))`.

## Format

```
oklch(L C H)
       │ │ └─ hue 0–360
       │ └─── chroma (saturation) ~0–0.4
       └───── lightness 0–1
```

Neutrals (white/black/grey): chroma + hue are `0` → `oklch(0.97 0 0)`.

## Exception

If the client brand guide mandates exact hex, the hex comment is the
reference/sign-off value — note it explicitly in the design spec.
