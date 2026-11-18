from machine import Pin, ADC, PWM
import time

pot_pin = ADC(Pin(26))
pwm_pin = PWM(Pin(16))

pwm_pin.freq(1000)


while True:
    # reads the raw analog input value of the adc from 0-65535
    # storing that value in pot_value
    pot_value = pot_pin.read_u16()
    #then we out_put it in the pwm_pin 
    pwm_pin.duty_u16(pot_value)

    #uncommet the line below to print voltage instead of the pot_value = pot_value *3.3 /65525

    print(pot_value)
    time.sleep(0.05)