################ Day 14 Advent of Code 2020 ################
################         12/13/2020         ################
################                            ################



################ Methods ################
def Day14(filename):
    with open(filename) as input:
        instructions = []
        linecounter = -1
        maskstrings = []
        for line in input:
            if line[0:4] == 'mask':
                maskstring = line.strip('\n').split(' ')[-1]
                maskstrings.append(maskstring)
                instructions.append([])
                linecounter += 1
            elif line == '':
                continue
            else:
                line1 = line.strip('\n')
                loc = int(line1.split('[')[1].split(']')[0])
                value = int(line1.split(' ')[-1])
                instructions[linecounter].append((loc,value))

    # initialize the memory dict (not in dict = bitlength*'0')
    memory = {}
    bitlength = 36
    # for each mask and set of instructions:
    for instrsetno in range(0,len(maskstrings)):
        mask = maskstrings[instrsetno]

        # for each instruction:
        for i in instructions[instrsetno]:
            register = i[0]
            instruction = i[1]
            
            # convert int instr to binary 36 bit instruction string:
            binaryinstr = bin(i[0])[2:]
            l = len(binaryinstr)
            currentbinloc = '0' * (36-l) + binaryinstr

            # update the dictionary with the instructions expanded for the floating digits:
            memory.update(expandinstruction(currentbinloc,instruction,mask))

    return sum(memory.values())#runningsum


def expandinstruction(binarylocation,currentinstr,mask): # instruction is decimal
    # binary location is binary memory register number
    maskedinstructions = {}

    # Apply the mask to the memory address:
    for c in range(len(mask)):
        if mask[c] == '1':
                    #print(c)
                    #rint(mask[c],currentinstr[c])
            binarylocation = binarylocation[:c] + mask[c] + binarylocation[c+1:]
        elif mask[c] == '0':
            pass
        elif mask[c] == 'X':
            binarylocation = binarylocation[:c] + 'X' + binarylocation[c+1:]

    # expand the list of memory locations with the floating 'X's equaling 1 or 0:
    xcount = binarylocation.count('X')
    newregisters = ['']
    for i in range(len(binarylocation)):
        if binarylocation[i] != 'X':
            for r in range(len(newregisters)):
                newregisters[r] = newregisters[r] + binarylocation[i]
        else:
            newxregisters = []
            for r in newregisters:
                newxregisters.append(r+'1')
                newxregisters.append(r+'0')
            newregisters = newxregisters
            
    # Add the expanded list of memory locations to a dictionary
    # with all locations returning the instruction value
    for newloc in newregisters:
        maskedinstructions[newloc] = currentinstr
    return maskedinstructions



    
################ Testing ################

#print('Test1 expand:',expandinstruction('000000000000000000000000000000000011',11,'00000000000000000000000000000000000X'))

#print('Test2 expand:',expandinstruction('000000000000000000000000000000011010',1,'00000000000000000000000000000000X0XX'))

print('Test 2  pt 2:',Day14('input_test2.txt'))
#print('Test 2 sum pt 2:',Day14('input_test2.txt'))





################ Running ################
#print('Actual sum: ',Day14('input.txt'))
# finished part1 at 22:45
print('Actual pt2 sum: ',Day14('input.txt'))
# finished pt2 at 2355! whoo! Answer: 2667858637669
