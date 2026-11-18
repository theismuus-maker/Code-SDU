from machine import Pin, ADC 
import time

#set up pin 26 as an analog input
# 26, 27, 28 is the only adc pins
pot = ADC(Pin(26))

#constant to convert range to 0 to 3.3 v
conversion_factor = 3.3/65535
# converts the interval into 0-3.3 instead of the 0-65535

while True:
    # read analog input
    pot_voltage = pot.read_u16()*conversion_factor
    #

    print (pot_voltage)
    time.sleep(0.1)