# Review

Use this for critiques and broad visual reviews, and as the last step of any implementation.

## Procedure

1. Write the page map from [page modes](surfaces.md).
2. Look at each page at a desktop width and a phone width (about 375 px), in its main states. Form your own visual judgment before reading the output of automated checks, then reconcile the two.
3. Walk the rules at a glance in `SKILL.md` against each page, in order, applying each rule's note for the page's mode.
4. Run the check for each page's mode.
5. Report the findings. When implementation was requested, fix them in priority order.

State which pages, widths and states you could not inspect.

## Severity

- **P0**: Blocks the task or misleads: a broken flow, hidden required information, a state that says the wrong thing.
- **P1**: Causes significant difficulty or fails WCAG AA: unreadable text, invisible focus, unreachable navigation, a missing state, brand material removed, hidden or dimmed on a convert or experience page.
- **P2**: An annoyance with a workaround: weak hierarchy, ambiguous grouping, inconsistent components, lost brand material on other pages.
- **P3**: Polish: alignment, tracking, small inconsistencies.

Fix in this order: P0 and P1, then missing states, then hierarchy, brand and responsive problems, then consistency, then polish. Fix contrast without dimming brand material (`preserve-brand-material`).

## Finding format

For each finding, give the page and element, its mode, the severity, what is wrong and why it matters, the rule id, and the specific change. Group findings by page.

## Verification after changes

- Before and after screenshots at the same widths and in the same states.
- Widths just below and above each layout switch, and long content.
- Text contrast over images and in every supported theme.
- The brand material from the page map is still present.
- Pages in different modes do not share one composition.
- Keyboard focus is visible, and the tab order follows the layout.

Take one round of screenshots, fix in one batch and confirm once, instead of re-checking after every small edit.
