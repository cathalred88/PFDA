#read_json.py
# Author Andrew Beatty (compiled by Cathal Redmond)
# 1 Oct 2025

import requests  
import json

url =" https://www.gov.uk/bank-holidays.json" 
response = requests.get(url) 
bankholidays = response.json() 

print(bankholidays['northern-ireland']['events'][0]) 

'''
with open('bankholidays_norther-ireland_first_row_only.json', 'w') as json_file:
    json.dump(bankholidays['northern-ireland']['events'], json_file)  ## remember you can press Alt, Shift & F when this .json file opens to view it tabulated nicely. 
'''