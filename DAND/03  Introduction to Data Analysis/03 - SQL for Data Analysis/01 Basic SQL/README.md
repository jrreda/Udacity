# Basic SQL

Here you will get your first taste at how SQL works, and learn the basics of the SQL language. You will learn how to write code to interact with tables similar to the ones we analyzed in Excel earlier. Specifically, you will learn a little about databases, the basic syntax of SQL, and you will write your first queries!



## Table of contents

- [Entity Relationship Diagrams](#erd)
- [SQL vs. NoSQL](#sns)
- [Why Businesses Like Databases](#wbld)
- [Types of Databases](#tod)
- [Types of Statements](#tos)
- [Commands Recap](#cr)
- [Other Tips](#ot)
- [Helpful Resources](#hr)



## Entity Relationship Diagrams <a name="erd"></a>

An **entity relationship diagram** (ERD) is a common way to view data in a database. Below is the ERD for the database we will use from Parch & Posey. These diagrams help you visualize the data you are analyzing including:

1. The names of the tables.
2. The columns in each table.
3. The way the tables work together.

You can think of each of the boxes below as a **spreadsheet**.

<img src='schema.png' alt="schema" width="80%;"/>



## SQL vs. NoSQL <a name="sns"></a>

You may have heard of NoSQL, which stands for not only SQL. Databases using NoSQL allow for you to write code that interacts with the data a bit differently than what we will do in this course. These NoSQL environments tend to be particularly popular for web based data, but less popular for data that lives in spreadsheets the way we have been analyzing data up to this point. One of the most popular NoSQL languages is called [MongoDB](https://www.mongodb.com/). Udacity has a full course on MongoDB that you can take for free [here](https://www.udacity.com/course/data-wrangling-with-mongodb--ud032), but these will not be a focus of this program.

NoSQL is not a focus of analyzing data in this Nanodegree program, but you might see it referenced outside this course!



## Why Businesses Like Databases <a name="wbld"></a>

1. **Data integrity is ensured** - only the data you want entered is entered, and only certain users are able to enter data into the database.
2. **Data can be accessed quickly** - SQL allows you to obtain results very quickly from the data stored in a database. Code can be optimized to quickly pull results.
3. **Data is easily shared** - multiple individuals can access data stored in a database, and the data is the same for all users allowing for consistent results for anyone with access to your database.



## Types of Databases <a name="tod"></a>

There are many different types of SQL databases designed for different purposes. In this course we will use [Postgres](https://www.postgresql.org/) within the classroom, which is a popular open-source database with a very complete library of analytical functions.

Some of the most popular databases include:

- MySQL
- Access
- Oracle
- Microsoft SQL Server
- Postgres

You can also write SQL within other programming frameworks like Python, Scala, and HaDoop.




## Types of Statements <a name="tos"></a>

The key to SQL is understanding *statements*. A few statements include:

- **CREATE TABLE** is a statement that creates a new table in a database.
- **DROP TABLE** is a statement that removes a table in a database.
- **SELECT** allows you to read data and display it. This is called a query.

The **SELECT** statement is the common statement used by analysts, and you will be learning all about them throughout this course!





## Commands Recap <a name="cr"></a>

You have already learned a lot about writing code in SQL! Let's take a moment to recap all that we have covered before moving on:  
**Statement** 	**How to Use It** 	**Other Details**  
SELECT  ```SELECT Col1, Col2, …``` 	Provide the columns you want  
FROM    ```FROM Table``` 	Provide the table where the columns exist  
LIMIT   ```LIMIT 10``` 	Limits based number of rows returned  
ORDER BY 	```ORDER BY Col``` 	Orders table based on the column. Used with **DESC**.  
WHERE 	```WHERE Col > 5``` 	A conditional statement to filter your results  
LIKE 	```WHERE Col LIKE '%me%'``` 	Only pulls rows where column has 'me' within the text  
IN  ```WHERE Col IN ('Y', 'N')``` 	A filter for only rows with column of 'Y' or 'N'  
NOT     ```WHERE Col NOT IN ('Y', 'N')``` 	**NOT** is frequently used with **LIKE** and **IN**  
AND 	```WHERE Col1 > 5 AND Col2 < 3``` 	Filter rows where two or more conditions must be true  
OR 	```WHERE Col1 > 5 OR Col2 < 3``` 	Filter rows where at least one condition must be true  
BETWEEN 	```WHERE Col BETWEEN 3 AND 5``` 	Often easier syntax than using an **AND**  


## Other Tips <a name="ot"></a>

Though SQL is **not case sensitive** (it doesn't care if you write your statements as all uppercase or lowercase), we discussed some best practices. **The order of the key words does matter!** Using what you know so far, you will want to write your statements as:  
```SQL
SELECT col1, col2
FROM table1
WHERE col3  > 5 AND col4 LIKE '%os%'
ORDER BY col5
LIMIT 10;
```

No  tice, you can retrieve different columns than those being used in the **ORDER BY** and **WHERE** statements. Assuming all of these column names existed in this way (`col1`, `col2`, `col3`, `col4`, `col5`) within a table called `table1`, this query would run just fine.



# Helpful Resources <a name="hr"></a>

- The article [here](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems) compares three of the most common types of SQL: SQLite, PostgreSQL, and MySQL. Though you will use PostgreSQL in the classroom, you will utilize SQLite for the project. Again, once you have learned how to write SQL in one environment, the skills are mostly transferable.
