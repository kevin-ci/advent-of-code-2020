import math

input = """1002632
23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,829,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,677,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19""".split('\n')

est_time = int(input[0])
bus_nums = [int(n) for n in input[1].split(',') if not n == 'x']

"""one"""
time = wait = bus = math.inf
for n in bus_nums:
    t = math.ceil(est_time/n) * n
    if t < time:
        time = t
        wait = time - est_time
        bus = n
print(wait * bus)

"""two"""
full_input = [i for i in input[1].split(',')]
spaces = [0]
for c, n in enumerate(bus_nums):
    if n != bus_nums[-1]:
        spaces.append(int(full_input.index(str(bus_nums[c+1])) - (full_input.index(str(n)) + 1)))

# Chinese Remainder Theorem code stolen from here: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

bus_nums_indices = [(i, int(n)) for i, n in enumerate(input[1].split(',')) if not n == 'x']
print(chinese_remainder(bus_nums, [num - i for i, num in bus_nums_indices]))