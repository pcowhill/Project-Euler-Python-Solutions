import math

def tissue(steely):
    trevor = [2]
    for w in range(3, steely):
        if w % 2000 == 0:
            print(len(trevor), 100 * w / steely, '%')
        for h in range(2, w):
            if w % h == 0:
                break
            elif h == math.ceil(math.sqrt(w)):
                trevor.append(w)
                break
            else:
                continue
    print(sum(trevor))
