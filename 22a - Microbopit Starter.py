# Micro:Bop Starter
# Mr. Scott
# Dec 14, 2023
# A bit of starter code for the bop-it game option

import microbit, time, random

choices = ["A", "B", "S"]  #would add more options
target_action = random.choice(choices)

#Main Loop
while True:
    microbit.display.show(target_action)
    
    #CHECKING FOR A USER ACTION
    #1. Check for a shake:
    motion = microbit.accelerometer.get_z()
    if motion > 1300 or motion < -1300:
        print("SHAKE")
        time.sleep(0.5) # no "shake detect" buffer time
        if target_action == "S":
            # user was correct. Display icon/animation showing it was right
            print("CORRECT")
            target_action = random.choice(choices)
        else:
            print("INCORRECT - game over")
    #2. Check for Button A
    #3. Check for Button B
    time.sleep(0.1)
    
    
    
    