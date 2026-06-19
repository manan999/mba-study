# Be Skilled — Visual Design System & Section Specifications

Reference document for implementing the homepage prototype (`be-skilled-homepage-prototype.html`) in Figma, Framer, or directly in code. All values below are the literal values used in that file, so the two documents stay in sync.

---

## Global Tokens

**Color**

| Token | Hex | Usage |
|---|---|---|
| Navy (primary) | `#0B1F3A` | Headlines on light bg, nav, dark section backgrounds |
| Navy Soft | `#142B4D` | Secondary dark panels (founder photo block) |
| Navy Deep | `#081628` | Footer background |
| Ivory (secondary) | `#F7F5F2` | Primary page background |
| Ivory Alt | `#F0EDE6` | Alternating section background, for rhythm |
| Ivory Muted | `#D9D5CC` | Body text on navy backgrounds |
| Gold (accent) | `#C8A96B` | Numerals, eyebrow labels on dark bg, dividers, hover accents |
| Gold Dark | `#AD8C4F` | Hover state for gold/secondary elements |
| Charcoal (text) | `#2E2E2E` | Primary body text on light backgrounds |
| Charcoal Muted | `#6B6864` | Secondary/supporting text |
| Teal (CTA) | `#3F7D7A` | Primary button fill, links, active states |
| Teal Dark | `#33645F` | Primary button hover |

**Typography** — Headlines: Fraunces (serif, 400/500/600). Body: Inter (sans, 400/500/600).

| Role | Desktop | Mobile | Weight / Line-height |
|---|---|---|---|
| H1 (Hero) | 58px | 36px | 500 / 1.08–1.15 |
| H2 (Section title) | 40px | 28px | 500 / 1.18–1.2 |
| H3 (Card / sub-head) | 21–22px | 19px | 600 |
| Eyebrow label | 13px | 13px | 600, uppercase, 0.14em tracking |
| Body large (intro) | 18–19px | 16px | 400 / 1.6–1.65 |
| Body | 15–15.5px | 15–15.5px | 400 / 1.6–1.7 |
| Caption / micro | 12.5–14px | 12.5–14px | 400 |

**Spacing scale** (8px base): 8 · 16 · 24 · 32 · 48 · 64 · 72 · 96 · 120px

**Grid** — Max content width 1200px, centered. Side margin 64px desktop → 24px mobile. Multi-column layouts use explicit CSS Grid column counts (3-col, 2-col, 4-col as noted per section) with 24–32px gutter desktop, collapsing to single column at 20px gutter below the **860px breakpoint**.

**Border radius** — sm `4px` (tag chips) · md `6px` (buttons) · lg `12px` (cards, photo blocks) · xl `16px` (reserved, unused on homepage)

**Shadow** — sm `0 1px 3px rgba(11,31,58,.07), 0 1px 2px rgba(11,31,58,.05)` (resting cards, nav) · md `0 10px 26px rgba(11,31,58,.10)` (hover state) · lg `0 18px 44px rgba(11,31,58,.16)` (hero visual, founder photo) · teal-glow `0 12px 26px rgba(63,125,122,.30)` (primary button hover only)

**Buttons**
- Primary: Teal fill / Ivory text / radius md / shadow sm at rest → Teal Dark fill + `translateY(-2px)` + teal-glow shadow on hover
- Secondary: transparent / 1.5px Navy border / Navy text → 5% navy tint fill + Gold Dark border on hover (on dark sections: Ivory text + translucent Ivory border → Gold border on hover)
- Gold (Final CTA only): Gold fill / Navy Deep text → lighter gold + lift on hover. Reserved exclusively for the highest-intent moment on the page.

---

## Section-by-Section Specifications

#### 1. Navigation
- Background: Ivory at 96% opacity, blurred (sticky)
- Grid: flex row, 3 zones (logo / links / CTA) → links collapse into hamburger drop-down below 860px
- Padding: 20px vertical, 64px → 24px horizontal
- Typography: logo serif 21px/600; nav links sans 15px/500
- Image: none
- CTA: Primary "Book a Consultation" + Secondary "Explore Programs" (secondary hides on mobile to reduce clutter)
- Hover states: link underline animates left-to-right in Gold Dark, 2px
- Radius: md (buttons)
- Shadow: none — separated by a 1px hairline border instead, to keep the nav feeling architectural rather than floating

#### 2. Hero
- Background: Ivory
- Grid: 2-column (1.05fr / .95fr) → 1-column; visual panel reorders above the headline on mobile
- Padding: 100/110px → 56/64px
- Typography: H1 serif 58px → 36px; intro body-large 19px → 16px
- Image: navy abstract placeholder panel with a faint gold grid-line pattern, captioned for real training photography
- CTA: Primary + Secondary side by side → wrap on mobile
- Hover states: primary lifts + teal-glow shadow; secondary fills with 5% navy tint
- Radius: lg (visual panel), md (buttons)
- Shadow: lg on the visual panel — this is the one section allowed a heavier shadow, since it needs to read as the page's anchor

#### 3. Positioning Statement (Navy Band)
- Background: Navy, full width
- Grid: single centered column, max-width 760–800px
- Padding: 72px → 56px
- Typography: serif 25px → 20px, editorial/quote weight
- Image: none
- CTA: none — this section is pure credibility, not conversion
- Hover states: none
- Radius / Shadow: n/a — flat color band, deliberately calm after the hero

#### 4. Diagnostic CTA Band
- Background: Ivory (page default)
- Grid: card spans container; internal flex row → stacks and centers on mobile
- Padding: 72px → 56px (section); 48px → 24px (card interior)
- Typography: H3 serif 24px/500; body 15.5px
- Image: none
- CTA: Secondary outline button
- Hover states: button fills 5% navy tint
- Radius: lg (card), md (button)
- Shadow: sm (card)

