-- List all genres from the database hbtn_0d_tvshows along with the number of:
-- shows linked to each.
-- Does not display genres without linked shows.
-- Records are ordered by descending number of shows linked.
SELECT tv_g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS tv_g
       INNER JOIN `tv_show_genres` AS tv_s_g
       ON tv_g.`id` = tv_s_g.`genre_id`
 GROUP BY tv_g.`name`
 ORDER BY `number_of_shows` DESC;
