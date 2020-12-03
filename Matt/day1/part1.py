data = []

with open("input.txt") as f:
    contents = f.read().split("\n")

for c in range(len(contents)):
    data.append(int(contents[c]))


for num in data:
    target = 2020 - num
    if target in data:
        print(target, num, target * num)
        break
