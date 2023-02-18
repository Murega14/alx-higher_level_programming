-- lists all cities contained in the database
SELECT c.id, c.name, s.name FROM cities c, states s
INNER JOIN states ON cities.state_id=s.id
ORDER BY c.id;