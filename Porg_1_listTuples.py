# -*- coding: utf-8 -*-
"""
Practising lists and tuples

Author: Kriyative Edge

"""

#####Python Program to Find the Largest Number in a List#####

#User must enter the number of elements and store it in a variable
a=[]
n=int(input("Enter number of elements:"))
#User must then enter the elements of the list one by one using a for loop and store it in a list
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
#The list should then be sorted
a.sort()
#Then the last element of the list is printed which is also the largest element of the list
print("Largest element is:",a[n-1])

"""
RUN TIME TEST CASES:
Enter number of elements:3
Enter element:100
Enter element:-567
Enter element:3
Largest element is: 567
"""

#####Python Program to Find the Second Largest Number in a List#####

#User must enter the number of elements and store it in a variable
a=[]
n=int(input("Enter number of elements:"))
#User must then enter the elements of the list one by one using a for loop and store it in a list
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
#The list should then be sorted
a.sort()
#Then the last element of the list is printed which is also the largest element of the list
print("Second largest element is:",a[n-2])

#####Python Program to Put Even and Odd elements in a List into Two Different Lists#####

#User must enter the number of elements and store it in a variable
a=[]
n=int(input("Enter number of elements:"))
#User must then enter the elements of the list one by one using a for loop and store it in a list
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
even=[]
odd=[]
#Another for loop is used to traverse through the elements of the list
for j in a:
    #The if statement checks if the element is even or odd and appends them to separate lists
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
#Both the lists are printed
print("The even list",even)
print("The odd list",odd)


#####Python Program to Merge Two Lists and Sort it#####

#User must enter the number of elements for the first list and store it in a variable
a=[]
c=[]
#User must then enter the elements of the list one by one using a for loop and store it in a list
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    a.append(b)
#User must similarly enter the elements of the second list one by one
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    c.append(d)
new=a+c				#The ‘+’ operator is then used to merge both the lists
new.sort()			#The sort function then sorts the list in ascending order
print("Sorted list is:",new)	#The sorted list is then printed


#####Python Program to Find Element Occurring Odd Number of Times in a List#####

#The user is promted to enter a list
#find_odd_occurring is called on the list
def find_odd_occurring(alist):
    """Return the element that occurs odd number of times in alist.
 
    alist is a list in which all elements except one element occurs an even
    number of times.
    """
    ans = 0
 
    for element in alist:
        ans ^= element
 
    return ans
alist = input('Enter the list: ').split()
alist = [int(i) for i in alist]
ans = find_odd_occurring(alist)
#The result is then displayed
print('The element that occurs odd number of times:', ans)


#####Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number#####

#User must enter the upper and lower range for the numbers
l_range=int(input("Enter the lower range:"))
u_range=int(input("Enter the upper range:"))
#List comprehension must be used to create a list of tuples where the first number is the number itself from the given range and the second element is a square of the first number
a=[(x,x**2) for x in range(l_range,u_range+1)]
#The list of tuples which is created is printed
print(a)


#####Python program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple#####

#The function last returns the last element of each tuple in the list of tuples
def last(n):
    return n[-1]  
#The function sort returns the sorted list with the last function as its key
def sort(tuples):
    return sorted(tuples, key=last)
#User must enter a list of tuples
a=input("Enter a list of tuples:")
#The sorted list is then printed
print("Sorted:")
print(sort(a))


















