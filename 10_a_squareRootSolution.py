# -*- coding: utf-8 -*-
"""
TASK:
Following the same pattern above, make a program to find square root of a given number.
Also the program should check for negative numbers, if any negative number is provided by the user, it should prompt
the user with a message with that effect

Author: Kriyative Edge
"""

x = int(input("Enter an integer: "))
epsilon = 0.01  #decrease epsilon to increase number of steps and better accuracy
step = epsilon**2
numGuess = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuess += 1
print("numGuess = ", numGuess)
if abs(ans**2 - x) >= epsilon:
    print("Failed on square root of ",x)
else:
    print(ans," is close to square root of ",x)
