import math

def isprime(tea):
    if tea <= 1:
        return False
    blah = int(math.sqrt(tea)) + 1
    for i in range(2, blah):
        if tea%i == 0:
            return False
    return True


def permy():
    finish = False
    term1 = 1488
    while not finish:
        term1 = term1 + 1
        if isprime(term1):
            for interval in range(4, int(5000-((term1+1)/2))):
                term2 = term1 + interval
                term3 = term2 + interval
                if isprime(term2) and isprime(term3):
                    s1 = str(term1)
                    s2 = str(term2)
                    s3 = str(term3)
                    if sorted(s1) == sorted(s2):
                        if sorted(s1) == sorted(s3):
                            return [s1,s2,s3]
