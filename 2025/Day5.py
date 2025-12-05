"""Day 5 Solve"""
from utilities.solver import InputType, Solver

class Day5(Solver):

    def parse_input(self) -> None:
        self.fresh_range = []
        self.available = []

        found_new_line = False
        for line in self.lines:
            if line == "":
                found_new_line = True
                continue
            if found_new_line:
                self.available.append(int(line.strip()))
            else:
                min, max = line.strip().split('-')
                self.fresh_range.append((int(min), int(max)))

    def solve(self) -> None:
        self.parse_input()

        for available_id in self.available:
            for min_id, max_id in self.fresh_range:
                if min_id <= available_id <= max_id:
                    self.part1 += 1
                    break

        sorted_ranges = sorted(self.fresh_range, key=lambda x: x[0])
        merged_ranges = [sorted_ranges[0]]

        for current in sorted_ranges:
            previous = merged_ranges[-1]
            if current[0] <= previous[1]:
                merged_ranges[-1] = (previous[0], max(previous[1], current[1]))
            else:
                merged_ranges.append(current)
            
        for min_id, max_id in merged_ranges:
            self.part2 += (max_id - min_id + 1)

    
Day5(2025, 5, InputType.LINES).run()
