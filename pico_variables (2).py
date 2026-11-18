from machine import Pin
import time 

#set up button and led

button = Pin(15,Pin.IN,Pin.PULL_DOWN)
led = Pin(16, Pin.OUT)

while True:
    b_state = button.value()


    if b_state == 1:
        led.value(1)

    else:
        led.value (0)


    print(b_state)
    time.sleep(0.01)