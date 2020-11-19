# Instructions

You're almost done with the lesson! There are just a couple more steps. In this exercise, you'll finish building the World Bank web app.

This exercise is inside the *4_flask+plotly+pandas_exercise* folder.  

First, make sure plotly is installed in your workspace. Open a terminal and run `pip install plotly`.

Then, in the terminal, go into the *3_flask+plotly+pandas_exercise* directory with
`cd 4_flask+plotly+pandas_exercise`. You need to do this step in order to run the app properly.

In this exercise, you'll add a fifth visualization to the web app. You'll need to do two things:
1. wrangle the data and set up the visualization on the back end. You'll do this in the *wrangle_data.py* file following along the TODO sections.
2. add an extra div in the *index.html* file where you want the visualization to show up. There will be a TODO section in the index.html file as well.

Remember to see the dashboard, you'll need to start the web app typing `python worldbank.py` in the terminal.

Then you need to find the workspace environmental variables with `env | grep WORK`, and you can open a new browser window and go to the address:
`http://WORKSPACESPACEID-3001.WORKSPACEDOMAIN` replacing WORKSPACEID and WORKSPACEDOMAIN with your values.

You'll find a solution in the solutions folder. It's in the *solutions/4_flask_exercise* folder.


## Beyond a CSV file

Besides storing data in a local csv file (or text, json, etc.), you could also store the data in a database such as a SQL database.

The database could be local to your website meaning that the database file is stored on the same server as your website; alternatively, the database could be stored somewhere else like on a separate database server or with a cloud service like Amazon AWS.

Using a database with your web app goes beyond the scope of this introduction to web development, here are a few resources for using databases with Flask apps:
- [Tutorial - Using Databases with Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database).
- [SQL Alchemy](http://docs.sqlalchemy.org/en/latest/) - a Python toolkit for working with SQL.
- [Flask SQLAlchemy](http://docs.sqlalchemy.org/en/latest/) - a Flask library for using SQLAlchemy with Flask. 
