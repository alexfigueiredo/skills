# Layout and Spacing

Read the matching rule below; use `scripts/find_examples.py --rule <id>` for its annotated figures. Figure paths are relative to this file.

<a id="start-with-too-much-white-space"></a>

## Start with too much white space

**When:** A card or form feels cramped and every section barely fits.

**Change:** Start with generous spacing, then remove excess until grouping and density fit the task.

**Why / how:** Designers add white space only until something stops looking actively bad, so elements end up with the minimum breathing room. Start with far too much space and remove it until it looks right; what seems like too much on one element reads as just enough in a whole screen. Dense interfaces have their place (a dashboard that must show everything at once), but density should be a decision, not the default. Excess space is easier to notice and remove than missing space is to notice and add.

**Watch for:** Dense dashboards are valid when deliberate; whitespace must not hide essential information.

**Visuals:** [fig-066-062 (comparison)](figures/fig-066-062.webp). Lookup: `start-with-too-much-white-space`.

<a id="establish-a-spacing-and-sizing-system"></a>

## Establish a spacing and sizing system

**When:** Margins and padding vary arbitrarily across similar components.

**Change:** Replace arbitrary values with a spacing scale whose steps remain perceptibly different.

**Why / how:** Trialing values one pixel at a time is slow and produces inconsistency. A linear rule such as "multiples of 4px" does not help, because the difference that matters is relative: 12px to 16px is a 33% jump, while 500px to 520px is 4%. Build the scale so that adjacent values differ by at least about 25%. Start from a base of 16px (divides cleanly, browser default) and use factors and multiples of it, packed tightly at the small end and spreading out at the large end: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 640, 768. With a scale, "a bit more space" means the next value, and consistency appears on its own.

**Watch for:** Reuse existing tokens; the scale and percentage guidance here are starting points, not required replacements.

**Visuals:** [fig-070-066 (before)](figures/fig-070-066.webp), [fig-074-070 (after)](figures/fig-074-070.webp). Lookup: `establish-a-spacing-and-sizing-system`.

<a id="you-dont-have-to-fill-the-whole-screen"></a>

## You don’t have to fill the whole screen

**When:** Forms or content stretch across a wide viewport without gaining usefulness.

**Change:** Constrain content to a readable width; put supporting descriptions beside fields when useful.

**Why / how:** A wide display is not an obligation. If a form needs 600px, give it 600px; spreading content out makes it harder to read, and margin around the edges costs nothing. The same applies to sections: a full-width nav does not require full-width content. When a narrow design feels unbalanced in a wide layout, split it into columns (supporting text beside the form) rather than widening it. If a small layout is hard to design on a big canvas, shrink the canvas: design at about 400px first, then move to wider screens and fix only what felt like a compromise. The reverse also holds; do not cram when the content needs room.

**Watch for:** Wide tables and other content may legitimately need the available width; reflow at narrow sizes.

**Visuals:** [fig-076-071 (before)](figures/fig-076-071.webp), [fig-077-072 (after)](figures/fig-077-072.webp). Lookup: `you-dont-have-to-fill-the-whole-screen`.

<a id="grids-are-overrated"></a>

## Grids are overrated

**When:** A percentage sidebar or grid-bound card becomes too wide or too narrow at different viewports.

**Change:** Size stable elements for their content and let the main content flex within useful limits.

**Why / how:** A column grid is a constrained set of percentage widths, and percentages are wrong for elements that should not scale. A 25% sidebar grows uselessly on wide screens and collapses below its readable minimum on narrow ones. Give the sidebar a fixed width tuned to its contents and let the main area flex, using its own internal grid. Inside components, use percentages only when scaling is the intent. For things like a login card, set a max-width (say 500px) and let it shrink only when the viewport is narrower than that; grid-fraction sizing can otherwise make the card wider on medium screens than on large ones.

**Watch for:** This critiques rigid percentage layouts, not CSS Grid. Collapse or reflow sidebars when narrow space demands it.

**Visuals:** [fig-087-083 (comparison)](figures/fig-087-083.webp), [fig-087-084 (comparison)](figures/fig-087-084.webp). Lookup: `grids-are-overrated`.

<a id="relative-sizing-doesnt-scale"></a>

## Relative sizing doesn’t scale

**When:** Mobile headings dominate the screen, or button variants look like zoomed copies.

**Change:** Tune headline sizes and component padding independently across size variants.

**Why / how:** Defining a headline as 2.5em of body text assumes the ratio holds across screens. It does not: 18px body with a 45px headline on desktop becomes 14px body with a 20 to 24px headline on mobile, a ratio of 1.5 to 1.7. Large elements must shrink faster than small ones, so the spread between sizes narrows on small screens. The same applies within a component: button padding should not be a fixed multiple of its font size. Large buttons want proportionally more padding and small buttons less, so that they feel like different buttons rather than zoomed copies.

**Watch for:** Keep body text readable and hit targets usable; shrinking every dimension is not the goal.

**Visuals:** [fig-093-090 (before)](figures/fig-093-090.webp), [fig-093-091 (after)](figures/fig-093-091.webp). Lookup: `relative-sizing-doesnt-scale`.

<a id="avoid-ambiguous-spacing"></a>

## Avoid ambiguous spacing

**When:** Labels, headings, list items or horizontal controls appear connected to the wrong neighbors.

**Change:** Make spacing inside a group smaller than spacing between groups.

**Why / how:** Without a border or background to group elements, spacing does the grouping, and equal spacing says nothing. A form where the gap below each label equals the gap below each input does not show which label belongs to which input. Increase the space between groups so the inside gap is clearly smaller. The same mistake shows up as headings with too little space above them, list items spaced exactly one line-height apart, and horizontally laid out controls with even gaps. Whenever spacing connects a group, put more space around the group than inside it.

**Watch for:** Keep programmatic relationships such as label-to-input associations as well as visual grouping.

**Visuals:** [fig-097-096 (before)](figures/fig-097-096.webp), [fig-097-097 (after)](figures/fig-097-097.webp). Lookup: `avoid-ambiguous-spacing`.
