"""Day 13 Solve"""
from dataclasses import dataclass
from sympy import symbols, solve
import re

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_lines

@dataclass
class Coordinate:
    X: int
    Y: int  

@dataclass
class Machine:
    button_a: Coordinate
    button_b: Coordinate
    prize: Coordinate

def parse_coord(line: str, sep: str) -> Coordinate:
    """Extract X and Y coordinates using the given separator ('+' or '=')"""
    x, y = map(int, re.findall(rf"X\{sep}(\d+), Y\{sep}(\d+)", line)[0])
    return Coordinate(x, y)

def solve_machine(machine: Machine, offset: int = 0) -> tuple[int, int] | None:
    """Solve the machine's linear system for button presses (a, b)."""
    ax, ay = machine.button_a.X, machine.button_a.Y
    bx, by = machine.button_b.X, machine.button_b.Y
    px, py = machine.prize.X + offset, machine.prize.Y + offset

    det = ax * by - ay * bx
    if det == 0:
        return None  # Parallel or no unique integer solution

    a = (px * by - py * bx) / det
    b = (py * ax - px * ay) / det

    if a.is_integer() and b.is_integer() and a >= 0 and b >= 0:
        return int(a), int(b)
    return None

def day13():
    """Day 13"""
    part1 = 0
    part2 = 0
    lines = read_lines(2024, 13)

    text = "\n".join(lines).strip()
    machines_raw = [block.splitlines() for block in text.split("\n\n")]

    machines = [
        Machine(
            button_a=parse_coord(raw[0], "+"),
            button_b=parse_coord(raw[1], "+"),
            prize=parse_coord(raw[2], "="),
        )
        for raw in machines_raw
    ]


    for machine in machines:
        OFFSET = 10000000000000
        if (sol := solve_machine(machine)):
            a, b = sol
            part1 += 3 * a + b
        if (sol := solve_machine(machine, OFFSET)):
            a, b = sol
            part2 += 3 * a + b

    return part1, part2

print(day13())
