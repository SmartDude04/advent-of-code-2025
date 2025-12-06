import io
from functools import reduce
from operator import mul

def solve_problem(problems: list[list[int]], operations: list[str]) -> int:
    problem_sum = 0
    for problem, operation in zip(problems, operations):
        if operation == "+":
            problem_sum += sum(problem)
        elif operation == "*":
            problem_sum += reduce(mul, problem)

    return problem_sum

def part_1(f: io.TextIOWrapper) -> int:
    problems: list[list[int]] = [[int(num)] for num in f.readline().strip().split()]
    operations: list[str] = []
    for line in f.readlines():
        line = line.strip()
        line = line.split()
        if line[0].isdigit():
            for i, num in enumerate(line):
                problems[i].append(int(num))
        else:
            operations = line

    return solve_problem(problems, operations)


def part_2(f: io.TextIOWrapper) -> int:
    problems: list[list[int]] = [[]]
    operations: list[str] = []

    lines = [line.replace("\n", "") for line in f.readlines()]
    
    for col in range(len(lines[0])):
        cur_col: list[str] = []
        for row, line in enumerate(lines):
            if line[col] in ["+", "*"]:
                operations.append(line[col])
                continue
            cur_col.append(line[col])
        col_num = 0
        for dig in cur_col:
            if dig.isdigit():
                col_num = 10 * col_num + int(dig)
        if col_num == 0:
            # If we have a separator line (all spaces)
            problems.append([])
        else:
            # Add to the latest problem
            problems[-1].append(col_num)
    
    return solve_problem(problems, operations)
