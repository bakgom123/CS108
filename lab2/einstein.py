"""CS 108 - Lab 2.1

This program is the process of the Einstein's number puzzle. It shows all the math work that needs to be done to do this "magic trick"
It is really interesting because it gives the same result (1089) if you enter a three-digit number and that the first and last digits differ by at least 2

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""
import math

number = int(input('Number: ')) #let the user input a three-digit number and that the first and last digits differ by at least 2
digit1 = number // 100 
digit2 = (number % 100) // 10 
digit3 = number % 10 

rev_number = digit3 * 100 + digit2 * 10 + digit1 #reverse the order of those digit to make a new number

difference = math.fabs(number - rev_number) 
digitd1 = difference // 100
digitd2 = (difference % 100) // 10
digitd3 = difference % 10
rev_diff = digitd3 * 100 + digitd2 * 10 + digitd1 #basically doing the same thing as above just using the new number - rev_num

sum = difference + rev_diff

print (int(sum)) #it will come out with a float, so we change the value to an integer.
