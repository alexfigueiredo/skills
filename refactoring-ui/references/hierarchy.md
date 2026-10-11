# Hierarchy

Read the matching rule below. `scripts/find_examples.py --rule <id>` returns its figures when it has them; open them when the rule concerns a visual quantity or you are unsure how far to take it. Figure paths are relative to this file.

<a id="rank-content-by-importance"></a>

## Rank content by importance

**When:** A crowded dashboard gives all information and actions equal emphasis.

**Change:** Identify the primary content and soften secondary information before adding decoration.

**Why / how:** When everything competes, a screen reads as a wall of content. De-emphasizing secondary and tertiary information and highlighting what matters makes the same layout, font and colors look better without changing any of them.

**Watch for:** Density can be intentional; preserve information needed for the user's task.

**By mode:**
- convert: Rank the sections by the page's job and vary their size and treatment instead of repeating identical cards.
- browse: Items are peers by design; rank the controls and metadata around them.

**Visuals:** [rank-content-by-importance-1 (before)](figures/rank-content-by-importance-1.webp), [rank-content-by-importance-2 (after)](figures/rank-content-by-importance-2.webp). Lookup: `rank-content-by-importance`.

<a id="emphasize-with-weight-and-color"></a>

## Emphasize with weight and color, not only size

**When:** The main text is oversized while supporting details are too small.

**Change:** Use weight and color alongside size to establish readable levels of emphasis.

**Why / how:** Leaning on font size alone produces primary text that is too big and secondary text that is too small. Use weight and color instead. Two or three text colors cover most interfaces: dark for primary content (a headline), grey for secondary (a date), lighter grey for tertiary (a footer notice). Two weights are enough: 400 or 500 for body, 600 or 700 for emphasis. Thin weights can work for large headings but often lose legibility at small sizes; to de-emphasize, use a lighter color or a smaller size instead.

**Watch for:** Secondary text still needs readable contrast and size; example pixel values are not mandates.

**By mode:**
- convert, experience: A display typeface keeps its own weight; the two-weight limit applies to interface text.

**Visuals:** [emphasize-with-weight-and-color-1 (before)](figures/emphasize-with-weight-and-color-1.webp), [emphasize-with-weight-and-color-2 (example)](figures/emphasize-with-weight-and-color-2.webp), [emphasize-with-weight-and-color-3 (example)](figures/emphasize-with-weight-and-color-3.webp), [emphasize-with-weight-and-color-4 (after)](figures/emphasize-with-weight-and-color-4.webp). Lookup: `emphasize-with-weight-and-color`.

<a id="tint-secondary-text-on-color"></a>

## Tint secondary text on colored backgrounds

**When:** Secondary text on a colored panel looks grey, washed out or disabled.

**Change:** Choose an opaque related text color and check it against the actual background.

**Why / how:** Grey on white works because it lowers contrast with the background. On a colored background, grey text is simply a different color, and white at reduced opacity looks washed out or disabled and lets any pattern behind it show through. Hand-pick a color instead: same hue as the background, saturation and lightness adjusted until the contrast is where you want it.

**Watch for:** Measure contrast; transparency is acceptable when its composited result is deliberate and verified.

**Visuals:** [tint-secondary-text-on-color-1 (before)](figures/tint-secondary-text-on-color-1.webp), [tint-secondary-text-on-color-5 (after)](figures/tint-secondary-text-on-color-5.webp). Lookup: `tint-secondary-text-on-color`.

<a id="de-emphasize-competitors"></a>

## De-emphasize competing elements

**When:** The active navigation or main content cannot stand out because neighboring elements compete.

**Change:** Reduce the emphasis of competitors, such as inactive links or a sidebar panel.

**Why / how:** When the main element will not stand out and there is nothing left to add to it, remove emphasis from its competitors. An active nav item stands out when the inactive ones get a softer color. A sidebar stops competing with the content when it loses its background and sits on the page background.

**Watch for:** Inactive navigation is still available navigation, not a disabled control; maintain contrast and a non-color active cue.

**By mode:**
- convert, experience: Quiet the neighbors; do not shrink or dim the headline or brand art to balance them.

**Visuals:** [de-emphasize-competitors-1 (before)](figures/de-emphasize-competitors-1.webp), [de-emphasize-competitors-2 (after)](figures/de-emphasize-competitors-2.webp). Lookup: `de-emphasize-competitors`.

<a id="let-values-identify-themselves"></a>

## Let values identify themselves

**When:** Displayed data is buried in repetitive label-value pairs.

**Change:** Use recognizable formats or combine labels with values, emphasizing what people scan for.

