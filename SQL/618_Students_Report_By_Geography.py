# beat 50%-80%
SELECT MAX(America) AS America, MAX(Asia) as Asia, MAX(Europe) AS Europe
#SELECT America, Asia, Europe
FROM (
    SELECT
        CASE WHEN continent = 'America' THEN @r1 := @r1 + 1
             WHEN continent = 'Asia'    THEN @r2 := @r2 + 1
             WHEN continent = 'Europe'  THEN @r3 := @r3 + 1 END id,
        CASE WHEN continent = 'America' THEN name ELSE NULL END America,
        CASE WHEN continent = 'Asia'    THEN name ELSE NULL END Asia,
        CASE WHEN continent = 'Europe'  THEN name ELSE NULL END Europe
    FROM student, (SELECT @r1 := 0, @r2 := 0, @r3 := 0) AS ids
    ORDER BY name
) AS tempTable
GROUP BY id;