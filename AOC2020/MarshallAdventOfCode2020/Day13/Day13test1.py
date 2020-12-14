def Day13():
    multiplier = 0
    finished = False
    current = 787
    divisor = 439
    distance = 31
    while finished == False:
        multiplier += 1
        top = multiplier * current
        if (top-distance)%divisor == 0:
            print(top,multiplier)
            finished = True

#Day13()
        
        
def try2():
    multiplier = 0
    finished = False
    current = 439*13*23*41*17
    while finished == False:
        multiplier += 1
        c = multiplier * current
        if (c+31)%787 == 0:
            if (c+2)%29 == 0 and (c+50)%19 == 0 and (c-6)%37 == 0:
                print(c,multiplier)
                print('starting number:',c-17)
                finished = True

        
        # if c%13 == 0 and c%23 == 0 and c%41 == 0 and c%17 == 0:
        #     print('mult of 13,23,41,439,17:',c)
        #     if (c+31)%787 == 0:
        #         if (c+2)%29 == 0 and (c+50)%19 == 0 and (c-6)%37 == 0:
        #             print(c,multiplier)
        #             finished = True

try2()
