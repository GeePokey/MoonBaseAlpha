import time
tstart = time.time()
def readInput():
    with open(r"C:\Users\Kody\GitExperiment\MoonBaseAlpha\AOC2020\D3_kinput.txt", "r",) as f:
    # with open(r"C:\Users\Kody\GitExperiment\MoonBaseAlpha\AOC2020\input.day3.txt", "r",) as f:
        data = f.read().split('\n')
    input = [list(i) for i in data]
    return input
# print(readInput())
# print(input)

# def splitToElements(toSplit):
#     f1,f2,f3 = toSplit.split(" ")
#     return f1,f2,f3

def oneloop(input,desiredslope):
    smackcounter = 0
    myloc = (0,0)

    width = len(input[0])
    while ifmoveLeft(input,myloc,desiredslope):#moveleft bool checking if you can go another layer down or if you are at the end condition
        # print(f"myloc start {myloc}")
        if locIsTree(input,myloc):

            smackcounter+=1
        addXOs(input, myloc, locIsTree(input, myloc))
        myloc = moveAtSlopeCoord(myloc,desiredslope,width)
        # print(f"myloc end {myloc}")
        # print(myloc,len(input[0]))
    # printBoard(input)
    # print(f"smcounter:{smackcounter}")
    return smackcounter
#myloc[0] is my x and [1] is my y
def ifmoveLeft(input,myloc,desiredslope):
    if myloc[1]+desiredslope[1] >= len(input):
        return False #if off bottom
    # elif len(input[0]) < myloc[0]: #if off right side
    #     return False
    # elif 0 > myloc[0]: #if off left side
    #     return False
    else:
        return True

def locIsTree(input,myloc):
    # print(input,myloc)
    try:
        if input[myloc[1]][myloc[0]] == "#":
            return True
        return False
    except IndexError:
        print(f"Index Error: {myloc}")
        raise

def addXOs(input,myloc,treeTrueOrSafeFalse):#prints on current location
    #myloc1 may be off by one slice is upto but not including i believe
    if treeTrueOrSafeFalse:
        input[myloc[1]][myloc[0]] = "X"
    else:
        input[myloc[1]][myloc[0]] = "O"

def moveAtSlopeCoord(myloc,desiredslope,width):
    #moveAtSlope gives (x,y) of next location
    return ((myloc[0]+desiredslope[0]) % width,myloc[1] + desiredslope[1])

def printBoard(input):
    for i in input:
        print("".join(i))


result = oneloop(readInput(),(1,1))*oneloop(readInput(),(3,1))*oneloop(readInput(),(5,1))*oneloop(readInput(),(7,1))*oneloop(readInput(),(1,2)) #should print out how many trees you encountered with the set slope
print(result)
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
def multslopes(listOfSlopes):
    total = 1
    input = readInput()
    for i in listOfSlopes:
        input = input[:]
        # print("i",i,"input",input)
        total *= oneloop(input,i)
    return total
print(multslopes(slopes))
line = '...#...#....#....##...###....#.', '#.#...#...#....#.........#..#..'
runtime = time.time() - tstart
print(f"Run time: {runtime:.5f}") #0.00600
# print(line[1][0])