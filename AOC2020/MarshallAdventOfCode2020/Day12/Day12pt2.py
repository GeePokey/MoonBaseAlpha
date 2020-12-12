################ Day 12 Advent of Code 2020 ################
################         12/11/2020         ################
################                            ################



################ Methods ################

def Day12(filename):
    instructions = []
    shipfacing = 'E'
    position = [0,0] # east, north i.e. x,y
    waypoint = [10,1]
    with open(filename) as input:
        for line in input:
            instructions.append(line.strip('\n'))
    for instruction in instructions:
        direction = instruction[:1]
        distance = int(instruction[1:])
        #print(direction,distance)
        if direction == 'L' or direction == 'R':
            waypoint = turn(waypoint,direction,distance)
        elif direction in ['N','S','E','W']:
            waypoint = movewaypoint(waypoint,direction,distance)
        elif direction == 'F':
            position = moveship(position,waypoint[:],distance)
        #print('instr finished,position:',position,'waypoint:',waypoint)
    #print(position)
    return manhattandistance(position)

def moveship(position,waypoint,distance):
    #print('moveship',waypoint)
    intwaypoint = [0,0] # what the hell. why did i have to add this?!
    for i in range(len(waypoint)):
        intwaypoint[i] = waypoint[i] * distance
    newposition = [position[0]+intwaypoint[0],position[1]+intwaypoint[1]]
    #print('move ship:',position,intwaypoint,distance,newposition)
    #print(waypoint)

    if newposition[0] - position[0] != distance * waypoint[0]:
        print('move error in move ship: ')
        
    return newposition

def movewaypoint(position,direction,distance):
    #print('move way point:',position,direction,distance)
    if direction == 'N':
        position[1] += distance
    elif direction == 'S':
        #print('help')
        position[1] -= distance
    elif direction == 'W':
        position[0] -= distance
    elif direction == 'E':
        position[0] += distance
    elif direction == 'F': # deprecated
        position = move(position,shipfacing,distance)
        print('I should not be here F in movewaypoint')
    else:
        print('invalid move', position, direction, distance)
    #print('new way point:',position)
    
    
    return position

def turn(waypoint,direction,degrees):
    #print('turning:', waypoint,direction,degrees)
    compass = ['N','E','S','W']
    compass = [waypoint[1],waypoint[0],0,0]
    turn = 0
    currentindex = 0
    turnamount = int(degrees/90)
    if direction == 'R':
        for i in range(turnamount):
            compass.insert(0,0)
            last = compass.pop()
            if last != 0:
                compass[0] = last
    else:
        for i in range(turnamount):
            #compass.insert(-1,0)
            compass.append(0)

            last = compass.pop(0)
            if last != 0:
                compass[-1] = last
    if compass[2] != 0:
        compass[0] -= compass[2]
    if compass[3] != 0:
        compass[1] -= compass[3]
    #print('new waypoint:',[compass[1],compass[0]])
    return [compass[1],compass[0]]

def manhattandistance(position):
    x = abs(position[0])
    y = abs(position[1])
    return x+y

################ Testing ################

print('Test 1 pt2: ',Day12('input_test.txt'))
#print(move([0,0],'N','W',90))


################ Running ################
print('Actual 1 pt 2: ',Day12('input.txt'))
# finish part 1 at 2304 beat by gumby
# pt 2 18546 wrong answer;too low
# found error finished part 2 at 00:21 Gumby won by 1 minute!
