
inputstart, inputend = 109165,576723
# Dad's input
# inputstart, inputend = 353096, 843212

def producePossiblePWs(startrange,endrange):
    possiblepws = []
    for i in range(startrange,endrange):#endrange +1?
        if neverDecrease(i):
            if minTwoAdjacent(i):
                possiblepws.append(i)
    return possiblepws

def neverDecrease(num):
    #Left to right digits never decrease
    pointer = 0
    strnum = str(num)
    for i in range(len(strnum)-1):
        if pointer > len(strnum)+1:
            break
        if int(strnum[pointer]) <= int(strnum[pointer+1]):
            pointer += 1
            continue
        else:
            return False
    return True

assert neverDecrease(123789) == True
assert neverDecrease(113389) == True
assert neverDecrease(123879) == False
assert neverDecrease(923781) == False


def minTwoAdjacent(num):
    pointer = 0
    strnum = str(num)
    for i in range(len(strnum)-1): #might be 1 off maybe -1
        if pointer > len(strnum)+1:
            return False
        if strnum[pointer] == strnum[pointer+1]:
            return True
        else:
            pointer += 1
    return False

assert (minTwoAdjacent(121211)) == True
assert (minTwoAdjacent(111212)) == True
assert (minTwoAdjacent(1212212)) == True
assert (minTwoAdjacent(121212)) == False
assert (minTwoAdjacent(123789)) == False

print(len(producePossiblePWs(inputstart,inputend)))
