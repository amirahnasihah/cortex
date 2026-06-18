# Prompt Cheat Sheet

Quick copy-paste prompts for common tasks with international clients.

---

## 1. Starting a New Project

### With i18n template:
```
I'm starting a new client project. Clone the nuxt-client-i18n template and update:
- Site name: [CLIENT_NAME]
- Domain: [https://example.com]
- Locales: [en, ja] (or add/remove)

Then help me fill the design spec from this Figma URL: [paste URL or describe]
```

### Without i18n (single locale):
```
Clone the nuxt-client-base template for a single-locale project.
- Site name: [CLIENT_NAME]
- Domain: [https://example.com]
- Locale: [en]

Design: [paste spec or Figma details]
```

---

## 2. Adding a New Page

### With i18n:
```
Add a new page at /about with:
- SEO meta (title, description, og*)
- i18n keys for en and ja
- Use the same layout pattern as [reference component]

Content: [paste content or describe sections]
```

### Without i18n:
```
Add a new page at /about with:
- SEO meta (title, description, og*)
- Same layout pattern as [reference component]

Content: [paste content]
```

---

## 3. Adding a New Section/Component

```
This project uses [paste design spec or reference "same pattern as VisionSection"].

Add a new section for [description]:
- Layout: [full-width / container / grid]
- Content: [headline, body, CTA, image, etc.]
- i18n keys for [en, ja]

Follow the existing Tailwind classes and component structure.
```

---

## 4. Translating Copy (i18n projects)

### From client copy:
```
Turn this copy into i18n JSON. Keys: pageName.sectionName.property.

[Paste client copy in English or Japanese]

Generate entries for:
- en (English, formal tone)
- ja (Japanese, です・ます form)
```

### Adding a new locale (e.g., German):
```
We're adding German to this project.
1. Update nuxt.config.ts with de locale
2. Here are the current en.json keys: [paste]
3. Translate to German (formal 'Sie' form)
```

---

## 5. SEO: Adding Schema.org

### Article page:
```
Add Article JSON-LD schema to this page [paste page or reference]:
- headline, description, image from page content
- datePublished from [field]
- author: Organization (use site config)
```

### ItemList (news/blog listing):
```
Add ItemList JSON-LD to the news list page:
- Use visibleNewsList items
- Each item: headline, url, image, datePublished
- numberOfItems from totalCount
```

---

## 6. Custom Design Components

### From Figma:
```
This project uses custom Tailwind (no shadcn). Design spec: [paste].

From this Figma design: [paste URL or screenshot or describe]:
- Primary color: #______
- Font: [name, weight]
- Card style: [image ratio, padding, border/shadow]

Generate a component for [hero / card / section] that matches this design.
```

### Matching existing component:
```
Generate a new [hero / section / card] component using the same pattern as [reference component path]:
- Same Tailwind classes and layout structure
- Content: [describe or paste]
- i18n keys for [locales]
```

---

## 7. Animations (GSAP)

```
Add GSAP ScrollTrigger fade-in animation to [component or section]:
- Trigger when section enters viewport
- Stagger for child elements if applicable
- Use existing GSAP setup from [reference if any]
```

---

## 8. Bug Fixes

```
This [component/page] does X but should do Y:

[Paste code or error or describe issue]

Fix while keeping the same pattern as the rest of the project.
```

---

## 9. Refactoring

```
Refactor [component/section] to:
- [specific change, e.g., "use the same section pattern as VisionSection"]
- Keep current behavior and i18n keys
- Match the project's Tailwind style
```

---

## 10. Language Switcher

```
Add a language switcher component to the header:
- Show all active locales from i18n config
- Current locale highlighted
- Links to same page in other locales
- Style: [describe or "same as nav links"]
```

---

## Tips for Better Results

1. **Always reference the project context:**
   - "This project uses [custom Tailwind / i18n / GSAP]"
   - "Follow the design spec: [paste or reference]"
   - "Use the same pattern as [component]"

2. **Be specific about locales and tone:**
   - "Add i18n keys for en (formal) and ja (です・ます)"
   - "Translate to German (formal 'Sie')"

3. **Paste examples when possible:**
   - Existing components to mirror
   - Client copy (even if mixed language)
   - Design specs or Figma URLs

4. **Ask AI to generate i18n keys, not full translations:**
   - You review and adjust tone/accuracy
   - Faster than translating manually

5. **Use the design spec:**
   - Fill it once per project
   - Paste into every component generation prompt
   - Ensures consistency without repeating details

---

**For your most common task (the one that takes the most time), create a custom prompt here and reuse it per project.**
