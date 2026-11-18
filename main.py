from traning import stepper_motor

motor = stepper_motor(pins=(0,1,2,3),freq=18000,pwm = 0.15)

motor.step(step_mode="full", direction = "forward")
