count = 0
line_str = ""

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        if line:
            line_str += line
        else:
            count += len("".join(set(line_str)))
            line_str = ""

print(count)
