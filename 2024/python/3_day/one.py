#!/usr/bin/env python3
from typing import Any
from advent import utils
from advent import config


def get_data(input_str: str) -> Any:
    line = input_str
    return line


def brut(line: str) -> int:
    answer = 0
    for i in range(len(line) - 5):
        if line[i:i+4] == "mul(":
            close = line.find(")", i)
            sub = line[i+4:close]
            parts = sub.split(",")
            if len(parts) != 2:
                continue
            if parts[0].isnumeric() and parts[1].isnumeric():
                answer += int(parts[0]) * int(parts[1])
    return answer


def solve(input_data) -> int:
    return brut(input_data)


if __name__ == "__main__":
    #  config.EXAMPLE_FILE = "example2"
    config.GET_DATA = get_data
    config.EXAMPLE_SOLUTION = 161
    config.SOLUTION = 188192787
    utils.test_solve(solve)
    utils.brut_solve(brut)
    utils.run(solve)
