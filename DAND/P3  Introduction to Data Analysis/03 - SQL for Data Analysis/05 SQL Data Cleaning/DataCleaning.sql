---------- LEFT & RIGHT Quizzes ----------


-- 1. In the accounts table, there is a column holding the website for each company. The last three digits specify what type of web address they are using. A list of extensions (and pricing) is provided here(https://iwantmyname.com/domains). Pull these extensions and provide how many of each website type exist in the accounts table.

SELECT RIGHT(website, 3), COUNT(*)
FROM accounts
GROUP BY 1;



-- 2. There is much debate about how much the name (or even the first letter of a company name) matters. Use the accounts table to pull the first letter of each company name to see the distribution of company names that begin with each letter (or number).

SELECT LEFT(name, 1), COUNT(*)
FROM accounts
GROUP BY 1
ORDER BY 2 DESC;



-- 3. Use the accounts table and a CASE statement to create two groups: one group of company names that start with a number and a second group of those company names that start with a letter. What proportion of company names start with a letter?

SELECT name,
    CASE
        WHEN LEFT(name, 1) IN ('0','1','2','3','4','5','6','7','8','9')
            THEN 'Number'
        ELSE 'Letter'
    END As start_with
FROM accounts
ORDER BY 1



-- 4. Consider vowels as a, e, i, o, and u. What proportion of company names start with a vowel, and what percent start with anything else?

SELECT
    CASE
        WHEN LEFT(UPPER(name), 1) IN ('A', 'E', 'I', 'O', 'U')
            THEN 'Vowel'
        ELSE 'not_Vowel'
    END As start_with,
    COUNT(*)
FROM accounts
GROUP BY 1
ORDER BY 1



---------- POSITION & STRPOS ----------


-- 1. Use the accounts table to create first and last name columns that hold the first and last names for the primary_poc.

SELECT primary_poc,
    LEFT(primary_poc, STRPOS(primary_poc,' ')-1) AS firstname,
    RIGHT(primary_poc, LENGTH(primary_poc)-STRPOS(primary_poc,' ')) AS lastname
FROM accounts


-- 2. Now see if you can do the same thing for every rep name in the sales_reps table. Again provide first and last name columns.

SELECT name,
    LEFT(name, STRPOS(name, ' ')-1) AS firstname,
    RIGHT(name, LENGTH(name)-STRPOS(name, ' ')) AS lastname
FROM sales_reps



------------ CONCAT ------------


-- 1. Each company in the accounts table wants to create an email address for each primary_poc. The email address should be the first name of the primary_poc . last name primary_poc @ company name .com.

SELECT LOWER(CONCAT(
            LEFT(primary_poc, STRPOS(primary_poc,' ')-1),
            '.',
            RIGHT(primary_poc, LENGTH(primary_poc)-STRPOS(primary_poc,' '))
            ,'@'
            ,name,
            '.com')) email
FROM accounts


-- 2. You may have noticed that in the previous solution some of the company names include spaces, which will certainly not work in an email address. See if you can create an email address that will work by removing all of the spaces in the account name, but otherwise your solution should be just as in question 1. Some helpful documentation is here.

SELECT LOWER(CONCAT(
            LEFT(primary_poc, STRPOS(primary_poc,' ')-1),
            '.',
            RIGHT(primary_poc, LENGTH(primary_poc)-STRPOS(primary_poc,' '))
            ,'@'
            ,TRANSLATE(name,' ',''),
            '.com')) email
FROM accounts


-- 3. We would also like to create an initial password, which they will change after their first log in. The first password will be the first letter of the primary_poc's first name (lowercase), then the last letter of their first name (lowercase), the first letter of their last name (lowercase), the last letter of their last name (lowercase), the number of letters in their first name, the number of letters in their last name, and then the name of the company they are working with, all capitalized with no spaces.

SELECT primary_poc,
    LOWER(
	LEFT(primary_poc, 1) ||
    RIGHT(LEFT(primary_poc, STRPOS(primary_poc,' ')-1),1) ||
    LEFT(RIGHT(primary_poc, LENGTH(primary_poc)-STRPOS(primary_poc,' ')),1) ||
    RIGHT(RIGHT(primary_poc, LENGTH(primary_poc)-STRPOS(primary_poc,' ')),1) ||
    LENGTH(LEFT(primary_poc, STRPOS(primary_poc,' ')-1)) ||
    LENGTH(RIGHT(primary_poc, LENGTH(primary_poc)-STRPOS(primary_poc,' ')))
    )||
    UPPER(TRANSLATE(name, ' ',''))
    AS password
FROM accounts;

-- or --

WITH sub AS(
    SELECT LEFT(primary_poc, STRPOS(primary_poc,' ')-1) AS firstname,
    RIGHT(primary_poc, LENGTH(primary_poc)-STRPOS(primary_poc,' ')) AS lastname,
    id
FROM accounts
)

SELECT LOWER(
        LEFT(sub.firstname, 1) ||
        RIGHT(sub.firstname, 1) ||
        LEFT(sub.lastname, 1) ||
        RIGHT(sub.lastname, 1) ||
        LENGTH(sub.firstname) ||
        LENGTH(sub.lastname) ) ||
        UPPER(TRANSLATE(name, ' ', '')) AS password,
        primary_poc, name
FROM accounts
JOIN sub
ON accounts.id = sub.id;



------------------ CAST ------------------

-- 1.
SELECT *
FROM sf_crime_data
LIMIT 10;

-- 5.
SELECT date,
	(SUBSTR(date, 7, 4) || '-' || SUBSTR(date, 1, 2) || '-' || SUBSTR(date, 4, 2)) :: DATE correct_formate
FROM sf_crime_data;



-------------- COALESCE  --------------

-- 1.
SELECT *
FROM accounts a
LEFT JOIN orders o
ON a.id = o.account_id
WHERE o.total IS NULL;
