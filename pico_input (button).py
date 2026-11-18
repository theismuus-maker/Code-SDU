from machine import Pin
import time

button = Pin(15, Pin.IN, Pin.PULL_DOWN) # set up pin 15 as an input with a pull-down resistor
led = Pin(16,Pin.OUT)


while True:
    #if the button is pressed then turn the led on
    if button.value() == 1:
        led.value(1)
        # if it is not pressed it turns off
    else:
        led.value(0)