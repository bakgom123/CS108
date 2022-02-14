"""CS 108 - Lab 6.0

This program has two functions
The first function computes the cost in dollars to drive miles that the user inputs.
The second function counts how many spaces are there in the string that the user inputs.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""


# This function which calculate the cost in dollars to drive those miles that user inputs
def compute_cost(miles, miles_per_gallon, dollars_per_gallon):
    '''Returns the cost for traveling a ceratin distance'''
    cost = (miles / miles_per_gallon) * dollars_per_gallon 
    return cost
    print(compute_cost(200,20,4)) # using the compute_cost function to calculate the cost



#This function count spaces in the string that the user inputs
def count_spaces(my_string):
    '''Returns the number of spaces in a given phrase'''
    spaces = 0
    for x in range(0,len(my_string)): 
        if my_string[x] == ' ': # if there is space in the string
            spaces += 1 # it adds 1 to the count 
    return spaces


