preamblelength = 5

def parsefile(filename):
    instructionset = {}
    instructionno = 1
    with open(filename) as input:
        for line in input:
            instructionset[instructionno] = int(line[:-1]) # gets rid of newline
            instructionno += 1
    # print(instructionset)
    return instructionset

# print(parsefile())

def checker(instructionset, preamblelength):
    # return first number that is not valid
    currentlineno = 1
    currentlineno += preamblelength
    for i in range(preamblelength+1,len(instructionset)+1): # gives index of instructions excluding preamble
        # print(i)
        
        preamble = []
        preamblerange = range(i-preamblelength,i)
        for p in preamblerange:
            #print(i)
            preamble.append(instructionset[p])
        # print(preamble)

        possiblesums = []
        for m in preamble:
            for n in preamble:
                if m != n:
                    possiblesums.append(m+n)
        
        if instructionset[i] not in possiblesums:
            return instructionset[i]


testinstructionset = parsefile('./input_test.txt')
instructionset = parsefile('./input.txt')

testnumber = checker(testinstructionset, 5)
actualnumber = checker(instructionset, 25)

print('first invalid number test: ', testnumber)

print('first invalid number actual: ', actualnumber)


### Part 2:

def weaknessfinder(invalidnumber, instructions):
    # for each starting point start accumulating lists;
    # check if sum of list is = to invalidnumber;
    # if it was = , then return sum of list min and max.
    indexcounter = 1
    startingcounter = 1
    currentlist = []
    while True:
        if indexcounter in instructions:
            currentlist.append(instructions[indexcounter])
        else:
        # reached end of the list, clear and start over with higher starting
            currentlist = []
            startingcounter += 1
            indexcounter = startingcounter - 1
            
        if len(currentlist) >= 2:
            thesum = sum(currentlist)
            if thesum == invalidnumber:
                # end condition
                return min(currentlist) + max(currentlist)
            elif thesum > invalidnumber:
                currentlist = []
                startingcounter += 1
                indexcounter = startingcounter - 1
            
        indexcounter += 1


### run stuff for part 2
print('weakness number sum test: ', weaknessfinder(testnumber, testinstructionset))

print('weakness number sum actual: ', weaknessfinder(actualnumber, instructionset))
