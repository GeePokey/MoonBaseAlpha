import math
import statistics
def readInput():
    with open(r"C:\Users\Kody\GitExperiment\MoonBaseAlpha\AOC2020\D5_kinput.txt", "r",) as f:
    # with open(r"C:\Users\Kody\GitExperiment\MoonBaseAlpha\AOC2020\good.txt", "r",) as f:
        data = f.read().split('\n')
    # input = [list(i) for i in data]
    return data

input = readInput()
print(f"input: {input}")

def returnRowAndCol(instruction,rows=127,cols=7):
    rlower, rupper = 0, rows
    clower, cupper = 0, cols
    for i in instruction:

        if i == "B":#UPPER
            rlower = math.ceil(statistics.mean([rupper, rlower]))
        elif i == "F":#LOWER
            # rlower = math.floor(rows / 2)
            rupper = math.floor(statistics.mean([rupper,rlower]))
        elif i == "L":#LOWER
            cupper = math.floor(statistics.mean([cupper,clower]))
        elif i == "R":#UPPER
            clower = math.ceil(statistics.mean([cupper, clower]))
    # print(instruction,(rlower*8)+clower)
    return((rlower*8)+clower)
#
#
# print(returnRowAndCol("FBFBBFFRLR"))
# a=("BBBFBFFLLL".replace("F","0"))
# a=(a.replace("B","1"))
# a=(a.replace("L","0"))
# a=(a.replace("R","1"))
# print(int(a,2))
# clower,cupper = 0,7
# # R means upper
# clower=math.ceil(statistics.mean([cupper,clower]))
# print(clower,cupper)
# #L means lower
# cupper = math.floor(statistics.mean([cupper,clower]))
# print(clower,cupper)
# #L means lower
# cupper = math.floor(statistics.mean([cupper,clower]))
# print(clower,cupper)
# # R means upper
# clower=math.ceil(statistics.mean([cupper,clower]))
# print(clower,cupper)

def getHighestID(input):
    highestID = 0
    for i in input:
        currentID = returnRowAndCol(i)
        if  currentID> highestID:
            print(i)
            highestID = returnRowAndCol(i)
    return highestID

# print(getHighestID(["BFFFBBFRRR","FFFBBBFRRR","BBFFBBFRLL"]))
# print(getHighestID(input))

def returnSortedIDs(input):
    IDs=[]
    for i in input:
        IDs.append(int(returnRowAndCol(i)))

    return sorted(IDs)


print(returnSortedIDs(input))

def getMySeat(list_of_sortedIDs):
    for i in list_of_sortedIDs:
        if i+1 not in list_of_sortedIDs:
            print(i+1)

getMySeat(returnSortedIDs(input))


