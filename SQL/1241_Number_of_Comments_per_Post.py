# Write your MySQL query statement below
SELECT s1.sub_id AS post_id, IFNULL(s2.cnt, 0) AS number_of_comments
FROM
(SELECT DISTINCT sub_id
FROM Submissions
WHERE parent_id IS NULL
) s1
LEFT JOIN
(SELECT parent_id, COUNT(DISTINCT sub_id) AS cnt
FROM Submissions
WHERE parent_id is not NULL
GROUP BY parent_id) s2
ON s1.sub_id=s2.parent_id
ORDER BY post_id