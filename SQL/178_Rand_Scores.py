# Write your MySQL query statement below

SELECT s1.Score, COUNT(s2.Score) AS Rank
FROM Scores s1, (SELECT DISTINCT Score FROM Scores) s2
WHERE s1.Score<=s2.Score
GROUP BY s1.Id
ORDER BY s1.Score DESC