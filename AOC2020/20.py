description = """
Advent of Code[About][Events][Shop][Settings][Log Out]geepokey 37*
      /^2020$/[Calendar][AoC++][Sponsors][Leaderboard][Stats]
Our sponsors help make Advent of Code possible:
GitHub - We're hiring engineers to make GitHub fast. Interested? Email fast@github.com with details of exceptional performance work you've done in the past.

--- Day 20: Jurassic Jigsaw ---

The high-speed train leaves the forest and quickly carries you
south. You can even see a desert in the distance! Since you have some
spare time, you might as well see if there was anything interesting in
the image the Mythical Information Bureau satellite captured.

After decoding the satellite messages, you discover that the data
actually contains many small images created by the satellite's camera
array. The camera array consists of many cameras; rather than produce
a single square image, they produce many smaller square image tiles
that need to be reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile
with a random unique ID number. The tiles (your puzzle input) arrived
in a random order.

Worse yet, the camera array appears to be malfunctioning: each image
tile has been rotated and flipped to a random orientation. Your first
task is to reassemble the original image by orienting the tiles so
they fit together.

To show how the tiles should be reassembled, each tile's image data
includes a border that should line up exactly with its adjacent
tiles. All tiles have this border, and the border lines up exactly
when the tiles are both oriented correctly. Tiles at the edge of the
image also have this border, but the outermost edges won't line up
with any other tiles.

For example, suppose you have the following nine tiles:

Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:

#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....
For reference, the IDs of the above tiles are:

1951    2311    3079
2729    1427    2473
2971    1489    1171
To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?

To begin, get your puzzle input.

Answer: 
 

You can also [Share] this puzzle.
"""
xinputdata = file("input.day20.txt").read()

inputdata = """

Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...

"""

