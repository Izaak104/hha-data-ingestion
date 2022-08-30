import pandas as pd 
import openpyxl
import requests
import json
#pip installed modules then imported them

tab1 = pd.read_excel('CPS MDCR ENROLL AB 33-39 2020 2.xlsx')
tab2 = pd.read_excel('CPS MDCR ENROLL AB 33-39 2020 2.xlsx', sheet_name= 1)

print(tab1,'\n', tab2)

#using pandas command to name tabs as tab1 and tab2
#in tab2, another variable was used to identify the sheet

json_data=requests.get('https://data.cms.gov/data-api/v1/dataset/60ccbf1c-d3f5-4354-86a3-465711d81c5a/data')

#apiDataset
apiDataset=json_data.json()

print(apiDataset)

