import os


def part_1(content):
    f_id = 0
    tape = []
    for pos, character in enumerate(content):
        count = int(character)
        if pos % 2 == 0:
            tape.extend([str(f_id)] * count)
            f_id += 1
        else:
            tape.extend(['.'] * count)

    i = 0
    j = len(tape) - 1
    while i < j:
        if tape[i] == '.':
            while tape[j] == '.' and i < j:
                j -= 1
            if i < j:
                tape[i], tape[j] = tape[j], '.'
        i += 1

    total = 0
    for i, character in enumerate(tape):
        if character == '.':
            break
        total += i * int(character)

    return total


def part_2(content):
    content = [line.strip() for line in content]
    tape = []

    for i in range(len(content)):
        x = int(content[i])
        if i % 2 == 0:
            tape.append((i // 2, x))
        else:
            tape.append((-1, x))

    i = len(tape) - 1
    while i > 0:
        v, s = tape[i]
        if v == -1:  # Empty space
            i -= 1
            continue
        ni = -1
        for j in range(i):
            nv, ns = tape[j]
            if nv == -1 and ns >= s:
                ni = j
                break
        if ni == -1:
            i -= 1
            continue
        _, ss = tape[ni]
        tape = tape[:ni] + [(v, s), (-1, ss - s)] + tape[ni + 1:i] + [(-1, s)] + tape[i + 1:]

    total = 0
    block = 0
    for i in tape:
        v, s = i
        if v == -1:
            block += s
            continue
        for j in range(s):
            total += block * v
            block += 1

    return total


if __name__ == '__main__':
    # _filename = os.path.join(os.getcwd(), 'test/test_09.2.txt')
    _filename = os.path.join(os.getcwd(), 'input/day_09.txt')

    with open(_filename) as f:
        _content = f.read()

    print(f'Part 1: {part_1(_content)}')
    print(f'Part 2: {part_2(_content)}')
