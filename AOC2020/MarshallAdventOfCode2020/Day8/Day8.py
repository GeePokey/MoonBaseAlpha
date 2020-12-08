# [1:{'op':nop,'arg':+0,'called':0},2:{'op':acc,'arg':+1,'called':0},...]
#instr 1 is called first and called is set to 1
#if called was not already zero then program is ended before instr 1 is completed
#and value of accumulator is returned.

def parseline(line):
    op = line.split(' ')[0]
    arg = int(line.split(' ')[1])
    called = 0
    return {'op':op,'arg':arg,'called':0}

# test:
# print(parseline('nop -4'))

def parsefile():
    instructionset = {}
    instructionno = 1
    with open('./input.txt') as input:
        for line in input:
            instructionset[instructionno] = parseline(line)
            instructionno += 1
        instructionset[instructionno] = {'op':'nop','arg':0,'called':'final'}
    return instructionset

# test:
# print(parsefile())

def machine(instructionset):
    accumulator = 0
    currentinstructionno = 1
    counter = 1
    running = True
    
    while running == True:
        currentinstruction = instructionset[currentinstructionno]
        if currentinstruction['called'] == 'final':
            return accumulator, True
        if not currentinstruction['called'] == 0:
            #print(currentinstruction)
            isvalid = currentinstruction['called'] == 'final'
            return accumulator, isvalid #,instructionset
        else: # current instruction has not been called
            currentinstruction['called'] = counter
            counter += 1

            if currentinstruction['op'] == 'nop': # do nothing, next instr
                currentinstructionno += 1

            elif currentinstruction['op'] == 'acc': # add to accumulator, next instr
                accumulator += currentinstruction['arg']
                currentinstructionno += 1

            elif currentinstruction['op'] == 'jmp': # do nothing, jump forward or back
                currentinstructionno += currentinstruction['arg']
            # print(currentinstruction)
                        

def clearset(instructionset):
    for i in instructionset:
        if not instructionset[i]['called'] == 'final':
            instructionset[i]['called'] = 0
    return instructionset
            
def checker(instructionset):
    for instructionno in instructionset:
        # print(instructionno,instructionset[instructionno])
        backupop = instructionset[instructionno]['op'] # default for backupop

        if instructionset[instructionno]['op'] == 'nop' and not instructionset[instructionno]['arg'] == 0 and instructionset[instructionno]['arg'] in instructionset:
            instructionset[instructionno]['op'] = 'jmp'
            
        elif instructionset[instructionno]['op'] == 'jmp':
            instructionset[instructionno]['op'] = 'nop'
            
        instructionset = clearset(instructionset) # reset called's to 0
        accumulator, isvalid = machine(instructionset)
        # print(instructionno,instructionset[instructionno])
        
        if isvalid == True:
            print('changed:',instructionno,instructionset[instructionno])
            return accumulator, isvalid
        # if it didn't make it valid, set it back:
        instructionset[instructionno]['op'] = backupop

    print('did not find valid code')
    # print(instructionset)

instructionset = parsefile()

print('accumulator:',checker(instructionset))
