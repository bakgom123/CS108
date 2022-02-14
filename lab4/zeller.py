"""CS 108 - Lab 4.2

This program lets the user input a year, a month, and a day of the month
and compute what day of the week is.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

import math

year = int(input('Enter year: '))
month = int(input('Enter month: '))
day = int(input('Enter day: '))

if month < 3:
    month += 12
    year -= 1

j = year//100
k = year % 100
h = (day+(month+1)*26/10+k+math.floor(k/4)+math.floor(j/4)+5*j)%7

h = math.floor(h)

days_of_week = [
    'Saturday',
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday'
]

print(days_of_week[h])

