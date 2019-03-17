# -*- coding: utf-8 -*-
"""
Working with Functions

Author: Kriyative Edge
"""

#The simplest function accepts no parameters and returns no value to the caller.
#The def keyword introduces a function definition

#Program to print two numbers
#print a message to prompt the user for input
def prompt():
	print("Please enter an integer value: ", end="")

#start of program
print("This program adds together two integers.")
prompt()	#call the function
value1 = int(input())
prompt()	#call the function again
value2 = int(input())

sum = value1 + value2
print(value1, "+", value2, "=", sum)

# Count to n and print each number on its own line
def count_to_n(n):
	for i in range(1, n + 1):
		print(i)

print("Going to count to ten . . .")
count_to_n(10);
print("Going to count to five . . .")
count_to_n(5);

#Let us work with GCD of m and n
#let us work with a program that has only one single free statement at the end 'main()'

#computes the greatest common divisor of m and n
def gcd(m,n):
	#determine the smaller of m and n
	min = m if m<n else n
	#1 is definitely a common factor to all this
	largestFactor = 1
	for i in range(1, min+1):
		if m%i==0 and n%i==0:
			largestFactor = i	#Found larger factor
	return largestFactor

#get an interger from the user
def get_int():
	return int(input("please enter an integer: "))

#main code to execute
def main():
	n1 = get_int()
	n2 = get_int()
	print("gcd(", n1, ",", n2, ") = ", gcd(n1,n2), sep="")

#Run the program
main()

#Program to understand parameter passing

def increment(x):
	print("Beginning execution of increment, x =", x)
	x += 1	#Increment x
	print("Ending execution of increment, x =", x)

def main():
	x = eval(input("Enter a value: "))
	print("Before increment, x =", x)
	increment(x)
	print("After increment, x =", x)

main()

#So far we are comfortable with creating a funciton and using them
#let us look into a problem now
#program for a prime generator

from math import sqrt
# is_prime(n)
# Determines the primality of a given value
# n an integer to test for primality
# Returns true if n is prime; otherwise, returns false 

def is_prime(n):
	result = True	#provisionally, n is prime
	root = sqrt(n)
	#try all potential factors from 2 to the square root of n
	trial_factor = 2
	while result and trial_factor <= root:
		result = (n % trial_factor != 0)	#Is it a factor?
		trial_Factor += 1	#try next candidate
	return result

# main
# Tests for primality each integer from 2
# up to a value provided by the user.
# If an integer is prime, it prints it;
# otherwise, the number is not printed.

def main():
	max_value = int(input("Display primes up to what value? "))
	for value in range(2, max_value + 1):
		if is_prime(value):	#see if value is prime
			print(value, end=" ")	#display the prime number
	print()	#move cursor down to next line
	
main()	#run the program

"""
Task:
------
design a calculator 
	- use your imagination
	- need to perform atleast 2 arithmetic operations
	- should support user to quit when ever he wish for
"""

#Fun task
#program to draw a tree of given height

# tree(height)
# Draws a tree of a given height
# height is the height of the displayed tree
def tree(height):
	row = 0 # First row, from the top, to draw
	while row < height: # Draw one row for every unit of height
		# Print leading spaces
		count = 0
		while count < height - row:
			print(end=" ")
			count += 1
		#Print out stars, twice the current row plus one:
			# 1. number of stars on left side of tree
			# = current row value
			# 2. exactly one star in the center of tree
			# 3. number of stars on right side of tree
			# = current row value

		count = 0
		while count < 2*row + 1:
			print(end="*")
			count += 1
		#move cursor down to next line
		print()
		#change to the next row
		row += 1

#main
#allows users to draw trees of various heights

def main():
	height = int(input("Enter height of tree: "))
	tree(height)

main()

#FUCTIONS AS ARGUMENTS

def func_a():
    print('inside func_a')
def func_b(y):
    print('inside func_b')
    return y
def func_c(z):
    print('inside func_c')
    return z()
print(func_a())
print(5 + func_b(2))
print(func_c(func_a))


























