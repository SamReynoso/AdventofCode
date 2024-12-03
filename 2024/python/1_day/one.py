#!/usr/bin/env python3


from typing import Any
from advent import utils
from advent import config


def get_data(input_str: str):
    input_lines = input_str.split("\n")
    left = []
    right = []
    for line in input_lines:
        if not line:
            continue
        lines = line.split("   ")
        left.append(int(lines[0]))
        right.append(int(lines[1]))
    return left, right


def brut(input_data: Any) -> int:
    left, right = input_data
    left.sort()
    right.sort()
    total = 0
    for i in range(len(left)):
        diff = abs(left[i] - right[i])
        total += diff
    answer = total
    return answer


def solve(input_data) -> int:
    return brut(input_data)


if __name__ == "__main__":
    #  config.EXAMPLE_FILE = "example2"
    config.GET_DATA = get_data
    config.EXAMPLE_SOLUTION = 11
    config.SOLUTION = 2375403
    utils.test_solve(solve)
    utils.brut_solve(brut)
    utils.run(solve)
