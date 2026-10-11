# Visual Direction

Decide how a page should look before refining it. The hierarchy, layout and typography rules decide what is primary and make it readable; the direction decides the look those rules work inside. Classify the page first with [page modes](surfaces.md).

## How much to change

- **Refine** (the default in an existing product). List the brand material first: logo and wordmark, display typeface, brand colors, illustrations, key art, banners and signature components. Keep each one. You may change its placement and crop, scale it for narrower screens, and change the contrast around it. On convert and experience pages, do not make the display headline or key art smaller or less visible. Removing, hiding, darkening, recoloring or neutralizing one is a change of direction: propose it and wait for approval.
- **Extend** (a new page in an existing product, or a brand that covers little). Inherit type, color, radius and components; derive what is missing from the existing material and the subject.
- **Propose** (no established brand, or the user asks for a new look or a redesign). Write a direction plan, offer two or three distinct options, and wait for the user's choice before building.

A convert page does not justify a new direction by itself. In an existing product it stays in Refine, with the brand at full strength.

## Direction plan

For Extend and Propose, write the plan in the response before writing code:

1. The subject, the audience and the page's one job.
2. Material from the subject's world: its imagery, palette, lettering, objects and conventions. For operate and read pages, take it from the product's domain, not from the tools the audience uses.
3. Type families and their roles; color roles and how much surface the brand color covers; corner radius; alignment; motion budget. Choose light or dark from where and when the product is used.
4. The first viewport, as a short description or an ASCII sketch.
5. The one region that carries the strongest treatment (`concentrate-expression`).

Check every decision with `avoid-template-defaults`. After building, describe the first viewport in one sentence, the way a visitor would an hour later. If that sentence fits any product in the category, the direction is not visible yet.

Read the matching rule below. `scripts/find_examples.py --rule <id>` returns its figures when it has them; open them when the rule concerns a visual quantity or you are unsure how far to take it. Figure paths are relative to this file.

<a id="preserve-brand-material"></a>

## Preserve brand material

**When:** A refactor dims, hides, recolors or removes a logo, key art, banner, display typeface or brand-colored action to fix hierarchy or contrast.

**Change:** Keep the brand material at its size, visibility and colors, and fix what surrounds it: quieter neighbors, a backing behind the text, a new crop or position.

**Why / how:** Brand material is content. It is how people recognize the product, and on convert and experience pages it is often what makes the page work. Solve hierarchy problems around it by lowering the competing elements, not the material. When text over art fails contrast, back only the text, move it to a calmer region or re-crop the art (`keep-text-contrast-over-images`). When art does not fit a narrow screen, re-crop or reposition it (`crop-art-per-viewport`). When a brand color fails contrast on a button, use a darker or lighter step of the same hue before changing the hue.

**Watch for:** Removing, replacing, shrinking or dimming brand material is a change of direction: propose it and wait for approval. Brand material still has to meet contrast and target-size requirements.

<a id="avoid-template-defaults"></a>

## Avoid template defaults

**When:** The page could belong to any product: an uppercase label above every heading, a headline over subcopy and two buttons, a row of identical icon cards, numbered sections, gradient text, glowing colored shadows, cards inside cards.

**Change:** For each choice, ask whether you would make the same one for an unrelated product; if so, tie it to this product's subject and content, or state why it stays.

**Why / how:** Generated and template interfaces converge on the same safe choices. Each is acceptable alone; together they make a page anonymous, and each one usually replaces a decision that would have done more work. A row of identical cards replaces ranking the content (`rank-content-by-importance`). Gradient text replaces weight and color (`emphasize-with-weight-and-color`). A colored glow replaces a shadow from one light direction (`use-one-light-direction`). Cards inside cards replace grouping with space (`group-with-space-not-borders`). Labels and numbers that state nothing true replace real structure (`structure-matches-content`).

**Watch for:** In an established product, its own design system is not a template to remove; apply this test to new decisions. Do not replace a familiar, working control with an unusual one only to look less generic.

**By mode:**
- browse: Uniform cards and rows are correct here; they make items comparable.

<a id="define-a-personality"></a>

## Define a personality

**When:** The interface feels generic or its typography, colors, corners and copy disagree.

**Change:** Choose a coherent visual and verbal personality suited to the audience.

**Why / how:** Four concrete choices set the personality.

- Typeface: serif reads elegant or classic, rounded sans reads playful, neutral sans reads plain and lets other elements carry the personality.
- Color: blue is safe and familiar, gold reads expensive, pink reads fun. Color psychology helps explain why a choice feels right; it is not a selection method.
- Border radius: none reads formal, small reads neutral, large reads playful. Pick one and keep it; mixing square and rounded corners looks worse than either.
- Language: impersonal copy reads official, casual copy reads friendly. Words matter as much as the visuals.

When unsure, match the register of sites your audience already uses, without borrowing from direct competitors.

**Watch for:** Preserve an existing brand; color associations and example fonts are possibilities, not universal meanings.

