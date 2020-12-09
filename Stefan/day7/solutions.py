import re
from copy import deepcopy
from collections import OrderedDict

root_pattern = '([a-z]*\s[a-z]*) bags contain'
child_pattern = ' [0-9]* ([a-z\s]*) bag'
shiny_pattern = '%s bags contain'
amount_pattern = ' ([0-9]*) [a-z\s]* bag'


def load_input(filepath):
    with open(filepath, 'r') as f:
        return [l.replace('\n', '') for l in f.readlines()]


def search_bags(file_input):
    bags = {}
    bags_dict = {}
    for line in file_input:
        root_bag = re.findall(root_pattern, line)[0]
        bag_chilren = re.findall(child_pattern, line)
        bag_amounts = re.findall(amount_pattern, line)
        bags[root_bag] = [bag_child for bag_child in bag_chilren]
        bags_dict[root_bag] = [int(amount) for amount in bag_amounts]
    return bags, bags_dict


def down(all_bags, new_bags, total_results=[]):
    if new_bags is not None and len(new_bags) == 0:
        return total_results
    
    add_new_bags = []
    for k, v in all_bags.items():
        for val in v:
            if val in new_bags and k not in total_results:
                add_new_bags.append(k)
    
    total_results += add_new_bags
    return down(all_bags, add_new_bags, total_results)


def part1(file_input):
    num_gold_bags = 0
    search_key = 'shiny gold'
    all_bags, all_bags_dict = search_bags(input_file)
    bags_with_shiny_gold = [k for k, v in all_bags.items()
                            if search_key in v]
    all_bags_with_shiny_gold = down(all_bags, bags_with_shiny_gold,
                                    bags_with_shiny_gold)
    return len(set(all_bags_with_shiny_gold))


def search_bag_type_and_amounts(file_input, bag_str, multiplier=1):
    bags_contain = [
        line for line in file_input
        if re.findall(shiny_pattern % bag_str, line)]
    bag_amounts = re.findall(amount_pattern, bags_contain[0])
    bag_types = re.findall(child_pattern, bags_contain[0])
    results = {
        t: {
            'amount': int(a),
            'multiplier': multiplier
        } for t, a in zip(bag_types, bag_amounts)}
    return results

def count_bags_down(file_input, bags, results):
    if len(bags) == 0:
        return results

    temp_results = []
    for item in bags:
        for bag_key, d in item.items():
            multiplier = d['amount'] * d['multiplier']
            _bags = search_bag_type_and_amounts(file_input, bag_key,
                                                multiplier)
            temp_results.append(_bags)
    results += temp_results
    return count_bags_down(input_file, temp_results, results)

def part2(file_input):
    all_bags, all_bags_dict = search_bags(input_file)
    bags = search_bag_type_and_amounts(file_input, 'shiny gold')
    results = count_bags_down(file_input, [bags], [])
    total_bag_count = sum([v['amount'] * v['multiplier'] 
                           for v in bags.values()])
    total_bag_count += sum([sum([v['amount'] * v['multiplier'] 
                            for v in item.values()]) for item in results])
    return total_bag_count


if __name__ == '__main__':
    input_file = load_input('./day7/input.txt')
    
    print('Part1 Solution: ', part1(input_file))
    print('Part2 Solution: ', part2(input_file))