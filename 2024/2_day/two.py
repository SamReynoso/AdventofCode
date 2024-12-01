#!/usr/bin/env python3
from typing import Any
from advent import utils
from advent import config
from copy import copy


def get_data(input_lines: list[str]) -> list[int]:
    new = []
    for line in input_lines:
        new.append([int(x) for x in line.split(" ")])
    return new


def all_increasing(line):
    for i in range(1, len(line)):
        if line[i] < line[i - 1]:
            return False
    return True


def all_decreasing(line):
    for i in range(1, len(line)):
        if line[i] > line[i - 1]:
            return False
    return True


def safe_diff(line):
    max_diff = 3
    for i in range(len(line) - 1):
        current = line[i]
        next = line[i + 1]
        if current == next:
            return False
        if abs(current - next) > max_diff:
            return False
    return True


def safe_line(line):
    if not safe_diff(line):
        return False
    if all_increasing(line):
        return True
    elif all_decreasing(line):
        return True
    return False


def safe_with_mask(line):
    for masked in range(len(line)):
        new_line = copy(line)
        new_line.pop(masked)
        if safe_line(new_line):
            return True
    return False


def brut(input_data: Any) -> int:
    total = 0
    for line in input_data:
        if safe_line(line):
            total += 1
        elif safe_with_mask(line):
            total += 1
    return total


'''


------------------------ solution ------------------------
'''


def is_a_problem(line, i):
    current = line[i]
    if i == 0:
        next = line[1]
        nextnext = line[2]
        if current == next:
            return True
        if abs(current - next) > 3:
            return True
        if current < next and next > nextnext:
            return True
        if current > next and next < nextnext:
            return True
    elif i == len(line) - 1:
        previous = line[i - 1]
        prevprev = line[i - 2]
        if current == previous:
            return True
        if abs(current - previous) > 3:
            return True
        if current < previous and previous > prevprev:
            return True
        if current > previous and previous < prevprev:
            return True
    else:
        previous = line[i - 1]
        next = line[i + 1]
        if current == next or current == previous:
            return True
        if current < next and current < previous:
            return True
        if current > next and current > previous:
            return True
        return abs(current - next) > 3 and abs(current - previous) > 3
    return False


def fast_safe_with_mask(line):
    for i in range(len(line)):
        if is_a_problem(line, i):
            mask = copy(line)
            mask.pop(i)
            if fast_safe_line(mask):
                return True
    return False


def diff_dec(line):
    for i in range(len(line) - 1):
        if line[i] <= line[i + 1] or line[i] - 3 > line[i + 1]:
            return False
    return True


def fast_safe_line(line):
    for i in range(len(line) - 1):
        if line[i] >= line[i + 1] or line[i] + 3 < line[i + 1]:
            if i == 0:
                return diff_dec(line)
            return False
    return True


def solve(input_data) -> int:
    total = 0
    for line in input_data:
        if fast_safe_line(line):
            total += 1
        elif fast_safe_with_mask(line):
            total += 1
    return total


if __name__ == "__main__":
    config.GET_DATA = get_data
    config.EXAMPLE_SOLUTION = 4
    config.SOLUTION = 665
    utils.test_solve(solve)
    utils.brut_solve(brut)
    utils.run(solve)
