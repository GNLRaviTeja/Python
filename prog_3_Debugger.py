# -*- coding: utf-8 -*-
"""
DEBUGGING USING INBUILT PYTHON LIBRARY FUNCTIONS
 pdb — The Python Debugger

NOW LET US LOOK AT A PRACTISE EXAMPLE

Author: Kriyative Edge

"""
#consider the following code
#understand the process of code and try to identify the possibilities of error before executing

def funcA(first_val, second_val):
    result = (first_val*2) - (second_val/4)
    return result

def functionB(first_val=23, last_val=72):
    response = funcA(first_val, last_vale)
    result = response * first_val / 7
    return result
    
functionB(33,88) # we are evaluating the funciton

"""
If we try running the snippet above, we would get an error:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in functionB
NameError: global name 'last_vale' is not defined
"""

#We should place our breakpoint. A breakpoint tells the Python interpreter to pause execution at a particular point in our application
#From the error message above, we can infer that the problem is coming from the functionB function
#To debug the problem, we would add a breakpoint to the start of our functionB implementation

def funcA(first_val, second_val):
    result = (first_val*2) - (second_val/4)
    return result

def functionB(first_val=23, last_val=72):
    import pdb
    pdb.set_trace()
    response = funcA(first_val, last_vale)
    result = response * first_val / 7
    return result
    
functionB(33,88)

#Executing, will make you enter into debugging console (pdb)
#As observed in the previous program, you can use all the key commands to control the program

#after compiling a line if you type 'n' inside (pdb) moves to next line and compiles it
#using this you can identify on which line you are getting the error

#To get python to continue execution of the program, we type c which means continue and the program executes as usual

#####################################################################################################################################

#Now let's look into the same program with different type of error

def funcA(first_val, second_val):
    result = (first_val * 2) - (second_val / 0) 	#dividing with zero gives trace back error
    return result


def functionB(first_val=23, last_val=72):
    # we would place our break point here
    response = funcA(first_val, last_val)
    result = response * first_val / 7
    return result


functionB(33, 88)

"""
Traceback (most recent call last):
  File "sample.py", line 13, in <module>
    functionB(33, 88)
  File "sample.py", line 8, in functionB
    response = funcA(first_val, last_val)
  File "sample.py", line 2, in funcA
    result = (first_val * 2) - (second_val / 0)
ZeroDivisionError: integer division or modulo by zero
"""

#as discussed we need to place our breakpoint
#since in the first program, we already had placed out breakpoint in functionB. Let us use the same program rather changing the breakpoint position

def funcA(first_val, second_val):
    result = (first_val*2) - (second_val/4)
    return result

def functionB(first_val=23, last_val=72):
    import pdb
    pdb.set_trace()
    response = funcA(first_val, last_vale)
    result = response * first_val / 7
    return result
    
functionB(33,88)

#we worked with 'n' condition above. Now if we use 's' --> step function, the compilation jumps to another function. That's how you jump to different function and use 'n' and 'c' functions to control the process and find the error location

#IF YOU WISH TO ADD MORE NUMBER OF TRACES, WE CAN RUN MULTIPLE CONSOLES SIMULTANEOUSLY AND VERIFY IT. BUT THE BEST WAY IS TO USE THE PDB LIBRARY AT THE BEGINNING AND PLACE TRACES WITH DIFFERENT NAMES AT DIFFERENT LOCATIONS. 
#JUMP TO YOUR REQUIRED TRACE OR BREAKPOINT EASILY



"""
GO THROUGH ALL THE PREVIOUS PROGRAMS YOU MADE, CHOSE FEW EXAMPLES AND TRY TO PRACTISE AND UNDERSTAND DIFFERENT TYPES OF ERRORS THAT OCCUR AND HOW TO IDENTIFY

IN THE NEXT SESSIONS, WE WILL LOOK INTO ERROR HANDLING METHODS AND EXCEMPTIONS DURING PROGRAMMING
"""
