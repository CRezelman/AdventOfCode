"""Day 2 Solve"""
from utilities.solver import InputType, Solver

class Day2(Solver):
    def solve(self) -> None:
        values = [x for x in self.line.split(',')]

        for v in values:
            low, high = map(int, v.split('-'))

            for id in range(low, high + 1):
                id_str = str(id)
                length = len(id_str)
                id_invalid = False

                for size in range(1, length // 2 + 1):
                    if length % size != 0:
                        continue
                    sub = id_str[:size]
                    repetitions = length // size
                    if sub * repetitions == id_str:
                        id_invalid = True
                        if repetitions == 2:
                            self.part1 += id

                if id_invalid:
                    self.part2 += id
    
Day2(2025, 2, InputType.SINGLE_LINE).run()
