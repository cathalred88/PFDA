#csv_reader_ver3b.py
# Author Cathal Redmond
# 01 Oct 2025 

import csv
FILENAME = "data.csv"
DATADIR = "../my-work/" # i know this just brings my up a level and then back into same folder, but it allows for the excercise. 

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0 
    for line in reader:
        if not linecount: #first row is header row (because it returns 0 which is read as false)
            pass
        else: # all subsequent rows 
            total += (line[1])
        linecount += 1
        
    print (f"average is {total/(linecount-1)}")