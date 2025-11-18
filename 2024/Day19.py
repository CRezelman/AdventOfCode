"""Day 19 Solve"""
import sys
import os
from functools import cache
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilities.input import read_lines

def day19():
    """Day 19"""
    part1 = 0
    part2 = 0
    lines = read_lines(2024, 19)

    towels = lines[0].split(', ')
    designs =  lines[2:]

    @cache
    def is_possible(design: str) -> bool:
        return (design == '' or any(
            design.startswith(towel) and is_possible(design[len(towel):])
            for towel in towels
        ))
    
    @cache
    def count_ways(design: str) -> int:
        if not design:
            return 1
        combinations = 0
        for towel in towels:
            if design.startswith(towel):
                combinations += count_ways(design[len(towel):])
        return combinations
    
    part1 = sum(1 for design in designs if is_possible(design))
    part2 = sum(count_ways(design) for design in designs)

    return part1, part2

print(day19())
