from machine import Pin
import time

LED_PIN = 4
ON_VALUE = 1
OFF_VALUE = 0
PERIOD = 0.01
#ON_OFF의 전체 시간
RATIO = 0.07
#전체 시간 중 불이 켜져 있는 시간의 비율
#defalt 0.5 / MAX 1
#값을 조절하면 밝기 조절이 됨
ON_LED = PERIOD * RATIO
OFF_LED = PERIOD - ON_LED

led = Pin(LED_PIN, Pin.OUT, value=OFF_VALUE)

while True:
    led.value(ON_VALUE)
    time.sleep(ON_LED)
    led.value(OFF_VALUE) 
    time.sleep(OFF_LED)