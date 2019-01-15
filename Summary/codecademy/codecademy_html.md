# HTML

1. The `<!DOCTYPE html>`declaration should always be the first line of code in your HTML files. This lets the browser know what version of HTML to expect.
2. The `<html>` element will contain all of your HTML code.
3. Information about the web page, like the title, belongs within the `<head>` of the page.
4. You can add a title to your web page by using the `<title>` element, inside of the head.
5. A webpage's title appears in a browser's tab.
6. Anchor tags (`<a>`) are used to link to internal pages, external pages or content on the same page.
7. You can create sections on a webpage and jump to them using `<a>` tags and adding `id`s to the elements you wish to jump to.
8. Whitespace between HTML elements helps make code easier to read while not changing how elements appear in the browser.
9. Indentation also helps make code easier to read. It makes parent-child relationships visible.
10. Comments are written in HTML using the following syntax: `<!-- comment -->`.



1. The `<table>` element creates a table.
2. The `<tr>` element adds rows to a table.
3. To add data to a row, you can use the `<td>` element.
4. Table headings clarify the meaning of data. Headings are added with the `<th>` element.
5. Table data can span columns using the `colspan` attribute.
6. Table data can span rows using the `rowspan` attribute.
7. Tables can be split into three main sections: a head, a body, and a footer.
8. A table's head is created with the `<thead>` element.
9. A table's body is created with the `<tbody>` element.
10. A table's footer is created with the `<tfoot>` element.
11. All the CSS properties you learned about in this course can be applied to tables and their data.



## Forms

```html
<form action="/example.html" method="POST">
  <h1>Creating a form</h1>
  <p>Looks like you want to learn how to create an HTML form. Well, the best way to learn is to play around with it.</p>
  <input type="text" name="first-text-field" value="already pre-filled">
</form>
```

### Label

To associate a `<label>` and an `<input>`, the `<input>` needs an `id` attribute. We then assign the `for` attribute of the `<label>` element with the value of the `id` attribute of `<input>`.

```html
<form action="/example.html" method="POST">
  <label for="meal">What do you want to eat?</label>
  <br>
  <input type="text" name="food" id="meal">
</form>
```

### Password

```html
<form>
  <label for="user-password">Password: </label>
  <input type="password" id="user-password" name="user-password">
</form>
```

### Number

```html
<form>
  <label for="years"> Years of experience: </label>
  <input id="years" name="years" type="number" step="1">
</form>
```

### Range

```html
<form>
  <label for="volume"> Volume Control</label>
  <input id="volume" name="volume" type="range" min="0" max="100" step="1">
</form>
```

### Checkbox

```html
<form>
  <p>Choose your pizza toppings:</p>
  <label for="cheese">Extra cheese</label>
  <input id="cheese" name="topping" type="checkbox" value="cheese">
  <br>
  <label for="pepperoni">Pepperoni</label>
  <input id="pepperoni" name="topping" type="checkbox" value="pepperoni">
  <br>
  <label for="anchovy">Anchovy</label>
  <input id="anchovy" name="topping" type="checkbox" value="anchovy">
</form>
```

- there are assigned values to the `value`attribute of the checkboxes. These values are not visible on the form itself, that's why it is important that we use an associated `<label>` to identify the checkbox.
- each `<input>` has the same value for the `name` attribute. Using the same `name` for each checkbox groups the `<input>`s together. However, each `<input>` has a unique `id` to pair with a `<label>`.

### Radio Button

```html
<form>
  <p>What is sum of 1 + 1?</p>
  <input type="radio" id="two" name="answer" value="2">
  <label for="two">2</label>
  <br>
  <input type="radio" id="eleven" name="answer" value="11">
  <label for="eleven">11</label>
</form>
```

### Dropdown list

```html
<form>
  <label for="lunch">What's for lunch?</label>
  <select id="lunch" name="lunch">
    <option value="pizza">Pizza</option>
    <option value="curry">Curry</option>
    <option value="salad">Salad</option>
    <option value="ramen">Ramen</option>
    <option value="tacos">Tacos</option>
  </select>
</form>
```

### Datalist

