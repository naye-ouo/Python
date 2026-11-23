from machine import Pin, PWM
import time

BUTTON_PIN = 0
LED_PIN = 4
PRESSED_VALUE = 0
DUTY_ON = 205
DUTY_OFF = 0

button = Pin(BUTTON_PIN,Pin.IN, Pin.PULL_UP)
led = PWM(LED_PIN, freq = 1000, duty = DUTY_OFF)


while True:
    if button.value() == PRESSED_VALUE:
        led.duty(DUTY_ON)
    else:
        led.duty(DUTY_OFF)
        time.sleep(0.05)