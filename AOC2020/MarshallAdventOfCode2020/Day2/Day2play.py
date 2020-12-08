
def password_count(part1=0, part2=0):
    with open('./input.txt') as input:
        for line in input:
            min, max, letter, password = line.replace('-', ' ').replace(':',' ').split()
            part1 += (int(min) <= password.count(letter) <= int(max))
            part2 += ((password[int(min)-1] == letter) ^ (password[int(max)-1] == letter))
    print('part1:',part1,'part2:',part2)
    
password_count()          
