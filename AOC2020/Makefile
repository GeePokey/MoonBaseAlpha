fcmd=/Library/Frameworks/Mono.framework/Versions/Current/bin/fsharpc
mcmd=time /Library/Frameworks/Mono.framework/Versions/Current/bin/mono



log16: 16.fs 
	$(fcmd) 16.fs
	$(mcmd) 16.exe > 16.log

all2:  aoc19_day19_part2.exe 


dall: aoc19_day9.exe   aoc19_day3.exe  


log: aoc19_day25.fs makefile mytyping.txt
	$(fcmd) aoc19_day25.fs
	$(mcmd) aoc19_day25.exe < mytyping.txt

%.exe : %.fs *.txt makefile
	$(fcmd) $<
	$(mcmd) $@


%.exerun : %.fs
	$(mcmd) $@

%.exeonly : %.fs
	$(fcmd) $<

