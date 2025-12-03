"""Day 10 Solve"""
from utilities.input import read_grid
from utilities.grid import string_to_int

def find_reachable_end_counts(grid):
    """Reachable 9s"""
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y, reachable_nines: set, visited: set):
        visited.add((x, y))

        if grid[x][y] == 9:
            reachable_nines.add((x, y))
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if grid[nx][ny] == grid[x][y] + 1:
                    dfs(nx, ny, reachable_nines, visited)

    results = {}
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                visited = set()
                reachable_nines = set()
                dfs(i, j, reachable_nines, visited)
                results[(i, j)] = len(reachable_nines)

    return results


def find_unique_paths(grid):
    """Unique Paths"""
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y, visited: set):
        if grid[x][y] == 9:
            return 1

        visited.add((x, y))
        path_count = 0

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if grid[nx][ny] == grid[x][y] + 1:
                    path_count += dfs(nx, ny, visited)

        visited.remove((x, y))
        return path_count

    results = {}
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                visited = set()
                results[(i, j)] = dfs(i, j, visited)

    return results


def day10():
    """Day 10"""
    part1 = 0
    part2 = 0
    grid = read_grid(2024, 10).grid
    grid = string_to_int(grid)

    result_p1 = find_reachable_end_counts(grid)
    result_p2 = find_unique_paths(grid)

    for start, count in result_p1.items():
        part1 += count

    for start, count in result_p2.items():
        part2 += count


    return part1, part2

print(day10())
