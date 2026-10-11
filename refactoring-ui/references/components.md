# Components

Read the matching rule below. `scripts/find_examples.py --rule <id>` returns its figures when it has them; open them when the rule concerns a visual quantity or you are unsure how far to take it. Figure paths are relative to this file.

<a id="refine-default-elements"></a>

## Refine default elements

**When:** A sound layout feels generic because its existing elements receive no attention.

**Change:** Refine list markers, quotation marks, link treatments and form-control styling.

**Why / how:** Improve the elements already on the page before adding new ones. Replace list bullets with icons: checkmarks or arrows generically, or something content-specific such as a padlock for security features. Promote the quotation marks of a testimonial into large, colored visual elements. Style links with weight and color, or with a thick colored underline that partially overlaps the text. Apply a suitable brand treatment to existing accessible checkboxes and radio buttons; that alone makes a form look styled rather than left at browser defaults.

**Watch for:** Preserve semantics, keyboard interaction and visible states; use established accessible controls rather than rebuilding behavior for decoration.

**Visuals:** [refine-default-elements-1 (comparison)](figures/refine-default-elements-1.webp), [refine-default-elements-5 (comparison)](figures/refine-default-elements-5.webp). Lookup: `refine-default-elements`.

<a id="design-every-state"></a>

## Design every state

**When:** Controls and data regions look finished only at rest; hover, focus, loading or error states are missing or inconsistent.

**Change:** Define hover, focus-visible, active, disabled, loading and error for each interactive component, and loading, empty and error for each region that shows data.

**Why / how:** People spend much of their time outside the resting state: waiting for data, recovering from an error, moving through controls with a keyboard. Design these states with the same tokens as the resting one. A loading region keeps the size and shape of its final content (a skeleton), so the layout does not jump when data arrives. An error state says what failed and keeps the user's input. A disabled control explains nearby what is needed to enable it when that is not obvious. Check each state by triggering it in the running interface.

**Watch for:** Hover can add information but must not be the only way to reach an action; touch and keyboard users have no hover. Focus-visible styles must stay visible on every background. First-use empty states are covered by `design-empty-states`.

<a id="design-empty-states"></a>

## Design empty states

**When:** A first-use screen shows only absence and gives no clear next action.

**Change:** Explain the feature and make its first useful action prominent, simplifying controls with no purpose yet.

**Why / how:** Features that depend on user content are usually designed with rich sample data, and the first thing a real user sees is an empty screen. Treat the empty state as a priority: an image or illustration, and an emphasized call to action toward the first step. Hide supporting UI such as tabs and filters until there is content for them to act on. It is the user's first interaction with the feature; make it inviting rather than plain.

**Watch for:** Distinguish first use from filtered zero results and errors; keep filters visible when users need them to recover.

**Visuals:** [design-empty-states-2 (before)](figures/design-empty-states-2.webp), [design-empty-states-3 (after)](figures/design-empty-states-3.webp). Lookup: `design-empty-states`.

<a id="name-actions-by-result"></a>

## Name actions by their result

**When:** Buttons say "Submit", "OK" or "Yes", or error messages are vague or only apologize.

**Change:** Label each action with its result in the user's terms, and make each error say what happened and how to fix it.

**Why / how:** People read button labels to predict what will happen. "Save changes", "Send invite" and "Delete project" tell them; "Submit" and "OK" do not. A destructive confirmation names the action on its button, so the choice can be made without rereading the question. Reuse the verb in the confirmation ("Invite sent"). An error states what went wrong and the next step ("Card expired. Use another card or update the expiry date."), next to the field or region it concerns.

**Watch for:** Use the product's existing terms and voice. Keep labels short enough for their controls, including translated text.

<a id="restructure-default-components"></a>

## Restructure default components

**When:** A dropdown, table or choice group is hard to scan in its default presentation.

**Change:** Reorganize related content with descriptions, grouped cells or selectable cards when it improves the task.

**Why / how:** Components do not have to look the way they usually do. A dropdown is a floating box and can hold sections, columns, supporting text and icons. A table column that need not be sortable can merge with a related column to introduce hierarchy, and cells can carry images and color. Important radio groups can become selectable cards. Constraints are useful, but conventions about a component's shape are not constraints.

**Watch for:** Preserve interaction semantics, keyboard behavior, data relationships and useful sorting; richer layouts need a narrow-screen plan.

**Visuals:** [restructure-default-components-6 (before)](figures/restructure-default-components-6.webp), [restructure-default-components-7 (after)](figures/restructure-default-components-7.webp). Lookup: `restructure-default-components`.
