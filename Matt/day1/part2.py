data = []

with open("input.txt") as f:
    contents = f.read().split("\n")

for c in range(len(contents)):
    data.append(int(contents[c]))

while data:
    num3 = data.pop(0)
    for num in data:
        target = 2020 - num - num3
        if target in data:
            print(target, num, target * num * num3)
            break
