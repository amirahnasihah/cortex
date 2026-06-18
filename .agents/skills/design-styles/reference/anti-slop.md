# Anti-slop — escaping the generic AI look

The goal of this design system: **distinctive, modern, cutting-edge** work
(awwwards-tier, animation-forward) — not the templated default that AI tends to
produce. Most AI-generated sites now look *competent and identical*. That's slop.

**Taste judgment lives elsewhere.** For the "is this generic / how do I make it
bolder" call, use the `impeccable`, `taste-skill`, and `frontend-design` skills.
This doc adds the **system-level discipline** that keeps the build from sliding
back into defaults.

## The slop tells (avoid)

- Centered hero → subtitle → two pill buttons, and nothing else above the fold.
- One typeface (Inter / system) everywhere, no scale contrast, no personality.
- Purple→blue gradient blobs, generic glassmorphism, soft drop shadows everywhere.
- Three equal feature cards in a row: lucide icon + bold title + grey paragraph.
- **Untouched default shadcn** — looks like every other shadcn site.
- No motion, or motion as an afterthought (a single fade-in).
- Emoji-as-icons, `rounded-2xl` on everything, perfectly symmetric, zero tension.

## Do instead

- **Type as identity** — a distinctive typeface (often a display/serif paired with
  a clean body), large scale contrast, deliberate hierarchy. See `typography/`.
- **Commit to a direction** — editorial, brutalist, swiss, terminal, maximal…
  pick one (taste profile in `inspo/design-refs.md`) and push it; don't average.
- **Asymmetry & rhythm** — break the grid intentionally; generous negative space
  *or* deliberate density — not safe symmetric padding everywhere.
- **Own the components** — cva variants, custom radius (square reads less generic),
  considered states. Never ship the default look (`shadcn/shadcn-patterns.md`).
- **Motion as the signature** — scroll-driven, spring, staggered, one memorable
  "wow" moment per page. See `animation/motion-patterns.md`.
- **Confident color** — a real palette with one strong accent, not gradient soup.
  Tune in `theme/theme.css`.
- **Real assets** — bespoke imagery/texture/video over stock + icon clip-art.
  See `assets.md`.

## Process

1. **Direction** — set the taste profile (`/taste-skill` or `/impeccable`),
   reference real awwwards-style sites (`inspo/design-refs.md`).
2. **System** — tokens + owned components (`theme/`, `shadcn/`).
3. **Motion** — layer the signature motion last (`animation/motion-patterns.md`).
4. **Critique** — run `/impeccable` against the result: "what here reads templated?"
