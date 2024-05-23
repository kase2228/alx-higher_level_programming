-- retrives scores of those records having names
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
