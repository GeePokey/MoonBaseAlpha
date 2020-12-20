print "day 19"
inputd = file("input.day19.txt").read()

xinputd = """0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"
"""

xinputd = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
 """
# again
xinputd = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba

"""
"""
mine
 
bbabb  	bbaab  	aabba
bbabbbbaabaabba

bbabb  	bbaab bbaab aabba aabba
bbabbbbaabbbaabaabbaaabba

"""


 # part 2
 # 8: 42 | 42 8
 # 11: 42 31 | 42 11 31
 #
 
inputl = inputd.split("\n")
rules = [i for i in inputl if ":" in i]
messages = [i for i in inputl  if len(i)>0 and not(":" in i)]

# print rules
print "\nMessages\n"
# print messages

rd={}

for r in rules:
    s = r.split(":")
    rd[s[0]] = s[1].strip()

# print rd

r0 = "0"
PIPE = "|"
def expand_rule(k):
    if k == PIPE:
        return PIPE
    if k == '"a"':
        return 'a'
    if k == '"b"':
        return 'b'


    return "".join(( "(?:" + expand_rule(j) + ")" for j in rd[k].split(" ") ))

            
def part1():    
   z = expand_rule("0")
   z = z.replace("(?:|)","|").replace('(?:a)', 'a').replace('(?:b)','b').replace('(?:a)', 'a').replace('(?:b)','b') + "$"
   # print z
   import re
   re = re.compile(z)

   for m in messages:
       if re.match(m):
           print "+",m
       else:
           print "-",m
           

   print "part 1 (173) ", sum( 1 for m in messages if re.match(m))

# part1()

