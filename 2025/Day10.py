"""Day 10 Solve"""
from utilities.solver import Solver
from dataclasses import dataclass
from itertools import combinations
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

@dataclass
class Procedure:
    indicator: int
    buttons_int: list[int]
    buttons_list: list[tuple]
    joltage: list[int]

class Day10(Solver):
    def parse_indicator(self, indicator_str: str) -> list[bool]:
        result = 0 
        for i, ind in enumerate(indicator_str.strip('[]')):
            result |= (1 << i) if ind == "#" else 0
        return result
    
    def parse_button(self, button_str: str) -> int:
        res = 0
        for c in button_str.strip('()').split(","):
            res |= 1 << int(c)
        return res
    
    def min_button_presses(self, procedure: Procedure) -> int:
        n = len(procedure.buttons_int)
        for r in range(1, n + 1):
            for comb in combinations(procedure.buttons_int, r):
                result = 0
                for button in comb:
                    result ^= button
                if result == procedure.indicator:
                    return r
        return 0

    def min_joltage(self, procedure: Procedure) -> int:
        B = np.zeros((len(procedure.joltage), len(procedure.buttons_list)), dtype=int)
        for i, button in enumerate(procedure.buttons_list):
            for j in button:
                B[j, i] = 1

        J = np.array(procedure.joltage, dtype=float)
        n_vars = len(procedure.buttons_list)
        c = np.ones(n_vars, dtype=float)
        constraints = LinearConstraint(B, lb=J, ub=J)
        bounds = Bounds(lb=np.zeros(n_vars), ub=np.full(n_vars, np.inf))
        integrality = np.ones(n_vars, dtype=int)

        result = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)
        x = np.rint(result.x).astype(int)
        return sum(x)


    def solve(self) -> None:
        self.procedures: list[Procedure] = []
        for line in self.lines:
            indicator, *buttons, joltage = line.split(" ")
            indicator = self.parse_indicator(indicator)
            buttons_int = [self.parse_button(button) for button in buttons]
            buttons_list = [tuple(map(int, button.strip('()').split(','))) for button in buttons]
            joltage = list(map(int, joltage.strip('{{}}').split(',')))
            self.procedures.append(Procedure(indicator, buttons_int, buttons_list, joltage))

        for procedure in self.procedures:
            self.part1 += self.min_button_presses(procedure)
            self.part2 += self.min_joltage(procedure)
    
Day10(2025, 10).run()
