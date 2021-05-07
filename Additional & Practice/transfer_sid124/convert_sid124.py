import csv
from csv import DictReader
import itertools

# cleans and sorts the patients timestamps by case id and what sort of timestamp it is
def create_list():
    with open("transfer_sid124.csv") as csv_file:

        f = open("temp1_sid124.txt", "a")

        dict_reader = DictReader(csv_file)
        """
        for row in dict_reader:       
            admittime = row['subject_id']  +","+  row['admittime'] +","+ row['gender'] +","+ 'admittime'
            f.write(admittime)
            f.write("\n")

            dischtime = row['subject_id'] +","+ row['dischtime'] +","+ row['gender'] +","+ 'dischtime'
            f.write(dischtime)
            f.write("\n")

            if len(row['deathtime']) != 0:  
                deathtime = row['subject_id'] +","+ row['deathtime'] +","+ row['gender'] +","+ 'deathtime'
                f.write(deathtime)
                f.write("\n")

            intime = row['subject_id'] +","+ row['intime'] +","+ row['gender'] +","+ 'intime'
            f.write(intime)
            f.write("\n")

            outtime = row['subject_id'] +","+ row['outtime'] +","+ row['gender'] +","+ 'outtime'
            f.write(outtime)
            f.write("\n") 
        """
        for row in dict_reader:       
            intime = row['hadm_id']  + "," + row['subject_id']  + "," + row['icustay_id'] + "," + row['intime'] + "," + row['prev_careunit']  + "," + row['curr_careunit']  + ","  + 'intime'
            f.write(intime)
            f.write("\n")

            outtime = row['hadm_id']  + "," + row['subject_id']  + ","  + row['icustay_id'] + "," + row['outtime'] + "," + row['prev_careunit']  + ","  + row['curr_careunit']  + ","  + 'outtime'
            f.write(outtime)
            f.write("\n")

def write_to_csv():
    
    with open("temp1_sid124.txt", "r") as infile:
        stripped = (line.strip() for line in infile)
        lines = (line.split(",") for line in stripped if line)
        with open("sid124_event_log1.csv", "w") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(("hadm_id", "subject_id", "icustay_id", "timestamp", "previous_careunit", "current_careunit", "time"))
            writer.writerows(lines)

create_list()
write_to_csv()