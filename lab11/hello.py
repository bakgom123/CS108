"""CS 108 Lab 11.0

This module lets the users enter their names and when they push the "Goodbye!" button, it quits.

@author: Keith VanderLinden (kvlinden)
@date: Spring, 2021
@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

from guizero import App, Text, Box, TextBox, PushButton


class MyApp:

    def __init__(self, app):

        # Configure the application GUI.
        app.title = 'My Application'
        app.width = 500
        app.height = 450
        app.font = 'Helvetica'
        app.text_size = 12
        
        
        box = Box(app, layout = 'grid')

        # Add the widgets.
        Text(box, text = 'Please enter your name:', grid = [150,150], align = 'right')


# Create the GuiZero application.
app = App()
my_app = MyApp(app)
app.display()
