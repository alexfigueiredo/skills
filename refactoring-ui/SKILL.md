---
name: refactoring-ui
description: "Design, restyle or critique interfaces. Classifies each page by its goal (convert, operate, browse, read, experience), sets a visual direction that keeps the brand, and applies searchable rules with visual examples for hierarchy, layout, typography, color, depth, imagery, components, states and motion. Use to make a UI clearer or better looking (polish, redesign), design a new page, landing page or dashboard, add motion or 3D, review a design, or decide design-system tokens."
---

# Refactoring UI

Make each page clear and good-looking for what it is for. Preserve the product's purpose, brand material, tokens and component behavior unless the user asks for a new direction. Match the user's scope: a critique produces findings; an implementation request authorizes the relevant edits.

## Working loop

1. **Read the context.** Read the relevant components and tokens, plus `PRODUCT.md`, `DESIGN.md` or a design-tokens file if the project has them. Look at the rendered pages, supplied screenshots or mockups. If you cannot see the interface, separate observations from code from unverified visual judgments.
2. **Classify each page** with [page modes](references/surfaces.md) and write the page map: page, mode, visitor's goal, success action and the brand material on it.
3. **Pick the intent** from the table below and read only its references.
4. **Find the rules** that explain the problems you see, using the helper below or the list at a glance. Read each rule in its reference, including its caution and its note for the page's mode. Open a rule's figures when it concerns a visual quantity (shadow, color, tracking, spacing proportions, image treatment) or when you are unsure how far to take it. Inspect both members of a before/after pair; a `comparison` image already contains several views. A caption alone is not visual inspection.
5. **Apply the mechanism** in the project's tokens and components. Each figure illustrates one rule; its colors, controls and visual style are not a direction to copy.
6. **Verify** with [review](references/review.md): screenshots at desktop and phone widths in the affected states. Report what changed and what you actually verified.

## Intents

The user can name the intent (`/refactoring-ui critique`, `/refactoring-ui bolder`); otherwise infer it from the request.

| Intent | Request | Do | Read |
| --- | --- | --- | --- |
| `critique` | Review, audit or give feedback on a UI | Page map, walk the rules, findings by severity | review, surfaces, direction, then the topics of the findings |
| `refine` | Improve or polish an existing page | Keep brand material; fix hierarchy, layout, type and states | surfaces, direction, hierarchy, layout, typography, imagery, components |
| `bolder` | Make it better looking, more distinctive or more on-brand | Refine or Extend; Propose only when the user asks for a new look. Concentrate expression in one region | direction, imagery, color, motion |
| `quieter` | Make it calmer, denser or less busy | Quiet competitors, group with space, tighten spacing | direction, hierarchy, layout |
| `new` | New page, screen or landing page | Classify, write a direction plan, build the smallest useful version | surfaces, new-screen, direction, layout |
| `system` | Design-system tokens or scales | Inspect current tokens, fill the gaps in each scale | new-screen, layout, typography, color, depth, motion |
| `responsive` | Mobile or narrow-screen problems | Layout by available width, navigation, art crops | layout, imagery |
| `motion` | Transitions, animated backgrounds, 3D | Check the mode's motion budget first | motion, surfaces |

## Rules at a glance

One line per rule: the symptom, then the change. A broad review walks every line against each page; a focused task reads the matching rule in its reference.

**New Screens** ([reference](references/new-screen.md))

- `design-the-feature-before-the-shell`: A new screen is stuck on navigation, page chrome or the app shell → Design the smallest useful feature around its real data and actions before choosing the surrounding shell.
- `settle-structure-before-detail`: Colors, fonts and shadows are slowing early layout decisions → Explore structure in low fidelity or grayscale, then add detail once the hierarchy works.
- `design-the-current-slice`: Mockups imply features or edge cases that are outside the current delivery scope → Design and implement one useful slice, learning from the working interface before expanding.
- `constrain-choices-to-scales`: Every component introduces another slightly different size, shade or shadow → Constrain choices to a reusable scale and compare neighboring options in context.

**Visual Direction** ([reference](references/direction.md))

