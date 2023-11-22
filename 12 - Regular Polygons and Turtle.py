# Turtle and Regular Polygons
# Mr. Scott
# Nov 22, 2023
# Using turtles and function to draw geometric shapes

# set up Turtle, Screen, etc...
import turtle
wn = turtle.Screen()
harold = turtle.Turtle()
harold.speed(30)
harold.pensize(3)

# Polygon Function Definitions
def triangle(side_length):
    # uses the turtle to draw a triangle shape, using
    # side_length to determine the overall size
    for i in range(3):  #repeat 3   [0,1,2]
        harold.fd(side_length)
        harold.left(120)

def square(side_length):
    # same as above, but 4 sides.
    for i in range(4):
        harold.fd(side_length)
        harold.left(90)

def pentagon(side_length):
    # same as above, but 5 sides
    for i in range(5):
        harold.fd(side_length)
        harold.left(72)

def r_poly(x, y, s):
    # draw a regular polygon at a given position
    # x → x-coordinate to draw from
    # y → 26 y-coordinate to draw from
    # s → number of sides for the polygon
    harold.up()
    harold.goto(x,y)  #move w/o drawing
    harold.down()
    for i in range(s):
        harold.fd(300/s)
        angle = 360/s
        harold.left(angle)

# Call the functions here
r_poly(-300,0,5)
r_poly(-100,0,7)
r_poly(100,0,11)
r_poly(300,0,100)

# pentagon(200)



# for i in range(120):
#     square(150)
#     harold.left(3)

# for i in range(10,300,10):  #[10,11, 12, 13, ...299
#     triangle(i)



