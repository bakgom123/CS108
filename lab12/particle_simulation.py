"""CS 108 Lab 12

This module implements a GUI controller for a particle simulation

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Fall, 2018 - updated to use callback animation
@date: Spring, 2021 - ported to GuiZero
@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

from guizero import App, Drawing, PushButton, Box
from random import randint
from particle import Particle
from helpers import get_random_color, distance


class ParticleSimulation:
    """ParticleSimulation runs a simulation of multiple particles interacting
    on a single canvas.
    """

    def __init__(self, app):
        """Instantiate the simulation GUI app."""

        app.title = 'Particle Simulation'
        UNIT = 500
        CONTROL_UNIT = 50
        app.width = UNIT
        app.height = UNIT + CONTROL_UNIT
        self.p_list = []

        # Add the widgets.
        box = Box(app, layout='grid', width=UNIT, height=UNIT + CONTROL_UNIT)
        self.drawing = Drawing(box, width=UNIT, height=UNIT, grid=[0, 0, 2, 1])

        # Draw the white background.
        self.drawing.rectangle(0, 0, self.drawing.width, self.drawing.height,
                               color='black')
        
        # Add a botton to add particles
        PushButton(box, text = 'Add particle', grid = [0,1], command = self.add_particle)
        
        
        # Start the animation 
        app.repeat(10, self.draw_frame)
        self.drawing.when_clicked = self.check_remove_particle
        
        
    def check_remove_particle(self, event):
        """Removes when the user clicked on the particle."""
        copy = self.p_list[:]
        for p in self.p_list:
            if p.is_clicked(event.x, event.y):
                self.p_list.remove(p)
                
                
    def add_particle(self):
        """Add particles with random colors, speed, sizes."""
        radius = randint(5,25)
        x = randint (25, 500-25)
        y = randint (25,500-25)
        vel_x = randint(-radius // 10, radius // 10)
        vel_y = randint(-radius // 10, radius // 10)
        color = get_random_color() 
        self.p_list.append(Particle(x,y,vel_x,vel_y , radius, color))
       
        
    def draw_frame(self):
        """It lets the particles to bounce off one another."""
        self.drawing.clear()
        for i in range (len(self.p_list)):
            for j in range(i):
                particle1 = self.p_list[i]
                particle2 = self.p_list[j]
                if particle1.hits(particle2):
                    self.p_list[i].bounce(self.p_list[j])
        for Particle in self.p_list:
            Particle.move(self.drawing)
            Particle.draw(self.drawing)
        
        

app = App()
ParticleSimulation(app)
app.display()

