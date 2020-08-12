# Write your MySQL query statement below

# beat 50%
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1, Logs l2, Logs l3
WHERE l1.Id = l2.Id - 1
AND l2.Id = l3.Id - 1
AND l1.num = l2.num
AND l2.num = l3.num

# beat 25%
SELECT DISTINCT l1.Num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2
ON l1.Id=l2.Id-1
JOIN Logs l3
ON l2.Id=l3.Id-1
WHERE l1.Num=l2.Num
AND l2.Num=l3.Num
