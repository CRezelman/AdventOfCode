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
    moves = 0

    while True:
        newPosition, pipe = move(currentPosition, previousPosition, pipe, pipeMap)
        previousPosition = currentPosition
        currentPosition = newPosition
        moves += 1

        if newPosition == start:
            part1 = moves // 2
            break

    return part1, part2

print(day10())