"""Grid functions"""

def search_grid(grid: list[list], condition: int | str | list, callback: lambda y, x: None) -> None:
    """Search a grid for a condition"""
    rows = len(grid)
    cols = len(grid[0])

    for y in range(cols):
        for x in range(rows):
            if grid[y][x] == condition:
                callback(y, x)

    return None
