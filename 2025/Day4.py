"""Day 4 Solve"""
from utilities.solver import InputType, Solver

class Day4(Solver):
    def find_possible_rolls(self, r: int, c: int) -> int:
        neighbours = self.grid.get_neighbours_conditional(r, c, '@', include_diagonals=True)
        if len(neighbours) < 4:
            self.rolls.add((r, c))

    def solve(self) -> None:
        state = 0
        while True:
            self.rolls = set()
            self.grid.search_grid('@', self.find_possible_rolls)
            if not self.rolls or state >= 100:
                break

            self.grid.set_multiple(self.rolls, '.')

            if state == 0:
                self.part1 = len(self.rolls)
            self.part2 += len(self.rolls)
            state += 1
    
Day4(2025, 4, InputType.GRID).run()
