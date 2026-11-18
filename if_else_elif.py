from machine import Pin, ADC
import time

pot = ADC(Pin(26)) 

# set up conversion constant and start a last volume variable at 0
last_volume = 0
const = 100 / 65535

'''
change this string to choose which method is used.
a uses if, else and elif in an inefficient method.
b uses a more efficient method.
'''
method = "b"

if method == "a":

    while True:
        # Read the value from the potentiometer
        current_volume = int(pot.read_u16() * const)

        # Check if the volume level has changed enough to print new line
        if ((current_volume - last_volume) >= 2) or ((current_volume - last_volume) <= -2):
            
            # use if, elif, else logic to print a volume bar based on the current volume
            if 0 <= current_volume < 10:
                print("__________", current_volume)

            elif 10 <= current_volume < 20:
                print("█_________", current_volume)

            elif 20 <= current_volume < 30:
                print("██________", current_volume)

            elif 30 <= current_volume < 40:
                print("███_______", current_volume)

            elif 40 <= current_volume < 50:
                print("████______", current_volume)

            elif 50 <= current_volume < 60:
                print("█████_____", current_volume)

            elif 60 <= current_volume < 70:
                print("██████____", current_volume)

            elif 70 <= current_volume < 80:
                print("███████___", current_volume)

            elif 80 <= current_volume < 90:
                print("████████__", current_volume)

            elif 90 <= current_volume < 100:
                print("█████████_", current_volume)
                
            else:
                print("██████████", 100)                
            
            # Update last volume
            last_volume = current_volume

        time.sleep(0.05)  # Small delay to prevent excessive reading



if method == "b":

    while True:
        # Read the value from the potentiometer
        current_volume = int(pot.read_u16() * const)

        # Check if the volume level has changed enough to move to a new 10% increment
        if ((current_volume - last_volume) >= 2) or ((current_volume - last_volume) <= -2):
            
            # This is a different way to create the volume bar based on volume
            num_bars = int(current_volume / 10)
            print("█" * num_bars + "_" * (10 - num_bars), current_volume)
            
            # update last volume
            last_volume = current_volume


        time.sleep(0.05)  # Small delay to prevent excessive reading

