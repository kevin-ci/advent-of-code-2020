bags = {}
count = 0
target = "shiny gold"
found_list = []

with open("input.txt") as f:
    data = f.read().split("\n")

def process_bags(bag_name, bag_types):


    if bag_types == " no other bags":
        bags[bag_name] = {"contains": False}
        return
    else:
        bags[bag_name] = {"contains": True}
        bags[bag_name]["contents"] = []

        types = bag_types.split(",")
        for t in types:
            breakdown = t.split(" ")
            bags[bag_name]["contents"].append(breakdown[2] + " " + breakdown[3])

    return

def calculate_bags(bag_item, trail):

    if bags[bag_item]["contains"]:
        if target in bags[bag_item]["contents"]:
            return True
        else:
            for inner_bag in bags[bag_item]["contents"]:
                if inner_bag not in trail:
                    trail.append(inner_bag)
                    if calculate_bags(inner_bag, trail):
                        return True

        return False
    
    return

for line in data:
    bag = line.split("contain")
    process_bags(bag[0][:-6], bag[1][:-1])

for item in bags:
    found_bags = []
    if calculate_bags(item, found_bags):
        count += 1

print(count)
    
