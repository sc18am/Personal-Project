set search_path to mimiciii;

COPY (  
    SELECT 
    s.subject_id, s.hadm_id, s.transfertime, s.prev_service, s.curr_service,
    a.hadm_id, a.admittime, a.dischtime, a.deathtime, a.admission_type, 
    i.hadm_id, i.icustay_id, i.intime
    FROM
    services s
    INNER JOIN admissions a
        ON s.hadm_id = a.hadm_id
    INNER JOIN icustays i
        ON a.hadm_id = i.hadm_id
    WHERE a.subject_id IN (111, 112, 127, 129, 36, 35, 49, 45, 44, 124)
) TO 'C:/Users/alexm/OneDrive/Desktop/Queries/10subjects/10subjects.csv' DELIMITER ',' CSV HEADER;