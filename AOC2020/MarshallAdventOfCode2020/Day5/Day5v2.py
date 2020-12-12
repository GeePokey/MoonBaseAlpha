### Day 5 Advent of Code 2020
###
### v2 is just for screwing around


################ Methods ################

def Day5(filename):
    passdict = {}
    with open(filename) as input:
        for line in input:
            passdict[line.strip('\n')] = {}
    for passport in passdict:
        row, column = getrowcolumn(passport)
        passdict[passport]['row'] = row
        passdict[passport]['column'] = column
        passdict[passport]['ID'] = row * 8 + column
    return(passdict)

def getrowcolumn(passport):
    # Version 2 converts to binary and uses builtin binary to int
    row = ''
    column = ''
    replacements = {'F':'0','B':'1','L':'0','R':'1'}
    
    for i in passport:
        if i == 'F' or i == 'B':
            row += replacements[i]
        elif i == 'L' or i == 'R':
            column += replacements[i]
            
    return int(row,2),int(column,2)


def gethighest(passdict):
    highestID = 0
    for passport in passdict:
        ID = passdict[passport]['ID']
        if ID > highestID:
            highestID = ID
    return highestID

def findmyseat(passdict):
    IDlist = []
    emptyseats = []
    for passport in passdict:
        IDlist.append(passdict[passport]['ID'])
    minimum = min(IDlist)
    maximum = max(IDlist)
    for IDno in range(minimum,maximum):
        if IDno not in IDlist:
            emptyseats.append(IDno)
    return emptyseats
        
################ Testing ################

print('TEST Highest ID in list: ',gethighest(Day5('input_test.txt')))

################ Running ################

print('Highest ID in list: ',gethighest(Day5('input.txt')))
print('Empty Seats: ',findmyseat(Day5('input.txt')))

# Finished 12/11/2020 at 16:32
