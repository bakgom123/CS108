"""CS 108 - Lab 3.2

This is the program that let the user put in 4 numbers
and print out the numbers in order (from min to max)
(not using sort for this program)

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

num1 = float(input('number: '))
num2 = float(input('number: '))
num3 = float(input('number: '))
num4 = float(input('number: '))

numlist = [num1,num2,num3,num4]

q = min(numlist)
numlist.remove(q)

w = min(numlist)
numlist.remove(w)

e = min(numlist)
numlist.remove(e)

r= min(numlist)

numlist2 = [q,w,e,r]
print(numlist2)