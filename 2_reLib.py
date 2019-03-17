#Program to use RE library and and print specific decimal values to their specific alphabet
import re
p = re.compile(r'\d+')

s = "Over \u0e55\u0e57 57 flavours" #random alphabets in malayalam language
m = p.search(s)
#prints the above two alphabets in malayalam language repo and prints it
print(repr(m.group()))

"""
Refer docs.python.org for more details and explanations
"""
