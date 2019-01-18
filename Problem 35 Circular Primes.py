import math

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True


def primez(top):
    total = 0
    for i in range(2,top):
        if isPrime(i):
            tf = True
            for j in range(1,len(str(i))):
                x = str(i)[j:] + str(i)[:j]
                x = float(x)
                if not isPrime(x):
                    tf = False
            if tf == True:
                total += 1
    print(total)
