from collections import defaultdict
import math
import os


def part_1(rules, page_sequences):
    total = 0
    ordering_rules_map = build_ordering_rules_map(rules)
    incorrect_pages = []

    for page_sequence in page_sequences:
        pages = page_sequence.split(',')
        is_correct = True
        for i, first in enumerate(pages[:-1]):
            if first not in ordering_rules_map or not all(fp in ordering_rules_map[first] for fp in pages[i + 1:]):
                is_correct = False
                incorrect_pages.append(page_sequence)
                break
        if is_correct:
            total += int(pages[math.ceil(len(pages) / 2 - 1)])

    return total, incorrect_pages


def part_2(rules, incorrect_sequences):
    total = 0
    ordering_rules_map = build_ordering_rules_map(rules)

    for incorrect_sequence in incorrect_sequences:
        pages = incorrect_sequence.split(',')
        overlap_map = {
            page: len(set(ordering_rules_map.get(page, [])) & set(pages)) for page in pages
        }

        corrected_sequence = sorted(overlap_map, key=overlap_map.get, reverse=True)
        total += int(corrected_sequence[math.ceil(len(corrected_sequence) / 2 - 1)])

    return total


def build_ordering_rules_map(rules):
    ordering_rules_map = defaultdict(list)
    for rule in rules:
        k, v = rule.split('|')
        ordering_rules_map[k].append(v)
    return ordering_rules_map


if __name__ == '__main__':
    # _filename = os.path.join(os.getcwd(), 'test/test_05.txt')
    _filename = os.path.join(os.getcwd(), 'input/day_05.txt')

    with open(_filename) as f:
        content = f.read().split('\n\n')

        _rules = content[0].strip().split('\n')
        _update_pages = content[1].strip().split('\n')

    total1, _incorrect_pages = part_1(_rules, _update_pages)
    print(f'Part 1: {total1}')

    total2 = part_2(_rules, _incorrect_pages)
    print(f'Part 2: {total2}')
