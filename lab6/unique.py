"""CS 108 - Lab 6.3

This program has two functions.The first function is the implementation of the second function.
The first function is designed to find the position of the word in the list.
If the word is not in the list, or it is an empty string, it returns -1.
And the second function is designed to collect words that are not on the list yet, and add those words to the list.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""
# This function is designed to find the position of the word that the user inputs
def search(str_list, target):
    '''Returns the position of the word'''
    for x in range (len(str_list)): # it loops until it finds the exact same word
        if target == str_list[x]:
            return x # it returns the position of the word if it found the word in the list
    return -1 # it returns -1 if the word is not on the list

def count_unique_words(str_list):
    unique_words = [] # make an empty list to get the list of words that are not on the list yet
    for word in str_list: 
        if search(unique_words, word) == -1: # use the first function to check whether the word is on the list or not.
            unique_words.append(word) # if it's a new word, then add it to the list.
    return unique_words # Finally, it returns the list of new words.



