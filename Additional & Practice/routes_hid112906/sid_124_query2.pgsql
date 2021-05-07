set search_path to mimiciii;

COPY (  
    SELECT 
    a.subject_id, a.hadm_id, a.admittime, a.dischtime, a.deathtime, a.admission_location, a.discharge_location,
    t.hadm_id, t.curr_careunit, t.curr_wardid, t.intime, t.eventtype
    FROM
    admissions a
    INNER JOIN transfers t
        ON a.hadm_id = t.hadm_id
    WHERE a.subject_id = '124'
) TO 'D:/mimic/Queries/routes_hid112906/temp1_sid124.csv' DELIMITER ',' CSV HEADER;