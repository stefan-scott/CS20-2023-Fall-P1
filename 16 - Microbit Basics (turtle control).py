# Microbit Basics
# Mr. Scott
# Nov 30, 2023

import microbit, time, turtle

w = turtle.Screen()
t = turtle.Turtle()

while True:
    x = microbit.accelerometer.get_x()   #left-right tilt 1024    0    +1024
    t.fd(10)                        #   LEFT  -300  FLAT  300    RIGHT
    if x > 300:
        print("RIGHT")
        t.right(12)
    elif x < -300:
        print("LEFT")
        t.left(12)
    else:
        print("FLAT")
    

# # DISPLAY TEXT (Show or scroll)
# for letter in "SASK":   #SHOW
#     microbit.display.show(letter)
#     time.sleep(0.5)
#     
# # Scroll
# microbit.display.scroll("abcd")
    