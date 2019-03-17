# -*- coding: utf-8 -*-
"""
Program to find the square root of a non negative integer

Author: Kriyative Edge
"""

ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while ans**2 < x:
    ans = ans + 1        #or ans += 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean", -x, "?")


"""
what should the program do if asked to find the square root of 2?
the square root of 2 is not a rational number. This means that there is no way to precisely
represent its value as a finite string of digits (or as a float).
So, the correct way of representing square root problem is to write a program that finds an
approximation to a square root i.e. an answer that is close enough to the actual square root
to be useful.
We will look into approximate solutions to find square root and cube roots problem from next topic
"""
