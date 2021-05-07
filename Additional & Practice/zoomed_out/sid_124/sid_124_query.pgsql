set search_path to mimiciii;

COPY (  
    SELECT 
    a.subject_id, a.hadm_id, a.admittime, a.dischtime, a.deathtime, 
    i.hadm_id, i.intime
    FROM
    admissions a
    INNER JOIN icustays i
        ON a.hadm_id = i.hadm_id
    WHERE a.subject_id = '124'
) TO 'D:/mimic/Queries/zoomed_out/sid124.csv' DELIMITER ',' CSV HEADER;