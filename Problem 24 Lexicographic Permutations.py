import math

def lexico(permutation):
    counter = 0
    for i in range(1,9999999999):
        num = str(i).zfill(10)
        if ('0' in num) and ('1' in num) and ('2' in num) and ('3' in num) and ('4' in num) and ('5' in num) and ('6' in num) and ('7' in num) and ('8' in num) and ('9' in num):
            counter +=1
            if counter % 1000 == 0:
                print(counter, i)
        if counter == permutation:
            return i
