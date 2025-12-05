import io

def part_1(f: io.TextIOWrapper) -> int:
    def within_range(num: int) -> bool:
        for cur_range in ranges:
            if cur_range[0] <= num <= cur_range[1]:
                return True
        return False

    # I could store every possible valid ID, but it's more efficient to store each range
    ranges: list[tuple[int, int]] = []
    in_ranges = True
    num_fresh = 0
    for line in f.readlines():
        line = line.strip()
        if line == "":
            in_ranges = False
            continue

        # Switch what the loop does for the line type
        if in_ranges:
            low, high = line.split("-")
            low, high = int(low), int(high)
            ranges.append((low, high))
        else:
            line = int(line)
            if within_range(line):
                num_fresh += 1
    return num_fresh


def part_2(f: io.TextIOWrapper) -> int:
    def merge() -> None:
        merged = False
        for i, id_1 in enumerate(fresh_id_ranges):
            for j, id_2 in enumerate(fresh_id_ranges[i + 1:]):
                j += i + 1
                # Check for overlap
                if id_1[0] <= id_2[1] and id_2[0] <= id_1[1]:
                    # Merge the two
                    fresh_id_ranges[i] = (min(id_1[0], id_2[0]), max(id_1[1], id_2[1]))

                    # Remove the second ID; do it slightly more efficiently by moving it to the back them removing it
                    fresh_id_ranges[j], fresh_id_ranges[len(fresh_id_ranges) - 1] = (
                        fresh_id_ranges[len(fresh_id_ranges) - 1], fresh_id_ranges[j])
                    del fresh_id_ranges[len(fresh_id_ranges) - 1]

                    merged = True
                    break
            if merged:
                break

        if merged:
            merge()

    fresh_id_ranges: list[tuple[int, int]] = []

    # The plan is to add each valid ID range. If an ID range overlaps, merge them
    for line in f.readlines():
        line = line.strip()
        if line == "":
            break
        low, high = line.split("-")
        low, high = int(low), int(high)
        fresh_id_ranges.append((low, high))
    merge()

    valid_ids = 0
    # Count all numbers in the merged ID ranges
    for low, high in fresh_id_ranges:
        valid_ids += high - low + 1

    return valid_ids



