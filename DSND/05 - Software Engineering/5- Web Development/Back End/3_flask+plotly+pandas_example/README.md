You'll find the code for the web app in the *3_flask+plotly+pandas* folder. Please look through the code to become familiar with it.

Remember to see the dashboard, you'll need to start the web app by opening a terminal and typing `cd 3_flask+plotly+pandas` then typing `python worldbank.py` in the terminal.

Then you need to find the workspace environmental variables with `env | grep WORK`, and you can open a new browser window and go to the address:
`http://WORKSPACESPACEID-3001.WORKSPACEDOMAIN` replacing WORKSPACEID and WORKSPACEDOMAIN with your values.


In part 3, the code iterated through the data set to create a visualization with multiple lines: one for each country.  

The original code for a line chart with a single line was:
```python
graph_one = [go.Scatter(
  x = data[0][1],
  y = data[0][2],
  mode = 'lines',
  name = country
)]
```

To make a visualization with multiple lines, `graph_one` will be a list of line charts. This was accomplished with the following code:
```python
graph_one = []
for data_tuple in data:
   graph_one.append(go.Scatter(
   x = data_tuple[1],
   y = data_tuple[2],
   mode = 'lines',
   name = data_tuple[0]
))
```
