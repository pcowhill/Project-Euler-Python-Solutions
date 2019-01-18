import math

def distinct(top):
    listy = []
    for i in range(2, top+1):
        for j in range(2, top+1):
            listy.append(i**j)
    lister = list(set(listy))
    return len(lister)
