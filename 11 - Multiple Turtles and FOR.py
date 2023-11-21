# Multiple Turtles and For Loops
# Mr. Scott
# Nov 21, 2023
# Look at multiple turtle instances, and driving them with loops

import turtle

wn = turtle.Screen()  #creates the window (and the canvas)

francis = turtle.Turtle()
francis.pensize(2)
francis.color("orange")

martha = turtle.Turtle()
martha.pensize(4)
martha.color("purple")

turtle_list = [] #empty list, to store turtles in
color_list = ["red", "blue", "orange", "green"]

turtle_list.append(francis) #add our Francis turtle onto the end of the list
turtle_list.append(martha) #same, but for Martha
turtle_list.append(turtle.Turtle()) #make a third generic turtle

# Now, loop through our list and give some instructions.
turtle_list[0].left(120)
turtle_list[1].left(240)

color_index = 0
for distance in range(50, 10, -1):  #[50, 48, 46, ..., 14, 12]
    for t in turtle_list:
        t.color(color_list[color_index])
        t.speed(0)
        t.forward(distance)
        t.right(20)
    #update the color for next time:
    color_index = color_index + 1
    if color_index > 3:
        color_index = 0




 
# my_list = ["Joe", "Amy", "Brad", "Zuki"]
# #            0      1      2       3


 
 
 
 
# #PROGRAM ONE 
# #first, move francis
# square_size = 100
# francis.forward(square_size)
# francis.left(90)
# francis.forward(square_size)
# francis.left(90)
# francis.forward(square_size)
# francis.left(90)
# francis.forward(square_size)
# francis.left(90)
# 
# #Martha's turn - first, reposition
# martha.penup() #lift the pen   .up()
# martha.back(200)
# martha.pendown()  #.down()
# 
# #Martha - draw an L-shape
# martha.lt(45)  #left-turn
# martha.fd(100)
# martha.lt(90)
# martha.fd(200)













