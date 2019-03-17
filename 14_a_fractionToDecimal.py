# -*- coding: utf-8 -*-

"""
Working with floats and integer.
Data conversion has its prominence in many industrial applications
This program converts any positive integer into its binary value

Author: Kriyative Edge
"""

x = float(input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))



"""
Explanation:
-------------
1. 3/8 = 0.375= 3*10^-1 + 7*10^-2 + 5*10^-3
2. So if we multiply by a power of 2 big enough to convert into a whole number, can then convert
to binary, and then divide by the same power of 2
3. 0.375*(2**3) = 3(decimal)
4. Convert 3 to binary (now 11)
5. Divide by 2**3 (shift right) to get 0.011 (binary)

Some Implications:
------------------
1. If there is no integer 'p' such that x*(2**p) is a whole number, then internal representation
is always an approximation
2. Suggest that testing equality of floats is not exact
    a. Use abs(x-y)<some small number, rather than x==y


"""

