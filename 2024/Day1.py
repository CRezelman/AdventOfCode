"""Day 1 Solve"""
from collections import Counter
from utilities.solver import Solver

class Day1(Solver):
    def solve(self) -> None:
        left = []
        right = []
        for line in self.lines:
            left_str, right_str = line.split('   ')
            left.append(int(left_str))
            right.append(int(right_str))

        left.sort()
        right.sort()

        right_counter = dict(Counter(right))
        for l, r in zip(left, right):
            self.part1 += abs(l - r)
        for item in left:
            self.part2 += right_counter.get(item, 0) * item


Day1(2024, 1).run()
