from machine import Pin, PWM
#this sets an pwm to pin 16
# all pins can out put a pwm 
pwm_pin = PWM(Pin(16))
max = 65535

#how many times a secound a duty cycle is
pwm_pin.freq(1000)

# this will chance the out put from the pin to a specifik volt. 
# we set the max to 65535 wich is ecuvalent to 3.3 valut
# then we can mulitply max by a number in the range of 0-1 to get a procentage of the volt we wish for
while True:
    PWM_value = int(0.5*max)
     
    pwm_pin.duty_u16(PWM_value)