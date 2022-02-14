"""CS 108 Lab 11.1

This module provides basic functionality for a calculator.

@author: Serita Nelesen (smb4)
@date: Fall, 2014
@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015 - replaced JUnit tests with assert tests
@date: Spring, 2020 - ported to ZyLabs

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

class Calculator:

    def __init__(self):
        """ Initialize calculator memory to 0.
        This is only needed for the extra credit exercise.
        """
        
    def calculate(self, operand1, operator, operand2):
        """ Perform the specified calculation. """

        operand1 = float(operand1)
        operand2 = float(operand2)

        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
    
        