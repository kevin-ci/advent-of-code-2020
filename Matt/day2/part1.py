passwords = {}
count = 0
valid = 0

with open("input.txt") as f:
    contents = f.read().split("\n")

for line in contents:
    els = line.split(" ")
    nums = els[0].split("-")
    passwords[count] = { "low": int(nums[0]),
                         "high": int(nums[1]),
                         "letter": els[1][0],
                         "password": els[2]}
    count += 1

for k,password in passwords.items():
    valid_range = range(password["low"], password["high"] + 1)
    letter_count = password["password"].count(password["letter"])
    valid += 1 if letter_count in valid_range else 0

print(valid)