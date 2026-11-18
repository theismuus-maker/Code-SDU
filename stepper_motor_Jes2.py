
from machine import Pin, PWM
from time import sleep, ticks_ms, ticks_diff


class stepper_motor:
    def __init__(self, pins=(0, 1, 2, 3), freq=18000, pwm=0.15):
        self.pins = pins
        self.freq = freq
        self.pwm = pwm

        # Opret PWM-objekter
        self.outputs = []

        for i in pins:
            self.outputs.append(PWM(Pin(i, Pin.OUT)))

        # Indstil PWM-frekvensen
        for i in self.outputs:
            i.freq(self.freq)

        # Full-step sekvens
        self.full_step_sequence = [
            [pwm, pwm, 0, 0],
            [0, pwm, pwm, 0],
            [0, 0, pwm, pwm],
            [pwm, 0, 0, pwm]
        ]

        # Half-step sekvens
        self.half_step_sequence = [
            [pwm, 0, 0, 0],
            [pwm, pwm, 0, 0],
            [0, pwm, 0, 0],
            [0, pwm, pwm, 0],
            [0, 0, pwm, 0],
            [0, 0, pwm, pwm],
            [0, 0, 0, pwm],
            [pwm, 0, 0, pwm]
        ]

        # Start med slukkede spoler
        self.stop()

    # Send PWM-værdier til de fire spoler
    def set_step(self, step):
        for i in range(4):
            self.outputs[i].duty_u16(int(step[i] * 65535))

    # Sluk motorens spoler
    def stop(self):
        for i in self.outputs:
            i.duty_u16(0)

    # Roter et bestemt antal trin
    def rotate(self, steps, delay, mode):
        if mode == "full":
            sequence = self.full_step_sequence
        elif mode == "half":
            sequence = self.half_step_sequence
        else:
            print("Choose a valid step sequence")
            return

        try:
            for i in range(abs(steps)):
                step = sequence[i % len(sequence)]
                self.set_step(step)
                sleep(delay)
        finally:
            self.stop()


# Opret motoren
motor = stepper_motor()

# Opret knappen
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Vælg motorens indstillinger
mode = "full"
delay = 0.01

if mode == "full":
    sequence = motor.full_step_sequence
elif mode == "half":
    sequence = motor.half_step_sequence
else:
    raise ValueError("Choose a valid step sequence")

# Startværdier
running = False
button_previous = 0
i = 0
last_press = -200

try:
    while True:
        button_now = button.value()

        # Registrer et nyt knaptryk
        if button_now == 1 and button_previous == 0:
            now = ticks_ms()

            if ticks_diff(now, last_press) >= 200:
                running = not running
                last_press = now

                if not running:
                    motor.stop()

        button_previous = button_now

        # Motorstyring
        if running:
            step = sequence[i % len(sequence)]
            motor.set_step(step)
            sleep(delay)
            i += 1
        else:
            sleep(0.001)

finally:
    motor.stop()
