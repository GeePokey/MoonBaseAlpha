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
while complete == False:
    list = bagcheck(list)
    if len(list) == length:
        print('finished')
        complete = True
    else:
        #do it again

        length = len(list) 

print(length-1,'containers') #(Shiny Gold doesn't count!!
