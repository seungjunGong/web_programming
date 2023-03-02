# make turtle game by python

import turtle

# Create a screen and set its background color
screen = turtle.Screen()
screen.bgcolor("lightgreen")

# Create a turtle object and set its shape, color, and speed
turtle_obj = turtle.Turtle()
turtle_obj.shape("turtle")
turtle_obj.color("blue")
turtle_obj.speed(2)

# Draw the square
for _ in range(4):  # repeat 4 times
    turtle_obj.forward(50)  # move forward 50 pixels
    turtle_obj.right(90)    # turn right 90 degrees

# Draw the circle
turtle_obj.penup()      # lift up the pen
turtle_obj.goto(-50, -50)  # move to (-50,-50)
turtle_obj.pendown()    # put down the pen

# draw a circle with radius 50
turtle_obj.circle(50)