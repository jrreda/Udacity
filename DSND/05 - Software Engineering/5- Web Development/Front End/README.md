# The Front-End

1. HTML
2. CSS
3. JavaScript



## HTML - Hypertext Markup Language

Explanation of the most popular HTML tags:  

* **`<head>`** tag is mostly for housekeeping like specifying the page title and adding meta tags.  
Meta tags are in essence information about the page that web crawlers see but users do not. The head tag also contains links to javascript and css files.  

* **`<body>`** tag can contain headers, paragraphs, images, links, forms, lists, and a handful of other tags. contain the website content.  

* **Full List of Tags and How to Use Them:**  
1. This is a link to one of the best references for html. Use [W3Schools](https://www.w3schools.com/tags/default.asp) website to look up html tags and how to use them.  
2. In fact, the [W3Schools website](https://www.w3schools.com/) has a lot of free information about web development syntax.  


### Checking your HTML

It's a good idea to check the validity of your HTML. Here is a website that checks your HTML for syntax errors: **[W3C Validator](https://validator.w3.org/#validate_by_input)**. Try pasting your HTML code here and running the validator. You can read through the error messages and fix your HTML.


### Div and Span

- You can use `<div>` elements to split off large chunks of html into sections.  
- `<span>` elements, on the other hand, are for small chunks of html. You generally use `<span>` elements in the middle of a piece of text in order to apply a specific style to that text.

Example:  
```HTML
<div>
   <p>This is an example of when to use a div elements versus a span element. A span element goes around <span>a small chunk of html</span></p>
</div>
```

---
## CSS - cascading style sheets

To build the data dashboard at the end of this lesson, you won't need to actually write any CSS. Instead, you'll use libraries that take care of the CSS for you. In this that, that would be the **[Bootstrap library](https://getbootstrap.com/)**.  

But if you are interested in understanding what Bootstrap is doing under the hood, then you need to understand how to style a website with CSS. This page has a summary of some important aspects of CSS programming.


### What is the Purpose of CSS?

In most professional websites, css is kept in a separate stylesheet. This makes it easier to separate content (html) from style (css). Code becomes easier to read and maintain.  
If you're interested in the history of css and how it came about, here is an interesting link: [history of css](https://www.w3.org/Style/CSS20/history.html).  
CSS stands for cascading style sheets. The "cascading" refers to how rules trickle down to the various layers of an html tree. For example, you might specify that all paragraphs have the same font type. But then you want to override one of the paragraphs to have a different font type. How does a browser decide which rules apply when there is a conflict? That's based on the cascade over. You can read more about that [here](https://www.lifewire.com/what-does-cascade-mean-3466872).


### Different ways to write CSS

As discussed in the video, there are essentially two ways to write CSS: **inline** or with a **stylesheet**.  
**Inline** means that you specify the CSS directly inside of an html tag like so:  
```html
<p style="font-size:20px;">This is a paragraph</p>
```


Alternatively, you can put the CSS in a **stylesheet**. The stylesheet can go underneath an html head tag like so:  
```html
<head>
   <style>
       p {font-size: 20px;}
   </style>
</head>
```

Or the css can go into its own separate css file (extension .css). Then you can link to the css file within the html head tag like so:  
```html
<head>
    <link rel="stylesheet" type"text/css" href="style.css">
</head>
```  
where `style.css` is the path to the style.css file. Inside the style.css file would be the style rules such as:  
```css
p {
  color:red;
}
```


### CSS Rules and Syntax

CSS is essentially a set of rules that you can use to stylize html. The [W3 Schools CSS Website](https://www.w3schools.com/css/default.asp) is a good place to find all the different rules you can use. These including styling text, links, margins, padding, image, icons and background colors among other options.  

The general syntax is that you:  
1. select the html element, id, and/or class of interest.  
2. specify what you want to change about the element.  
3. specify a value, followed by a semi-colon.  


**For example:**  
```CSS
a {
  text-decoration: none;
  color: blue;
  font-weight: bold;
}
```
where `a` is the element of interest, `text-decoration` is what you want to change, and `none` is the value.  


To select by **class** name, you use a dot like so:
```CSS
.class_name {
   color: red;
}
```

To select by **id** name, you use the pound sign:
```CSS
#id_name {
  color: red;
}
```


You can make more complex selections as well like "select paragraphs inside the `div` with `id="div_top"` . If your html looks like this:
```HTML
<div id="div_top">
   <p>This is a paragraph</p>
</div>
```  
then the CSS would be like this:  
```CSS
div#div_top p {
  color: red;
}
```

---
## Javascript

To build the data dashboard at the end of this lesson, you won't need to write any JavaScript at all. That's because you'll use libraries ([Bootstrap](https://getbootstrap.com/) and [Plotly](https://plot.ly/)) that take care of the JavaScript for you.

You won't need to get into the details of JavaScript syntax, but it's good to have at least an idea of what is happening under the hood.


### What is JavaScript?

* JavaScript is a high level language like Python, PHP, Ruby, and C++. It was specifically developed to make the front-end of a web application more dynamic; however, you can also use javascript to program the back-end of a website with the JavaScript runtime environment [node](https://nodejs.org/en/).  
* Java and javaScript are two completely different languages that happen to have similar names.
* JavaScript syntax, especially for front-end web development, is a bit tricky. It's much easier to write front-end JavaScript code using a framework such as [jQuery](http://api.jquery.com/).


### Basic JavaScript Syntax

Here are a few rules to keep in mind when writing JavaScript:

* a line of code ends with a semi-colon `;`.
* `()` parenthesis are used when calling a function much like in Python.
* `{}` curly braces surround large chunks of code or are used when initializing dictionaries.
* `[]` square brackets are used for accessing values from arrays or dictionaries much like in Python.

Here is an example of a JavaScript function that sums the elements of an array:
```js
function addValues(x) {
  var sum_array = 0;
  for (var i=0; i < x.length; i++) {   
    sum_array += x[i];
  }
  return sum_array;
}

addValues([3,4,5,6]);
```


### What is jQuery?

* Jquery is a JavaScript library that makes developing the front-end easier. JavaScript specifically helps with manipulating html elements. The reason we are showing you Jquery is because the Bootstrap library you'll be using depends on Jquery. But you won't need to write any Jquery yourself.  
* Here is a link to the documentation of the core functions in jquery: [jQuery API documentation](https://api.jquery.com/).  
* Jquery came out in 2006. There are newer JavaScript tools out there like [React](https://reactjs.org/) and [Angular](https://angularjs.org/).  

As a data scientist, you probably won't need to use any of these tools. But if you work in a startup environment, you'll most likely hear front-end engineers talking about these tools.


### jQuery Syntax

The jQuery library simplifies JavaScript quite a bit. Compare the syntax. Compare these two examples for changing the `h1 title` element when clicking on the image.  

This is pure **JavaScript** code for changing the words in the `h1 title` element.  
```js
function headFunction() {
    document.getElementsByTagName("h1")[0].innerHTML =
          "A Photo of a Breathtaking View";
}
```  

This code searches the html document for all `h1` tags, grabs the first `h1` tag in the array of `h1` tags, and then changes the html. Note that the above code is only the function. You'd also have to add an `onClick` action in the image html tag like so:
```HTML
<img src="image.jpg" onclick="headFunction()">
```  


The **jQuery** code is more intuitive. Once the document has loaded, the following code adds an `onclick` event to the image. Once the image is clicked, the `h1` tag's text is changed.
```JS
$(document).ready(function() {
    $("img").click(function() {
        $("h1").text("A Photo of a Breathtaking View");
    });
});
```  
The dollar sign `$` is jQuery syntax that says "grab this element, class or id". That part of the syntax should remind you somewhat of CSS. For example `$("p#first")` means find the paragraph with id="first". Or `$("#first")` would work as well.



**Javascript** has something called callback function, which can make learning javascript a bit tricky. Callback functions are essentially functions that can be inputs into other functions. In the above code, there is the `ready()` function that waits for the html document to load. Then there is another function being passed into the ready function. This section function adds an on-click event to an image tag. Then there's another function passed into the `click()` function, which changes the `h1` text.
