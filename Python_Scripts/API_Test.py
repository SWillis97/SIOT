import gspread
from oauth2client.service_account import ServiceAccountCredentials
"""
File used to check if the API is connecting to the google sheets file.
"""

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Days_Combined").sheet1

#Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
