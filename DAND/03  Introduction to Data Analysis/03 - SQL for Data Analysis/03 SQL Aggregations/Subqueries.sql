--------------- Subquery Mania ---------------

-- Find the average number of events for each day for each channel.

SELECT channel,
	AVG(num_events) avg_num_events
FROM (
	SELECT channel,
		DATE_TRUNC('day', occurred_at),
    	COUNT(*) num_events
	FROM web_events
	GROUP BY 1, 2
  ) sub
GROUP BY channel;


-- Use DATE_TRUNC to pull "month" level information about the first order ever placed in the orders table. Use this result to find only the orders that took place in the same month-year combo as the first order and then pull the average for each type of paper 'qty' in this month and the total amount spent on all orders.

SELECT AVG(standard_qty) standard,
	AVG(gloss_qty) gloss,
    AVG(poster_qty) poster,
    SUM(total_amt_usd)
FROM orders
WHERE DATE_TRUNC('month', occurred_at) =
	(SELECT MIN(DATE_TRUNC('month', occurred_at))
	FROM orders)



-- 1. Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.

SELECT t3.rep_name, t3.region_name, t3.total_amt
FROM(SELECT region_name, MAX(total_amt) total_amt
     FROM(SELECT s.name rep_name, r.name region_name, SUM(o.total_amt_usd) total_amt
             FROM sales_reps s
             JOIN accounts a
             ON a.sales_rep_id = s.id
             JOIN orders o
             ON o.account_id = a.id
             JOIN region r
             ON r.id = s.region_id
             GROUP BY 1, 2) t1
     GROUP BY 1) t2
JOIN (SELECT s.name rep_name, r.name region_name, SUM(o.total_amt_usd) total_amt
     FROM sales_reps s
     JOIN accounts a
     ON a.sales_rep_id = s.id
     JOIN orders o
     ON o.account_id = a.id
     JOIN region r
     ON r.id = s.region_id
     GROUP BY 1,2
     ORDER BY 3 DESC) t3
ON t3.region_name = t2.region_name AND t3.total_amt = t2.total_amt;



-- 2. For the region with the largest (sum) of sales total_amt_usd, how many total (count) orders were placed?

SELECT total_orders
FROM(
    SELECT r.name region, SUM(o.total_amt_usd) total_amt_usd, COUNT(*) total_orders
    FROM orders o
    JOIN accounts a
    ON a.id = o.account_id
    JOIN sales_reps s
    ON s.id = a.sales_rep_id
    JOIN region r
    ON r.id = s.region_id
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 1
)t1;



-- 3. How many accounts had more total purchases than the account name which has bought the most standard_qty paper throughout their lifetime as a customer?

SELECT COUNT(*)
FROM
    (SELECT a.name
    FROM orders o
    JOIN accounts a
    ON a.id = o.account_id
    GROUP BY 1
    HAVING sum(o.total) > (SELECT total
        FROM (SELECT a.name account, SUM(o.standard_qty) standard_qty, SUM(o.total) total
            FROM orders o
            JOIN accounts a
            ON a.id = o.account_id
            GROUP BY 1
            ORDER BY 2 DESC
            LIMIT 1)t1 )
        )counter_tab;



-- 4. For the customer that spent the most (in total over their lifetime as a customer) total_amt_usd, how many web_events did they have for each channel?

SELECT a.name, w.channel, COUNT(*)
FROM accounts a
JOIN web_events w
ON a.id = w.account_id AND a.name = (SELECT name
        FROM (SELECT a.name, SUM(o.total_amt_usd) total_spent
        FROM orders o
        JOIN accounts a
        ON a.id = o.account_id
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 1)t1 )
GROUP BY 1,2
ORDER BY 3 DESC;



-- 5. What is the lifetime average amount spent in terms of total_amt_usd for the top 10 total spending accounts?

SELECT AVG(total_spent)
FROM(
    SELECT a.name, SUM(o.total_amt_usd)  total_spent
    FROM orders o
    JOIN accounts a
    ON a.id = o.account_id
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 10
)t1 ;



