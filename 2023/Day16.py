class Light:
    def __init__(self, position: tuple[int, int], direction: tuple[int, int]) -> None:
        self.position = position
        self.direction = direction

def solve(grid, start):
    visited = set()
    visitedDir = set()
    lights: list[Light] = [start]
    while len(lights):
        current = lights.pop(0)
        if current.position[0] < 0 or current.position[0] >= len(grid) or current.position[1] < 0 or current.position[1] >= len(grid[0]):
            continue
        visited.add(current.position)
        visitedDir.add((current.position, current.direction))

        if grid[current.position[0]][current.position[1]] == '.':
            nextDir = current.direction
        elif grid[current.position[0]][current.position[1]] == '\\':
            nextDir = (current.direction[1] , current.direction[0])
        elif grid[current.position[0]][current.position[1]] == '/':
            nextDir = (-current.direction[1] , -current.direction[0])
        elif grid[current.position[0]][current.position[1]] == '-':
            if current.direction[0] == 0:
                nextDir = current.direction
            else:
                if ((current.position[0], current.position[1] - 1), (0, -1)) not in visitedDir:
                    lights.append(Light((current.position[0], current.position[1] - 1), (0, -1)))
                if ((current.position[0], current.position[1] + 1), (0,  1)) not in visitedDir:
                    lights.append(Light((current.position[0], current.position[1] + 1), (0,  1)))
                continue
        elif grid[current.position[0]][current.position[1]] == '|':
            if current.direction[1] == 0:
                nextDir = current.direction
            else:
                if ((current.position[0] - 1, current.position[1]), (-1, 0)) not in visitedDir:
                    lights.append(Light((current.position[0] - 1, current.position[1]), (-1, 0)))
                if ((current.position[0] + 1, current.position[1]), ( 1, 0)) not in visitedDir:
                    lights.append(Light((current.position[0] + 1, current.position[1]), ( 1, 0)))
                continue
        
        nextPos = (current.position[0] + nextDir[0], current.position[1] + nextDir[1])
        lights.append(Light(nextPos, nextDir))

    return len(visited)

def day16(): 
    part1 = 0
    part2 = 0
    start = Light((0, 0), (0, 1))

    grid = [list(line) for line in open('2023/inputs/day16.txt', 'r').read().splitlines()]

    part1 = solve(grid, start)

    results = []

    for i in range(len(grid)):
        start = Light((i, 0), (0, 1))
        results.append(solve(grid, start))
        start = Light((i, len(grid)-1), (0, -1))
        results.append(solve(grid, start))

    for i in range(len(grid[0])):
        start = Light((0, i), (1, 0))
        results.append(solve(grid, start))
        start = Light((len(grid[0])-1, i), (-1, 0))
        results.append(solve(grid, start))

    part2 = max(results)


    return part1, part2

print(day16())
