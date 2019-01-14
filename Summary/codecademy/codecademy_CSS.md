# CSS

## Display and Positioning

- `position`
- `display`
- `z-index`
- `float`
- `clear`

### Position

1. `static` - the default value (it does not need to be specified) and the z-index will be ignored
2. `relative`
3. `absolute`
4. `fixed`

#### Position: Relative

The `<div>` has been positioned using two of the four *offset properties*.

1. `top` - moves the element down.
2. `bottom` - moves the element up.
3. `left` - moves the element right.
4. `right` - moves the element left.

```css
.box-bottom {
  background-color: DeepSkyBlue;
  position: relative;
  top: 20px;
  left: 50px;
}
```

![relative](C:\Users\student\TIL\Summary\codecademy\image\relative.png)

#### Position: Absolute

```css
.box-bottom {
  background-color: DeepSkyBlue;
  position: absolute;
  top: 20px;
  left: 50px;
}
```

![absolute](C:\Users\student\TIL\Summary\codecademy\image\absolute.gif)

#### Position: Fixed

```css
.box-bottom {
  background-color: DeepSkyBlue;
  position: fixed;
  top: 20px;
  left: 50px;
}
```

![fixed](C:\Users\student\TIL\Summary\codecademy\image\fixed.gif)

#### Z-Index

```css
.box-top {
  background-color: Aquamarine;
  position: relative;
  z-index: 2;
}

.box-bottom {
  background-color: DeepSkyBlue;
  position: absolute;
  top: 20px;
  left: 50px;
  z-index: 1;
}
```

The z-index of `2` moves the `.box-top` element forward, because it is greater than the `.box-bottom` z-index, `1`. See the example image below:

![z-index](C:\Users\student\TIL\Summary\codecademy\image\z-index.png)

### Display

`display` property: 1. `inline`, 2. `block`, and 3. `inline-block`

#### Inline Display

Inline elements have a box that wraps tightly around their content, only taking up the amount of space necessary to display their content and not requiring a new line after each element. 

Ex) `<em>`, `<strong>`, and `<a>`, is called *inline*.

```html
To learn more about <em>inline</em> elements, read <a href="#">MDN documentation</a>.
```

To learn more about *inline* elements, click [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements).

```css
h1 {
  display: inline;
}
```

The CSS in the example above will change the display of all `<h1>` elements to `inline`.

**does not start a new line and cannot be sized using the `height` and `width` properties.**

#### Block Display

*Block-level* elements are **not** displayed in the same line as the content around them.

Ex) all levels of heading elements (`<h1>` through `<h6>`), `<p>`, `<div>` and `<footer>`.

```css
strong {
  display: block;
}
```

**starts a new line and can be sized using the `height` and `width` properties.**

#### Inline-Block Display

Ex) ` <div>`

```html
<div class="rectangle">
  <p>I’m a rectangle!</p>
</div>
<div class="rectangle">
  <p>So am I!</p>
</div>
<div class="rectangle">
  <p>Me three!</p>
</div>
```

```css
.rectangle {
  display: inline-block;
  width: 200px;
  height: 300px;
}
```

**does not start a new line and can be sized using the `height` and `width` properties.**

### Float

The `float` property can be set to one of two values:

1. `left` - this value will move, or float, elements as far left as possible.
2. `right` - this value will move elements as far right as possible.

```css
.boxes {
  width: 120px;
  height: 70px;
}

.box-bottom {
  background-color: DeepSkyBlue;
  float: right;
}
```

![float-right](C:\Users\student\TIL\Summary\codecademy\image\float-right.png)

### Clear

The `clear` property specifies how elements should behave when they bump into each other on the page.

1. `left` — the left side of the element will not touch any other element within the same containing element.
2. `right` — the right side of the element will not touch any other element within the same containing element.
3. `both` — neither side of the element will touch any other element within the same containing element.
4. `none` — the element can touch either side.

### Summary

1. The `position` property allows you to specify the position of an element in three different ways.
2. When set to `relative`, an element's position is relative to its default position on the page.
3. When set to `absolute`, an element's position is relative to its closest positioned parent element. It can be pinned to any part of the web page, but the element will still move with the rest of the document when the page is scrolled.
4. When set to `fixed`, an element's position can be pinned to any part of the web page. The element will remain in view no matter what.
5. The `z-index` of an element specifies how far back or how far forward an element appears on the page when it overlaps other elements.
6. The `display` property allows you control how an element flows vertically and horizontally a document.
7. `inline` elements take up as little space as possible, and they cannot have manually-adjusted `width` or `height`.
8. `block` elements take up the width of their container and can have manually-adjusted `height`s.
9. `inline-block` elements can have set `width`and `height`, but they can also appear next to each other and do not take up their entire container width.
10. The `float` property can move elements as far left or as far right as possible on a web page.
11. You can clear an element's left or right side (or both) using the `clear` property.

## Color

Colors in CSS can be described in three different ways:

