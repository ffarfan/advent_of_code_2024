import os
import re


def part_1(input_lines):
    accumulator = 0
    for line in input_lines:
        matches = re.findall(r'mul\([1-9]\d*,[1-9]\d*\)', line)
        for match in matches:
            numbers = re.findall(r'[1-9]\d*', match)
            accumulator += int(numbers[0]) * int(numbers[1])

    return accumulator


def part_2(input_lines):
    # The entire file was one single line!!!!!
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)'
    matches = re.findall(pattern, input_lines)

    accumulator = 0
    flag = True
    for match in matches:
        if match == 'do()':
            flag = True
        elif match == "don't()":
            flag = False
        else:
            if flag:
                x, y = map(int, match[4:-1].split(','))
                accumulator += x * y
    return accumulator


def extract_and_multiply(corrupted_memory):
    # Regular expression to match valid mul(X,Y) instructions and control instructions
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)')

    # Initialize the enabled state
    enabled = True
    total_sum = 0

    for match in pattern.finditer(corrupted_memory):
        token = match.group(0)
        print(token)

        if token.startswith('mul'):
            if enabled:
                x, y = int(match.group(1)), int(match.group(2))
                total_sum += x * y
        elif token == 'do()':
            enabled = True
        elif token == "don't()":
            enabled = False

    print(f'Total: {total_sum}\n\n')
    return total_sum


if __name__ == '__main__':
    _filename = os.path.join(os.getcwd(), 'input/day_03.txt')
    # _filename = os.path.join(os.getcwd(), 'test/test_03_1.txt')
    # _filename = os.path.join(os.getcwd(), 'test/test_03_2.txt')

    with open(_filename) as f:
        lines = f.read()
        print(f'Part 1: {part_1(lines)}')
        print(f'Part 2: {part_2(lines)}')
