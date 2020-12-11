### Day 10 Advent of Code 2020
###
###


################ Methods ################
validseqlist = []


def Day10(filename):
    adapters = [0]
    with open(filename) as input:
        for line in input:
            adapters.append(int(line.strip('\n')))
    #print(adapters)
    return adapters

def mymain(adapters):
    onecount = 0
    threecount = 0
    sortedadapters = sorted(adapters)
    #print(sortedadapters)
    builtin = max(sortedadapters) + 3
    sortedadapters.append(builtin)
    for i in range(0,len(sortedadapters)-1):
        difference = sortedadapters[i+1] - sortedadapters[i]
        if difference == 1:
            #print('one')
            onecount += 1
        elif difference == 3:
            #print('three')
            threecount += 1
        else:
            print('invalid adapter: ',difference)
        #print(sortedadapters[i+1], sortedadapters[i])
        #print('one:',onecount,' three: ',threecount)
    return onecount * threecount

def isvalidseq(adapterlist):
    isvalid = True
    for i in range(0,len(adapterlist)-1):
        difference = adapterlist[i+1] - adapterlist[i]
        # print(adapterlist[i+1],adapterlist[i],difference)
        if difference > 3 or difference < 0:
            isvalid = False
        # dont add else True b/c one failure fails all
    if isvalid == True:
        if adapterlist in validseqlist:
            isvalid = False
        else:
            validseqlist.append(adapterlist)
    return isvalid

def countvalidcombos(adapters):
    
    validcount = 0
    if isvalidseq(adapters) == True:
        # print(adapters,'is valid')
        validcount += 1
    else: # break out if invalid
        return validcount
    for i in range(1,len(adapters)-1):
        if adapters[i+1]-[i-1] <= 3:
            newseq = adapters[0:i]+adapters[i+1:]
            # print(newseq)
            if newseq not in validseqlist:
                validcount += countvalidcombos(newseq)
    return validcount

def mymain2(adapters):
    
    sortedadapters = sorted(adapters)
    builtin = max(sortedadapters) + 3
    sortedadapters.append(builtin)
    # print(sortedadapters)
    validseqlist = []
    return countvalidcombos(sortedadapters)

################ Testing ################

adapters = Day10('input_test.txt')
print('test1: ',mymain(adapters))
#print('test1pt2: ',mymain2(adapters))


adapters = Day10('input_test2.txt')
print('test2: ',mymain(adapters))
#print('test2pt2: ',mymain2(adapters))


# print(isvalidseq([0,1,2,5,8]))
# print(isvalidseq([0,1,2,5,9]))



################ Running ################
adapters = Day10('input.txt')
print('actual: ',mymain(adapters))
print('actualpt2: ',mymain2(adapters))

# finished pt1 at 21:25
# started pt2 ver1 running around 22:08
# finished ver1 running at

# started pt2 v2 at 22:17
# finished pt2 v2 at 
