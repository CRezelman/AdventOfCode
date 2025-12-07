"""Day 6 Solve"""
from utilities.solver import Solver

class Day6(Solver):

    def solve(self) -> None:
        self.problems = [line.split() for line in self.lines]

        for *nums, op in zip(*self.problems):
            self.part1 += eval(op.join(nums))

        group = []
        op = None
        for column in reversed(list(zip(*self.grid.grid))):
            if all(c == " " for c in column):
                continue

            op = column[-1]
            group.append("".join(column[:-1]).strip())

            if op != " " and op is not None:
                self.part2 += eval(op.join(group))
                op = None
                group = []
    
Day6(2025, 6, strip=False).run()
