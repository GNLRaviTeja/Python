# -*- coding: utf-8 -*-

"""
Studying approximate solutions using bisection search
Program to find cube root

Author: Kriyative Edge
"""
#previous cube root also serves the same idea but, this program gives iterative output

x = int(input("Enter an Integer: "))
epsilon = 0.01 #change epsilon and try different executions and observe results
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))


"""
1. what would the code do if cube is given a negative integer. 
2. what would have to be changed to make the code work for finding an approximation to the
cube root of both negative and positive numbers?

HINT: Think about changing 'low' to ensure that the answer lies with in the region
being searched.

"""

