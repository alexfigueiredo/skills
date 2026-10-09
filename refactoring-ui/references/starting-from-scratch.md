# Starting from Scratch

Read the matching rule below; use `scripts/find_examples.py --rule <id>` for its annotated figures. Figure paths are relative to this file.

<a id="start-with-a-feature-not-a-layout"></a>

## Start with a feature, not a layout

**When:** A new screen is stuck on navigation, page chrome or the app shell.

**Change:** Design the smallest useful feature around its real data and actions before choosing the surrounding shell.

**Why / how:** An app is a collection of features. The shell (top nav or sidebar, container or full width, where the logo goes) exists to connect features, so it cannot be decided before a few of them exist. Starting with the shell is why "designing the app" feels stuck. Begin with one concrete piece of functionality and its minimum elements. Flight search needs a departure field, a destination field, two dates and a button. Design that. The shell may turn out to be unnecessary; Google's home page is a search box.

**Watch for:** Reuse established navigation in an existing product; this advice targets an undecided new design.

**Visuals:** [fig-009-002 (example)](figures/fig-009-002.webp), [fig-010-003 (example)](figures/fig-010-003.webp). Lookup: `start-with-a-feature-not-a-layout`.

<a id="detail-comes-later"></a>

## Detail comes later

**When:** Colors, fonts and shadows are slowing early layout decisions.

**Change:** Explore structure in low fidelity or grayscale, then add detail once the hierarchy works.

**Why / how:** Early on, typefaces, shadows and icons are noise. Work in low fidelity; paper and a thick marker make detail impossible, which is the point. When moving up in fidelity, stay in grayscale. Without color, spacing, contrast and size have to carry the hierarchy, and the result is a clearer interface that color later enhances instead of rescues. Sketches and wireframes are disposable: users cannot do anything with a static mockup, so do not over-invest in them.

**Watch for:** Grayscale is a design exercise, not a demand to remove a product's established visual language.

**Visuals:** [fig-013-005 (before)](figures/fig-013-005.webp), [fig-013-006 (after)](figures/fig-013-006.webp). Lookup: `detail-comes-later`.

<a id="dont-design-too-much"></a>

## Don’t design too much

**When:** Mockups imply features or edge cases that are outside the current delivery scope.

**Change:** Design and implement one useful slice, learning from the working interface before expanding.

**Why / how:** Edge cases (2,000 contacts, two events at the same time, where the error message goes) are hard to solve in the abstract. Work in cycles: design a simple version of the next feature, build it, fix the problems in the running thing, then design the next feature. Be a pessimist about scope. Drawing functionality you are not about to build (an attachments area on a comment form) means the whole feature waits on the hardest part. A comment system without attachments ships; one blocked on attachments does not. Expect every feature to be hard to build and design the smallest useful version.

**Watch for:** Keep required functionality and known constraints; simplify only genuinely optional scope.

**Visuals:** [fig-018-010 (before)](figures/fig-018-010.webp), [fig-019-011 (after)](figures/fig-019-011.webp). Lookup: `dont-design-too-much`.

<a id="choose-a-personality"></a>

## Choose a personality

**When:** The interface feels generic or its typography, colors, corners and copy disagree.

**Change:** Choose a coherent visual and verbal personality suited to the audience.

**Why / how:** Personality is set by a few concrete levers.

- Typeface: serif reads elegant or classic, rounded sans reads playful, neutral sans reads plain and lets other elements carry the personality.
- Color: blue is safe and familiar, gold reads expensive, pink reads fun. Color psychology helps explain why a choice feels right; it is not a selection method.
- Border radius: none reads formal, small reads neutral, large reads playful. Pick one and keep it; mixing square and rounded corners looks worse than either.
- Language: impersonal copy reads official, casual copy reads friendly. Words matter as much as the visuals.

When unsure, match the register of sites your audience already uses, without borrowing from direct competitors.

**Watch for:** Preserve an existing brand; color associations and example fonts are possibilities, not universal meanings.

**Visuals:** [fig-021-013 (example)](figures/fig-021-013.webp), [fig-021-014 (example)](figures/fig-021-014.webp), [fig-022-015 (example)](figures/fig-022-015.webp). Lookup: `choose-a-personality`.

<a id="limit-your-choices"></a>

## Limit your choices

**When:** Every component introduces another slightly different size, shade or shadow.

**Change:** Constrain choices to a reusable scale and compare neighboring options in context.

**Why / how:** Unconstrained choices (12px or 13px, 10% or 15% shadow opacity, medium or semibold) are slow because several answers are equally right. Define systems in advance: 8 to 10 shades per color, a restrictive type scale, and so on. Then choose by elimination: guess (a 16px icon), compare the neighbours (12 and 24), and two of the three will be obviously wrong. If an outer value wins, repeat with it in the middle. Systematize anything you catch yourself deliberating: font size, weight, line-height, color, margin, padding, width, height, shadows, radius, border width, opacity.

**Watch for:** Use the project's existing tokens before proposing new scales.

**Visuals:** [fig-030-028 (comparison)](figures/fig-030-028.webp), [fig-031-029 (comparison)](figures/fig-031-029.webp). Lookup: `limit-your-choices`.
