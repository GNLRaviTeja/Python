# -*- coding: utf-8 -*-

"""
Practice problem
Check the program below:
1. It has one error, try to rectify it
2. If your program works fine then, why does it get to the else clause in the first place?

Observe the program, write down the expected answer before running the program and check it

Author: Kriyative Edge
"""

x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x, "= 1.0")
else:
    print(x, "is not 1.0")


"""
Explanation:
-------------
1. We now see that the test x == 1.0 produces the result False because the calue to which x is bound is not exactly 1.0.
2. What gets printed if we add to the end of the else class the code print x == 10*0.1?
It prints False because during atleast one iteration of the loop python ran out of significant digits and dit
some rounding.
3. So, adding 0.1 ten times does not produce the same value as multiplying 0.1 by 10.

FACTS:
-------
In python 2 a strange thing happens. Because the print statemtn does some automatic
rounding, the else clause would print 1.0 is not 1.0
"""

