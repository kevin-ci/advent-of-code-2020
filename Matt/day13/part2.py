with open("input.txt") as f:
    shuttles = f.read().split(",")
    for s in range(len(shuttles)):
        shuttles[s] = int(shuttles[s]) if shuttles[s] != "x" else "x"

earliest = 0
running_total = 1

for (i, shuttle) in enumerate(shuttles):
    if shuttle == "x":
        continue

    while((earliest + i) % shuttle != 0):
        earliest += running_total
    
    running_total *= shuttle

print(f"{earliest}")

