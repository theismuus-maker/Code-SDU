
import time

class stepper_motor():
    def __init__(self,pins=(0,1,2,3),freq=18000,pwm = 0.15) -> None:
        self.pins = pins
        self.freq = freq
        self.pwm = pwm 

        full_1 = [pwm,pwm,0,0]
        full_2 = [0,pwm,pwm,0]
        full_3 = [0,0,pwm,pwm]
        full_4 = [pwm,0,0,pwm]
        
        half_1 = [pwm,0,0,0]
        half_2 = [pwm,pwm,0,0]
        half_3 = [0,pwm,0,0]
        half_4 = [0,pwm,pwm,0]
        half_5 = [0,0,pwm,0]
        half_6 = [0,0,pwm,pwm]
        half_7 = [0,0,0,pwm]
        half_8 = [pwm,0,0,pwm]
        
        
        
        full_step = [full_1,full_2,full_3,full_4]
        half_step = [half_1,half_2,half_3,half_4,half_5,half_6,half_7,half_8]
        self.modes = {"full": full_step ,"half" : half_step}


    def step(self,step_mode = "full",direction = "forward"):
        self.step_mode = step_mode
        self.direction = direction
        

        


        if direction == "forward":
            for i in self.modes[step_mode]:
                print (i)
        elif direction == "backward" :
            for i in reversed(self.modes[step_mode]):
                print (i)
        else: 
            print ("Choose a valid direction")