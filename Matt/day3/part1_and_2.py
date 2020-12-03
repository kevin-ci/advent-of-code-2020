with open("input.txt") as f:
    map = f.read().split("\n")

map_width = len(map[0])
map_height = len(map) - 1
right = 1
down = 2
left = 0 # Not used but I didn't know what was coming
up = 0   # in part 2
x = 0
y = 0
trees = 0

while True:
    try:
        trees += 1 if map[y][x] == "#" else 0
        x += right
        x -= left
        y += down
        y -= up
    except IndexError:
        if x >= map_width and y <= map_height:
            x = x - map_width
        else:
            print(trees)
            break

