# New Screens

Read the matching rule below. `scripts/find_examples.py --rule <id>` returns its figures when it has them; open them when the rule concerns a visual quantity or you are unsure how far to take it. Figure paths are relative to this file.

<a id="design-the-feature-before-the-shell"></a>

## Design the feature before the shell

**When:** A new screen is stuck on navigation, page chrome or the app shell.

**Change:** Design the smallest useful feature around its real data and actions before choosing the surrounding shell.

**Why / how:** An app is a collection of features. The shell (top nav or sidebar, container or full width, where the logo goes) exists to connect features, so it cannot be decided before a few of them exist. Starting with the shell is why "designing the app" feels stuck. Begin with one concrete piece of functionality and its minimum elements. Flight search needs a departure field, a destination field, two dates and a button. Design that. The shell may turn out to be unnecessary; Google's home page is a search box.

**Watch for:** Reuse established navigation in an existing product; this advice targets an undecided new design.

**Visuals:** [design-the-feature-before-the-shell-2 (example)](figures/design-the-feature-before-the-shell-2.webp), [design-the-feature-before-the-shell-3 (example)](figures/design-the-feature-before-the-shell-3.webp). Lookup: `design-the-feature-before-the-shell`.

<a id="settle-structure-before-detail"></a>

## Settle structure before detail

**When:** Colors, fonts and shadows are slowing early layout decisions.

**Change:** Explore structure in low fidelity or grayscale, then add detail once the hierarchy works.

**Why / how:** Early on, typefaces, shadows and icons are noise. Work in low fidelity; paper and a thick marker make detail impossible, which is the point. When moving up in fidelity, stay in grayscale. Without color, spacing, contrast and size have to carry the hierarchy, and the result is an interface that is already clear before color is added. Sketches and wireframes are disposable: users cannot do anything with a static mockup, so do not over-invest in them.

**Watch for:** Grayscale is a design exercise, not a demand to remove a product's established visual language.

**Visuals:** [settle-structure-before-detail-2 (before)](figures/settle-structure-before-detail-2.webp), [settle-structure-before-detail-3 (after)](figures/settle-structure-before-detail-3.webp). Lookup: `settle-structure-before-detail`.

<a id="design-the-current-slice"></a>

## Design the current slice

**When:** Mockups imply features or edge cases that are outside the current delivery scope.

**Change:** Design and implement one useful slice, learning from the working interface before expanding.

**Why / how:** Edge cases (2,000 contacts, two events at the same time, where the error message goes) are hard to solve in the abstract. Work in cycles: design a simple version of the next feature, build it, fix the problems in the running thing, then design the next feature. Be a pessimist about scope. Drawing functionality you are not about to build (an attachments area on a comment form) means the whole feature waits on the hardest part. A comment system without attachments ships; one blocked on attachments does not. Expect every feature to be hard to build and design the smallest useful version.

**Watch for:** Keep required functionality and known constraints; simplify only genuinely optional scope.

**Visuals:** [design-the-current-slice-4 (before)](figures/design-the-current-slice-4.webp), [design-the-current-slice-5 (after)](figures/design-the-current-slice-5.webp). Lookup: `design-the-current-slice`.

<a id="constrain-choices-to-scales"></a>

## Constrain choices to scales

**When:** Every component introduces another slightly different size, shade or shadow.

**Change:** Constrain choices to a reusable scale and compare neighboring options in context.

**Why / how:** Unconstrained choices (12px or 13px, 10% or 15% shadow opacity, medium or semibold) are slow because several answers are equally right. Define systems in advance: 8 to 10 shades per color, a restrictive type scale, and so on. Then choose by elimination: guess (a 16px icon), compare the neighbours (12 and 24), and two of the three will be obviously wrong. If an outer value wins, repeat with it in the middle. Systematize anything you catch yourself deliberating: font size, weight, line-height, color, margin, padding, width, height, shadows, radius, border width, opacity.

**Watch for:** Use the project's existing tokens before proposing new scales.

**Visuals:** [constrain-choices-to-scales-5 (comparison)](figures/constrain-choices-to-scales-5.webp), [constrain-choices-to-scales-6 (comparison)](figures/constrain-choices-to-scales-6.webp). Lookup: `constrain-choices-to-scales`.
