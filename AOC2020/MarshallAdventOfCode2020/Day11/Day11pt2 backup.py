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
        for row in seatmap:
            print(row)
        print('\n')
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
            # newseatmap[y] = newseatmap[y] + seatmap[y][x]
            adjacent = countadjoccupied(seatmap,x,y)
            #oldadjacent = oldcountadjoccupied(seatmap,x,y)
            if seatmap[y][x] == '.':
                appendchar = '.'
            elif seatmap[y][x] == 'L' and adjacent == 0:
                appendchar = '#'
            elif seatmap[y][x] == '#' and adjacent >= 5:
                appendchar = 'L' 
            else:
                appendchar = seatmap[y][x]
            newseatmap[y] = newseatmap[y] + appendchar
    #print(countadjoccupied(seatmap,9,9))
    if newseatmap == seatmap:
        changed = False

    return newseatmap, changed
            

    # return seatmap,changed # changed is False
    # if no update was necessary. i.e. finished

def oldcountadjoccupied(seatmap,x,y): #deprecated
    adjacentpositions = []
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i >= 0 and j >= 0 and i < len(seatmap[0]) and j < len(seatmap):
                adjacentpositions.append([i,j])
    adjacentpositions.remove([x,y])
    # print(adjacentpositions)
    count = 0
    for pair in adjacentpositions:
        if seatmap[pair[1]][pair[0]] == '#':
            count += 1
    return(count)


def countadjoccupied(seatmap,x,y):
    adjacentpositions = []
    count = 0
    width = len(seatmap[0])
    height = len(seatmap)
    # left
    if '#' in seatmap[y][:x]:
        count += 1
    # right
    if '#' in seatmap[y][x+1:]:
        count += 1
    # up
    upcount = 0
    for row in seatmap[:y]:
        if row[x] == '#':
            upcount = 1
    count += upcount
    # down
    downcount = 0
    for row in seatmap[y+1:]:
        if row[x] == '#':
            downcount = 1
    count += downcount
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
            inrange = False
    # downright
    inrange = True
    newx = x
    newy = y
    while inrange == True:
        newx -= 1
        newy += 1
        if newx >= width  or newy >= height:
            inrange = False
        elif seatmap[newy][newx] == '#':
            count += 1
            inrange = False
    
    # for i in range(x-1,x+2):
    #     for j in range(y-1,y+2):
    #         if i >= 0 and j >= 0 and i < len(seatmap[0]) and j < len(seatmap):
    #             adjacentpositions.append([i,j])
    # adjacentpositions.remove([x,y])
    # print(adjacentpositions)
    # for pair in adjacentpositions:
    #     if seatmap[pair[1]][pair[0]] == '#':
    #         count += 1
    return(count)

    
################ Testing ################
print('test1: ',Day11('input_test.txt'))






################ Running ################
#print('actual: ', Day11('input.txt'))
