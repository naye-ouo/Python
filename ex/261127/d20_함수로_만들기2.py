from machine import Pin
import time

LED_PIN = 4
BUTTON_PIN = 0
ON_VALUE = 1
OFF_VALUE = 0
PRESSED_VALUE = 0
PERIOD = 0.01 #0.01초
levels = [0.1, 0.3, 0.6, 0.9]
index = 0
was_pressed = False

led = Pin(LED_PIN, Pin.OUT, value=OFF_VALUE)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

def get_ratio(index):
    ratio = levels[index]
    return ratio


def ratio_control(ratio):
    #global on_time, off_time
    ###############################
    # Ratio 제어 부분
    ###############################
    ratio = levels[index]
    on_time = PERIOD * ratio
    off_time = PERIOD - on_time
    return on_time, off_time
    
    
def led_control(on_time, off_time):
    #global on_time, off_time
    ###############################
    # LED On Off 제어 부분
    ###############################
    led.value(ON_VALUE)
    time.sleep(on_time)
    led.value(OFF_VALUE)
    time.sleep(off_time)
    
def button_control():
    global was_pressed, index
    if button.value() == PRESSED_VALUE:
        if was_pressed == False :
            index = index + 1
            if index > 3:
                index = 0
                
    if button.value() == PRESSED_VALUE:
        was_pressed = True
    else :
        was_pressed = False

while True:
    button_control()
    a = get_ratio(index)
    #a, b = ratio_control()
    #led_control(a, b)
    led_control(*ratio_control(a))
