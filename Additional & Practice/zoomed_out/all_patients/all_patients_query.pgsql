set search_path to mimiciii;

COPY (  
    SELECT 
    a.subject_id, a.hadm_id, a.admittime, a.dischtime, a.deathtime,
    i.hadm_id, i.intime
    FROM
    admissions a
    INNER JOIN icustays i
        ON a.hadm_id = i.hadm_id
) TO 'D:/mimic/Queries/zoomed_out/all_patients.csv' DELIMITER ',' CSV HEADER;