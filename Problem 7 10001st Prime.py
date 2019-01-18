import math

def primm(rose):
    gard = [2]
    tool = 3
    counter = 1
    while counter < rose:
        for w in range(2, math.ceil(math.sqrt(tool))+1):
            if tool % w == 0:
                tool = tool + 1
                break
            elif w == math.ceil(math.sqrt(tool)):
                gard.append(tool)
                counter = counter + 1
                tool = tool + 1
                break
            else:
                continue
    print('The', rose, 'th prime number is', gard[-1])
