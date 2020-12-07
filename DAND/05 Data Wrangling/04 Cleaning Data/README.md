# Cleaning Data
Cleaning your data is the third step in data wrangling. It is where you fix the quality and tidiness issues that you identified in the assess step.

#### Data wrangling process:

1. Gather
2. Assess
3. Clean *(this lesson)*



## There are two types of cleaning:

1. Manual (not recommended unless the issues are one-off occurrences).
2. Programmatic.



## The programmatic data cleaning process:

1. **Define**: convert our assessments into defined cleaning tasks. These definitions also serve as an instruction list so others (or yourself in the future) can look at your work and reproduce it.
2. **Code**: convert those definitions to code and run that code.
3. **Test**: test your dataset, visually or with code, to make sure your cleaning operations worked.

Always make copies of the original pieces of data before cleaning!

```py
df_clean = df.copy()
```



## Resources

- [Why should I make a copy of a DataFrame in pandas?](https://stackoverflow.com/questions/27673231/why-should-i-make-a-copy-of-a-data-frame-in-pandas).
