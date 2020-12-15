################ Day 15 Advent of Code 2020 ################
################         12/14/2020         ################
################                            ################



################           Methods          ################
def Day15(startingnumbers = []):
    numbers = ['x'] + startingnumbers
    turncounter = len(startingnumbers)
    limit = 30000000 #2020 or 30000000
    lastcalledindex = {}
    for i in startingnumbers[:-1]:
        lastcalledindex[i] = numbers.index(i)
        
    while turncounter != limit:
        current = numbers[turncounter]
        if current not in lastcalledindex:
            numbers.append(0)
            lastcalledindex[current] = turncounter
            #print('not called before:',current)
        else:
            age = turncounter - lastcalledindex[current]
            lastcalledindex[current] = turncounter
            numbers.append(age)
        turncounter += 1
    print('Final number called:',numbers[-1])
    return numbers[-1]

                
################           Testing          ################
#print('Test 1v2:',Day15([0,3,6])) # 436 @ 2020 or 175594 @ 30000000

#print('Test 2v2:',Day15([1,3,2])) # 1 @ 2020 or 2578 @ 30000000
# v2 passed!





################           Running          ################

print('Actualv2: ',Day15([2,20,0,4,1,17]))
# Answer 758 correct at 2125 won
# part 2 answer 814 finished correct at 2149 won
