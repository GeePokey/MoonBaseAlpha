import time
startime= time.time()
#Day2 part1
"""
deref values[1] = 12 deref value[2] = 2
1,2,99
1 adds deref pos[1] with deref pos[2] and stores in deref pos[3]
2 does the same but multiplies can make one func for both
99 means program is finished and should end immediately

Ask dad if theres a way to use deref=self.deref(params) or something so you can say deref(params) instead of self. everywhere
"""
class Day2part1():

    def readInput(self):
        with open(r"C:\Users\Kody\Dropbox\Programming\AdventOfCode\2019\D2_input.txt", "r",) as f:
            data = f.read().split(",")
            data =self.convertToInts(data)
        # data = "1,1,1,4,99,5,6,0,99".split(",")
        # data = self.convertToInts(data)
        return data

    def convertToInts(self,list_to_convert):
        return [int(i) for i in list_to_convert]

    def set1202error(self,data):
        data[1],data[2] = 12,2
        return data
    def setnounverb(self,data,noun,verb):
        data[1],data[2] = noun,verb
        return data

    def runProgram(self,print_or_return,data,programinput):
        # data = self.set1202error(data)
        data = self.setnounverb(data,programinput[0],programinput[1])
        endOfProgram = False
        pointer = 0
        while not endOfProgram:
            pos0 = data[pointer]
            if pos0 == 99:
                endOfProgram == True
                break
            destination,a,b = data[pointer + 3] , data[pointer + 1] , data[pointer + 2]
            if pos0 == 1: #Addinstruction
                data[destination] = data[a] + data[b]
            elif pos0 == 2: #Multinstruction
                data[destination] = data[a] * data[b]
            else:
                print(f"Error: Ran with {pos0} in {data}")
            pointer += 4
            if pointer > len(data):
                print("Ran out of code")
                endOfProgram == True
                break

        if print_or_return == "r":
            return data[0]
        elif print_or_return == "p":
            print(data[0], data)
        else:
            print("'p' for print 'r' for return")

    def findVerbNounForTarget(self,target):
        data = self.readInput()
        answerfound = False
        while not answerfound:
            for noun in range(0,99):
                for verb in range(0,99):
                    data0=self.runProgram("r",data[:],(noun,verb))
                    if data0 == target:
                        # print(noun,verb)
                        print(f"Answer:{100*noun+verb} noun={noun} verb={verb}")
                        answerfound = True
        # print(data[0])

Day2part1().runProgram("p",Day2part1().readInput(),(79,60))
Day2part1().findVerbNounForTarget(19690720)
print("Runtime:%5.3f"%(time.time()-startime))
"""
1.08 initial time
        data = self.readInput()
        data = self.part2setselection(data,(noun,verb))
        endOfProgram = False
        pointer = 0
        while not endOfProgram:
            pos0 = self.getNextFour(data,pointer)[0]
            # print("pos0",pos0)
            if pos0 == 1:
                data = self.placeResultInList(self.operator("add",data,pointer),data,pointer)
            elif pos0 == 2:
                data = self.placeResultInList(self.operator("mult",data,pointer),data,pointer)
            elif pos0 == 99:
                endOfProgram == True
                break
            else:
                print(f"Error: Ran with {pos0} in {data}")
            pointer += 4
            if pointer > len(data):
                endOfProgram == True
                break
        if data[0] == 19690720:
            print(noun,verb)
            print(f"Answer:{100*noun+verb}noun={noun} verb={verb}")
            answerfound = True

"""