"""Day 2 Solve"""
from utilities.solver import InputType, Solver

class Day2(Solver):
    def is_increasing(self, arr:list[int]) -> bool:
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1] or arr[i] - arr[i - 1] > 3:
                return False
        return True

    def is_decreasing(self, arr:list[int]) -> bool:
        for i in range(1, len(arr)):
            if arr[i] >= arr[i - 1] or arr[i - 1] - arr[i] > 3:
                return False
        return True

    def is_safe_p1(self, arr:list[int]) -> bool:
        return self.is_increasing(arr) or self.is_decreasing(arr)

    def is_safe_p2(self, arr:list[int]) -> bool:
        for i in range(len(arr)):
            if self.is_safe_p1(arr[:i] + arr[i + 1:]):
                return True
        return False

    def solve(self) -> None:
        for line in self.lines:
            line = list(map(int, line.split(' ')))

            if self.is_safe_p1(line):
                self.part1 += 1
                self.part2 += 1
            elif self.is_safe_p2(line):
                self.part2 += 1


Day2(2024, 2, InputType.LINES).run()
