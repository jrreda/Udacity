# SQL Data Cleaning

In this lesson, you will be learning a number of techniques to

- Clean and re-structure messy data.
- Convert columns to different data types.
- Tricks for manipulating **NULL**s.

This will give you a robust toolkit to get from raw data to clean data that's useful for analysis.


## Commands

In this lesson, you learned about:

- **LEFT** - pulls a specified number of characters for each row in a specified column starting at the beginning (or from the left). As you saw here, you can pull the first three digits of a phone number using `LEFT(phone_number, 3)`.
- **RIGHT** - pulls a specified number of characters for each row in a specified column starting at the end (or from the right). As you saw here, you can pull the last eight digits of a phone number using `RIGHT(phone_number, 8)`.
- **LENGTH** - provides the number of characters for each row of a specified column. Here, you saw that we could use this to get the length of each phone number as `LENGTH(phone_number)`.

- **POSITION** - takes a character and a column, and provides the index where that character is for each row. The index of the first position is 1 in SQL. If you come from another programming language, many begin indexing at 0. Here, you saw that you can pull the index of a comma as `POSITION(',' IN city_state)`.
- **STRPOS** - provides the same result as POSITION, but the syntax for achieving those results is a bit different as shown here: `STRPOS(city_state, ',')`.
- **LOWER**
- **UPPER**

Note, both **POSITION** and **STRPOS** are case sensitive, so looking for `A` is different than looking for `a`.

Therefore, if you want to pull an index regardless of the case of a letter, you might want to use **LOWER** or **UPPER** to make all of the characters lower or uppercase.

- **CONCAT**
- **Piping `||`**

Each of these will allow you to combine columns together across rows. In this video, you saw how first and last names stored in separate columns could be combined together to create a full name: `CONCAT(first_name, ' ', last_name)` or with piping as `first_name || ' ' || last_name`.

- **TO_DATE**
- **CAST**
- **Casting with `::`**

`DATE_PART('month', TO_DATE(month, 'month'))` here changed a month name into the number associated with that particular month.

Then you can change a string to a date using **CAST**. **CAST** is actually useful to change lots of column types. Commonly you might be doing as you saw here, where you change a `string` to a `date` using `CAST(date_column AS DATE)`. However, you might want to make other changes to your columns in terms of their data types. You can see other examples [here](http://www.postgresqltutorial.com/postgresql-cast/).

In this example, you also saw that instead of `CAST(date_column AS DATE)`, you can use `date_column::DATE`.


---
For a reminder on any of the data cleaning functionality, the concepts in this lesson are labeled according to the functions you learned. If you felt uncomfortable with any of these functions at first, that is normal - these take some getting used to. Don't be afraid to take a second pass through the material to sharpen your skills!


Memorizing all of this functionality isn't necessary, but you do need to be able to follow documentation, and learn from what you have done in solving previous problems to solve new problems.


There are a few other functions that work similarly. You can read more about those [here](https://www.w3schools.com/sql/sql_isnull.asp). You can also get a walk through of many of the functions you have seen throughout this lesson [here](https://community.modeanalytics.com/sql/tutorial/sql-string-functions-for-cleaning/).
