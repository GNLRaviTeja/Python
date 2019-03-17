#String Manipulation
#To manipulate strings, we can use some of Pythons built-in methods.
#Creation
word = "Hello World"
print (word)

#Accessing
#Use [ ] to access characters in a string

word = "Hello World"
letter=word[0]
print (letter)


#Length
word = "Hello World"

len(word)

#Finding
word = "Hello World"

print (word.count('l'))	# count how many times l is in the string
print (word.find("H"))  	# find the word H in the string
print (word.index("World")) 	# find the letters World in the string

#Count
s =  "Count, the number     of spaces"
print (s.count(' '))

#Slicing
#Use [ # : # ] to get set of letter
#Keep in mind that python, as many other languages, starts to count from 0!! 

word = "Hello World"

print (word[0])        #get one char of the word
print (word[0:1])       #get one char of the word (same as above)
print (word[0:3])        #get the first three char
print (word[:3])         #get the first three char
print (word[-3:])        #get the last three char
print (word[3:])         #get all but the three first char
print (word[:-3])        #get all but the three last character
word = "Hello World"
 
#word[start:end]    	# items start through end-1
#word[start:]            # items start through the rest of the list
#word[:end]              # items from the beginning through end-1
#word[:]                 # a copy of the whole list

#Split Strings
word = "Hello World"
print(word.split(' '))  # Split on whitespace

#Startswith / Endswith
word = "hello world"

print(word.startswith("H"))
print(word.endswith("d"))
print(word.endswith("w"))

#Repeat Strings
print ("."* 10)	# prints ten dots


#Replacing
word = "Hello World"

print(word.replace("Hello", "Goodbye"))

#Changing Upper and Lower Case Strings
string = "Hello World"
print (string.upper())
print (string.lower())
print (string.title())
print (string.capitalize())
print (string.swapcase())

#Reversing
string = "Hello World"
print (' '.join(reversed(string)))

#Strip

#Python strings have the strip(), lstrip(), rstrip() methods for removing 
#any character from both ends of a string. 
#If the characters to be removed are not specified then white-space will be removed

word = "Hello World"
#Strip off newline characters from end of the string
print (word.strip(''))

#strip()     #removes from both ends
#lstrip()    #removes leading characters (Left-strip)
#rstrip()    #removes trailing characters (Right-strip)

word = "    xyz    "
print (word)
print (word.strip())
print (word.lstrip())
print (word.rstrip())

#Concatenation
#To concatenate strings in Python use the "+" operator. 
print("Hello " + "World") # = "Hello World"
print("Hello " + "World" + "!")# = "Hello World!"

#Join
print (":".join(word))  # #add a : between every char
print (" ".join(word))  # add a whitespace between every char

#Testing
#A string in Python can be tested for truth value. 
#The return type will be in Boolean value (True or False)

word = "Hello World"
 
print(word.isalnum())         #check if all char are alphanumeric 
print(word.isalpha())         #check if all char in the string are alphabetic
print(word.isdigit())         #test if string contains digits
print(word.istitle())         #test if string contains title words
print(word.isupper())         #test if string contains upper case
print(word.islower())         #test if string contains lower case
print(word.isspace())         #test if string contains spaces
print(word.endswith('d'))     #test if string endswith a d
word.startswith('H')   #test if string startswith H
