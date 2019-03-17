# -*- coding: utf-8 -*-
"""
Working with Functions

Author: Kriyative Edge
"""

# Program to find square root using squareroot function from math library

from math import sqrt
#Get value from user
num = eval(input("Enter a number: "))
#Compute the square root
root = sqrt(num)
# Report result
print("Square root of", num, "=", root)

# This program shows the various ways the
# sqrt function can be used.

from math import sqrt

x = 16
# Pass a literal value and display the result
print(sqrt(16.0))
# Pass a variable and display the result
print(sqrt(x))
# Pass an expression
print(sqrt(2 * x - 5))
# Assign result to variable
y = sqrt(x)
print(y)
# Use result in an expression
y = 2 * sqrt(x + 16) - 4
print(y)
# Use result as argument to a function call
y = sqrt(sqrt(256.0))
print(y)
print(sqrt(int('45')))


"""
Math Function Module:
---------------------
sqrt - computes the square root of a number: sqrt(x) = √x

exp - computes e raised to power:              exp(x) = e^x

log - computes the natural logarithm of a number: log(x) = lnx

log10 - computes the common logarithm of a number

cos / sin / tan etc. - computes the trignometric functions include sine, tangent, arc cosine, arc sine, arc tangent, hyperbolic cosine, hyperbolic sine, and hyperbolic tangent

pow - raises one number to a powr of another: pow(x,y) = x^y

degrees - raises a value in radians to degrees: degrees(x) = (pi/180)x

radians - converts a value in degrees to radians: radians(x) = (180/pi)x

fabs - computes the absolute value of a number: fabs(x) = |x| 
"""

#Time functions
from time import clock

print("Enter your name: ", end="")
start_time = clock()
name = input()
elapsed = clock() - start_time
print(name, "it took you", elapsed, "seconds to respond")

# Now, let us write a program to add up all the integers from 1 to 100,000

from time import clock

sum = 0	# Iniatialize sum accumulator
start = clock()	# start the stopwatch
for n in range(1,100001):	#sum the numbers
	sum += n
elapsed = clock() - start	#stop the stopwatch
print("sum:", sum, "time:", elapsed)

#measures how long it takes a program to count all the prime numbers up to 10,000 using the same algorithm

from time import clock

max_value = 10000
count = 0
start_time = clock() # Start timer
# Try values from 2 (smallest prime number) to max_value
for value in range(2, max_value + 1):
	# See if value is prime
	is_prime = True # Provisionally, value is prime
	# Try all possible factors from 2 to value - 1
	for trial_factor in range(2, value):
		if value % trial_factor == 0:
			is_prime = False # Found a factor
			break # No need to continue; it is NOT prime
	if is_prime:
		count += 1 # Count the prime number
print() # Move cursor down to next line
elapsed = clock() - start_time # Stop the timer
print("Count:", count, " Elapsed time:", elapsed, "sec")

#LET US WORK WITH ANOTHER TYPE OF FUNCTION CALLED "RANDOM"
#RANDOM FUNCTION IS WIDELY USED TO GENERATE A RANDOM VALUE
#LET US WRITE A PROGRAM THAT SIMULATES THE ROLLING OF A DIE

from random import randrange

#Roll the die three times
for i in range(0,3):
	#generate random number in the range 1 . . . 6
	value = randrange(1,6)
	
	#show the die
	print("+--------+")
	if value == 1:
		print("|     |")
		print("|  *  |")
		print("|     |")
	elif value == 2:
		print("| *   |")
		print("|     |")
		print("|    *|")
	elif value == 3:
		print("|    *|")
		print("|  *  |")
		print("|*    |")
	elif value == 4:
		print("|*   *|")
		print("|     |")
		print("|*   *|")
	elif value == 5:
		print("|*   *|")
		print("|  *  |")
		print("|*   *|")
	elif value == 6:
		print("|* * *|")
		print("|     |")
		print("|* * *|")
	else:
		print(" *** Error: illegal die value ***"
	print("+--------+")
		

