"""CS 108 - Homework 3

This program lets the user inputs several data, and use those data to draw bar graphs.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

#Import the guizero
from guizero import App,  Drawing
app = App('Drawing Canvas')

# Set the width and the height of this canvas to 500 pixels each.
width = 500 
height = 500
drawing = Drawing(app, width=width, height=height)

# Set an empty list, and add all the data inputted by the user in this list.
my_list = []

while True:
    x = input('Enter a number: ') 
    if x == '' : # When the user hits enter, it finishes the loop.
        break
    my_list.append(float(x)) # Add all data to the list.


# Draw rectangles in the order in which the user enters the data.
# It keeps drawing until it has all the bar graphs with all the assigned data.
a = 0 
while 0 <= a < len(my_list): 
    height_each = height - my_list[a]*(height/max(my_list)) #Set the height for each graph.
    start_x = (width/len(my_list))*a # Set start_x as the top-left point of the rectangle.
    finsh_x = (width/len(my_list))*(a+1) # Set finish_x as the bottom-right point of the rectangle.
    for x in my_list:
        drawing.rectangle(
            start_x, height_each, 
            finsh_x, height,
            color = 'green',
            outline = True 
        )
    a += 1 # To compute height and width for the next graph, it keeps adding 1 to a for the next loop.
    
    
    
    