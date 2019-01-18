import math

def jeff(quiggles):
    cheese = 0
    for x in range(2, quiggles):
        if quiggles % x == 0:
            dennis = quiggles/x
            for y in range(2, math.ceil(math.sqrt(dennis)) + 1):
                if dennis % y == 0:
                    break
                elif y == math.ceil(math.sqrt(dennis)):
                    print('This is the one!', dennis)
                    global cheese
                    cheese = 1
                    break
                else:
                    continue
            if cheese == 1:
                break
            else:
                continue
        else:
            continue
