# LED GPIO test
import board
import digitalio
import time

led_aa = digitalio.DigitalInOut(board.C0)
led_aa.direction = digitalio.Direction.OUTPUT
led_bb = digitalio.DigitalInOut(board.D7)
led_bb.direction = digitalio.Direction.OUTPUT

while True:
    led_aa.value = True
    led_bb.value = False
    time.sleep(0.5)
    led_aa.value = False
    led_bb.value = True
    time.sleep(0.5)
    
