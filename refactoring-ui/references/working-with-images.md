# Working with Images

Read the matching rule below; use `scripts/find_examples.py --rule <id>` for its annotated figures. Figure paths are relative to this file.

<a id="use-good-photos"></a>

## Use good photos

**When:** Weak lighting or composition undermines an otherwise clear card or hero.

**Change:** Use imagery with appropriate lighting, composition and subject matter at the actual display size.

**Why / how:** Bad photography ruins an otherwise good design. Either hire a photographer (good photos are lighting, composition and color, not equipment) or use high-quality stock, including free sources such as Unsplash. Never design with placeholders expecting to swap in phone photos later; it does not work.

**Watch for:** Work with supplied assets and permissions; do not assume stock imagery suits every product or misrepresents it.

**Visuals:** [fig-200-223 (comparison)](figures/fig-200-223.webp). Lookup: `use-good-photos`.

<a id="text-needs-consistent-contrast"></a>

## Text needs consistent contrast

**When:** Hero text disappears over bright or dark parts of an image.

**Change:** Treat the image or text backing to create a consistent readable foreground-background relationship.

**Why / how:** When no text color works on a hero image, the image is the problem: it has very light and very dark regions, so any single text color fails somewhere. Reduce the image's dynamics. Options, combinable: a semi-transparent overlay (black to support light text, white to support dark text); lowering the image's own contrast, with brightness adjusted to compensate, which is more targeted than an overlay; colorizing it (lower contrast, desaturate, then a solid fill with the multiply blend mode), which also ties the image to the brand palette; a text shadow with a large blur and no offset, which reads as a glow and adds contrast only where needed, letting you reduce image contrast less.

**Watch for:** Check the actual crop and every supported breakpoint; overlays and shadows do not automatically prove sufficient contrast.

**Visuals:** [fig-202-224 (before)](figures/fig-202-224.webp), [fig-203-226 (after)](figures/fig-203-226.webp). Lookup: `text-needs-consistent-contrast`.

<a id="everything-has-an-intended-size"></a>

## Everything has an intended size

**When:** Enlarged icons look chunky, small screenshots are unreadable, or favicons lose their shape.

**Change:** Use graphics designed for the target size; crop, simplify or recapture screenshots as needed.

**Why / how:** Upscaled bitmaps go fuzzy; everyone knows that. Vector icons drawn for 16 to 24px also fail when blown up to three or four times their size: they lack detail and look chunky. Keep the icon near its intended size and enclose it in a shape with a background color to fill the larger space. Screenshots fail in the other direction: shrinking a full desktop capture by 70% turns 16px text into 4px. Capture at a smaller viewport (the tablet layout) and give it room, show a partial screenshot, or draw a simplified version with text replaced by lines. Shrinking detailed logos to favicon size turns them to mush; redraw a simplified version at the target size so you control the compromises.

**Watch for:** Keep real product details accurate; a small icon's visual size is separate from its interactive hit area.

**Visuals:** [fig-209-232 (comparison)](figures/fig-209-232.webp), [fig-209-233 (comparison)](figures/fig-209-233.webp). Lookup: `everything-has-an-intended-size`.

<a id="beware-user-uploaded-content"></a>

## Beware user-uploaded content

**When:** Varied aspect ratios break card layouts, or avatars lose their visible edges.

**Change:** Use consistent image containers with deliberate cropping and subtle edge treatment where needed.

**Why / how:** You cannot tune uploaded images, but you can contain them. Display them in fixed containers, centered and cropped to fit (`background-size: cover` or the equivalent), so varying aspect ratios do not break the layout. When an upload's background matches the UI background, the image loses its edge. A border clashes with the image's colors; a subtle inner box shadow, or a semi-transparent inner border if the inset look is unwanted, keeps the shape without being noticed.

**Watch for:** Preserve the subject and meaningful content; cover-cropping is unsuitable when the entire image must be visible.

**Visuals:** [fig-214-241 (before)](figures/fig-214-241.webp), [fig-215-242 (after)](figures/fig-215-242.webp). Lookup: `beware-user-uploaded-content`.
