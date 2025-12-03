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

    return total_joltage


def part_2(f: io.TextIOWrapper) -> int:
    def highest_battery(cur: str, length: int) -> int:
        # Same greedy algorithm as part 1, but with a varying battery length (12 in this case, but could be anything)
        if length == 0:
            return 0

        # Choose this number
        max_num, max_index = -1, -1
        for i, num in enumerate(cur[:len(cur) - length + 1]):
            num = int(num)
            if num > max_num:
                max_num, max_index = num, i
        return 10**(length - 1) * max_num + highest_battery(cur[max_index+1:], length - 1)

    total_joltage = 0
    for line in f.readlines():
        joltage = highest_battery(line.replace("\n", ""), 12)
        total_joltage += joltage

    return total_joltage