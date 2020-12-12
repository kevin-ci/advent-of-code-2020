with open("input.txt") as f:
    data = f.read().split("\n")

wx = 10
wy = 1
sx = 0
sy = 0

for d in data:
    comm = d[0]
    par = int(d[1:])
    if comm == "L":
        wx, wy = (-wy, wx) if par == 90 else (-wx, -wy) if par == 180 else (wy, -wx)
    elif comm == "R":
        wx, wy = (wy, -wx) if par == 90 else (-wx, -wy) if par == 180 else (-wy, wx)
    elif comm == "F":
        sx += wx * par
        sy += wy * par
    else:
        wx = wx + par if comm == "E" else wx
        wx = wx - par if comm == "W" else wx
        wy = wy + par if comm == "N" else wy
        wy = wy - par if comm == "S" else wy

print(abs(sx) + abs(sy))