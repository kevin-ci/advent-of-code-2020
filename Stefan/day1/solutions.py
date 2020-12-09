from itertools import combinations


def part1(numbers):
    combos = [pair for pair in combinations(numbers, 2)
              if sum(pair) == 2020]
    return combos[0][0] * combos[0][1]


def part2(numbers):
    combined_sum = 2020
    combos = [pair for pair in combinations(numbers, 3)
              if sum(pair) == combined_sum]
    return combos[0][0] * combos[0][1] *combos[0][2]


if __name__ == '__main__':
    with open('./day1/input.txt', 'r') as f:
        numbers = [int(n) for n in f.read().split('\n')]

    print('Part1 Solution: ', part1(numbers))
    print('Part2 Solution: ', part2(numbers))
