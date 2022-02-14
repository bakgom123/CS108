"""CS 108 - Lab 3.1

This program let the user input their first name, last name, and student ID
and use the first name(the first letter only), last name, and student ID to make the User ID

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

First_name = input('First name: ')
First_name = First_name.lower()

Last_name = input('Last name: ')
Last_name = Last_name.lower()

Student_ID = input('Student ID: ')

print('User ID:',First_name[0] + Last_name + Student_ID[0:2])