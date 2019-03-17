"""
Program to find whether a given number is divisible by 2 and 3
Author: Kriyative Edge
"""
# -*- coding: utf-8 -*-

x = int(input("Enter an integer: "))

if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')


"""
It is often convenient to use a compound Boolean expression in the test of conditional
example:
---------
if x<y and x<z:
    print("x is least")
elif y<z:
    print("y is least")
else:
    print("z is least")

Try to recreate the divisible by 2 and 3 program using compound Boolean expression and check the result
"""

"""
Exercise:
Write a program that examines three variables x,y,z and prints the largest odd number among them. If
none of them are odd, it should print a message to that effect
"""
