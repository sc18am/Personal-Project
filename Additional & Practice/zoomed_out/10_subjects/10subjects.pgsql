set search_path to mimiciii;

COPY (  
    SELECT 
    a.subject_id, a.hadm_id, a.admittime, a.dischtime, a.deathtime, a.admission_type,
    i.hadm_id, i.intime
    FROM
    admissions a
    INNER JOIN icustays i
        ON a.hadm_id = i.hadm_id
    WHERE a.subject_id IN (111, 112, 127, 129, 36, 35, 49, 45, 44, 124)
) TO 'D:/mimic/Queries/zoomed_out/10subjects.csv' DELIMITER ',' CSV HEADER;