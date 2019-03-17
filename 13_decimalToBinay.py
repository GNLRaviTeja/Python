# -*- coding: utf-8 -*-

"""
Working with floats and integer.
Data conversion has its prominence in many industrial applications
This program converts any positive integer into its binary value

Author: Kriyative Edge
"""

num = int(input("Enter an Integer: "))

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = '-' + result

print("Binary format of ", str(num), " is: ", result)
"""
Explanation:
-------------
1. consider example of
    x = 1*2^4 + 0*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 10011
2. If we take remainder relative to 2 (x%2) of this number,
that gives us the last binary bit
3. If we then devide x by 2 (x//2), all the bits get shifted
right
    x//2 = 1*2^3 + 0*2^2 + 0*2^1 + 1*2^0 = 1001
4. Keep doing successive divisions, now remainder gets next
bit, and so on
5. let's us convert to binary form

"""

