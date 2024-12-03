#!/usr/bin/env python3
from typing import Any
from advent import utils
from advent import config


def get_data(input_str: str) -> Any:
    return input_str


def brut(input_data: Any) -> int:
    answer = input_data
    return answer


def solve(input_data) -> int:
    return brut(input_data)


if __name__ == "__main__":
    #  config.EXAMPLE_FILE = "example2"
    config.GET_DATA = get_data
    config.EXAMPLE_SOLUTION = None
    config.SOLUTION = None
    utils.test_solve(solve)
    utils.brut_solve(brut)
    utils.run(solve)
