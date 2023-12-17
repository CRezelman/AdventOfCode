def findLowestNumber(column: list[int], target: int):
    validNumbers = [num for num in column if num < target]
    
    if validNumbers:
        lowest_number = min(validNumbers)
        column.remove(lowest_number)
        return lowest_number
    else:
        return None

def findHighestNumber(column: list[int], target: int):
    validNumbers = [num for num in column if num > target]
    
    if validNumbers:
        highest_number = max(validNumbers)
        column.remove(highest_number)
        return highest_number
    else:
        return None
    

def tiltNorth(grid: list[list[str]]):
    for x, col in enumerate(zip(*grid)):
        openPositions = []
        for y, char in enumerate(col):
            if char == '.':
                openPositions.append(y)
            elif char == '#':
                openPositions.clear()
            elif char == 'O':
                openPos = findLowestNumber(openPositions, y)
                if openPos != None:
                    grid[openPos][x] = 'O'
                    grid[y][x] = '.'
                    openPositions.append(y)

def tiltSouth(grid: list[list[str]]):
    for x, col in enumerate(zip(*grid)):
        openPositions = []
        for y, char in enumerate(col[::-1]):
            if char == '.':
                openPositions.append(len(col) - y - 1)
            elif char == '#':
                openPositions.clear()
            elif char == 'O':
                openPos = findHighestNumber(openPositions, len(col) - y - 1)
                if openPos != None:
                    grid[openPos][x] = 'O'
                    grid[len(col) - y - 1][x] = '.'
                    openPositions.append(len(col) - y - 1)

def tiltWest(grid: list[list[str]]):
    for y, row in enumerate(grid):
        openPositions = []
        for x, char in enumerate(row):
            if char == '.':
                openPositions.append(x)
            elif char == '#':
                openPositions.clear()
            elif char == 'O':
                openPos = findLowestNumber(openPositions, x)
                if openPos != None:
                    grid[y][openPos] = 'O'
                    grid[y][x] = '.'
                    openPositions.append(x)


def tiltEast(grid: list[list[str]]):
    for y, row in enumerate(grid):
        openPositions = []
        for x, char in enumerate(row[::-1]):
            if char == '.':
                openPositions.append(len(row) - x - 1)
            elif char == '#':
                openPositions.clear()
            elif char == 'O':
                openPos = findHighestNumber(openPositions, len(row) - x - 1)
                if openPos != None:
                    grid[y][openPos] = 'O'
                    grid[y][len(row) - x - 1] = '.'
                    openPositions.append(len(row) - x - 1)

def day14(): 
    part1 = 0
    part2 = 0

    grid = [list(line) for line in open('2023/inputs/day14.txt').read().splitlines()]
    tiltNorth(grid)
    for y, row in enumerate(grid[::-1]):
        part1 += (y+1)*row.count('O')
    
    grid = [list(line) for line in open('2023/inputs/day14.txt').read().splitlines()]

    for i in range(1000):
        tiltNorth(grid)
        tiltWest(grid)
        tiltSouth(grid)
        tiltEast(grid)

    for y, row in enumerate(grid[::-1]):
        part2 += (y+1)*row.count('O')


    return part1, part2

print(day14())
