# -*- coding: utf-8 -*-
"""
Program to find a positive integer that is divisible by both 11 and 12

Author: Kriyative Edge
"""

x = 133
while True:
    if x%11 == 0 and x%12 == 0:
        break
    x = x + 1
print(x, " is divisible by 11 and 12")

"""
Code starts by binding the variable x to 1.
until the loop gets to an integer which is divisible by both 11 and 12 the program continues

OUTPUT prints: 132

Let us give x = 133 and see which will be next positive integer after 132 which is divisible by both 11 and 12

"""
