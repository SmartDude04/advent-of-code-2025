import io
from typing import cast

def part_1(f: io.TextIOWrapper) -> int:
    coords: list[tuple[int, int]] = cast(list[tuple[int, int]], [tuple(map(int, line.strip().split(","))) for line in f.readlines()])
    largest_area = 0
    for i, coord1 in enumerate(coords):
        for coord2 in coords[i + 1:]:
            cur_area = abs(coord1[1] - coord2[1] + 1) * abs(coord1[0] - coord2[0] + 1)
            largest_area = max(largest_area, cur_area)
    return largest_area