timestamp = 1002392
# timestamp = 939

with open("input.txt") as f:
    shuttles = [int(i) for i in f.read().split(",") if i != "x"]

nearest = [timestamp % shuttle for shuttle in shuttles]

for shuttle in range(len(shuttles)):
    print(shuttles[shuttle] - nearest[shuttle])

print(shuttles)
    
        
