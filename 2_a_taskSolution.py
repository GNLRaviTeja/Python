# -*- coding: utf-8 -*-
"""
CALCULATOR

Author: Kriyative Edge

Task:
------
design a calculator 
	- use your imagination
	- need to perform atleast 2 arithmetic operations
	- should support user to quit when ever he wish for
"""

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

# main
# Runs a command loop that allows users to
# perform simple arithmetic.

def main():
	result = 0.0
	done = False	#initially not done
	while not done:
		choice = menu()	#get user's choice
		if choice == "A" or choice == "a": # Addition
			arg1 = float(input("Enter arg 1: "))
			arg2 = float(input("Enter arg 2: "))
			result = arg1 + arg2
			print(result)
		elif choice == "S" or choice == "s": # Subtraction
			arg1 = float(input("Enter arg 1: "))
			arg2 = float(input("Enter arg 2: "))
			result = arg1 - arg2
			print(result)
		elif choice == "P" or choice == "p": # Print
			print(result)
		elif choice == "H" or choice == "h": # Help
			help_screen()
		elif choice == "Q" or choice == "q": # Quit
			done = True

main()










