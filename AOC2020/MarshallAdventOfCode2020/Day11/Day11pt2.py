################ Day 11 Advent of Code 2020 ################
################         12/10/2020         ################
################                            ################

# Notes:
# upper left is 0,0. x is left to right, y is up down
# seatmap[y][x] for position starting index 0.
# 




################ Methods ################

def Day11(inputfilename):
    seatmap = []
    occupied = 0
    with open(inputfilename) as input:
        for line in input:
            seatmap.append(line.strip('\n'))
    #count = occupiedcounter(seatmap)
    #print(count)
    #print(occupied(seatmap))
    changed = True
    while changed == True:
        seatmap, changed = seatmapupdate(seatmap)
        #for row in seatmap:
        #    print(row)
        #print('\n')
    #print(occupied(seatmap))
    #x, changed = seatmapupdate(seatmap)
    #newseatmap, changed = seatmapupdate(x)
    count = occupiedcounter(seatmap)

    #print(count)
    #print(seatmap)
    return count

def occupiedcounter(seatmap):
    count = 0
    for row in seatmap:
        count += row.count('#')
    return count

            
def seatmapupdate(seatmap):
    newseatmap = []
    changed = True
    for y in range(0,len(seatmap)):
        newseatmap.append('')
        for x in range(0,len(seatmap[0])):
            adjacent = countadjoccupied(seatmap,x,y)
            if seatmap[y][x] == '.':
                appendchar = '.'
            elif seatmap[y][x] == 'L' and adjacent == 0:
                appendchar = '#'
            elif seatmap[y][x] == '#' and adjacent >= 5:
                appendchar = 'L' 
            else:
                appendchar = seatmap[y][x]
            newseatmap[y] = newseatmap[y] + appendchar
    if newseatmap == seatmap:
        changed = False

    return newseatmap, changed


def countadjoccupied(seatmap,x,y):
    adjacentpositions = []
    count = 0
    width = len(seatmap[0])
    height = len(seatmap)
    # print(width,height)
    # left
    newx = x
    newy = y
    inrange = True
    while inrange == True:
        newx -= 1
        if newx < 0:
            inrange = False
        elif seatmap[newy][newx] == '#':
            count += 1
            #print('L')
            inrange = False
        elif seatmap[newy][newx] == 'L':
            inrange = False
    # right
    newx = x
    newy = y
    inrange = True
    while inrange == True:
        newx += 1
        if newx >= width:
            inrange = False
        elif seatmap[newy][newx] == '#':
            count += 1
            #print('R')

            inrange = False
        elif seatmap[newy][newx] == 'L':
            inrange = False
    # up
    newx = x
    newy = y
    inrange = True
    while inrange == True:
        newy -= 1
        if newy < 0:
            inrange = False
        elif seatmap[newy][newx] == '#':
            count += 1
            #print('U')

            inrange = False
        elif seatmap[newy][newx] == 'L':
            inrange = False
    # down
    newx = x
    newy = y
    inrange = True
    while inrange == True:
        newy += 1
        if newy >= height:
            inrange = False
        elif seatmap[newy][newx] == '#':
            count += 1
            #print('D')
            inrange = False
        elif seatmap[newy][newx] == 'L':
            inrange = False
    # diagonals
    # upleft
    
    inrange = True
    newx = x
    newy = y
    while inrange == True:
        newx -= 1
        newy -= 1
        if newx < 0 or newy < 0:
            inrange = False
        elif seatmap[newy][newx] == '#':
            count += 1
            #print('UL')
            inrange = False
        elif seatmap[newy][newx] == 'L':
            inrange = False

    # upright
    inrange = True
    newx = x
    newy = y
    while inrange == True:
        newx += 1
        newy -= 1
        if newx >= width  or newy < 0:
            inrange = False
        elif seatmap[newy][newx] == '#':
            count += 1
            #print('UR')
            inrange = False
        elif seatmap[newy][newx] == 'L':
            inrange = False
    # downleft
    inrange = True
    newx = x
    newy = y
    while inrange == True:
        newx -= 1
        newy += 1
        if newx < 0  or newy >= height:
            inrange = False
        elif seatmap[newy][newx] == '#':
            count += 1
            #print('DL')
            inrange = False
        elif seatmap[newy][newx] == 'L':
            inrange = False
    # downright
    inrange = True
    newx = x
    newy = y
    while inrange == True:
        newx += 1
        newy += 1
        if newx >= width  or newy >= height:
            inrange = False
        elif seatmap[newy][newx] == '#':
            count += 1
            #print('DR')
            inrange = False
        elif seatmap[newy][newx] == 'L':
            inrange = False

    return(count)

    
################ Testing ################
testmap = ['#.##.##.##',
'#######.##',
'#.#.#..#..',
'####.##.##',
'#.##.##.##',
'#.#####.##',
'..#.#.....',
'##########',
'#.######.#',
'#.#####.##']
#print(countadjoccupied(testmap,0,8))


    
print('test1: ',Day11('input_test.txt'))


################ Running ################
print('actual: ', Day11('input.txt'))
