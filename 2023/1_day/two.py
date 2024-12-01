#!/usr/bin/env python3
from typing import Any
from advent import utils
from advent import config


def get_data(input_lines: list[str]) -> Any:
    return input_lines


def brut(input_data: Any) -> int:
    answer = 0

    words = [
            "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"
            ]
    map = {words[i]: i + 1 for i in range(len(words))}

    for line in input_data:
        values = []
        for i, char in enumerate(line):
            if char.isnumeric():
                values.append(int(char))
            else:
                for word in words:
                    if line[i:].startswith(word):
                        values.append(map[word])
                        i += len(word)
        answer += values[0] * 10 + values[-1]
    return answer


WORDS: list[str] = [
        "one", "two", "six", "four",
        "five", "nine", "three", "seven", "eight"
        ]
VALUES: list[int] = [1, 2, 6, 4, 5, 9, 3, 7, 8]
MAP: dict[str, int] = {word: VALUES[i] for i, word in enumerate(WORDS)}


def get_word(segment) -> int | None:
    words = WORDS
    if segment[0].isnumeric():
        return int(segment[0])
    else:
        if len(segment) < 3:
            return
        if len(segment) == 3:
            words = words[:3]
        if len(segment) == 4:
            words = words[:6]
        for word in words:
            if segment.startswith(word):
                return MAP[word]


def get_first_number(line: str) -> int:
    for i in range(len(line)):
        seg = line[i:]
        num = get_word(seg)
        if num:
            return num
    raise ValueError("No number found")


def get_last_number(line: str) -> int:
    for i in range(len(line)):
        index = len(line) - i - 1
        seg = line[index:]
        num = get_word(seg)
        if num:
            return num
    raise ValueError("No number found")


def solve(input_data) -> int:
    answer = 0
    for line in input_data:
        first = get_first_number(line)
        last = get_last_number(line)
        answer += first * 10 + last
    return answer


if __name__ == "__main__":
    config.EXAMPLE_FILE = "example2"
    config.GET_DATA = get_data
    config.EXAMPLE_SOLUTION = 281
    config.SOLUTION = 55218
    utils.test_solve(solve)
    utils.brut_solve(brut)
    utils.run(solve)
