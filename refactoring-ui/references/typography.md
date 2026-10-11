# Typography

Read the matching rule below. `scripts/find_examples.py --rule <id>` returns its figures when it has them; open them when the rule concerns a visual quantity or you are unsure how far to take it. Figure paths are relative to this file.

<a id="use-a-type-scale"></a>

## Use a type scale

**When:** Similar text roles use many nearly identical font sizes.

**Change:** Define a small set of useful type sizes and reuse them by role.

**Why / how:** Without a system, every size from 10px to 24px ends up in use somewhere. A linear scale fails for the same reason as in spacing: small sizes need small steps, large sizes do not. Modular scales are useful starting points, but a fixed ratio can leave gaps between the sizes an interface actually needs. Fractional values are valid; choose sizes for their usefulness and rendered result. Hand-pick instead; a scale that works for most projects and lines up with the spacing scale is 12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72. Prefer stable type tokens, commonly expressed in rem, to avoid accidental nested em compounding: an element at 1.25em makes a nested .875em compute to 17.5px, which is on no scale.

**Watch for:** Prefer existing tokens and avoid accidental em compounding; intentional relative sizing and fractional values are valid.

**By mode:**
- operate, browse: One family; most text uses the small end of the scale (about 12–24 px).
- convert: A display face and a wide ratio between headline and body are appropriate.

**Visuals:** [use-a-type-scale-1 (before)](figures/use-a-type-scale-1.webp), [use-a-type-scale-4 (after)](figures/use-a-type-scale-4.webp). Lookup: `use-a-type-scale`.

<a id="choose-legible-typefaces"></a>

## Choose legible typefaces

**When:** Body text is hard to read or font selection is consuming the design process.

**Change:** Start with a legible family and verify its actual weights, proportions and language coverage.

**Why / how:** For interface text, a legible neutral sans-serif or a suitable system stack is a useful starting point. Shortcuts for picking a typeface: filter directories to families with 10 or more styles (5 or more weights with italics), as a rough indication of available weights; sort by popularity; look at what well-designed sites use. Families built for headlines have tight spacing and short lowercase letters, families built for small text have wider spacing and taller x-heights, so avoid condensed or short x-height faces for body copy.

**Watch for:** Popularity and number of styles are selection shortcuts, not quality guarantees; variable fonts need not have many files.

**Visuals:** [choose-legible-typefaces-3 (comparison)](figures/choose-legible-typefaces-3.webp). Lookup: `choose-legible-typefaces`.

<a id="limit-line-length"></a>

## Limit line length

**When:** Paragraphs span too much of the page and are tiring to read.

**Change:** Constrain reading measure independently of the wider layout.

**Why / how:** Lines sized to the layout rather than to reading are usually too long. Aim for 45 to 75 characters per line, which is roughly 20 to 35em of width. When paragraphs sit beside images or wide components, keep the paragraphs narrow even though the content area is wider; mixed widths look more polished than long lines.

**Watch for:** The 45-75 character range is a prose heuristic; judge the actual script, font, device and content.

**By mode:**
- read: Keep body text at about 60–75 characters per line and near 16 px.

**Visuals:** [limit-line-length-4 (before)](figures/limit-line-length-4.webp), [limit-line-length-5 (after)](figures/limit-line-length-5.webp). Lookup: `limit-line-length`.

<a id="align-mixed-sizes-on-baseline"></a>

## Align mixed sizes on the baseline

**When:** A title and smaller adjacent actions look vertically misaligned.

**Change:** Align mixed text sizes on their baseline.

**Why / how:** Mixed font sizes on one line (a card title next to smaller actions) look off when vertically centered, because their baselines no longer align. Align them on the baseline, the line the letters sit on, which the eye already uses as a reference.

**Watch for:** Use optical or center alignment when it suits icons or non-text controls; inspect the rendered result.

**Visuals:** [align-mixed-sizes-on-baseline-2 (before)](figures/align-mixed-sizes-on-baseline-2.webp), [align-mixed-sizes-on-baseline-4 (after)](figures/align-mixed-sizes-on-baseline-4.webp). Lookup: `align-mixed-sizes-on-baseline`.

