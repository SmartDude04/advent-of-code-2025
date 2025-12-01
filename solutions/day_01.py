import io


def part_1(f: io.TextIOWrapper) -> int:
    password = 0
    current = 50

    for line in f:
        rot_num = int(line[1:]) * (-1 if line[0] == "L" else 1)
        current += rot_num
        if current < 0:
            current = 100 - (-current % 100)
        elif current > 100:
            current %= 100

        if current % 100 == 0:
            current = 0
            password += 1

    return password


def part_2(f: io.TextIOWrapper) -> int:
    password = 0
    current = 50

    for line in f:
        rot_num = int(line[1:]) * (-1 if line[0] == "L" else 1)
        prev = current
        current += rot_num

        if current * prev < 0:
            password += 1

        if current == 0:
            password += 1
        elif current % 100 == 0:
            password += abs(current) // 100
            current = 0
        elif current >= 100:
            password += current // 100
            current %= 100
        elif current < 0:
            password += -current // 100
            current = 100 - (-current % 100)

    return password
