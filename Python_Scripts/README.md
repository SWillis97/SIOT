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

## Master_Code_Standalone
As mentioned above, this master code is used to generate the cheapest option over 20 years. This is the optimiation to use if a local community is supporting itselfas they are paying for it.

## Master_Code_Looped
This master code should be used if looking for outside investment as it also considers returning their money, and profits, to them, whilst giving the community free sustainable energy

### Outputs
Running either master code will generate the following outputs:

_wind_turbine_profile_: the wind turbine profile which creates the optimal BESS WTG combination

_capacity_: The Capacity, in kWh, which creates the optimal BESS WTG combination

_optimal_Cost_: the cost of installing and maintaining the system over the 20 year period
