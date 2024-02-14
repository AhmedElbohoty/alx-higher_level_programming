-- Lists all the cities of California that can be found in
-- the database hbtn_0d_usa.

SELECT c.id, c.name
  FROM cities AS c INNER JOIN states AS s
    ON s.id = c.state_id
 ORDER BY c.id;
