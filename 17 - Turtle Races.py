# Turtle Racing v1
# Mr. Scott
# Dec 4, 2023

import random, turtle

# Reminder: Random  random.randint(l,h)  random.uniform(l,h)  random.choice(list)

# Set up the window and turtles
w = turtle.Screen()

#Turtles
lance = turtle.Turtle()
andy = turtle.Turtle()
lance.shape("turtle")
andy.shape("turtle")
lance.color("blue")
andy.color("red")

# Go to the race starting positions
andy.up()
lance.penup()
andy.goto(-250,20)
lance.goto(-250,-20)

# Race! 4 Types of races...
# Race1: Single Random Number Generation
# andy.forward(random.randint(100,500))
# lance.forward(random.randint(100,500))

# Race 2: Random number of "loops"
# for i in range(random.randint(20,100)):
#     andy.fd(5)
# 
# for j in range(random.randint(20,100)):
#     lance.fd(5)

# Race 3: One loop, moving in little slices
# for i in range(150):
#     andy.fd(random.randint(1,6))
#     lance.fd(random.randint(1,6))
    
print(f"Andy's location: {andy.xcor()}, {andy.ycor()}")
print(f"Lance's location: {lance.xcor()}, {lance.ycor()}")

# Race 4: While loop. Race until one turtle passes x==250
while andy.xcor() < 250 and lance.xcor() < 250:
    andy.fd(random.randint(3,6))
    lance.fd(random.randint(3,6))

# Reporting who the race winner is:
if andy.xcor() > lance.xcor():
    print("Andy (RED) wins!!")
elif andy.xcor() < lance.xcor():
    print("Lance (BLUE) wins!!")
else:
    print("TIE!!")



w.exitonclick()  #final instruction