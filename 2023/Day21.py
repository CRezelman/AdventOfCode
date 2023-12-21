from collections import deque

def isValid(grid, R, C, x, y):
    return 0 <= y < R and 0 <= x < C and grid[y][x] != '#'


def day21():
    part2 = 0
    grid = [list(line) for line in open('2023/inputs/day21.txt', 'r').read().splitlines()]
    R = len(grid)
    C = len(grid[0])
    GOAL = 64
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



    part1 = len(goalSet)

    return part1, part2

print(day21())