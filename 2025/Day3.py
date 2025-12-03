"""Day 3 Solve"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_lines

def find_max_values(values: list[int], digits: int) -> int:
    result = 0
    start_index = -1
    length = len(values)

    for i in range(1 - digits, 1):
        max_value = max(values[start_index + 1:length + i])
        start_index = values.index(max_value, start_index + 1, length + i)
        result += max_value*(10**abs(i))

    return result


def day3():
    """Day 3"""
    part1 = 0
    part2 = 0
    lines = read_lines(2025, 3, True)

    for line in lines:
        values = [int(x) for x in line.strip()]

        part1 += find_max_values(values, 2)
        part2 += find_max_values(values, 12)

    return part1, part2

print(day3())
