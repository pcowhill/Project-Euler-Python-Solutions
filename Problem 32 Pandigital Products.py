import math

def Pr32():
    total = []
    for i in range(1,50000):
        if i%500 == 0:
            print(str(i/500)+'%')
        for j in range(1,i):
            test = ''.join(sorted(str(i)+str(j)+str(i*j)))
            if test == '123456789':
                total.append(i*j)
                break
    print(sum(set(total)))
