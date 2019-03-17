# -*- coding: utf-8 -*-
"""
Understanding different types of program interpretations

Author: Kriyative Edge
"""

#Building a global calculator

# help_screen
# Displays information about how the program works
# Accepts no parameters
# Returns nothing

def help_screen():
	print("Add: Adds two numbers")
	print("Subtract: Subtracts two numbers")
	print("Print: Displays the result of the latest operation")
	print("Help: Displays this help screen")
	print("Quit: Exits the program")

# menu
# Display a menu
# Accepts no parameters
# Returns the string entered by the user.

def menu():
	# Display a menu
	return input("=== A)dd S)ubtract P)rint H)elp Q)uit ===")

# Global variables used by several functions
result = 0.0
arg1 = 0.0
arg2 = 0.0

# get_input
# Assigns the globals arg1 and arg2 from user keyboard
# input
def get_input():
	global arg1, arg2 # arg1 and arg2 are globals
	arg1 = float(input("Enter argument #1: "))
	arg2 = float(input("Enter argument #2: "))

# report
# Reports the value of the global result
def report():
	# Not assigning to result, global keyword not needed
	print(result)

# add
# Assigns the sum of the globals arg1 and arg2
# to the global variable result
def add():
	global result # Assigning to result, global keyword needed
	result = arg1 + arg2

# subtract
# Assigns the difference of the globals arg1 and arg2
# to the global variable result
def subtract():
	global result # Assigning to result, global keyword needed
	result = arg1 - arg2

# main
# Runs a command loop that allows users to
# perform simple arithmetic.
def main():
	done = False; # Initially not done
	while not done:
		choice = menu() # Get user's choice

		if choice == "A" or choice == "a": # Addition
			get_input()
			add()
			report()
		elif choice == "S" or choice == "s": # Subtraction
			get_input()
			subtract()
			report()
		elif choice == "P" or choice == "p": # Print
			report()
		elif choice == "H" or choice == "h": # Help
			help_screen()
		elif choice == "Q" or choice == "q": # Quit
			done = True

main()

#PROGRAM TO WORK WITH RECURSIVE FUNCTIONS

# factorial(n)
# Computes n!
# Returns the factorial of n.
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

def main():
	#Try out the factorial function
	print(" 0! = ", factorial(0))
	print(" 1! = ", factorial(1))
	print(" 6! = ", factorial(6))
	print("10! = ", factorial(10))

main()

# Python program to display the Fibonacci sequence up to n-th term using recursive functions

def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# Change this value for a different result
nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))

# Another way of representing the same problem above
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print (fibonacci(i))

"""
Tasks:
--------
1. Think of a recusive version of the function f(n) = 3 * n, i.e. the multiples of 3
2. Write a recursive Python function that returns the sum of the first n integers. 
(Hint: The function will be similiar to the factorial function!)
3. Write a function which implements the Pascal's triangle

"""
#Program to find GCD using Euclideon Method

# gcd(m, n)
# Uses Euclid's method to compute
# the greatest common divisor
# (also called greatest common
# factor) of m and n.
# Returns the GCD of m and n.
def gcd(m, n):
	if n == 0:
		return m
	else:
		return gcd(n, m % n)

def iterative_gcd(num1, num2):
	# Determine the smaller of num1 and num2
	min = num1 if num1 < num2 else num2
	# 1 is definitely a common factor to all integers
	largestFactor = 1;
	for i in range(1, min + 1):
		if num1 % i == 0 and num2 % i == 0:
			largestFactor = i # Found larger factor
	return largestFactor

def main():
	# Try out the gcd function
	for num1 in range(1, 101):
		for num2 in range(1, 101):
			print("gcd of", num1, "and", num2, "is", gcd(num1, num2))

main()



#Program to solve towers of Hanoi
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))

#Program to check a given string is palindrome or not
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

print("")
print('Is eve a palindrome?')
print(isPalindrome('eve'))

print('')
print('Is able was I ere I saw Elba a palindrome?')
print(isPalindrome('Able was I, ere I saw Elba'))

