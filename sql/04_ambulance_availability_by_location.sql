USE responsight;

SELECT
    location,
    COUNT(*) AS total_calls,
    SUM(ambulance_available) AS available_ambulances,
    ROUND(AVG(ambulance_available) * 100, 2) AS availability_rate_pct
FROM ambulance_developing_ems
GROUP BY location
ORDER BY availability_rate_pct ASC;
