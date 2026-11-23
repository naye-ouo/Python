from machine import Pin, PWM
import time

BUTTON_PIN = 0
LED_PIN = 4
PRESSED_VALUE = 0
ON_VALUE = 1
OFF_VALUE = 0

button = Pin(BUTTON_PIN,Pin.IN, Pin.PULL_UP)
led = Pin(LED_PIN, Pin.OUT, value=OFF_VALUE)
pwm = PWM(Pin(LED_PIN), freq = 1000, duty = 0)

while True:
    if button.value() == PRESSED_VALUE:
        led.value(ON_VALUE)
        pwm.duty(100)
    else:
        led.value(OFF_VALUE)
        time.sleep(0.05)
        pwm.duty(0)