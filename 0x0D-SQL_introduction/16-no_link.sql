-- lists all records of the table second_table with no name order
SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;



