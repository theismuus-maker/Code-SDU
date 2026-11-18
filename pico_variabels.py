from machine import Pin
import time

# so this example checks how long the button is pressed down 
button = Pin(15,Pin.IN, Pin.PULL_DOWN)

# this starts the timer at 0
timer = 0

while True:
    time.sleep(1) # we sleep this a secound so the timer only goes up every secound 

    # if the button is pressed we add 1 to the timer 
    if button.value() == 1:
        timer = timer + 1
        # this will happend only happen if the button is pressed

    print(timer)