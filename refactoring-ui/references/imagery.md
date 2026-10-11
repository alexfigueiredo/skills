# Imagery

Read the matching rule below. `scripts/find_examples.py --rule <id>` returns its figures when it has them; open them when the rule concerns a visual quantity or you are unsure how far to take it. Figure paths are relative to this file.

<a id="choose-strong-photos"></a>

## Choose strong photos

**When:** Weak lighting or composition undermines an otherwise clear card or hero.

**Change:** Use imagery with appropriate lighting, composition and subject matter at the actual display size.

**Why / how:** Bad photography ruins an otherwise good design. Either hire a photographer (good photos are lighting, composition and color, not equipment) or use high-quality stock, including free sources such as Unsplash. Never design with placeholders expecting to swap in phone photos later; it does not work.

**Watch for:** Work with supplied assets and permissions; do not assume stock imagery suits every product or misrepresents it.

**Visuals:** [choose-strong-photos-1 (comparison)](figures/choose-strong-photos-1.webp). Lookup: `choose-strong-photos`.

<a id="keep-text-contrast-over-images"></a>

## Keep text contrast over images

**When:** Hero text disappears over bright or dark parts of an image.

**Change:** Treat the image or text backing to create a consistent readable foreground-background relationship.

**Why / how:** When no text color works on a hero image, the image is the problem: it has very light and very dark regions, so any single text color fails somewhere. Reduce the image's dynamics. Options, combinable: a semi-transparent overlay (black to support light text, white to support dark text); lowering the image's own contrast, with brightness adjusted to compensate, which is more targeted than an overlay; colorizing it (lower contrast, desaturate, then a solid fill with the multiply blend mode), which also ties the image to the brand palette; a text shadow with a large blur and no offset, which reads as a glow and adds contrast only where needed, letting you reduce image contrast less.

**Watch for:** Check the actual crop and every supported breakpoint; overlays and shadows do not automatically prove sufficient contrast. Video, animated and WebGL backgrounds change brightness over time; check contrast against the brightest frame behind the text. A backdrop blur does not darken what it blurs; add a backing behind the text when the background can approach the text color.

**By mode:**
- convert, experience: Back only the text or move it to a calmer region before darkening the whole image; the art is brand material.

**Visuals:** [keep-text-contrast-over-images-1 (before)](figures/keep-text-contrast-over-images-1.webp), [keep-text-contrast-over-images-3 (after)](figures/keep-text-contrast-over-images-3.webp). Lookup: `keep-text-contrast-over-images`.

<a id="crop-art-per-viewport"></a>

## Crop art per viewport

**When:** Hero art, illustrations or banners disappear, shrink to a thin strip or lose their subject on narrow screens.

**Change:** Re-crop or reposition the art for each viewport so its subject stays visible, instead of hiding it.

**Why / how:** Art that sets the mood on desktop usually carries the brand on a phone too, where it may be the only image on the screen. Choose the focal point for each size: `object-position` for a single image, `<picture>` with separate crops when the composition must change, or a layout that moves the art below the headline. Keep text off the important parts of the subject.

**Watch for:** Check text contrast for each crop. Serve an image size suited to each viewport so phones do not download the desktop file.

<a id="use-graphics-at-their-intended-size"></a>

## Use graphics at their intended size

**When:** Enlarged icons look chunky, small screenshots are unreadable, or favicons lose their shape.

**Change:** Use graphics designed for the target size; crop, simplify or recapture screenshots as needed.

**Why / how:** Upscaled bitmaps become blurry. Vector icons drawn for 16 to 24px also fail when blown up to three or four times their size: they lack detail and look chunky. Keep the icon near its intended size and enclose it in a shape with a background color to fill the larger space. Screenshots fail in the other direction: shrinking a full desktop capture by 70% turns 16px text into 4px. Capture at a smaller viewport (the tablet layout) and give it room, show a partial screenshot, or draw a simplified version with text replaced by lines. Shrinking detailed logos to favicon size makes them illegible; redraw a simplified version at the target size so you control the compromises.

**Watch for:** Keep real product details accurate; a small icon's visual size is separate from its interactive hit area.

**Visuals:** [use-graphics-at-their-intended-size-3 (comparison)](figures/use-graphics-at-their-intended-size-3.webp), [use-graphics-at-their-intended-size-4 (comparison)](figures/use-graphics-at-their-intended-size-4.webp). Lookup: `use-graphics-at-their-intended-size`.

<a id="contain-user-uploaded-images"></a>

## Contain user-uploaded images

**When:** Varied aspect ratios break card layouts, or avatars lose their visible edges.

**Change:** Use consistent image containers with deliberate cropping and subtle edge treatment where needed.

**Why / how:** You cannot tune uploaded images, but you can contain them. Display them in fixed containers, centered and cropped to fit (`background-size: cover` or the equivalent), so varying aspect ratios do not break the layout. When an upload's background matches the UI background, the image loses its edge. A border clashes with the image's colors; a subtle inner box shadow, or a semi-transparent inner border if the inset look is unwanted, keeps the shape without being noticed.

**Watch for:** Preserve the subject and meaningful content; cover-cropping is unsuitable when the entire image must be visible.

**Visuals:** [contain-user-uploaded-images-1 (before)](figures/contain-user-uploaded-images-1.webp), [contain-user-uploaded-images-2 (after)](figures/contain-user-uploaded-images-2.webp). Lookup: `contain-user-uploaded-images`.
