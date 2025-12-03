from abc import ABC, abstractmethod
from enum import Enum
from utilities.input import read_lines, read_grid, read_line

class InputType(Enum):
    LINES = 1
    GRID = 2
    SINGLE_LINE = 3


class Solver(ABC):
    def __init__(self, year: int, day: int, input_type: InputType = InputType.LINES, demo: bool = False):
        self.part1: int = 0
        self.part2: int = 0

        match input_type:
            case InputType.LINES:
                self.lines = read_lines(year, day, demo)
            case InputType.GRID:
                self.grid = read_grid(year, day, demo)
            case InputType.SINGLE_LINE:
                self.line = read_line(year, day, demo)
            case _:
                raise ValueError("Invalid input type")


    def run(self) -> None:
        """Run the solver."""
        self.solve()
        print(f"Part 1: {self.part1}\nPart 2: {self.part2}")

    @abstractmethod
    def solve(self) -> None:
        """Solve the puzzle for the given year and day."""
        pass