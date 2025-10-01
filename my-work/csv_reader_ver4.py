#csv_reader_ver3b.py
# Author Cathal Redmond
# 01 Oct 2025 

import csv
FILENAME = "data.csv"
DATADIR = "../my-work/" # i know this just brings my up a level and then back into same folder, but it allows for the excercise. 

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    count = 0
    total = 0 
    for line in reader:
        total += line['age']
        print  (line)
        count += 1
        
    print (f"average is {total/(count-1)}")