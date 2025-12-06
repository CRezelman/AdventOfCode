"""Day 12 Solve"""
from utilities.solver import Solver
import json

class Day12(Solver):

    def solve(self) -> None:
        data = json.loads(self.line)

        def walk(obj, ignore_red: bool) -> int:
            if isinstance(obj, int):
                return obj

            if isinstance(obj, list):
                return sum(walk(item, ignore_red) for item in obj)

            if isinstance(obj, dict):
                if ignore_red and "red" in obj.values():
                    return 0
                return sum(walk(v, ignore_red) for v in obj.values())

            return 0

        self.part1 = walk(data, ignore_red=False)
        self.part2 = walk(data, ignore_red=True)

Day12(2015, 12).run()
