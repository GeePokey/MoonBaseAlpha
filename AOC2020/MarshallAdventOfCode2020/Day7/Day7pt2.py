def parseline(line):
    wopunct = []
    for i in line:
        
        if not i == ' ' and not i =='.':
            wopunct.append(i)
        stripped_line = ''.join(wopunct)
    print(stripped_line)
    container = stripped_line.split('contain')[0][:-4]
    print(container)
            
    contents_list = stripped_line.split('contain')[1]
    contents_list = contents_list.split(',')

    contents_dict = {}
    for c in contents_list:
        print('c',c)
        if not c == 'nootherbags\n':
            number = int(c[:1])
            bag = c[1:]
            if bag.endswith('\n'):
                bag = bag[:-1]
                    #print('stripped n',k)
                
            if bag.endswith('bag'):
                bag = bag[:-3]
            if bag.endswith('bags'):
                bag = bag[:-4]
            contents_dict[bag] = number
    print(container, contents_dict)
    return container, contents_dict
        
# test line for parseline:
# parseline('dotted lavender bags contain 3 pale crimson bags, 3 wavy gray bags, 2 plaid plum bags, 5 mirrored bronze bags.\n')

def bagcheck2():
    # make a dictionary of all bags and contents:
    bagsandcontents = {}
    with open('./input.txt') as input:
        for line in input:
            container,contents_dict = parseline(line)
            bagsandcontents[container] = contents_dict
    #print(bagsandcontents)
    #print(bagsandcontents['drabturquoise'])
    return bagsandcontents


def countbags(currentbag):
    contents = bagsandcontents[currentbag]
    numberofbags = 1 # (the container/current bag)
    if len(contents) == 0:
        return numberofbags
    else: # there are bags inside
        for bagtype in contents:
            numberofbags += contents[bagtype] * countbags(bagtype)

    return numberofbags


############## Run Stuff for Part 2 ##############

# Make dictionary:
bagsandcontents = bagcheck2()
# Count the bags inside
currentbag = 'shinygold'
totalbags = countbags(currentbag)
totalbags -= 1 # Subtract the initial shiny gold bag
print('total bags:',totalbags)






############## Old Stuff from Part 1 ##############


def bagcheck(current_list):
    with open('./input.txt') as input:
        for line in input:
            wodigits = []
            print('line',line)

            for i in line:
                if not i.isdigit() and not i == ' ' and not i =='.':
                    wodigits.append(i)
            stripped_line = ''.join(wodigits)
            #print(stripped_line)
            container = stripped_line.split('contain')[0][:-4]
            #print(container)
            
            contents = stripped_line.split('contain')[1]
            contents = contents.split(',')
            if isinstance(contents,str):
                contents = [contents]
            #print(contents)
            #print('string?',isinstance(contents,str))
            newcontents = []
            
            for k in contents:
                #print('k',k)
                if k.endswith('\n'):
                    k = k[:-1]
                    #print('stripped n',k)
                
                if k.endswith('bag'):
                    newcontents = newcontents + [k[:-3]]
                if k.endswith('bags'):
                    newcontents = newcontents + [k[:-4]]
                else:
                    newcontents = newcontents + [k]
            contents = newcontents
            #print('newcontents:',newcontents)
            for i in current_list:
                if i in newcontents and not container in current_list:
                    current_list = current_list + [container]
                    print('line:',line)
                    print('valid:',container)
                    print('currentlist',current_list)
        return current_list
        


list = ['shinygold'] # have to remove from list later!
length = 1
complete = False
while complete == True:
    list = bagcheck(list)
    if len(list) == length:
        # print('finished')
        complete = True
    else:
        #do it again

        length = len(list) 

#print(length-1,'containers') #(Shiny Gold doesn't count!!
