"""Day 8 Solve"""
from itertools import combinations
from utilities.input import read_grid


def search_grid(grid: list[list]) -> dict:
    """Search a grid for a condition"""
    rows = len(grid)
    cols = len(grid[0])
    antennas = {}

    for y in range(cols):
        for x in range(rows):
            if grid[y][x] != '.':
                if grid[y][x] not in antennas:
                    antennas[grid[y][x]] = []
                antennas[grid[y][x]].append((y, x))

    return antennas

def create_antinodes(antinodes: set, node: tuple, dx: int, dy: int, rows: int, cols: int, max_nodes: int | None = None):
    """Create antinodes for a given node"""
    next_loc = (node[0] + dy, node[1] + dx)
    count = 0

    while 0 <= next_loc[0] < rows and 0 <= next_loc[1] < cols:
        antinodes.add(next_loc)
        count += 1
        if max_nodes and count >= max_nodes:
            break
        next_loc = (next_loc[0] + dy, next_loc[1] + dx)


def day8():
    """Day 8"""
    part1 = 0
    part2 = 0
    grid = read_grid(2024, 8).grid
    rows = len(grid)
    cols = len(grid[0])
    antennas = search_grid(grid)
    antinodes_p1 = set()
    antinodes_p2 = set()

    for key, values in antennas.items():
        for value in values:
            antinodes_p2.add(value)

        for pair in list(combinations(values, 2)):
            node1 = pair[0]
            node2 = pair[1]

            dx1 = node2[1] - node1[1]
            dy1 = node2[0] - node1[0]

            dx2 = node1[1] - node2[1]
            dy2 = node1[0] - node2[0]

            create_antinodes(antinodes_p1, node2, dx1, dy1, rows, cols, 1)
            create_antinodes(antinodes_p1, node1, dx2, dy2, rows, cols, 1)
            create_antinodes(antinodes_p2, node2, dx1, dy1, rows, cols)
            create_antinodes(antinodes_p2, node1, dx2, dy2, rows, cols)

    part1 = len(antinodes_p1)
    part2 = len(antinodes_p2)

    return part1, part2

print(day8())
