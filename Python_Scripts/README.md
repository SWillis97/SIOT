# Python Scripts
This README file outlines the use of the .py scripts within this folder, and which packages need to be downloaded to run them. For  instructions on how to create the circuits used please refer to FILENAME

### client_secret
`client_secret.json` must be in the same directory as the file `shutdown.py` in order for the google drive API to work

### Libraries
Please install the following libraries if they have not been installed previously.

Adafruit_DHT: Follow instructions on https://github.com/adafruit/Adafruit_Python_DHT

Numpy: `pip install numpy`

Pandas: `pip install pandas`

DateTime: `pip install DateTime`

multiproccessing: `pip install multiprocess`

googleapiclient: Follow instructions on https://github.com/googleapis/google-api-python-client

oauth2client: `pip install oauth2client`

gspread: `pip install gspread`

pygsheets: `pip install pygsheets`

### Test Functions
These functions are only to be used whilst setting up the circuitry and system to check it works and troubleshoot any problems.

`API_Test.py`: Used to check if the API is working and pulls data from google drive.

`fsr.py`: File used to check if the force sensitive resistor is working. If it detects a footstep it prints 'Under Pressure'.

`humidity.py`: Uses the `Adafruit_DHT` Library to run a DHT11 humidity and temperature sensor.

`Update_Checker.py`: Used to check your data is in the correct format for the google sheet.

## Main Functions
These functions are the main python scripts and are used to record and update the data for the use of the MatLab script later on

`combined_final.py`: This file operates the sensing for the project. The force sensitive resitor senses all of the time, with interrupts each minute to run the DHT11 sensor and the date and time.

`shutdown.py`: This file is run after the day's data is recorded and before shutting the raspberry pi down for the night. This is manually run currently and processes the day's data before updating the google spreadsheets file. After this it delets the used data.
