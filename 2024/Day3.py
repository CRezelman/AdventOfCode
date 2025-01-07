"""Day 3 Solve"""
import re

def day3():
    """Day 3""" 
    part1 = 0
    part2 = 0
    data = open('2024/inputs/day3.txt', 'r', encoding='utf-8').read().strip().split('\n')

    pattern = r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))"
    matches = []

    for line in data:
        matches += re.findall(pattern, line)

    must_match = True

    for match in matches:
        if match[0]:
            part1 += int(match[1]) * int(match[2])
        if must_match and match[0]:
            part2 += int(match[1]) * int(match[2])
        if match[3]:
            must_match = True
        if match[4]:
            must_match = False


    return part1, part2

print(day3())
