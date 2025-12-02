import io

def part_1(f: io.TextIOWrapper) -> int:
    def is_invalid_id(cur_id: str) -> bool:
        # If the ID is not an even number of digits, two halves cannot match
        if len(cur_id) % 2 != 0:
            return False

        # Confirm the first half matches the second half
        return cur_id[:len(cur_id) // 2] == cur_id[len(cur_id) // 2:]

    line = f.readline()
    id_ranges = line.split(",")
    invalid_id_sum = 0
    for id_range in id_ranges:
        low, high = id_range.split("-")
        for cur_id in range(int(low), int(high)+1):
            if is_invalid_id(str(cur_id)):
                invalid_id_sum += cur_id

    return invalid_id_sum

def part_2(f: io.TextIOWrapper) -> int:
    def is_invalid_id(cur_id: str) -> bool:
        # If the string is divisible into equal segments of a specific number, it needs to be checked
        for i in range(1, len(cur_id) // 2 + 1):
            if len(cur_id) % i == 0:
                match = True
                # Number is perfectly divisible by this number, check if all segments match
                for j in range(1, len(cur_id) // i):
                    segment_start = i * j
                    segment_end = segment_start + i
                    if cur_id[0:i] != cur_id[segment_start:segment_end]:
                        match = False
                        break

                # If we make it here, all segments are equal. Return true
                if match:
                    return True

        return False

    line = f.readline()
    id_ranges = line.split(",")
    invalid_id_sum = 0
    for id_range in id_ranges:
        low, high = id_range.split("-")
        for cur_id in range(int(low), int(high)+1):
            if is_invalid_id(str(cur_id)):
                invalid_id_sum += cur_id

    return invalid_id_sum