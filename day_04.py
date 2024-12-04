import os
import re


def part_1(matrix):
    total = 0
    # Horizontal matches
    for row in matrix:
        line = ''.join(row)
        forward_matches = re.findall(r'XMAS', line)
        total += len(forward_matches)
        backward_matches = re.findall(r'SAMX', line)
        total += len(backward_matches)

    # Vertical matches
    num_cols = len(matrix[0])
    num_rows = len(matrix)
    for col in range(num_cols):
        line = ''.join([matrix[row][col] for row in range(num_rows)])
        forward_matches = re.findall(r'XMAS', line)
        total += len(forward_matches)
        backward_matches = re.findall(r'SAMX', line)
        total += len(backward_matches)

    # Diagonal matches (top-left to bottom-right)
    for start in range(num_rows + num_cols - 1):
        line = ''.join([matrix[row][start - row] for row in range(max(0, start - num_cols + 1), min(num_rows, start + 1))])
        forward_matches = re.findall(r'XMAS', line)
        total += len(forward_matches)
        backward_matches = re.findall(r'SAMX', line)
        total += len(backward_matches)

    # Anti-diagonal matches (top-right to bottom-left)
    for start in range(num_rows + num_cols - 1):
        line = ''.join([matrix[row][num_cols - 1 - (start - row)] for row in range(max(0, start - num_cols + 1), min(num_rows, start + 1))])
        forward_matches = re.findall(r'XMAS', line)
        total += len(forward_matches)
        backward_matches = re.findall(r'SAMX', line)
        total += len(backward_matches)

    return total


def part_2(matrix):
    total = 0

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    fragments = []

    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            fragment = [row[j:j+3] for row in matrix[i:i+3]]
            fragments.append(fragment)

    for fragment in fragments:
        diag1 = fragment[0][0] + fragment[1][1] + fragment[2][2]
        diag2 = fragment[0][2] + fragment[1][1] + fragment[2][0]

        if fragment[1][1] == 'A' and re.match(r'MAS|SAM', diag1) and re.match(r'MAS|SAM', diag2):
            total += 1

    return total


if __name__ == '__main__':
    _filename = os.path.join(os.getcwd(), 'input/day_04.txt')
    # _filename = os.path.join(os.getcwd(), 'test/test_04.txt')

    with open(_filename) as f:
        _input = [list(line.strip()) for line in f.readlines()]

        print(f'Part 1: {part_1(_input)}')
        print(f'Part 2: {part_2(_input)}')
