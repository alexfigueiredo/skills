---
name: refactoring-ui
description: "Design or critique interfaces using practical rules and annotated visual examples for hierarchy, spacing, typography, color, depth, imagery and finishing touches. Use for visual UI improvements, new screens and design-system decisions."
disable-model-invocation: true
---

# Refactoring UI

Use the principles and visual examples to make concrete design decisions. Preserve the product's purpose, existing tokens, brand and component behavior. Match the user's scope: a critique produces findings; an implementation request authorizes the relevant edits.

## Working loop

1. **Inspect the actual interface.** Read the relevant components and tokens, then look at a rendered screen, supplied screenshot or mockup. Identify the primary content and action. If no visual evidence is available, distinguish code-based observations from unverified visual judgments.
2. **Find the relevant principle.** Search by the visible problem using the helper below, or select a topic from the table. Start with the few rules that explain the problem; load additional topics when the task warrants them.
3. **Read and look.** Read the matching rule in its topic reference, including its caution. Open the returned image paths with an image-viewing tool. Inspect both members of a before/after pair; a `comparison` image already contains multiple views. A filename, caption or Markdown link alone is not visual inspection.
4. **Apply the mechanism.** Explain what changes the hierarchy or readability in the example, then translate that mechanism into the current product's tokens and content. The figures illustrate individual principles; their colors, controls and typography are not complete implementation or accessibility specifications.
5. **Verify the result.** For implementation, compare before/after screenshots in the affected states and viewport sizes. Check relevant wrapping, grouping, contrast and interaction behavior. Report the changes and the verification actually performed. For critique, give prioritized findings with the element, observed problem and specific recommended change.

For a **new screen**, start with its smallest useful feature and real content. Explore structure before decoration, using grayscale when helpful; reuse the existing shell in established products. Build the requested behavior and review the rendered result.

For a **design system**, inspect the current tokens first. Use the spacing, type, color and elevation references to fill demonstrated gaps. Values in the examples are starting points, not a replacement for a working system.

