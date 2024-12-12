import os


def part_1(input_content):
    total = 0

    for line in input_content.split('\n'):
        expected, rest = line.strip().split(':')
        expected = int(expected)
        values = [int(x.strip()) for x in rest.strip().split()]
        if test_equation1(expected, values):
            total += expected

    return total


def part_2(input_content):
    total = 0

    for line in input_content.split('\n'):
        expected, rest = line.strip().split(':')
        expected = int(expected)
        values = [int(x.strip()) for x in rest.strip().split()]
        if test_equation2(expected, values):
            total += expected

    return total


def test_equation1(expected, values):
    if values[0] > expected:
        return False
    if len(values) == 1:
        return values[0] == expected
    if test_equation1(expected, [values[0] + values[1]] + values[2:]):
        return True
    if test_equation1(expected, [values[0] * values[1]] + values[2:]):
        return True

    return False


def test_equation2(expected, values):
    if values[0] > expected:
        return False
    if len(values) == 1:
        return values[0] == expected
    if test_equation2(expected, [values[0] + values[1]] + values[2:]):
        return True
    if test_equation2(expected, [values[0] * values[1]] + values[2:]):
        return True
    if test_equation2(expected, [int(str(values[0]) + str(values[1]))] + values[2:]):
        return True

    return False


if __name__ == '__main__':
    # _filename = os.path.join(os.getcwd(), 'test/test_07.txt')
    _filename = os.path.join(os.getcwd(), 'input/day_07.txt')

    _content = open(_filename, 'r').read()

    print(f'Part 1: {part_1(_content)}')
    print(f'Part 2: {part_2(_content)}')
