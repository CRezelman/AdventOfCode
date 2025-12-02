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
            found_ids = set()

            for div in range(2, length + 1):
                size = length // div
                if length % div != 0:
                    continue

                substrings = [id_str[i*size:(i+1)*size] for i in range(div)]

                if all(sub == substrings[0] for sub in substrings):
                    found_ids.add(id)
                    if div == 2:
                        part1 += id

            part2 += sum(found_ids)

    return part1, part2

print(day2())