- `preserve-brand-material`: A refactor dims, hides, recolors or removes a logo, key art, banner, display typeface or brand-colored action to fix hierarchy or contrast → Keep the brand material at its size, visibility and colors, and fix what surrounds it: quieter neighbors, a backing behind the text, a new crop or position.
- `avoid-template-defaults`: The page could belong to any product: an uppercase label above every heading, a headline over subcopy and two buttons, a row of identical icon cards, numbered sections, gradient text, glowing colored shadows, cards inside cards → For each choice, ask whether you would make the same one for an unrelated product; if so, tie it to this product's subject and content, or state why it stays.
- `define-a-personality`: The interface feels generic or its typography, colors, corners and copy disagree → Choose a coherent visual and verbal personality suited to the audience.
- `open-with-the-subject`: A convert or experience page opens with an abstract headline, stock imagery or a generic illustration, while the product's own screens, art or results sit further down → Put the most characteristic thing about the subject in the first viewport: the product working, real screenshots, the game's art, the work itself.
- `concentrate-expression`: Every section of a page competes with its own color, large type, illustration or animation, or no section stands out at all → Choose one region per page for the strongest type, color, imagery or motion, and keep the other regions calmer.
- `add-accent-lines`: A restrained interface needs a small amount of identity or a clearer active state → Add a purposeful accent line to a card, alert, heading or active navigation item.
- `decorate-plain-backgrounds`: Hierarchy and spacing work but a surface still feels plain → Try a restrained background tone, gentle gradient or low-contrast decorative fragment.
- `rebuild-references-to-learn`: You want to understand which subtle decisions make an admired interface work → Study unexpected choices and reconstruct a small example to expose details in spacing, type and layers.

**Hierarchy** ([reference](references/hierarchy.md))

- `rank-content-by-importance`: A crowded dashboard gives all information and actions equal emphasis → Identify the primary content and soften secondary information before adding decoration.
- `emphasize-with-weight-and-color`: The main text is oversized while supporting details are too small → Use weight and color alongside size to establish readable levels of emphasis.
- `tint-secondary-text-on-color`: Secondary text on a colored panel looks grey, washed out or disabled → Choose an opaque related text color and check it against the actual background.
- `de-emphasize-competitors`: The active navigation or main content cannot stand out because neighboring elements compete → Reduce the emphasis of competitors, such as inactive links or a sidebar panel.
- `let-values-identify-themselves`: Displayed data is buried in repetitive label-value pairs → Use recognizable formats or combine labels with values, emphasizing what people scan for.
- `structure-matches-content`: Numbered markers, small uppercase labels above headings, or dividers appear where the content has no order, category or boundary → Remove them; keep each one only where it states something true that the heading and navigation do not.
- `separate-visual-hierarchy-from-document-hierarchy`: A large page title competes with more important task content → Choose heading elements for document structure and style their visual emphasis independently.
- `balance-weight-and-contrast`: Solid icons overpower nearby labels, or thin borders are either harsh or invisible → Balance visual area against contrast: soften heavy icons or slightly thicken pale separators.
- `style-actions-by-priority`: Every action is a loud colored button, including rare destructive actions → Assign primary, secondary and tertiary emphasis according to each action's role in the current task.

**Layout** ([reference](references/layout.md))

- `start-generous-then-tighten`: A card or form feels cramped and every section barely fits → Start with generous spacing, then remove excess until grouping and density fit the task.
- `use-a-spacing-scale`: Margins and padding vary arbitrarily across similar components → Replace arbitrary values with a spacing scale whose steps remain perceptibly different.
- `avoid-ambiguous-spacing`: Labels, headings, list items or horizontal controls appear connected to the wrong neighbors → Make spacing inside a group smaller than spacing between groups.
- `group-with-space-not-borders`: An interface looks boxed in by repeated outlines and dividers → Use spacing, surface tones or a restrained shadow where they communicate the same grouping.
- `constrain-content-width`: Forms or content stretch across a wide viewport without gaining usefulness → Constrain content to a readable width; put supporting descriptions beside fields when useful.
- `fix-stable-widths`: A percentage sidebar or grid-bound card becomes too wide or too narrow at different viewports → Size stable elements for their content and let the main content flex within useful limits.
- `switch-layout-by-available-width`: A component keeps its wide layout inside a narrow column, or the layout changes on device type or orientation instead of on the space it has → Change a component's layout at the width it receives: container queries for reusable components, viewport queries for the page shell.
- `tune-sizes-per-context`: Mobile headings dominate the screen, or button variants look like zoomed copies → Tune headline sizes and component padding independently across size variants.
- `keep-navigation-reachable`: On narrow screens, navigation items are cut off at the edge, hidden without a cue, or the collapsed navigation drops destinations → Show that more items exist or move the extra items into a labeled menu, keeping the same destinations, order, labels and active state.

**Typography** ([reference](references/typography.md))

