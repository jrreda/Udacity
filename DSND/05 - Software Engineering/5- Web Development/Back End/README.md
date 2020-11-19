# The Back-End

In this lesson, you'll build a backend using **Flask**. Because Flask is written in Python, you can use any Python library in your backend including pandas and scikit-learn.  

In this part of the lesson, you'll practice:
1. setting up the backend.
2. linking the backend and the frontend together.
3. deploying the app to a server so that the app is available from a web address.



## What is Flask?

- **[Flask](http://flask.pocoo.org/)** is a web framework takes care of all the routing needed to organize a web page so that you don't have to write the code yourself!
- When you type "http://www.udacity.com" into a browser, your computer sends out a request to another computer (ie the server) where the Udacity website is stored. Then the Udacity server sends you the files needed to render the website in your browser. The Udacity computer is called a server because it "serves" you the files that you requested.
- The HTTP part of the web address stands for Hypter-text Transfer Protocol. HTTP defines a standard way of sending and receiving messages over the internet.
- When you hit enter in your browser, your computer says "get me the files for the web page at www.udacity.com": except that message is sent to the server with the syntax governed by HTTP. Then the server sends out the files via the protocol as well.
- There needs to be some software on the server that can interpret these HTTP requests and send out the correct files. That's where a web framework like Flask comes into play. A framework abstracts the code for receiving requests as well as interpreting the requests and sending out the correct files.


### Why Flask?

* First and foremost, you'll be working with Flask because it is written in Python. You won't need to learn a new programming language.
* Flask is also a relatively simple framework, so it's good for making a small web app.
* Because Flask is written in Python, you can use Flask with any other Python library including pandas, numpy and scikit-learn. In this lesson, you'll be deploying a data dashboard and pandas will help get the data ready.
