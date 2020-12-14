################ Day 13 Advent of Code 2020 ################
################         12/12/2020         ################
################                            ################



################ Methods ################
def Day13(filename):
    with open(filename) as input:
        linecounter = 0
        for line in input:
            if linecounter == 0:
                departtime = int(line.strip('\n'))
            if linecounter == 1:
                busstring = line.strip('\n')
            linecounter += 1
        busstringsplit = busstring.split(',')
        busIDs = {} # {ID:offset}
        IDcounter = 0
        for i in busstringsplit:
            if not i == 'x':
                busIDs[int(i)] = IDcounter
            IDcounter += 1
        maxID = max(busIDs.keys())

    currentmaxmultiplier = 1
    currenttime = currentmaxmultiplier * maxID - busIDs[maxID]
    print(currenttime)
    finished = False
    while finished == False:
        finished = True
        for ID in busIDs:
            if (currenttime+busIDs[ID])%ID != 0:
                currentmaxmultiplier += 1
                currenttime = currentmaxmultiplier * maxID - busIDs[maxID]
                finished = False
                continue
    return(currenttime)


        
    print(busIDs)
    print(maxID)
        
    #currenttime = departtime - 1
#    departed = False
#    while not departed:
#        currenttime += 1
#        for t in busIDs:
#            if currenttime%t == 0:
#                soonestbusID = t
#                departed = True
#    waittime = currenttime - departtime
#    print(currenttime)
#    print(soonestbusID)
#    return waittime * soonestbusID
        
                
    
################ Testing ################

print('Test 1:',Day13('input_test.txt'))






################ Running ################
print('Actual 1: ',Day13('input.txt'))
#finished 2120

#  LocalWords:  currentmaxmultiplier