- `use-a-type-scale`: Similar text roles use many nearly identical font sizes → Define a small set of useful type sizes and reuse them by role.
- `choose-legible-typefaces`: Body text is hard to read or font selection is consuming the design process → Start with a legible family and verify its actual weights, proportions and language coverage.
- `limit-line-length`: Paragraphs span too much of the page and are tiring to read → Constrain reading measure independently of the wider layout.
- `align-mixed-sizes-on-baseline`: A title and smaller adjacent actions look vertically misaligned → Align mixed text sizes on their baseline.
- `set-line-height-by-size-and-measure`: Body lines are hard to track, or a wrapped heading feels disconnected → Adjust line-height to both line length and font size, usually giving small or wide body text more room.
- `color-links-only-where-needed`: Repeated colored links overwhelm cards or navigation → Establish hierarchy with weight and neutral tones where the component context already indicates interaction.
- `align-for-reading`: Long centered text or uneven numeric columns are hard to scan → Align prose with its reading direction and numeric columns for comparison; keep centered text brief.
- `adjust-tracking-by-size-and-case`: Headlines feel loose or all-caps labels feel crowded → Keep body tracking near the typeface default, testing tighter headlines or wider uppercase text when useful.

**Color** ([reference](references/color.md))

- `use-a-relational-color-model`: Related colors are difficult to reason about when editing raw color values → Use a color model that exposes useful relationships and retain the project's palette format.
- `plan-full-color-ranges`: A small palette cannot support readable text, surfaces and semantic states → Provide tonal ranges for neutrals, brand colors and the accent roles the product actually needs.
- `define-shade-scales-up-front`: Components accumulate slightly different ad hoc lightened and darkened colors → Choose useful dark, middle and light anchors, fill a stable shade scale, and name semantic roles.
- `keep-saturation-at-the-extremes`: Light and dark palette shades look washed out or muddy → Adjust saturation or chroma and sometimes hue while shaping the tonal range.
- `tint-neutrals`: Neutral surfaces feel disconnected from the intended warm or cool personality → Use a coherent, subtly tinted neutral ramp when it serves the design.
- `use-dark-text-on-light-tints`: Readable status colors become too visually heavy, or colored text loses its character → Try dark colored text on a light tint, checking actual foreground-background contrast.
- `dont-rely-on-color-alone`: Trends, statuses or chart categories are distinguishable only by hue → Pair color with labels, signs, icons, patterns or another independent signal.
- `design-dark-themes-separately`: A dark theme was made by inverting the light palette, and surfaces blur together, text glares or brand colors vibrate → Make higher layers lighter instead of relying on shadows, measure every contrast pair again, and tune text and brand colors for the dark surfaces.

**Depth** ([reference](references/depth.md))

- `use-one-light-direction`: Raised and inset controls feel flat or their light cues contradict each other → Use a consistent implied light direction with restrained edge highlights and shadows.
- `map-shadows-to-elevation`: Buttons, menus and dialogs appear to sit at arbitrary or indistinguishable depths → Choose shadows from a small elevation scale matched to each element's layering role.
- `combine-ambient-and-contact-shadows`: A shadow feels muddy or its surface edge lacks definition → Combine a broad soft shadow with a tighter contact shadow, reducing the latter at higher elevation.
- `layer-flat-designs-with-tone`: A flat interface needs clearer separation without realistic soft shadows → Use surface tones or a crisp offset shadow to indicate layering.
- `overlap-to-create-layers`: Separate blocks feel disconnected, or overlapping images visually collide → Let selected elements cross a section boundary and use a background-colored gap between overlapping images.

**Imagery** ([reference](references/imagery.md))

- `choose-strong-photos`: Weak lighting or composition undermines an otherwise clear card or hero → Use imagery with appropriate lighting, composition and subject matter at the actual display size.
- `keep-text-contrast-over-images`: Hero text disappears over bright or dark parts of an image → Treat the image or text backing to create a consistent readable foreground-background relationship.
- `crop-art-per-viewport`: Hero art, illustrations or banners disappear, shrink to a thin strip or lose their subject on narrow screens → Re-crop or reposition the art for each viewport so its subject stays visible, instead of hiding it.
- `use-graphics-at-their-intended-size`: Enlarged icons look chunky, small screenshots are unreadable, or favicons lose their shape → Use graphics designed for the target size; crop, simplify or recapture screenshots as needed.
- `contain-user-uploaded-images`: Varied aspect ratios break card layouts, or avatars lose their visible edges → Use consistent image containers with deliberate cropping and subtle edge treatment where needed.

**Components** ([reference](references/components.md))

- `refine-default-elements`: A sound layout feels generic because its existing elements receive no attention → Refine list markers, quotation marks, link treatments and form-control styling.
- `design-every-state`: Controls and data regions look finished only at rest; hover, focus, loading or error states are missing or inconsistent → Define hover, focus-visible, active, disabled, loading and error for each interactive component, and loading, empty and error for each region that shows data.
- `design-empty-states`: A first-use screen shows only absence and gives no clear next action → Explain the feature and make its first useful action prominent, simplifying controls with no purpose yet.
- `name-actions-by-result`: Buttons say "Submit", "OK" or "Yes", or error messages are vague or only apologize → Label each action with its result in the user's terms, and make each error say what happened and how to fix it.
- `restructure-default-components`: A dropdown, table or choice group is hard to scan in its default presentation → Reorganize related content with descriptions, grouped cells or selectable cards when it improves the task.

