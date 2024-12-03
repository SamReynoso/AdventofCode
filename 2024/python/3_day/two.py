#!/usr/bin/env python3
from typing import Any
from advent import utils
from advent import config


def get_data(input_line: str) -> Any:
    data = input_line.split("don't()")
    return data


def brut(data: Any) -> int:
    first = data.pop(0)
    acts = []
    for deact in data:
        active = deact.split("do()")
        active.pop(0)
        acts += active

    answer = 0
    acts.append(first)
    act = "".join(acts)
    mults = act.split("mul(")
    for mult in mults:
        close = mult.find(")")
        if close == -1:
            continue
        sub = mult[:close]
        parts = sub.split(",")
        if len(parts) == 2:
            if parts[0].isnumeric() and parts[1].isnumeric():
                answer += int(parts[0]) * int(parts[1])
    return answer


def solve(input_data) -> int:
    return brut(input_data)


if __name__ == "__main__":
    config.EXAMPLE_FILE = "example2"
    config.GET_DATA = get_data
    config.EXAMPLE_SOLUTION = 48
    config.SOLUTION = 113965544
    utils.test_solve(solve)
    utils.brut_solve(brut)
    utils.run(solve)
