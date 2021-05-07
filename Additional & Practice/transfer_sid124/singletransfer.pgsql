set search_path to mimiciii;

COPY (
     
    SELECT 
    subject_id, hadm_id, icustay_id, prev_careunit, 
    curr_careunit, intime, outtime
    
    FROM
    transfers
    
    WHERE
    subject_id = '124'

) TO '/transfer_sid124.csv' DELIMITER ',' CSV HEADER;