**Motion** ([reference](references/motion.md))

- `animate-to-explain-state`: Sections fade in on scroll, every card moves on hover, content waits for an animation, or transitions feel slow → Animate feedback, state changes and spatial continuity, and keep content visible without the animation.
- `reserve-3d-for-visual-subjects`: A 3D scene, shader or animated background is being considered, or one already slows the page or competes with its content → Use one only where the subject is visual or spatial (a product, a game world, a map, the brand's mood on a convert page), in one region, behind or beside HTML text, with a static fallback.

## Find rules and figures

Run from this skill directory, or use the helper's absolute path. It needs Python 3.9+ and only the standard library.

```sh
python3 scripts/find_examples.py "busy navigation" --limit 2
python3 scripts/find_examples.py "landing page looks generic" --mode convert
python3 scripts/find_examples.py --rule de-emphasize-competitors
python3 scripts/find_examples.py --rule use-graphics-at-their-intended-size --all-figures
python3 scripts/find_examples.py --list-topics
```

Search returns ranked rules with the change, a caution, the note for `--mode` when the rule has one, the reference path and absolute figure paths with captions. It matches keywords, not meaning: if a result is weak, describe the visible symptom more concretely, add `--topic`, or use an exact `--rule` id. `--json` gives structured output. Some rules have no figures; their reference text is the whole rule. By default each result includes one group of related figures; use `--groups 2` or `--all-figures` only when more examples help.

The [index](references/examples.json) covers 63 rules and 283 figures. Do not load the whole index or all images. Without a shell, open the topic reference from the table below and follow its figure links.

| Problem | Read |
| --- | --- |
| Unsure what a page is for; many pages sharing one template | [Page modes](references/surfaces.md) |
| Generic look, brand lost in a refactor, making a page bolder or more distinctive | [Visual direction](references/direction.md) |
| Starting a screen, scope, too many slightly different values | [New screens](references/new-screen.md) |
| Competing information, labels, action priority, decorative numbering and labels | [Hierarchy](references/hierarchy.md) |
| Cramped or stretched layouts, grouping, responsive layout, mobile navigation | [Layout](references/layout.md) |
| Type scales, line length, alignment, links, tracking | [Typography](references/typography.md) |
| Palettes, shade scales, tinted neutrals, readable states, dark themes | [Color](references/color.md) |
| Shadows, elevation, inset controls, overlapping layers | [Depth](references/depth.md) |
| Photos, text over images, art on narrow screens, icon sizes, uploaded content | [Imagery](references/imagery.md) |
| Plain default elements, missing and empty states, button and error text | [Components](references/components.md) |
| Transitions, animated backgrounds, 3D and shaders | [Motion](references/motion.md) |
| Critique format, severity, verification | [Review](references/review.md) |

## Boundaries

- Brand material (logo, wordmark, key art, banners, illustrations, display typeface, brand-colored primary actions) stays present, visible and in its colors. You may move it, re-crop it and scale it for narrower screens; removing, hiding, shrinking, darkening, recoloring or neutralizing it at the same width needs the user's approval. Fix contrast and competition around it.
- Advice about removing labels concerns **displayed data**, not form labels or accessible names. Visual heading size does not determine semantic level.
- Softer text must remain readable. Normal text needs at least 4.5:1 contrast; the 3:1 large-text threshold starts at 24 CSS px regular or about 18.67 CSS px bold. The [color reference](references/color.md#use-dark-text-on-light-tints) has the definition. The brightness approximation in the color examples is not a contrast calculator.
- Preserve discoverable controls, visible keyboard focus and meaningful states; styling advice does not authorize hiding required information. Interactive targets need at least 24×24 CSS px (WCAG 2.5.8); for touch, follow the platform size (44 pt on iOS, 48 dp on Android). Enlarge the hit area, not the icon.
- Animation you add must stop or reduce under `prefers-reduced-motion`. Decorative animated, video or 3D layers stay behind the content, out of the tab order, and fall back to a still image.
- Use the project's current color model and layout tools. The HSL examples and the criticism of rigid percentage grids do not require migrating OKLCH tokens or avoiding CSS Grid.
- Outside the web, read CSS px as logical pixels (Flutter logical pixels, Android dp, iOS pt). `max-width` corresponds to `ConstrainedBox` or `.frame(maxWidth:)`, and container queries to `LayoutBuilder` or `GeometryReader`. Contrast thresholds are the same. Verify with emulator, simulator or golden-test screenshots at several sizes.
