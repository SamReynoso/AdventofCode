#!/usr/bin/env python3
from typing import Any
from advent import utils
from advent import config


def get_data(input_str: str) -> list[int]:
    input_lines = input_str.split("\n")
    input_lines.pop()
    new = []
    for line in input_lines:
        new.append([int(x) for x in line.split(" ")])
    return new


def all_up(line: list[int]) -> bool:
    for i in range(len(line) - 1):
        if line[i] >= line[i + 1]:
            return False
    return True


def all_down(line: list[int]) -> bool:
    for i in range(len(line) - 1):
        if line[i] <= line[i + 1]:
            return False
    return True


def zags(line: list[int]) -> bool:
    start = line[1] - line[0]
    if start == 0:
        return True
    elif start > 0:
        if all_up(line):
            return False
        return True
    if all_down(line):
        return False
    return True


def diff_to_big(line: list[int]) -> bool:
    limit = 3
    for i in range(1, len(line)):
        if abs(line[i] - line[i - 1]) > limit:
            return True
    return False


def brut(input_data: Any) -> int:
    answer = len(input_data)
    for line in input_data:
        if zags(line):
            answer -= 1
            continue
        if diff_to_big(line):
            answer -= 1
    return answer


def solve(input_data) -> int:
    return brut(input_data)


if __name__ == "__main__":
    #  config.EXAMPLE_FILE = "example2"
    config.GET_DATA = get_data
    config.EXAMPLE_SOLUTION = 2
    config.SOLUTION = 631
    utils.test_solve(solve)
    utils.brut_solve(brut)
    utils.run(solve)
