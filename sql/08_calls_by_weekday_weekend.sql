USE responsight;

SELECT
    day_of_week,
    COUNT(*) AS total_calls,
    ROUND(AVG(response_time_min), 2) AS avg_response_time_min
FROM ambulance_developing_ems
GROUP BY day_of_week
ORDER BY total_calls DESC;
