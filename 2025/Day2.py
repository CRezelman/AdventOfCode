"""Day 2 Solve"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_line

def day2():
    """Day 2"""
    part1 = 0
    part2 = 0
    line = read_line(2025, 2)

    values = [x for x in line.split(',')]

    for v in values:
        low, high = map(int, v.split('-'))

        for id in range(low, high + 1):
            id_str = str(id)
            length = len(id_str)
            id_invalid = False

            for size in range(1, length // 2 + 1):
                if length % size != 0:
                    continue
                sub = id_str[:size]
                repetitions = length // size
                if sub * repetitions == id_str:
                    id_invalid = True
                    if repetitions == 2:
                        part1 += id

            if id_invalid:
                part2 += id

    return part1, part2

print(day2())
