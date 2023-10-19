-- List all cities sorted in ascending order by cities.id

SELECT
    cities.id,
    cities.name,
    states.name
FROM cities, states
WHERE
    cities.state_id = states.id
ORDER BY cities.id ASC;