<a id="set-line-height-by-size-and-measure"></a>

## Set line-height by size and measure

**When:** Body lines are hard to track, or a wrapped heading feels disconnected.

**Change:** Adjust line-height to both line length and font size, usually giving small or wide body text more room.

**Why / how:** Line spacing exists so the eye can find the next line after wrapping. Longer lines need taller line-height: about 1.5 for narrow columns, up to 2 for wide ones. Larger text needs less: small text benefits from extra spacing, large headlines can sit at a line-height of 1. Line-height is proportional to line length and inversely proportional to font size.

**Watch for:** Test actual glyphs and wrapping; tight headline leading must not clip accents or overlap lines.

**Visuals:** [set-line-height-by-size-and-measure-4 (comparison)](figures/set-line-height-by-size-and-measure-4.webp), [set-line-height-by-size-and-measure-5 (comparison)](figures/set-line-height-by-size-and-measure-5.webp). Lookup: `set-line-height-by-size-and-measure`.

<a id="color-links-only-where-needed"></a>

## Color links only where needed

**When:** Repeated colored links overwhelm cards or navigation.

**Change:** Establish hierarchy with weight and neutral tones where the component context already indicates interaction.

**Why / how:** A colored, underlined link stands out in a paragraph of plain text. In an interface where most things are links, that treatment is overwhelming. Emphasize most links with a heavier weight or a darker color, and keep ancillary links quieter when context identifies them as interactive. Preserve a visible keyboard-focus state and useful hover feedback. Inline prose links must remain identifiable without requiring hover.

**Watch for:** Keep links identifiable without hover, preserve keyboard focus, and distinguish inline prose links from surrounding text.

**Visuals:** [color-links-only-where-needed-2 (before)](figures/color-links-only-where-needed-2.webp), [color-links-only-where-needed-3 (after)](figures/color-links-only-where-needed-3.webp). Lookup: `color-links-only-where-needed`.

<a id="align-for-reading"></a>

## Align for reading

**When:** Long centered text or uneven numeric columns are hard to scan.

**Change:** Align prose with its reading direction and numeric columns for comparison; keep centered text brief.

**Why / how:** Text aligns with its language's direction, so for English almost everything is left-aligned. Centering works for headlines and short independent blocks; anything beyond two or three lines looks better left-aligned, and a block that is too long to center is often best fixed by shortening the copy. Right-align numbers in tables so the decimals line up and values compare at a glance. Justified text needs hyphenation enabled to avoid rivers of white space, and even then left alignment is a fine alternative.

**Watch for:** Account for RTL and locale-specific number formats. Justification needs careful hyphenation and language support.

**Visuals:** [align-for-reading-3 (comparison)](figures/align-for-reading-3.webp), [align-for-reading-5 (comparison)](figures/align-for-reading-5.webp). Lookup: `align-for-reading`.

<a id="adjust-tracking-by-size-and-case"></a>

## Adjust tracking by size and case

**When:** Headlines feel loose or all-caps labels feel crowded.

**Change:** Keep body tracking near the typeface default, testing tighter headlines or wider uppercase text when useful.

**Why / how:** Trust the typeface designer and leave letter-spacing alone, with two exceptions. A family designed for legibility at small sizes (Open Sans) has wide spacing; tighten it when using the family for headlines to mimic a purpose-built headline face. The reverse does not work; headline faces rarely survive small sizes even with added spacing. All-caps text loses the ascenders and descenders that make lowercase words distinguishable, so widen its letter-spacing to restore legibility.

**Watch for:** Tracking adjustments are font- and script-dependent; do not apply Latin uppercase habits universally.

**Visuals:** [adjust-tracking-by-size-and-case-3 (comparison)](figures/adjust-tracking-by-size-and-case-3.webp), [adjust-tracking-by-size-and-case-5 (comparison)](figures/adjust-tracking-by-size-and-case-5.webp). Lookup: `adjust-tracking-by-size-and-case`.
