#Exercise 4-19 Stop Sign
# Nakshtra Nitin Kawthale
# CS 175/501A 

import math
import turtle
window_width = 400
window_height = 400
num_sides = 8
length = 100
angle = 45
turtle.setup(window_width, window_height)
turtle.penup()
turtle.goto(-50,100)
turtle.pendown()
turtle.shape('turtle')

turtle.pensize(5)
turtle.color('black')
turtle.fillcolor('red')
turtle.begin_fill()

for stop in range(num_sides):
    turtle.pendown()
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()

turtle.penup()
turtle.goto(-75,-70)
turtle.color("white")
turtle.write("STOP", font=("Impact",60))
turtle.hideturtle()





