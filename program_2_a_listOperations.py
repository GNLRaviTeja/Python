# -*- coding: utf-8 -*-
"""
LISTS

Author: Kriyative Edge

"""
#List refers to collection of objects; it represents an ordered sequence of data.

lst = [2, -3, 0, 4, -1]
#Printing is done in two ways
#printing literals
print([2, -3, 0, 4, -1])
#printing the list variable
print(lst)

#Accessing elements in a list
lst = [2, -3, 0, 4, -1] # Assign the list
lst[0] = 5 # Make the first element 5
print(lst[1]) # Print the second element
lst[4] = 12 # Make the last element 12
print(lst) # Print a list variable
print([10, 20, 30][1]) # Print second element of literal list

#List cane be heterogeneous
collection = [24.2, 4, 'word', eval, 19, -0.03, 'end']
print(collection[0])
print(collection[1])
print(collection[2])
print(collection[3])
print(collection[4])
print(collection[5])
print(collection[6])
print(collection)

#The elements of a list extracted with [] can be treated as any other variable
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Print the fourth element
print(nums[3])
# The third element is the average of two other elements
nums[2] = (nums[0] + nums[9])/2;
# Assign elements at indices 1 and 4 from user input
# using tuple assignment
nums[1], nums[4] = eval(input("Enter a, b: "))

#creating a heterolist with for loop
collection = [24.2, 4, 'word', eval, 19, -0.03, 'end']
for item in collection:
	print(item) # Print each element

#The name len stands for length. We can print the elements of a list in reverse order as follows

nums = [2, 4, 6, 8]
# Print last element to first (zero index) element
for i in range(len(nums) - 1, -1, -1):
	print(nums[i])

#The statement
a = [2, 4, 6, 8]
#assigns the given list literal to the variable a. The expression
a + [1, 3, 5]
#evaluates to the list [2, 4, 6, 8, 1, 3, 5], but the statement does not change the list to which a refers.
#The statement
a = a + [1, 3, 5]
#actually reassigns a to the new list [2, 4, 6, 8, 1, 3, 5]. The statement
a += [10]
#updates a to be the new list [2, 4, 6, 8, 1, 3, 5, 10]. Observe that the + will concatenate two lists,
#but it cannot join a list and a non-list. The following statement
####a += 20
#is illegal since a refers to a list, and 20 is an integer, not a list.If used within a program under these
#conditions, this statement will produce a run-time exception.

#Program to build a lists as program executes
# Build a custom list of non-negative integers specified by the user

def make_list():
	'''
	Builds a list from input provided by the user.
	'''
	result = []	#List to return is initially empty
	in_val = 0 # Ensure loop is entered at least once
	while in_val >= 0:
		in_val = int(input("Enter integer (-1 quits): "))
		if in_val >= 0:
			result = result + [in_val] # Add item to list
	return result

def main():
	col = make_list()
	print(col)
main()

#There are several ways to build a list without explicitly listing every element in the list. We can use the range function to produce a regular sequence of integers. The range object returned by range is not itself a list, but we can make a list from a range using the list function

def main():
	a = list(range(0, 10))
	print(a)
	a = list(range(10, -1, -1))
	print(a)
	a = list(range(0, 100, 10))
	print(a)
	a = list(range(-5, 6))
	print(a)
main()

#build several lists using the * list multiplication operator

def main():
	a =[0] * 10
	print(a)

	a = [3.4] * 5
	print(a)
	
	a = 3 * ['ABC']
	print(a)

	a = 4 * [10, 20, 30]
	print(a)

main()

#Program to create a list of average numbers input by users

def main():
	# Set up variables
	sum = 0.0
	NUMBER_OF_ENTRIES = 5
	numbers = []

	# Get input from user
	print("Please enter", NUMBER_OF_ENTRIES, "numbers: ")
	for i in range(0, NUMBER_OF_ENTRIES):
		num = eval(input("Enter number " + str(i) + ": "))
		numbers += [num]
		sum += num;

	# Print the numbers entered
	print(end="Numbers entered: ")
	for num in numbers:
		print(num, end=" ")
	print() # Print newline

	# Print average
	print("Average:", sum/NUMBER_OF_ENTRIES)

main() # Execute main

#List assignments

a = [10, 20, 30, 40]
b = [10, 20, 30, 40]
print('a =', a)
print('b =', b)
b[2] = 35
print('a =', a)
print('b =', b)

#List aliasing

a = [10, 20, 30, 40]
b = a
print('a =', a)
print('b =', b)
b[2] = 35
print('a =', a)
print('b =', b)

