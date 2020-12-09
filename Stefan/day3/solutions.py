def load_input(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n')


def traverse(input_file, x_hat, y_hat):
    num_trees = 0
    x, y = 0, 0
    limit = len(input_file[0])
    y_limit = len(input_file)
    tree_rows = [list(tree_row) for tree_row in input_file]
    while y < y_limit:
        if x >= limit:
            x = x % limit

        if tree_rows[y][x] == '#':
            num_trees += 1
        x, y = (x + x_hat), (y + y_hat)
    return num_trees


if __name__ == '__main__':
    input_file = load_input('./day3/input.txt')
    part1 = traverse(input_file, 3, 1)
    print("Part1 Solution: ", part1)

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    num_trees = 1
    for slope in slopes:
        t = traverse(input_file, slope[0], slope[1])
        num_trees *= t
    print("Part2 Solution: ", num_trees)
