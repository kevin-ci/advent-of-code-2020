passwords = {}
count = 0
valid = 0

with open("input.txt") as f:
    contents = f.read().split("\n")

for line in contents:
    els = line.split(" ")
    nums = els[0].split("-")
    passwords[count] = { "first": int(nums[0]) - 1,
                         "second": int(nums[1]) - 1,
                         "letter": els[1][0],
                         "password": els[2]}
    count += 1

# Ugh. Janky horrid code.

for k,password in passwords.items():
    if password["password"][password["first"]] == password["letter"] and \
       password["password"][password["second"]] != password["letter"]:
        valid += 1
    elif password["password"][password["first"]] != password["letter"] and \
         password["password"][password["second"]] == password["letter"]:
        valid += 1

print(valid)