import io

def part_1(f: io.TextIOWrapper) -> int:
    total_joltage = 0

    # Classic greedy algorithm: choose the highest number that is the most to the left,
    # then choose the highest that is to the right of that one
    for line in f:

        # Choose the first number
        max_first_num, max_first_index = -1, -1
        for i, num in enumerate(line[:-2]):
            num = int(num)
            if num > max_first_num:
                max_first_num, max_first_index = num, i

        # Choose the second number
        max_second_num = -1
        for i, num in enumerate(line[max_first_index+1:-1]):
            num = int(num)
            if num > max_second_num:
                max_second_num = num

        joltage = 10 * int(max_first_num) + int(max_second_num)
        total_joltage += joltage

    print(total_joltage)