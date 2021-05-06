set search_path to mimiciii;

COPY (  
    SELECT 
    a.hadm_id, a.admittime, a.dischtime, a.deathtime, a.admission_type, 
    s.subject_id, s.hadm_id, s.transfertime, s.curr_service,
    t.hadm_id, t.icustay_id, t.intime, t.outtime, t.curr_wardid, t.curr_careunit
    FROM
    services s
    INNER JOIN admissions a
        ON s.hadm_id = a.hadm_id
    INNER JOIN transfers t
        ON a.hadm_id = t.hadm_id
    WHERE a.admission_type = 'ELECTIVE' and s.curr_service = 'SURG'
) TO 'C:/Users/alexm/OneDrive/Desktop/elective - surg/elective-surg.csv' DELIMITER ',' CSV HEADER;