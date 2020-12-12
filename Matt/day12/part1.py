with open("input.txt") as f:
    data = f.read().split("\n")

x = 0
y = 0
facing = 90

for d in data:
    if d[0] == "L":
        new_direction = facing - int(d[1:])
        facing = new_direction if new_direction >= 0 else abs(abs(new_direction) - 360)
    elif d[0] == "R":
        facing = abs(facing + int(d[1:])) % 360
    else:
        x = x + int(d[1:]) if d[0] == "E" or (d[0] == "F" and facing == 90) else x
        x = x - int(d[1:]) if d[0] == "W" or (d[0] == "F" and facing == 270) else x
        y = y + int(d[1:]) if d[0] == "N" or (d[0] == "F" and facing == 0) else y
        y = y - int(d[1:]) if d[0] == "S" or (d[0] == "F" and facing == 180) else y

print(abs(x) + abs(y))
