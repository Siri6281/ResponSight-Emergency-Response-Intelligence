USE responsight;

SELECT
    COUNT(*) AS total_records,
    SUM(location IS NULL) AS missing_location,
    SUM(time_of_day IS NULL) AS missing_time_of_day,
    SUM(priority IS NULL) AS missing_priority,
    SUM(response_time_min IS NULL) AS missing_response_time,
    SUM(ambulance_available IS NULL) AS missing_ambulance_availability,
    SUM(met_target_response IS NULL) AS missing_target_status
FROM ambulance_developing_ems;