# Hierarchy is Everything

Read the matching rule below; use `scripts/find_examples.py --rule <id>` for its annotated figures. Figure paths are relative to this file.

<a id="not-all-elements-are-equal"></a>

## Not all elements are equal

**When:** A crowded dashboard gives all information and actions equal emphasis.

**Change:** Identify the primary content and soften secondary information before adding decoration.

**Why / how:** When everything competes, a screen reads as a wall of content. De-emphasizing secondary and tertiary information and highlighting what matters makes the same layout, font and colors look better without changing any of them.

**Watch for:** Density can be intentional; preserve information needed for the user's task.

**Visuals:** [fig-036-030 (before)](figures/fig-036-030.webp), [fig-037-031 (after)](figures/fig-037-031.webp). Lookup: `not-all-elements-are-equal`.

<a id="size-isnt-everything"></a>

## Size isn’t everything

**When:** The main text is oversized while supporting details are too small.

**Change:** Use weight and color alongside size to establish readable levels of emphasis.

**Why / how:** Leaning on font size alone produces primary text that is too big and secondary text that is too small. Use weight and color instead. Two or three text colors cover most interfaces: dark for primary content (a headline), grey for secondary (a date), lighter grey for tertiary (a footer notice). Two weights are enough: 400 or 500 for body, 600 or 700 for emphasis. Thin weights can work for large headings but often lose legibility at small sizes; to de-emphasize, use a lighter color or a smaller size instead.

**Watch for:** Secondary text still needs readable contrast and size; example pixel values are not mandates.

**Visuals:** [fig-038-032 (before)](figures/fig-038-032.webp), [fig-039-033 (example)](figures/fig-039-033.webp), [fig-039-034 (example)](figures/fig-039-034.webp), [fig-040-035 (after)](figures/fig-040-035.webp). Lookup: `size-isnt-everything`.

<a id="dont-use-grey-text-on-colored-backgrounds"></a>

## Don’t use grey text on colored backgrounds

**When:** Secondary text on a colored panel looks grey, washed out or disabled.

**Change:** Choose an opaque related text color and check it against the actual background.

**Why / how:** Grey on white works because it lowers contrast with the background. On a colored background, grey text is simply a different color, and white at reduced opacity looks washed out or disabled and lets any pattern behind it show through. Hand-pick a color instead: same hue as the background, saturation and lightness adjusted until the contrast is where you want it.

**Watch for:** Measure contrast; transparency is acceptable when its composited result is deliberate and verified.

**Visuals:** [fig-042-036 (before)](figures/fig-042-036.webp), [fig-044-040 (after)](figures/fig-044-040.webp). Lookup: `dont-use-grey-text-on-colored-backgrounds`.

<a id="emphasize-by-de-emphasizing"></a>

## Emphasize by de-emphasizing

**When:** The active navigation or main content cannot stand out because neighboring elements compete.

**Change:** Reduce the emphasis of competitors, such as inactive links or a sidebar panel.

**Why / how:** When the main element will not stand out and there is nothing left to add to it, remove emphasis from its competitors. An active nav item pops when the inactive ones get a softer color. A sidebar stops competing with the content when it loses its background and sits on the page background.

**Watch for:** Inactive navigation is still available navigation, not a disabled control; maintain contrast and a non-color active cue.

**Visuals:** [fig-046-041 (before)](figures/fig-046-041.webp), [fig-046-042 (after)](figures/fig-046-042.webp). Lookup: `emphasize-by-de-emphasizing`.

<a id="labels-are-a-last-resort"></a>

## Labels are a last resort

**When:** Displayed data is buried in repetitive label-value pairs.

**Change:** Use recognizable formats or combine labels with values, emphasizing what people scan for.

**Why / how:** Showing data as `label: value` pairs gives every field equal weight. Formats identify themselves: an email address, a phone number, a price. Context identifies more: "Customer Support" under a name in a directory is clearly a department. When a label is still needed, fold it into the value: "12 left in stock", "3 bedrooms". When several similar values must be scanned (a dashboard), keep the label but make it secondary: smaller, lighter, or lower contrast. The exception is pages users scan by label, such as a spec sheet where they look for "depth", not "7.6mm"; there, make the label darker and the value slightly lighter, without burying the value.

**Watch for:** This rule concerns displayed data, not form labels or accessible names. Keep labels when meaning is ambiguous or users scan by label.

**Visuals:** [fig-048-044 (before)](figures/fig-048-044.webp), [fig-049-045 (after)](figures/fig-049-045.webp). Lookup: `labels-are-a-last-resort`.

<a id="separate-visual-hierarchy-from-document-hierarchy"></a>

## Separate visual hierarchy from document hierarchy

**When:** A large page title competes with more important task content.

**Change:** Choose heading elements for document structure and style their visual emphasis independently.

**Why / how:** Browsers make `h1` big and `h6` small, which suits articles and tempts you into oversized page titles in applications. Section titles usually act as labels for the content below them and can be visually modest without losing their semantic heading level. Choose the element for semantics and style it for hierarchy.

**Watch for:** Do not change heading levels or remove accessible structure merely to make text smaller.

**Visuals:** [fig-054-050 (before)](figures/fig-054-050.webp), [fig-055-051 (after)](figures/fig-055-051.webp). Lookup: `separate-visual-hierarchy-from-document-hierarchy`.

<a id="balance-weight-and-contrast"></a>

## Balance weight and contrast

**When:** Solid icons overpower nearby labels, or thin borders are either harsh or invisible.

**Change:** Balance visual area against contrast: soften heavy icons or slightly thicken pale separators.

**Why / how:** Bold text feels emphasized because it covers more surface area. Solid icons are heavy for the same reason and tend to overpower the text next to them. For a fixed icon asset, try a softer color to balance its visual weight; another suitable icon weight is also an option. The reverse also holds: a 1px border that is too subtle in a soft color but harsh when darkened can be made heavier instead; a thicker border adds emphasis while keeping the soft color.

**Watch for:** Required control boundaries and meaningful icons need adequate contrast; decorative examples are not universal tokens.

**Visuals:** [fig-057-053 (before)](figures/fig-057-053.webp), [fig-057-054 (after)](figures/fig-057-054.webp). Lookup: `balance-weight-and-contrast`.

<a id="semantics-are-secondary"></a>

## Semantics are secondary

**When:** Every action is a loud colored button, including rare destructive actions.

**Change:** Assign primary, secondary and tertiary emphasis according to each action's role in the current task.

**Why / how:** Styling buttons purely by meaning yields a row of equally loud actions. Each page has one true primary action, a couple of secondary ones and some rarely used tertiary ones. Primary: solid, high-contrast fill. Secondary: outline or low-contrast fill. Tertiary: link style. A destructive action that is not the primary action on the page gets secondary or tertiary styling; the big red button belongs on the confirmation step, where destroying is the primary action.

**Watch for:** The title refers to visual button priority, not HTML semantics. Keep destructive labels and required confirmations clear.

**Visuals:** [fig-060-057 (before)](figures/fig-060-057.webp), [fig-061-058 (after)](figures/fig-061-058.webp). Lookup: `semantics-are-secondary`.
