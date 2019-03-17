# -*- coding: utf-8 -*-
"""
Generating a file input output functions. Valid for text and csv formats

Author: Kriyative Edge

"""
#FILE INPUT OUTPUT SYSTEMS
#Working with TEXT files

########################################################
#Reading a Text file
#The text file sample.txt consists of information gathered from a random wikipedia page

a=str(input("Enter the name of the file with .txt extension:"))	#User must enter a file name.
file2=open(a,'r')		#The file is opened using the open() function in the read mode.
line=file2.readline()		#The readline() outside the while loop is used to read the first line of the file.
while(line!=""):
	#Inside the loop, the first line is first printed and then the remaining lines are read and subsequently printed.		
    print(line)			
    line=file2.readline()	#This continues this the end of file.
file2.close()			#The file is then closed.

#########################################################
#Program to read number of words in the text file

fname = input("Enter file name: ")	#User must enter a file name
 
num_words = 0				
 
with open(fname, 'r') as f:		#The file is opened using the open() function in the read module
    for line in f:			#A for loop is used to read through each line in the file
        words = line.split()		#Each line is split into a list of words using split()
        num_words += len(words)		#The number of words in each line is counted using len() and the count variable is incremented
print("Number of words:")
print(num_words)			#The number of words inthe file is printed

#########################################################
#Python program to read a string from the user and append it into a file

fname = input("Enter file name: ")		#User must enter a file name
file3=open(fname,"a")				#The is opened using open() function in the append mode
#A string is taken from the user, appended to the existing file and is closed
c=input("Enter string to append: \n");
file3.write("\n")
file3.write(c)
file3.close()
print("Contents of appended file:");
#The file is opened again inthe read mode
file4=open(fname,'r')
#The readline() in the while loop reads eah and every line in the file and print() prints the contents on the output screen
line1=file4.readline()
while(line1!=""):
    print(line1)
    line1=file4.readline()    
file4.close()					#Once the overall process is done the file is closed using close() function

'''
ONCE ENTERING THE FILE NAME, PROGRAM WILL ASK FOR THE NEW STRING TO BE ADDED TO THE TEXT DOCUMENT.
PROVIDING THE STRING THE TEXT FILE IS UPDATED WITH NEW ADDED STRING AT THE END
'''

#########################################################
#Python program to copy the contents of one file into another

with open("sample.txt") as f:		#The file sample.txt is opened using the open() function using the f stream
    with open("output.txt", "w") as f1:	#Another file output.txt is opened using the open() function in the write mode using the f1 stream
        for line in f:			#Each line in the file is iterated over using a for loop (in the input stream)
            f1.write(line)		#Each of the iterated lines is written into the output.txt file











