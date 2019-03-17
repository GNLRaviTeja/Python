# -*- coding: utf-8 -*-
"""
Program to square an integer, the hard iterative way

Author: Kriyative Edge
"""

x = int(input("Enter an integer: "))
ans = 0
iterationsLeft = x
while (iterationsLeft != 0):
    ans = ans + x
    iterationsLeft = iterationsLeft - 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))

"""
Code starts by binding the variable x to the user input.
It then proceeds to square x by using repetitive addition as below.
Consider the integer variable x = 3

| TEST # | x | ans | iterationsLeft |
--------------------------------------
|   1    | 3 |  0  |        3       |
|   2    | 3 |  3  |        2       |
|   3    | 3 |  6  |        1       |
|   4    | 3 |  9  |        0       |

"""
