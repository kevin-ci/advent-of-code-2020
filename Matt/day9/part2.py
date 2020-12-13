with open("input.txt") as f:
    data = [int(i) for i in f.read().split("\n")]

target = 144381670

for d in range(len(data)):
    data_range = []
    running_total = target
    for n in range(d, len(data)):
        running_total += data[n]
        data_range.append(data[n])
        if running_total == 0 and len(data_range) > 1:
            data_range.sort()
            print(f"Sum is: {data_range[0] + data_range[-1]}")
            break
