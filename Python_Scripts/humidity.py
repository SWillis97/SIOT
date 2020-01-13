import Adafruit_DHT as ada
import time

#Checking run time for interrupts in combined file 
start_time = time.time()

#Set Sensor Type : current model is DHT11 3 pin, inbuilt 10k ohm resistor 
sensor = ada.DHT11

#Set GPIO sensor is connected to 
gpio = 17

#Use read_retry method. This will retry up to 15 times to 
#get a sensor reading (2 seconds between each retry)
humidity, temperature = ada.read_retry(sensor, gpio)

#Reading the DHT11 is sensitive to timings and occasionally the Pi might 
#fail to get a valid reading. Checking the readings are valid.
if humidity is not None and temperature is not None:
	print('Temperature={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
else:
	print('Failed to get a reading. Try again!')

print("--- %s seconds ---" % (time.time() - start_time))
