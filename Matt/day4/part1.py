passports = {}
count = 0
valid = 0

def process_line(line):
    working = line.split(" ")
    for i in working:
        s = i.split(":")
        if count not in passports:
            passports[count] = {}
        passports[count][s[0]] = s[1]

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        if len(line) > 1:
            process_line(line)
        else:
            count += 1

valid_keys = ("byr",
              "iyr",
              "eyr",
              "hgt",
              "hcl",
              "ecl",
              "pid")

for k,v in passports.items():
    valid += 1 if all(key in v for key in valid_keys) else 0

print(valid)
