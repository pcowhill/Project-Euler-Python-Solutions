import math

def divy():
    set = {'0','1','2','3','4','5','6','7','8','9'}
    answers = []
    for a in set:
        for b in set-{a}:
            for c in set-{a,b}:
                for d in set-{a,b,c}:
                    for e in set-{a,b,c,d}:
                        for f in set-{a,b,c,d,e}:
                            for g in set-{a,b,c,d,e,f}:
                                for h in set-{a,b,c,d,e,f,g}:
                                    for i in set-{a,b,c,d,e,f,g,h}:
                                        for j in set-{a,b,c,d,e,f,g,h,i}:
                                            num = a+b+c+d+e+f+g+h+i+j
                                            if int(num[1:4]) % 2 == 0:
                                                if int(num[2:5]) % 3 == 0:
                                                    if int(num[3:6]) % 5 == 0:
                                                        if int(num[4:7]) % 7 == 0:
                                                            if int(num[5:8]) % 11 == 0:
                                                                if int(num[6:9]) % 13 == 0:
                                                                    if int(num[7:10]) % 17 == 0:
                                                                        answers.append(int(num))
    print(sum(answers))
