# -*- coding: utf-8 -*-
"""
DEBUGGING AS SEARCH
1. want to narrow down space of possible sources of error
2. design experiments that expose intermediate stages of computation (use print statements!), and use results to further narrow search
3. binary search can be a powerful tool for this

Author: Kriyative Edge

"""
# LOOK AT THIS PROGRAM
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False

def silly(n):
    for i in range(n):
        result = []
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')

"""
TEST - 1
----------
STEPPING THROUGH THE TESTS
1. suppose we run this code:
    ◦ we try the input ‘abcba’, which succeeds
    ◦ we try the input ‘palinnilap’, which succeeds
    ◦ but we try the input ‘ab’, which also ‘succeeds’
2. let’s use binary search to isolate bug(s)
3. pick a spot about halfway through code, and devise experiment
    ◦ pick a spot where easy to examine intermediate values

"""
################################################################################################
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False

def silly(n):
    for i in range(n):
        result = []
        elem = input('Enter element: ')
        result.append(elem)
    print(result)			#<-------- print statement
    if isPal(result):
        print('Yes')
    else:
        print('No')
"""
TEST - 2
----------
STEPPING THROUGH THE TESTS
1. at this point in the code, we expect (for our test case of ‘ab’), that result should be a list [‘a’, ‘b’]
2. we run the code, and get [‘b’].
3. because of binary search, we know that at least one bug must be present earlier in the code
4. so we add a second print, this time inside the loop

"""
################################################################################################
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False

def silly(n):
    for i in range(n):
        result = []
        elem = input('Enter element: ')
        result.append(elem)
        print(result)			#<-----print statement inside the for loop
    if isPal(result):
        print('Yes')
    else:
        print('No')
"""
TEST - 3
----------
STEPPING THROUGH THE TESTS
1. when we run with our example, the print statement returns
    ◦ [‘a’]
    ◦ [‘b’]
2. this suggests that result is not keeping all elements
    ◦ so let’s move the initialization of result outside the loop and retry

"""
################################################################################################
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = []					#<-----result pushed outside for loop
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
        print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
"""
TEST - 4
----------
STEPPING THROUGH THE TESTS
1. this now shows we are getting the data structure result properly set up, but we still have a bug somewhere
    ◦ a reminder that there may be more than one problem!
    ◦ this suggests second bug must lie below print statement;
####let’s look at isPal
    ◦ pick a point in middle of code, and add print statement again; remove the earlier print statement

"""
################################################################################################
def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse
    print(temp, x)		#<-----print statement in the first function
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')
"""
TEST - 5
----------
STEPPING THROUGH THE TESTS
1. at this point in the code, we expect (for our example of ‘ab’) that x should be [‘a’, ‘b’], but temp should be [‘b’, ‘a’], however they both have the value [‘a’, ‘b’]
2. so let’s add another print statement, earlier in the code

"""
################################################################################################
def isPal(x):
    assert type(x) == list
    temp = x
    print('before reverse', temp, x)		#<-----
    temp.reverse
    print('after reverse', temp, x)		#<-----
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')
"""
TEST - 6
----------
STEPPING THROUGH THE TESTS
1. we see that temp has the same value before and after the call to reverse
2. if we look at our code, we realize we have committed a standard bug – we forgot to actually invoke the reverse method
    ◦ need temp.reverse()
3. so let’s make that change and try again

"""
################################################################################################
def isPal(x):
    assert type(x) == list
    temp = x
    print('before reverse', temp, x)	#<----
    temp.reverse()			#<----
    print('after reverse', temp, x)	#<----
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')
"""
TEST - 7
----------
STEPPING THROUGH THE TESTS
1. but now when we run on our simple example, both x and temp have been reversed!!
2. we have also narrowed down this bug to a single line. The error must be in the reverse step
3. in fact, we have an aliasing bug – reversing temp has also caused x to be reversed
    ◦ because they are referring to the same object

"""
################################################################################################
def isPal(x):
    assert type(x) == list
    temp = x[:]		#<----
    print(temp, x)	#<----
    temp.reverse()	#<----
    print(temp, x)	#<----
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')

"""
TEST - 8
----------
STEPPING THROUGH THE TESTS
1. now running this shows that before the reverse step, the two variables have the same form, but afterwards only temp is reversed.
2. we can now go back and check that our other tests cases still work correctly

"""




