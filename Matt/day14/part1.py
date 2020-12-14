with open("input.txt") as f:
    data = f.read().split("\n")

memory = {}
total = 0

for d in data:
    d = d.split(" = ")
    if d[0] == "mask":
        mask = d[1]
    else: 
        num = format(int(d[1]), "b")
        padding = "0" * (len(mask) - len(num))
        num = padding + num
        l = len(mask) - len(num)
        return_num = ""
        for n in range(len(num)):
            return_num += "1" if mask[n] == "1" else "0" if mask[n] == "0" else num[n]
            
        memory[d[0][3:]] = int(return_num, 2)


print(sum(memory.values()))
