#csv_reader.py
# Author Cathal Redmond
# 01 Oct 2025 

import csv
FILENAME = "data.csv"
DATADIR = "../my-work/" # i know this just brings my up a level and then back into same folder, but it allows for the excercise. 

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print (line)