import math

def digitcancel():
    numerators = []
    denominators = []
    for i in range(2,100):
        for j in range(1,i):
            for k in str(j):
                if k in str(i):
                    newj = '0' + str(j).replace(k,"")
                    newi = '0' + str(i).replace(k,"")
                    if int(newi) != 0:
                        if int(newj)/int(newi) == j/i:
                            numerators.append(j)
                            denominators.append(i)
    print(numerators)
    print(denominators)
