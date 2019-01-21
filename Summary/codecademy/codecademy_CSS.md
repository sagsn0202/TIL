# CSS

## CSS Selectors

- CSS can change the look of HTML elements. In order to do this, CSS must select HTML elements, then apply styles to them.
- CSS can select HTML elements by tag, class, or ID.
- Multiple CSS classes can be applied to one HTML element.
- Classes can be reusable, while IDs can only be used once.
- IDs are more specific than classes, and classes are more specific than tags. That means IDs will override any styles from a class, and classes will override any styles from a tag selector.
- Multiple selectors can be chained together to select an element. This raises the specificity, but can be necessary.
- Nested elements can be selected by separating selectors with a space.
- The `!important` flag will override any style, however it should almost never be used, as it is extremely difficult to override.
- Multiple unrelated selectors can receive the same styles by separating the selector names with commas.

## Visual Rules

- CSS declarations are structured into property and value pairs.
- The `font-family` property defines the typeface of an element.
- `font-size` controls the size of text displayed.
- `font-weight` defines how thin or thick text is displayed.
- The `text-align` property places text in the left, right, or center of its parent container.
- Text can have two different color attributes: `color` and `background-color`. `color` defines the color of the text, while `background-color`defines the color behind the text.
- CSS can make an element transparent with the `opacity` property.
- CSS can also set the background of an element to an image with the `background-image` property.

## Box Model

1. Width and height — specifies the width and height of the content area.
2. Padding — specifies the amount of space between the content area and the border.
3. Border — specifies the thickness and style of the border surrounding the content area and padding.
4. Margin — specifies the amount of space between the border and the outside edge of the element.

![diagram-boxmodel](C:\Users\복지실\Desktop\diagram-boxmodel.svg)

![diagram-verticalmargins](C:\Users\복지실\Desktop\diagram-verticalmargins.svg)

1. The box model comprises a set of properties used to create space around and between HTML elements.
2. The height and width of a content area can be set in pixels or percentage.
3. Borders surround the content area and padding of an element. The color, style, and thickness of a border can be set with CSS properties.
4. Padding is the space between the content area and the border. It can be set in pixels or percent.
5. Margin is the amount of spacing outside of an element's border.
6. Horizontal margins add, so the total space between the borders of adjacent elements is equal to the sum of the right margin of one element and the left margin of the adjacent element.
7. Vertical margins collapse, so the space between vertically adjacent elements is equal to the larger margin.
8. `margin: 0 auto` horizontally centers an element inside of its parent content area, if it has a width.
9. The `overflow` property can be set to `display`, `hide`, or `scroll`, and dictates how HTML will render content that overflows its parent's content area.
10. The `visibility` property can hide or show elements.

## Box Model + a

![htmlcss1-diagram__contentbox](C:\Users\복지실\Desktop\htmlcss1-diagram__contentbox.svg)

![htmlcss1-diagram__borderbox](C:\Users\복지실\Desktop\htmlcss1-diagram__borderbox.svg)

1. In the default box model, box dimensions are affected by border thickness and padding.
2. The `box-sizing` property controls the box model used by the browser.
3. The default value of the `box-sizing` property is `content-box`.
4. The value for the new box model is `border-box`.
5. The `border-box` model is not affected by border thickness or padding.

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

### Line Height

Line heights can take one of several values:

1. A unitless number, such as `1.2`. The unitless ratio value is the *preferred method*,  if we change the font size, a unitless line-height would automatically readjust.
2. A number specified by unit, for instance  `12px`, such as pixels, percents, ems, or rems.

```css
p {
  line-height: 1.4;
}
```

### Serif and Sans Serif

1. Serif — fonts that have extra details on the ends of each letter, like Times New Roman or Georgia, among others.
2. Sans-Serif — fonts that have straight, flat edges, like Arial or Helvetica.
3. Monospace — fonts with the same width

### Fallback Fonts

If the stylesheet specifies a font which is not installed on a user's computer, pre-installed fonts serve as *fallback fonts*

```css
h1 {
  font-family: "Garamond", "Times", serif;
}
```

Garamond font for all `<h1>` elements -> If Garamond is not available, use the Times font -> If Garamond and Times are not available, use any serif font pre-installed on the user's computer.

The fonts specified after Garamond are the fallback fonts (`Times`, `serif`). 

### Linking Fonts

