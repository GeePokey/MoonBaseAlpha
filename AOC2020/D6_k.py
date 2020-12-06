import re

def readInput():
    with open(r"C:\Users\Kody\GitExperiment\MoonBaseAlpha\AOC2020\D6_kinput.txt", "r",) as f:
    # with open(r"C:\Users\Kody\GitExperiment\MoonBaseAlpha\AOC2020\good.txt", "r",) as f:
        data = f.read()#.split('\n\n')
    # input = [list(i) for i in data]
    return data

input = readInput()
# print(input)
#input is

def countSingleTotal(oneGroup):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    total = 0
    for i in alphabet:
        if i in oneGroup:
            total += 1
    return total

def addAllTotals(strOfGroups):
    total = 0
    groups = list(strOfGroups.split("\n\n"))
    for group in groups:
        total += countSingleTotal(group)
    return total

def countYesTotal(oneGroup):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    total = 0
    eachPerson = oneGroup.split("\n")
    for letter in alphabet:
        flag = 0
        for person in eachPerson:

            if letter in person:
               flag += 1
               continue
        if flag == len(eachPerson):
            total += 1
    return total


def addAllYes(strOfGroups):
    total = 0
    groups = list(strOfGroups.split("\n\n"))
    for group in groups:
         total += countYesTotal(group)
    return total

example = '''abc

a
b
c

ab
ac

a
a
a
a

b'''
# print(addAllTotals(example))
# print(addAllTotals(input))
print(countYesTotal("""abc
a
abc"""))
print(addAllYes(example))
print(addAllYes(input))