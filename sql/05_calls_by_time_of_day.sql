USE responsight;

SELECT
    time_of_day,
    COUNT(*) AS total_calls,
    ROUND(AVG(response_time_min), 2) AS avg_response_time_min
FROM ambulance_developing_ems
GROUP BY time_of_day
ORDER BY total_calls DESC;
