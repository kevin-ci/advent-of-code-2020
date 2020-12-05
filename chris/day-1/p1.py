import itertools
import functools


def get_product(nums, r_len):
  combos = itertools.combinations(nums, r=r_len)
  result = itertools.filterfalse(lambda x: sum(x) != 2020, combos)
  return functools.reduce(lambda x, y: x*y, *list(result))


if __name__ == '__main__':
  with open('input.txt') as f:
    nums = [int(line) for line in f.readlines()]
  print(get_product(nums, 2))
