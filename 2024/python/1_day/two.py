#!/usr/bin/env python3

from advent import utils
from advent import config

from one import get_data


def find_insert_index(val, target_list: list) -> int:
    start = 0
    end = len(target_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if target_list[mid] == val:
            return mid
        elif target_list[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return start


def get_matches_sum(val, right: list[int]):
    insert = find_insert_index(val, right)

    total = 0

    check = insert
    while check > 0:
        check -= 1
        if right[check] == val:
            total += val
        else:
            break

    while insert < len(right):
        if right[insert] == val:
            total += val
            insert += 1
        else:
            break

    return total


def brut(input_data) -> int:
    left, right = input_data
    answer = 0
    for val in left:
        for r_val in right:
            if val == r_val:
                answer += val
    return answer


def solve(input_data) -> int:
    left, right = input_data
    right.sort()
    answer = 0
    for val in left:
        answer += get_matches_sum(val, right)
    return answer


if __name__ == "__main__":
    #  config.EXAMPLE_FILE = "example2"
    config.GET_DATA = get_data
    config.EXAMPLE_SOLUTION = 31
    config.SOLUTION = 23082277
    utils.test_solve(solve)
    utils.brut_solve(brut)
    utils.run(solve)
