# Write your MySQL query statement below

# Method 1 - beat 10%, sometimes 70% - DENSE_RANK()
SELECT Score, DENSE_RANK() OVER (ORDER BY Score DESC) AS "Rank"
FROM Scores

# Method 2 - too complicate to remember....
SELECT s1.Score, COUNT(s2.Score) AS Rank
FROM Scores s1, (SELECT DISTINCT Score FROM Scores) s2
WHERE s1.Score<=s2.Score
GROUP BY s1.Id
ORDER BY s1.Score DESC
