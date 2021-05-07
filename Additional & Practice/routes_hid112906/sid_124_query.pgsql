set search_path to mimiciii;

COPY (  
    SELECT 
    a.subject_id, a.hadm_id, a.admittime, a.dischtime, a.deathtime, a.edregtime, a.edouttime, a.admission_location,
    i.hadm_id, i.first_careunit, i.last_careunit, i.first_wardid, i.last_wardid, i.intime, i.outtime
    FROM
    admissions a
    INNER JOIN icustays i
        ON a.hadm_id = i.hadm_id
    WHERE a.subject_id = '124'
) TO 'D:/mimic/Queries/routes_hid112906/temp_sid124.csv' DELIMITER ',' CSV HEADER;c