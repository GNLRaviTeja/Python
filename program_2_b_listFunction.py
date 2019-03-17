# -*- coding: utf-8 -*-
"""
LIST and FUNCTIONS

Author: Kriyative Edge

"""
#A list can be passed to a function

def sum(lst):
	'''
	Adds up the contents of a list of 		numeric values. lst is the list to sum. 
	Returns the sum of all the elements or 		zero if the list is empty
	'''

	result = 0;
	for item in lst:
		result += item
	return result

def clear(lst):
	'''
	Makes every element in list lst zero
	'''
	for i in range(len(lst)):
		lst[i] = 0
	
def random_list(n):
	'''
	Builds a list of n integers, where each 	integer is a pseudorandom number in the 	range 0...99. Returns the random list.
	'''

	import random
	result = []
	for i in range(n):
		rand = random.randrange(100)
		result += [rand]
	return result

def main():
	a = [2, 4, 6, 8]
	#print the contents of the list
	print(a)
	#compute and display sum
	print(sum(a))
	#zero out all the elements of list
	clear(a)
	#reprint the contents of the list
	print(a)
	#compute and display sum
	print(sum(a))
	#test empty list
	a=[]
	print(a)
	print(sum(a))
	#test pseudorandom list with 10 elements
	a = random_list(10)
	print(a)
	print(sum(a))

main()

"""
TASK: sol_2_a
Make a list of all the integers two and larger. Two is a prime number, but any multiple of two
cannot be a prime number (since a multiple of two has two as a factor). Go through the rest of the list and
mark out all multiples of two (4, 6, 8, ...). Move to the next number in the list (in this case, three). If it is
not marked out, it must be prime, so go through the rest of the list and mark out all multiples of that number
(6, 9, 12, ...). Continue this process until you have listed all the primes you want.

DISPLAY THE PRIME NUMBERS BETWEEN 2 AND 500
"""

#Count the number of prime numbers less than 2 million and time how long it takes Compares the performance of two different algorithms.
		
from time import clock
from math import sqrt

def count_primes(n):
	'''
	Generates all the prime numbers from 2 to n - 1.
	n - 1 is the largest potential prime considered.
	'''
	start = clock() # Record start time

	count = 0
	for val in range(2, n):
		result = True # Provisionally, n is prime
		root = int(sqrt(val) + 1)
		# Try all potential factors from 2 to the square root of n
		trial_factor = 2
		while result and trial_factor <= root:
			result = (val % trial_factor != 0 ) # Is it a factor?
			trial_factor += 1 # Try next candidate
		if result:
			count += 1

	stop = clock() # Stop the clock
	print("Count =", count, "Elapsed time:", stop - start, "seconds")

def seive(n):
	'''
	Generates all the prime numbers from 2 to n - 1.
	n - 1 is the largest potential prime considered.
	Algorithm originally developed by Eratosthenes.
	'''

	start = clock() # Record start time

	# Each position in the Boolean list indicates
	# if the number of that position is not prime:
	# false means "prime," and true means "composite."
	# Initially all numbers are prime until proven otherwise
	nonprimes = n * [False] # Global list initialized to all False

	count = 0

	# First prime number is 2; 0 and 1 are not prime
	nonprimes[0] = nonprimes[1] = True

	# Start at the first prime number, 2
	for i in range(2, n):
	# See if i is prime
	if not nonprimes[i]:
		count += 1
		# It is prime, so eliminate all of its
		# multiples that cannot be prime
		for j in range(2*i, n, i):
			nonprimes[j] = True
	# Print the elapsed time
	stop = clock()
	print("Count =", count, "Elapsed time:", stop - start, "seconds")


def main():
	count_primes(2000000)
	seive(2000000)

main()











