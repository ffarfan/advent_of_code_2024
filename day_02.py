import os


def part_1(input_lines):
    safe_reports = 0

    for line in input_lines:
        levels = line.split()
        if is_safe_1(levels):
            safe_reports += 1

    return safe_reports


def is_safe_1(levels):
    increasing = None

    for i in range(len(levels) - 1):
        left = int(levels[i])
        right = int(levels[i + 1])
        new_increasing = (left < right)

        if left == right:
            return False  # Neither increasing nor decreasing
        if increasing is not None and (new_increasing != increasing):  # Changed direction
            return False

        if abs(left - right) > 3:  # Too big a jump
            return False

        increasing = new_increasing

    return True


def part_2(input_lines):
    safe_reports = 0

    for line in input_lines:
        levels = line.split()
        if is_safe_2(levels):
            safe_reports += 1

    return safe_reports


def is_safe_2(levels):
    sub_levels = [levels[:i] + levels[i + 1:] for i in range(len(levels))]
    for sub_level in sub_levels:
        if is_safe_1(sub_level):
            return True

    return False


if __name__ == '__main__':
    _filename = os.path.join(os.getcwd(), 'input/day_02.txt')
    # _filename = os.path.join(os.getcwd(), 'test/test_02.txt')

    with open(_filename) as f:
        lines = f.readlines()
        print(f'Part 1: {part_1(lines)}')
        print(f'Part 2: {part_2(lines)}')
