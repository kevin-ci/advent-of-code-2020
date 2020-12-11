from copy import deepcopy

movements = {
    'down': [1, 0],
    'up': [-1, 0],
    'left': [0, -1],
    'right': [0, 1],
    'left_up': [-1, -1],
    'right_up': [-1, 1],
    'left_down': [1, -1],
    'right_down': [1, 1],
}


def load_input(filename):
    with open(filename, 'r') as f:
        return [list(row) for row in f.read().split('\n')]


def check_fields_around(seats, x, y):
    adjacent_occupied = 0
    for movement in movements.values():
        try:
            y_hat, x_hat = y + movement[0], x + movement[1]
            if x_hat < 0 or y_hat < 0:
                continue
            if seats[y_hat][x_hat] == '#':
                adjacent_occupied += 1
        except IndexError:
            continue
    return adjacent_occupied


def part1(seats, num_seats):
    while True:
        changes, x, y = 0, 0, 0
        dupe_seats = deepcopy(seats)
        for i in range(len(seats) * len(seats[y])):
            adjacent_occupied = check_fields_around(seats, x, y)
            if seats[y][x] == 'L' and adjacent_occupied == 0:
                dupe_seats[y][x] = '#'
                changes += 1
            elif seats[y][x] == '#' and adjacent_occupied > num_seats:
                dupe_seats[y][x] = 'L'
                changes += 1

            if x == len(seats[y])-1:
                x, y = 0, y + 1
            else:
                x += 1

        if changes == 0:
            break
        seats = deepcopy(dupe_seats)
    return sum([sum([1 for item in r if item == '#']) for r in dupe_seats])


def check_fields_in_a_line(seats, x, y):
    adjacent_occupied = 0
    for movement in movements.values():
        adjacent_occupied += move(seats, x, y, movement)
    return adjacent_occupied


def move(seats, x, y, movement):
    y_hat, x_hat = y + movement[0], x + movement[1]
    try:
        if x_hat < 0 or y_hat < 0:
            return 0
        if seats[y_hat][x_hat] == '#':
            return 1
        elif seats[y_hat][x_hat] == 'L':
            return 0
        else:
            return move(seats, x_hat, y_hat, movement)
    except IndexError:
        return 0


def part2(seats, num_seats):
    while True:
        changes, x, y = 0, 0, 0
        dupe_seats = deepcopy(seats)
        for i in range(len(seats) * len(seats[y])):
            adjacent_occupied = check_fields_in_a_line(seats, x, y)
            if seats[y][x] == 'L' and adjacent_occupied == 0:
                dupe_seats[y][x] = '#'
                changes += 1
            elif seats[y][x] == '#' and adjacent_occupied > num_seats:
                dupe_seats[y][x] = 'L'
                changes += 1

            if x == len(seats[y])-1:
                x, y = 0, y + 1
            else:
                x += 1
            if len(seats) == y:
                break

        if changes == 0:
            break
        seats = deepcopy(dupe_seats)
    return sum([sum([1 for item in r if item == '#']) for r in dupe_seats])


if __name__ == '__main__':
    input_file = load_input('./day11/input.txt')
    print("Soultion Part1: ", part1(input_file, 3))
    print("Soultion Part2: ", part2(input_file, 4))
