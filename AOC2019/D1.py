
import math



nums = """110321
61817
107271
126609
84016
119187
53199
117553
83163
69434
62734
76774
75016
126859
114626
70782
102903
105871
108500
149367
99266
131731
86778
110561
116521
138216
55347
135516
126801
124902
103083
130858
54885
126837
71103
143975
135207
77264
149331
85252
78910
84007
123953
87355
113433
57750
78394
106081
110942
118180
71745
60080
56637
105491
111329
71799
59962
60597
75241
102506
75341
129539
71011
127185
51245
144401
78592
116835
52029
134905
80104
146304
113780
108124
131268
124765
78847
76897
56445
116487
62068
125176
122259
134261
101127
127089
55793
113113
132835
118901
59574
113399
73232
93720
144450
129604
101741
108759
55891
52939"""

splitnums = nums.split("\n")
#advent of code day 1 part 1

def findfuel(list_of_masses):
    fueltotal = 0
    for i in list_of_masses:
        fueltotal += math.floor(int(i) / 3) - 2
    return fueltotal
print(findfuel(splitnums))

#day 1 advent of code


def beard(mass_orfuel):
    return findSingleFuelWeightTotal(mass_orfuel)

def findSingleFuelWeightTotal(mass_or_fuel,total=0):
    mass_or_fuel = int(mass_or_fuel)
    fuel_cost = math.floor(int(mass_or_fuel) / 3) - 2
    if fuel_cost <= 0:
        return total
    else:
        print(total)
        total += fuel_cost
        return findSingleFuelWeightTotal(fuel_cost,total)

def findAllFuelIncFuelWeight(list_of_masses):
    fueltotal = 0
    for i in list_of_masses:
        fueltotal += findSingleFuelWeightTotal(i)
    return fueltotal
print(findAllFuelIncFuelWeight(splitnums))





