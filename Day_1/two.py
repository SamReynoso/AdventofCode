#!/usr/bin/env python3

import time

EXAMPLE_FILE = "example"
INPUT_FILE = "input"
EXAMPLE_SOLUTION = None
SOLUTION = None


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.interval = self.end - self.start
        self.milliseconds = self.interval * 1000
        self.result()

    def __str__(self):
        return str(self.interval)

    def result(self):
        print(f"Execution time: {self.milliseconds:.2f}ms")


def read_input_from_file(file_name):
    try:
        with open(file_name) as f:
            input_lines = f.read().split("\n")
        assert len(input_lines) > 0
        return input_lines
    except FileNotFoundError:
        print("File not found")
        exit(1)
    except AssertionError:
        print("Empty file")
        exit(1)


def assert_solution(solution):
    if not SOLUTION:
        print("Solution unknown")
        print("Result", solution)
        return
    try:
        assert solution == SOLUTION
    except AssertionError:
        print(f"Solution failed '{solution}' != '{SOLUTION}'")
        exit(1)
    print("Solution passed", solution)


def test_solve(get_input, solver):
    input_data = get_input(EXAMPLE_FILE)
    solution = solver(input_data)
    try:
        assert solution == EXAMPLE_SOLUTION
    except AssertionError:
        print(f"Example failed {solution} != {EXAMPLE_SOLUTION}")
        exit(1)
    return solution


def time_and_check(input_data, solver):
    with Timer():
        solution = solver(input_data)
    assert_solution(solution)
    return solution


def brut_solve(get_data, brut_force_function):
    input_data = get_data(INPUT_FILE)
    print("Brut force solution")
    time_and_check(input_data, brut_force_function)


def run(get_input, solver):
    input_data = get_input(INPUT_FILE)
    print("Solving for solution")
    time_and_check(input_data, solver)


'''


-------------------------------- START OF SOLUTION ----------------------------


'''


def get_input_data(file_name):
    input_lines = read_input_from_file(file_name)
    left = []
    right = []
    for line in input_lines:
        if not line:
            continue
        lines = line.split("   ")
        left.append(int(lines[0]))
        right.append(int(lines[1]))
    return left, right


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
    EXAMPLE_SOLUTION = 31
    SOLUTION = 23082277
    test_solve(get_input_data, solve)
    brut_solve(get_input_data, brut)
    run(get_input_data, solve)
