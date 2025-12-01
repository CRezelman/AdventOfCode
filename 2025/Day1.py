"""Day 1 Solve"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_lines

def day1():
    """Day 1"""
    part1 = 0
    part2 = 0
    lines = read_lines(2025, 1)
    location = 50

    for line in lines:
        direction = line[0]
        steps = int(line[1:])

        if direction == 'R':
            min_steps = 100 - location
            location += steps

            if steps >= min_steps:
                part2 += location // 100
        else:
            min_steps = location
            location -= steps

            if steps >= min_steps:
                offset = min_steps == 0
                part2 += (100 - location) // 100 - offset
        location %= 100

        if location == 0:
            part1 += 1

    return part1, part2

print(day1())
