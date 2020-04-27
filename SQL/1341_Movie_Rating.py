# Write your MySQL query statement below

SELECT t1.name AS results
FROM
(SELECT u.name AS name, COUNT(m.movie_id) AS cnt
FROM Movie_Rating m
JOIN Users u
ON u.user_id = m.user_id
GROUP BY m.user_id
ORDER BY cnt DESC, u.name
LIMIT 1) t1

UNION
SELECT t2.title AS results
FROM
(SELECT m.title AS title, AVG(mr.rating) as grade
 FROM Movie_Rating mr
 JOIN Movies m
 ON m.movie_id=mr.movie_id
 WHERE substring(mr.created_at,1,7)="2020-02"
 GROUP BY mr.movie_id
 ORDER BY grade DESC, m.title
 LIMIT 1
 ) t2

#AVG(mr.rating) = SUM(mr.rating) / COUNT(mr.rating)