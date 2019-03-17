# -*- coding: utf-8 -*-

"""
Studying approximate solutions in exhaustive enumeration
Program to find cube root

Author: Kriyative Edge
"""
# good enough solution
# start with a guess and increment by some small value
#|guess^3|-cube <= epsilon - for some small epsilon

# decreasing increment size --> slower program
# increasing epsilon --> less accurate answer

cube = 29
epsilon = 0.01  #decrease epsilon to increase number of steps and better accuracy
guess = 0.0
increment = 0.01
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)


# try with cube = 27, and large step (e.g. 2.0)

"""OBSERVATIONS"""
# Step could be any small number
    #If too small, takes a long time to find square root
    #If too large, might skip over answer without getting close enough
# In general, will take x/step times through code to find solution
# Need a more efficient way to do this

"""
TASK:
Following the same pattern above, make a program to find square root of a given number.
Also the program should check for negative numbers, if any negative number is provided by the user, it should prompt
the user with a message with that effect
"""

