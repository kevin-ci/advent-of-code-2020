from itertools import permutations

with open("input.txt") as f:
    data = f.read().split("\n")

for d in range(len(data)):
    data[d] = int(data[d])

for d in range(26, len(data)):

    numbers = data[d - 26 : d]
    
    target = data[d]

    sol = [nums for nums in permutations(numbers, 2) if sum(nums) == target]
    if not sol:
        print(f"Target is: {target}")
        
