from googleapiclient.discovery import build
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pygsheets
import numpy as np
import pandas as pd
import os
import csv

#Set authorisation credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

#Define the location and name of the spreadsheet the API is targeting 
SPREADSHEET_ID = '1HLoDasR_YAcyZkQLkCRk67cBzrFpOnLatv81vD_qb3A'
worksheet_name = 'Days_Combined'

#
path_to_csv = 'Days_Combined.csv'
file = open("/home/pi/SIOT/Days_Combined.csv","a")

def write_list_to_file(guest_list, filename):
    """Write the list to csv file."""

    with open(filename, "w") as outfile:
        for entries in guest_list:
            outfile.write(entries)
            outfile.write("\n")

def update_sheet():
    """
    Function used to create the temporary list which gets appended to the google 
    sheets document. Runs the function write_list_to_file within it.
    """
    
    #Open new csv file
    whole_csv = pd.read_csv('Logging_final.csv', delimiter=',')

    #Rename .csv file columns to ensure no errors
    whole_csv.columns = ['humidity', 'temperature', 'footsteps', 'date&time']

    #call the individual lists from file
    hlist = whole_csv['humidity']
    tlist = whole_csv['temperature']
    plist = whole_csv['footsteps']

    havg = round(np.average(hlist),5)
    tavg = round(np.average(tlist),5)
    pavg = round(np.average(plist),5)

    Day_List = [str(havg)+','+str(tavg)+','+str(pavg)]
    write_list_to_file(Day_List,"Days_Combined.csv")

def find_sheet_id_by_name(sheet_name):
    # Get sheet id
    sheets_with_properties = API \
        .spreadsheets() \
        .get(spreadsheetId=SPREADSHEET_ID, fields='sheets.properties') \
        .execute() \
        .get('sheets')

    for sheet in sheets_with_properties:
        if 'title' in sheet['properties'].keys():
            if sheet['properties']['title'] == sheet_name:
                return sheet['properties']['sheetId']

sheet = client.open('Days_Combined').sheet1  
list_hashes = sheet.get_all_records()
print(list_hashes)

def push_csv_to_gsheet(csv_path, sheet_id):
    """ 
    Function used to take the new csv file and push it to the google sheets file.
    """
    gc = pygsheets.authorize(service_file='client_secret.json') #authorization
    worksheet = gc.open('Days_Combined').sheet1 #opens the first sheet in "Sign Up"

    cells = worksheet.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
    end_row = len(cells) # THIS FINDS THE INDEX NUMBER OF AN EMPTY CELL

    with open(csv_path, 'r') as csv_file:
        csvContents = csv_file.read()
    body = {
        'requests': [{
            'pasteData': {
                "coordinate": {
                    "sheetId": sheet_id,
                    "rowIndex": end_row,  # means it appends onto an empty row
                    "columnIndex": "0", 
                 },
                "data": csvContents,
                    "type": 'PASTE_NORMAL',
                    "delimiter": ',',
            }
        }]
    }
    request = API.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body)
    response = request.execute()
    return response

#Reformat the day's data into useful data
update_sheet()

API = build('sheets', 'v4', credentials=creds)

push_csv_to_gsheet(
        csv_path=path_to_csv,
        sheet_id=find_sheet_id_by_name(worksheet_name)
)

#Delete track file after upload - UNCOMMENT IF WANT TO DELETE FILE
os.unlink('Days_Combined.csv')
os.unlink('Logging_final.csv')
print('file removed')
