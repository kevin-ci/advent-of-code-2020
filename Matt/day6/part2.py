group_count = 0
count = 0
group = {}

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        if line:
            group_count += 1
            for letter in line:
                group[letter] = 1 if letter not in group else group[letter] + 1
        else:
            for k, v in group.items():
                count = count + 1 if v == group_count else count + 0
            group_count = 0
            group.clear()

print(count)