[Google Fonts](https://fonts.google.com/) is one such directory of thousands of open-source fonts, available for free use.

Add the font to *the `<head>` section of the HTML document*, using the `<link>` tag and the `href`.

1. A single linked font, using `Droid Serif` as an example:

```html
<head>
  <link href="https://fonts.googleapis.com/css?family=Droid+Serif" type="text/css" rel="stylesheet">
</head>
```

1. Multiple linked fonts, using the `Droid Serif` and `Playfair Display`fonts as an example:

```html
<head>
  <link href="https://fonts.googleapis.com/css?family=Droid+Serif|Playfair+Display" type="text/css" rel="stylesheet">
</head>
```

1. Multiple linked fonts, along with weights and styles. Here `Droid Serif`has font weights of `400`, `700`, and `700i`, while `Playfair Display` has font weights of `400`, `700`, and `900i`:

```html
<head>
  <link href="https://fonts.googleapis.com/css?family=Droid+Serif:400,700,700i|Playfair+Display:400,700,900i" rel="stylesheet">
</head>
```

### Font-Face

 `@font-face`: import fonts directly into stylesheets**(CSS)**

1. focus on the rules that are directly labeled as `/* latin */`
2. Copy each of the CSS rules labeled latin, and paste the rules to the top of **style.css**.

Ex) Direct link: https://fonts.googleapis.com/css?family=Space+Mono:400,700/

#### from External Service

```css
@font-face {
  font-family: "Roboto";
  src: url(fonts/Roboto.woff2) format('woff2'),
       url(fonts/Roboto.woff) format('woff'),
       url(fonts/Roboto.tff) format('truetype');
}
```

1. use of a relative filepath instead of a web URL
2. add a format for each file to specify which font to use, so providing multiple font file options will support more browsers

- Free Fonts: https://www.fontsquirrel.com/

### Summary

- *Typography* is the art of arranging text on a page.
- Text can appear in any number of weights, with the `font-weight` property.
- Text can appear in italics with the `font-style`property.
- The vertical spacing between lines of text can be modified with the `line-height` property.
- *Serif* fonts have extra details on the ends of each letter. *Sans-Serif* fonts do not.
- *Fallback fonts* are used when a certain font is not installed on a user's computer.
- Google Fonts provides free fonts that can be used in an HTML file with the `<link>` tag or the `@font-face` property.
- Local fonts can be added to a document with the `@font-face` property and the path to the font's source.
- The `word-spacing`property changes how far apart individual words are.
- The `letter-spacing`property changes how far apart individual letters are.
- The `text-align` property changes the horizontal alignment of text.

## Grid

Three possible ways to approach layout: the box model, Flexbox, and CSS display

Whereas Flexbox is mostly useful for positioning items in a one-dimensional layout, CSS grid is most useful for two-dimensional layouts.

properties to create grid layouts:

- `grid-template-columns`
- `grid-template-rows`
- `grid-template`
- `grid-template-area`
- `grid-gap`
- `grid-row-start` / `grid-row-end`
- `grid-column-start` / `grid-column-end`
- `grid-area`

### Creating a Grid

1. To set up a grid, you need to have both a *grid container* and *grid items*.
2. To turn an HTML element into a grid container, you must set the element's `display` property to `grid` (for a block-level grid) or `inline-grid` (for an inline grid). 

### Creating Columns

```css
.grid {
  display: grid;
  width: 500px;
  grid-template-columns: 100px 200px;
}
```

```css
.grid {
  display: grid;
  width: 1000px;
  grid-template-columns: 20% 50%;
}
```

```css
.grid {
  display: grid;
  width: 100px;
  grid-template-columns: 20px 40% 60px;
}
```

The total width of our columns (120 pixels) exceeds the width of the grid (100 pixels). This might make our grid cover other elements on the page!

### Creating Rows

```css
.grid {
  display: grid;
  width: 1000px;
  height: 500px;
  grid-template-columns: 100px 200px;
  grid-template-rows: 10% 20% 600px;
}
```

### Grid Template

```css
.grid {
  display: grid;
  width: 1000px;
  height: 500px;
  grid-template: 200px 300px / 20% 10% 70%;
}
```

The values before the slash determine the size of each row. 

The values after the slash determine the size of each column.

### Fraction

Using `fr` makes it easier to prevent grid items from overflowing the boundaries of the grid.

(Responsive units: percentages (`%`), `em`s and `rem`s)

```css
.grid {
  display: grid;
  width: 1000px;
  height: 400px;
  grid-template: 2fr 1fr 1fr / 1fr 3fr 1fr;
}
```

```css
.grid {
  display: grid;
  width: 100px;
  grid-template-columns: 1fr 60px 1fr;
}
```

60 pixels are taken up by the second column. The first and third columns have 40 available to split between them.

### Repeat

