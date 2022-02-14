"""CS 108 - Homework 1

This program is to draw a Dutch flag with the turtle graphic.
The proportion of the Dutch flag is 2:3.
I have set the UNIT(180) as the horizontal side of the flag
2/3 of the length of the horizontal should be the length of the vertical, which is 120
and since it has 3 same sizes of rectangles (red, white, blue)
so each length of the rectangles should be 2/9 of the UNIT, which is 40

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""
import turtle

window = turtle.Screen()

UNIT = 180

turtle.color('#AE1C28','#AE1C28') 
turtle.begin_fill()
turtle.forward(UNIT)
turtle.right(90)
turtle.forward(UNIT*2/9)
turtle.right(90)
turtle.forward(UNIT)
turtle.end_fill()

turtle.color('#000000','#FFFFFF')
turtle.begin_fill()
turtle.left(90)
turtle.forward(UNIT*2/9)
turtle.left(90)
turtle.forward(UNIT)
turtle.left(90)
turtle.forward(UNIT*2/9)
turtle.right(180)
turtle.forward(UNIT*2/9)
turtle.end_fill()

turtle.color('#21468B','#21468B') 
turtle.begin_fill()
turtle.forward(UNIT*2/9)
turtle.right(90)
turtle.forward(UNIT)
turtle.right(90)
turtle.forward(UNIT*2/9)
turtle.end_fill()

turtle.hideturtle() # to make it look nicer, hide the turtle