"""
(* attempt 1
 (((a((a((b(aa)|a(ba|aa))a|((ab|b(a|b))b|(a(a|b)|bb)a)b)|b(b((ba|aa)b|(ab|b(a|b))a)|a(b(ab|b(a|b))|a(ba|aa))))b|((b((a(a|b)|bb)(a|b))|a((bb|ab)a|(a(a|b)|bb)b))a|((a(bb|ab)|b(ab|aa))a|((bb|ab)a|(aa|bb)b)b)b)a)|b(((((bb)a|(a(a|b)|bb)b)b|((aa)b|(bb|ab)a)a)a|(a(a(a(a|b)|bb)|b(ab))|b(b(ab|b(a|b))|a(ab|aa)))b)b|(b((b(bb|ab)|a(ba))a|((aa)b|(bb|ab)a)b)|a((a(a(a|b)|bb)|b(ab))a|(a(bb|ab)|b(ab|aa))b))a))a|((((a((ab)a|((a|b)(a|b))b)|b(b(ab|aa)|a(aa|bb)))a|(b((bb|ab)a|((a|b)a|ab)b)|a(((a|b)a|ab)b|(bb)a))b)b|(b(a((bb)a|(bb|ab)b)|b((aa|bb)b|(ab|b(a|b))a))|a(a(b((a|b)a|ab)|a(ab|aa))|b(b(ba|aa))))a)b|(b(a((a(aa|bb)|b(bb|ab))a|((ba|aa)b|(ab|b(a|b))a)b)|b(b((ba)a|(bb)b)|a(((a|b)(a|b))a|(ab|b(a|b))b)))|a((((bb)b)a|((ba)a|(bb|ab)b)b)a|((a(aa))b|((a|b)(aa|bb))a)b))a)b))(((a((a((b(aa)|a(ba|aa))a|((ab|b(a|b))b|(a(a|b)|bb)a)b)|b(b((ba|aa)b|(ab|b(a|b))a)|a(b(ab|b(a|b))|a(ba|aa))))b|((b((a(a|b)|bb)(a|b))|a((bb|ab)a|(a(a|b)|bb)b))a|((a(bb|ab)|b(ab|aa))a|((bb|ab)a|(aa|bb)b)b)b)a)|b(((((bb)a|(a(a|b)|bb)b)b|((aa)b|(bb|ab)a)a)a|(a(a(a(a|b)|bb)|b(ab))|b(b(ab|b(a|b))|a(ab|aa)))b)b|(b((b(bb|ab)|a(ba))a|((aa)b|(bb|ab)a)b)|a((a(a(a|b)|bb)|b(ab))a|(a(bb|ab)|b(ab|aa))b))a))a|((((a((ab)a|((a|b)(a|b))b)|b(b(ab|aa)|a(aa|bb)))a|(b((bb|ab)a|((a|b)a|ab)b)|a(((a|b)a|ab)b|(bb)a))b)b|(b(a((bb)a|(bb|ab)b)|b((aa|bb)b|(ab|b(a|b))a))|a(a(b((a|b)a|ab)|a(ab|aa))|b(b(ba|aa))))a)b|(b(a((a(aa|bb)|b(bb|ab))a|((ba|aa)b|(ab|b(a|b))a)b)|b(b((ba)a|(bb)b)|a(((a|b)(a|b))a|(ab|b(a|b))b)))|a((((bb)b)a|((ba)a|(bb|ab)b)b)a|((a(aa))b|((a|b)(aa|bb))a)b))a)b)(a(b((a((a(aa|bb)|b((a|b)(a|b)))a|(b(ba|aa)|a((a|b)(a|b)))b)|b((b(bb)|a((a|b)(a|b)))a|((bb|ab)a|(aa|bb)b)b))b|((a(a(bb|ab)|b(aa))|b(b(bb)|a(aa|bb)))b|(((ba)a|(ba)b)a|(a(bb|ab)|b(ba|aa))b)a)a)|a((((b(ab|aa)|a(aa))a|((aa|bb)b|(ba|aa)a)b)a|((a(ab)|b(aa))b|(b(ab|b(a|b))|a(bb|ab))a)b)a|(((a(ba|bb)|b(a(a|b)|bb))b|(a((a|b)(a|b))|b((a|b)a|ab))a)a|(a(a(bb|ab)|b(ba|aa))|b((ab)b|(bb)a))b)b))|b((a((a(((a|b)a|ab)a|(ba|ab)b)|b((aa)b|(ab|aa)a))b|(((ab|b(a|b))a|(aa)b)a|(b(bb)|a(aa|bb))b)a)|b(((a(aa|bb)|b(ab))a|((aa|bb)b|(ba|bb)a)b)b|(a(a(ab))|b(b(ba|ab)|a((a|b)(a|b))))a))b|(a(a(a((ab)a|(ba|aa)b)|b((ab)b|(ab|aa)a))|b((b((a|b)(a|b))|a(aa))a|(b(a(a|b)|bb)|a(ba|ab))b))|b(a((a(ba|aa)|b((a|b)(a|b)))b|(b(ba|bb)|a((a|b)a|ab))a)|b((a(ab)|b(aa))b|((ba|aa)a|(a(a|b)|bb)b)a)))a)))$
Traceback (most recent call last):
  File "19.py", line 58, in <module>
    re = re.compile(z)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/re.py", line 194, in compile
    return _compile(pattern, flags)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/re.py", line 249, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/sre_compile.py", line 583, in compile
    "sorry, but this version only supports 100 named groups"
AssertionError: sorry, but this version only supports 100 named groups

Compilation exited abnormally with code 1 at Fri Dec 18 21:30:10

 *)

attempt 2



attempt #3 gold star
- 
- abbbaaaaaabbbaabababaaab

+ bbbbbbabaaabbbaabaaaaaba
- babbbabbaabbaaaabbaaaaabbbaabbbbabaabbba
+ abbbaabbababbaaabaaaaaba
- 
part 1  173

Compilation finished at Fri Dec 18 21:34:58


part 2


(?:(?:(?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a))(?:(?:(?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a)(?:b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))))$
- 
- abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
+ bbabbbbaabaabba
- babbbbaabbbbbabbbbbbaabaaabaaa
- aaabbbbbbaaaabaababaabababbabaaabbababababaaa
- bbbbbbbaaaabbbbaaabbabaaa
- bbbababbbbaaaaaaaabbababaaababaabab
+ ababaaaaaabaaab
+ ababaaaaabbbaba
- baabbaaaabbaaaababbaababb
- abbbbabbbbaaaababbbbbbaaaababb
- aaaaabbaabaaaaababaa
- aaaabbaaaabbaaa
- aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
- babaaabbbaaabaababbaabababaaab
- aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
- 
part 1 (173)  3
((?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a)|((?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a)((?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)ab(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a)))|((?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)ab(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a)))$
- 
+ abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
+ bbabbbbaabaabba
+ babbbbaabbbbbabbbbbbaabaaabaaa
+ aaabbbbbbaaaabaababaabababbabaaabbababababaaa
+ bbbbbbbaaaabbbbaaabbabaaa
+ bbbababbbbaaaaaaaabbababaaababaabab
+ ababaaaaaabaaab
+ ababaaaaabbbaba
+ baabbaaaabbaaaababbaababb
+ abbbbabbbbaaaababbbbbbaaaababb
+ aaaaabbaabaaaaababaa
+ aaaabbaaaabbaaa
+ aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
- babaaabbbaaabaababbaabababaaab
+ aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
- 
part 2 (173)  14

Compilation finished at Fri Dec 18 21:50:53

 ((?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a)
|((?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a  \1)

 ((?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a  b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a)))
|((?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a \2
b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a)))$
"""


 # part 2
 # 8: 42 | 42 8
 # 11: 42 31 | 42 11 31
 # 0: 8 11

# | (?: 42    -     31
# | (?: 42 42 31 31
# | (?: 42 42 42 31 31 31
# | (?: 42 42 42 42 31 31 31 31
# | (?: 42 42 42 42 42 31 31 31 31 31 
"""
(?:
 (?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a
)
+
 (?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a
 (?:
 e (?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)ab(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))
 )
*
                                                                                                                            b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))$

 r31:b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))$
 r42:(?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a

(?:
    (?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a
)+

(?:
    (?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a 
    b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))
)

|

(?:
    (?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a
    (?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a
    b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))
    b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))
)
|
(?:
    (?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a
    (?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a
    (?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a
    b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))
    b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))
    b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))
)
|
(?:
    (?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a(?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a(?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a(?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)ab(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a)))$

((?:(?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a)+)
(|(?:(?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)ab(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a)))|(?:(?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a(?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)ab(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))b(?:b(?:a(?:ba)|b(?:aa))|a(?:b(?:ab|(?:a|b)a)|a(?:ba|ab)))|a(?:b(?:(?:ab|(?:a|b)a)b|(?:(?:a|b)a|bb)a)|a(?:(?:ba)b|(?:ba|bb)a))))$

"""

   # r42s = " r42 "
   # r31s = " r31 "
   # r11s = "(?:"+r42s+r31s+")"       

   # for i in range(2,6):
   #     r11s = r11s + "|(?:" + r42s * i + r31s * i +")"
       
   # print "R11s = ",r11s

