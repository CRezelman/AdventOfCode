from abc import ABC, abstractmethod
from enum import Enum
import time
from rich.console import Console
from utilities.grid import Grid
from utilities.input import read_lines, read_grid, read_line

console = Console()

class InputType(Enum):
    LINES = 1
    GRID = 2
    SINGLE_LINE = 3

class Solver(ABC):
    def __init__(self, year: int, day: int, input_type: InputType = InputType.LINES, demo: bool = False):
        self.part1: int = 0
        self.part2: int = 0

        self.lines: list[str] = None
        self.grid: Grid = None
        self.line: str = None

        match input_type:
            case InputType.LINES:
                self.lines = read_lines(year, day, demo)
            case InputType.GRID:
                self.grid = read_grid(year, day, demo)
            case InputType.SINGLE_LINE:
                self.line = read_line(year, day, demo)
            case _:
                raise ValueError("Invalid input type")

        console.rule(f"[bold cyan]Advent of Code {year} - Day {day} {'(Demo)' if demo else ''}[/bold cyan]")

    def run(self) -> None:
        """Run the solver."""
        start = time.perf_counter_ns()
        self.solve()
        end = time.perf_counter_ns()
        elapsed_ms = (end - start) / 1_000_000

        console.print(f"[bold green]Part 1:[/bold green] [yellow]{self.part1}[/yellow]")
        console.print(f"[bold green]Part 2:[/bold green] [yellow]{self.part2}[/yellow]")
        console.print(f"[bold blue]Time:[/bold blue] {elapsed_ms:.3f}ms")
        console.rule()

    @abstractmethod
    def solve(self) -> None:
        """Solve the puzzle for the given year and day."""
        pass
