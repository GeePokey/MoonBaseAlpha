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
    count = occupiedcounter(seatmap)
    print(count)
    #print(occupied(seatmap))
    changed = True
    while changed == True:
        seatmap, changed = seatmapupdate(seatmap)
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
            if seatmap[y][x] == '.':
                appendchar = '.'
            elif seatmap[y][x] == 'L' and adjacent == 0:
                appendchar = '#'
            elif seatmap[y][x] == '#' and adjacent >= 4:
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

def countadjoccupied(seatmap,x,y):
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

    
################ Testing ################
print('test1: ',Day11('input_test.txt'))






################ Running ################
print('actual: ', Day11('input.txt'))
