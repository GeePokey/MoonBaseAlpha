debug_flag = True

def debug(*argv):
    if debug_flag == True:
        for arg in argv:
            print(arg, end=' ')
        print() # one newline at end


x = 4
debug('test')
debug('test',123)
debug('test',123,x,'testend')
