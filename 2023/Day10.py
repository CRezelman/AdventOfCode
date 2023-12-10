from enum import Enum

class Pipe(Enum):
    NS = '|'
    EW = '-'
    NE = 'L'
    NW = 'J'
    SW = '7'
    SE = 'F'
    NONE = '.'
    START = 'S'

MOVEMENTS = {
    Pipe.NS: ((-1, 0), (1, 0)),
    Pipe.EW: ((0, -1), (0, 1)),
    Pipe.NE: ((-1, 0), (0, 1)),
    Pipe.NW: ((-1, 0), (0, -1)),
    Pipe.SW: ((1, 0), (0, -1)),
    Pipe.SE: ((1, 0), (0, 1)),
    Pipe.START: ((1, 0), (0, 1)),
}


def move(start: tuple[int, int], previous: tuple[int, int], pipe: Pipe,  pipeMap: list[list[str]]) -> tuple[tuple[int, int], Pipe]:
    moves = MOVEMENTS[pipe]

    for move in moves:
        newPosition = (start[0] + move[0], start[1] + move[1])
        if newPosition != previous:
            return newPosition, Pipe(pipeMap[start[0] + move[0]][start[1] + move[1]])

            
def day10(): 
    part1 = 0
    part2 = 0
    with open('2023/inputs/day10.txt', 'r') as f:
       pipeMap = [list(line.strip()) for line in f]
    
    for i, row in enumerate(pipeMap):
        for j, char in enumerate(row):
            if char == Pipe.START.value:
                start = (i, j)
                break

    pipe = Pipe.START
    currentPosition = start
    previousPosition = (start[0] + 1, start[1])
    visited: set[tuple[int, int]] = { start }

    while True:
        newPosition, pipe = move(currentPosition, previousPosition, pipe, pipeMap)
        previousPosition = currentPosition
        currentPosition = newPosition
        visited.add(currentPosition)

        if newPosition == start:
            part1 = len(visited) // 2
            break

    
    for y, line in enumerate(pipeMap):
        for x, char in enumerate(line):
            if (y, x) in visited:
                continue
            
            crosses = 0
            x2, y2 = x, y

            while x2 < len(pipeMap[0]) and y2 < len(pipeMap):
                char2 = Pipe(pipeMap[y2][x2])
                if (y2, x2) in visited and char2 != Pipe.NE and char2 != Pipe.SW:
                    crosses += 1
                x2 += 1
                y2 += 1


            if crosses % 2 == 1:
                part2 += 1

    return part1, part2

print(day10())