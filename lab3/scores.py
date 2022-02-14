"""CS 108 - Lab 3.3

This program has a dictionary that has names and scores for each person
It prints out the specified value from the dictionary
It changes the value of the dictionary
It deletes one value from the dictionary
And those changes are saved to the original dictionary
so when you print it out, at last, it will give you the fixed one


@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

score_dict = {
    'Joe':10,
    'Tom':23,
    'Barb':13,
    'Sue':19,
    'Sally':12
}

print(score_dict['Barb'])

score_dict['Sally'] = 13

del score_dict['Tom']

print(score_dict)




