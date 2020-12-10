from itertools import tee

count1 = 1
count3 = 1

with open("input.txt") as f:
    data = [int(d) for d in f.read().split("\n")]

data.sort()

def differences():
    i, c = tee(data)
    next(c)
    for x, y in zip(i, c):
        yield y - x

for i in differences():
    if i == 1:
        count1 += 1
    else:
        count3 += 1

print(count1 * count3)