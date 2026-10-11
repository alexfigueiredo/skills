# Layout

Read the matching rule below. `scripts/find_examples.py --rule <id>` returns its figures when it has them; open them when the rule concerns a visual quantity or you are unsure how far to take it. Figure paths are relative to this file.

<a id="start-generous-then-tighten"></a>

## Start generous, then tighten

**When:** A card or form feels cramped and every section barely fits.

**Change:** Start with generous spacing, then remove excess until grouping and density fit the task.

**Why / how:** Designers add white space only until something stops looking actively bad, so elements end up with the minimum breathing room. Start with far too much space and remove it until it looks right; what seems like too much on one element reads as just enough in a whole screen. Dense interfaces have their place (a dashboard that must show everything at once), but density should be a decision, not the default. Excess space is easier to notice and remove than missing space is to notice and add.

**Watch for:** Dense dashboards are valid when deliberate; whitespace must not hide essential information.

**By mode:**
- operate, browse: Dense layouts are often correct; start from the density the task needs and check the grouping.

**Visuals:** [start-generous-then-tighten-1 (comparison)](figures/start-generous-then-tighten-1.webp). Lookup: `start-generous-then-tighten`.

<a id="use-a-spacing-scale"></a>

## Use a spacing scale

**When:** Margins and padding vary arbitrarily across similar components.

**Change:** Replace arbitrary values with a spacing scale whose steps remain perceptibly different.

**Why / how:** Trialing values one pixel at a time is slow and produces inconsistency. A linear rule such as "multiples of 4px" does not help, because the difference that matters is relative: 12px to 16px is a 33% jump, while 500px to 520px is 4%. Build the scale so that adjacent values differ by at least about 25%. Start from a base of 16px (divides cleanly, browser default) and use factors and multiples of it, packed tightly at the small end and spreading out at the large end: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 640. With a scale, "a bit more space" means the next value, and consistency appears on its own.

**Watch for:** Reuse existing tokens; the scale and percentage guidance here are starting points, not required replacements.

**Visuals:** [use-a-spacing-scale-1 (before)](figures/use-a-spacing-scale-1.webp), [use-a-spacing-scale-5 (after)](figures/use-a-spacing-scale-5.webp). Lookup: `use-a-spacing-scale`.

<a id="avoid-ambiguous-spacing"></a>

## Avoid ambiguous spacing

**When:** Labels, headings, list items or horizontal controls appear connected to the wrong neighbors.

**Change:** Make spacing inside a group smaller than spacing between groups.

**Why / how:** Without a border or background to group elements, spacing does the grouping, and equal spacing says nothing. A form where the gap below each label equals the gap below each input does not show which label belongs to which input. Increase the space between groups so the inside gap is clearly smaller. The same mistake shows up as headings with too little space above them, list items spaced exactly one line-height apart, and horizontally laid out controls with even gaps. Whenever spacing connects a group, put more space around the group than inside it.

**Watch for:** Keep programmatic relationships such as label-to-input associations as well as visual grouping.

**Visuals:** [avoid-ambiguous-spacing-2 (before)](figures/avoid-ambiguous-spacing-2.webp), [avoid-ambiguous-spacing-3 (after)](figures/avoid-ambiguous-spacing-3.webp). Lookup: `avoid-ambiguous-spacing`.

<a id="group-with-space-not-borders"></a>

## Group with space, not borders

**When:** An interface looks boxed in by repeated outlines and dividers.

**Change:** Use spacing, surface tones or a restrained shadow where they communicate the same grouping.

