"""CS 108 - Lab 5.2

This program draws spirograph.
A spirograph is a geometric drawing toy that produces hypotrochoids and epitrochoids.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

#import the guizero and math libraries
import math 
from guizero import App,  Drawing
app = App('Drawing Canvas')
drawing = Drawing(app, width='fill', height='fill')


moving_radius = float(input('moving radius: ')) #get the user input for the radius of the moving circle
fixed_radius = float(input('fixed radius: ')) #get the user input for the radius of the fixed circle
pen_offset = float(input('pen offset: ')) #get the user input for the offset of the pen point in the moving circle
color1 = input('color: ') #get the user input for the color for the drawing
center = app.width/2

#to make the parametric equations easy to read, assign small equations into a variable
a = moving_radius + fixed_radius
r = fixed_radius
p = pen_offset

#two equations for drawing a spirograph picture
#x = a*cos(t) + p*cos(a*t/r) + center 
#y = a*sin(t) + p*sin(a*t/r) + center

#set the initial point
x = a*math.cos(0) + p*math.cos(a*0/r) + center
y = a*math.sin(0) + p*math.sin(a*0/r) + center

t = 0.0
while t < 360: #it repeats as long as t is less than 360
    t += 0.1 #keep adding 0.1 to t
    next_x = a*math.cos(t) + p*math.cos(a*t/r) + center #assign new t's to the equations
    next_y = a*math.sin(t) + p*math.sin(a*t/r) + center
    #draw lines from point1(x,y) to point2(next_x, next_y) with user-assigned color
    drawing.line( 
    x,y,
    next_x,next_y,
    color = color1
)
    #set x and y equal to next_x and next_y respectively so that they can get back to the loop
    x = next_x 
    y = next_y
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    