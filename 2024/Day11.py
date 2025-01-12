"""Day 11 Solve"""
from functools import cache
from math import floor, log10
from utilities.input import read_lines

@cache
def count(x, d=75):
    """Recursive Count"""
    if d == 0:
        return 1
    if x == 0:
        return count(1, d-1)

    l = floor(log10(x))+1
    if l % 2:
        return count(x*2024, d-1)

    return (count(x // 10**(l//2), d-1)+
            count(x %  10**(l//2), d-1))


def day11():
    """Day 11"""
    part1 = 0
    part2 = 0
    data = read_lines(2024, 11)[0]
    stones = list(map(int, data.split(' ')))

    part1 = sum(map(lambda x: count(x, d=25), stones))
    part2 = sum(map(lambda x: count(x, d=75), stones))

    return part1, part2

print(day11())
