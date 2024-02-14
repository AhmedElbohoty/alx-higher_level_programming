-- Lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each.

SELECT g.name AS genre, COUNT(tv_show_genres.genre_id) AS number_shows
  FROM tv_show_genres AS sg
 INNER JOIN tv_genres AS g
    ON g.id = sg.genre_id
 GROUP BY g.name
 ORDER BY number_shows DESC;
