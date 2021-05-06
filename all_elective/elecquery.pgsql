set search_path to mimiciii;

COPY (  
    SELECT 
    a.hadm_id, a.admittime, a.dischtime, a.deathtime, a.admission_type, 
    s.subject_id, s.hadm_id, s.transfertime, s.prev_service, s.curr_service,
    t.hadm_id, t.icustay_id, t.intime, t.outtime, t.curr_wardid, t.prev_wardid
    FROM
    services s
    INNER JOIN admissions a
        ON s.hadm_id = a.hadm_id
    INNER JOIN transfers t
        ON a.hadm_id = t.hadm_id
    WHERE a.admission_type = 'ELECTIVE' 
) TO 'C:/Users/alexm/OneDrive/Desktop/Queries/elective_planned/all/elective.csv' DELIMITER ',' CSV HEADER;