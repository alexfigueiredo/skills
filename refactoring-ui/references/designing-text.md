# Designing Text

Read the matching rule below; use `scripts/find_examples.py --rule <id>` for its annotated figures. Figure paths are relative to this file.

<a id="establish-a-type-scale"></a>

## Establish a type scale

**When:** Similar text roles use many nearly identical font sizes.

**Change:** Define a small set of useful type sizes and reuse them by role.

**Why / how:** Without a system, every size from 10px to 24px ends up in use somewhere. A linear scale fails for the same reason as in spacing: small sizes need small steps, large sizes do not. Modular scales are useful starting points, but a fixed ratio can leave gaps between the sizes an interface actually needs. Fractional values are valid; choose sizes for their usefulness and rendered result. Hand-pick instead; a scale that works for most projects and lines up with the spacing scale is 12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72. Prefer stable type tokens, commonly expressed in rem, to avoid accidental nested em compounding: an element at 1.25em makes a nested .875em compute to 17.5px, which is on no scale.

**Watch for:** Prefer existing tokens and avoid accidental em compounding; intentional relative sizing and fractional values are valid.

**Visuals:** [fig-102-101 (before)](figures/fig-102-101.webp), [fig-106-104 (after)](figures/fig-106-104.webp). Lookup: `establish-a-type-scale`.

<a id="use-good-fonts"></a>

## Use good fonts

**When:** Body text is hard to read or font selection is consuming the design process.

**Change:** Start with a legible family and verify its actual weights, proportions and language coverage.

**Why / how:** For interface text, a legible neutral sans-serif or a suitable system stack is a useful starting point. Shortcuts for picking a typeface: filter directories to families with 10 or more styles (5 or more weights with italics), as a rough indication of available weights; sort by popularity; look at what well-designed sites use. Families built for headlines have tight spacing and short lowercase letters, families built for small text have wider spacing and taller x-heights, so avoid condensed or short x-height faces for body copy.

**Watch for:** Popularity and number of styles are selection shortcuts, not quality guarantees; variable fonts need not have many files.

**Visuals:** [fig-110-108 (comparison)](figures/fig-110-108.webp). Lookup: `use-good-fonts`.

<a id="keep-your-line-length-in-check"></a>

## Keep your line length in check

**When:** Paragraphs span too much of the page and are tiring to read.

**Change:** Constrain reading measure independently of the wider layout.

**Why / how:** Lines sized to the layout rather than to reading are usually too long. Aim for 45 to 75 characters per line, which is roughly 20 to 35em of width. When paragraphs sit beside images or wide components, keep the paragraphs narrow even though the content area is wider; mixed widths look more polished than long lines.

**Watch for:** The 45-75 character range is a prose heuristic; judge the actual script, font, device and content.

**Visuals:** [fig-115-114 (before)](figures/fig-115-114.webp), [fig-116-115 (after)](figures/fig-116-115.webp). Lookup: `keep-your-line-length-in-check`.

<a id="baseline-not-center"></a>

## Baseline, not center

**When:** A title and smaller adjacent actions look vertically misaligned.

**Change:** Align mixed text sizes on their baseline.

**Why / how:** Mixed font sizes on one line (a card title next to smaller actions) look off when vertically centered, because their baselines no longer align. Align them on the baseline, the line the letters sit on, which the eye already uses as a reference.

**Watch for:** Use optical or center alignment when it suits icons or non-text controls; inspect the rendered result.

**Visuals:** [fig-119-117 (before)](figures/fig-119-117.webp), [fig-120-119 (after)](figures/fig-120-119.webp). Lookup: `baseline-not-center`.

<a id="line-height-is-proportional"></a>

## Line-height is proportional

**When:** Body lines are hard to track, or a wrapped heading feels disconnected.

**Change:** Adjust line-height to both line length and font size, usually giving small or wide body text more room.

**Why / how:** Line spacing exists so the eye can find the next line after wrapping. Longer lines need taller line-height: about 1.5 for narrow columns, up to 2 for wide ones. Larger text needs less: small text benefits from extra spacing, large headlines can sit at a line-height of 1. Line-height is proportional to line length and inversely proportional to font size.

**Watch for:** Test actual glyphs and wrapping; tight headline leading must not clip accents or overlap lines.

**Visuals:** [fig-124-123 (comparison)](figures/fig-124-123.webp), [fig-125-124 (comparison)](figures/fig-125-124.webp). Lookup: `line-height-is-proportional`.

<a id="not-every-link-needs-a-color"></a>

## Not every link needs a color

**When:** Repeated colored links overwhelm cards or navigation.

**Change:** Establish hierarchy with weight and neutral tones where the component context already indicates interaction.

**Why / how:** A colored, underlined link stands out in a paragraph of plain text. In an interface where most things are links, that treatment is overwhelming. Emphasize most links with a heavier weight or a darker color, and keep ancillary links quieter when context identifies them as interactive. Preserve a visible keyboard-focus state and useful hover feedback. Inline prose links must remain identifiable without requiring hover.

**Watch for:** Keep links identifiable without hover, preserve keyboard focus, and distinguish inline prose links from surrounding text.

**Visuals:** [fig-126-126 (before)](figures/fig-126-126.webp), [fig-127-127 (after)](figures/fig-127-127.webp). Lookup: `not-every-link-needs-a-color`.

<a id="align-with-readability-in-mind"></a>

## Align with readability in mind

**When:** Long centered text or uneven numeric columns are hard to scan.

**Change:** Align prose with its reading direction and numeric columns for comparison; keep centered text brief.

**Why / how:** Text aligns with its language's direction, so for English almost everything is left-aligned. Centering works for headlines and short independent blocks; anything beyond two or three lines looks better left-aligned, and a block that is too long to center is often best fixed by shortening the copy. Right-align numbers in tables so the decimals line up and values compare at a glance. Justified text needs hyphenation enabled to avoid rivers of white space, and even then left alignment is a fine alternative.

**Watch for:** Account for RTL and locale-specific number formats. Justification needs careful hyphenation and language support.

**Visuals:** [fig-129-131 (comparison)](figures/fig-129-131.webp), [fig-130-133 (comparison)](figures/fig-130-133.webp). Lookup: `align-with-readability-in-mind`.

<a id="use-letter-spacing-effectively"></a>

## Use letter-spacing effectively

**When:** Headlines feel loose or all-caps labels feel crowded.

**Change:** Keep body tracking near the typeface default, testing tighter headlines or wider uppercase text when useful.

**Why / how:** Trust the typeface designer and leave letter-spacing alone, with two exceptions. A family designed for legibility at small sizes (Open Sans) has wide spacing; tighten it when using the family for headlines to mimic a purpose-built headline face. The reverse does not work; headline faces rarely survive small sizes even with added spacing. All-caps text loses the ascenders and descenders that make lowercase words distinguishable, so widen its letter-spacing to restore legibility.

**Watch for:** Tracking adjustments are font- and script-dependent; do not apply Latin uppercase habits universally.

**Visuals:** [fig-133-138 (comparison)](figures/fig-133-138.webp), [fig-134-140 (comparison)](figures/fig-134-140.webp). Lookup: `use-letter-spacing-effectively`.
