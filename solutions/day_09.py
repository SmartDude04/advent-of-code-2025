import io
from typing import cast
from collections import deque

def part_1(f: io.TextIOWrapper) -> int:
    coords: list[tuple[int, int]] = cast(list[tuple[int, int]], [tuple(map(int, line.strip().split(","))) for line in f.readlines()])
    largest_area = 0
    for i, coord1 in enumerate(coords):
        for coord2 in coords[i + 1:]:
            cur_area = abs(coord1[1] - coord2[1] + 1) * abs(coord1[0] - coord2[0] + 1)
            largest_area = max(largest_area, cur_area)
    return largest_area


def add_to_tiles(coord1: tuple[int, int], coord2: tuple[int, int], tiles: set[tuple[int, int]], coords: tuple[list[int], list[int]]) -> None:
    if coord1[1] == coord2[1]:
        # Coords go across rows
        if coord1[0] < coord2[0]:
            # Coords go top -> bottom
            for i in range(coord1[0], coord2[0] + 1):
                if i in coords[0]:
                    tiles.add((i, coord1[1]))
        else:
            # Coords go bottom -> up
            for i in range(coord2[0], coord1[0] + 1):
                if i in coords[0]:
                    tiles.add((i, coord1[1]))
    else:
        # Coords go across cols
        if coord1[1] < coord2[1]:
            # Coords go left -> right
            for i in range(coord1[1], coord2[1] + 1):
                if i in coords[1]:
                    tiles.add((coord1[0], i))
        else:
            # Coords go right -> left
            for i in range(coord2[1], coord1[1] + 1):
                if i in coords[1]:
                    tiles.add((coord1[0], i))


def fill_tiles(grid: list[list[bool]]) -> None:
    # floodfill return a set of coordinates floodfilled *unless* it hits the edge of the grid, in which case it returns
    # an empty set. This is to show when the floodfill is inside the shape or not
    def floodfill(start_coord: tuple[int, int]) -> set[tuple[int, int]]:
        if grid[start_coord[0]][start_coord[1]] == True:
            return set()
        coords: set[tuple[int, int]] = set()
        queue: deque[tuple[int, int]] = deque()
        queue.append(start_coord)
        coords.add(start_coord)
        while len(queue) != 0:
            cur: tuple[int, int] = queue.popleft()
            for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if not (0 <= cur[0] + d[0] < len(grid) and 0 <= cur[1] + d[1] < len(grid)):
                    return set()
                if (cur[0] + d[0], cur[1] + d[1]) not in coords and grid[cur[0] + d[0]][cur[1] + d[1]] == False:
                    queue.append((cur[0] + d[0], cur[1] + d[1]))
                    coords.add((cur[0] + d[0], cur[1] + d[1]))
        return coords
        
    for row_i, row in enumerate(grid):
        for col_i, col in enumerate(row):
            cur_floodfill = floodfill((row_i, col_i))
            if len(cur_floodfill) != 0:
                # Inside the shape found, fill all points
                for coord in cur_floodfill:
                    grid[coord[0]][coord[1]] = True
                return


def valid_rect(grid: list[list[bool]], coord1: tuple[int, int], coord2: tuple[int, int]) -> bool:
    # Go along the edge of the rectangle and make sure all points are tiles
    (row1, col1) = coord1
    (row2, col2) = coord2
    if row1 > row2:
        row1, row2 = row2, row1
    if col1 > col2:
        col1, col2 = col2, col1
    

    # Top + bottom edges
    for i in range(col1, col2 + 1):
        if grid[row1][i] == False or grid[row2][i] == False:
            return False
    # Left + right edges
    for i in range(row1, row2 + 1):
        if grid[i][col1] == False or grid[i][col2] == False:
            return False
    return True
    


def part_2(f: io.TextIOWrapper) -> int:
    red_tiles: list[tuple[int, int]] = cast(list[tuple[int, int]], [tuple(map(int, reversed(line.strip().split(",")))) for line in f.readlines()])
    
    # The goal here is to make tiles a "compressed" version of the original grid. We do not need to consider rows
    # or columns without green tiles on them, greatly reducing the number of tiles needed to check
    row_coords: list[int] = sorted(list(set([coord[0] for coord in red_tiles])))
    row_dict: dict[int, int] = {v:i for i, v in enumerate(row_coords)}
    col_coords: list[int] = sorted(list(set([coord[1] for coord in red_tiles])))
    col_dict: dict[int, int] = {v:i for i, v in enumerate(col_coords)}
    

    # Make the grid that only has the coordinates in row_coords and col_coords    
    grid: list[list[bool]] = [[False for _ in range(len(col_coords))] for _ in range(len(row_coords))]
    
    # Change the row coords to be in the new coordinate system
    compressed_tiles: list[tuple[int, int]] = []
    for tile in red_tiles:
        compressed_tiles.append((row_dict[tile[0]], col_dict[tile[1]]))
    
    for coord1, coord2 in zip(compressed_tiles, [*compressed_tiles[1:], compressed_tiles[0]]):
        if coord1[1] == coord2[1]:
        # Coords go across rows
            if coord1[0] < coord2[0]:
                # Coords go top -> bottom
                for i in range(coord1[0], coord2[0] + 1):
                    grid[i][coord1[1]] = True
            else:
                # Coords go bottom -> up
                for i in range(coord2[0], coord1[0] + 1):
                    grid[i][coord1[1]] = True
        else:
            # Coords go across cols
            if coord1[1] < coord2[1]:
                # Coords go left -> right
                for i in range(coord1[1], coord2[1] + 1):
                    grid[coord1[0]][i] = True
            else:
                # Coords go right -> left
                for i in range(coord2[1], coord1[1] + 1):
                    grid[coord1[0]][i] = True
    
    # Grid is now compressed, find a point inside it and fill it in
    fill_tiles(grid)
    
    # Find the max area of a valid rectangl;e
    max_area = 0
    for i, coord1 in enumerate(compressed_tiles):
        for coord2 in compressed_tiles[i + 1:]:
            if valid_rect(grid, coord1, coord2):
                # Get its actual size
                area = (abs(row_coords[coord2[0]] - row_coords[coord1[0]]) + 1) * (abs(col_coords[coord2[1]] - col_coords[coord1[1]]) + 1)
                if area > max_area:
                    max_area = area
    
    return max_area