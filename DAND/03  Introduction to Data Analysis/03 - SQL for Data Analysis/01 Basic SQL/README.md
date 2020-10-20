# Recap

##Commands

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


## Other Tips

Though SQL is **not case sensitive** (it doesn't care if you write your statements as all uppercase or lowercase), we discussed some best practices. **The order of the key words does matter!** Using what you know so far, you will want to write your statements as:  
```SQL
SELECT col1, col2
FROM table1
WHERE col3  > 5 AND col4 LIKE '%os%'
ORDER BY col5
LIMIT 10;
```

No  tice, you can retrieve different columns than those being used in the **ORDER BY** and **WHERE** statements. Assuming all of these column names existed in this way (`col1`, `col2`, `col3`, `col4`, `col5`) within a table called `table1`, this query would run just fine.
