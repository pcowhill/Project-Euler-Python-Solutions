import math

def isprime(tea):
    if tea <= 1:
        return False
    blah = int(math.sqrt(tea)) + 1
    for i in range(2, blah):
        if tea%i == 0:
            return False
    return True

maxprime = 0
maxa = 0
maxb = 0

def programify(rana, ranb):
    maxprime = 0
    maxa = 0
    maxb = 0
    for i in range(-rana, rana):
        for j in range(-ranb, ranb):
            check = True
            k = -1
            while check == True:
                k += 1
                prim = k**2+(i*k)+j
                check = isprime(prim)
            if k > maxprime:
                maxprime = k
                maxa = i
                maxb = j
    print('n^2 + ' + str(maxa) + 'n + ' + str(maxb) + ' has ' + str(maxprime) + ' primes.')
