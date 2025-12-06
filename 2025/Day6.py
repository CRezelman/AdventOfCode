"""Day 6 Solve"""
from utilities.solver import InputType, Solver
import math

class Day6(Solver):

    def solve(self) -> None:
        self.problems = []

        for line in self.lines:
            items = line.split()
            self.problems.append(items)

        cols = len(self.problems[0]) 
        
        for col in range(cols):
            column_items = [self.problems[row][col] for row in range(len(self.problems)) if col < len(self.problems[row])]
            operation = column_items.pop(-1)
            if operation == "*":
                self.part1 += math.prod(map(int, column_items))
            elif operation == "+":
                self.part1 += sum(map(int, column_items))


        current_numbers = []
        current_operation = None
        for column in reversed(list(zip(*self.grid.grid))):
            if all(c == " " for c in column):
                continue

            if column[-1] != " ":
                current_operation = column[-1]

            current_numbers.append("".join(column[:-1]).strip())

            if current_operation == "*":
                self.part2 += math.prod(map(int, current_numbers))
                current_operation = None
                current_numbers = []
            elif current_operation == "+":
                self.part2 += sum(map(int, current_numbers))
                current_operation = None
                current_numbers = []

    
Day6(2025, 6, strip=False).run()
