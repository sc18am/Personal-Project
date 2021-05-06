import csv
from csv import DictReader
import itertools

# cleans and sorts the patients timestamps by case id and what sort of timestamp it is
def create_list():
    with open("elective-csurg.csv") as csv_file:

        f = open("elective.txt", "a")

        dict_reader = DictReader(csv_file)
        
        for row in dict_reader:    

            if len(row['outtime']) != 0:  
                
                
                admittime = row['hadm_id']  +","+  row['subject_id'] +","+ row['admittime'] +", ADMISSION"
                f.write(admittime)
                f.write("\n")
                
                
                if row['transfertime'] == row['intime']:
                    service =  row['hadm_id']  +","+ row['subject_id'] +","+ row['intime']  +","+  row['curr_service'] 
                    f.write(service)
                    f.write("\n")


                if row['transfertime'] == row['intime'] and len(row['curr_careunit']) != 0 and row['curr_careunit'] == "CSRU":
                    icustay =  row['hadm_id']  +","+ row['subject_id'] +","+ row['intime']  +","+  row['curr_careunit'] 
                    f.write(icustay)
                    f.write("\n")
                
                
                if row['transfertime'] == row['intime'] and len(row['curr_careunit']) != 0 and row['curr_careunit'] != "CSRU":
                    icustay =  row['hadm_id']  +","+ row['subject_id'] +","+ row['intime']  +", OTHER ICU"
                    f.write(icustay)
                    f.write("\n")


                elif len(row['icustay_id']) == 0 and row['transfertime'] != row['intime'] and len(row['curr_wardid']) != 0:
                    wardstay =  row['hadm_id']  +","+ row['subject_id'] +","+ row['intime']  + ", WARD"
                    f.write(wardstay)
                    f.write("\n")


                elif len(row['icustay_id']) != 0 and row['curr_careunit'] == "CSRU":
                    icustay =  row['hadm_id']  +","+ row['subject_id'] +","+ row['intime']  + "," + row['curr_careunit']  
                    f.write(icustay)
                    f.write("\n")


                elif len(row['icustay_id']) != 0 and row['curr_careunit'] != "CSRU":
                    icustay =  row['hadm_id']  +","+ row['subject_id'] +","+ row['intime']  + ", OTHER ICU" 
                    f.write(icustay)
                    f.write("\n")


                dischtime = row['hadm_id']  +","+  row['subject_id'] +","+ row['dischtime'] + ', DISCHARGED'
                f.write(dischtime)
                f.write("\n")   


                if len(row['deathtime']) != 0 and row['deathtime'] == row['dischtime']:  
                    deathtime = row['hadm_id']  +","+  row['subject_id'] +","+ row['deathtime'] + ', DEAD'
                    f.write(deathtime)
                    f.write("\n")
            
            else:
                continue

def write_to_csv():
    
    with open("elective.txt", "r") as infile:
        stripped = (line.strip() for line in infile)
        lines = (line.split(",") for line in stripped if line)
        with open("event_log.csv", "w") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(("hadm_id", "subject_id", "timestamp", "event"))
            writer.writerows(lines)

create_list()
write_to_csv()