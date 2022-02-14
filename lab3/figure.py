"""CS 108 - Lab 3.4

This program uses the GuiZero methods to draw a stick figure
this is really different from the turtle
the GuiZero methods can draw things with parameters
and the figure came up right away

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

from guizero import App, Drawing

app = App('Drawing Canvas')

drawing = Drawing(app, width='fill', height='fill')


unit = 50                # Change this value to rescale the drawing.

drawing.oval(
    1 * unit, 2 * unit,  # bounding box x1, y1
    3 * unit, 4 * unit,  # bounding box x2, y2
    outline=True,
    color='white'
)

drawing.line(
    1 * unit, 5 * unit, # x1, y1
    3 * unit, 5 * unit, # x2, y2
    color='black'
)

drawing.line(
    2 * unit, 4 * unit,  # x1, y1
    2 * unit, 6 * unit,  # x2, y2
    color='red'
)

drawing.line(
    2 * unit, 6 * unit,  # x1, y1
    1 * unit, 7 * unit,  # x2, y2
    color='black'
)

drawing.line(
    2 * unit, 6 * unit,  # x1, y1
    3 * unit, 7 * unit,  # x2, y2
    color='black'
)

app.display()
