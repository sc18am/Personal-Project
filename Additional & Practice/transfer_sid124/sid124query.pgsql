set search_path to mimiciii;

COPY (  
    SELECT 
    a.subject_id, a.hadm_id, a.admittime, a.dischtime, a.deathtime, a.edregtime, a.edouttime,
    t.hadm_id, t.prev_careunit, t.curr_careunit, t.intime, t.outtime
    FROM
    admissions a
    INNER JOIN transfers t
        ON a.subject_id = t.subject_id
    WHERE a.subject_id = '124'
) TO 'D:/mimic/Queries/transfer_sid124/transfer_sid124_2.csv' DELIMITER ',' CSV HEADER;