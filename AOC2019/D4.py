

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
    strnum = str(num)
    for i in range(len(strnum)-1):
        if i > len(strnum)+1:
            break
        if int(strnum[i]) <= int(strnum[i+1]):
            continue
        else:
            return False
    return True

assert neverDecrease(123789) == True
assert neverDecrease(113389) == True
assert neverDecrease(123879) == False
assert neverDecrease(923781) == False


def minTwoAdjacent(num):
    strnum = str(num)
    for i in range(len(strnum)-1): #might be 1 off maybe -1
        if i > len(strnum)+1:
            return False
        if strnum[i] == strnum[i+1]:
            return True
    return False

assert (minTwoAdjacent(121211)) == True
assert (minTwoAdjacent(111212)) == True
assert (minTwoAdjacent(1212212)) == True
assert (minTwoAdjacent(121212)) == False
assert (minTwoAdjacent(123789)) == False

# print(len(producePossiblePWs(inputstart,inputend)))


#part 2
def p2producePossiblePWs(startrange,endrange):
    possiblepws = []
    for i in range(startrange,endrange):#endrange +1?
        if neverDecrease(i):
            if ONLYTWO(i):
                possiblepws.append(i)
    return possiblepws

def ONLYTWO(num):

    strnum = "!" + str(num)
    for i in range(len(strnum)-1):
        if i == 0:
            continue
        if i+2 > len(strnum)-1:
            if strnum[i] == strnum[i+1] and strnum[i] > strnum[i-1]:
                return True
            return False
        if strnum[i] == strnum[i+1] and strnum[i] < strnum[i+2] and strnum[i]>strnum[i-1]:
            return True

#number needs ONLY ONE pair that isnt part of a larger group
assert (ONLYTWO(112233)) == True
assert (ONLYTWO(123444)) == False
assert (ONLYTWO(111122)) == True
assert (ONLYTWO(111122)) == True
assert (ONLYTWO(111122)) == True


print(len(p2producePossiblePWs(inputstart,inputend)))

