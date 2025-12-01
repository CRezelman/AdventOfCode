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
            first = (100 - location) % 100
            offset = first == 0

            if first <= steps:
                part2 += 1 - int(offset) + (steps - first) // 100
            location = (location + steps) % 100
        else:
            first = location % 100
            offset = first == 0

            if first <= steps:
                part2 += 1 - int(offset) + (steps - first) // 100
            location = (location - steps) % 100
  
        if location == 0:
            part1 += 1

    return part1, part2

print(day1())
