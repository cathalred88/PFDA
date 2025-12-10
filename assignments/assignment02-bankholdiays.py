#r assignment02-bankholidays.py
# Author Cathal Redmond
# 1 Oct 2025

# references : https://www.geeksforgeeks.org/python/how-to-add-new-line-in-dictionary-in-python/


import requests  
import json

# Request from Web
# this method downloads the file from the web new each time
url =" https://www.gov.uk/bank-holidays.json" 
r = requests.get(url) 

# Check the status of the request
# if the server sucessfully handles the request, this will respond with the value "200"
#print(r.status_code) 

#Alternatively, we can access the file locally: 
FILENAME = "bankholidays.json"
DATADIR = "../my-work/"
FULLPATH = DATADIR + FILENAME

# function to read the json into a Dict type object
with open (FULLPATH, "rt") as fp:
    bankholidays = json.load(fp)

#print the data from the dict
#print(bankholidays['northern-ireland']['events'])

# call the event titles that happen in Norther ireland from the lists
NIevents = bankholidays['northern-ireland'].get('events')
#print("\nNorthern Ireland List:\n")
NIlist = []
for titles in NIevents:
    y=list(titles.values())[0]
    NIlist.append(y)
#print(NIlist)
with open("Northern-Ireland Bank Holidays.txt","w") as output:
    output.write(str(NIlist))


#Scotland
Scotlandevents = bankholidays['scotland'].get('events')
#print("\nScotland List:\n")
ScotlandList =[]
for titles in Scotlandevents:
    y=list(titles.values())[0]
    ScotlandList.append(y)
#print(ScotlandList)
with open("Scotland Bank Holidays.txt","w") as output:
    output.write(str(ScotlandList))

#England and Wales
EnglandAndWalesevents = bankholidays['england-and-wales'].get('events')
#print("\nEngland and Wales List:\n")
EnglandAndWalesList = []
for titles in EnglandAndWalesevents:
    y=list(titles.values())[0]
    EnglandAndWalesList.append(y)
#print(EnglandAndWalesList)
with open("England and Wales Bank Holidays.txt","w") as output:
    output.write(str(EnglandAndWalesList))


# Now we just need a way to detect the unique individual elements from these 3 text files. 
# I will acomplish this using Sets # https://stackoverflow.com/questions/64422967/how-to-get-values-unique-to-each-list-for-three-lists
set_NI = set(NIlist)
set_Scot = set(ScotlandList)
set_EngWales = set(EnglandAndWalesList)

onlyinNI = set_NI - set_Scot - set_EngWales
onlyinScot = set_Scot - set_NI - set_EngWales
onlyinEng = set_EngWales - set_NI - set_Scot

print("\n","Only in Northern Ireland:", onlyinNI,"\n")
print("Only in Scotland:", onlyinScot,"\n")
print("Only in England:",onlyinEng,"\n")

# End of code
# Completed on 10 Dec 2025