**Why / how:** Showing data as `label: value` pairs gives every field equal weight. Formats identify themselves: an email address, a phone number, a price. Context identifies more: "Customer Support" under a name in a directory is clearly a department. When a label is still needed, fold it into the value: "12 left in stock", "3 bedrooms". When several similar values must be scanned (a dashboard), keep the label but make it secondary: smaller, lighter, or lower contrast. The exception is pages users scan by label, such as a spec sheet where they look for "depth", not "7.6mm"; there, make the label darker and the value slightly lighter, without burying the value.

**Watch for:** This rule concerns displayed data, not form labels or accessible names. Keep labels when meaning is ambiguous or users scan by label.

**Visuals:** [let-values-identify-themselves-1 (before)](figures/let-values-identify-themselves-1.webp), [let-values-identify-themselves-2 (after)](figures/let-values-identify-themselves-2.webp). Lookup: `let-values-identify-themselves`.

<a id="structure-matches-content"></a>

## Structure matches content

**When:** Numbered markers, small uppercase labels above headings, or dividers appear where the content has no order, category or boundary.

**Change:** Remove them; keep each one only where it states something true that the heading and navigation do not.

**Why / how:** Readers treat visual structure as information. Numbers say the items form a sequence, a label above a heading says the section belongs to a category, and a divider says two parts are separate. A "Team Builder" label above a page titled "Build Lab" repeats the navigation. "01" to "04" on four independent links implies an order that does not exist. Number steps that happen in order, label sections with a category the reader needs, and separate parts that are distinct.

**Watch for:** Ordered steps, real categories and real boundaries still need their markers.

<a id="separate-visual-hierarchy-from-document-hierarchy"></a>

## Separate visual hierarchy from document hierarchy

**When:** A large page title competes with more important task content.

**Change:** Choose heading elements for document structure and style their visual emphasis independently.

**Why / how:** Browsers make `h1` big and `h6` small, which suits articles and tempts you into oversized page titles in applications. Section titles usually act as labels for the content below them and can be visually modest without losing their semantic heading level. Choose the element for semantics and style it for hierarchy.

**Watch for:** Do not change heading levels or remove accessible structure merely to make text smaller.

**By mode:**
- convert, experience: The display headline is content; keep it large. Style the section titles below it modestly.

**Visuals:** [separate-visual-hierarchy-from-document-hierarchy-1 (before)](figures/separate-visual-hierarchy-from-document-hierarchy-1.webp), [separate-visual-hierarchy-from-document-hierarchy-2 (after)](figures/separate-visual-hierarchy-from-document-hierarchy-2.webp). Lookup: `separate-visual-hierarchy-from-document-hierarchy`.

<a id="balance-weight-and-contrast"></a>

## Balance weight and contrast

**When:** Solid icons overpower nearby labels, or thin borders are either harsh or invisible.

**Change:** Balance visual area against contrast: soften heavy icons or slightly thicken pale separators.

**Why / how:** Bold text feels emphasized because it covers more surface area. Solid icons are heavy for the same reason and tend to overpower the text next to them. For a fixed icon asset, try a softer color to balance its visual weight; another suitable icon weight is also an option. The reverse also holds: a 1px border that is too subtle in a soft color but harsh when darkened can be made heavier instead; a thicker border adds emphasis while keeping the soft color.

**Watch for:** Required control boundaries and meaningful icons need adequate contrast; decorative examples are not universal tokens.

**Visuals:** [balance-weight-and-contrast-2 (before)](figures/balance-weight-and-contrast-2.webp), [balance-weight-and-contrast-3 (after)](figures/balance-weight-and-contrast-3.webp). Lookup: `balance-weight-and-contrast`.

<a id="style-actions-by-priority"></a>

## Style actions by priority

**When:** Every action is a loud colored button, including rare destructive actions.

**Change:** Assign primary, secondary and tertiary emphasis according to each action's role in the current task.

**Why / how:** Styling buttons purely by meaning yields a row of equally loud actions. Each page has one true primary action, a couple of secondary ones and some rarely used tertiary ones. Primary: solid, high-contrast fill. Secondary: outline or low-contrast fill. Tertiary: link style. A destructive action that is not the primary action on the page gets secondary or tertiary styling; the big red button belongs on the confirmation step, where destroying is the primary action.

**Watch for:** The title refers to visual button priority, not HTML semantics. Keep destructive labels and required confirmations clear.

**By mode:**
- convert: The page's primary action keeps the brand color at full strength; make the secondary actions quieter instead.

**Visuals:** [style-actions-by-priority-1 (before)](figures/style-actions-by-priority-1.webp), [style-actions-by-priority-2 (after)](figures/style-actions-by-priority-2.webp). Lookup: `style-actions-by-priority`.
