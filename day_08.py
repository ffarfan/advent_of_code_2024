from collections import defaultdict
from itertools import combinations
import os


def part_1(content):
    anti_nodes = set()
    grid_size = len(content)
    frequencies_to_positions = get_frequencies_for_grid(content)

    for signal in frequencies_to_positions.keys():
        positions = frequencies_to_positions[signal]
        for pos1, pos2 in combinations(positions, 2):
            delta = get_slope(pos1, pos2)

            point1 = add_points(pos1, delta)
            point2 = subtract_points(pos2, delta)
            if is_within_bounds(point1, grid_size):
                anti_nodes.add(point1)
            if is_within_bounds(point2, grid_size):
                anti_nodes.add(point2)

    return len(anti_nodes)


def part_2(content):
    anti_nodes = set()
    grid_size = len(content)
    frequencies_to_positions = get_frequencies_for_grid(content)

    for signal in frequencies_to_positions.keys():
        positions = frequencies_to_positions[signal]
        for pos1, pos2 in combinations(positions, 2):
            delta = get_slope(pos1, pos2)

            for point, fn in (pos1, add_points), (pos2, subtract_points):
                anti_nodes.add(point)
                while is_within_bounds(next_point := fn(point, delta), grid_size):
                    anti_nodes.add(next_point)
                    point = next_point

    return len(anti_nodes)


def get_frequencies_for_grid(grid):
    frequencies_to_positions = defaultdict(list)

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] != '.':
                frequencies_to_positions[grid[x][y]].append((x, y))

    return frequencies_to_positions


def get_slope(a, b):
    return a[0] - b[0], a[1] - b[1]


def add_points(a, b):
    return a[0] + b[0], a[1] + b[1]


def subtract_points(a, b):
    return a[0] - b[0], a[1] - b[1]


def is_within_bounds(point, grid_size):
    return 0 <= point[0] < grid_size and 0 <= point[1] < grid_size


if __name__ == '__main__':
    # _filename = os.path.join(os.getcwd(), 'test/test_08.txt')
    _filename = os.path.join(os.getcwd(), 'input/day_08.txt')

    with open(_filename) as f:
        _content = [list(line.strip()) for line in f.readlines()]

    print(f'Part 1: {part_1(_content)}')
    print(f'Part 2: {part_2(_content)}')