alltiles={}
allborders={}
BLEFT = 0
BTOP = 1
BRIGHT =2
BBOTTOM = 3
class CTile:
    def __init__(self,idnum):
        self.idnum = idnum
        alltiles[idnum] = self
        self.data = []
        self.borders =[]
        self.flipped =[]
        self.corner = False
        
    def __repr__(self):
        return "\nTile #%d\n" % self.idnum + "\n".join(self.data)+"\n"


    def record_border_key(self,key):
        self.borders.append(key)
        if not key in allborders:
            allborders[key] = []
        if not self in allborders[key]:
            allborders[key].append(self)


    def record_flipped_key(self,key):
        self.flipped.append(key)
        if not key in allborders:
            allborders[key] = []
        allborders[key].append(self)

            
    def record_both_keys(self,key):
        self.record_border_key(  hashtobin( key        ) )
        self.record_flipped_key( hashtobin( key[::-1]  ) )                            

    def gen_border_keys(self):
        self.borders = []  # re-initialize for post spin update
        self.flipped = []  # re-initialize for post spin update
        # self.record_both_keys( self.data[  0] ) #top
        # self.record_both_keys( self.data[ -1][::-1] )     #bottom    
        # self.record_both_keys( "".join(i[  0] for i in self.data[::-1]) ) #left    
        # self.record_both_keys( "".join(i[ -1] for i in self.data) ) #right

        self.record_both_keys( "".join(i[  0] for i in self.data[::-1]) ) #left    
        self.record_both_keys( self.data[  0] ) #top
        self.record_both_keys( "".join(i[ -1] for i in self.data) ) #right
        self.record_both_keys( self.data[ -1][::-1] )     #bottom    
        
    def common_boarder_count(self):
        return sum( len(allborders[k]) for k in self.borders) + sum( len(allborders[k]) for k in self.flipped) 


    def rotate_cw_90(self):
        r = []
        for i in range(len(self.data)):
            r.append( "".join( d[i] for d in self.data[::-1] ))
        self.data = r
        self.gen_border_keys()

    def rotate_180(self):
        self.data =  [  d[::-1] for d in self.data[::-1] ]
        self.gen_border_keys()

    def mirror(self):
        self.data =  [  d[::-1] for d in self.data ]
        self.gen_border_keys()
        
    def spin_by_left_side_key(self, key):
        """ for left side matching - we need the flipped version of the key
        so if found in borders, get the key in the same orientation from
        the flipped list, and rotate THAT to the left."""
        if key in self.borders:
            key = self.flipped[self.borders.index(key)]
            self.mirror()
        else:
            key = self.borders[self.flipped.index(key)]
            
        assert( key in self.borders)
        if key in self.borders:
            i = self.borders.index(key)
            if i == 0:
                pass
            elif i == 1:
                self.rotate_cw_90()
                self.rotate_180()
            elif i == 2:
                self.rotate_180()
            elif i == 3:
                self.rotate_cw_90()

    def spin_by_top_side_key(self, key):
        """ for left side matching - we need the flipped version of the key
        so if found in borders, get the key in the same orientation from
        the flipped list, and rotate THAT to the left."""
        if key in self.borders:
            key = self.flipped[self.borders.index(key)]
            self.mirror()
        else:
            key = self.borders[self.flipped.index(key)]
            
        assert( key in self.borders)
        if key in self.borders:
            i = self.borders.index(key)
            if i == 0:
                self.rotate_cw_90()
            elif i == 1:
                pass
            elif i == 2:
                self.rotate_cw_90()
                self.rotate_180()
            elif i == 3:
                self.rotate_180()

                

    def xspin_by_left_side_key(self, key):
        """ for left side matching - we need the flipped version of the key
        so if found in borders, get the key in the same orientation from
        the flipped list, and rotate THAT to the left."""
        if key in self.borders:
            key = self.flipped[self.borders.index(key)]
            self.mirror()
        else:
            key = self.borders[self.flipped.index(key)]
            
        assert( key in self.borders or key in self.flipped)
        if key in self.borders:
            i = self.borders.index(key)
            if i == 0:
                pass
            elif i == 1:
                self.rotate_cw_90()
                self.rotate_180()
            elif i == 2:
                self.rotate_180()
            elif i == 3:
                self.rotate_cw_90()
        if key in self.flipped:
            self.mirror()
            i = self.flipped.index(key)
            if i == 0:
                self.rotate_180()
            elif i == 1:
                self.rotate_cw_90()
                self.rotate_180()
            elif i == 2:
                pass
            elif i == 3:
                self.rotate_cw_90()
        self.gen_border_keys()
        
    def get_non_shared_side(self):
        for i in self.borders:
            if len(allborders[i]) == 1:
                return i

    def get_right_neighboor(self):
        rid = self.borders[BRIGHT]
        rightneighboor = [i for i in allborders[rid] if not i == self]
        if rightneighboor:
            return rightneighboor[0]
        else:
            return None

    def get_bottom_neighboor(self):
        bid = self.borders[BBOTTOM]
        # print "\nbid.b = ",bid, [len(allborders[a]) for a in self.borders]
        bottomneighboor = [i for i in allborders[bid] if not i == self]
        if bottomneighboor:
            return bottomneighboor[0]
        else:
            bid = self.flipped[BBOTTOM]
            # print "bid.f = ",bid,  [len(allborders[a]) for a in self.flipped]
            bottomneighboor = [i for i in allborders[bid] if not i == self]
            if bottomneighboor:
                return bottomneighboor[0]
            else:
                return None
        
    
    def spin_to_top_left(self):
        orient = [len(allborders[i]) for i in self.borders]        
        for i in range(4):
            if not (( orient[0] == 1) and (orient[1] == 1)):
                self.rotate_cw_90()
                orient = [len(allborders[i]) for i in self.borders]
            
    def show_shared_sides(self):
        for i in self.borders:
            print i, len(allborders[i])
        for i in self.flipped:
            print i, len(allborders[i])

        
        

        
def hashtobin(s):
    "convert #.# to 101 and return int"
    return int(s.replace('#','1').replace('.','0'),2)


def scan_input(lines):
    for i in lines:
        if "Tile" in i:
            t = CTile( int(i.split()[1][:-1]) )
        if len(i)>0 and i[0] in ".#":
            t.data.append(i.strip())

            
            
