# Happy Mates Design System

A working design kit for **Happy Mates** — a Danish social-impact tech organization that bridges young AI-curious gamers (often neurodivergent / Asperger's) with companies that need real AI capability.

> *"You have the talent. Your company has the ambition. We connect the dots — with AI as the common language."*

The brand carries a warm, optimistic, slightly playful tone. It mixes **clean SaaS-y product UI** with **food/kitchen metaphors** (the "Digital Sourdough", recipes, the digital kitchen, the Mate Kiosk drive-thru). It is bilingual — Danish first, English second.

---

## Sources

Everything in this system was reverse-engineered from the live codebase:

- **Repo:** `happy-mates/web` — <https://github.com/happy-mates/web>
- React 19 + Vite + TypeScript + Tailwind v4 + lucide-react icons + radix-ui slot
- Companion repos in the same org expand into infrastructure, kiosks, padel, the **Surdej** framework book, plus dozens of "*-mate" workers and agents. Browse <https://github.com/happy-mates> for more.

Read on demand — most of the visual DNA lives in `src/index.css`, `src/components/hero.tsx`, `src/components/navigation.tsx`, `src/components/cards-section.tsx`, `src/components/hubs-section.tsx`, and `src/components/kiosk/kiosk-frame.tsx`.

---

## Index

| File | Purpose |
|---|---|
| `README.md` | This file — brand context, content rules, visual foundations, iconography |
| `colors_and_type.css` | All design tokens (colors, type, radii, shadows) + semantic helpers |
| `assets/` | Logos, brand mark, hero photo, team imagery |
| `reference/` | Screenshots of the production site for cross-reference |
| `preview/` | Design-system swatch / specimen cards (registered for the Design System tab) |
| `ui_kits/web/` | High-fidelity recreation of the marketing site (`index.html` + JSX components) |
| `SKILL.md` | Agent-skill manifest for use as a Claude Code skill |

---

## Content fundamentals

**Voice.** Warm, plain-spoken, occasionally cheeky. Always inclusive — the brand exists to bridge two groups (talents + companies) so language puts both sides at ease. Slight Danish irony peeks through in English copy. Never corporate, never aggressive.

**You vs we.** "You" speaks directly to the reader; "we" speaks for Happy Mates as a collective ("we connect the dots", "we bake new digital products"). "I" is never used.

**Bilingualism.** Every visible string ships as `t(en, da)`. Danish is the primary audience; English exists for partners and international readers. Treat both as first-class — never machine-translated feel.

**Casing.**
- **Sentence case** for headings, buttons, labels, nav items ("Read more", not "Read More").
- **TitleCase** only for branded nouns: *Happy Mates*, *Mate Trainee*, *Dele Mate*, *Super Prompt*, *Digital Sourdough*, *Digital Kitchen*.
- **ALL CAPS** *only* for the wordmark (`HAPPY MATES`) and the kiosk chrome (`MATE KIOSK · ONLINE`, `HAPPY MATES · 2026`). Plus tiny tag pills (`AUTH`, `DATA`, `AI`, `INTEGRATION`, `UI`).

**Sentence pattern.** Short, punchy, em-dashes (`—`) for asides instead of parentheses. Often a three-beat structure: setup — twist — payoff.

> *"Turn your gaming skills into a real IT career. Learn to build with AI, work on live projects, and get hired — all in 6 months."*

> *"Like a fast-food restaurant, but for IT services."*

**Metaphor library.** Lean into them — they are the brand:
- *Digital Kitchen* (the platform you cook your product in)
- *Digital Sourdough / Surdej* (the reusable starter template you never bake without)
- *Recipes* (codified Super Prompts)
- *Mate Kiosk / Drive-thru* (intake counter for orders)
- *Curly brain / Krøllet hjerne* (neurodivergent thinkers)
- *Warm heart / Varmt hjerte* (the volunteer / Happy Hearts side)

**CTA verbs.** "Read more", "Learn more", "See how it works", "See more", "Contact us". Never "Click here", never "Submit", never "Sign up now!".

**Emoji.** Used sparingly. **Only on the Mate Kiosk surface** (chef hat 👨‍🍳, basket 🛒, receipt 🧾, wave 👋) and on the occasional process step. Never on the marketing site headings or in product UI. Treat as illustrative punctuation, not decoration.

**Numerics.** Tabular nums for countdowns and prices. Prices in **DKK** (`499 DKK`, `750 DKK/mo`). Dates locale-aware (`Sep 15, 2026` / `15. sep 2026`).

---

## Visual foundations

### Layout DNA

- **Full-width sticky nav** with logo + wordmark on the left, links centred-right, language toggle, countdown chip, and a single high-contrast CTA on the far right.
- **Full-bleed hero sections** with a background photo or video, then a vertical gradient overlay fading to the page background so headlines sit comfortably on the lower half.
- **Container** is `mx-auto max-w-7xl px-4`, generous vertical padding (`py-20`/`py-24`), and most marketing sections aim for `min-h-screen` so they read as discrete chapters.
- **Section rhythm.** Each scroll-section gets its own background tone — alternating `background` → `muted/30` → `background` → `muted/10` — separated by a hairline `border-b border-border`.
- **In-section nav.** Floating round pill button bottom-right ("See more ▾") with `animate-bounce` — the brand's signature scroll affordance. Pair it with a quieter circular "scroll up" button stacked above.
- **Two-column hub blocks** alternate sides (`md:flex-row` / `md:flex-row-reverse`) — image one side, copy + CTA the other, with a soft colored glow blurring out from behind the image.

### Cards

- **Marketing card:** `bg-background`, `border border-primary/20`, `rounded-2xl`, generous padding (`p-8`), an outer **gradient glow** (`absolute -inset-1 bg-gradient-to-r from-X to-Y rounded-2xl blur opacity-25 group-hover:opacity-40`). The glow is the brand's signature card treatment — never use a plain shadow alone where a glow would fit.
- **News / product card:** `bg-background`, `rounded-2xl`, `border border-border`, `overflow-hidden`, image on top with `aspect-[16/9]` and `group-hover:scale-105` zoom on hover.
- **Glassmorphism on hero:** the about-section overlays a `bg-background/85 backdrop-blur-md` card on top of the team photo — the only place blur is used.

### Buttons

The shadcn-style `Button` from the codebase has six variants. The brand uses **default**, **outline**, and **ghost** on the marketing site; the kiosk has its own punkier brutalist button.

| Variant | Use | Style |
|---|---|---|
| `default` | Primary CTA | `bg-primary` (blue), white text, soft shadow, `hover:bg-primary/90` |
| `outline` | Secondary CTA | Transparent, 1px input border, hover swaps to `bg-accent` |
| `ghost` | Tertiary | No chrome, hover paints the `accent` background |
| `link` | Inline | Primary-color text, underline on hover |
| `destructive` | Dangerous | Red bg, white text |
| `secondary` | Soft alt | Slate-50 fill |

Sizes: `default` (h-9 px-4), `sm` (h-8 px-3 text-xs), `lg` (h-10 px-8), `icon` (h-9 w-9 square). Radii are `rounded-md` on default buttons, but **pill-shaped (`rounded-full`)** for the bouncing "See more" and hub CTAs.

### Press / hover / focus

- **Hover.** Cards get more gradient glow, images scale up `1.05`, link text shifts to `text-primary`, an arrow icon translates `1` to the right (`group-hover/link:translate-x-1`).
- **Press.** Kiosk buttons shrink `active:scale-[0.97]`; marketing buttons rely on the `bg-primary/90` darken.
- **Focus.** `focus-visible:ring-1 ring-ring` (a blue 1px ring) — minimal and accessibility-correct.

### Borders

- **Hairlines** for separators: `border-border` ≈ `#E2E8F0`.
- **Primary tints** for card outlines: `border-primary/20` → `border-primary/40` on hover.
- **The kiosk is the exception** — heavy 4–8px solid black borders with hard offset drop shadows (`shadow-[4px_4px_0_0_rgba(0,0,0,1)]`), aggressively retro-fast-food.

### Shadows

- Marketing surface: `shadow-sm` for resting, `shadow-lg` on hover, `shadow-2xl` for the about-section glass card.
- Kiosk surface: hard 2D offset shadows in solid black, no blur.
- The **gradient glow** is the dominant elevation device — it replaces shadow on every primary card.

### Animations

- **Rainbow text shimmer.** The wordmark animates `background-position 0% → 100% → 0%` over 3 s on a horizontal gradient. The single signature motion.
- **Bounce.** `animate-bounce` on the "See more" pill so the scroll affordance always nags.
- **Image hover zoom.** 500 ms `transform: scale(1.05)` inside `overflow-hidden`.
- **Opacity / color fades.** Always `transition-colors duration-300` or shorter. Defaults to ease-in-out (Tailwind default).
- No bespoke spring physics, no scroll-tied parallax. Motion is restrained.

### Transparency & blur

- Background image legibility uses **vertical fade overlays** — `bg-gradient-to-b from-background/95 via-background/90 to-background` — *not* a solid scrim.
- The hero video uses a darker top-to-bottom gradient (`from-black/70 via-black/50 to-black/80`).
- Glass cards only on the about section (`/85 backdrop-blur-md`).

### Imagery

- **Photography:** warm, daylight-lit, group shots of real diverse young people in informal collaboration. Slight grain. No stocky boardroom shots.
- **Generated 3-D scenes:** the *kling/* and *digital-kitchen.png* assets are stylised Pixar-like 3-D renders of chef-coded characters at neon-trimmed code-kitchens. Use these for the metaphor moments (sourdough, kitchen, drive-thru).
- **Color mood:** warm overall (amber light), with cool neon highlights (cyan, magenta) in the 3-D scenes — but the marketing site itself sits on near-white slate.
- No black-and-white filter, no duotone, no heavy desaturation.

### Corner radii

| Token | Px | Used on |
|---|---|---|
| `rounded-md` (--radius) | 8 | Buttons, inputs, small chips |
| `rounded-xl` | 12 | Icon tiles inside cards (`p-3 rounded-xl bg-blue-500/10`) |
| `rounded-2xl` | 16 | Cards (marketing + product) |
| `rounded-3xl` | 24 | The kiosk shell + the about-section glass card |
| `rounded-full` | ∞ | Pill CTAs, tag pills, language switcher, social/avatar |

### Spacing scale

Tailwind defaults — but in practice the system uses a narrow vocabulary:
`gap-2 / gap-3` (chips & inline rows) · `gap-4 / gap-6` (card internals) · `gap-8 / gap-12` (grid layouts) · `py-20 / py-24` (section padding) · `space-y-4 / space-y-6 / space-y-8` (stacked card content).

### Color vibe at a glance

- **Neutral palette.** Cool, near-white slate (HSL `210 40% 96.1%`) and very dark navy (`222.2 84% 4.9%`) for foreground. Borders are slate-200.
- **Primary blue.** A vivid `221 83% 53%` ≈ `#2563EB`. Confident, trustworthy. Used for default buttons and link hovers.
- **Brand rainbow.** Red → yellow → blue gradient (the logo's vertical gradient) animates across the wordmark and appears on big keyword spans in headlines. This is the single most recognisable brand element.
- **Hub accents.** Each hub has its own gradient pair — Plans (orange/amber), Sourdough (amber/yellow), Operations (indigo/purple), Daily (teal/emerald).
- **Kiosk accents.** Bold McDonalds-coded `#E4002B` red and `#FFC72C` yellow on a `#1a0a0a` near-black ground, contained inside the kiosk surface only.

---

## Iconography

The codebase imports **[lucide-react](https://lucide.dev)** (`lucide-react@0.562.0`) exclusively. No icon font, no inline SVG sprites, no Heroicons.

Conventions in the codebase:
- Default size is `h-4 w-4` (set by the button variant CSS — `[&_svg]:size-4`). Hero icons inside accent tiles are `h-7 w-7` or `h-8 w-8`.
- Stroke-only, default lucide stroke width.
- Colored via Tailwind `text-blue-500` / `text-orange-500` / `text-primary` etc. — never multi-color.
- Common icons in use: `ArrowRight`, `ChevronDown` / `ChevronUp`, `Brain`, `Rocket`, `Users`, `Lightbulb`, `Sparkles`, `Calendar`, `Clock`, `ShoppingBag`, `Menu`, `X`.

For this design system we use lucide via the CDN script (`https://unpkg.com/lucide@latest`) inside the UI kit so the visual match is exact.

**Logo & brand mark.** The `happy-mates-logo.svg` is a single circle with the red→orange→yellow→green→blue vertical gradient (the wordmark animation pulls from the same palette horizontally). Inside a white inner circle sits a simple two-dot-eye smiley. Always pair the mark with the **rainbow wordmark** — the two are inseparable.

**Emoji.** Used only inside the **Mate Kiosk** stepper (`👋 🤔 👨‍🍳 🛒 🧾`) and inline as a "tone of voice" punctuation on a few list items (`📝`, `🔄`, `🍞`). Never on marketing pages.

**Unicode glyphs.** `›` is used as a step separator inside the kiosk stepper. `—` (em-dash) is the brand's signature punctuation.

---

## Visual variations and divergence

When designing new screens for Happy Mates, decide first **which surface** you're on. They are visually distinct:

1. **Marketing site** — clean SaaS, generous whitespace, gradient glows, soft elevation, the rainbow wordmark, hero photos with fade overlays.
2. **Mate Kiosk** — brutalist McDonalds-aesthetic, hard borders, offset shadows, big touch targets, emoji-led stepper, red + yellow + black palette.
3. **Recipe / catalog product UI** — closer to the marketing surface but denser; small icon-tile + tag + price product cards in a 3-column grid.
4. **Process / docs pages** — single-column long-read with stat cards and step illustrations.

Mixing these breaks the brand. The kiosk's brutalism never appears on the marketing site, and vice versa.

---

## Substitutions & caveats

- **Inter is loaded from Google Fonts** in production (`<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700">`). This design system does the same. No local font files needed.
- The `videos/welcome-kitchen-team.mp4` and `kling/*` 3-D renders are not redistributed here — substitute the `assets/happy-mates-team.jpeg` photo on hero screens. Ask the user for replacements if you need the rendered kitchen scenes.
- The brand uses **lucide-react** at a pinned version. The CDN icon font we link in the UI kit serves the same SVG paths, but if you author code that will be imported into the production app, install `lucide-react` instead.