-- 6. What is the lifetime average amount spent in terms of total_amt_usd, including only the companies that spent more per order, on average, than the average of all orders.

SELECT AVG(avg_amt)
FROM(
    SELECT o.account_id, AVG(o.total_amt_usd) avg_amt
    FROM orders o
    GROUP BY 1
    HAVING AVG(o.total_amt_usd) > (SELECT AVG(o.total_amt_usd) avg_all
    FROM orders o)
)temp ;


--------------- with ---------------


-- You need to find the average number of events for each channel per day.

WITH events AS (
          SELECT DATE_TRUNC('day',occurred_at) AS day,
                        channel, COUNT(*) as events
          FROM web_events
          GROUP BY 1,2)

SELECT channel, AVG(events) AS average_events
FROM events
GROUP BY channel
ORDER BY 2 DESC;


-- 1. Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.

WITH table1 AS(
        SELECT s.name rep_name, r.name region_name, SUM(o.total_amt_usd) total_amt
        FROM sales_reps s
        JOIN accounts a
        ON a.sales_rep_id = s.id
        JOIN orders o
        ON o.account_id = a.id
        JOIN region r
        ON r.id = s.region_id
        GROUP BY 1,2
        ORDER BY 3 DESC),
    table2 AS(
        SELECT region_name, MAX(total_amt) total_amt
        FROM table1
        GROUP BY 1
    )

SELECT table1.rep_name, table1.region_name, table1.total_amt
FROM table1
JOIN table2
ON table1.region_name=table2.region_name AND table1.total_amt=table2.total_amt


-- 2. For the region with the largest sales total_amt_usd, how many total orders were placed?

WITH t1 AS(
    SELECT r.name region, SUM(o.total_amt_usd) total_amt_usd, COUNT(*) total_orders
    FROM orders o
    JOIN accounts a
    ON a.id = o.account_id
    JOIN sales_reps s
    ON s.id = a.sales_rep_id
    JOIN region r
    ON r.id = s.region_id
    GROUP BY 1
    ORDER BY 2 DESC
)

SELECT total_orders
FROM t1
LIMIT 1;


-- 3. For the account that purchased the most (in total over their lifetime as a customer) standard_qty paper, how many accounts still had more in total purchases?

WITH t1 AS (
        SELECT a.name account_name, SUM(o.standard_qty) total_std, SUM(o.total) total
        FROM accounts a
        JOIN orders o
        ON o.account_id = a.id
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 1),
    t2 AS(
        SELECT a.name
        FROM orders o
        JOIN accounts a
        ON a.id = o.account_id
        GROUP BY 1
        HAVING sum(o.total) > (SELECT total FROM t1)
    )

SELECT COUNT(*)
FROM t2;


-- 4. For the customer that spent the most (in total over their lifetime as a customer) total_amt_usd, how many web_events did they have for each channel?

WITH t1 AS (
        SELECT a.name, SUM(o.total_amt_usd) total_spent
        FROM orders o
        JOIN accounts a
        ON a.id = o.account_id
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 1)

SELECT a.name, w.channel, COUNT(*)
FROM accounts a
JOIN web_events w
ON a.id = w.account_id AND a.name =  (SELECT name FROM t1)
GROUP BY 1,2
ORDER BY 3 DESC;


-- 5. What is the lifetime average amount spent in terms of total_amt_usd for the top 10 total spending accounts?

WITH t1 AS(
    SELECT a.name, SUM(o.total_amt_usd)  total_spent
    FROM orders o
    JOIN accounts a
    ON a.id = o.account_id
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 10
)

SELECT AVG(total_spent)
FROM t1;


-- 6. What is the lifetime average amount spent in terms of total_amt_usd, including only the companies that spent more per order, on average, than the average of all orders.

WITH t1 AS(
    SELECT o.account_id, AVG(o.total_amt_usd) avg_amt
    FROM orders o
    GROUP BY 1
    HAVING AVG(o.total_amt_usd) > (SELECT AVG(o.total_amt_usd) avg_all FROM orders o)
)

SELECT AVG(avg_amt)
FROM t1;
