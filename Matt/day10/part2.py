with open("input.txt") as f:
    data = [int(d) for d in f.read().split("\n")]

data.sort()

counts = {i: 0 for i in data}

counts[1] = 1 # Need to initialise the first three
counts[2] = 1
counts[5] = 1

for i in range(2, len(data)):
    num = data[i]
    counts[num] += sum(counts[c] for c in range(num - 3, num) if c in counts)

print(counts[data[-1]])
