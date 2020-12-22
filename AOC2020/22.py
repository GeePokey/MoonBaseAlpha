sample = True
sample = False


"""

--- Day 22: Crab Combat ---
It only takes a few hours of sailing the ocean on a raft for boredom to sink in. Fortunately, you brought a small deck of space cards! You'd like to play a game of Combat, and there's even an opponent available: a small crab that climbed aboard your raft before you left.

Fortunately, it doesn't take long to teach the crab the rules.

Before the game starts, split the cards so each player has their own deck (your puzzle input). Then, the game consists of a series of rounds: both players draw their top card, and the player with the higher-valued card wins the round. The winner keeps both cards, placing them on the bottom of their own deck so that the winner's card is above the other card. If this causes a player to have all of the cards, they win, and the game ends.

For example, consider the following starting decks:

Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
This arrangement means that player 1's deck contains 5 cards, with 9 on top and 1 on the bottom; player 2's deck also contains 5 cards, with 5 on top and 10 on the bottom.

The first round begins with both players drawing the top card of their decks: 9 and 5. Player 1 has the higher card, so both cards move to the bottom of player 1's deck such that 9 is above 5. In total, it takes 29 rounds before a player has all of the cards:

-- Round 1 --
Player 1's deck: 9, 2, 6, 3, 1
Player 2's deck: 5, 8, 4, 7, 10
Player 1 plays: 9
Player 2 plays: 5
Player 1 wins the round!

-- Round 2 --
Player 1's deck: 2, 6, 3, 1, 9, 5
Player 2's deck: 8, 4, 7, 10
Player 1 plays: 2
Player 2 plays: 8
Player 2 wins the round!

-- Round 3 --
Player 1's deck: 6, 3, 1, 9, 5
Player 2's deck: 4, 7, 10, 8, 2
Player 1 plays: 6
Player 2 plays: 4
Player 1 wins the round!

-- Round 4 --
Player 1's deck: 3, 1, 9, 5, 6, 4
Player 2's deck: 7, 10, 8, 2
Player 1 plays: 3
Player 2 plays: 7
Player 2 wins the round!

-- Round 5 --
Player 1's deck: 1, 9, 5, 6, 4
Player 2's deck: 10, 8, 2, 7, 3
Player 1 plays: 1
Player 2 plays: 10
Player 2 wins the round!

...several more rounds pass...

-- Round 27 --
Player 1's deck: 5, 4, 1
Player 2's deck: 8, 9, 7, 3, 2, 10, 6
Player 1 plays: 5
Player 2 plays: 8
Player 2 wins the round!

-- Round 28 --
Player 1's deck: 4, 1
Player 2's deck: 9, 7, 3, 2, 10, 6, 8, 5
Player 1 plays: 4
Player 2 plays: 9
Player 2 wins the round!

-- Round 29 --
Player 1's deck: 1
Player 2's deck: 7, 3, 2, 10, 6, 8, 5, 9, 4
Player 1 plays: 1
Player 2 plays: 7
Player 2 wins the round!


== Post-game results ==
Player 1's deck: 
Player 2's deck: 3, 2, 10, 6, 8, 5, 9, 4, 7, 1
Once the game ends, you can calculate the winning player's score. The bottom card in their deck is worth the value of the card multiplied by 1, the second-from-the-bottom card is worth the value of the card multiplied by 2, and so on. With 10 cards, the top card is worth the value on the card multiplied by 10. In this example, the winning player's score is:

   3 * 10
+  2 *  9
+ 10 *  8
+  6 *  7
+  8 *  6
+  5 *  5
+  9 *  4
+  4 *  3
+  7 *  2
+  1 *  1
= 306
So, once the game ends, the winning player's score is 306.

Play the small crab in a game of Combat using the two decks you just dealt. What is the winning player's score?

To begin, get your puzzle input.

Answer: 
 

You can also [Share] this puzzle.
"""

xinputdata="""
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""


player1_sample="""
9
2
6
3
1
"""

player2_sample = """
5
8
4
7
10"""

player1_input = """
19
5
35
6
12
22
45
39
14
42
47
38
2
26
13
30
4
34
43
40
16
8
23
50
36
"""

player2_input = """
1
21
29
41
32
28
9
37
49
20
17
27
24
3
33
44
48
31
15
25
18
46
7
10
11
"""

if sample:
    player1 = player1_sample[:]
    player2 = player2_sample[:]
else:
    player1 = player1_input[:]
    player2 = player2_input[:]

p1 = [int( i ) for i in player1.split() if len(i) > 0]
p2 = [int( i ) for i in player2.split() if len(i) > 0]

while p1 and p2:
    a,b = p1.pop(0), p2.pop(0)
    if a>b:
        p1.append(a)
        p1.append(b)
    else:
        p2.append(b)
        p2.append(a)

winner = p1 if p1 else p2


print "part1 ", sum( (i+1)*v for i,v in enumerate( winner[::-1] ))

print "\n".join( "%d %3d" % ( i,v)  for i,v in enumerate( winner[::-1] ))

# =============================================================================
# part2

if sample:
    player1 = player1_sample[:]
    player2 = player2_sample[:]
else:
    player1 = player1_input[:]
    player2 = player2_input[:]

p1 = [int( i ) for i in player1.split() if len(i) > 0]
p2 = [int( i ) for i in player2.split() if len(i) > 0]

    
def score( w ): return sum( (i+1)*v for i,v in enumerate( w[::-1] ))

print score(p1), score(p2)

PLAYER1WIN=1
PLAYER2WIN=2
# playedbefore = set()

def combat2( p1,p2 ):
    playedbefore = set()    
    # print p1
    # print p2
    # print
    #raw_input()
    
    
    while p1 and p2:
        result = None

        key =  (score(p1),score(p2))
        # print "KEY:",key, len(p1), len(p2)
        if key in playedbefore:
            # print "DUP: alert   ------------"
            result = PLAYER1WIN
        else:
            playedbefore.add(key)

        a,b = p1.pop(0), p2.pop(0)
            
        if not result:
            if len(p1) >= a and len(p2) >= b:
                result =  combat2( p1[:a], p2[:b] )
            else:
                result = PLAYER1WIN if a>b else PLAYER2WIN

        # print "result:",result," of ",a,b

        
        if result == PLAYER1WIN:
            p1.append(a)
            p1.append(b)
        else:
            p2.append(b)
            p2.append(a)

        # print p1
        # print p2
        # print
            

    # winner = p1 if p1 else p2
    # print "part2 ", sum( (i+1)*v for i,v in enumerate( winner[::-1] ))
    # print "\n".join( "%d %3d" % ( i+1,v)  for i,v in enumerate( winner[::-1] ))
            
    
    return PLAYER1WIN if p1 else PLAYER2WIN

combat2( p1,p2)

winner = p1 if p1 else p2

print "part2 (35055) ", sum( (i+1)*v for i,v in enumerate( winner[::-1] ))


#part2  35055  11 PM
