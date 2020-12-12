### Day 4 Advent of Code 2020
### to change between part 1 and part 2 see 6th line of isvalid()


def passportfilereader(filename):
    with open(filename) as input:
        passportindex = 0
        passports = [{}]
        for line in input:
            if line == '\n':
                passportindex += 1
                passports.append({})
                # print('next', passportindex)
            else:
                pairs = line.split(' ')
                # print(pairs)
                for pair in pairs:
                    attr, value = pair.split(':')
                    if value.endswith('\n'):
                        value = value.strip('\n')
                    passports[passportindex][attr] = value
    return passports

# print(passportfilereader('input_test.txt'))

    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID)

def isvalid(passport):
    attributes = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] # ,'cid']
    valid = True
    for attr in attributes:
        if attr not in passport:
            valid = False
        # Following elif adds part 2 to the checker; remove for part 1
        elif checkfield(attr,passport[attr]) == False:
            valid = False
    return valid

def checkfield(field,value):
    isvalid = False
    if field == 'byr':
        if value.isdigit() == True:
            if (1920 <= int(value) <= 2002):
                isvalid = True
    elif field == 'iyr':
        if value.isdigit() == True:
            if (2010 <= int(value) <= 2020):
                isvalid = True
    elif field == 'eyr':
        if value.isdigit() == True:
            if (2020 <= int(value) <= 2030):
                isvalid = True
    elif field == 'hgt':
        # (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        if value.endswith('cm') == True:
            if (150 <= int(value.strip('cm')) <= 193):
                isvalid = True
        elif value.endswith('in') == True:
            if (59 <= int(value.strip('in')) <= 76):
                isvalid = True
        else:
            isvalid = False
        
    elif field == 'hcl':
        allowedvalues = '0123456789abcdef'
        if (len(value) == 7) and (value[0] == '#'):
            isvalid = True
            for i in range(1,7):
                if not value[i] in allowedvalues:
                    isvalid = False
                    
    elif field == 'ecl':
        allowedvalues = ['amb','blu','brn','gry','grn','hzl','oth']
        if value in allowedvalues:
            isvalid = True
    elif field == 'pid':
        if value.isdigit() == True and len(value) == 9:
            isvalid = True
    elif field == 'cid':
        isvalid = True
    else: # field is not a valid name of attribute
        isvalid = False
    return isvalid


def checkallpassports(passports):
    validcount = 0
    for passport in passports:
        if isvalid(passport) == True:
            validcount += 1
            # print('valid')
        # else:
            # print('invalid')
    return validcount


########## Running Stuff ##########
passports = passportfilereader('input_test2.txt')
print('valid test: ', checkallpassports(passports))

passports = passportfilereader('input.txt')
print('valid actual: ', checkallpassports(passports))






########## Tests for checkfield ##########
# print(checkfield('byr','2002')) # Failed fixed
# print(checkfield('byr','2003')) # Failed fixed
# print(checkfield('byr','202'))

# print(checkfield('hgt','60in'))
# print(checkfield('hgt','190cm'))
# print(checkfield('hgt','190in')) #Pass
# print(checkfield('hgt','190'))

# print(checkfield('hcl','#123abc'))
# print(checkfield('hcl','#123abz')) # Pass
# print(checkfield('hcl','123abc'))

# print(checkfield('ecl','brn'))
# print(checkfield('ecl','wat'))

# print(checkfield('pid','000000001')) # Failed
# print(checkfield('pid','0123456789'))
