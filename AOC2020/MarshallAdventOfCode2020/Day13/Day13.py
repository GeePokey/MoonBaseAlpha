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
        busIDs = []
        for i in busstringsplit:
            if not i == 'x':
                busIDs.append(int(i))

    currenttime = departtime - 1
    departed = False
    while not departed:
        currenttime += 1
        for t in busIDs:
            if currenttime%t == 0:
                soonestbusID = t
                departed = True
    waittime = currenttime - departtime
    print(currenttime)
    print(soonestbusID)
    return waittime * soonestbusID
        
                
    
################ Testing ################

print('Test 1:',Day13('input_test.txt'))






################ Running ################
print('Actual 1: ',Day13('input.txt'))
#finished 2120
