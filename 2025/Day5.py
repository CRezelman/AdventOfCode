"""Day 5 Solve"""
from utilities.solver import Solver

class Day5(Solver):
    def solve(self) -> None:
        range_lines, value_lines = "\n".join(self.lines).split("\n\n")
        self.fresh_ranges: list[tuple[int, int]] = [
            tuple(map(int, line.split('-'))) 
            for line in range_lines.splitlines()
        ]
        self.available: list[int] = [
            int(line) for line in value_lines.splitlines()
        ]

        self.fresh_ranges = sorted(self.fresh_ranges, key=lambda x: x[0])
        self.merged_fresh_ranges = [self.fresh_ranges[0]]

        for current in self.fresh_ranges:
            previous = self.merged_fresh_ranges[-1]
            if current[0] <= previous[1]:
                self.merged_fresh_ranges[-1] = (previous[0], max(previous[1], current[1]))
            else:
                self.merged_fresh_ranges.append(current)

        self.part1 = sum(any(min_id <= available_id <= max_id for min_id, max_id in self.merged_fresh_ranges) for available_id in self.available)
        self.part2 = sum(max_id - min_id + 1 for min_id, max_id in self.merged_fresh_ranges)
    
Day5(2025, 5).run()
