
from copy import deepcopy


def load_input(filepath):
    with open(filepath, 'r') as f:
        return [l.replace('\n', '') for l in f.readlines()]


def part1(input_file):
    exectued_steps = []
    terminated = True
    accumulator = 0
    instructions = [[i, step] for i, step in zip(range(len(input_file)), input_file)]
    count = 0
    c = 0
    while True:
        count += 1
        idx = instructions[c][0]
        if idx in exectued_steps:
            terminated = True
            break
        
        line = instructions[c][1]
        exectued_steps.append(idx)
        cmd = line.split(' ')[0]
        step = int(line.split(' ')[1])

        if cmd == 'nop':
            c += 1
        elif cmd == 'acc':
            accumulator += step
            c += 1
        else:
            c = c + step
    return accumulator


def part2(input_file):
    instructions = [[i, step]
                    for i, step in zip(range(len(input_file)), input_file)]
    nop_count = [i for i in instructions if 'jmp' in i[1]]

    for i, nop in enumerate(nop_count):
        exectued_steps = []
        terminated = False
        new_nop = [nop[0], nop[1].replace('jmp', 'nop')]
        new_instructions = deepcopy(instructions)
        new_instructions[nop[0]] = new_nop
        accumulator = 0
        c = 0

        while True:
            try:
                idx = new_instructions[c][0]
            except IndexError:
                terminated = False
                break

            if idx in exectued_steps:
                terminated = True
                break
            
            line = new_instructions[c][1]
            exectued_steps.append(idx)
            cmd = line.split(' ')[0]
            step = int(line.split(' ')[1])

            if cmd == 'nop':
                c += 1
                continue
            elif cmd == 'acc':
                accumulator += step
                c += 1
                continue
            else:
                c = c + step
                continue

        if not terminated:
            return accumulator

    return None


if __name__ == '__main__':
    input_file = load_input('./day8/input.txt')
    print("Solution Part1: ", part1(input_file))
    print("Solution Part2: ", part2(input_file))