```css
.grid {
  display: grid;
  width: 300px;
  grid-template-columns: repeat(3, 100px);
}
```

```css
 repeat(5, 1fr)
```

 Split table into five equal rows or columns.

```css
grid-template-columns: repeat(2, 20px 50px)
```

The first and third columns will be 20 pixels wide and the second and fourth will be 50 pixels wide.

### MinMax

```css
.grid {
  display: grid;
  grid-template-columns: 100px minmax(100px, 500px) 100px;
}
```

### Grip Gap

`grid-row-gap` and `grid-column-gap`

```css
.grid {
  display: grid;
  width: 320px;
  grid-template-columns: repeat(3, 1fr);
  grid-column-gap: 10px;
}
```

`grid-gap: 20px 10px;` set the distance between rows to 20 pixels and the distance between columns to 10 pixels. This shorthand does not take a `/` between values!

### Grid Items

![css_grid_diagram_2](C:\Users\student\TIL\Summary\codecademy\image\css_grid_diagram_2.svg)

#### Grid Row

```css
.item {
  grid-row-start: 1;
  grid-row-end: 3;
}
```

The HTML element of class `item` will take up two rows in the grid, rows 1 and 2.

It is possible for the value of `grid-row-start` to be greater than that of `grid-row-end`. Both properties can also each have negative values. Consult the [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-row-start)to learn more about how to use these features.

```python
.item {
  grid-row: 1 / 3;
}
```

It will also include the `grid-gap` if any exists. If an item spans two rows of height 100 pixels and there is a ten-pixel grid-gap, then the item will have a total height of 210 pixels.

#### Grid Column

```css
.item {
  grid-column: 4 / span 2;
}
```

```css
.item {
  grid-column: 4 / 6;
}
```

```css
.item {
  grid-column-start: 4;
  grid-column-end: span 2;
}
```

```css
.item {
  grid-column-start: span 2;
  grid-column-end: 6;
}
```

#### Grid Area

```css
.item {
  grid-area: 2 / 3 / 4 / span 5;
}
```

1. `grid-row-start`
2. `grid-column-start`
3. `grid-row-end`
4. `grid-column-end`

### Summary

- `grid-template-columns` defines the number and sizes of the columns of the grid
- `grid-template-rows` defines the number and sizes of the rows of the grid
- `grid-template` is a shorthand for defining both `grid-template-columns`and `grid-template-rows` in one line
- `grid-gap` puts blank space between rows and/or columns of the grid
- `grid-row-start` and `grid-row-end`makes elements span certain rows of the grid
- `grid-column-start` and `grid-column-end` makes elements span certain columns of the grid
- `grid-area` is a shorthand for `grid-row-start`, `grid-column-start`, `grid-row-end`, and `grid-column-end`, all in one line

## Grid II

- `grid-template-areas`
- `justify-items`
- `justify-content`
- `justify-self`
- `align-items`
- `align-content`
- `align-self`
- `grid-auto-rows`
- `grid-auto-columns`
- `grid-auto-flow`

### Grid Template Areas

`grid-template-areas`: name sections as values in the `grid-row-start`, `grid-row-end`, `grid-col-start`, `grid-col-end`, and `grid-area`

```html
<div class="container">
  <header>Welcome!</header>
  <nav>Links!</nav>
  <section class="info">Info!</section>
  <section class="services">Services!</section>
  <footer>Contact us!</footer>
</div>
```

```css
.container {
  display: grid;
  max-width: 900px;
  position: relative;
  margin: auto;
  grid-template-areas: "head head"
                       "nav nav" 
                       "info services"
                       "footer footer";
  grid-template-rows: 300px 120px 800px 120px;
  grid-template-columns: 1fr 3fr; 
}

header {
  grid-area: head;
} 

nav {
  grid-area: nav;
} 

.info {
  grid-area: info;
} 

.services {
  grid-area: services;
}

footer {
  grid-area: footer;
}
```

#### Overlapping

```html
<div class="container">
  <div class="info">Info!</div> 
  <img src="#" />
  <div class="services">Services!</div>
</div>
```

```css
.container {
  display: grid;
  grid-template: repeat(8, 200px) / repeat(6, 100px);
}

.info {
  grid-area: 1 / 1 / 9 / 4;
}

.services {
  grid-area: 1 / 4 / 9 / 7;
}

img {
  grid-area: 2 / 3 / 5 / 5;
  z-index: 5;
}
```

The z-index property renders the image element on top of the `services` and `info` sections.

### Justify-items

how to position grid items from left to right

- `start` — aligns grid items to the left side of the grid area
- `end` — aligns grid items to the right side of the grid area
- `center` — aligns grid items to the center of the grid area
- `stretch` — stretches all items to fill the grid area

