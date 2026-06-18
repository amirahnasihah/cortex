# Visual assets — gen-AI images & video pipeline

`design-styles` builds the **code / layout / motion**; this is where the **visual
assets** come from (hero imagery, textures, backgrounds, video). The skill *uses*
assets — it does not generate them. Generation is a separate, usually **paid**,
step (run manually or via an MCP).

## Honest reality

There is **no free Midjourney-tier** image generator. Pick a tier per project:

### Images
| Tool | Quality | Programmatic / API | Notes |
|---|---|---|---|
| Midjourney | top | no official API (web/Discord) | best look, manual |
| **FLUX** (Black Forest Labs) via **fal.ai** / **Replicate** | very high | ✅ pay-per-image | the practical "MJ-level" for automation |
| **Nano Banana Pro** (Gemini 3 image) | high | ✅ paid API | strong at edits + text-in-image |
| OpenAI images | high | ✅ paid API | good general fallback |

### Video
| Tool | Notes |
|---|---|
| Runway · Kling · Google Veo · fal.ai-hosted | all paid; for hero/bg motion clips |

## MCP angle

- **Figma MCP** (already connected) — generate designs, design→code, assets.
- **Image-gen MCPs** wrap fal.ai / Replicate / Gemini — let an agent generate
  inside the loop, but they spend **paid credits**. Availability varies; confirm
  the server before relying on it in a headless/cron run.

## Pipeline (the part that matters for the harness)

```
generate  →  optimize  →  integrate
```

1. **Generate** — prompt the chosen tool to the project's taste profile
   (`inspo/design-refs.md`): style, palette, mood. Keep prompts on-brand.
2. **Optimize** — convert to **AVIF/WebP**, export responsive widths, compress.
   Video → compressed `mp4` + `webm` + a poster frame.
3. **Integrate**
   - Images: `<Image>` primitive (required `alt`, lazy, width/height) — never bare `<img>`.
   - Background video: `autoplay muted loop playsinline` + `poster`; pause off-screen;
     drop to the poster image under `prefers-reduced-motion` and on slow connections.

## Performance guardrails

- Hero imagery is usually the LCP element — prioritise/preload it, everything else lazy.
- Never ship an uncompressed PNG/MOV. Budget hero ≲ 200–300 KB image, video ≲ a few MB.
- A texture/gradient that Tailwind or CSS can render → don't generate an image for it.
