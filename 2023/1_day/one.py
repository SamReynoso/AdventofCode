#!/usr/bin/env python3
from typing import Any
from advent import utils
from advent import config


def get_data(input_lines: list[str]) -> Any:
    return input_lines


def brut(input_data: Any) -> int:
    answer = 0
    for line in input_data:
        for char in line:
            if char.isnumeric():
                answer += int(char) * 10
                break
        for i in range(len(line)):
            index = len(line) - i - 1
            if line[index].isnumeric():
                answer += int(line[index])
                break

    return answer


def solve(input_data) -> int:
    return brut(input_data)


if __name__ == "__main__":
    config.GET_DATA = get_data
    config.EXAMPLE_SOLUTION = 142
    config.SOLUTION = 54951
    utils.test_solve(solve)
    utils.brut_solve(brut)
    utils.run(solve)
