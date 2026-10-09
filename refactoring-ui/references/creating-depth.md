# Creating Depth

Read the matching rule below; use `scripts/find_examples.py --rule <id>` for its annotated figures. Figure paths are relative to this file.

<a id="emulate-a-light-source"></a>

## Emulate a light source

**When:** Raised and inset controls feel flat or their light cues contradict each other.

**Change:** Use a consistent implied light direction with restrained edge highlights and shadows.

**Why / how:** Raised and inset looks come from one rule: light comes from above. A raised panel has a lighter top edge (facing the light) and a darker bottom edge; an inset panel has a shadow at the top (the lip above blocks the light) and a lighter bottom edge. Decide the element's profile, then mimic how light would hit it. Raised button: because people look slightly down at their screens, show a bit of the top edge and hide the bottom one. Make the top edge slightly lighter with a top border or an inset shadow with a small positive vertical offset, hand-picking the lighter color rather than overlaying translucent white, which desaturates. Then add a small, dark, sharp shadow below with a slight vertical offset and only a couple of pixels of blur; a window frame's shadow is the real-world reference. Inset well, input or checkbox: a lighter bottom edge via a bottom border or an inset shadow with a negative offset, plus a small dark inset shadow at the top with a positive offset. Stop before photo-realism; a few cues add depth, more add noise.

**Watch for:** Depth is optional and should suit the established visual style; avoid decorative cues that imply nonexistent controls.

**Visuals:** [fig-176-197 (comparison)](figures/fig-176-197.webp), [fig-176-198 (comparison)](figures/fig-176-198.webp). Lookup: `emulate-a-light-source`.

<a id="use-shadows-to-convey-elevation"></a>

## Use shadows to convey elevation

**When:** Buttons, menus and dialogs appear to sit at arbitrary or indistinguishable depths.

**Change:** Choose shadows from a small elevation scale matched to each element's layering role.

**Why / how:** Shadow size places an element on a virtual z-axis. Tight, small shadows feel slightly raised; large, blurry shadows feel close to the viewer, and closeness draws attention. Buttons get small shadows, dropdowns medium, modals large. Define a fixed set; five is plenty. Set the smallest and largest, then fill in roughly linear steps. A set that works, all in `hsla(0, 0%, 0%, .2)`: `0 1px 3px`, `0 4px 6px`, `0 5px 15px`, `0 10px 24px`, `0 15px 35px`. Shadows also answer interaction: a list item grows a shadow when picked up for dragging, a button loses or shrinks its shadow when pressed. Choose shadows by asking where the element sits on the z-axis, not by taste.

**Watch for:** Shadow does not fix stacking, clipping or focus behavior; dark themes may need other separation cues.

**Visuals:** [fig-181-204 (comparison)](figures/fig-181-204.webp), [fig-181-205 (comparison)](figures/fig-181-205.webp), [fig-182-206 (comparison)](figures/fig-182-206.webp). Lookup: `use-shadows-to-convey-elevation`.

<a id="shadows-can-have-two-parts"></a>

## Shadows can have two parts

**When:** A shadow feels muddy or its surface edge lacks definition.

**Change:** Combine a broad soft shadow with a tighter contact shadow, reducing the latter at higher elevation.

**Why / how:** Polished shadows are usually two shadows with distinct jobs. The first is large, soft and offset: the shadow a direct light casts behind the object. The second is tight and dark with little offset and blur: the area underneath where even ambient light does not reach. Together they let the large shadow stay subtle while the edge stays defined. The tight one fades as elevation rises, since an object far from a surface no longer darkens the surface directly beneath it; make it distinct at the lowest elevation and nearly or completely gone at the highest.

**Watch for:** Use the project's elevation tokens and inspect both supported themes; two shadows are a technique, not a requirement.

**Visuals:** [fig-188-213 (comparison)](figures/fig-188-213.webp), [fig-189-214 (diagram)](figures/fig-189-214.webp). Lookup: `shadows-can-have-two-parts`.

<a id="even-flat-designs-can-have-depth"></a>

## Even flat designs can have depth

**When:** A flat interface needs clearer separation without realistic soft shadows.

**Change:** Use surface tones or a crisp offset shadow to indicate layering.

**Why / how:** Flat design drops shadows and gradients but still conveys depth. Lighter objects feel closer, darker ones further away, so an element lighter than its background reads as raised and one darker reads as a well. Solid shadows (short vertical offset, zero blur) lift a card or button while keeping the flat look.

**Watch for:** Lightness-to-depth is a visual convention, not a universal rule; verify it in the current theme.

**Visuals:** [fig-191-216 (diagram)](figures/fig-191-216.webp), [fig-192-217 (example)](figures/fig-192-217.webp). Lookup: `even-flat-designs-can-have-depth`.

<a id="overlap-elements-to-create-layers"></a>

## Overlap elements to create layers

**When:** Separate blocks feel disconnected, or overlapping images visually collide.

**Change:** Let selected elements cross a section boundary and use a background-colored gap between overlapping images.

**Why / how:** Overlap creates layers. Offset a card so it crosses the boundary between two background colors, make an element taller than its parent so it overlaps on both sides, or let carousel controls straddle the image edge. Overlapping images clash unless each has an invisible border in the background color, which keeps a gap between them while preserving the layered effect.

**Watch for:** Preserve readable content, focus visibility and narrow-screen flow; do not introduce overlap solely for decoration.

**Visuals:** [fig-196-221 (before)](figures/fig-196-221.webp), [fig-194-218 (comparison)](figures/fig-194-218.webp), [fig-196-222 (after)](figures/fig-196-222.webp). Lookup: `overlap-elements-to-create-layers`.
