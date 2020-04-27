SELECT IFNULL(ROUND(r.total_accept / f.total_send, 2), 0.00) AS accept_rate
FROM
(SELECT COUNT(DISTINCT sender_id, send_to_id) AS total_send
FROM friend_request) f,

(SELECT COUNT(DISTINCT requester_id, accepter_id) AS total_accept
FROM request_accepted) r