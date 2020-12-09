import re


def load_input(filename):
    p = re.compile(r'\n')
    with open(filename, 'r') as f:
        return f.read().split('\n\n')


def get_unique_question_sets(input_file):
    answered_questions = [[e for e in line if e != '\n']
                           for line in input_file]
    return [list(set(question)) for question in answered_questions]


def part1(input_file):
    question_sets = get_unique_question_sets(input_file)
    return sum([len(q) for q in question_sets])


def part2(input_file):
    num_answers = 0
    question_groups = [l.split('\n') for l in input_file]
    question_sets = get_unique_question_sets(input_file)

    for i in range(len(question_sets)):
        q_set = question_sets[i]
        q_group_len = len(question_groups[i])
        group_str = ''.join(question_groups[i])
        num_answers += sum([1 for s in q_set 
                            if (len(group_str) - len(group_str.replace(s, '')) 
                            == q_group_len)])
    return num_answers


if __name__ == '__main__':
    input_file = load_input('./day6/input.txt')

    print('Part1 Solution: ', part1(input_file))
    print('Part2 Solution: ', part2(input_file))
