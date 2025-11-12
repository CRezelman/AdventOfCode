"""Day 12 Solve"""
from dataclasses import dataclass
from itertools import product
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_grid

@dataclass
class Group:
    """Group"""
    letter: str
    area: int
    perimeter: int
    sides: int = 0


def find_groups(grid):
    """Find like-wise groups"""
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def is_valid(x, y, char):
        return 0 <= x < rows and 0 <= y < cols and not visited[x][y] and grid[x][y] == char

    def dfs(x, y):
        stack = [(x, y)]
        area = 0
        perimeter = 0
        visited[x][y] = True
        cells = set()
        while stack:
            cx, cy = stack.pop()
            area += 1
            local_perimeter = 0
            cells.add((cx, cy))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny, grid[cx][cy]):
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                else:
                    if not (0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == grid[cx][cy]):
                        local_perimeter += 1

            perimeter += local_perimeter

        return area, perimeter, cells

    groups: list[Group] = []

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                area, perimeter, cells = dfs(i, j)
                groups.append(Group(grid[i][j], area, perimeter, count_corners(cells)))

    return groups


def count_corners(cells: set[tuple[int, int]]) -> int:
    corners = 0

    for cell in cells:
        row, col = cell

        for row_offset, col_offset in product([1, -1], repeat=2):
            row_neighbor = (row + row_offset, col)
            col_neighbor = (row, col + col_offset)
            diagonal_neighbor = (row + row_offset, col + col_offset)

            # External corner
            if row_neighbor not in cells and col_neighbor not in cells:
                corners += 1

            # Internal corner
            if (
                row_neighbor in cells
                and col_neighbor in cells
                and diagonal_neighbor not in cells
            ):
                corners += 1

    return corners

def day12():
    """Day 12"""
    part1 = 0
    part2 = 0
    grid = read_grid(2024, 12, False)

    result = find_groups(grid)
    for group in result:
        part1 += group.area * group.perimeter
        part2 += group.area * group.sides

    return part1, part2

print(day12())
