from machine import Pin
import time

# LED Port define
RED_LED = 33
FLASH_LED = 4

# LED Time Control
ON_LED = 0.001
OFF_LED = 0.009

#led = Pin(RED_LED, Pin.OUT, value = 1)
led_F = Pin(FLASH_LED, Pin.OUT, value= 0)

while True :
    led_F.value(1)
    time.sleep(ON_LED)
    led_F.value(0)
    time.sleep(OFF_LED)

    