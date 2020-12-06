import itertools
import re


def readInput():
    with open(r"C:\Users\Kody\GitExperiment\MoonBaseAlpha\AOC2020\D4_kinput.txt", "r",) as f:
    # with open(r"C:\Users\Kody\GitExperiment\MoonBaseAlpha\AOC2020\good.txt", "r",) as f:
        data = f.read().split('\n\n')
    # input = [list(i) for i in data]
    return data

input = readInput()
# print(input)
def flatten(list_of_lists):
    "Flatten one level of nesting"
    return itertools.chain.from_iterable(list_of_lists)

def printPassports(input):
    for i in input:
        print(i,"\n")


def hasRequiredFields(passport,reqFields):
    for i in reqFields:
        if i in passport:
            continue
        else:
            return False
    return True
reqFields = ["byr","iyr","eyr", "hgt", "hcl","ecl","pid"]
pass1 = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm """
pass2 = """iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929"""
pass3 = """hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm"""
pass4 = """hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
# printPassports(input)
assert (hasRequiredFields(pass1,reqFields)) == True
assert (hasRequiredFields(pass2,reqFields)) == False
assert (hasRequiredFields(pass3,reqFields)) == True
assert (hasRequiredFields(pass4,reqFields)) == False

def checkAllPassports(listOfPassports):
    totalValid = 0
    totalInvalid = 0
    for i in listOfPassports:
        if hasRequiredFields(i,reqFields):
            totalValid += 1
        else:
            totalInvalid += 1
    return totalValid,totalInvalid

# print(checkAllPassports(input))

def splitPassportToFields(passport):
    # print("thefuckingpassport:",passport)
    returnlist = passport.split(" ")
    # print("rlist:",returnlist)
    b = []
    for i in returnlist:
        # print(i)
        if "\n" in i:
            b.append(i.split("\n"))
        elif i == "":
            continue
        else:
            b.append(i)
    # print("b:",b)
    breturn = []
    for i in b:
        if type(i) == type([]):
            breturn += i
        elif i == "":
            continue
        else:
            breturn.append(i)
    # print(f"returnlist2 {breturn}")
    # print("breturn:",breturn)
    return breturn

thelist = ['iyr:2020', 'byr:1968\necl:gry\neyr:2030', 'hcl:#1976b0\ncid:127', 'pid:701862616\nhgt:161cm\n']
# print(splitPassportToFields(thelist))
splitPassportToFields(pass1)
# print(splitPassportToFields(pass2))
# print(splitPassportToFields(pass3))
# print(splitPassportToFields(pass4))

def checkFieldsValid(passport):
    approvedEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    # print(f"PASSPORT: {passport}")
    for i in passport:
        if i == "":
            continue

        key,value = i.split(":")
        assert len(key)==3
        # print(f"key: {key} value: {value} field: {i}")
        if "byr" in key:
            value = int(value)
            if value >= 1920 and value <= 2002:
                continue
            # print("byr didnt pass")
            return False
        if "iyr" in key:
            value = int(value)
            if value >= 2010 and value <= 2020:
                continue
            # print("iyr didnt pass")
            return False
        if "eyr" in key:
            value = int(value)
            if value >= 2020 and value <= 2030:
                continue
            # print("eyr didnt pass")
            return False
        if "hgt" in key:
            if "cm" in value:
                value,mtype = value.split("cm")
                value = int(value)
                if value >= 150 and value <= 193:
                    continue
                # print("hgt didnt pass")
                return False
            elif "in" in value:
                value,mtype = value.split("in")
                value = int(value)
                if value >= 59 and value <= 76:
                    continue
                # print("hgt didnt pass")
                return False
            else:
                # print("Given Invalid hgt measurement")
                return False
        if "hcl" in key:
            match = re.match(r"#[0-9a-f]{6}$",value)
            if match:
                continue
            # print("hcl didnt pass")
            return False
        if "ecl" in key:
            if value in approvedEyeColors:
                continue
            # print("ecl didnt pass")
            return False
        if "pid" in key:
            match = re.match(r"[0-9]{9}$",value)
            # print(match)
            if match:
                continue
            # print("pid didnt pass")
            return False
    return True


def countFullyValidPassports(listOfPassports):
    totalValid = 0
    totalInvalid = 0
    for passport in listOfPassports:
        if hasRequiredFields(passport, reqFields):
            if checkFieldsValid(splitPassportToFields(passport)):
                totalValid += 1
            else:
                totalInvalid+=1
        else:
            totalInvalid += 1
    return totalValid, totalInvalid


#
# assert (checkFieldsValid(splitPassportToFields(validpassport1))) == True
# assert (checkFieldsValid(splitPassportToFields(validpassport2))) == True
# assert (checkFieldsValid(splitPassportToFields(validpassport3))) == True
# assert (checkFieldsValid(splitPassportToFields(validpassport4))) == True

print(checkAllPassports(input))
print(countFullyValidPassports(input))
