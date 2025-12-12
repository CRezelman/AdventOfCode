"""Day 12 Solve"""
from utilities.solver import Solver
from itertools import groupby
import re

class Day12(Solver):

    def solve(self) -> None:
        *shapes, grids = [list(group) for key, group in groupby(self.lines, key=lambda x: x == "") if not key]
        sizes = []
        for shape in shapes:
            count = 0
            for line in shape[1:]:
                count += line.count('#')
            sizes.append(count)

        for grid in grids:
            nr, nc, *vs = map(int, re.findall('\d+', grid))
            self.part1 += nr * nc > sum( v * s for v, s in zip(vs, sizes))

Day12(2025, 12).run()
