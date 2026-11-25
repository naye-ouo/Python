from machine import Pin
import time

LED_PIN = 4
BUTTON_PIN = 0
ON_VALUE = 1
OFF_VALUE = 0
PRESSED_VALUE = 0
PERIOD = 0.01 #0.01초
levels = [0, 0.1, 0.3, 0.6, 0.9]
index = 0
was_pressed = False

led = Pin(LED_PIN, Pin.OUT, value=OFF_VALUE)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

def ratio_controler():
    global RATIO, on_time, off_time
    RATIO = levels[index]
    on_time = PERIOD * RATIO # 0.01 * 0
    off_time = PERIOD - on_time # 0.01 - 0

def led_controler():
    global RATIO, ON_VALUE, OFF_VALUE, on_time, off_time
    if RATIO > 0:
        led.value(ON_VALUE) #1
        time.sleep(on_time) #0.01
        led.value(OFF_VALUE) #0
        time.sleep(off_time) #0.01

while True:
    if button.value() == PRESSED_VALUE:
        if not was_pressed:
            index = index + 1
            if index > 4:
                index = 0
    was_pressed = button.value() == PRESSED_VALUE
    
    ratio_controler()
    led_controler()