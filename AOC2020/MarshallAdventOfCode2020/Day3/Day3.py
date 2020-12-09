# Day 3 Advent of Code 2020:


def map(x, y):
### returns istree = True or False, finished = T or F
### based on map coords
### given where x and y start counting from 0,0
### in the upper left corner.
### not map [[],[],[]] first index will be y and second
### will be x
    map = []
    with open('input.txt') as input:
        for line in input:
            map.append(line)
    if y >= len(map):
        return False, True
    # print(map[0])
    width = len(map[0])-1
    if x >= width:
        # print(x, width,x%width)
        x = x % width
    # print(map[y][x])
    if map[y][x] == '#':
        return True, False
    elif map[y][x] == '.':
        return False, False
    else:
        print('error in map program')
        return



def ski(slopex,slopey):
    treecount = 0
    x = 0
    y = 0
    finished = False
    while not finished:
        
        istree, finished = map(x,y)
        if istree:
            treecount += 1
        # print(x,y,istree)
        x += slopex
        y += slopey
        
    return treecount
        
### running:
#Tests:
print(map(0,2),'nottree should be False, False')
print(map(2,0), 'is tree should be True, False')
print(map(0,11), 'finish should be False, True')

print('tree count: ', ski(3,1))

# part 2:
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

def part2():
    treecounts = []
    for [x,y] in slopes:
        treecounts.append(ski(x,y))
    result = 1
    for i in treecounts:
        result = result * i
    return result

print('part 2: ', part2())
