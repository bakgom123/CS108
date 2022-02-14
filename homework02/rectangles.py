"""CS 108 - Homework 2

This program is drawing 2 rectangles with assigned coordinates by the user
and tells if the rectagles are disjoint, overlap or contains another one

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""


from guizero import App,  Drawing
app = App('Drawing Canvas')
drawing = Drawing(app, width='fill', height='fill')


# get the user input for the coordinates of the rectangles
r1_x = int(input ('Enter rectangle 1 x: '))
r1_y = int(input ('Enter rectangle 1 y: '))
r1_width = int(input ('Enter rectangle 1 width: '))
r1_height = int(input ('Enter rectangle 1 height: '))
r2_x = int(input ('Enter rectangle 2 x: '))
r2_y = int(input ('Enter rectangle 2 y: '))
r2_width = int(input ('Enter rectangle 2 width: '))
r2_height = int(input ('Enter rectangle 2 height: '))

# set 8 points of nodes to the proper position
# this is needed because user inputs are not in order
# so it is hard to set up each node 
r1_x1 = min(r1_x, r1_width)
r1_x2 = max(r1_x, r1_width)
r1_y1 = min(r1_y, r1_height)
r1_y2 = max(r1_y, r1_height)
r2_x1 = min(r2_x, r2_width)
r2_x2 = max(r2_x, r2_width)
r2_y1 = min(r2_y, r2_height)
r2_y2 = max(r2_y, r2_height)

#determine the disjoint/overlap/containment,
#and print out both on canvas and the standard output console
if r1_x1 < r2_x1 and r1_y1 < r2_y2 and r2_x2 < r1_x2 and r2_y2 < r1_y2:
    drawing.text(
        100,300, #x,y coordinates of the text
        'Rectangle 2 contains rectangle 1.', 
        color='black'
    )
    print('Rectangle 2 contains rectangle 1.')
elif r2_x1 < r1_x1 and r2_y1 < r1_y2 and r1_x2 < r2_x2 and r1_y2 < r2_y2:
    drawing.text(
        100,300, #x,y coordinates of the text
        'Rectangle 1 contains rectangle 2.',
        color='black'
    )
    print('Rectangle 1 contains rectangle 2.')
elif r1_x2 < r2_x1 or r2_x2 < r1_x1 or r1_y1 < r2_y1 or r2_y2 < r2_y1:
    drawing.text(
        100,300, #x,y coordinates of the text
        'The rectangles are disjoint.',
        color='black'
    )
    print('The rectangles are disjoint.')
elif r1_x1 < r2_x1 < r1_x2 or r2_x1 == r1_x2 or r2_x1 < r1_x1 < r2_x2 or r2_x2 == r1_x1:
    drawing.text(
        100,300, #x,y coordinates of the text
        'The rectangles overlap.',
        color='black'
    )
    print('The rectangles overlap.')
    
#Draws the first rectangle between 2 assigned points      
drawing.rectangle(
    r1_x1, r1_y1, 
    r1_x2, r1_y2,
    color = 'white',
    outline = True 
)
#Draws the second rectangle between 2 assigned points
drawing.rectangle(
    r2_x1, r2_y1,
    r2_x2, r2_y2,
    color = 'white',
    outline = True 
)

app.display()











