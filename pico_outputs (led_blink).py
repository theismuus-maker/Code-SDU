from machine import Pin #lets us use certain comands
import time # lets os use the sleep coman

# a pico will read the code from top to bottom step by step

led = Pin("LED", Pin.OUT) # set up pin 16 which is connected to the LED

# the first part of the bracket tells the pico wich pin we are going to use. 
# By typeing "LED" we tell the pico to select inbuilt led in the pico.
# the secound part is if we want to use the pico as an input or an outout
# we store it in a variable 

while True: # will keep repat a line of code until it isent true
    led.value(1) # turns the led on. This gives the pico 3,3 v
    time.sleep(2)

    led.value(0) # turns the led off. This gives the pico 0 v
    time.sleep(2)
    