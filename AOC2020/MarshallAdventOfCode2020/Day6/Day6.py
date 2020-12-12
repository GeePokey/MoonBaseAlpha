### Day 6 Advent of Code 2020
###         12/11/2020
###


################ Methods ################
def Day6(filename):
    groups = ['']
    counter = 0
    with open(filename) as input:
        for line in input:
            strippedline = line.strip('\n')
            if strippedline == '':
                counter += 1
                groups.append('')
            else:
                for c in strippedline:
                    if c not in groups[counter]:
                        groups[counter] += c
    return groups

def Day6pt2(filename):
    loners = ['']
    groups = ['']
    groupcount = [0]
    counter = 0
    first = True
    with open(filename) as input:
        for line in input:
            strippedline = line.strip('\n')
            if strippedline == '':
                counter += 1
                groups.append('')
                groupcount.append(0)
                first = True
            else:
                groupcount[counter] += 1
                for c in strippedline:
                    groups[counter] += c

    # leave only answers that all members in group said yes to:
    for i in range(0,len(groups)):
        answers = groups[i]
        numberingroup = groupcount[i]
        #print(answers,numberingroup)
        for c in answers:
            if answers.count(c) < numberingroup:
                answers = answers.replace(c,'')
        groups[i] = answers
    
    return groups # contains duplicates


def part1count(groups):
    count = 0
    for group in groups:
        count += len(group)
    return count

def part2count(groups):
    count = 0
    for group in groups:
        count += len(set(group))
    return count

################ Testing ################
#print(Day6('input_test.txt'))
#print('Part 1 Test: ',part1count(Day6('input_test.txt')))
#print(Day6pt2('input_test.txt'))
print('Part 2 Test: ',part2count(Day6pt2('input_test.txt')))

################ Running ################

print('Part 1 Actual: ',part1count(Day6('input.txt')))
# Finished part 1! 16:59 12/11/2020

print('Part 2 Actual: ',part2count(Day6pt2('input.txt')))
# Finished part 2! 17:35 12/11/2020
