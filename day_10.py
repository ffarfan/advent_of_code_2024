import os


def part_1(content):
    """
    Find unique trailheads

    :param content: 2-D Map layout
    :return: Total number of unique trailheads
    """

    total = 0
    map_layout = [list([int(pos) for pos in line]) for line in content.split('\n')]
    for x, line in enumerate(map_layout):
        for y, char in enumerate(line):
            trail_tails = set()
            if char == 0:
                find_trail_tails_1(map_layout, (x, y), 0, trail_tails)

            if len(trail_tails) > 0:
                total += len(trail_tails)

    return total


def part_2(content):
    """
    Find all possible trails

    :param content: 2-D Map layout
    :return: All possible trails
    """

    map_layout = [list([int(pos) for pos in line]) for line in content.split('\n')]
    total = 0
    for x, line in enumerate(map_layout):
        for y, char in enumerate(line):
            count = 0
            if char == 0:
                count += find_trailhead_2(map_layout, (x, y), 0)

            total += count

    return total


def find_trail_tails_1(map_layout, point, current_number, trail_tails):
    x, y = point
    if map_layout[x][y] == current_number:
        if current_number == 9:
            trail_tails.add((x, y))
        for direction in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
            next_x, next_y = x + direction[0], y + direction[1]
            if 0 <= next_x < len(map_layout) and 0 <= next_y < len(map_layout[next_x]):
                find_trail_tails_1(map_layout, (next_x, next_y), current_number + 1, trail_tails)


def find_trailhead_2(map_layout, point, current_number):
    x, y = point
    total = 0
    if map_layout[x][y] == current_number:
        if current_number == 9:
            return 1
        for direction in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
            next_x, next_y = x + direction[0], y + direction[1]
            if 0 <= next_x < len(map_layout) and 0 <= next_y < len(map_layout[next_x]):
                total += find_trailhead_2(map_layout, (next_x, next_y), current_number + 1)
    return total


if __name__ == '__main__':
    # _filename = os.path.join(os.getcwd(), 'test/test_10.txt')
    _filename = os.path.join(os.getcwd(), 'input/day_10.txt')

    with open(_filename) as f:
        _content = f.read()

    print(f'Part 1: {part_1(_content)}')
    print(f'Part 2: {part_2(_content)}')
