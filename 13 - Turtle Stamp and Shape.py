# A couple of Turtle extras
# Mr. Scott
# Nov 23, 2023
# Icon, Stamp, etc...

import turtle

window = turtle.Screen()
roman = turtle.Turtle()

# setting up some turtle attributes
roman.speed(30)
roman.color("purple")
roman.pensize(3)
roman.shape("classic")  #turtle
roman.penup()  #.up()   don't draw when moving

def hollow_c():
    #draw a block letter c, starting from lower-left
    long = 100
    short = 15
    medium = long - short
    
    #solution
    roman.left(90)
    roman.fd(short)
    roman.left(90)
    for i in range(3):
        roman.fd(medium)
        roman.right(90)
    roman.left(180)
    roman.fd(short)
    roman.left(90)
    roman.fd(long)
    roman.left(90)
    roman.fd(long + short)
    roman.left(90)
    roman.fd(long)
    
roman.down()
print(roman.xcor(), roman.ycor())


for i in range(8):
    hollow_c()
    roman.left(45)





# turtle.tracer(False)  #just draw the final image
# some movement code
# def single_line():
#     for d in range(15,55,5):  #[5, 10, 15, ..., 45]
#         roman.fd(d)
#         roman.stamp()
#     roman.goto(0,0)
# 
# for i in range(180):
#     single_line()
#     roman.left(2)

window.exitonclick()




