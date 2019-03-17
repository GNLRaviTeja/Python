"""
Program to represent unicode UTF-8 into the code and print something in different
languages

These techniques are mostly used in creating voice translations and language translations

We need other libraries as well for working with language translations. Below are just overview
of UTF-8 unicode technique

"""

#-*- coding: utf-8 -*-

# "hello, how are you?" is the string we are trying to read in different languages

print("Hola como estas?") #SPANISH
print("Hallo, wie geht's dir?")  #GERMAN
print("你好，你好吗？")    #CHINESE

# Program to encode a language data into hexadecimal format and decoding to
# actual language again, using utf-8
byte_string = '你好，你好吗？' #hello, how are you?
unicode_string = byte_string.encode('utf-8')
output_string = unicode_string.decode('utf-8')
print(unicode_string)
print(output_string)

# Program to read a latin alphabets and print the output

# -*- coding: latin-1 -*-

u = 'abcdé' #This program gives the decimal output of combination of alphabets
print(ord(u[-1]))


