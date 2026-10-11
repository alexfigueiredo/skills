# Color

Read the matching rule below. `scripts/find_examples.py --rule <id>` returns its figures when it has them; open them when the rule concerns a visual quantity or you are unsure how far to take it. Figure paths are relative to this file.

<a id="use-a-relational-color-model"></a>

## Use a relational color model

**When:** Related colors are difficult to reason about when editing raw color values.

**Change:** Use a color model that exposes useful relationships and retain the project's palette format.

**Why / how:** In hex or RGB, visually related colors look unrelated in code. HSL exposes three editable channels: hue (position on the wheel, 0° red, 120° green, 240° blue), saturation (0% grey, 100% vivid) and lightness (0% black, 50% the pure hue, 100% white). HSL is not HSB: 100% brightness in HSB is white only at 0% saturation, while at full saturation it equals 50% lightness in HSL. This explains the HSL examples in the figures, not a requirement to migrate a working palette. OKLCH exposes perceived lightness, chroma and hue; preserve the color format and tokens used by the project. Its hue angles differ from HSL, so do not copy HSL hue adjustments numerically into OKLCH. See [MDN on OKLCH](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch).

**Watch for:** HSL explains the examples; it is not mandatory. Preserve an existing OKLCH or other color workflow.

**Visuals:** [use-a-relational-color-model-1 (diagram)](figures/use-a-relational-color-model-1.webp), [use-a-relational-color-model-2 (diagram)](figures/use-a-relational-color-model-2.webp). Lookup: `use-a-relational-color-model`.

<a id="plan-full-color-ranges"></a>

## Plan full color ranges

**When:** A small palette cannot support readable text, surfaces and semantic states.

**Change:** Provide tonal ranges for neutrals, brand colors and the accent roles the product actually needs.

**Why / how:** Five-color palette generators cannot build a real interface. A working palette has three parts. Greys: 8 to 10 shades, because text, backgrounds, panels and controls are almost all grey, and 3 or 4 shades always leave you wanting one in between. Start from a very dark grey rather than true black, which looks unnatural. Primary: one or two colors with 5 to 10 shades, from ultra-light tints for alert backgrounds to dark shades for text. Accents: a highlight color for new features, semantic colors (red for destructive, yellow for warning, green for positive), and categorical colors for charts, calendars or tags, each with its own shades. Ten colors with 5 to 10 shades each is normal for a complex product.

**Watch for:** Do not create unused palette families or overwhelm the interface with saturated colors.

**Visuals:** [plan-full-color-ranges-2 (before)](figures/plan-full-color-ranges-2.webp), [plan-full-color-ranges-3 (after)](figures/plan-full-color-ranges-3.webp). Lookup: `plan-full-color-ranges`.

<a id="define-shade-scales-up-front"></a>

## Define shade scales up front

**When:** Components accumulate slightly different ad hoc lightened and darkened colors.

**Change:** Choose useful dark, middle and light anchors, fill a stable shade scale, and name semantic roles.

**Why / how:** Generating shades with `lighten` and `darken` at the point of use produces dozens of nearly identical blues. Define a fixed set instead. Pick the base first: for primaries and accents, a shade that works as a button background. Then the edges: the darkest shade is usually text, the lightest a tinted background, and an alert component exercises both, so design one to find them. Keep the hue, adjust saturation and lightness. Fill the gaps with nine steps, 100 to 900 with the base at 500: choose 300 and 700 as the midpoint compromises, then 200, 400, 600 and 800 the same way. Greys follow the same process, with the darkest grey chosen as the darkest text and the lightest as a subtle off-white background. Trust the eye over the math afterwards, but resist adding new shades once the system exists.

**Watch for:** Judge shades in real components and both supported themes; the displayed base shade is not a contrast guarantee.

**Visuals:** [define-shade-scales-up-front-3 (example)](figures/define-shade-scales-up-front-3.webp), [define-shade-scales-up-front-4 (diagram)](figures/define-shade-scales-up-front-4.webp), [define-shade-scales-up-front-5 (diagram)](figures/define-shade-scales-up-front-5.webp), [define-shade-scales-up-front-6 (diagram)](figures/define-shade-scales-up-front-6.webp). Lookup: `define-shade-scales-up-front`.

<a id="keep-saturation-at-the-extremes"></a>

## Keep saturation at the light and dark ends

**When:** Light and dark palette shades look washed out or muddy.

**Change:** Adjust saturation or chroma and sometimes hue while shaping the tonal range.

**Why / how:** As lightness moves toward 0% or 100%, the same saturation looks weaker, so light and dark shades wash out unless saturation is raised as they move away from 50%. When the base is already fully saturated, use perceived brightness instead. The examples illustrate hue-dependent brightness with the approximation √(0.299r² + 0.587g² + 0.114b²) / 255 (not the WCAG contrast formula); yellow, cyan and magenta (60°, 180°, 300°) are the bright peaks, red, green and blue (0°, 120°, 240°) the dark troughs. To lighten a color without washing it out, rotate its hue toward the nearest bright hue; to darken, toward the nearest dark hue. This is how a yellow palette gets warm, rich dark shades (toward orange) instead of brown ones. Combine hue rotation with lightness changes, and keep rotations within 20 to 30° or the color stops reading as the same color.

