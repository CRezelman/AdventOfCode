"""Day 20 Solve"""
import sys
import os
from collections import deque

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_grid
from utilities.grid import find_in_grid


def bfs_distance_map(grid, start):
    """Distance from start to every reachable '.' tile."""
    h, w = len(grid), len(grid[0])
    dist = [[None]*w for _ in range(h)]
    q = deque([start])
    dist[start[0]][start[1]] = 0

    while q:
        y, x = q.popleft()

        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = y+dy, x+dx
            if 0 <= ny < h and 0 <= nx < w:
                if grid[ny][nx] == '.' and dist[ny][nx] is None:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))

    return dist


def count_cheats(dist_start, dist_end, max_cheat_radius, min_saving):
    """
    Counts how many cheats save at least min_saving steps.

    A cheat is:
        start → p1 → (cheat zone) → p2 → end
    where:
        Manhattan(p1, p2) <= max_cheat_radius
        p1 and p2 are path tiles ('.')
    """
    h, w = len(dist_start), len(dist_start[0])
    original_steps = dist_start[end_y][end_x]
    count = 0

    # Iterate over every reachable path tile p1
    for y1 in range(h):
        for x1 in range(w):
            d1 = dist_start[y1][x1]
            if d1 is None:
                continue

            # Expand a diamond (Manhattan distance ball)
            for dy in range(-max_cheat_radius, max_cheat_radius + 1):
                remaining = max_cheat_radius - abs(dy)

                for dx in range(-remaining, remaining + 1):
                    y2 = y1 + dy
                    x2 = x1 + dx

                    if not (0 <= y2 < h and 0 <= x2 < w):
                        continue

                    d2 = dist_end[y2][x2]
                    if d2 is None:
                        continue  # must land back on a valid '.' path

                    cheat_distance = abs(dy) + abs(dx)

                    new_len = d1 + cheat_distance + d2
                    saving = original_steps - new_len

                    if saving >= min_saving:
                        count += 1

    return count


def day20():
    """Day 20"""
    grid = read_grid(2024, 20)

    start = find_in_grid(grid, 'S')
    end = find_in_grid(grid, 'E')

    grid[start[0]][start[1]] = '.'
    grid[end[0]][end[1]] = '.'

    dist_start = bfs_distance_map(grid, start)
    dist_end = bfs_distance_map(grid, end)

    global end_y, end_x
    end_y, end_x = end

    part1 = count_cheats(dist_start, dist_end, max_cheat_radius=2,min_saving=100)
    part2 = count_cheats(dist_start, dist_end, max_cheat_radius=20, min_saving=100)

    return part1, part2


print(day20())
