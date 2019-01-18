import math
import fractions

def cony(top):
    elist = [2]
    for i in range(1,top):
        elist.append(1)
        elist.append(2*i)
        elist.append(1)
    elist.reverse()
    prevnum = elist[0]
    prevden = 1
    for i in elist[1:]:
        newnum = prevden + i*prevnum
        prevden = prevnum
        prevnum = newnum
    #numerator = prevnum/fractions.gcd(prevnum, prevden)
    numerator = prevnum
    answernum = '{:.0f}'.format(numerator)
    answerden = '{:.0f}'.format(prevden)
    print(answernum + '/' + answerden)
        
