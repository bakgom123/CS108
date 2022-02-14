"""CS 108 - Lab 1.2

This program uses turtle graphic to draw a five-pointed star.
The internal angle is 36 degrees, and each legs has the same length.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

import turtle

# Start the turtle window in the corner of the screen (helpful for dual monitor).
# turtle.setup(width=800, height=600, startx=100, starty=100)

window = turtle.Screen()
pen = turtle.Turtle()

pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)
pen.right(144)
pen.forward(250)





# window.mainloop() # Needed for some IDEs.
