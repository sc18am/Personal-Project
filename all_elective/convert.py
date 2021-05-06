import csv
from csv import DictReader
import itertools

# cleans and sorts the patients timestamps by case id and what sort of timestamp it is
def create_list():
    with open("elective.csv") as csv_file:

        f = open("elective.txt", "a")

        dict_reader = DictReader(csv_file)
        
        for row in dict_reader:      
            admittime = row['hadm_id']  +","+  row['subject_id'] +","+ row['admittime'] +","+  row['admission_type'] 
            f.write(admittime)
            f.write("\n")
            
            
            if row['transfertime'] == row['intime']:
                service =  row['hadm_id']  +","+ row['subject_id'] +","+ row['intime']  +","+  row['curr_service'] + " - " + row['curr_wardid']
                f.write(service)
                f.write("\n")

            
            elif len(row['icustay_id']) == 0 and row['transfertime'] != row['intime'] and len(row['curr_wardid']) != 0:
                wardstay =  row['hadm_id']  +","+ row['subject_id'] +","+ row['intime']  + "," + row['curr_wardid'] + " WARD"
                f.write(wardstay)
                f.write("\n")


            elif len(row['icustay_id']) != 0:
                icustay =  row['hadm_id']  +","+ row['subject_id'] +","+ row['intime']  + "," + " ICU - " + row['curr_wardid'] 
                f.write(icustay)
                f.write("\n")
           
           
            dischtime = row['hadm_id']  +","+  row['subject_id'] +","+ row['dischtime'] + ', DISCHARGED'
            f.write(dischtime)
            f.write("\n")


            if len(row['deathtime']) != 0:  
                deathtime = row['hadm_id']  +","+  row['subject_id'] +","+ row['deathtime'] + ', DEAD'
                f.write(deathtime)
                f.write("\n")
    


def write_to_csv():
    
    with open("elective.txt", "r") as infile:
        stripped = (line.strip() for line in infile)
        lines = (line.split(",") for line in stripped if line)
        with open("elective_event_log.csv", "w") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(("hadm_id", "subject_id", "timestamp", "event"))
            writer.writerows(lines)

create_list()
write_to_csv()