**Visuals:** [define-a-personality-2 (example)](figures/define-a-personality-2.webp), [define-a-personality-3 (example)](figures/define-a-personality-3.webp), [define-a-personality-4 (example)](figures/define-a-personality-4.webp). Lookup: `define-a-personality`.

<a id="open-with-the-subject"></a>

## Open with the subject

**When:** A convert or experience page opens with an abstract headline, stock imagery or a generic illustration, while the product's own screens, art or results sit further down.

**Change:** Put the most characteristic thing about the subject in the first viewport: the product working, real screenshots, the game's art, the work itself.

**Why / how:** Visitors decide what a product is from the first screen. Showing the thing is proof; describing it is a claim. A download page shows the product and the download for the visitor's platform. A tool's landing page shows the tool with real data, or puts its main action (a search form, an upload field) on the page in working form. A portfolio opens with the work.

**Watch for:** Use real data or clearly labeled example data. Keep the headline and primary action visible at common laptop and phone heights.

<a id="concentrate-expression"></a>

## Concentrate expression in one region

**When:** Every section of a page competes with its own color, large type, illustration or animation, or no section stands out at all.

**Change:** Choose one region per page for the strongest type, color, imagery or motion, and keep the other regions calmer.

**Why / how:** Emphasis is relative. When every section is loud, none reads as primary and the page looks busy. Pick the region that carries the page's job, usually the hero on a convert page or the main work area on an operate page, and give it the strongest treatment. Keep the other regions consistent and quieter so the chosen one stands out (`de-emphasize-competitors`). To make a page bolder, increase the chosen region's size, contrast or color coverage before adding effects elsewhere.

**Watch for:** Calmer does not mean grey or empty: supporting regions still use the brand's type and color, at lower intensity.

<a id="add-accent-lines"></a>

## Add accent lines

**When:** A restrained interface needs a small amount of identity or a clearer active state.

**Change:** Add a purposeful accent line to a card, alert, heading or active navigation item.

**Why / how:** A colored rectangle needs no illustration skill and makes an interface feel designed. Put an accent border across the top of a card, under the active nav item, along the side of an alert, as a short bar under a headline, or across the top of the whole layout.

**Watch for:** Avoid redundant accents everywhere; selected-state cues must remain perceivable in supported display modes. On square-cornered panels and alerts a side border works. On rounded cards, list items or alerts, a side stripe thicker than 1px clashes with the corner and is a common default in generated interfaces; use a top bar, an underline, a short bar under a heading, or a tinted background with an icon.

**Visuals:** [add-accent-lines-1 (comparison)](figures/add-accent-lines-1.webp), [add-accent-lines-2 (comparison)](figures/add-accent-lines-2.webp). Lookup: `add-accent-lines`.

<a id="decorate-plain-backgrounds"></a>

## Decorate plain backgrounds

**When:** Hierarchy and spacing work but a surface still feels plain.

**Change:** Try a restrained background tone, gentle gradient or low-contrast decorative fragment.

**Why / how:** When hierarchy, spacing and type are right and the result is still plain, change a background. Give a panel or page section a different color, or a subtle gradient between two hues no more than about 30° apart. Add a low-contrast repeating pattern across the background or along a single edge. Place one simple geometric shape, a fragment of a pattern, or a simplified illustration such as a world map. Keep the contrast between decoration and background low so content stays readable.

**Watch for:** Keep decoration behind the content and avoid degrading contrast or implying meaningful data. Diagonal stripes, dot grids and graph-paper grids are common defaults in generated interfaces; use one only when it fits the product's personality. Animated backgrounds follow `reserve-3d-for-visual-subjects`.

**By mode:**
- operate, read: Keep new decoration quiet; existing brand banners stay.
- convert, experience: Brand material can cover large surfaces.

**Visuals:** [decorate-plain-backgrounds-2 (comparison)](figures/decorate-plain-backgrounds-2.webp), [decorate-plain-backgrounds-4 (example)](figures/decorate-plain-backgrounds-4.webp). Lookup: `decorate-plain-backgrounds`.

<a id="rebuild-references-to-learn"></a>

## Rebuild references to learn

**When:** You want to understand which subtle decisions make an admired interface work.

**Change:** Study unexpected choices and reconstruct a small example to expose details in spacing, type and layers.

**Why / how:** When an interface works especially well, identify decisions you would not have made: an inverted date picker, an action placed inside a field, or a headline with selective color emphasis. Rebuilding a small example without inspecting its implementation exposes the effect of line-height, cropping, shadows and tracking. Compare the result with the reference, name the missed decisions, and use those observations in later work.

**Watch for:** Use reconstruction as a learning exercise when requested; apply principles to the current product's identity.

**Visuals:** [rebuild-references-to-learn-1 (example)](figures/rebuild-references-to-learn-1.webp), [rebuild-references-to-learn-2 (example)](figures/rebuild-references-to-learn-2.webp), [rebuild-references-to-learn-3 (example)](figures/rebuild-references-to-learn-3.webp), [rebuild-references-to-learn-4 (diagram)](figures/rebuild-references-to-learn-4.webp). Lookup: `rebuild-references-to-learn`.
