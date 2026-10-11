USE responsight;

SELECT
    location,
    COUNT(*) AS total_calls
FROM ambulance_developing_ems
GROUP BY location
ORDER BY total_calls DESC;