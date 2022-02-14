"""CS 108 - Homework 5

This module draws a bar graph with assigned color and data.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""
import random

class BarGraph:
    
    def __init__(self, data, color):
        """Constructs a BarGraph instance with the given data and color."""
        self.data = data
        self.color = color

        
    def __str__(self):
        """Returns the information of the color and data of the bar graph."""
        return 'Bar Graph - Color: ' + self.color + 'Data: ' + self.data
    
    
    def draw(self, drawing, width, height):
        """Draw bar graphs with the user assigned color and data."""
        a = 0 
        while 0 <= a < len(self.data): 
            height_each = height - self.data[a]*(height/max(self.data)) #Set the height for each graph.
            start_x = (width/len(self.data))*a # Set start_x as the top-left point of the rectangle.
            finsh_x = (width/len(self.data))*(a+1) # Set finish_x as the bottom-right point of the rectangle.
            for x in self.data:
                drawing.rectangle(
                start_x, height_each, 
                finsh_x, height,
                color = self.get_color(),
                outline = True 
            )
            a += 1 # To compute height and width for the next graph, it keeps adding 1 to a for the next loop.
    
    
    def get_color(self):
        """Returns the specified graph color or a random color"""
        if self.color == 'random':
            return random.choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
        else:
            return self.color
        



