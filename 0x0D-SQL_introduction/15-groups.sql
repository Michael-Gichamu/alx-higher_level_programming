-- Lists the number of records with the same score in the table second_table.
-- sorted number of records in descending order.
SELECT `score`, COUNT(*) AS `record_no`
FROM `second_table`
GROUP BY `score`
ORDER BY `record_no` DESC;
