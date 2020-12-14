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
                #print(loc, value)
        #print(maskstrings)
        #print(instructions)
    # initialize the memory dict (not in dict = bitlength*'0')
    memory = {}
    bitlength = 36
    # for each mask and set of instructions
    for instrsetno in range(0,len(maskstrings)):
        mask = maskstrings[instrsetno]
        print(mask)
        print(len(mask))
        # for each instruction
        for i in instructions[instrsetno]:
            print(i)
            register = i[0]
            
            # convert int instr to binary 36 bit instruction string
            binaryinstr = bin(i[1])[2:]
            l = len(binaryinstr)
            currentinstr = '0' * (36-l) + binaryinstr
            print('instruction:',currentinstr)
            
        # parse the mask insto set of commands
        # apply mask to instruction

            for c in range(len(mask)):
                if mask[c] != 'X':
                    print(c)
                    print(mask[c],currentinstr[c])
                    currentinstr = currentinstr[:c] + mask[c] + currentinstr[c+1:]
            print('masked:     ',currentinstr)
        # apply masked instruction to register
        # if register already exists overwrite it.
            memory[register] = currentinstr
    # get sum of all registers
    runningsum = 0
    for register in memory.keys():
        runningsum += int(memory[register],2)

    
    return runningsum
    
################ Testing ################

print('Test 1 sum:',Day14('input_test.txt'))






################ Running ################
print('Actual sum: ',Day14('input.txt'))
# finished part1 at 22:45
