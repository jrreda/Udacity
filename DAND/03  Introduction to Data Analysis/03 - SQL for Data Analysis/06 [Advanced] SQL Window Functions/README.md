# SQL Window Functions [Advanced]

**Window function** performs a calculation across a set of table rows that are somehow related to the current row. This is comparable to the type of calculation that can be done with an aggregate function. But unlike regular aggregate functions, use of a window function does not cause rows to become grouped into a single output row — the rows retain their separate identities. Behind the scenes, the window function is able to access more than just the current row of the query result.

Through introducing window functions, we have also introduced two statements that you may not be familiar with: `OVER` and `PARTITION BY`. These are key to window functions. Not every window function uses `PARTITION BY`; we can also use `ORDER BY` or no statement at all depending on the query we want to run. You will practice using these clauses in the upcoming quizzes. If you want more details right now, [this resource](https://blog.sqlauthority.com/2015/11/04/sql-server-what-is-the-over-clause-notes-from-the-field-101/) from Pinal Dave is helpful.

Note: _You can’t use window functions and standard aggregations in the same query. More specifically, you can’t include window functions in a **GROUP BY** clause._










- PostgreSQL’s documentation does an excellent job of [introducing the concept of Window Functions](https://www.postgresql.org/docs/9.1/static/tutorial-window.html).
