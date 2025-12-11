"""Day 11 Solve"""
from utilities.solver import Solver
from functools import cache

class Day11(Solver):
    @cache
    def count_paths(self, source, target) -> int:
        return 1 if source == target else sum(
            self.count_paths(neighbor, target)
            for neighbor in self.G.get(source, [])
        ) 

    def solve(self) -> None:

        self.G = dict()
        for line in self.lines:
            input, output = line.split(': ')
            output = output.split(' ')
            self.G[input] = output

        self.part1 = self.count_paths('you', 'out')
        self.part2 = self.count_paths('svr', 'fft') * self.count_paths('fft', 'dac') * self.count_paths('dac', 'out')
    
Day11(2025, 11).run()