- *Named colors* — English words that describe colors, also called *keyword colors*
- *RGB* — numeric values that describe a mix of red, green, and blue
- *HSL* — numeric values that describe a mix of hue, saturation, and lightness

### Foreground vs Background

1. `color` - this property styles an element's foreground color.
2. `background-color` - this property styles an element's background color.

```css
h1 {
  color: Red;
  background-color: Blue;
}
```

### Hexadecimal

```css
DarkSeaGreen: #8FBC8F
Sienna:       #A0522D
SaddleBrown:  #8B4513
Brown:        #A52A2A
Black:        #000000 or #000
White:        #FFFFFF or #FFF
Aqua:         #00FFFF or #0FF
```

### RGB Colors

```css
h1 {
  color: rgb(23, 45, 23);
}
```

The first number represents the amount of red, the second is green, and the third is blue. 

### Hex and RGB

`256 * 256 * 256 = 16,777,216`. Compare that to the 147 named CSS colors.

### Hue, Saturation, and Lightness(색조, 채도 및 밝기)

```css
color: hsl(120, 60%, 70%);
```

* *Hue* is the first number. It refers to an angle on a color wheel. Red is 0 degrees, Green is 120 degrees, Blue is 240 degrees, and then back to Red at 360. You can see an example of a color wheel below:

![color_wheel_4_background](C:\Users\student\TIL\Summary\codecademy\image\color_wheel_4_background.svg)

* *Saturation* refers to the intensity or purity of the color. The saturation increases towards 100% as the point gets closer to the edge (the color becomes more rich). The saturation decreases towards 0% as the point gets closer to the center (the color becomes more gray).

* *Lightness* refers to how light or dark the color is. Halfway, or 50%, is normal lightness. Imagine a sliding dimmer on a light switch that starts halfway. Sliding the dimmer up towards 100% makes the color lighter, closer to white. Sliding the dimmer down towards 0% makes the color darker, closer to black.

#### HSL vs RGB

In RGB, making the color a little darker may affect all three color components. In HSL, that's as easy as changing the lightness value. 

### Opacity and Alpha

```css
color: hsla(34, 100%, 50%, 0.1);
```

```css
color: rgba(234, 45, 98, 0.33);
```

The value for half transparent would be `0.5`.  And the blending happens for each pixel; no blurring occurs.

A named color keyword for zero opacity:

```css
color: transparent;
/* equivalent to is rgba(0, 0, 0, 0) */
```

### Summary

- Named colors — there are 147 named colors, which you can review [here](https://msdn.microsoft.com/en-us/library/aa358802(v=vs.85).aspx).
- Hexadecimal or hex colors
  - Hexadecimal is a number system with has sixteen digits, 0 to 9 followed by "A" to "F".
  - Hex values always begin with `#` and specify values of red, blue and green using hexademical numbers such as `#23F41A`.
- RGB
  - RGB colors use the `rgb()`syntax with one value for red, one value for blue and one value for green.
  - RGB values range from 0 to 255 and look like this: `rgb(7, 210, 50)`.
- HSL
  - HSL stands for hue (the color itself), saturation (the intensity of the color), and lightness (how light or dark a color is).
  - Hue ranges from 0 to 360 and saturation and lightness are both represented as percentages like this: `hsl(200, 20%, 50%)`.
- You can add opacity to color in RGB and HSL by adding a fourth value, `a`, which is represented as a percentage.

## Typography

### Font Family

```css
h1 {
  font-family: Garamond;
}
```

1.  Limit the number of typefaces used on a web page to 2 or 3
2.  The name of a typeface consists of more than one word, it must be enclosed in double quotes
3.  A stylesheet must be installed on a user's computer
4.  The default typeface for all most browsers is Times New Roman

```css
h1 {
  font-family: "Courier New";
}
```

### Font Weight

```css
p {
  font-weight: bold;
}
```

```css
p {
  font-weight: normal;
}
```

The `font-weight` property can also be assigned ranging from 100 to 900. And valid values are multiples of 100 within this range such as `200` or `500`.

1. `400` is the default `font-weight`of most text.
2. `700` signifies a bold `font-weight`.
3. `300` signifies a light `font-weight`.

```css
header {
  font-weight: 800;
}

footer {
  font-weight: 200;
}
```

### Font Style

```css
h3 {
  font-style: italic;
}
```

### Word Spacing

The default amount of space between words is usually `0.25em`, increasing of only `.05em`in word spacing.

```css
h1 {
  word-spacing: 0.3em;
}
```

### Letter Spacing

```css
h1 {
  letter-spacing: 0.3em;
}
```

### Text Transformation

```css
h1 {
  text-transform: uppercase;
}
```

```css
h1 {
  text-transform: lowercase;
}
```

### Text Alignment

```css
h1 {
  text-align: right;
}
```

1. `left` - aligns text to the left hand side of the browser.
2. `center` - centers text.
3. `right` - aligns text to the right hand side of the browser.