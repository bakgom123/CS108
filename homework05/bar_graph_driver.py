"""CS 108 - Homework 5

This driver uses the BarGraph class to draw bar graphs.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

from bar_graph import BarGraph
from guizero import App,  Drawing
app = App('Drawing Canvas')
        
# Set the width and the height of this canvas to 500 pixels each.
width = 500 
height = 500
drawing = Drawing(app, width=width, height=height)

data = []
filename = input('Filename: ') # Get the filename from the user.

dataset = open(filename,'r')  # Open file that user has assigned.
datalines = dataset.readlines()
for dataline in datalines:
    data.append(dataline)
color = data.pop(0).strip() # Set the first index of data to be the color of the graph.
for i in range (len(data)):
    data[i] = int(data[i]) # Set the rest of the numbers to be the data of each bar.
dataset.close()


bg = BarGraph(data,color)
bg.draw(drawing, width, height) # draw the bar graph with assigned color and data.

    



    
    
    
    
    
    
    
    
    