import math

def isprime(tea):
    if tea <= 1:
        return False
    blah = int(math.sqrt(tea)) + 1
    for i in range(2, blah):
        if tea%i == 0:
            return False
    return True

def primy():
    num = 10
    answers = []
    while len(answers) < 11:
        num = num+1
        if isprime(num):
            istrun = True
            for i in range(1,len(str(num))):
                if not isprime(int(str(num)[:i])):
                    istrun = False
                if not isprime(int(str(num)[i:])):
                    istrun = False
            if istrun:
                answers.append(num)
                print(len(answers),num)
    print(sum(answers))