#### 5. Who We Help
- Background: Ivory
- Grid: 3-column → 1-column
- Padding: 120px → 72px
- Typography: eyebrow 13px; H2 40px → 28px; card H3 21px serif/600; card body 15px
- Image: none — typographic cards by design, no icons or stock photography
- CTA: text link "Explore →" per card
- Hover states: card lifts 5px, shadow deepens to md, a 3px Gold top border fades in; link shifts Teal Dark → Teal
- Radius: lg (cards)
- Shadow: sm at rest → md on hover

#### 6. Services
- Background: Ivory Alt
- Grid: 2×2 → 1-column
- Padding: 72px → 56px (compact section)
- Typography: numeral serif 15px/600 in Gold Dark; H3 22px serif/600; included-services line 13px italic, muted; body 15px
- Image: none — the Gold numeral substitutes for an icon, deliberately avoiding the lightbulb/handshake icon-pack cliché
- CTA: none — these are descriptive clusters, not individual conversion points
- Hover states: card lifts 3px, shadow deepens (no top-border accent here — that accent is reserved for the Who We Help cards so the two grids feel distinct, not duplicated)
- Radius: lg
- Shadow: sm → md

#### 7. Why Choose Be Skilled
- Background: Navy
- Grid: single-column list; each row is a micro-grid (90px numeral column / 1fr content) → 56px / 1fr on mobile
- Padding: 120px → 72px
- Typography: H2 centered, Ivory, 40px → 28px; row numeral serif 34px → 26px in Gold; row H3 21px serif, Ivory; row body 15.5px, Ivory Muted
- Image: none
- CTA: none
- Hover states: none — intentionally static; this is a manifesto list, not an interactive component
- Radius / Shadow: n/a

#### 8. Organizations We've Worked With
- Background: Ivory
- Grid: centered flex row, wraps on mobile
- Padding: 120px → 72px
- Typography: org names serif 21px/500, Charcoal Muted; tag chips 12.5px/600, uppercase
- Image: none — names are styled as text wordmarks rather than logo graphics. **Replace with real logo marks only once you have explicit permission from Navation, Udayan Care, and BHU to display them**; until then, text mentions are the lower-risk, still-credible option
- CTA: none
- Hover states: org name shifts Charcoal Muted → Navy — a small detail that signals these are real, verifiable names rather than decoration
- Radius: sm (tag chips only)
- Shadow: none

#### 9. Founder Section
- Background: Ivory Alt
- Grid: 2-column (.85fr / 1.15fr) → 1-column, photo stacks above text on mobile
- Padding: 72px → 56px
- Typography: eyebrow 13px; H2 32px serif; role line 15.5px/600 in Teal Dark; body 17px; emphasis line 20px serif italic with a 2px Gold left border
- Image: Navy Soft placeholder block with a caption noting the direction — candid, mid-session, not a posed studio headshot
- CTA: none — deliberately. This section's job is trust, not conversion; adding a button here would compete with the Final CTA's authority
- Hover states: none
- Radius: md (photo block)
- Shadow: md

#### 10. Impact Metrics
- Background: Navy
- Grid: 4-column → 2-column
- Padding: 72px → 56px
- Typography: number serif 42px in Gold; label sans 14px, Ivory Muted
- Image: none
- CTA: none
- Hover states: none
- Radius / Shadow: n/a

#### 11. Methodology
- Background: Ivory
- Grid: 4-column, connected by a thin horizontal line → 1-column stack with the connecting line removed on mobile
- Padding: 120px → 72px
- Typography: H2 centered 40px → 28px; step numeral in a circle, serif 15px/600; step H3 17px/600; step body 14.5px
- Image: none — numbered circle markers (Navy text, 1.5px Gold border) instead of icons
- CTA: none
- Hover states: none — restrained on purpose, consistent with the "Why Choose" section
- Radius: 50% (36px diameter circles)
- Shadow: none

#### 12. FAQ
- Background: Ivory Alt
- Grid: single column, max-width 820px, centered
- Padding: 72px → 56px
- Typography: H2 centered; question (summary) 17px/600, Navy; answer 15.5px, Charcoal Muted
- Image: none
- CTA: none
- Hover states: question row shows a pointer cursor; the "+" marker rotates 45° into an "×" on open (built with native `<details>/<summary>` — no JavaScript required, which also makes it accessible by default)
- Radius: n/a — divider-line style rather than boxed cards, to feel lighter after the denser sections above
- Shadow: none

#### 13. Final CTA
- Background: Navy
- Grid: single centered column
- Padding: 72px → 56px
- Typography: H2 38px serif, Ivory; body 17px, Ivory Muted; micro-caption 13.5px
- Image: none
- CTA: Gold-filled primary button — the only place on the page Gold is used as a button fill, reserved for this single highest-intent moment
- Hover states: lighter gold fill + lift + gold-glow shadow
- Radius: md
- Shadow: gold-glow on hover only

#### 14. Footer
- Background: Navy Deep
- Grid: 4-column (1.4fr / 1fr / 1fr / 1fr) → 2-column
- Padding: 80px top, 36px bottom (reduced gaps on mobile, same vertical rhythm)
- Typography: column headers 13px/600, Gold, uppercase; links/body 14.5px, Ivory Muted; logo 22px serif, Ivory
- Image: none
- CTA: none — the conversion ask has already been made above; the footer's job is navigation and credibility, not another pitch
- Hover states: links shift Ivory Muted → Ivory
- Radius / Shadow: n/a

---

**Breakpoint reference:** one primary breakpoint at **860px** governs the desktop → mobile collapse across every section above. This is intentional — a single, consistently-applied breakpoint is easier for a developer to implement correctly than five different ones scattered across sections.
