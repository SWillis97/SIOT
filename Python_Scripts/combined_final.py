from __future__ import print_function
import RPi.GPIO as GPIO
import time
import Adafruit_DHT as ada
import multiprocessing as multip
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from oauth2client.service_account import ServiceAccountCredentials as SAC
import pandas as pd
import os

#Setting  pins for the force sensitive resistor (fsr)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

#Setting GPIO and sensor type for Adafruit program
sensor = ada.DHT11
gpio = 17

#Function to make new csv files
def write_list_to_file(guest_list, filename):
    """Write the list to csv file."""

    with open(filename, "w") as outfile:
        for entries in guest_list:
            outfile.write(entries)
            outfile.write("\n")

#Initiating file if it does not exist after shutdown
file_check = os.path.isfile('./Logging_final.csv')
print(file_check)
if file_check:
    file = open("./Logging_final.csv","a")
    print("File already exists")
else:
    New_List = ['Humidity,Temperature,Footsteps,Date/Time']
    write_list_to_file(New_List,"Logging_final.csv")
    file = open("./Logging_final.csv","a")

#Setting up function to check the force sensitive resistor
def fsr(total_time):
	step_count = 0
	prev_input = 0
	end = datetime.now() + timedelta(seconds=5-total_time)

	#Ensure it runs until told to stop running
	while True:
		input = GPIO.input(4)

		#Ensure it only runs for the sample time
		if datetime.now() < end:
			if ((not prev_input) and input):
				#Increase step_count
				step_count += 1

			#Update prev_input so that only one footstep
			#can be checked at a time
			prev_input = input

			#Short wait before next sample
			time.sleep(0.10)

		else:
			return [step_count]

#Function to check the humidity and temperature
def humid_temp():
	humidity, temperature = ada.read_retry(sensor,gpio)
	return [humidity,temperature]

# a tick to alter which function is being run
tick = 1

try:
	while True:
		if tick == 1:
			#This function takes a varying time from 0.5 seconds to 3 seconds.
			#In order for a consistent sample rate this provides a limit for fsr
			start_time = time.time()
			[h,t] = humid_temp()
			total_time = time.time() - start_time
			tick = 0

		elif tick == 0:
			[s] = fsr(total_time)
			now = datetime.now()
			#Get the time and date of this data point
			date_now = now.strftime("%d/%m/%y %H:%M:%S")
			csvlist = [h,t,s,date_now]
			print(csvlist)

			#Update Logging.csv
			file.write(str(h)+","+str(t)+","+str(s)+","+str(date_now)+"\n")
			tick = 1
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
