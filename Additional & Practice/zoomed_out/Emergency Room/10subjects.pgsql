set search_path to mimiciii;

COPY (  
   WITH first_admission_time AS
    (
    SELECT
        p.subject_id, p.dob, p.gender
        , MIN (a.admittime) AS first_admittime
        , MIN( ROUND( (cast(admittime as date) - cast(dob as date)) / 365.242,2) )
            AS first_admit_age
    FROM patients p
    INNER JOIN admissions a
    ON p.subject_id = a.subject_id
    GROUP BY p.subject_id, p.dob, p.gender
    ORDER BY p.subject_id
    )
    SELECT
        subject_id, dob, gender
        , first_admittime, first_admit_age
        , CASE
            -- all ages > 89 in the database were replaced with 300
            WHEN first_admit_age >= 65 
                THEN 'Seniors'
            WHEN first_admit_age >= 25 AND first_admit_age <= 64
                THEN 'Adult'
            WHEN first_admit_age >= 15 AND first_admit_age <= 24
                THEN 'Youth'
            WHEN first_admit_age >= 1 AND first_admit_age <=14
                THEN 'Child'
            ELSE 'other'
            END AS age_group
    FROM first_admission_time
    ORDER BY subject_id
) TO 'D:/mimic/Queries/zoomed_out/agesort.csv' DELIMITER ',' CSV HEADER;