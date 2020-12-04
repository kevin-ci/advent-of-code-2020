import re

passports = {}
valid_passports = {}
valid_eyes = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
valid_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
count = 0
valid = 0

def process_line(line):
    working = line.split(" ")
    for i in working:
        s = i.split(":")
        if count not in passports:
            passports[count] = {}
        passports[count][s[0]] = s[1].strip("\n")

with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        if len(line) > 1:
            process_line(line)
        else:
            count += 1

for k,v in passports.items():
    if all(key in v for key in valid_keys):
        valid_passports[valid] = v
        valid += 1

valid = 0

for k, v in valid_passports.items():

    byr = int(v["byr"]) in range(1920, 2003)
    iyr = int(v["iyr"]) in range(2010, 2021)
    eyr = int(v["eyr"]) in range(2020, 2031)
    hgt = bool(re.match(
        "(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)", v["hgt"]))
    hcl = bool(re.match("#([a-f]?[0-9]?){6}", v["hcl"]))
    ecl = v["ecl"].lower() in valid_eyes
    pid = bool(re.match("[0-9]{9}$", v["pid"]))

    valid += (byr * iyr * eyr * hgt * hcl * ecl * pid)
    
print(valid)
