# Per-client design spec

The look is driven by a **per-client design spec**, not by this skill's
defaults. Don't duplicate the template here — copy the canonical one:

**Source:** `dotclaude/docs/design-spec-template.md`

## Flow

1. Copy `docs/design-spec-template.md` → `PROJECT_NAME-design-spec.md` in the
   client repo.
2. Fill **Brand → Colors** from Figma (hex). Convert to oklch
   (`theme/hex-to-oklch.md`) → overwrite values in `theme/theme.css`.
3. Fill layout, components, typography, animation sections.
4. Paste the filled spec into Cursor/Claude when generating components.

## What maps to what

| Spec section | Drives |
|--------------|--------|
| Brand → Colors | `theme/theme.css` token values (`:root` / `.dark`) |
| Brand → Fonts | `@nuxt/fonts` + typography utilities |
| Layout / Components / Typography | cva variants in owned `components/ui/*` |
| Animations | `animation/gsap-and-lenis.md` (Lenis only if requested) |
