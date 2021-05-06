set search_path to mimiciii;

COPY (  
    SELECT 
    s.subject_id, s.hadm_id, s.transfertime, s.prev_service, s.curr_service,
    a.hadm_id, a.admittime, a.dischtime, a.deathtime, a.admission_location, 
    t.hadm_id, t.icustay_id, t.intime
    FROM
    services s
    INNER JOIN admissions a
        ON s.hadm_id = a.hadm_id
    INNER JOIN transfers t
        ON a.hadm_id = t.hadm_id
    WHERE a.hadm_id = '112906' 
) TO 'C:/Users/alexm/OneDrive/Desktop/Queries/general/3tables.csv' DELIMITER ',' CSV HEADER;