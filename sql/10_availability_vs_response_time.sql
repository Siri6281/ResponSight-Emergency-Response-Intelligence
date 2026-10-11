USE responsight;

SELECT
    ambulance_available,
    COUNT(*) AS total_calls,
    ROUND(AVG(response_time_min), 2) AS avg_response_time_min,
    SUM(met_target_response) AS targets_met
FROM ambulance_developing_ems
GROUP BY ambulance_available
ORDER BY ambulance_available DESC;
