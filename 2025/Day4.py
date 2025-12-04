"""Day 4 Solve"""
from utilities.solver import InputType, Solver

class Day4(Solver):

    def find_possible_rolls(self, r: int, c: int) -> int:
        neighbours = self.grid.get_neighbors(r, c, include_diagonals=True)
        count = sum(1 for nr, nc in neighbours if self.grid.get_value(nr, nc) == '@')
        if count < 4:
            self.rolls.add((r, c))

    def solve(self) -> None:
        self.rolls = set()
        self.grid.search_grid('@', self.find_possible_rolls)
        self.part1 = len(self.rolls)
        self.part2 = len(self.rolls)

        for r, c in self.rolls:
            self.grid.set_value(r, c, '.')

        while len(self.rolls) > 0:
            self.rolls = set()
            self.grid.search_grid('@', self.find_possible_rolls)
            self.part2 += len(self.rolls)
            for r, c in self.rolls:
                self.grid.set_value(r, c, '.')
    
Day4(2025, 4, InputType.GRID).run()
