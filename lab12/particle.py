"""CS 108 Lab 12

This module implements a model of a particle.

@author: Serita Nelesen (smn4)
@date: Fall, 2014
@author: Ken Arnold (ka37)
@date: Fall, 2019 - updated bounce algorithm
@author: Keith VanderLinden (kvlinden)
@date: Spring, 2021 - ported to GuiZero
@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

from helpers import distance


class Particle:
    """ Particle models a single particle that may be rendered to a canvas. """

    def __init__(self, x=50, y=50, vel_x=1, vel_y=5, radius=40, color="red"):
        """Instantiate a particle object."""
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.radius = radius
        self.color = color

    # Add your methods here.
    def draw(self, drawing):
        """Draw an oval."""
        drawing.oval(self.x - self.radius,
             self.y - self.radius,
             self.x + self.radius,
             self.y + self.radius,
             color=self.color
             )


    def move(self, drawing):
        """Lets the particles move around, bouncing off the walls, floor and ceiling."""
        # When the particle reaches either right or the left wall, it negate the x velocity.
        if self.x + self.radius > drawing.width or self.x - self.radius < 0:
            self.vel_x *= -1
        # When the particle reaches either top or the bottom wall, it negate the y velocity.
        if self.y + self.radius > drawing.height or self.y - self.radius < 0:
            self.vel_y *= -1
        self.y += self.vel_y
        self.x += self.vel_x



    def hits(self, other):
        """ Determine if I've collided with 'other'. """
        if self == other:
            # I can't collide with myself.
            return False

        # Determine if I overlap with the other particle.
        return (
                self.radius + other.radius >=
                distance(self.x, self.y, other.x, other.y)
        )

    
    def is_clicked(self,x,y):
        """It recieves coordinate of the point the user clicked on."""
        dis = distance(x,y,self.x, self.y)
        return dis <= self.radius

    def bounce(self, other):
        """Handle elastic collisions between this particle and 'other'.

        This method checks if the two particles collide and, if so, modifies
        the positions and velocities to reflect the result of the collision.

        The result is reasonably physically accurate, but limited by being
        run only *after* a collision has already occurred.

        Both objects are changed, so this method should only be run once for each pair of objects.

        Thanks to Dr. Paul Harper (Calvin Physics).
        """
        if not self.hits(other):
            return

        # Calculate masses (proportional to area)
        m1 = self.radius ** 2
        m2 = other.radius ** 2

        # Calculate velocity of center of mass
        v_cm_x = (m1 * self.vel_x + m2 * other.vel_x) / (m1 + m2)
        v_cm_y = (m1 * self.vel_y + m2 * other.vel_y) / (m1 + m2)

        # Calculate new velocities.
        # Note that the velocity of the center of mass is unchanged, and
        # that if the center of mass is not moving, the velocity just inverts.
        self.vel_x = 2 * v_cm_x - self.vel_x
        self.vel_y = 2 * v_cm_y - self.vel_y

        other.vel_x = 2 * v_cm_x - other.vel_x
        other.vel_y = 2 * v_cm_y - other.vel_y

        # Fix up the positions to ensure they're not stuck together.
        dist_x = self.x - other.x
        dist_y = self.y - other.y
        dist = (dist_x ** 2 + dist_y ** 2) ** 0.5
        dist_x_norm = dist_x / dist
        dist_y_norm = dist_y / dist
        intrusion_distance = (self.radius + other.radius - dist) / 2 + 1e-6

        self.x += intrusion_distance * dist_x_norm
        self.y += intrusion_distance * dist_y_norm
        other.x -= intrusion_distance * dist_x_norm
        other.y -= intrusion_distance * dist_y_norm

    

        
        
        
        
        
        