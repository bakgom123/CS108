"""CS 108 - Lab 2.2

This program is to use a turtle graphic to draw a stick man.
It has a specific size for all the body parts.
The size of the head should be a circle of radius of the assigned UNIT
The length of the body and arms should be 2 UNIT
the length of the legs should be sqrt of the UNIT, and the angle of those two legs should be 90 degrees.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

import turtle
import math

window = turtle.Screen()
pen = turtle.Turtle()

UNIT = 50 # Set the constant value for UNIT
pen.circle(UNIT) #head 
pen.right(90)
pen.forward(UNIT) #neck
pen.right(90)
pen.forward(UNIT) #arms
pen.backward(UNIT*2) 
pen.forward(UNIT)
pen.left(90)
pen.forward(UNIT) #body
pen.right(45)
pen.forward(math.sqrt(2)*UNIT) #legs
pen.backward(math.sqrt(2)*UNIT)
pen.left(90)
pen.forward(math.sqrt(2)*UNIT)

pen.hideturtle() # to make it look nicer, hide the turtle



