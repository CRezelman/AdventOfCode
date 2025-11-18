"""Day 18 Solve"""
import os
import sys
import re
from dataclasses import dataclass
from collections import deque
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_lines

@dataclass
class Coordinate:
    x: int
    y: int


def bfs_shortest_path(start, goal, walls):
    MIN_X = MIN_Y = start[0]
    MAX_X = MAX_Y = goal[0]

    if start == goal:
        return [start]

    queue = deque([(start, [start])])
    visited = {start}

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        (x, y), path = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (MIN_X <= nx <= MAX_X and MIN_Y <= ny <= MAX_Y):
                continue

            nxt = (nx, ny)

            if nxt in walls or nxt in visited:
                continue

            if nxt == goal:
                return path + [nxt]

            visited.add(nxt)
            queue.append((nxt, path + [nxt]))

    return None



def day18():
    """Day 18"""
    part1 = 0
    part2 = 0
    lines = read_lines(2024, 18)

    coordinates = [Coordinate(*map(int, re.findall(r"-?\d+", line))) for line in lines]

    part1_coords = coordinates[:1024]

    start = (0, 0)
    end = (70, 70)

    walls = set((coord.x, coord.y) for coord in part1_coords)

    path_p1 = bfs_shortest_path(start, end, walls)
    part1 = len(path_p1) -1

    path_p2 = set()
    i = 1023

    while path_p2 is not None:
        walls.add((coordinates[i].x, coordinates[i].y))
        path_p2 = bfs_shortest_path(start, end, walls)
        i += 1

    part2 = (coordinates[i-1].x, coordinates[i-1].y)


    return part1, part2

print(day18())
