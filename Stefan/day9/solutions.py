from itertools import combinations


def load_input(filename):
    with open(filename, 'r') as f:
        return [int(num) for num in f.read().split('\n')]


def part1(input_file, preamble_num):
    start, end = 0, preamble_num
    for i in range(end+1, len(input_file)):
        numbers = input_file[start:end+1]
        number_check = input_file[i]
        combos = [pair for pair in combinations(numbers, 2)
                  if sum(pair) == number_check]
        if len(combos) == 0:
            return number_check

        start, end = (start + 1), (end + 1)


def part2(input_file, expected_sum):
    start, end = 0, 2
    increments = [i for i in range(2, 30)]
    for increment in increments:
        start = 0
        end = increment
        while end < len(input_file):
            if sum(input_file[start:end]) == expected_sum:
                return min(input_file[start:end]) + max(input_file[start:end])
            start, end = (start + 1), (end + 1)


if __name__ == '__main__':
    input_file = load_input('./day9/input.txt')
    part1_solution = part1(input_file, 25)
    print("Solution Part1: ", part1_solution)
    print("Solution Part2: ", part2(input_file, part1_solution))