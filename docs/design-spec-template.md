# Design Spec Template

**Copy this file per project** (e.g., `PROJECT_NAME-design-spec.md`) and fill in from Figma, brand guidelines, or client brief. Then paste into Cursor when generating components.

---

## Project: `[PROJECT_NAME]`

**Client:** [Company name]
**Locales:** [e.g., en, ja, de]
**Design system:** [Custom Tailwind / shadcn / MUI / none]

---

## Brand

### Colors
- **Primary:** `#______` (e.g., `#DE0017` for red)
- **Secondary:** `#______` (if applicable)
- **Background:** `#______` (e.g., `#FFFFFF`, `#F5F5F5`)
- **Text:** `#______` (e.g., `#333333`, `#000000`)
- **Accent/Link:** `#______`

### Fonts
- **Headings:** [Font family, weight] (e.g., `Noto Sans JP, 700`)
- **Body:** [Font family, weight] (e.g., `Noto Sans JP, 400`)
- **Monospace/Code:** [if applicable]

### Tone
- **Corporate / Formal:** [JP: です・ます, DE: Sie, EN: formal]
- **Startup / Casual:** [JP: だ・である, DE: du, EN: casual]
- **Other notes:** [e.g., "avoid slang," "use technical terms," "friendly but professional"]

---

## Layout

### Container & Spacing
- **Max width:** [e.g., `1280px`, `1440px`, or `full-width`]
- **Section padding (desktop):** [e.g., `py-20`, `py-32`]
- **Section padding (mobile):** [e.g., `py-12`, `py-16`]
- **Horizontal padding:** [e.g., `px-5`, `px-8`, `site-contents`]

### Section Heights
- **Hero/KV:** [e.g., `100vh`, `h-[600px]`, `auto`]
- **Typical section:** [e.g., `auto`, `min-h-screen`]

### Grid & Gaps
- **Default grid (desktop):** [e.g., `grid-cols-3`, `grid-cols-4`]
- **Default grid (mobile):** [e.g., `grid-cols-1`, `grid-cols-2`]
- **Gap:** [e.g., `gap-8`, `gap-x-8 gap-y-16`]

---

## Components

### Cards
- **Style:** [e.g., "Image top, title + date below, rounded corners, shadow on hover"]
- **Image ratio:** [e.g., `aspect-[4/3]`, `aspect-video`]
- **Padding:** [e.g., `p-4`, `p-6`]
- **Border/Shadow:** [e.g., `border border-grey`, `shadow-lg`, `none`]

### Buttons / CTAs
- **Primary button:** [e.g., "Red background, white text, rounded-full, px-8 py-4"]
- **Secondary button:** [e.g., "White background, red border, red text"]
- **Hover state:** [e.g., "scale-105, darker background"]

### Typography Scale
- **Hero title:** [e.g., `text-5xl md:text-7xl`, `font-bold`]
- **Section title:** [e.g., `text-3xl md:text-5xl`, `font-semibold`]
- **Body text:** [e.g., `text-base md:text-lg`, `leading-relaxed`]
- **Small/Caption:** [e.g., `text-sm`, `text-xs`]

### Navigation
- **Style:** [e.g., "Fixed header, white background, logo left, menu right, language switcher in header"]
- **Mobile:** [e.g., "Hamburger menu, slide-in drawer"]

### Footer
- **Style:** [e.g., "Dark background, white text, multi-column links, social icons"]
- **Columns:** [e.g., "3 columns on desktop, stack on mobile"]

---

## Animations

- **Scroll animations:** [e.g., "GSAP ScrollTrigger fade-in on scroll"]
- **Transitions:** [e.g., "Page transitions with Nuxt viewTransition or GSAP"]
- **Hover effects:** [e.g., "scale-105, shadow-lg, color shift"]

---

## Reference Components (existing codebase)

List 2–3 existing components to use as patterns:

1. **Hero/KV:** [e.g., `app/components/hero.client.vue`] — full-height, centered, overlay
2. **Section:** [e.g., `app/components/about/VisionSection.vue`] — standard section pattern
3. **Card:** [e.g., `app/components/card/content.vue`] — image + title + date

---

## Notes

- [Any special design rules, e.g., "Full-bleed images," "No shadows," "Always use rounded-3xl," "GSAP for all animations"]
- [Any accessibility requirements, e.g., "WCAG AA," "keyboard navigation for all interactive elements"]

---

**Usage:** Paste this spec into Cursor when starting a new task or generating components for this project. Example prompt:

> "This project uses the design spec above. Generate a new section for [description]. Use the same layout pattern as VisionSection. Add i18n keys for en and ja."
