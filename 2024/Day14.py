"""Day 14 Solve"""
import os
import sys
from dataclasses import dataclass
from itertools import chain
from math import prod

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_lines


@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int

    def move(self, steps: int, max_x: int, max_y: int) -> None:
        """Move robot position modulo the grid size."""
        self.px = (self.px + self.vx * steps) % (max_x + 1)
        self.py = (self.py + self.vy * steps) % (max_y + 1)


def simulate(robots: list[Robot], seconds: int, max_x: int, max_y: int) -> None:
    """Advance all robots by N seconds."""
    for r in robots:
        r.move(seconds, max_x, max_y)


def render_grid(robots: list[Robot], max_x: int, max_y: int) -> str:
    """Render the current grid state (for visual confirmation)."""
    grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for r in robots:
        grid[r.py][r.px] = '#'
    return '\n'.join(''.join(row) for row in grid)


def day14():
    """Day 14"""
    lines = read_lines(2024, 14, False)

    robots: list[Robot] = []
    for line in lines:
        p, v = line.split(" v=")
        px, py = map(int, p[2:].split(","))
        vx, vy = map(int, v.split(","))
        robots.append(Robot(px, py, vx, vy))

    MAX_X = 100
    MAX_Y = 102
    N_SECONDS = 100

    # --- Part 1 ---
    part1_robots = [Robot(r.px, r.py, r.vx, r.vy) for r in robots]
    simulate(part1_robots, N_SECONDS, MAX_X, MAX_Y)

    mid_x, mid_y = MAX_X // 2, MAX_Y // 2
    quadrants = [[0, 0], [0, 0]]
    for r in part1_robots:
        if r.px == mid_x or r.py == mid_y:
            continue
        quadrants[int(r.px > mid_x)][int(r.py > mid_y)] += 1
    part1 = prod(chain.from_iterable(quadrants))

    # --- Part 2 ---
    # Run until all robot positions are unique
    current_robots = [Robot(r.px, r.py, r.vx, r.vy) for r in robots]
    total = len(current_robots)

    seconds = 0
    while True:
        simulate(current_robots, 1, MAX_X, MAX_Y)
        seconds += 1

        positions = {(r.px, r.py) for r in current_robots}
        if len(positions) == total:
            part2 = seconds
            break

    print(f"\n--- Christmas Tree at second {part2} ---\n")
    print(render_grid(current_robots, MAX_X, MAX_Y))

    return part1, part2

print(day14())
