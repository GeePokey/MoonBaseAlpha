print "Day 17 part2"

ACTIVE = '#'
INACTIVE = '.'

input1 = """..#..#..
.###..#.
#..##.#.
#.#.#.#.
.#..###.
.....#..
#...####
##....#."""

xinput1 = """.#.
..#
###"""

#   01234567
# 0 ..#..#..
# 1 .###..#.
# 2 #..##.#.
# 3 #.#.#.#.
# 4 .#..###.
# 5 .....#..
# 6 #...####
# 7 ##....#.

print sum(1 for i in input1 if i == ACTIVE)
input = input1.split("\n") 

print input
u = {}

w = 0
z = 0
for r, row in enumerate(input):
    for c,col in enumerate(row):
        if col == ACTIVE :
            u[c,r,z,w] = col

print len(u)

#  If a cube is active and exactly 2 or 3 of its neighbors are also active,
#  the cube remains active. Otherwise, the cube becomes inactive.
# 
#  If a cube is inactive but exactly 3 of its neighbors are active,
#  the cube becomes active. Otherwise, the cube remains inactive.

offsets = [ (x,y,z,w) for x in [-1,0,1] for y in  [-1,0,1] for z in [-1,0,1] for w in [-1,0,1] if not(x==0 and y==0 and z==0 and w==0)]
print "offsets\n",offsets
print len(offsets)

def activeneighboorcount(pre, (x,y,z,w) ):
    genex =  ( (x + a, y + b , z + c , w + d ) for a,b,c,d in offsets ) 
    return sum( 1 for c3 in genex if c3 in pre and pre[c3] == ACTIVE)

def all_inactive_neighboors(pre):
    for x,y,z,w in pre:
        genex =  ( (x + a, y + b , z + c, w + d ) for a,b,c,d in offsets ) 
        for nc in genex:
            if not nc in pre: # [nc] == INACTIVE:
                yield nc
        
def cycle(pre):
    newu = {}            
    for ka in pre:
        if activeneighboorcount( pre,ka) in [2,3]:
            newu[ka] = ACTIVE
            # del newu[k] # remove from active array

    for ki in all_inactive_neighboors(pre):
        if activeneighboorcount(pre,ki) == 3:
            newu[ki] = ACTIVE

    return newu


def dump_u(univ,cycleid):
    x1 = min( a for a,b,c,d in univ )
    x2 = max( a for a,b,c,d in univ )    

    y1 = min( b for a,b,c,d in univ )
    y2 = max( b for a,b,c,d in univ )
    
    z1 = min( c for a,b,c,d in univ )
    z2 = max( c for a,b,c,d in univ )    

    w1 = min( d for a,b,c,d in univ )
    w2 = max( d for a,b,c,d in univ )    
    
    print "Cycle ",cycleid, len(univ)
    
    for w in range(w1,w2+1):
        for z in range(z1,z2+1):
            print "  z = ",z
            for y in range(y1,y2+1):
                row = "       "
                for x in range(x1,x2+1):
                    row += ACTIVE if (x,y,z,w) in univ else INACTIVE
                print row


for i in range(7):
    dump_u(u,i)
    u = cycle(u)

# part1 Cycle  6 242
# Compilation finished at Wed Dec 16 21:54:42

