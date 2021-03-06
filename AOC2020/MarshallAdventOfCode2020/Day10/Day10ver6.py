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
    validseqlist.append(adapters)
    validcount = 1
    #if isvalidseq(adapters) == True:
        # print(adapters,'is valid')
     #   validcount += 1
    #else: # break out if invalid
     #   return validcount
    for i in range(1,len(adapters)-1):
        if adapters[i+1]-adapters[i-1] <= 3:
            newseq = adapters[0:i]+adapters[i+1:]
            if newseq not in validseqlist:
                validcount += countvalidcombos(newseq)
    return validcount

def mymain2():
    
    #sortedadapters = sorted(adapters)
    #builtin = max(sortedadapters) + 3
    #sortedadapters.append(builtin)
    # print(sortedadapters)
    a = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 21, 22, 23, 24, 25, 28, 29, 30, 33, 34, 35, 38, 39, 40, 41, 42]
    b = [45, 48, 51, 52, 53, 54, 55, 58, 61, 62, 63, 64, 65, 68, 69, 70, 73, 74, 77, 80, 81, 82, 83, 84, 87, 90, 91, 92]
    c = [95, 96, 97, 98, 99, 102, 103, 104, 105, 108, 109, 110, 111, 112, 115, 116, 117, 118, 121, 122, 123, 126, 127, 128, 129, 130, 133, 134, 135, 136, 137, 140, 141, 144, 145, 146, 147, 148, 151]
    validseqlist = []
    acount = countvalidcombos(a)
    validseqlist = []
    bcount = countvalidcombos(b)
    validseqlist = []
    ccount = countvalidcombos(c)
    return acount * bcount * ccount

def mymain2test():
    
    #sortedadapters = sorted(adapters)
    #builtin = max(sortedadapters) + 3
    #sortedadapters.append(builtin)
    # print(sortedadapters)
    a = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11]

    b = [14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39]
    c = [42, 45, 46, 47, 48, 49, 52]
    validseqlist = []
    acount = countvalidcombos(a)
    validseqlist = []
    bcount = countvalidcombos(b)
    validseqlist = []
    ccount = countvalidcombos(c)
    return acount * bcount * ccount


################ Testing ################

adapters = Day10('input_test.txt')
#print('test1: ',mymain(adapters))
#print('test1pt2: ',mymain2(adapters))


adapters = Day10('input_test2.txt')
#print('test2: ',mymain(adapters))
print('test2pt2: ',mymain2test())


# print(isvalidseq([0,1,2,5,8]))
# print(isvalidseq([0,1,2,5,9]))



################ Running ################
adapters = Day10('input.txt')
#print('actual: ',mymain(adapters))
print('actualpt2v6: ',mymain2())

# finished pt1 at 21:25

# started pt2 ver1 running around 22:08
# finished ver1 running at


# started pt2 v2 at 22:17
# finished pt2 v2 at 


# started pt2 v3 at 22:28
# finished pt2 v3 at 

# started pt2 v4 at 22:44
# finished pt2 v4 at 
