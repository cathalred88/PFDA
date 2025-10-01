#csv_reader_ver2.py
# Author Cathal Redmond
# 01 Oct 2025 

import csv
FILENAME = "data.csv"
DATADIR = "../my-work/" # i know this just brings my up a level and then back into same folder, but it allows for the excercise. 

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        if not linecount: #first row is header row (because it returns 0 which is read as false)
            print(f"{line}\n---------------")
        else: # all subsequent rows 
            print (line)
        linecount += 1