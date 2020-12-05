with open('input.txt') as f:
  lines = f.readlines()

valid = 0
for line in lines:
  split_line = line.split()
  positions = [int(x) - 1 for x in split_line[0].split('-')]
  valid_letter = split_line[1].replace(':', '')
  password = split_line[2]
  letter_positions = [password[position] for position in positions]
  matches = letter_positions.count(valid_letter)
  if matches == 1:
    valid += 1

print(valid)