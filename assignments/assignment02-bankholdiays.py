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
print("\nNorthern Ireland List:\n")
NIlist = []
for titles in NIevents:
    y=list(titles.values())[0],list(titles.values())[1]
    NIlist.append(y)
print(NIlist)
with open("Northern-Ireland Bank Holidays.txt","w") as output:
    output.write(str(NIlist))
'''
Scotlandevents = bankholidays['scotland'].get('events')
print("\nScotland List:\n")
ScotlandList =[]
for titles in Scotlandevents:
    print(list(titles.values())[0],":",list(titles.values())[1])
    


EnglandAndWalesevents = bankholidays['england-and-wales'].get('events')
print("\nEngland and Wales List:\n")
EnglandAndWalesList = []
for titles in EnglandAndWalesevents:
    print(list(titles.values())[0],":",list(titles.values())[1])
    
'''

#for dates in titles:
    #list(dates.keys())[0]
    #print(dates)

#titles = events.items()
#print(titles)

#dict = r.json() 
#bankholidays = json.dumps(dict['northern-ireland']['events'], indent = 4)
#bankholidays = json.dumps(dict)
#print(type(bankholidays))

#print(dict['northern-ireland']['events'])

#print(json.dumps(dict['northern-ireland']['events']['title'], indent = 4))  # This is working code, dont mess with it! 

#print(json.dumps(dict['events'] for ['northern-ireland'] in dict if(['date'] == ['2027-05-31'])else: () ))
#print(obj for obj in dict if(obj['type'] == 1))