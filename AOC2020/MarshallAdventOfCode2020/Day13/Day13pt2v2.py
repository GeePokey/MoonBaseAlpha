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

    currentmaxmultiplier = int(100000000000000/maxID)
    currenttime = currentmaxmultiplier * maxID - busIDs[maxID]
    print((currenttime+busIDs[maxID])%maxID)
    finished = False
    millioncounter = 1000000000
    while finished == False:
        #contflag = False

        finished = True
        if currenttime >= millioncounter:
            print('currenttime: ',currenttime)
            millioncounter += 1000000000
        for ID in busIDs:
            #if contflag == True:
            #    print('shouldnt be here')
                
            if (currenttime+busIDs[ID])%ID != 0:
                currentmaxmultiplier += 1
                currenttime += maxID
                finished = False
                #print('continue')
                #contflag = True
                break
            #if contflag == True:
            #    contflag = False
            #    continue
            #print('match')
            
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

#print('Test 1:',Day13('input_test.txt'))






################ Running ################
print('Actual pt2: ',Day13('input.txt'))
#finished 2120

#  LocalWords:  currentmaxmultiplier
