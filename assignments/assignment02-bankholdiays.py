#r assignment02-bankholidays.py
# Author Cathal Redmond
# 1 Oct 2025

# references : https://www.geeksforgeeks.org/python/how-to-add-new-line-in-dictionary-in-python/


import requests  
import json

url =" https://www.gov.uk/bank-holidays.json" 
response = requests.get(url) 
dict = response.json() 

 print(json.dumps(dict['northern-ireland']['events'], indent = 4))  ## This is working code, dont fuck with it! 

#print ( ['events'] for ['northern-ireland'] in dict if(['date'] == ['2027-05-31'])else: () )
#print (obj for obj in dict if(obj['type'] == 1))