# Write your MySQL query statement below


# Method 1 - Use SUM + CASE WHEN to deal with NULL,
# ELSE 0 END must be at the end, not ELSE 1 END
SELECT t1.team_id, t1.team_name, SUM(CASE WHEN t2.my_goal>t2.op_goal THEN 3 WHEN t2.my_goal=t2.op_goal THEN 1 ELSE 0 END) AS num_points

FROM Teams t1

LEFT JOIN

(SELECT host_team as id, host_goals as my_goal, guest_goals as op_goal
FROM Matches

UNION ALL

SELECT guest_team as id, guest_goals as my_goal, host_goals as op_goal
FROM Matches) t2

ON t1.team_id=t2.id

GROUP BY t1.team_id, t1.team_name
ORDER BY num_points DESC, t1.team_id ASC


# Method 2 - IFNULL deal with NULL, SUM should be at the inner level, not in IFULL
# function
# IFNULL could not use SUM inside directly
SELECT t.team_id, t.team_name, IFNULL(t.num_points, 0) AS num_points
FROM
(SELECT t1.team_id, t1.team_name, SUM(t2.point) AS num_points

FROM Teams t1

LEFT JOIN

((SELECT host_team AS tid, CASE WHEN host_goals>guest_goals THEN 3 WHEN host_goals<guest_goals THEN 0 ELSE 1 END AS point
FROM Matches)

UNION ALL

(SELECT guest_team AS tid, CASE WHEN host_goals>guest_goals THEN 0 WHEN host_goals<guest_goals THEN 3 ELSE 1 END AS point
FROM Matches)) t2
ON t2.tid=t1.team_id

GROUP BY t1.team_id, t1.team_name
) t
ORDER BY num_points DESC, t.team_id ASC