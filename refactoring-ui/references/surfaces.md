# Page Modes

Classify every page before applying other rules. The same rule can be right on a tool and wrong on a landing page, so the mode decides how each rule applies. Classify by what success means for the visitor on that page, not by the product: a game's download page converts; its leaderboard is browsed.

## The five modes

| Mode | Visitor's success | Typical pages | First viewport shows |
| --- | --- | --- | --- |
| convert | decides and acts | marketing home, landing, download, pricing, sign-up | the offer, the primary action in working form, one piece of proof |
| operate | completes a task | dashboard, editor, builder, settings, admin | the work area and its current data |
| browse | scans and compares items | catalog, tier list, leaderboard, search results, gallery, item or profile detail | the items, with filters and sorting next to them |
| read | understands something | docs, wiki, guide, changelog, legal, status | the title and the start of the reading column |
| experience | uses or enjoys the work itself | game, portfolio, interactive showcase, media | the work, with controls small or hidden until needed |

A page can contain regions in other modes, such as a pricing table on a landing page. Classify the page by its main job and each region by its own. A logged-in home or a hub of tools is operate or browse.

## What changes by mode

| | convert | operate | browse | read | experience |
| --- | --- | --- | --- | --- | --- |
| Brand expression | Full: display type, brand art, brand color on large surfaces | Logo, accents and one product-specific detail, such as the brand color on the active navigation item; standard controls and navigation | Carried by item images; new chrome stays quiet | In the frame (header, section openings, tables, code); the reading column stays neutral | Carried by the work |
| Density | Low; one idea per viewport | High when deliberate | High; many comparable items per screen | Moderate | Set by the work |
| Type | Display face allowed; wide ratio between headline and body | One family; the small end of the type scale (about 12–24 px) | Compact scale; tabular figures for numbers | Body near 16 px; 60–75 characters per line | Set by the work |
| Imagery | The product, its art or real screenshots, as proof | Functional only (avatars, thumbnails, previews) | Uniform containers that make items comparable | Diagrams and screenshots that explain | The work itself |
| Motion | One entrance in the first viewport or one scroll-linked scene, plus feedback | Feedback and state changes at the durations in `animate-to-explain-state` | Feedback, filtering and sorting transitions | Almost none | As the work requires |
| Repetition | Identical cards are a weakness; vary composition by content | Consistent components are a strength | Uniform cards and rows are correct | Consistent headings and spacing | Varies |

The rows set how much new expression to design. Existing brand material stays on every page (`preserve-brand-material`).

Rules whose advice changes by mode carry a note for each affected mode under **By mode** in the reference. `scripts/find_examples.py "<symptom>" --mode <mode>` prints the note for that mode.

## Sites with several modes

Keep the shell shared: navigation, footer, tokens, type families, button styles and focus treatment. Vary each page's composition by its mode. If pages in different modes end up with the same composition (the same label, heading, paragraph and card grid on every page), the classification was not applied.

## Page map

Before changing anything, write the page map in the response:

| Page | Mode | Visitor's goal | Success action | Brand material on the page |
| --- | --- | --- | --- | --- |

For a single page, one line is enough. List the brand material even when the request is only about layout; [visual direction](direction.md) explains what may change.

## Checks by mode

- **convert**: Within five seconds, a visitor can say what this is, why it matters to them and what to do next. With the product name covered, the page should not fit a competitor.
- **operate**: With the product name covered, the page is recognizable as a tool of its category, and the main task can be done without instructions.
- **browse**: Items can be compared without opening them; filters and sorting are next to the results.
- **read**: The reader can tell where they are, what the page answers and where to go next.
- **experience**: The work appears first, and the controls can be found when needed.
