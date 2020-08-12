# beat 50%
SELECT ROUND(AVG(cnt), 2) AS average_daily_percent 
FROM
(
SELECT (COUNT(DISTINCT r.post_id)/ COUNT(DISTINCT a.post_id))*100  AS cnt  # This line is so neat
FROM Actions a

LEFT JOIN Removals r

ON a.post_id = r.post_id

WHERE a.extra='spam' AND a.action = 'report'
GROUP BY a.action_date )tmp
