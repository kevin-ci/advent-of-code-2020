def count_trees(initial_input, initial_position, slope):
  lines = initial_input.splitlines()
  trees = 0 if lines[initial_position[0]][initial_position[1]] == '.' else 1
  position = initial_position + (trees,)
  i = initial_position[1] + slope['y']

  while i < len(lines):
    linelength = len(lines[i])
    new_position = (position[0] + slope['x'], position[1] + slope['y'])
    if new_position[0] > linelength - 1:
      new_position = (position[0] + slope['x'] - linelength, position[1] + slope['y'])
    char = lines[new_position[1]][new_position[0]]
    if char == '#':
      trees += 1
    position = new_position + (char,)
    i += slope['y']
  return trees

if __name__ == '__main__':
  with open('input.txt') as f:
    lines = f.read()

  slope = {'x': 3, 'y': 1}
  start = (0, 0)
  print(count_trees(lines, start, slope))