from machine import Pin
import time 

button = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        #start stepper motor (jeg tror vi kan sætte _init__ her)
    else:
        #stop (stop funktionen vi har lavet)
