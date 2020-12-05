bin_data = []

with open("input.txt") as f:
    data = f.read().split("\n")

for line in data:
    bin_string = ""
    for c in line:
        bin_string += "0" if c == "F" or c == "L" else "1"
    bin_data.append(int(bin_string,2))

bin_data.sort()

list2 = [b for i, b in enumerate(bin_data) if i < len(bin_data) - 2 and bin_data[i + 1] == b + 2]
print(f"Your seat is: {list2[0] + 1}")
