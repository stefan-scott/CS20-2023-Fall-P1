# First Turtle Program
# Mr. Scott
# Nov 20, 2023
# How to import and use the turtle graphics library
# NOTE: do NOT save your file as turtle.py

import turtle   #looks for the library (turtle.py)


moves = int(input("How many moves? "))

# turtle boilerplate code
window = turtle.Screen()   # looks in the turtle library for a function called Screen()
window.bgcolor("PaleGoldenRod")     # use a color string for background color selection

alex = turtle.Turtle()     # creates a turtle named Alex
alex.color("MidnightBlue")
alex.pensize(5)
alex.speed(0)   # 0 → maximum speed

for i in range(moves):  #[0,1,2,3,4,5,6,7...,moves-1]
    alex.forward(i)
    alex.right(30)


window.exitonclick()   # wait for the user to click on the canvas








# PROGRAM ONE
# give some instructions to our turtle
# alex.forward(150)   #move forward 150 units (pixels)
# alex.left(90)       #turn left 90 degrees
# alex.forward(75)  




