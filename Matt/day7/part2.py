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
            bags[bag_name]["contents"].append((int(breakdown[1]), breakdown[2] + " " + breakdown[3]))

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


def count_bags(outer_bag):
  """
  This function adds the number of each inner bag and multiplies that count by the count returned
  by calling itself on the inner bag color. If the bag contains no other bags, do not return a count.
  """
  count = 0
  if "contents" in bags[outer_bag]:
    for num,inner_bag in bags[outer_bag]["contents"]:
      count += num
      count += num * count_bags(inner_bag)
    return count
  else:
    return 0

print(count_bags(target))
    
