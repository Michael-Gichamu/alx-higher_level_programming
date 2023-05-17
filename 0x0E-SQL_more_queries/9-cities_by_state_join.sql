-- List all cities in the database hbtn_0d_usa.
-- records sorted in ascending order by cities.id.
SELECT `cities`.`id`, `cities`.`name`, `states`.`name`
FROM `cities`
    INNER JOIN `states` ON `cities`.`id` = `states`.`id`
ORDER BY `cities`.`id`;
