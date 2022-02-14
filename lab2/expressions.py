"""CS 108 - Lab 2.0
this python file has comments about arithmetics operators with example
and a prompt to let the user input a integer

@author: Gunju Yoo (gy24)
@date: Spring, 2021
"""

# 3 + 4 = 7 
# it is the addition operator, 3+4=7.

# 2 + 3 * 5 = 17
# it gives 17 because multiple operators have higher precedence than the addition operator.

# 8 - 4 - 2 = 2
# it is the subtraction operator, it calculates from left to right.

# (3 + 7) * 2 = 20
#'()'has the higher precedence than the multiple operator,
# so calculate 3+7 first, and then multiple the result of 3+7 ,which equals to 10, with 2 we get 20.

# 13 % 4 = 1
#'%' is the modulo operator, 13 divide by 4 and the remainder should be 1.

# 8.2 // 4 = 2.0 ,
# '//' is the floored division operator,
# it rounds down the result of a floating-point division to the closest whole number value.
# Since it is float floor divide int, so it will give a float as an answer, which in this case, 2.0

# 2 ** 10 = 1024,
#'**' is the exponent operator, 2 to the power of 10 is equal to 1024.

# 5.1 % 2 = 1.1
# '%' is the modulo operator, 5.1 (float) divide by 2 (int) and the remainder should be 1.1 (float). 

num = int(input('Please enter an integer: '))



