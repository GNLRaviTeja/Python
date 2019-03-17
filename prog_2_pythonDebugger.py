# -*- coding: utf-8 -*-
"""
DEBUGGING USING INBUILT PYTHON LIBRARY FUNCTIONS
 pdb — The Python Debugger

The Python debugger is an interactive source code debugger for Python programs. It can set conditional breakpoints and single stepping at the source line level. It also supports inspection of stack frames, source code listing, and evaluation of arbitrary Python code in any stack frame’s context. Other facilities include post-mortem debugging.


Author: Kriyative Edge

"""
# importing the pdb library
import pdb

#consider the below code
import pdb
x=8
def power_of_itself(a):
    return a**a
pdb.set_trace()
seven=power_of_itself(7)
print(seven)
three=power_of_itself(3)
print(three)

#pdb can easily help to create break points easily in the command prompt
"""
We first import pdb. Then, we define a variable ‘x’ with the value 8. Next, we define a function ‘power_of_itself’ that returns a number to its own power.
Now here, we slip in a breakpoint in the code; we enter the debugger. The next statement is a call to ‘power_of_itself’, with the argument 7, storing the return value into the variable ‘seven’. After that, we print the value of ‘seven’. Finally, we store the return value of power_of_itself(3) into the variable ‘three’, and print it out.

"""

#ALL THE KEY PROCESS HAPPENS FROM HERE

"""
Executing the above code gives you the below output
----------------------------
tej@tej-PC:~/Desktop/Programs/Excercises$ python3 pythonDebugger.py 
> /home/tej/Desktop/Programs/Excercises/pythonDebugger.py(21)<module>()
-> seven=power_of_itself(7)
(Pdb)
----------------------------

As you can see, the prompt is at the first line after the breakpoint we set in our code. This is a call to ‘power_of_itself’ with the argument 7. Now we’re at the debugger, and we can type in some Python debugger commands to proceed with the debugging.

a		-	argumentlist
c or cont	-	creates a breakpoint in the program execution
h		-	help for a certain command
j		-	jumps to the next line to be executed
l		-	prints the source code around the line
p		-	evaluates the expression in the current context and prints its value

we can type any of the above characters in the debugging mode and check or modify the context easily


*** DEBUGGING TECHNIQUES IS ALL ABOUT IDENTIFYING EXACT LOCATION WHERE ERROR IS OCCURED
IF WE CANNOT FIND THE EXACT LOCATION OF ERROR, WE NEED TO MAKE OUR PROGRAM TO RUN THE CODE STEP BY STEP OR LINE BY LINE USING 'c' OR 'cont' FUNCTION
***

""" 
























