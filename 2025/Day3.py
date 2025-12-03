"""Day 3 Solve"""
from utilities.solver import InputType, Solver

class Day3(Solver):
    def find_max_values(self, values: list[int], digits: int) -> int:
        result = 0
        start_index = -1
        length = len(values)

        for i in range(1 - digits, 1):
            max_value = max(values[start_index + 1:length + i])
            start_index = values.index(max_value, start_index + 1, length + i)
            result += max_value*(10**abs(i))

        return result

    def solve(self) -> None:
        for line in self.lines:
            values = [int(x) for x in line.strip()]

            self.part1 += self.find_max_values(values, 2)
            self.part2 += self.find_max_values(values, 12)
    
Day3(2025, 3, InputType.LINES).run()
