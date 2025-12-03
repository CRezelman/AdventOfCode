"""Day 3 Solve"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_lines

def find_max_values(values: list[int], digits: int) -> int:
    result_str = ""
    prev_max_index = -1

    for i in range(-digits + 1, 1):
        if i == 0:
            max_value = max(values[prev_max_index+1:])
            prev_max_index = values.index(max_value, prev_max_index + 1)
        else:
            max_value = max(values[prev_max_index+1:i])
            prev_max_index = values.index(max_value, prev_max_index + 1, i)
        result_str += str(max_value)

    return int(result_str)
    

def day3():
    """Day 3"""
    part1 = 0
    part2 = 0
    lines = read_lines(2025, 3)

    for line in lines:
        values = [int(x) for x in line.strip()]

        part1 += find_max_values(values, 2)
        part2 += find_max_values(values, 12)


    return part1, part2

print(day3())
