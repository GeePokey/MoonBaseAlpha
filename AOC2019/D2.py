#Day2 part1
"""
kody only work but didnt optimize did day2dad and optimized with him
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

    def getNextFour(self,data,pointer):
        if data == []:
            print("getnextfour given empty list")
        if data[pointer]== 99:
            return 99,0,0,0
        try:
            return data[pointer],data[pointer+1],data[pointer+2],data[pointer+3]
        except:
            print(pointer,data)
            raise

    def part2nounverbcombo(self,data,pointer,desoutput):
        opcode,noun,verb,trash = self.getNextFour(data,pointer)
        print(100*noun+verb)
        if 100*noun+verb == desoutput:
            print(f"noun={noun} verb={verb}")
        else:
            pass

    def deref(self,toderef,data):
        return data[toderef]

    def operator(self,operation,data,pointer,desoutput=0):
        pos0, pos1, pos2, pos3 = self.getNextFour(data,pointer)

        if operation == "add":
            # print(pos1,pos2)
            return self.deref(pos1,data)+self.deref(pos2,data)
        elif operation == "mult":
            return self.deref(pos1,data)*self.deref(pos2,data)
        elif operation == "nounverb":
            self.part2nounverbcombo(data,pointer,desoutput)
        else:
            print(f"'add','mult','nounverb' are the available operations. Operation: '{operation}' in {data}")
            exit()

    def advancefour(self,data):
        return data[3:]

    def placeResultInList(self,toplace,data,pointer):
        where_to_place = data[pointer+3]
        data[where_to_place] = toplace
        return data

    def set1202error(self,data):
        data[1],data[2] = 12,2
        return data
    def setnounverb(self,data,noun,verb):
        data[1],data[2] = noun,verb
        return data
    def part2setselection(self,data,nounverbpair):
        noun,verb = nounverbpair
        data[1],data[2]=noun,verb
        return data

    def runProgram(self,print_or_return,programinput):
        data = self.readInput()
        # data = self.set1202error(data)
        data = self.setnounverb(data,programinput[0],programinput[1])
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
        if print_or_return == "p":
            print(data[0], data)
        elif print_or_return == "r":
            return data
        else:
            print("'p' for print 'r' for return")

    def findVerbNounForTarget(self,target):
        answerfound = False
        while not answerfound:
            for noun in range(0,99):
                for verb in range(0,99):
                    data =self.runProgram("r",(noun,verb))
                    if data[0] == target:
                        # print(noun,verb)
                        print(f"Answer:{100*noun+verb} noun={noun} verb={verb}")
                        answerfound = True
        # print(data[0])

Day2part1().runProgram("p",(79,60))
Day2part1().findVerbNounForTarget(19690720)

"""
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