def cleanup(rulez):
     return rulez.replace("(?:|)","|").replace('(?:a)', 'a').replace('(?:b)','b').replace('(?:a)', 'a').replace('(?:b)','b')
     # return rulez.replace("(?:|)","|")
 
def part2_original_gold_star_earning():    
   r42 = cleanup( expand_rule("42"))
   r31 = cleanup( expand_rule("31"))
   r8  = "\n#r8\n(?:\n"+r42+"\n)+\n"
   # r8  = "(("+r42+")+)"
   # r11 = r42+"(?:"+r42+r31+")"+r31
#   r11 = "(?:"+r42+r31+")"
#   r11 = "("+r42+r31+")"
#   r11 = "q"

   # r42 = "r42"
   # r31 = "R31"
 
#   for i in range(2,9):
#       r11 = r11 + "|(?:" + r42 * i + r31 * i + ")"
#      r11 = r11 + "|("   + r42 * i + r31 * i + ")"


   # r42 = "bbaab"
   # r31 = "aabba"
 

   r42 = '(%s)'% r42
   r31 = '(%s)'% r31 
   r11 = '\n#r11\n(%s)\n' % ")\n  |\n(".join("\n# n%d\n  (%s)\n  (%s)"%(i,r42*i,r31*i) for i in range(1,5))
   
 # part 2
 # 8: 42 | 42 8
 # 11: 42 31 | 42 11 31
 # 0: 8 11

# | (?: 42 31
# | (?: 42 42 31 31
# | (?: 42 42 42 31 31 31
# | (?: 42 42 42 42 31 31 31 31
# | (?: 42 42 42 42 42 31 31 31 31 31 
       

   
   z = "("+r8+")\n("+r11+")$"
#   z = r8+r11+"$"   

   #   z = cleanup(expand_rule( "0" )) # without 8 and 11
   print len(z)
   print
   if len(z) < 27000:
       print z
   import re
   myre = re.compile(z , re.VERBOSE)

   for m in messages:
       mm =  myre.match(m)
       if mm :
           # print "+\t",m
           for g in mm.groups():
               # print " \t",g
               pass
       else:
           #print "-",m
           pass
           
   print
   #    print "part 2 (12 sample) ", sum( 1 for m in messages if myre.match(m))
   print "part 2 (367) ", sum( 1 for m in messages if myre.match(m))
   # print "r42 ", r42
   # print "r31 ", r31

 
def part2():
    """prettiffied
    # part 2
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    # 0: 8 11
    
    # | (?: 42 31
    # | (?: 42 42 31 31
    # | (?: 42 42 42 31 31 31
    # | (?: 42 42 42 42 31 31 31 31
    # | (?: 42 42 42 42 42 31 31 31 31 31 
    """

    r42 = cleanup( expand_rule("42"))
    r31 = cleanup( expand_rule("31"))
    r42 = '(%s)'% r42
    r31 = '(%s)'% r31 
    r8  = "\n#r8\n(?:\n"+r42+"\n)+\n"
 

    r11 = '\n#r11\n(%s)\n' % ")\n  |\n(".join("\n# n%d\n  (%s)\n  (%s)"%(i,r42*i,r31*i) for i in range(1,5))
   
    z = "("+r8+")\n("+r11+")$"
    #   z = cleanup(expand_rule( "0" )) # without 8 and 11
    print len(z)
    print
    if len(z) < 27000:
        #print z
        print

    import re
    myre = re.compile(z , re.VERBOSE)

    for m in messages:
        mm =  myre.match(m)
        if mm :
            # print "+\t",m
            for g in mm.groups():
                # print " \t",g
                pass
        else:
            #print "-",m
            pass
           
    print
    #    print "part 2 (12 sample) ", sum( 1 for m in messages if myre.match(m))
    print "part 2 (367) ", sum( 1 for m in messages if myre.match(m))
    # print "r42 ", r42
    # print "r31 ", r31
   
part2()

# print " max(len(m) for m in messages)", max(len(m) for m in messages)
# print "".join(sorted(" r42:(?:b(?:a(?:bb|ab)|b(?:(?:a|b)(?:a|b)))|a(?:b(?:bb)|a(?:bb|a(?:a|b))))b|(?:(?:(?:aa|ab)a|(?:bb)b)b|(?:(?:(?:a|b)a|bb)a)a)a"))
# aaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbr

"""
part 2 (12)  367  GOLD STAR 

Compilation finished at Sat Dec 19 01:40:10

"""