```html
<form>
  <label for="city">Ideal city to visit?</label>
  <input type="text" list="cities" id="city" name="city">

  <datalist id="cities">
    <option value="New York City"></option>
    <option value="Tokyo"></option>
    <option value="Barcelona"></option>
    <option value="Mexico City"></option>
    <option value="Melbourne"></option>
    <option value="Other"></option>  
  </datalist>
</form>
```

The `<input>` is associated to the `<datalist>` via the `<input>`'s `list` attribute and the `id` of the `<datalist>`.

### Textarea

```html
<form>
  <label for="blog">New Blog Post: </label>
  <br>
  <textarea id="blog" name="blog" rows="5" cols="30">
    Adding default text
  </textarea>
</form>
```

### Submit Form

```html
<form>
  <input type="submit" value="Send">
</form>
```

### Summary

- The purpose of a `<form>` is to allow users to input information and send it.

- The `<form>`'s `action` attribute determines where the form's information goes.

- The `<form>`'s `method` attribute determines how the information is sent and processed.

- To add fields for users to input information we use the

  `input` element and set the `type` attribute to a field of our choosing:

  - Setting `type` to `"text"` creates a single row field for text input.
  - Setting `type` to `"password"` creates a single row field that censors text input.
  - Setting `type` to `"number"` creates a single row field for number input.
  - Setting `type` to `"range"` creates a slider to select from a range of numbers.
  - Setting `type` to `"checkbox"` creates a single checkbox which can be paired with other checkboxes.
  - Setting `type` to `"radio"` creates a radio button that can be paired with other radio buttons.
  - Setting `type` to `"list"` will pair the `<input>` with a `<datalist>` element.
  - Setting `type` to `"submit"` creates a submit button.

- A `<select>` element is populated with `<option>` elements and renders a dropdown list selection.

- A `<datalist>` element is populated with `<option>` elements and works with an `<input>` to search through choices.

- A `<textarea>` element is a text input field that has a customizable area.

- When a `<form>` is submitted, the `name` of the fields that accept input and the `value` of those fields are sent as `name=value` pairs.

## Form Validation

* One type is server-side validation, this happens when data is sent to another machine (typically a server) for validation.
* On the other hand, we use *client-side validation* if we want to check the data on the browser (the client).

### Requiring an Input

```html
<form action="/example.html" method="POST">
  <label for="allergies">Do you have any dietary restrictions?</label>
  <br>
  <input id="allergies" name="allergies" type="text" required>
  <br>
  <input type="submit" value="Submit">
</form>
```

### Minumum and Maximum

```html
<form action="/example.html" method="POST">
  <label for="guests">Enter # of guests:</label>
  <input id="guests" name="guests" type="number" min="1" max="4">
  <input type="submit" value="Submit">
</form>
```

`<input type="number">` and `<input type="range">`

### Checking Text Length

```html
<form action="/example.html" method="POST">
  <label for="summary">Summarize your fillings in less than 250 characters</label>
  <input id="summary" name="summary" type="text" minlength="5" maxlength="250" required>
  <input type="submit" value="Submit">
</form>
```

### Matching a Pattern

```html
<form action="/example.html" method="POST">
  <label for="payment">Credit Card Number (no spaces):</label>
  <br>
  <input id="payment" name="payment" type="text" required pattern="[0-9]{14,16}">
  <!--[0-9]{14,16} which checks that the user provided only numbers and that they entered at least 14 digits and at most 16 digits. To add this to a form:-->
  <input type="submit" value="Submit">
</form>
```

Regular expressions are a sequence of characters that make up a search pattern. Use the `pattern` attribute and assign it a *regular expression*, or regex. 

### Summary

- Client-side validations happen in the browser before information is sent to a server.
- Adding the `required` attribute to an input related element will validate that the input field has information in it.
- Assigning a value to the `min` attribute of a number input element will validate an acceptable minimum value.
- Assigning a value to the `max` attribute of a number input element will validate an acceptable maximum value.
- Assigning a value to the `minlength` attribute of a text input element will validate an acceptable minimum number of characters.
- Assigning a value to the `maxlength` attribute of a text input element will validate an acceptable maximum number of characters.
- Assigning a regex to `pattern` matches the input to the provided regex.
- If validations on a `<form>` do not pass, the user gets a message explaining why and the `<form>` cannot be submitted.