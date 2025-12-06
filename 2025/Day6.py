"""Day 6 Solve"""
from utilities.solver import Solver
import math

class Day6(Solver):

    def solve(self) -> None:
        ops = {
            "*": lambda xs: math.prod(map(int, xs)),
            "+": lambda xs: sum(map(int, xs)),
        }

        self.problems = [line.split() for line in self.lines]
        
        for column_items in zip(*self.problems):
            operation = column_items[-1]
            self.part1 += ops[operation](column_items[:-1])


        current_numbers = []
        operation = None
        for column in reversed(list(zip(*self.grid.grid))):
            if all(c == " " for c in column):
                continue

            if column[-1] != " ":
                operation = column[-1]

            current_numbers.append("".join(column[:-1]).strip())

            if operation:
                self.part2 += ops[operation](current_numbers)
                operation = None
                current_numbers = []

    
Day6(2025, 6, strip=False).run()
