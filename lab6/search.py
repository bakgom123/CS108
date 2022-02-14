"""CS 108 - Lab 6.1

This function is designed to find the position of the word in the list.
If the word is not in the list, or it is an empty string, it returns -1.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""


def search(str_list, target):
    '''Returns the position of the word'''
    for x in range (len(str_list)): # it loops until it finds the exact same word
        if target == str_list[x]:
            return x # it returns the position of the word if it found the word in the list
    return -1 # it returns -1 if the word is not on the list

