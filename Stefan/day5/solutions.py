import os
import math


def load_lines(filepath):
    with open(filepath, 'r') as f:
        return [l.replace('\n', '') for l in f.readlines()]


def read_seat(filepath):
    result = []
    lines = load_lines(os.path.join(os.getcwd(), filepath))
    for line in lines:
        rows = list(line)[:7]
        cols = list(line)[-3:]
        row_num = binary_search(
            tree=rows,
            element=rows.pop(0),
            lower=0,
            upper=127)
        col_num = binary_search(
            tree=cols,
            element=cols.pop(0),
            lower=0,
            upper=7)
        result.append(row_num * 8 + col_num)
    return max(result), result


def binary_search(tree, element, lower, upper):
    result = None
    difference = math.ceil(upper / 2 if lower == 0 else (upper - lower) / 2)
    if element in ['F', 'L']:
        upper -= difference
        result = upper
    elif element in ['B', 'R']:
        lower += difference
        result = lower
    
    if not tree:
        return result
    else:
        return binary_search(tree, tree.pop(0), lower, upper)


if __name__ == '__main__':
    seat, all_seats = read_seat('day5/input.txt')
    print("Highest Seat ID: ", seat)

    missing_seats = []
    for seat in range(seat+1):
        if seat not in all_seats and seat > min(all_seats):
            missing_seats.append(seat)
    print('My Seat: ', missing_seats)
