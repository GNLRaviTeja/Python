# -*- coding: utf-8 -*-
"""
Program to find x is a perfect cube or not

Author: Kriyative Edge
"""

x = int(input('Enter an integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) , ' is ' , ans)

# The above program only works for positive integers
# By taking the abs(x) value, the code now will yeild same type of result as before
# but the condition inside else case makes the program to find the nearest cube root of the given number

x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = - ans
print('Cube root of ' + str(x) + ' is ' + str(ans))

# The above 2 programs use direct method with absolute value to check for negative integers to identify the answer

# guess and check method helps to keep repeating a guess from a random point rather than looking into
# every possible case. This is a classic example of Exhaustive Enumeration

cube = -28
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))


"""
Exercise:
---------
Write a program that asks the user to enter an integer and prints 2 integers, root and pwr, such that
0 < pwr < 6 and root**pwr is equal to integer entered by the user.
If no such pair of integers exists, it should print a message to that effect
"""


                                                                                                                                                                                  
