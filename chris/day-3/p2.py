import functools
from p1 import count_trees

slopes = [
  {'x': 1, 'y': 1},
  {'x': 3, 'y': 1},
  {'x': 5, 'y': 1},
  {'x': 7, 'y': 1},
  {'x': 1, 'y': 2},
]

with open('input.txt') as f:
  lines = f.read()

all_trees = []
for slope in slopes:
  start = (0, 0)
  all_trees.append(count_trees(lines, start, slope))
total = functools.reduce(lambda x, y: x * y, all_trees)
print(total)
