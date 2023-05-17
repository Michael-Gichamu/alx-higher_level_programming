-- Lists all shows in the database hbtn_0d_tvshows without a genre linked.
-- Records are ordered by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT tv_s.`title`, tv_g.`genre_id`
  FROM `tv_shows` AS tv_s
       LEFT JOIN `tv_show_genres` AS tv_g
       ON tv_s.`id` = tv_g.`show_id`
       WHERE tv_g.`genre_id` IS NULL
 ORDER BY tv_s.`title`, tv_g.`genre_id`;
