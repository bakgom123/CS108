"""CS 108 - Lab 3.0

This program lets the user input quiz scores, system password,
GPS coordinates of your dorm, and names of two favorite states with capitals
in different types (list, tuple, and dictionary)

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

scores1 = int(input('score: '))
scores2 = int(input('score: '))
scores = [scores1,scores2]

password = input('password: ')

latitude = float(input('latitude: '))
longitude = float(input('longitude: '))
dorm = (latitude, longitude)

state1 = input('state: ')
capital1 = input('capital: ')
state2 = input('state: ')
capital2 = input('capital: ')
state_capitals = {
    'state1':state1,
    'capital1':capital1,
    'state2':state2,
    'capital2':capital2
}
