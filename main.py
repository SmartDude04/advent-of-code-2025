import importlib
import argparse

day = "01"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Advent of Code 2025",
        description="Run a solution to a 2025 Advent of Code problem.")
    parser.add_argument("-e", "--example", action='store_true', help="Whether to use the example file.")
    parser.add_argument("-p", "--part", default=1, help="Determines the part of the problem to run. Defaults to part 1.", type=int)
    args = parser.parse_args()

    if args.part < 1 or args.part > 2:
        raise ValueError("Part must be 1 or 2.")

    use_example = args.example
    part = args.part

    file_name = f"solutions.day_{day}"
    program = importlib.import_module(file_name)

    if part == 1:
        if use_example:
            with open("example.txt") as f:
                print(program.part_1(f))
        else:
            with open("input.txt") as f:
                print(program.part_1(f))
    elif part == 2:
        if use_example:
            with open("example.txt") as f:
                print(program.part_2(f))
        else:
            with open("input.txt") as f:
                print(program.part_2(f))