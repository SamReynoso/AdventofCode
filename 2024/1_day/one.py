#!/usr/bin/env python3


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


def process_line(line) -> tuple[int, int]:
    assert line
    lines = line.split("   ")
    left = int(lines[0])
    right = int(lines[1])
    return left, right


def get_input_data(file_name) -> tuple[list[int], list[int]]:
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


def solve(input_data) -> int:
    left, right = input_data
    left.sort()
    right.sort()
    total = 0
    for i in range(len(left)):
        diff = abs(left[i] - right[i])
        total += diff
    solution = total
    return solution


def test_solve():
    input_data = get_input_data(EXAMPLE_FILE)
    solution = solve(input_data)
    try:
        assert solution == EXAMPLE_SOLUTION
    except AssertionError:
        print(f"Test failed {solution} != {EXAMPLE_SOLUTION}")
        exit(1)
    print("Test passed", solution)
    return solution


def main():
    input_data = get_input_data(INPUT_FILE)
    solution = solve(input_data)
    return solution


if __name__ == "__main__":
    INPUT_FILE = "input"
    EXAMPLE_FILE = "example"
    EXAMPLE_SOLUTION = 11

    test_solve()
    solution = main()
    print("Solution:", solution)