#List equivalence

# a and b are distinct lists that contain the same elements
a = [10, 20, 30, 40]
b = [10, 20, 30, 40]
print('Is ', a, ' equal to ', b, '?', sep='', end=' ')
print(a == b)

print('Are ', a, ' and ', b, ' aliases?', sep='', end=' ')
print(a is b)

# c and d alias are distinct lists that contain the same elements
c = [100, 200, 300, 400]
d = c # Makes d an alias of c
print('Is ', c, ' equal to ', d, '?', sep='', end=' ')
print(c == d)

print('Are ', c, ' and ', d, ' aliases?', sep='', end=' ')
print(c is d)

#List copy

def list_copy(lst):
	result = []
	for item in lst:
		result += [item]
	return result
def main():
	# a and b are distinct lists that contain the same elements
	a = [10, 20, 30, 40]
	a = list_copy(a)	#Make a copy
	print('a =', a, ' b =', b)

	print('Is ', a, ' equal to ', b, '?', sep='', end=' ')
	print( a== b)

	print('Are ', a, ' and ', b, ' aliases?', sep='', end=' ')
	print(a is b)

	b[2] = 35 # Change an element of b
	print('a =', a, ' b =', b)

main()

#List bounds# Make a list containing 100 zeros
v = [0] * 100
# User enters x at run time
x = int(input("Enter an integer: "))
# Ensure index is within list bounds
if 0 <= x < len(v):
	v[x] = 1 # This should be fine
else:
	print("Value provided is out of range")

#Bad reverse
#program attempts to print the list’s elements in reverse order, but it fails to stay inside the bounds of the list.

def make_list():
	'''
	Builds a list from input provided by the user.
	'''
	result = [] # List to return is initially empty
	in_val = 0 # Ensure loop is entered at least once
	while in_val >= 0:
		in_val = int(input("Enter integer (-1 quits): "))
		if in_val >= 0:
			result = result + [in_val] # Add item to list
	return result

def main():
	col = make_list()
	#print the list in reverse
	for i in range(len(col), 0, -1):
		print(col[i], end=" ")
	print()
main()

'''
The for statement
for i in range(len(col), 0, -1):
	print(col[i], end=" ")
considers first the element at col[len(col)], which is one index past the end of the list. The corrected
for statement is
for i in range(len(col) - 1, -1, -1):
	print(col[i], end=" ")
'''
#negative indices

def main():
	data = [10, 20, 30, 40, 50, 60]

	# Print the individual elements with negative indices
	print(data[-1])
	print(data[-2])
	print(data[-3])
	print(data[-4])
	print(data[-5])
	print(data[-6])

	print('------')
	#print the list contents in reverse using negative indices
	for i in range(-1, -len(data) -1, -1):
		print(data[i], end=' ')
	print()	#print new line

main()	#execute main

#List slicing

lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst) # [10, 20, 30, 40, 50, 60, 70, 80]
print(lst[0:3]) # [10, 20, 30]
print(lst[4:8]) # [50, 60, 70, 80]
print(lst[2:5]) # [30, 40, 50]
print(lst[-5:-3]) # [40, 50]
print(lst[:3]) # [10, 20, 30]
print(lst[4:]) # [50, 60, 70, 80]
print(lst[:]) # [10, 20, 30, 40, 50, 60, 70, 80]
print(lst[-100:3]) # [10, 20, 30]
print(lst[4:100]) # [50, 60, 70, 80]

#program to pring prefixes and suffixes of the list

a = [1, 2, 3, 4, 5, 6, 7, 8]
print('Prefixes of', a)
for i in range(0, len(a) + 1):
	print('<', a[0:i], '>', sep='')
print('----------------------------------')
print('Suffixes of', a)
for i in range(0, len(a) + 1):
	print('<', a[i, len(a) + 1], '>', sep='')

#List slice assignement
#A slice assignment can modify a list by removing or adding a subrange of elements in an existing list.

lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst) # Print the list
lst[2:5] = ['a', 'b', 'c'] # Replace [30, 40, 50] segment with ['a', 'b', 'c']
print(lst)
print('==================')
lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst) # Print the list
lst[2:6] = ['a', 'b'] # Replace [30, 40, 50, 60] segment with ['a', 'b']
print(lst)
print('==================')
lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst) # Print the list
lst[2:2] = ['a', 'b', 'c'] # Insert ['a', 'b', 'c'] segment at index 2
print(lst)
print('==================')
lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst) # Print the list
lst[2:5] = [] # Replace [30, 40, 50] segment with []
print(lst)