For a **broad visual review**, walk every line of [Rules at a glance](#rules-at-a-glance) against the screen, in order: hierarchy, grouping, typography, color, depth, imagery and finishing touches. Prioritize the issues that affect understanding or task completion, and state any areas you could not inspect.

## Rules at a glance

One line per rule: the symptom, then the change. A broad review walks every line; a focused task reads the matching rule in its reference and looks at its figures.

**Starting from scratch** ([reference](references/starting-from-scratch.md))

- `start-with-a-feature-not-a-layout`: A new screen is stuck on navigation, page chrome or the app shell → Design the smallest useful feature around its real data and actions before choosing the surrounding shell.
- `detail-comes-later`: Colors, fonts and shadows are slowing early layout decisions → Explore structure in low fidelity or grayscale, then add detail once the hierarchy works.
- `dont-design-too-much`: Mockups imply features or edge cases that are outside the current delivery scope → Design and implement one useful slice, learning from the working interface before expanding.
- `choose-a-personality`: The interface feels generic or its typography, colors, corners and copy disagree → Choose a coherent visual and verbal personality suited to the audience.
- `limit-your-choices`: Every component introduces another slightly different size, shade or shadow → Constrain choices to a reusable scale and compare neighboring options in context.

**Hierarchy** ([reference](references/hierarchy-is-everything.md))

- `not-all-elements-are-equal`: A crowded dashboard gives all information and actions equal emphasis → Identify the primary content and soften secondary information before adding decoration.
- `size-isnt-everything`: The main text is oversized while supporting details are too small → Use weight and color alongside size to establish readable levels of emphasis.
- `dont-use-grey-text-on-colored-backgrounds`: Secondary text on a colored panel looks grey, washed out or disabled → Choose an opaque related text color and check it against the actual background.
- `emphasize-by-de-emphasizing`: The active navigation or main content cannot stand out because neighboring elements compete → Reduce the emphasis of competitors, such as inactive links or a sidebar panel.
- `labels-are-a-last-resort`: Displayed data is buried in repetitive label-value pairs → Use recognizable formats or combine labels with values, emphasizing what people scan for.
- `separate-visual-hierarchy-from-document-hierarchy`: A large page title competes with more important task content → Choose heading elements for document structure and style their visual emphasis independently.
- `balance-weight-and-contrast`: Solid icons overpower nearby labels, or thin borders are either harsh or invisible → Balance visual area against contrast: soften heavy icons or slightly thicken pale separators.
- `semantics-are-secondary`: Every action is a loud colored button, including rare destructive actions → Assign primary, secondary and tertiary emphasis according to each action's role in the current task.

**Layout and spacing** ([reference](references/layout-and-spacing.md))

- `start-with-too-much-white-space`: A card or form feels cramped and every section barely fits → Start with generous spacing, then remove excess until grouping and density fit the task.
- `establish-a-spacing-and-sizing-system`: Margins and padding vary arbitrarily across similar components → Replace arbitrary values with a spacing scale whose steps remain perceptibly different.
- `you-dont-have-to-fill-the-whole-screen`: Forms or content stretch across a wide viewport without gaining usefulness → Constrain content to a readable width; put supporting descriptions beside fields when useful.
- `grids-are-overrated`: A percentage sidebar or grid-bound card becomes too wide or too narrow at different viewports → Size stable elements for their content and let the main content flex within useful limits.
- `relative-sizing-doesnt-scale`: Mobile headings dominate the screen, or button variants look like zoomed copies → Tune headline sizes and component padding independently across size variants.
- `avoid-ambiguous-spacing`: Labels, headings, list items or horizontal controls appear connected to the wrong neighbors → Make spacing inside a group smaller than spacing between groups.

**Typography** ([reference](references/designing-text.md))

- `establish-a-type-scale`: Similar text roles use many nearly identical font sizes → Define a small set of useful type sizes and reuse them by role.
- `use-good-fonts`: Body text is hard to read or font selection is consuming the design process → Start with a legible family and verify its actual weights, proportions and language coverage.
- `keep-your-line-length-in-check`: Paragraphs span too much of the page and are tiring to read → Constrain reading measure independently of the wider layout.
- `baseline-not-center`: A title and smaller adjacent actions look vertically misaligned → Align mixed text sizes on their baseline.
- `line-height-is-proportional`: Body lines are hard to track, or a wrapped heading feels disconnected → Adjust line-height to both line length and font size, usually giving small or wide body text more room.
- `not-every-link-needs-a-color`: Repeated colored links overwhelm cards or navigation → Establish hierarchy with weight and neutral tones where the component context already indicates interaction.
- `align-with-readability-in-mind`: Long centered text or uneven numeric columns are hard to scan → Align prose with its reading direction and numeric columns for comparison; keep centered text brief.
- `use-letter-spacing-effectively`: Headlines feel loose or all-caps labels feel crowded → Keep body tracking near the typeface default, testing tighter headlines or wider uppercase text when useful.

**Color** ([reference](references/working-with-color.md))

- `ditch-hex-for-hsl`: Related colors are difficult to reason about when editing raw color values → Use a color model that exposes useful relationships and retain the project's palette format.
- `you-need-more-colors-than-you-think`: A small palette cannot support readable text, surfaces and semantic states → Provide tonal ranges for neutrals, brand colors and the accent roles the product actually needs.
- `define-your-shades-up-front`: Components accumulate slightly different ad hoc lightened and darkened colors → Choose useful dark, middle and light anchors, fill a stable shade scale, and name semantic roles.
- `dont-let-lightness-kill-your-saturation`: Light and dark palette shades look washed out or muddy → Adjust saturation or chroma and sometimes hue while shaping the tonal range.
- `greys-dont-have-to-be-grey`: Neutral surfaces feel disconnected from the intended warm or cool personality → Use a coherent, subtly tinted neutral ramp when it serves the design.
- `accessible-doesnt-have-to-mean-ugly`: Readable status colors become too visually heavy, or colored text loses its character → Try dark colored text on a light tint, checking actual foreground-background contrast.
- `dont-rely-on-color-alone`: Trends, statuses or chart categories are distinguishable only by hue → Pair color with labels, signs, icons, patterns or another independent signal.

**Depth** ([reference](references/creating-depth.md))

- `emulate-a-light-source`: Raised and inset controls feel flat or their light cues contradict each other → Use a consistent implied light direction with restrained edge highlights and shadows.
- `use-shadows-to-convey-elevation`: Buttons, menus and dialogs appear to sit at arbitrary or indistinguishable depths → Choose shadows from a small elevation scale matched to each element's layering role.
- `shadows-can-have-two-parts`: A shadow feels muddy or its surface edge lacks definition → Combine a broad soft shadow with a tighter contact shadow, reducing the latter at higher elevation.
- `even-flat-designs-can-have-depth`: A flat interface needs clearer separation without realistic soft shadows → Use surface tones or a crisp offset shadow to indicate layering.
- `overlap-elements-to-create-layers`: Separate blocks feel disconnected, or overlapping images visually collide → Let selected elements cross a section boundary and use a background-colored gap between overlapping images.

**Images** ([reference](references/working-with-images.md))

- `use-good-photos`: Weak lighting or composition undermines an otherwise clear card or hero → Use imagery with appropriate lighting, composition and subject matter at the actual display size.
- `text-needs-consistent-contrast`: Hero text disappears over bright or dark parts of an image → Treat the image or text backing to create a consistent readable foreground-background relationship.
- `everything-has-an-intended-size`: Enlarged icons look chunky, small screenshots are unreadable, or favicons lose their shape → Use graphics designed for the target size; crop, simplify or recapture screenshots as needed.
- `beware-user-uploaded-content`: Varied aspect ratios break card layouts, or avatars lose their visible edges → Use consistent image containers with deliberate cropping and subtle edge treatment where needed.

**Finishing touches** ([reference](references/finishing-touches.md))

- `supercharge-the-defaults`: A sound layout feels generic because its existing elements receive no attention → Refine list markers, quotation marks, link treatments and form-control styling.
- `add-color-with-accent-borders`: A restrained interface needs a small amount of identity or a clearer active state → Add a purposeful accent line to a card, alert, heading or active navigation item.
- `decorate-your-backgrounds`: Hierarchy and spacing work but a surface still feels plain → Try a restrained background tone, gentle gradient or low-contrast decorative fragment.
- `dont-overlook-empty-states`: A first-use screen shows only absence and gives no clear next action → Explain the feature and make its first useful action prominent, simplifying controls with no purpose yet.
- `use-fewer-borders`: An interface looks boxed in by repeated outlines and dividers → Use spacing, surface tones or a restrained shadow where they communicate the same grouping.
- `think-outside-the-box`: A dropdown, table or choice group is hard to scan in its default presentation → Reorganize related content with descriptions, grouped cells or selectable cards when it improves the task.

**Developing an eye for design** ([reference](references/leveling-up.md))

- `leveling-up`: You want to understand which subtle decisions make an admired interface work → Study unexpected choices and reconstruct a small example to expose details in spacing, type and layers.

## Find rules and figures

Run from this skill directory, or use the helper's absolute path from any working directory. Requires Python 3.9+ and only the standard library; no network or site server is needed.

```sh
python3 scripts/find_examples.py "busy navigation" --limit 2
python3 scripts/find_examples.py "form labels confusing" --limit 2
python3 scripts/find_examples.py --rule emphasize-by-de-emphasizing
python3 scripts/find_examples.py --rule everything-has-an-intended-size --all-figures
python3 scripts/find_examples.py --list-topics
```

Search returns ranked rules, a short recommendation and caution, a reference path with its heading anchor, and absolute image paths with descriptions. It uses keyword matching, not semantic search; if a result is weak, use a more concrete symptom, `--topic`, or an exact `--rule` ID. `--json` gives structured output. The default selects one relevant figure group per search result, preserving paired views; exact rule lookup returns its curated figures. Use `--groups 2` or `--all-figures` only when more examples are useful.

The [index](references/examples.json) covers 50 sections and 283 figures. Do not load the entire index or all images by default. Without a shell, open a topic reference below and follow its curated figure links. Figure paths are bundled locally.

| Problem | Read |
| --- | --- |
| Starting a screen, scope, personality, too many choices | [Starting from scratch](references/starting-from-scratch.md) |
| Competing information, labels, icons, action priority | [Hierarchy](references/hierarchy-is-everything.md) |
| Cramped or stretched layouts, responsive sizing, unclear groups | [Layout and spacing](references/layout-and-spacing.md) |
| Type scales, line length, alignment, links, tracking | [Typography](references/designing-text.md) |
| Palettes, shade scales, tinted neutrals, readable states | [Color](references/working-with-color.md) |
| Shadows, elevation, inset controls, overlapping layers | [Depth](references/creating-depth.md) |
| Photography, text over images, icon sizes, uploaded content | [Images](references/working-with-images.md) |
| Plain components, accents, empty states, excessive borders | [Finishing touches](references/finishing-touches.md) |
| Learning from or reconstructing a visual reference | [Developing an eye for design](references/leveling-up.md) |

## Important boundaries

- Advice about removing labels concerns **displayed data**, not form labels or accessible names. Visual heading size does not determine its semantic level.
- Softer text must remain readable. Normal text needs at least 4.5:1 contrast; the 3:1 large-text threshold starts at 24 CSS px regular or about 18.67 CSS px bold. The [color reference](references/working-with-color.md#accessible-doesnt-have-to-mean-ugly) includes the authoritative definition. The brightness approximation is not a contrast calculator.
- Preserve discoverable controls, visible keyboard focus and meaningful states. Styling examples do not authorize hiding required information, discarding semantics or reducing interactive targets to an icon's visual size.
- Use the project's current color model and layout tools. The HSL examples and criticism of rigid grids do not require migrating OKLCH tokens or avoiding CSS Grid.

To check this package after editing the index, figures or the rule list (the check also confirms every rule is listed above):

```sh
python3 scripts/find_examples.py --check
python3 -B scripts/test_find_examples.py
```
