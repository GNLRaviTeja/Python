# -*- coding: utf-8 -*-

"""
A human player has to guess a number between a range of 1 to n.
The player inputs his guess. The program informs the player, if this number is larger,
smaller or equal to the secret number, i.e. the number which the program has randomly created.
If the player wants to gives up, he or she can input a 0 or a negative number. 
Hint: The program needs to create a random number.
Therefore it's necessary to include the module "random".

Author: Kriyative Edge
"""

#This program is having some troubles, please go through the program and rectify the problems occured


import random
n = 20
guessedNumber = int(n * random.random()) + 1  # Guessing number should be incrementing to increment loop count
guess = 0
while guess != guessedNumber:   # Loop should be negating to create an infinite loop
    guess = int(input("New number: "))
    if guess > 0:
        if guess > guessedNumber:
            print("Number too large")
        elif guess < guessedNumber:
            print("Number too small")
    else:
        print("Sorry that you're giving up!")
        break       #A break should accompany to break the program if the user is giving up
else:
    print("Congratulation. You made it!")

#Now try to modify program where user gets 3 chances to guess a number else should print 'guess failed'
    

