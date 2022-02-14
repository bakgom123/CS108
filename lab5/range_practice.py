"""CS 108 - Lab 5.0

This program lets the user input two integers,
and keep adding 10 to the first integer as long as the value is less than or equal to the second integer.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

#get the user input for two integers
first_int = int(input())
second_int = int(input())

#if the first number is greater than the second number,
#then let the user know the first number must be less than or equal to the second number
if first_int > second_int:
    print("Second integer can't be less than the first.")
else: #if the user correctly input two numbers (first_num <= second_int)
    while first_int <= second_int: #keep adding 10 to the first integer as long as the value is less than or equal to the second integer
        print (first_int)
        first_int += 10 
        
        
        