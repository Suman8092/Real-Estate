# Exact logo colors and their application

**Current scope:** Only the homepage uses the new black-and-white design. The other eight pages have been restored to their layouts and styles from commit `388c3a7`, before the site-wide redesign, using isolated styles in `css/legacy/`. The separately requested footer logo, single email and combined About paragraph are retained. New-palette browser checks apply only to the homepage.
The source is the existing **Premium Property Depot LLP** logo at `images/premium-property-depot-logo.png` (971 x 257 pixels). The actual image has shaded gold artwork and anti-aliased edges, rather than a single flat gold. The values below are exact existing pixel colors selected by frequency; they are not claimed to be an external official brand guide.

| Role | Exact HEX | Fully opaque pixel count | Sample coordinate (x, y) | Application |
| --- | --- | ---: | --- | --- |
| Logo charcoal | `#4C4B47` | 12,379 | (582, 22) | Secondary text on white, placeholders |
| Primary gold | `#9A6C14` | 162 | (160, 33) | White-section accents, links, borders, primary buttons with white text |
| Gold highlight | `#BE851A` | 129 | (221, 37) | Black-section accents, gold buttons with black text, inverse hover states |
| Black neutral | `#000000` | User-required neutral | Not sampled | Black sections and text on white |
| White neutral | `#FFFFFF` | User-required neutral | Not sampled | White sections and text on black |

## Reproducible extraction

`npm run brand:extract` decodes the full-resolution PNG with Sharp and counts exact RGB values only where alpha is 255. No resizing, averaging, clustering, color quantization, saturation/brightness adjustment or opacity change is used. The most frequent opaque RGB value is the charcoal. Among gold pixels satisfying R > G > B and R - B > 50, the two most frequent exact values are the two gold tokens.

The machine-readable evidence is in `brand-palette.json`, including the sample coordinates and source SHA-256:

`b9e98f2d94918d1427b553f60a80d5e4452e838de2d98ee9810532a95f56858e`

Generated `css/brand-tokens.css` supplies the same tokens to shared pages and, by inherited custom properties, the homepage Shadow DOM. Tailwind's color aliases use this palette too. Production builds regenerate the evidence and tokens before compiling CSS. `npm test` verifies the documented pixels and unchanged source logo, rejects unapproved literal colors or gradients in active custom stylesheets, and checks the text pairings below.

## Contrast and interaction rules

| Foreground / background | Contrast ratio |
| --- | ---: |
| White / black | 21.00:1 |
| Logo charcoal / white | 8.73:1 |
| Primary gold / white | 4.64:1 |
| Gold highlight / black | 6.56:1 |

These pairings exceed 4.5:1 for normal-size text. The lighter sampled gold is used against black; it is not used as small text on white. Primary gold buttons use white text; highlight-gold buttons use black text. Hover states invert between these verified pairings rather than generating a new shade. Focus outlines use the sampled gold appropriate to the background. No accent opacity or gradient variants are introduced.

## Section sequence and originality

The eight homepage body sections follow **white, black, white, black, white, black, white, black**. Other pages retain their previous section layouts and colors. The shared white header and footer have global navigation roles and are not counted as body sections. Cards remain part of their containing section, not additional numbered sections.

The visual identity uses an image-led split hero, left-aligned serif headings, a featured horizontal project presentation, paired open project rows, an asymmetric gallery, thin sampled-gold rules and a numbered process layout. Existing business copy, project facts, property images, navigation destinations and form behavior are retained. No complete reference-site layout, new marketing claims, inventory or dummy interactions are introduced.

The actual logo, source property images and external map retain their inherent colors. The restricted palette applies to the website's authored UI; it does not recolor photographs or control an external map provider's interface.
