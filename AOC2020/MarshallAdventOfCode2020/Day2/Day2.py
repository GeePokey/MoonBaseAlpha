

def password_count():
    valid_password_count = 0
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

    print("number of valid passwords: ", valid_password_count)

password_count()
