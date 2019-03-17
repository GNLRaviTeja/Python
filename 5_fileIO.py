# -*- coding: utf-8 -*-
"""
File Input / Output structure

Author: Kriyative Edge
"""

#What is a file?
"""
File is a named location on disk to store related information. It is used to permanently store data in a non-volatile memory (e.g. hard disk).

Since, random access memory (RAM) is volatile which loses its data when computer is turned off, we use files for future use of the data.

When we want to read from or write to a file we need to open it first. When we are done, it needs to be closed, so that resources that are tied with the file are freed.

Hence, in Python, a file operation takes place in the following order.

1. Open a file
2. Read or write (perform operation)
3. Close the file
"""

#HOW TO OPEN A FILE?
f = open("test.txt")    # open file in current directory
f = open("C:/Python33/README.txt")  # specifying full path

"""
Python File Modes
Mode	Description
'r'	Open a file for reading. (default)
'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'	Open in text mode. (default)
'b'	Open in binary mode.
'+'	Open a file for updating (reading and writing)
"""		

f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode

#Hence, when working with files in text mode, it is highly recommended to specify the encoding type.

f = open("test.txt",mode = 'r',encoding = 'utf-8')

#HOW TO CLOSE A FILE?
f = open("test.txt",encoding = 'utf-8')
# perform file operations
f.close()
#This method is not entirely safe. If an exception occurs when we are performing some operation with the file, the code exits without closing the file.

#A safer way is to use a try...finally block

try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()

#This way, we are guaranteed that the file is properly closed even if an exception is raised, causing program flow to stop.

"""
The best way to do this is using the with statement. This ensures that the file is closed when the block inside with is exited.
"""
#We don't need to explicitly call the close() method. It is done internally.

with open("test.txt",encoding = 'utf-8') as f:
   # perform file operations

#HOW TO WRITE TO FILE?

with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
#This program will create a new file named 'test.txt' if it does not exist. If it does exist, it is overwritten.

#HOW TO READ FROM FILES?

f = open("test.txt",'r',encoding = 'utf-8')
f.read(4)    # read the first 4 data
f.read(4)    # read the next 4 data
f.read()     # read in the rest till end of file
f.read()     # further reading returns empty string



















































