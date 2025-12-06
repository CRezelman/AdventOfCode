"""Day 3 Solve"""
import re
from utilities.solver import Solver

class Day3(Solver):
    def solve(self) -> None:
        pattern = r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))"
        matches = []

        for line in self.lines:
            matches += re.findall(pattern, line)

        must_match = True

        for match in matches:
            if match[0]:
                self.part1 += int(match[1]) * int(match[2])
            if must_match and match[0]:
                self.part2 += int(match[1]) * int(match[2])
            if match[3]:
                must_match = True
            if match[4]:
                must_match = False
    
Day3(2024, 3).run()
