# -*- coding: utf-8 -*-
"""
Python makes is easy for developers to package their functions into modules. These modules can be developed independently from the programs that use them, just as we have been using the
functions in the standard math and random modules.

Author: Kriyative Edge
"""
#creating a module primecode.py
# Contains the definition of the is_prime function
from math import sqrt

# Returns True if non-negative integer n is prime;
# otherwise, returns false
def is_prime(n):
	trial_factor = 2
	root = sqrt(n)

	while trial_factor <= root:
		if n % trialFactor == 0: # Is trialFactor a factor?
			return False; # Yes, return right away

	return True; # Tried them all, must be prime

"""
This code primecode.py file can be used by other python programs. In the simplest case, this module appears in the same directory (folder) as the client code file that uses it.
Below code usingprimecode.py contains a sample client program that uses our packaged is_prime function
"""

from primecode import is_prime

def main():
	num = int(input("Enter an integer: "))
	if is_prime(num):
		print(num, "is prime")
	else:
		print(num, "is NOT prime")
