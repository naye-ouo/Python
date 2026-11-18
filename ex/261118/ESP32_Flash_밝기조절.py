from machine import Pin
import time

# LED Port define
RED_LED = 33
FLASH_LED = 4

led_F = Pin(FLASH_LED, Pin.OUT, value= 0)

for led_cnt in range(1000):
    led_F.value(1)
    time.sleep(0.001)
    
    led_F.value(0)
    time.sleep(0.009)