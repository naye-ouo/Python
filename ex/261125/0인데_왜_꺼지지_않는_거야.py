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

while True:
    if button.value() == PRESSED_VALUE:
        if not was_pressed:
            index = index + 1
            if index > 4:
                index = 0
    was_pressed = button.value() == PRESSED_VALUE
    RATIO = levels[index]
    on_time = PERIOD * RATIO # 0.01 * 0
    off_time = PERIOD - on_time # 0.01 - 0
    
    led.value(ON_VALUE) #1
    time.sleep(on_time) #0
    led.value(OFF_VALUE) #0
    time.sleep(off_time) #0
    # 여기서 1로 켜졌어 근데 time.sleep 대기 시간이
    # 없으니까 바로 넘어가 OFF_VALUE 에서 껐어
    # 근데 그러고 나서 또 대기 시간이 없어서 바로 켜
    # 사실 기계는 켜졌다 꺼졌다 엄청 빨리 일을 하고 있는데
    # 억울하게도 인간의 눈에는 계속 켜진 거 처럼 보여서
    # 얘 왜 안꺼지냐? 이러고 있는 거임...
    
# 원래 0이라면 꺼져야 하는 거 아닌가?
# 근데 왜 계속 켜져 있음?
# 그건 이 몸의 잔상이다..