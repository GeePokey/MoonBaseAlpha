

def password_count():
    valid_password_count = 0
    valid_password_count_part2 = 0
    with open('./input.txt') as input:
        for line in input:
          rule_and_password = line.split(':')
          print('rule_and_password',rule_and_password)
          rule = rule_and_password[0]
          print('rule', rule)
          password = rule_and_password[1]
          print('password', password)
          # deal with rule:
          min_value_pull = rule.split('-')
          min_value = min_value_pull[0]
          max_value_and_rule_letter = min_value_pull[1]
          max_value_pull = max_value_and_rule_letter.split(' ')
          max_value = max_value_pull[0]
          rule_letter = max_value_pull[1]
          
          print(min_value)
          print(max_value)
          print(rule_letter)
          # check password against rule:
          rule_letter_count = password.count(rule_letter)
          print('count', rule_letter_count)
          if int(min_value) <= rule_letter_count <= int(max_value):
              valid_password_count += 1
              print("valid password", line)
          else:
              print("invalid password", line)
          # part 2
          occurence_count = 0
          pos1 = int(min_value)
          pos2 = int(max_value)
          # note index starts at 1 but ok b/c erroneus ' ' at beginning takes 0
          if password[pos1] == rule_letter:
              occurence_count += 1
          if password[pos2] == rule_letter:
              occurence_count += 1
          if occurence_count == 1:
              valid_password_count_part2 += 1
              print('valid_pw_p2 ', line)
          else:
              print('invalid_p2 ', line)  
    print("number of valid passwords part 1: ", valid_password_count)
    print("number of valid passwords part 2: ", valid_password_count_part2)

password_count()
