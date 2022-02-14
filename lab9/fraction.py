"""CS 108 - Lab 9.1

This module gets the numerator and denominator for a fraction and simplifies the fraction.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""


import math

class Fraction:
    """This class receives numerator and denominator for a fraction and simplifies it."""
    
    def __init__(self, numerator, denominator):
        """Constructs a Fraction instance with the given numerator and denominator."""
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    
    def __str__(self):
        """Returns the fraction with assigned numerator and denominator."""
        return ('{}/{}'.format(self.numerator, self.denominator))
    

    def is_valid(self):
        """Returns True if the fraction is valid, and returns False if the fraction is invalid."""
        if self.denominator == 0: # the denominator should not equal zero.
            return False # If the fraction is invalid, then return False.
        else:
            return True # If the fraction is valid, then return True.
    
    def simplify(self):
        """Simplifies the fraction."""
        gcd = math.gcd(self.numerator, self.denominator)
        if gcd != 0:
            self.numerator = self.numerator // gcd
            self.denominator = self.denominator // gcd
        if self.denominator < 0:
            self.numerator = self.numerator * (-1)
            self.denominator = self.denominator * (-1) # Changes values of self.numerator and self.denominator. 

            
    def __mul__(self, other):
        """Simplifies the fraction after the multiplication."""
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)
    

        
        
        