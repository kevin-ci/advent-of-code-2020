from itertools import permutations

with open("input.txt") as f:
    data = [int(i) for i in f.read().split("\n")]

preamble = 25

for d in range(preamble + 1, len(data)):

    numbers = data[d - (preamble + 1):d]
    
    target = data[d]

    sol = [nums for nums in permutations(numbers, 2) if sum(nums) == target]
    if not sol:
        print(f"Target is: {target}")
        
