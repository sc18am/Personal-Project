import csv
from csv import DictReader
import itertools

# cleans and sorts the patients timestamps by case id and what sort of timestamp it is
def create_list():
    with open("limit200.csv") as csv_file:

        f = open("temp_limit200.txt", "a")

        dict_reader = DictReader(csv_file)
        
        for row in dict_reader:      
            admittime = row['hadm_id']  +","+  row['subject_id'] +","+ row['admittime'] + ", admission"
            f.write(admittime)
            f.write("\n")
            
            icustay =  row['hadm_id']  +","+ row['subject_id'] +","+ row['intime'] + ", icu stay"
            f.write(icustay)
            f.write("\n")

            dischtime = row['hadm_id']  +","+  row['subject_id'] +","+ row['dischtime'] + ', discharged'
            f.write(dischtime)
            f.write("\n")

            if len(row['deathtime']) != 0:  
                deathtime = row['hadm_id']  +","+  row['subject_id'] +","+ row['deathtime'] + ', DEAD'
                f.write(deathtime)
                f.write("\n")
    
            #edregtime =  row['hadm_id']  +","+  row['edregtime'] +"," + 'edregtime'
            #f.write(edregtime)
            #f.write("\n")
            
            #edregouttime =  row['hadm_id']  +","+  row['edregouttime'] +","+ 'edregouttime'
            #f.write(edregouttime)
            #f.write("\n")

           # admission_location =  row['hadm_id']  +","+  row['admission_location'] +","+ 'admission_location'
           # f.write(admission_location)
           # f.write("\n")

            #last_careunit =  row['hadm_id']  +","+ row['outtime'] +","+ row['last_careunit'] +"-"+'lastcareunit'
            #f.write(last_careunit)
            #f.write("\n")

            #first_wardid =  row['hadm_id']  +","+  row['first_wardid'] +","+ 'first_wardid'
            #f.write(first_wardid)
            #f.write("\n")

            #last_wardid = row['hadm_id']  +","+  row['last_wardid'] +","+ 'last_wardid'
            #f.write(last_wardid)
            #f.write("\n")

           # intime = row['hadm_id']  +","+  row['intime'] +","+ 'intime'
           # f.write(intime)
           # f.write("\n")



def write_to_csv():
    
    with open("temp_limit200.txt", "r") as infile:
        stripped = (line.strip() for line in infile)
        lines = (line.split(",") for line in stripped if line)
        with open("limit200_event_log.csv", "w") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(("hadm_id", "subject_id", "timestamp", "event"))
            writer.writerows(lines)

create_list()
write_to_csv()