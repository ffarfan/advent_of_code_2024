from itertools import cycle, takewhile, chain
import os
import time

OBSTACLE = '#'
OPEN = '.'
UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'


def part_1(input_content):
    map_layout = [list(line) for line in input_content.split('\n')]
    row, col = find_coordinates(map_layout, UP)
    direction = UP
    visited = set()

    while True:
        visited.add((row, col))
        next_row, next_col = move_to_next(row, col, direction)
        if is_out_of_bounds(next_row, next_col, map_layout):
            break
        elif map_layout[next_row][next_col] == OBSTACLE:
            direction = turn_right(direction)
            next_row, next_col = move_to_next(row, col, direction)
        row, col = next_row, next_col

    return len(visited)


def part_2(input_content):
    map_layout = [list(line) for line in input_content.split('\n')]
    map_size = (len(input_content.split("\n")), len(input_content.split('\n')[0]))
    start_pos = find_coordinates(map_layout, UP)
    blockers = list(chain(*filter(lambda a: len(a) > 0, [list(
        filter(lambda i: i is not False, [(col_idx, row_idx) if col == '#' else False for col_idx, col in enumerate(row)]))
                                                         for row_idx, row in enumerate(input_content.split("\n"))])))
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    move = lambda start, direction: (
        (x, y) for x, y in takewhile(
            lambda p: -1 <= p[0] <= map_size[0] and -1 <= p[1] <= map_size[1] and (p[0], p[1]) not in blockers,
            ([start[0] + direction[0] * i, start[1] + direction[1] * i]
             for i in takewhile(
                lambda i: -1 <= start[0] + direction[0] * i <= map_size[0] and -1 <= start[1] + direction[1] * i <=
                    map_size[1] and [start[0] + direction[0] * i, start[1] + direction[1] * i] not in blockers,
                range(max(map_size[0], map_size[1]) + 1)))
        )
    )

    p_count = 0
    for y in range(map_size[1]):
        for x in range(map_size[0]):
            if (x, y) in blockers:
                continue
            if x == start_pos[0] and y == start_pos[1]:
                continue

            blockers.append((x, y))
            start_time = time.time()

            c_pos = [start_pos]
            pdir = directions[0]
            test = [c_pos := list(move(c_pos[-1], pdir := direction)) for direction in takewhile(
                lambda p: time.time() - start_time < 1 and -1 <= c_pos[-1][0] + pdir[0] <= map_size[0] and -1 <=
                    c_pos[-1][1] + pdir[1] <= map_size[1], cycle(directions))]
            if time.time() - start_time > 0.5:
                p_count += 1
            blockers.remove((x, y))

    return p_count


def find_coordinates(map_layout, target_char):
    for row, line in enumerate(map_layout):
        for col, char in enumerate(line):
            if char == target_char:
                return row, col
    return None


def move_to_next(row, col, direction):
    direction_map = {
        UP: (-1, 0),
        DOWN: (1, 0),
        LEFT: (0, -1),
        RIGHT: (0, 1)
    }
    if direction in direction_map:
        delta_row, delta_col = direction_map[direction]
        return row + delta_row, col + delta_col
    return None


def is_out_of_bounds(row, col, map_layout):
    return row < 0 or row >= len(map_layout) or col < 0 or col >= len(map_layout[0])


def turn_right(direction):
    right_turn_map = {
        UP: RIGHT,
        RIGHT: DOWN,
        DOWN: LEFT,
        LEFT: UP
    }
    return right_turn_map[direction]


if __name__ == '__main__':
    # _filename = os.path.join(os.getcwd(), 'test/test_06.txt')
    _filename = os.path.join(os.getcwd(), 'input/day_06.txt')

    _content = open(_filename, 'r').read()

    print(f'Part 1: {part_1(_content)}')
    print(f'Part 2: {part_2(_content)}')
