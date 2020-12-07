# SQL Joins

In this lesson, you will learn the real power of SQL. You will learn about Entity Relationship Diagrams (ERDs), and how to join multiple tables together from a relational database. The power to join tables is what really moved companies to adopt this approach to holding data.


## Database Normalization

When creating a database, it is really important to think about how data will be stored. This is known as **normalization**, and it is a huge part of most SQL classes. If you are in charge of setting up a new database, it is important to have a thorough understanding of database **normalization**.

There are essentially three ideas that are aimed at database normalization:

1. Are the tables storing logical groupings of the data?
2. Can I make changes in a single location, rather than in many tables for the same information?
3. Can I access and manipulate data quickly and efficiently?

This is discussed in detail [here](http://sqlmag.com/database-performance-tuning/sql-design-why-you-need-database-normalization).

However, most analysts are working with a database that was already set up with the necessary properties in place. As analysts of data, you don't really need to think too much about data **normalization**. You just need to be able to pull the data from the database, so you can start drawing insights. This will be our focus in this lesson.




##  Keys

You learned a key element for **JOIN**ing tables in a database has to do with primary and foreign keys:


* **primary keys** - are unique for every row in a table. These are generally the first column in our database (like you saw with the id column for every table in the Parch & Posey database).  
* **foreign keys** - are the **primary key** appearing in another table, which allows the rows to be non-unique.  

Choosing the set up of data in our database is very important, but not usually the job of a data analyst. This process is known as **Database Normalization**.


## JOINs

In this lesson, you learned how to combine data from multiple tables using **JOINs**. The three **JOIN** statements you are most likely to use are:  

1. **JOIN** - an **INNER JOIN** that only pulls data that exists in both tables.  
2. **LEFT JOIN** - a way to pull all of the rows from the table in the FROM even if they do not exist in the JOIN statement.  
3. **RIGHT JOIN** - a way to pull all of the rows from the table in the JOIN even if they do not exist in the FROM statement.

There are a few more advanced JOINs that we did not cover here, and they are used in very specific use cases. [UNION and UNION ALL](https://www.w3schools.com/sql/sql_union.asp), [CROSS JOIN](https://www.w3schools.com/sql/cross-join.php), and the tricky [SELF JOIN](https://www.w3schools.com/sql/sql_join_self.asp). These are more advanced than this course will cover, but it is useful to be aware that they exist, as they are useful in special cases.


## Alias

You learned that you can alias tables and columns using **AS** or not using it. This allows you to be more efficient in the number of characters you need to write, while at the same time you can assure that your column headings are informative of the data in your table.
