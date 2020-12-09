def load_input(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n')


def part1(input_file):
    num_valid = 0
    for line in input_file:
        split_line = ''.join(line.split(':')).split(' ')
        minimum = int(split_line[0].split('-')[0])
        maximum = int(split_line[0].split('-')[1])
        letter = split_line[1]
        password = split_line[2]
        
        remove_char = [char for char in password
                       if char != letter]
        num_valid += bool(minimum <= (len(password) - len(remove_char)) <=
                          maximum)
    return num_valid


def part2(input_file):
    num_valid = 0
    for line in input_file:
        split_line = ''.join(line.split(':')).split(' ')
        first_index = int(split_line[0].split('-')[0]) - 1
        second_index = int(split_line[0].split('-')[1]) - 1
        letter = split_line[1]
        password = split_line[2]
        first_char = password[first_index]
        second_char = password[second_index]

        num_valid += bool((first_char == letter or second_char == letter)
                           and first_char != second_char)
    return num_valid


if __name__ == '__main__':
    input_file = load_input('./day2/input.txt')
    print('Part1 Solution: ', part1(input_file))
    print('Part2 Solution: ', part2(input_file))
