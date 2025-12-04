from typing import Callable
from warnings import deprecated

class Grid:
    def __init__(self, grid: list[list]):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def search_grid(self, condition: int | str | list, callback: Callable[[int, int], None]) -> None:
        """Search the grid for a condition and execute a callback"""
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == condition:
                    callback(r, c)
        return None
    
    def find_in_grid(self, condition: int | str | list) -> None:
        """Search the grid for a condition"""
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == condition:
                    return (r, c)
        return None
    
    def string_to_int(self) -> None:
        """Convert grid of strings to int"""
        self.grid = list(map(lambda row: list(map(int, row)), self.grid))


    def get_neighbours(self, r: int, c: int, include_diagonals: bool = False) -> list[tuple[int, int]]:
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if not include_diagonals and dr != 0 and dc != 0:
                    continue

                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    neighbors.append((nr, nc))
        return neighbors
    
    
    def get_neighbours_conditional(self, r: int, c: int, condition_value: int | str, include_diagonals: bool = False) -> list[tuple[int, int]]:
        conditional_neighbours = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if not include_diagonals and dr != 0 and dc != 0:
                    continue

                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == condition_value:
                    conditional_neighbours.append((nr, nc))
        return conditional_neighbours


    def get_value(self, r: int, c: int):
        if 0 <= r < self.rows and 0 <= c < self.cols:
            return self.grid[r][c]
        return None

    def set_value(self, r: int, c: int, value):
        if 0 <= r < self.rows and 0 <= c < self.cols:
            self.grid[r][c] = value
        return None
    
    def set_multiple(self, positions: set[tuple[int, int]], value) -> None:
        for r, c in positions:
            self.set_value(r, c, value)
        return None

    def print_grid(self) -> None:
        for row in self.grid:
            print("".join(map(str, row)))
        return None
    
    def __repr__(self):
        return "\n".join("".join(map(str, row)) for row in self.grid)


@deprecated("Use Grid class instead")
def search_grid(grid: list[list], condition: int | str | list, callback: lambda y, x: None) -> None:
    """Search a grid for a condition"""
    rows = len(grid)
    cols = len(grid[0])

    for y in range(cols):
        for x in range(rows):
            if grid[y][x] == condition:
                callback(y, x)

    return None

@deprecated("Use Grid class instead")
def find_in_grid(grid: list[list], condition: int | str | list) -> None:
    """Search a grid for a condition"""
    rows = len(grid)
    cols = len(grid[0])

    for y in range(cols):
        for x in range(rows):
            if grid[y][x] == condition:
                return (y, x)

    return None

@deprecated("Use Grid class instead")
def string_to_int(grid: list[list]) -> None:
    """Convert grid of strings to int"""
    return list(map(lambda row: list(map(int, row)), grid))
