USE responsight;

SELECT
    call_type,
    COUNT(*) AS total_calls,
    SUM(met_target_response) AS targets_met,
    ROUND(AVG(met_target_response) * 100, 2) AS target_rate_pct
FROM ambulance_developing_ems
GROUP BY call_type
ORDER BY target_rate_pct DESC;