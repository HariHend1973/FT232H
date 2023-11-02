# Test writing BME280 readings to a spreadsheet

import time
import sys
import board
from adafruit_bme280 import basic as adafruit_bme280
from datetime import datetime

# Set up sensor
i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)


while True:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    with open('/home/hari/FT232H/bme280.txt', 'a') as sys.stdout:
        #print(bme280.temperature, bme280.relative_humidity, bme280.pressure)
        print(' {} Temp: {:04.2f} Hum: {:04.2f} Press: {:04.2f} Alt: {:04.0f}'.format(dt_string , bme280.temperature, bme280.relative_humidity, bme280.pressure, bme280.altitude))
    time.sleep(3)

