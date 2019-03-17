# -*- coding: utf-8 -*-

"""
Studying approximate solutions using bisection search
Program to find cube root

Author: Kriyative Edge
"""
cube = int(input("Enter the integer to find cube root: "))
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)

"""
1. what would the code do if cube is given a negative integer. Try '-125'
2. what would have to be changed to make the code work for finding an approximation to the
cube root of both negative and positive numbers?

HINT: Think about changing 'low' to ensure that the answer lies with in the region
being searched.

"""

