from collections import deque

def isValidPart1(grid, R, C, x, y):
    return 0 <= y < R and 0 <= x < C and grid[y][x] != '#'

def isValidPart2(grid, R, C, x, y):
    return grid[y % R][x % C] != '#'

def solve(grid, GOAL: int, isValid):
    R = len(grid)
    C = len(grid[0])
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    y, x = next((y, x) for y in range(R) for x in range(C) if grid[y][x] == 'S')
    q = deque()
    q.append((y, x, 0))

    visited = set()
    goalSet = set()

    while q:
        (y, x, steps) = q.popleft()

        if steps == GOAL:
            goalSet.add((y, x))
            continue

        if (y, x, steps) in visited: 
            continue
        visited.add((y, x, steps))

        for direction in DIRECTIONS:
            dy, dx = direction
            if isValid(grid, R, C, y + dy, x + dx):
                q.append((y + dy, x + dx, steps + 1))

    return len(goalSet)


def f(n, y0, y1, y2):
    a = (y2+y0-2*y1)/2
    b = y1-y0 -a
    c = y0
    return int(a*n**2 + b*n + c)


def day21():
    grid = [list(line) for line in open('2023/inputs/day21.txt', 'r').read().splitlines()]
    part1 = solve(grid, 64, isValidPart1)

    y0 = solve(grid, 65, isValidPart2)
    y1 = solve(grid, 196, isValidPart2)
    y2 = solve(grid, 327, isValidPart2)

    part2 = f(26501365 // len(grid), y0, y1, y2)    

    return part1, part2

print(day21())