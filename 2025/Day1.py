"""Day 1 Solve"""
from utilities.solver import Solver

class Day1(Solver):
    def solve(self) -> None:
        location = 50

        for line in self.lines:
            direction = line[0]
            steps = int(line[1:])

            if direction == 'R':
                location += steps
                if location >= 100:
                    self.part2 += location // 100
            else:
                offset = location == 0
                location -= steps
                if location <= 0:
                    self.part2 += 1 + location // -100 - offset
            location %= 100

            if location == 0:
                self.part1 += 1
    
Day1(2025, 1).run()

