import getpass
pass_len = 8
dig_min = 3
char_min = 3
spec_min = 1
dig_count = char_count = spec_count = 0
pas = getpass.getpass(prompt='Enter a password:')
if len(pas) == pass_len:
  for char in pas:
    if char.isdigit():
      dig_count = dig_count + 1
    elif char.isalpha():
      char_count = char_count + 1
    else:
      spec_count = spec_count + 1

  if dig_count >= dig_min and char_count >= char_min and spec_count >= spec_min:
    pin = getpass.getpass(prompt='Enter your 5 Digit pin:')
    input('Press ENTER to retrieve data.....')
    print('Password:{}'.format(pas))
    print('Pin:{}'.format(pin))
  else:
    print('Validation failed')

else:
  print('Password length is not okay')

