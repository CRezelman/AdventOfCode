"""Utility File for reading Input Data"""

def read_lines(year: int, day: int, demo: bool = False) -> list:
    """Reads a file and returns a list of lines"""
    return open(f'{year}/inputs/day{day}{"demo" if demo else ""}.txt', 'r', encoding='utf-8').read().strip().split('\n')

def read_grid(year: int, day: int, demo: bool = False) -> list:
    """Reads a file and returns a list of lists"""
    return [list(line) for line in open(f'{year}/inputs/day{day}{"demo" if demo else ""}.txt', 'r', encoding='utf-8').read().strip().split('\n')]
