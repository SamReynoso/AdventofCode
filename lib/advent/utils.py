import time
from advent.exceptions import AdventException
from advent import config


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
        print(f"        Execution time: {self.milliseconds:.2f}ms")


def read_input_from_file(file_name) -> str:
    try:
        with open(file_name) as f:
            input_str = f.read()
    except FileNotFoundError:
        AdventException.InputNotFound(file_name)
        exit(1)
    try:
        assert input_str and len(input_str) > 0
    except AssertionError:
        AdventException.InputEmpty(file_name)
        exit(1)
    return input_str


def get_data(file_name):
    input_str = read_input_from_file(file_name)
    return config.GET_DATA(input_str)


def assert_solution(solution):
    if not config.SOLUTION:
        print("Solution unknown")
        print("    Result", solution)
        return
    try:
        assert solution == config.SOLUTION
    except AssertionError:
        AdventException.SolutionFailed(solution, config.SOLUTION)
        exit(1)


def test_solve(solver):
    input_data = get_data(config.EXAMPLE_FILE)
    solution = solver(input_data)
    try:
        assert config.EXAMPLE_SOLUTION
    except AssertionError:
        AdventException.NoExampleSolution()
        exit(1)
    try:
        assert solution == config.EXAMPLE_SOLUTION
    except AssertionError:
        AdventException.ExampleFailed(solution, config.EXAMPLE_SOLUTION)
        exit(1)
    return solution


def time_and_check(input_data, solver):
    with Timer():
        solution = solver(input_data)
    assert_solution(solution)
    return solution


def brut_solve(brut_force_function):
    input_data = get_data(config.INPUT_FILE)
    print("Brut force solution")
    time_and_check(input_data, brut_force_function)


def run(solver):
    input_data = get_data(config.INPUT_FILE)
    print("Solving for solution")
    time_and_check(input_data, solver)
