################ Day 12 Advent of Code 2020 ################
################         12/11/2020         ################
################                            ################



################ Methods ################

def Day12(filename):
    instructions = []
    shipfacing = 'E'
    position = [0,0] # east, north i.e. x,y
    with open(filename) as input:
        for line in input:
            instructions.append(line.strip('\n'))
    for instruction in instructions:
        direction = instruction[:1]
        distance = int(instruction[1:])
        #print(direction,distance)
        if direction == 'L' or direction == 'R':
            shipfacing = turn(position,shipfacing,direction,distance)
        elif direction in ['N','S','E','W','F']:
            position = move(position,shipfacing,direction,distance)
    print(position)
    return manhattandistance(position)
    
def move(position,shipfacing,direction,distance):
    if direction == 'N':
        position[1] += distance
    elif direction == 'S':
        position[1] -= distance
    elif direction == 'W':
        position[0] -= distance
    elif direction == 'E':
        position[0] += distance
    elif direction == 'F':
        position = move(position,shipfacing,shipfacing,distance)
    else:
        print('invalid move', position, shipfacing, direction, distance)
    return position

def turn(position,shipfacing,direction,degrees):
    compass = ['N','E','S','W']
    turn = 0
    currentindex = compass.index(shipfacing)
    if direction == 'R':
        turn = +1
    else:
        turn = -1
    turnamount = degrees/90 * turn
    newindex = currentindex + turnamount
    while newindex > 3:
        newindex -= 4
    while newindex < 0:
        newindex += 4
    return compass[int(newindex)]

def manhattandistance(position):
    x = (position[0])
    y = abs(position[1])
    return x+y

################ Testing ################

print('Test 1: ',Day12('input_test.txt'))
#print(move([0,0],'N','W',90))



################ Running ################
print('Actual 1: ',Day12('input.txt'))
# finish part 1 at 2304 beat by gumby
