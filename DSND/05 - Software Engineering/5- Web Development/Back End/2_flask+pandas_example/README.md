# Instructions

The *2_flask+pandas_example* folder contains the files from the screencast. There's nothing to do here other than to see that you can use pandas and flask together.   

If you run the web app, you'll find that it still works. To run the web app:  
1. In the terminal, type `cd 2_flask+pandas_example`.
2. Then `python worldbank.py`.
3. The data variable will print out to the terminal.
4. You can open the web app in the browser as well. You can do this using the `env | grep WORK` command in the terminal to see your WORKSPACE envirnomental variables. And from there the web address is `http://WORKSPACESPACEID-3001.WORKSPACEDOMAIN` replacing WORKSPACEID and WORKSPACEDOMAIN with your values.


## Screencast

In the screencast, the data set was sent from the back end to the front end. This was accomplished by including a variable in the `render_template()` function like so:

```python
data = data_wrangling()

@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html', data_set = data)
```

What this code does is to first load the data using the `data_wrangling` function from *wrangling.py*. This data gets stored in a variable called data.

In `render_template`, that data is sent to the front end via a variable called `data_set`. Now the data is available to the front_end in the `data_set` variable.

In the *index.html* file, you can access the `data_set` variable using the following syntax:
```html
{{ data_set }}
```

You can do this because Flask comes with a template engine called **[Jinja](http://jinja.pocoo.org/)**. Jinja also allows you to put control flow statements in your html using the following syntax:  
```HTML
{% for tuple in data_set %}
  <p>{{tuple}}</p>
{% end_for %}
```


The logic is:
1. Wrangle data in a file (aka *Python module*). In this case, the file is called *wrangling.py*. The *wrangling.py* has a function that returns the clean data.
2. Execute this function in routes.py to get the data in *routes.py*.
3. Pass the data to the front-end (*index.html* file) using the `render_template` method.
4. Inside of *index.html*, you can access the data variable with the squiggly bracket syntax `{{ }}`.


The next step will be to use this wrangled data in a Plotly visualization. You can do this in the back-end of the web app with Plotly's Python library and Python dictionaries. And then finally, you'll need to send these dictionaries containing the visualizations to the front-end of the web app.
