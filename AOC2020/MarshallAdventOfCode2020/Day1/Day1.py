def Day1(filename):
    numberlist = []
    with open(filename) as input:
        for line in input:
            numberlist.append(int(line))
    for m in numberlist:
        for n in numberlist:
            if m + n == 2020:
                return m*n

print('Day 1 test:   ', Day1('input_test.txt'))
print('Day 1 actual: ', Day1('input.txt'))

### Part 2:

def Day1p2(filename):
    numberlist = []
    with open(filename) as input:
        for line in input:
            numberlist.append(int(line))
    for m in numberlist:
        for n in numberlist:
            for k in numberlist:
                if m + n + k == 2020:
                    return m*n*k

print('Day 1pt2 test:   ', Day1p2('input_test.txt'))
print('Day 1pt2 actual: ', Day1p2('input.txt'))
