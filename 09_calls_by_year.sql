USE responsight;

SELECT
    year,
    COUNT(*) AS total_calls,
    ROUND(AVG(response_time_min), 2) AS avg_response_time_min
FROM ambulance_developing_ems
GROUP BY year
ORDER BY year;