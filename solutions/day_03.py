import io

def highest_battery(cur: str, length: int) -> int:
    # Greedy algorithm; chooses the best battery at each step
    if length == 0:
        return 0

    # Choose this number
    max_num, max_index = -1, -1
    for i, num in enumerate(cur[:len(cur) - length + 1]):
        num = int(num)
        if num > max_num:
            max_num, max_index = num, i
    return 10**(length - 1) * max_num + highest_battery(cur[max_index+1:], length - 1)

def part_1(f: io.TextIOWrapper) -> int:
    total_joltage = 0
    for line in f.readlines():
        joltage = highest_battery(line.replace("\n", ""), 2)
        total_joltage += joltage

    return total_joltage


def part_2(f: io.TextIOWrapper) -> int:
    total_joltage = 0
    for line in f.readlines():
        joltage = highest_battery(line.replace("\n", ""), 12)
        total_joltage += joltage

    return total_joltage