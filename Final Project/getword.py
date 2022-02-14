""" CS 108 Final Project

This model is for choosing the word for Hangman game.

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

from random import randint
  
def get_easyword():
    '''Read from easy_wordlist file, and choose an easy word to play hangman.'''
    infile = open('easy_wordlist.txt', 'r')
    listofword = infile.read().splitlines()
    random_num = randint(0, len(listofword) - 1) 
    chosen_word = listofword[random_num] # Get a random word from the word list.
    infile.close()
    return chosen_word
        
        
def get_advancedword():
    '''Read from sat_wordlist file, and choose a SAT word to play hangman.'''
    infile = open('sat_wordlist.txt', 'r')
    listofword = infile.read().splitlines()
    random_num = randint(0, len(listofword) - 1)
    chosen_word = listofword[random_num] # Get a random word from the word list.
    infile.close()
    return chosen_word
        