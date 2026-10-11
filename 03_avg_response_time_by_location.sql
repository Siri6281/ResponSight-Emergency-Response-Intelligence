USE responsight;

SELECT
    location,
    ROUND(AVG(response_time_min), 2) AS avg_response_time_min
FROM ambulance_developing_ems
GROUP BY location
ORDER BY avg_response_time_min DESC;