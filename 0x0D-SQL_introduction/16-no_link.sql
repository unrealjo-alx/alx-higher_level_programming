-- Lists all records in the second_table with a name value.

SELECT score, name
FROM second_table
WHERE
    name IS NOT NULL
    AND name != ''
ORDER BY score DESC;