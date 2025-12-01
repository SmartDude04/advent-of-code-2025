import importlib

day = "01"
use_example = False
part = 2

if __name__ == "__main__":
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