**Watch for:** The HSL brightness approximation shown in the examples is not WCAG relative luminance. HSL hue offsets do not transfer directly to OKLCH.

**Visuals:** [keep-saturation-at-the-extremes-11 (comparison)](figures/keep-saturation-at-the-extremes-11.webp). Lookup: `keep-saturation-at-the-extremes`.

<a id="tint-neutrals"></a>

## Tint neutrals

**When:** Neutral surfaces feel disconnected from the intended warm or cool personality.

**Change:** Use a coherent, subtly tinted neutral ramp when it serves the design.

**Why / how:** True grey has 0% saturation, but most greys that look good carry some. Blue tint reads cool, yellow or orange reads warm, the same way light bulbs do. Apply the same saturation correction at the light and dark ends so the temperature stays consistent. How much tint is a matter of taste, from a slight lean to a strong one.

**Watch for:** Neutral greys and black are valid choices; preserve the existing brand and measure text contrast.

**Visuals:** [tint-neutrals-3 (comparison)](figures/tint-neutrals-3.webp), [tint-neutrals-4 (example)](figures/tint-neutrals-4.webp). Lookup: `tint-neutrals`.

<a id="use-dark-text-on-light-tints"></a>

## Use dark text on light tints

**When:** Readable status colors become too visually heavy, or colored text loses its character.

**Change:** Try dark colored text on a light tint, checking actual foreground-background contrast.

**Why / how:** For WCAG AA, normal text needs at least 4.5:1 contrast. The 3:1 large-text threshold applies at 18pt (24 CSS px) regular or 14pt (about 18.67 CSS px) bold, not at 18px regular. Measure the actual foreground/background pair without rounding a failing ratio up; see [W3C contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). Dark text on light backgrounds passes easily; color is where it gets hard. White text on a colored background needs a surprisingly dark color to pass, which drags attention to elements that should be quiet. Flip the contrast: dark colored text on a light tint of the same color keeps the meaning while staying calm. Colored text on a colored background (secondary text inside a dark panel) rarely passes by adjusting lightness alone without approaching white; rotate the hue toward a brighter color (cyan, magenta, yellow) to gain contrast while staying colorful.

**Watch for:** Normal text needs 4.5:1; large text needs 3:1 at 18pt/24px regular or 14pt/about 18.67px bold. Do not round a failing ratio up.

**Visuals:** [use-dark-text-on-light-tints-2 (before)](figures/use-dark-text-on-light-tints-2.webp), [use-dark-text-on-light-tints-3 (example)](figures/use-dark-text-on-light-tints-3.webp), [use-dark-text-on-light-tints-4 (after)](figures/use-dark-text-on-light-tints-4.webp). Lookup: `use-dark-text-on-light-tints`.

<a id="dont-rely-on-color-alone"></a>

## Don't rely on color alone

**When:** Trends, statuses or chart categories are distinguishable only by hue.

**Change:** Pair color with labels, signs, icons, patterns or another independent signal.

**Why / how:** Red-versus-green trends are invisible to a colorblind user. Pair color with another signal, such as an up or down icon. For chart series, add labels or other independent cues and use light-versus-dark differences to supplement hue; light and dark are far easier to tell apart than two colors. Color should reinforce what the design already says, never be the only carrier.

**Watch for:** Lightness differences help but do not alone identify every chart series; preserve labels and values.

**Visuals:** [dont-rely-on-color-alone-1 (before)](figures/dont-rely-on-color-alone-1.webp), [dont-rely-on-color-alone-2 (after)](figures/dont-rely-on-color-alone-2.webp). Lookup: `dont-rely-on-color-alone`.

<a id="design-dark-themes-separately"></a>

## Design dark themes separately

**When:** A dark theme was made by inverting the light palette, and surfaces blur together, text glares or brand colors vibrate.

**Change:** Make higher layers lighter instead of relying on shadows, measure every contrast pair again, and tune text and brand colors for the dark surfaces.

**Why / how:** Shadows barely show on dark backgrounds, so elevation comes from surface tone: each raised layer (card, menu, dialog) is one step lighter than the layer below (`layer-flat-designs-with-tone`). Pure white body text on near-black has more contrast than reading needs; an off-white step of the neutral ramp is easier to read. Saturated colors that work on white can vibrate on dark surfaces; use a lighter, less saturated step of the same hue. Light text on dark looks heavier and thin weights can break up, so check line-height, tracking and weight in the rendered dark theme.

**Watch for:** Measure text, icon and focus colors in both themes; a pair that passes in light mode can fail in dark mode. Keep the meaning of status colors the same in both themes. Choose dark or light as the default from where and when the product is used.
