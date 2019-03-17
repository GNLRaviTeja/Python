def printName(firstName,lastName,reverse):
    if reverse:
        print(lastName + " , " + firstName)
    else:
        print(firstName, lastName)
#printName('Grand', 'prix')
printName('Grand', 'prix', True)
