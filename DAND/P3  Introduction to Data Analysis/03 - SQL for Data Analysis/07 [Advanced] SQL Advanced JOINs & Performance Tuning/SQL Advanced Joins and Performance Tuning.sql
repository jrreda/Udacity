------------ FULL OUTER JOIN ------------


/* Say you're an analyst at Parch & Posey and you want to see:

- each account who has a sales rep and each sales rep that has an account (all of the columns in these returned rows will be full).
- but also each account that does not have a sales rep and each sales rep that does not have an account (some of the columns in these returned rows will be empty).

This type of question is rare, but FULL OUTER JOIN is perfect for it. In the following SQL Explorer, write a query with FULL OUTER JOIN to fit the above described Parch & Posey scenario (selecting all of the columns in both of the relevant tables, accounts and sales_reps) then answer the subsequent multiple choice quiz.
*/

SELECT *
FROM accounts a
FULL JOIN sales_reps s
on a.sales_rep_id = s.id;
-- If unmatched rows existed (they don't for this query), you could isolate them by adding the following line to the end of the query:
WHERE accounts.sales_rep_id IS NULL OR sales_reps.id IS NULL



------------ JOINs with Comparison Operators ------------

/* In the following SQL Explorer, write a query that left joins the accounts table and the sales_reps tables on each sale rep's ID number and joins it using the < comparison operator on accounts.primary_poc and sales_reps.name.

The query results should be a table with three columns: the account name (e.g. Johnson Controls), the primary contact name (e.g. Cammy Sosnowski), and the sales representative's name (e.g. Samuel Racine). Then answer the subsequent multiple choice question.
*/

SELECT a.name account_name,
       a.primary_poc contact_name,
       s.name sales_representatives_name
FROM accounts a
LEFT JOIN sales_reps s
ON a.sales_rep_id = s.id
    AND a.primary_poc < s.name;



------------ Self JOINs ------------

/* Modify the query from the previous video, which is pre-populated in the SQL Explorer below, to perform the same interval analysis except for the web_events table. Also:

- change the interval to 1 day to find those web events that occurred after, but not more than 1 day after, another web event
- add a column for the channel variable in both instances of the table in your query
*/

SELECT w1.id AS w1_id,
       w1.account_id AS w1_account_id,
       w1.occurred_at AS w1_occurred_at,
       w1.channel AS w1_channel,

       w2.id AS w2_id,
       w2.account_id AS w2_account_id,
       w2.occurred_at AS w2_occurred_at,
       w2.channel AS w2_channel
  FROM web_events w1
 LEFT JOIN web_events w2
   ON w1.account_id = w2.account_id
  AND w1.occurred_at > w2.occurred_at
  AND w1.occurred_at <= w2.occurred_at + INTERVAL '1 day'
ORDER BY w1.account_id, w1.occurred_at



------------ UNION ------------

-- 1. Write a query that uses UNION ALL on two instances (and selecting all columns) of the accounts table. Then inspect the results and answer the subsequent quiz.

SELECT *
FROM accounts

UNION ALL

SELECT *
FROM accounts;

-- 2. Add a WHERE clause to each of the tables that you unioned in the query above, filtering the first table where name equals Walmart and filtering the second table where name equals Disney. Inspect the results then answer the subsequent quiz.

SELECT *
FROM accounts
WHERE name = 'Walmart'

UNION ALL

SELECT *
FROM accounts
WHERE name = 'Disney';

-- 3. Perform the union in your first query (under the Appending Data via UNION header) in a common table expression and name it double_accounts. Then do a COUNT the number of times a name appears in the double_accounts table. If you do this correctly, your query results should have a count of 2 for each name.

WITH double_accounts AS (
    SELECT *
    FROM accounts

    UNION ALL

    SELECT *
    FROM accounts
)

SELECT name,
       COUNT(*) AS name_count
 FROM double_accounts
GROUP BY 1
ORDER BY 2 DESC;
