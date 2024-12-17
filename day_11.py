from collections import Counter
import os


def part_1(content):
    stones = Counter(content)
    blinks = 25
    stones = manipulate_stones(stones, blinks)
    return sum(stones.values())


def part_2(content):
    stones = Counter(content)
    blinks = 75
    stones = manipulate_stones(stones, blinks)
    return sum(stones.values())


def manipulate_stones(stones, blinks):
    for _ in range(blinks):
        new_stones = Counter()
        for stone, qty in stones.items():
            if stone == 0:
                new_stones[1] += qty
            elif len(str(stone)) % 2 == 0:
                full = str(stone)
                left = int(full[:len(full) // 2])
                right = int(full[len(full) // 2:])
                new_stones[left] += qty
                new_stones[right] += qty
            else:
                new_stones[stone * 2024] += qty
        stones = new_stones

    return stones


def count_digits(n):
    return len(str(abs(n)))


if __name__ == '__main__':
    # _filename = os.path.join(os.getcwd(), 'test/test_11.txt')
    _filename = os.path.join(os.getcwd(), 'input/day_11.txt')

    with open(_filename) as f:
        _content = list(map(int, f.read().strip().split()))

    print(f'Part 1: {part_1(_content)}')
    print(f'Part 2: {part_2(_content)}')
