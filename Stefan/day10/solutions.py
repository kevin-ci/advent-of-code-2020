from itertools import combinations
from copy import deepcopy


def load_input(filename):
    with open(filename, 'r') as f:
        return [int(num) for num in f.read().split('\n')]


def part1(input_file):
    start = 0
    results = {}
    input_file = sorted(input_file)
    while len(input_file) > 0:
        next_min = min(input_file)
        difference = next_min - start
        if difference > 3:
            break
        results[next_min] = difference
        start = next_min
        input_file = input_file[1:]
    final = {1: 0, 2: 0, 3: 1,}
    for res in results.values():
        final[res] += 1
    return final[1] * final[3], max(results.keys())


if __name__ == '__main__':
    input_file = load_input('./day10/test2.txt')
    part1_solution, max_value = part1(input_file)
    print("Soultion Part1: ", part1_solution)
    print("Soultion Part2: ", part2(input_file, max_value))