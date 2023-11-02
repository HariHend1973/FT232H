# Test writing BME280 readings to a spreadsheet

import time
import board
from adafruit_bme280 import basic as adafruit_bme280
import datetime
from datetime import date
from openpyxl import load_workbook

# Set up sensor
i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# Load workbook and select sheet
wb = load_workbook('/home/ec/Python_Code/weather.xlsx')
sheet = wb['Sheet1']


while True:
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.relative_humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    today = date.today()
    now = datetime.datetime.now().time()
    # Append readings to spreadsheet
    row = (today, now, bme280.temperature, bme280.relative_humidity, bme280.pressure)
    sheet.append(row)
    wb.save('/home/ec/Python_Code/weather.xlsx')
    print("Readings saved in spreadsheet.")
    time.sleep(3)
