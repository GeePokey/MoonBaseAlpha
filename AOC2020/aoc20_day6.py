#!python2
# this took a ridiculous amount of debugging

import fileinput
import operator

def scan_file( myop):
    accum = None
    with open("input.day6.txt") as fp:
        for i in fp:
            if len(i.strip()) == 0:
                   yield len(accum)
                   accum = None
            else:
                accum = set(i.strip())  if accum is None else myop(accum , set(i.strip()))


print "Part 1", sum( scan_file( operator.__or__))
print "Part 2", sum( scan_file( operator.__and__))


                
