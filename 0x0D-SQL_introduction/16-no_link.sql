-- Lists all records of the table second_table.
-- list row with name value and descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
