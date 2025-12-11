"""Day 10 Solve"""
from utilities.solver import Solver
from dataclasses import dataclass
from itertools import combinations

@dataclass
class Procedure:
    indicator: str
    buttons: list[str]
    joltage: str

class Day10(Solver):
    def solve(self) -> None:
        self.procedures: list[Procedure] = []
        for line in self.lines:
            indicator, *buttons, joltage = line.split(" ")
            indicator = [True if ind == "#" else False for ind in indicator.strip('[]')]
            buttons = [tuple(map(int, button.strip('()').split(','))) for button in buttons]
            joltage = list(map(int, joltage.strip('{{}}').split(',')))
            self.procedures.append(Procedure(indicator, buttons, joltage))

        for procedure in self.procedures:
            comb_found = set()
            for r in range(1, len(procedure.buttons) + 1):
                for comb in combinations(procedure.buttons, r):
                    result = [False] * len(procedure.indicator)
                    for button in comb:
                        for b in button:
                            result[b] = not result[b]
                    if result == procedure.indicator:
                        comb_found.add(comb)
                        break
            self.part1 += min(len(c) for c in comb_found)
    
Day10(2025, 10).run()
