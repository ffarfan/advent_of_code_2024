from collections import defaultdict
import os


def part_1(input_lines):
    list_1 = []
    list_2 = []
    total_distance = 0

    for line in input_lines:
        items = line.split()
        list_1.append(items[0])
        list_2.append(items[1])

    list_1 = sorted(list_1)
    list_2 = sorted(list_2)

    for i in range(len(list_1)):
        total_distance += abs(int(list_2[i]) - int(list_1[i]))

    return total_distance


def part_2(input_file):
    list_1 = []
    frequencies = defaultdict(int)
    similarity_score = 0

    for line in input_file:
        items = line.split()
        list_1.append(items[0])
        frequencies[items[1]] += 1

    for item in list_1:
        similarity_score += int(item) * frequencies[item]

    return similarity_score


if __name__ == '__main__':
    _filename = os.path.join(os.getcwd(), 'input/day_01.txt')
    # _filename = os.path.join(os.getcwd(), 'test/test_01.txt')

    with open(_filename) as f:
        lines = f.readlines()
        print(f'Part 1: {part_1(lines)}')
        print(f'Part 2: {part_2(lines)}')
