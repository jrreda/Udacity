# Multiple Linear Regression

Learn to apply multiple linear regression models in python. Learn to interpret the results and understand if your model fits well.


## Dummy Variables

The way that we add categorical variables into our multiple linear regression models is by using dummy variables. The most common way dummy variables are added is through 1, 0 encoding. In this encoding method, you create a new column for each level of a category (in this case A, B, or C). Then our new columns either hold a 1 or 0 depending on the presence of the level in the original column.

<img src='dummy.png.jpg' alt="Dummy Variables" width="80%;"/>

When we add these dummy variables to our multiple linear regression models, we always drop one of the columns. The column you drop is called the **baseline**. The coefficients you obtain from the output of your multiple linear regression models are then an indication of how the encoded levels compare to the baseline level (the dropped level).


## Linear Model Assumptions

Here are the five assumptions addressed in the previous video addressed in [Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Seventh%20Printing.pdf):

1. Non-linearity of the response-predictor relationships
2. Correlation of error terms
3. Non-constant Variance and Normally Distributed Errors
4. Outliers/ High leverage points
5. Collinearity


# Recap

The topics in this lesson included:  

- You learned how to build a multiple linear regression model in Python, which was actually very similar to what you did in the last lesson on simple linear regression.  
- You learned how to encode **dummy variables**, and interpret the coefficients attached to each.  
- You learned about higher order terms, and how this impacts your ability to interpret coefficients.  
- You learned how to identify what it would mean for an interaction to be needed in a multiple linear regression model, as well as how to identify other higher order terms. But again, these do make interpreting coefficients directly less of a priority, and move your model towards one that, rather, aims to predict better at the expense of interpretation.  
- You learned about the model assumptions, and we took a closer look at **multicollinearity**. You learned about variance inflation factors, and how multicollinearity impacts the model coefficients and standard errors.
