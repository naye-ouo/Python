from machine import Pin, PWM
from time import sleep

# LED Port define
#FLASH_LED = 4

led_F = PWM(Pin(4), freq = 1000)
i = 0

while True:
    for i in range(0, 1024):
        led_F.duty(i)
        sleep(0.001)
    for i in range(1023, -1, -1):
        led_F.duty(i)
        sleep(0.001)
