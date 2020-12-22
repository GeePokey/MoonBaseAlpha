print "day21"
#dad

inputdata = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""

xinputdata = file('input.day21.txt').read()

possible = {}
allfoods = set()
allfoodcounters = {}
for i in inputdata.split("\n"):
    if "(contains" in i:
        foodstr, allergenstr = i.split("(contains ")
        foods = [i.strip() for i in foodstr.split(" ")]
        for f in foods:
            allfoods.add(f)
            if f in allfoodcounters:
                allfoodcounters[f] += 1
            else:
                allfoodcounters[f] = 1                
                
        allergens = [i.strip(" )") for i in allergenstr.split(",")]
        for a in allergens:
            if not a in possible:
                possible[a] = set(foods)
            else:
                possible[a] = possible[a] & set(foods)


print "\n Summary"                
for a in possible:
    print a, possible[a]
    allfoods = allfoods - possible[a]

print "\n Food's not in candidate ist", "none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen."
for s in allfoods:
    print s
print "part 1 (2374) ", sum(allfoodcounters[f] for f in allfoods)

"""
That's not the right answer. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 192.) [Return to Day 21]


192

Compilation finished at Sun Dec 20 21:46:08


2374 <<- gold star!!

Compilation finished at Mon Dec 21 20:39:43

part 1 (2374)  2374

Compilation finished at Mon Dec 21 20:40:36

"""
        
