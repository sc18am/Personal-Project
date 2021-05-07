set search_path to mimiciii;

COPY (  
    SELECT 
    subject_id, hadm_id, admittime, dischtime, deathtime, admission_type, 
    admission_location, discharge_location, edregtime, edouttime
    FROM
    admissions
    WHERE hadm_id = '160958'
) TO 'C:/Users/alexm/OneDrive/Desktop/Queries/general/admissions.csv' DELIMITER ',' CSV HEADER;