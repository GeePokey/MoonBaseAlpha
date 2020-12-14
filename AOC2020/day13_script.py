
base = 99999999999551L
increment =  8399999999774L

command = "time /Library/Frameworks/Mono.framework/Versions/Current/bin/mono ./13.exe %d %d "

for i in range(1,5):
    print command % (base + i * increment , base + i * increment + increment)