**Why / how:** Borders separate, but too many make a design busy. Alternatives: a box shadow outlines an element more quietly (best when the element's color differs from the background); two slightly different background colors distinguish adjacent areas, and if a border is already paired with them it can usually go; and more spacing separates groups without adding any UI at all.

**Watch for:** Retain required control boundaries, focus indicators and separators needed for dense data or forced-colors modes.

**Visuals:** [group-with-space-not-borders-1 (before)](figures/group-with-space-not-borders-1.webp), [group-with-space-not-borders-4 (after)](figures/group-with-space-not-borders-4.webp). Lookup: `group-with-space-not-borders`.

<a id="constrain-content-width"></a>

## Constrain content width

**When:** Forms or content stretch across a wide viewport without gaining usefulness.

**Change:** Constrain content to a readable width; put supporting descriptions beside fields when useful.

**Why / how:** A wide display is not an obligation. If a form needs 600px, give it 600px; spreading content out makes it harder to read, and margin around the edges costs nothing. The same applies to sections: a full-width nav does not require full-width content. When a narrow design feels unbalanced in a wide layout, split it into columns (supporting text beside the form) rather than widening it. If a small layout is hard to design on a big canvas, shrink the canvas: design at about 400px first, then move to wider screens and fix only what felt like a compromise. The reverse also holds; do not cram when the content needs room.

**Watch for:** Wide tables and other content may legitimately need the available width; reflow at narrow sizes.

**By mode:**
- browse: Item grids can use the full width; constrain the text and filters instead.
- convert, experience: Key art and section backgrounds can run full width; constrain the text inside them.

**Visuals:** [constrain-content-width-1 (before)](figures/constrain-content-width-1.webp), [constrain-content-width-2 (after)](figures/constrain-content-width-2.webp). Lookup: `constrain-content-width`.

<a id="fix-stable-widths"></a>

## Fix stable widths, flex the rest

**When:** A percentage sidebar or grid-bound card becomes too wide or too narrow at different viewports.

**Change:** Size stable elements for their content and let the main content flex within useful limits.

**Why / how:** A column grid is a constrained set of percentage widths, and percentages are wrong for elements that should not scale. A 25% sidebar grows uselessly on wide screens and collapses below its readable minimum on narrow ones. Give the sidebar a fixed width tuned to its contents and let the main area flex, using its own internal grid. Inside components, use percentages only when scaling is the intent. For things like a login card, set a max-width (say 500px) and let it shrink only when the viewport is narrower than that; grid-fraction sizing can otherwise make the card wider on medium screens than on large ones.

**Watch for:** This critiques rigid percentage layouts, not CSS Grid. Collapse or reflow sidebars when narrow space demands it. Where a component should switch layout is covered by `switch-layout-by-available-width`.

**Visuals:** [fix-stable-widths-6 (comparison)](figures/fix-stable-widths-6.webp), [fix-stable-widths-7 (comparison)](figures/fix-stable-widths-7.webp). Lookup: `fix-stable-widths`.

<a id="switch-layout-by-available-width"></a>

## Switch layout by available width

**When:** A component keeps its wide layout inside a narrow column, or the layout changes on device type or orientation instead of on the space it has.

**Change:** Change a component's layout at the width it receives: container queries for reusable components, viewport queries for the page shell.

**Why / how:** A card in a narrow sidebar of a wide window needs its narrow layout, and a phone in landscape can be as wide as a small desktop window. Device type and orientation do not tell you the available width. Find where the content breaks (a title wrapping into its button, a table that needs horizontal scrolling) and switch there, not at a device preset. In CSS, use `@container` for components and `@media (width …)` for the shell. Outside the web, use the platform equivalent: `LayoutBuilder` in Flutter, `GeometryReader` or size classes in SwiftUI, window size classes on Android.

**Watch for:** Check widths just below and above each switch, a narrow container inside a wide window, and long content such as long names and translated labels. Do not lock orientation to avoid layout work.

<a id="tune-sizes-per-context"></a>

## Tune sizes per screen size and variant

**When:** Mobile headings dominate the screen, or button variants look like zoomed copies.

**Change:** Tune headline sizes and component padding independently across size variants.

**Why / how:** Defining a headline as 2.5em of body text assumes the ratio holds across screens. It does not: 18px body with a 45px headline on desktop becomes 14px body with a 20 to 24px headline on mobile, a ratio of 1.5 to 1.7. Large elements must shrink faster than small ones, so the spread between sizes narrows on small screens. The same applies within a component: button padding should not be a fixed multiple of its font size. Large buttons want proportionally more padding and small buttons less, so that they feel like different buttons rather than zoomed copies.

**Watch for:** Keep body text readable and hit targets usable; shrinking every dimension is not the goal.

**By mode:**
- read: Keep body text at 16 px or more on phones; shrink only headings.

**Visuals:** [tune-sizes-per-context-2 (before)](figures/tune-sizes-per-context-2.webp), [tune-sizes-per-context-3 (after)](figures/tune-sizes-per-context-3.webp). Lookup: `tune-sizes-per-context`.

<a id="keep-navigation-reachable"></a>

## Keep navigation reachable

**When:** On narrow screens, navigation items are cut off at the edge, hidden without a cue, or the collapsed navigation drops destinations.

**Change:** Show that more items exist or move the extra items into a labeled menu, keeping the same destinations, order, labels and active state.

**Why / how:** A scrolling tab bar that cuts "Leaderboard" to "Leaderbo" with no other cue hides part of the navigation. Fit the items (fewer top-level items, shorter labels), show the overflow (a fade at the edge with the next item partly visible), or move the extra items into a "More" menu. When a sidebar becomes a bottom bar, rail or menu, keep the same destinations in the same order and mark the active one.

**Watch for:** The active item must be visible on load; scroll it into view if needed. Targets need at least 24×24 CSS px; the platform recommendations are 44 pt on iOS and 48 dp on Android.
