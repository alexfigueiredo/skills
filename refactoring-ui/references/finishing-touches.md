# Finishing Touches

Read the matching rule below; use `scripts/find_examples.py --rule <id>` for its annotated figures. Figure paths are relative to this file.

<a id="supercharge-the-defaults"></a>

## Supercharge the defaults

**When:** A sound layout feels generic because its existing elements receive no attention.

**Change:** Refine list markers, quotation marks, link treatments and form-control styling.

**Why / how:** Liven up what is already there before adding anything. Replace list bullets with icons: checkmarks or arrows generically, or something content-specific such as a padlock for security features. Promote the quotation marks of a testimonial into large, colored visual elements. Style links with weight and color, or with a thick colored underline that partially overlaps the text. Apply a suitable brand treatment to existing accessible checkboxes and radio buttons; that alone moves a form from boring to considered.

**Watch for:** Preserve semantics, keyboard interaction and visible states; use established accessible controls rather than rebuilding behavior for decoration.

**Visuals:** [fig-220-247 (comparison)](figures/fig-220-247.webp), [fig-222-251 (comparison)](figures/fig-222-251.webp). Lookup: `supercharge-the-defaults`.

<a id="add-color-with-accent-borders"></a>

## Add color with accent borders

**When:** A restrained interface needs a small amount of identity or a clearer active state.

**Change:** Add a purposeful accent line to a card, alert, heading or active navigation item.

**Why / how:** A colored rectangle needs no illustration skill and makes an interface feel designed. Put an accent border across the top of a card, under the active nav item, along the side of an alert, as a short bar under a headline, or across the top of the whole layout.

**Watch for:** Avoid redundant accents everywhere; selected-state cues must remain perceivable in supported display modes.

**Visuals:** [fig-224-252 (comparison)](figures/fig-224-252.webp), [fig-225-253 (comparison)](figures/fig-225-253.webp). Lookup: `add-color-with-accent-borders`.

<a id="decorate-your-backgrounds"></a>

## Decorate your backgrounds

**When:** Hierarchy and spacing work but a surface still feels plain.

**Change:** Try a restrained background tone, gentle gradient or low-contrast decorative fragment.

**Why / how:** When hierarchy, spacing and type are right and the result is still plain, change a background. Give a panel or page section a different color, or a subtle gradient between two hues no more than about 30° apart. Add a low-contrast repeating pattern across the background or along a single edge. Place one simple geometric shape, a fragment of a pattern, or a simplified illustration such as a world map. Keep the contrast between decoration and background low so content stays readable.

**Watch for:** Keep decoration behind the content and avoid degrading contrast or implying meaningful data.

**Visuals:** [fig-229-258 (comparison)](figures/fig-229-258.webp), [fig-230-260 (example)](figures/fig-230-260.webp). Lookup: `decorate-your-backgrounds`.

<a id="dont-overlook-empty-states"></a>

## Don’t overlook empty states

**When:** A first-use screen shows only absence and gives no clear next action.

**Change:** Explain the feature and make its first useful action prominent, simplifying controls with no purpose yet.

**Why / how:** Features that depend on user content are usually designed with rich sample data, and the first thing a real user sees is an empty screen. Treat the empty state as a priority: an image or illustration, and an emphasized call to action toward the first step. Hide supporting UI such as tabs and filters until there is content for them to act on. It is the user's first interaction with the feature; make it inviting rather than plain.

**Watch for:** Distinguish first use from filtered zero results and errors; keep filters visible when users need them to recover.

**Visuals:** [fig-235-266 (before)](figures/fig-235-266.webp), [fig-235-267 (after)](figures/fig-235-267.webp). Lookup: `dont-overlook-empty-states`.

<a id="use-fewer-borders"></a>

## Use fewer borders

**When:** An interface looks boxed in by repeated outlines and dividers.

**Change:** Use spacing, surface tones or a restrained shadow where they communicate the same grouping.

**Why / how:** Borders separate, but too many make a design busy. Alternatives: a box shadow outlines an element more quietly (best when the element's color differs from the background); two slightly different background colors distinguish adjacent areas, and if a border is already paired with them it can usually go; and more spacing separates groups without adding any UI at all.

**Watch for:** Retain required control boundaries, focus indicators and separators needed for dense data or forced-colors modes.

**Visuals:** [fig-238-269 (before)](figures/fig-238-269.webp), [fig-241-272 (after)](figures/fig-241-272.webp). Lookup: `use-fewer-borders`.

<a id="think-outside-the-box"></a>

## Think outside the box

**When:** A dropdown, table or choice group is hard to scan in its default presentation.

**Change:** Reorganize related content with descriptions, grouped cells or selectable cards when it improves the task.

**Why / how:** Components do not have to look the way they usually do. A dropdown is a floating box and can hold sections, columns, supporting text and icons. A table column that need not be sortable can merge with a related column to introduce hierarchy, and cells can carry images and color. Important radio groups can become selectable cards. Constraints are useful, but conventions about a component's shape are not constraints.

**Watch for:** Preserve interaction semantics, keyboard behavior, data relationships and useful sorting; richer layouts need a narrow-screen plan.

**Visuals:** [fig-245-278 (before)](figures/fig-245-278.webp), [fig-246-279 (after)](figures/fig-246-279.webp). Lookup: `think-outside-the-box`.
