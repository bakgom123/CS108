"""CS 108 - Lab 6.2

This function is designed to find the longest word in the list.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

def find_longest(word_list):
    if word_list == []: # if it's an empty list, then return an empty string
        return ''
    x = 0 
    for word in word_list: # it loops until it checks every word in the list
        if len(word) > x:  # if the length of the word is longer than other words in the list
            x = len(word) 
            longest_word = word # returns the longest word in the list
        elif len(word) == 0: # if it has one blank word list
            return '' # it returns empty string
    return longest_word 
    

