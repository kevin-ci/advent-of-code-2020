with open('input.txt') as f:
  lines = f.readlines()

valid = 0
for line in lines:
  split_line = line.split()
  valid_range = list(range(
    int(split_line[0].split('-')[0]),
    int(split_line[0].split('-')[1]) + 1))

  valid_letter = split_line[1].replace(':', '')
  matches = split_line[2].count(valid_letter)
  if matches in valid_range:
    valid += 1

print(valid)
