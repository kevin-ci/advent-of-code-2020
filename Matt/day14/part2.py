from itertools import product

with open("input.txt") as f:
    data = f.read().split("\n")

memory = {}
total = 0

for d in data:
    d = d.split(" = ")
    if d[0] == "mask":
        mask = d[1]
    else:
        num = int(d[1])
        mem = format(int(d[0][4:-1]), "b")
        padding = "0" * (len(mask) - len(mem))
        mem = padding + mem
        masked_address = ""

        for n in range(len(mask)):
            masked_address += mem[n] if mask[n] == "0" else mask[n]

        c = masked_address.count("X")
        masked_address = masked_address.replace("X", "{}")

        for x in product("01", repeat=c):
            address = int(masked_address.format(*x),2)
            memory[address] = num
  
print(sum(memory.values()))
