# -*- coding: utf-8 -*-
"""
Practising dictionaries

Author: Kriyative Edge

"""

#####Python Program to Add a Key-Value Pair to the Dictionary#####

key=int(input("Enter the key (int) to be added:"))		#user must enter a key-value pair and store it in seperate variables
value=int(input("Enter the value for the key to be added:"))	#a dictionary is declared and initialized to an empty dicitonary
d={}
d.update({key:value})						#the update() function is used to add the key-value pair to the dictionary
print("Updated dictionary is:")					#the final dictionary is printed
print(d)


"""
RUN TIME TEST CASES:
Enter the key (int) to be added:12
Enter the value for the key to be added:34
Updated dictionary is:
{12: 34}
"""

#####Python Program to Concatenate Two Dictionaries Into One#####

#user must enter declare and initialize two dictionaries with a few key-value pairs and store it in seperate variables				
d1={'A':1,'B':2}				
d2={'C':3}	
#the update() function is used to add the key-value pair from the second to the first dictionary.
d1.update(d2)
print("Concatenated dictionary is:")
print(d1)		#the final updated dictionary is printed


#####Python Program to Check if a Given Key Exists in a Dictionary or Not#####

d={'A':1,'B':2,'C':3}
#user must enter the key to be checked and store it in a variable
key=raw_input("Enter key to check:")
#an if statement and the in operation is used to check if the key is present in the list containing the keys of the dictionary
if key in d.keys():
      print("Key is present and value of the key is:")	#if it is present, the value of the key is printed
      print(d[key])
else:
      print("Key isn't present!")	#if it isn't present, "key isn't present! is printed


#####Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x)#####

#use must enter a number and store it in a variable
n=int(input("Enter a number:"))
#a dictionary is declared and initialized to values
d={x:x*x for x in range(1,n+1)}
#final dictionary is printed
print(d)


#####Python Program to Map Two Lists into a Dictionary#####

#User must enter the number of elements in the list and store it in a variable
keys=[]
#User must enter the values to the same number of elements into the list
values=[]
n=int(input("Enter number of elements for dictionary:"))
print("For keys:")
#The append function obtains each element from the user and adds the same to the end of the list as many times as the number of elements taken
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    keys.append(element)
print("For values:")
#The same of 2 and 3 is done for the second values list also.
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    values.append(element)
#The zipped lists are then merged to form a dictionary using dict()
d=dict(zip(keys,values))	#The two lists are merged together using the zip() function
#The dictionary formed from the two lists is then printed
print("The dictionary is:")
print(d)


#####Python Program to Form a Dictionary from an Object of a Class#####

#A class named A is declared
class A(object):  
     def __init__(self):  		#The keys are initialized with their values in the __init__ method of the class
         self.A=1  
         self.B=2  
obj=A()  				#The dictionary is formed using the object of the class and by using the __dict__ method
print(obj.__dict__)			#The dictionary formed from the object of the class is printed

















