import math

def plobz(thing):
    highest = 0
    highnum = 0
    for i in range(2, thing):
        num = i
        chain = 0
        check = 0
        while check == 0:
            if num % 2 == 0:
                num = num/2
                chain = chain + 1
            elif num != 1:
                num = num*3 + 1
                chain = chain + 1
            else:
                check = 1
                chain = chain + 1
        if chain > highest:
            highest = chain
            highnum = i
    print(highnum, highest)

def showchain(thing):
    num = thing
    check = 0
    chain = [num]
    while check == 0:
        if num % 2 == 0:
            num = num/2
            chain = chain + [num]
        elif num != 1:
            num = num*3 +1
            chain = chain + [num]
        else:
            check = 1
    print(chain)
            
