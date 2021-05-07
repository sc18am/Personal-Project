set search_path to mimiciii;

COPY (  
   WITH first_admission_time AS
    (
    SELECT
        p.subject_id, p.dob
        , a.admittime
        , ROUND( (cast(admittime as date) - cast(dob as date)) / 365.242,2) 
            AS admit_age, a.hadm_id,
        i.hadm_id, i.intime
    FROM patients p
    INNER JOIN admissions a
    ON p.subject_id = a.subject_ids
    )
    SELECT
        subject_id, dob,
        admittime, admit_age, hadm_id, i.hadm_id, i.intime
        FROM icustays i
        INNER JOIN first_admission_time f
        ON i.hadm_id = f.hadm_id,

        CASE
            -- all ages > 89 in the database were replaced with 300
            WHEN admit_age >= 65 
                THEN 'Seniors'
            WHEN admit_age >= 25 AND admit_age <= 64
                THEN 'Adult'
            WHEN admit_age >= 15 AND admit_age <= 24
                THEN 'Youth'
            WHEN admit_age >= 1 AND admit_age <=14
                THEN 'Child'
            ELSE 'other'
            END AS age_group
    FROM first_admission_time
    WHERE subject_id = '124'
) TO 'D:/mimic/Queries/zoomed_out/124age.csv' DELIMITER ',' CSV HEADER;