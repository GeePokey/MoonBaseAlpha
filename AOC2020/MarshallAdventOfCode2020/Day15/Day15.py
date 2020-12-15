################ Day 15 Advent of Code 2020 ################
################         12/14/2020         ################
################                            ################



################           Methods          ################
def Day15(startingnumbers = []):
    numbers = ['x'] + startingnumbers
    turncounter = len(startingnumbers)
    limit = 30000000 #2020
    
    while turncounter != limit:
        current = numbers[turncounter]
        if current not in numbers[:turncounter]:
            numbers.append(0)
        else:
            lastcalledlist = [index for index,val in enumerate(numbers[:turncounter]) if val == current]
            age = turncounter - lastcalledlist[-1]
            numbers.append(age)
        turncounter += 1
        #print(numbers[-1])
    #print(numbers)
    return numbers[-1]
            



                
################           Testing          ################
#print('Test 1:',Day15([0,3,6]))

#print('Test 2:',Day15([1,3,2]))






################           Running          ################

print('Actual : ',Day15([2,20,0,4,1,17]))
# Answer 758 correct at 2125 beat Gumby!