scan_input(inputdata.split("\n"))
print len(alltiles), "found."

def gen_all_tiles():
    k = alltiles.keys()
    k.sort()
    for i in k:
        v = alltiles[i]
        v.gen_border_keys()

def dump_all_tiles():
    k = alltiles.keys()
    k.sort()
    for i in k:
        v = alltiles[i]
        print v
        print
        print ["%03X"%hashtobin(d) for d in v.data]
        print ["%03X"%h for h in v.borders]
        print ["%03X"%h for h in v.flipped]

gen_all_tiles()

# print allborders

for zl in allborders:
    print "\n"*3
    print zl
    for z in allborders[zl]:
        print z
        print z.borders, z.flipped
    break

# count = 0
# for zl in allborders:
#     if len(allborders[zl]) > 1:
#         count+=1
#         print count,"key",zl, "=", len(allborders[zl])


corners = sorted([(v.common_boarder_count(),v) for v in alltiles.values()])
accum = 1
for i,j in corners:
    # print i, j.idnum, accum
    if i == 12:
        accum = accum * j.idnum
        j.corner = True

PART1_ANSWER= 17148689442341        
SAMPLE_ANSWER= 20899048083289
ANSWER = SAMPLE_ANSWER

print "part1 (17148689442341) ", accum        , accum- SAMPLE_ANSWER

assert ( accum == SAMPLE_ANSWER )
"""
14 2729 20899048083289
16 1427 20899048083289
part1  20899048083289
       20899048083289 sample
Compilation finished at Sat Dec 19 23:20:56

16 3169 17148689442341
16 1193 17148689442341
part1  17148689442341  gold star

Compilation finished at Sat Dec 19 23:21:36
"""


"""
Layout Tiles
pick any corners - i.e. first four entries in corners
rotate that tile until the sides with no shared borders are top and left
find right side tile rotate appropriately
repeat until we reach another corner
go back to left or just move down ?
"""


start = corners[0][1]
# start.show_shared_sides()
# print start.get_non_shared_side()
# print start
# start.show_shared_sides()
start.spin_to_top_left()
# print start
# start.show_shared_sides()
# rightside = start.borders[BRIGHT]
# print "rightside", rightside
# # print "allborders[rightside]"
# # print allborders[rightside]
# rn = start.get_right_neighboor()
# print rn
# rn.show_shared_sides()
# rn.spin_by_left_side_key(rightside)
# print start
# print rn


def advance_right_neighboor(start):
    rightside = start.borders[BRIGHT]
    print "rightside", rightside
    rn = start.get_right_neighboor()
    if rn:
        rn.spin_by_left_side_key(rightside)
    return rn


def dump_row_of(tilelist):
    for i in range(len(tilelist[0].data)):
        print " ".join(t.data[i] for t in tilelist)

def dump_trimmed_row_of(tilelist):
    for i in range(1,len(tilelist[0].data)-1):
        print "".join(t.data[i][1:-1] for t in tilelist)
        

def advance_bottom_neighboors(rowtiles):
    rowtiles2 = []

    for t in rowtiles:
        bside = t.borders[BBOTTOM]
        bn = t.get_bottom_neighboor()
        if bn:
            bn.spin_by_top_side_key(bside)
            rowtiles2.append(bn)
        else:
            print "No bottom neighboor for ", t.idnum
    return rowtiles2

def do_puzzle_from_corner( c ):
    atile = c
    rowtiles = [atile]
    print "======="
    while atile:
        # print atile
        atile = advance_right_neighboor(atile)
        if atile:
            rowtiles.append(atile)
        
    puzzle = [rowtiles]

    puzzle.append( advance_bottom_neighboors( rowtiles ) )
    puzzle.append( advance_bottom_neighboors( rowtiles ) )
    return puzzle

puzzle = do_puzzle_from_corner( start )
    
for prow in puzzle:
    dump_row_of( prow )
    print

print "\nTrimmed\n"    
for prow in puzzle:
    dump_trimmed_row_of( prow )

    
""" sample trimmed image
.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###
"""