There are several other values on the [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Box_Alignment_in_CSS_Grid_Layout#Justifying_Items_on_the_Inline_or_Row_Axis). The definitions can be found in the [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-items#Values). It is important the definitions including some values are not accepted in CSS Grid layout.

```html
<main>
  <div class="card">Card 1</div>
  <div class="card">Card 2</div>
  <div class="card">Card 3</div>
</main>
```

```css
main {
  display: grid;
  grid-template-columns: repeat(3, 400px);
  justify-items: center;
}
```

### Justify Content

how to position a grid within its parent element

`justify-content`

- `start` — aligns the grid to the left side of the grid container
- `end` — aligns the grid to the right side of the grid container
- `center` — centers the grid horizontally in the grid container
- `stretch` — stretches the grid items to increase the size of the grid to expand horizontally across the container
- `space-around` — includes an equal amount of space on each side of a grid element, resulting in double the amount of space between elements as there is before the first and after the last element
- `space-between` — includes an equal amount of space between grid items and no space at either end
- `space-evenly` — places an even amount of space between grid items and at either end

There are several other values on the [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Box_Alignment_in_CSS_Grid_Layout#Justifying_Items_on_the_Inline_or_Row_Axis). The definitions can be found in the [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-items#Values). It is important the definitions including some values are not accepted in CSS Grid layout.

```html
<main>
  <div class="left">Left</div>
  <div class="right">Right</div>
</main>
```

```css
main {
  display: grid;
  width: 1000px;
  grid-template-columns: 300px 300px;
  grid-template-areas: "left right"; 
  justify-content: center;
}
```

`justify-content: center;` positions the columns in the center of the grid, leaving 200 pixels on the right and 200 pixels on the left of the grid.

**`justify-content` and `justify-self` align along the row axis.**

### Align Items

how to position grid items from top to bottom

`align-items`

- `start` — aligns grid items to the top side of the grid area
- `end` — aligns grid items to the bottom side of the grid area
- `center` — aligns grid items to the center of the grid area
- `stretch` — stretches all items to fill the grid area

There are several other values on the [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Box_Alignment_in_CSS_Grid_Layout#Justifying_Items_on_the_Inline_or_Row_Axis). The definitions can be found in the [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-items#Values). It is important the definitions including some values are not accepted in CSS Grid layout.

```html
<main>
  <div class="card">Card 1</div>
  <div class="card">Card 2</div>
  <div class="card">Card 3</div>
</main>
```

```css
main {
  display: grid;
  grid-template-rows: repeat(3, 400px);
  align-items: center;
}
```

### Align Content

 `align-content` positions the rows along the column axis, or from top to bottom

- `start` — aligns the grid to the top of the grid container
- `end` — aligns the grid to the bottom of the grid container
- `center` — centers the grid vertically in the grid container
- `stretch` — stretches the grid items to increase the size of the grid to expand vertically across the container
- `space-around` — includes an equal amount of space on each side of a grid element, resulting in double the amount of space between elements as there is before the first and after the last element
- `space-between` — includes an equal amount of space between grid items and no space at either end
- `space-evenly` — places an even amount of space between grid items and at either end

There are several other values on the [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Box_Alignment_in_CSS_Grid_Layout#Justifying_Items_on_the_Inline_or_Row_Axis). The definitions can be found in the [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-items#Values). It is important the definitions including some values are not accepted in CSS Grid layout.

```html
<main>
  <div class="top">Top</div>
  <div class="bottom">Bottom</div>
</main>
```

```css
main {
  display: grid;
  height: 600px;
  rows: 200px 200px;
  grid-template-areas: "top"
                       "bottom"; 
  align-content: center;
}
```

**`align-content` and `align-self` align along the column axis**

### Justify Self and Align Self

`justify-self` / `align-self` specifies how an individual element should position itself with respect to the row / column axis. This property will override `justify-items` / `align-items` for any item on which it is declared.

- `start` — positions grid items on the left side/top of the grid area
- `end` — positions grid items on the right side/bottom of the grid area
- `center` — positions grid items on the center of the grid area
- `stretch` — positions grid items to fill the grid area (default)

There are several other values on the [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Box_Alignment_in_CSS_Grid_Layout#Justifying_Items_on_the_Inline_or_Row_Axis). The definitions can be found in the [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-items#Values). It is important the definitions including some values are not accepted in CSS Grid layout.

### Implicit vs Explicit Grid

The implicit grid is an algorithm built into the specification for CSS Grid.

The default behavior of the implicit grid is as follows: items fill up rows first, adding new rows as necessary. New grid rows will only be tall enough to contain the content within them.

### Grid Auto Rows and Grid Auto Columns

implicit `grid-auto-rows` and `grid-auto-columns`accept the same values as their explicit counterparts, `grid-template-rows` and `grid-template-columns`:

- pixels (`px`)
- percentages (`%`)
- fractions (`fr`)
- the `repeat()` function

```html
<body>
  <div>Part 1</div>   
  <div>Part 2</div>
  <div>Part 3</div>
  <div>Part 4</div>
  <div>Part 5</div>
</body>
```

```css
body {
  display: grid;
  grid: repeat(2, 100px) / repeat(2, 150px); 
  grid-auto-rows: 50px;
}
```

The fifth `<div>` will be added to an implicit row that will be 50 pixels tall.

If we did not specify `grid-auto-rows`, the rows would be auto-adjusted to the height of the content of the grid items.

### Grid Auto Flow

specify the order in which they are rendered.

- `row` — specifies the new elements should fill rows from left to right and create new rows when there are too many elements (default)
- `column` — specifies the new elements should fill columns from top to bottom and create new columns when there are too many elements
- `dense` — this keyword invokes an algorithm that attempts to fill holes earlier in the grid layout if smaller elements are added

can pair `row` and `column` with `dense`, like `grid-auto-flow: row dense;`

### Summary

- `grid-template-areas` specifies grid named grid areas
- grid layouts are two-dimensional: they have a row, or inline, axis and a column, or block, axis.
- `justify-items` specifies how individual elements should spread across the row axis
- `justify-content` specifies how groups of elements should spread across the row axis
- `justify-self` specifies how a single element should position itself with respect to the row axis
- `align-items` specifies how individual elements should spread across the column axis
- `align-content` specifies how groups of elements should spread across the column axis
- `align-self` specifies how a single element should position itself with respect to the column axis
- `grid-auto-rows` specifies the height of rows added implicitly to the grid
- `grid-auto-columns` specifies the width of columns added implicitly to the grid
- `grid-auto-flow` specifies in which direction implicit elements should be created

### FlexBox

#### justify-content

- `flex-start`: 요소들을 컨테이너의 왼쪽으로 정렬합니다.
- `flex-end`: 요소들을 컨테이너의 오른쪽으로 정렬합니다.
- `center`: 요소들을 컨테이너의 가운데로 정렬합니다.
- `space-between`: 요소들 사이에 동일한 간격을 둡니다.
- `space-around`: 요소들 주위에 동일한 간격을 둡니다.

#### align-items

- `flex-start`: 요소들을 컨테이너의 꼭대기로 정렬합니다.
- `flex-end`: 요소들을 컨테이너의 바닥으로 정렬합니다.
- `center`: 요소들을 컨테이너의 세로선 상의 가운데로 정렬합니다.
- `baseline`: 요소들을 컨테이너의 시작 위치에 정렬합니다.
- `stretch`: 요소들을 컨테이너에 맞도록 늘립니다.

#### flex-direction

- `row`: 요소들을 텍스트의 방향과 동일하게 정렬합니다.
- `row-reverse`: 요소들을 텍스트의 반대 방향으로 정렬합니다.
- `column`: 요소들을 위에서 아래로 정렬합니다.
- `column-reverse`: 요소들을 아래에서 위로 정렬합니다.

#### etc

* `order`:  `order` 속성을 각 요소에 적용, order의 기본 값은 0이며, 양수나 음수로 수정

* `align-self`는 개별 요소에 적용할 수 있는 또 다른 속성

#### flex-wrap

- `nowrap`: 모든 요소들을 한 줄에 정렬합니다.
- `wrap`: 요소들을 여러 줄에 걸쳐 정렬합니다.
- `wrap-reverse`: 요소들을 여러 줄에 걸쳐 반대로 정렬합니다.

#### flex-flow

* `flex-direction`과 `flex-wrap`이 자주 같이 사용되기 때문에, `flex-flow`가 이를 대신

* `flex-flow: row wrap`

#### align-content

- `flex-start`: 여러 줄들을 컨테이너의 꼭대기에 정렬합니다.
- `flex-end`: 여러 줄들을 컨테이너의 바닥에 정렬합니다.
- `center`: 여러 줄들을 세로선 상의 가운데에 정렬합니다.
- `space-between`: 여러 줄들 사이에 동일한 간격을 둡니다.
- `space-around`: 여러 줄들 주위에 동일한 간격을 둡니다.
- `stretch`: 여러 줄들을 컨테이너에 맞도록 늘립니다.