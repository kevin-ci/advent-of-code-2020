from p1 import get_product


with open('input.txt') as f:
  nums = [int(line) for line in f.readlines()]

print(get_product(nums, 3))
