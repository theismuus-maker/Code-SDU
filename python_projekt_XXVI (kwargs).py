#** kwargs = parameter that will pack all arguments into dictionary
# useful so that a funcktion can accept a varying amout of keyword arguments 
from time import sleep

def hello (**kwargs):
    #print("Hello " +kwargs["first"]+ " " +kwargs["last"])
    print("Hello ",end=" ")
    for key, value in kwargs.items():
        print(value,end=" ")





def moter (**motor_setting):
    print("Motor settting: ", end = " ")
    for key, value in motor_setting.items():
        print(value, end=" ")

moter(pwm_pct = 1, direction = "forward", step_mode = "full")

hello(title="The goat",first="Theis", last="Muusmann", middle="Seje")
