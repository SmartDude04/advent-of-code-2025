import io

def part_1(f: io.TextIOWrapper) -> int:
    grid = []
    for line in f.readlines():
        grid.append(line.strip())

    def can_access_paper(row: int, col: int) -> bool:
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

    num_can_be_accessed = 0
    for cur_row in range(len(grid)):
        for cur_col in range(len(grid[0])):
            if grid[cur_row][cur_col] == "@" and can_access_paper(cur_row, cur_col):
                num_can_be_accessed += 1

    return num_can_be_accessed

