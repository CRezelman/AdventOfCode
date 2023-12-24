from collections import deque        

def getNeighbors(grid, y, x, R, C):
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if grid[y][x] == 'v':
        yield y + 1, x
        return

    if grid[y][x] == '^':
        yield y - 1, x
        return

    if grid[y][x] == '>':
        yield y, x + 1
        return

    if grid[y][x] == 'v':
        yield y, x - 1
        return

    for direction in DIRECTIONS:
        dy, dx = direction
        newPoint = y + dy, x + dx
        if  not (0 <= y + dy < R) or not (0 <= x + dx < C) or grid[y+dy][x+dx] == '#':
            continue

        yield newPoint
        

def solve(grid):
    R = len(grid)
    C = len(grid[0])
    yGoal, xGoal = R - 1, C - 2
    y, x = 0, 1
    q = deque()
    q.append((y, x, set()))
    cost = dict()
    cost[(y, x)] = 0

    while q:
        (y, x, path) = q.popleft()

        if y == yGoal and x == xGoal:
            continue

        for (yi, xi) in getNeighbors(grid, y, x, R, C):
            newCost = cost[(y, x)] + 1

            if (yi, xi) in path:
                continue

            if (yi, xi) not in cost or newCost > cost[(yi, xi)]:
                cost[(yi, xi)] = newCost

                new_path = path.copy()
                new_path.add((yi, xi))

                q.appendleft((yi, xi, new_path))

    return cost[(yGoal, xGoal)]

def day23():
    part2 = 0
    grid = [list(line) for line in open('2023/inputs/day23.txt', 'r').read().splitlines()]
    part1 = solve(grid)

    return part1, part2

print(day23())