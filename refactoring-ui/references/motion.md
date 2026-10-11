# Motion

Motion and expressive surfaces (animated backgrounds, 3D scenes, shaders) follow the page mode; see the motion budget in [page modes](surfaces.md). Add them after hierarchy, layout and contrast work, never in place of it.

Read the matching rule below. `scripts/find_examples.py --rule <id>` returns its figures when it has them; open them when the rule concerns a visual quantity or you are unsure how far to take it. Figure paths are relative to this file.

<a id="animate-to-explain-state"></a>

## Animate to explain state

**When:** Sections fade in on scroll, every card moves on hover, content waits for an animation, or transitions feel slow.

**Change:** Animate feedback, state changes and spatial continuity, and keep content visible without the animation.

**Why / how:** Motion helps when it answers an action or shows where something came from: a button that responds to a press, a panel that slides from the control that opened it, a list item that collapses when deleted. Motion the user did not trigger competes with the content. Keep durations short: about 100–200 ms for feedback on a control, 200–300 ms for state changes, up to about 400 ms for large panels and overlays. Exits can be faster than entrances. Use easing that decelerates into the final position.

**Watch for:** Content must be present and readable if the animation never runs. Under `prefers-reduced-motion: reduce`, remove movement and keep the color or opacity changes that confirm an action.

**By mode:**
- convert, experience: One entrance in the first viewport or one scroll-linked scene, not a reveal on every section, plus feedback on actions.
- operate, browse: Feedback, filtering and state changes only, at the durations above; no load choreography.
- read: Almost none beyond feedback on controls.

<a id="reserve-3d-for-visual-subjects"></a>

## Reserve 3D and shaders for visual subjects

**When:** A 3D scene, shader or animated background is being considered, or one already slows the page or competes with its content.

**Change:** Use one only where the subject is visual or spatial (a product, a game world, a map, the brand's mood on a convert page), in one region, behind or beside HTML text, with a static fallback.

**Why / how:** An expressive surface can carry a brand on convert and experience pages; on operate, browse and read pages it competes with the task. Use the cheapest medium that works: the product's own art, then CSS gradients, SVG patterns or grain, then OGL for one shader or three.js or React Three Fiber for a scene, then a component from a catalog such as ThreeUI as a starting point. To integrate one:

- Map its colors and fonts to the project's tokens. Hue and saturation filters only approximate a brand color.
- Keep headlines and actions in HTML, in the product's type.
- Load it after the main content, cap the pixel ratio at 2, pause it off-screen and in hidden tabs, and check the frame rate on a mid-range phone.
- Show a static poster before it starts and when WebGL is unavailable.
- Under reduced motion, show a still frame with the same composition.
- Measure text contrast against the brightest frame.
- Mark decorative canvases `aria-hidden` with `pointer-events: none`.

Treat catalog components as starting points to adapt to the product, not files to copy unchanged, and check each one's license.

**Watch for:** On operate pages, do not add decorative 3D, shaders or animated backgrounds; a 3D view that is the work itself, such as a model viewer, is content. A canvas must never be the only place that holds text, the primary action or information.
