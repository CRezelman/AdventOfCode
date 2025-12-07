"""Day 7 Solve"""
from utilities.solver import Solver

class Day7(Solver):
    def solve(self) -> None:
        start = self.grid.find_in_grid("S")

        current = [0] * self.grid.cols
        current[start[1]] = 1

        for r in range(self.grid.rows - 1):
            next_row = [0] * self.grid.cols

            for c in range(self.grid.cols):
                count = current[c]
                if count == 0:
                    continue

                if self.grid.get_value(r + 1, c) == '^':
                    self.part1 += 1
                    next_row[c - 1] += count
                    next_row[c + 1] += count
                else:
                    next_row[c] += count

            current = next_row

        self.part2 = sum(current)

Day7(2025, 7).run()
