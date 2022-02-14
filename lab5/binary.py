"""CS 108 - Lab 5.1

This program lets the user input a positive integer,
and gives the user a string of 1's and 0's representing the integer in reversed binary.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

#get the user input for a positive integer
x = int(input('integer: '))

#print out a string of 1's and 0's representing the integer in reversed binary
#it repeats as long as x is greater than 0
while x > 0: 
    print(x%2, end='') #print out the value of x%2
    x=int(x/2) #put the value of x/2 (rounded down to the nearest integer) to x and run it over again
print() #print out a newline