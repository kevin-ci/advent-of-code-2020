import re

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
SPECIFICATIONS = {
    'byr': {
        'min': 1920,
        'max': 2002
    }, 
    'iyr': {
        'min': 2010,
        'max': 2020
    }, 
    'eyr': {
        'min': 2020,
        'max': 2030
    }, 
    'hgt': {
        'identifiers': [
            'in', 'cm',
        ],
        'cm': {
            'min': 150,
            'max': 193
        },
        'in': {
            'min': 59,
            'max': 76
        }
    }, 
    'hcl': {
        'identifiers': ['#'],
        'regex': r'^[#]([0-9]|[a-f]).*$'
    }, 
    'ecl': [
        'amb','blu', 'brn', 'gry', 'grn', 'hzl', 'oth',
    ], 
    'pid': {
        'length': 9,
        'type': int
    }
}


def load_input(filename):
    p = re.compile(r'\n')
    with open(filename, 'r') as f:
        raw_input_file = f.read().split('\n\n')
    return [p.sub(' ', line) for line in raw_input_file]


def get_passport_attributes(line):
    return {attrs.split(':')[0]: attrs.split(':')[1]
            for attrs in line.split(' ')}


def has_required_fields(line):
    assport_attributes = get_passport_attributes(line)
    return bool(all([True if field in assport_attributes else False 
                     for field in REQUIRED_FIELDS]))


def part1(input_file):
    num_correct = 0
    for line in input_file:
        num_correct += has_required_fields(line)
    return num_correct


def part2(input_file):
    num_correct = 0
    for line in lines:
        invalid = 0
        invalid += not(has_required_fields(line))
        if invalid:
            continue

        for k, v in get_passport_attributes(line).items():
            if k in ['byr', 'iyr', 'eyr']:
                _range = SPECIFICATIONS[k]
                invalid += not(_range['min'] <= int(v.replace('cm', '').replace('in', '')) <= _range['max'])  # noqa: E501
            elif k == 'hgt':
                identifier = 'cm' if 'cm' in v else 'in'
                _range = SPECIFICATIONS[k][identifier]
                invalid += not(_range['min'] <= int(v.replace('cm', '').replace('in', '')) <= _range['max'])   # noqa: E501
            elif k == 'hcl':
                r = SPECIFICATIONS[k]['regex']
                invalid += not((True if bool(re.match(r, v)) and len(v) == 7
                         else False))
            elif k == 'ecl':
                invalid += not(True if v in SPECIFICATIONS[k] else False)
            elif k == 'pid':
                invalid += not(
                    True if len(str(v)) == 9 and isinstance(int(v), int)
                    else False)            
            if invalid:
                continue
        if not invalid:
            num_correct += 1

    return num_correct


if __name__ == '__main__':
    input_file = lines = load_input('./day4/input.txt')

    print('Part1 Solution: ', part1(input_file))
    print('Part2 Solution: ', part2(input_file))
