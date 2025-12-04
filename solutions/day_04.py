import io

def can_access_paper(grid: list[list[str]], row: int, col: int) -> bool:
    assert grid[row][col] == "@"
    num_rolls = 0
    for pos in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        check_row, check_col = row + pos[0], col + pos[1]
        if 0 <= check_row < len(grid) and 0 <= check_col < len(grid[0]):
            # Position is able to be checked
            if grid[check_row][check_col] == "@":
                num_rolls += 1
                if num_rolls == 4:
                    return False
    return True

def remove_paper(grid: list[list[str]]) -> int:
    # We can check the whole board then remove them, but it doesn't matter if we remove them as we go
    # We will still get the same number, and it will still stop at the same spot

    num_removed = 0
    for cur_row in range(len(grid)):
        for cur_col in range(len(grid[0])):
            if grid[cur_row][cur_col] == "@" and can_access_paper(grid, cur_row, cur_col):
                # Remove the paper and increment num_removed
                grid[cur_row][cur_col] = "."
                num_removed += 1

    return num_removed


def part_1(f: io.TextIOWrapper) -> int:
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))

    num_can_be_accessed = 0
    for cur_row in range(len(grid)):
        for cur_col in range(len(grid[0])):
            if grid[cur_row][cur_col] == "@" and can_access_paper(grid, cur_row, cur_col):
                num_can_be_accessed += 1

    return num_can_be_accessed


def part_2(f: io.TextIOWrapper) -> int:
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))

    cur_num_removed = remove_paper(grid)
    total_num_removed = cur_num_removed
    while cur_num_removed != 0:
        cur_num_removed = remove_paper(grid)
        total_num_removed += cur_num_removed

    return total_num_removed