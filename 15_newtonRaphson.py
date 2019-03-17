# -*- coding: utf-8 -*-

"""
Using Newton-Raphson method, program to find the square root of a given number
Note: In the program we used float value as user input. If we enter 20, it reads as 20.0. This gives much ease and reliability
particularly with Newton-Raphson technique
You can simply use int as well.

Author: Kriyative Edge
"""

epsilon = 0.01
y = float(input("Enter a number: "))
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))


"""
Excercise:
----------
Add some code to the implementation of Newton-Raphson that keeps track of the number of iterations used to find the root.
Use the code as part of a program that compares the efficiency of Newton-Raphson and bisection search
(You should discover that Newton-Raphson is more efficient)
"""

