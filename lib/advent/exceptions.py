
class AdventException(Exception):
    @staticmethod
    def ExampleFailed(solution, example_solution):
        print(f"Example failed {solution} != {example_solution}")

    @staticmethod
    def SolutionFailed(solution, correct_solution):
        print(f"Solution failed {solution} != {correct_solution}")

    @staticmethod
    def InputNotFound(file_name):
        print(f"Input file not found: {file_name}")

    @staticmethod
    def InputEmpty(file_name):
        print(f"Input file is empty: {file_name}")

    @staticmethod
    def NoExampleSolution():
        print("Example solution not set.")
