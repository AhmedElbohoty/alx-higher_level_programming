-- Lists all shows, and all genres linked to that show. 

SELECT tv_shows.title, tv_genres.name
  FROM tv_genres LEFT JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
 INNER JOIN tv_shows
    ON tv_shows.id = tv_show_genres.show_id
  ORDER BY tv_shows.title;
