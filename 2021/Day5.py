class Points:
    def __init__(self, x1: str, y1: str, x2: str, y2: str) -> None:
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

    def isStraight(self) -> bool:
        return self.isHorizontal() or self.isVertical()
    
    def isHorizontal(self) -> bool:
        return self.y1 == self.y2
    
    def isVertical(self) -> bool:
        return self.x1 == self.x2
    
    def isDiagonalIncreasing(self) -> bool:
        return (self.x2 > self.x1 and self.y1 > self.y2) or (self.x1 > self.x2 and self.y2 > self.y1)
    
    def isDiagonalDecreasing(self) -> bool:
        return (self.x2 > self.x1 and self.y2 > self.y1) or (self.x1 > self.x2 and self.y1 > self.y2)
    
    def minY(self) -> int:
        return min(self.y1, self.y2)
    
    def maxY(self) -> int:
        return max(self.y1, self.y2)
    
    def minX(self) -> int:
        return min(self.x1, self.x2)
    
    def maxX(self) -> int:
        return max(self.x1, self.x2)

def day5(): 
    part1 = 0
    part2 = 0
    vents: list[Points] = []
    grid1 = [[0 for i in range(1000)] for j in range(1000)]
    grid2 = [[0 for i in range(1000)] for j in range(1000)]
    with open('2021/inputs/day5.txt') as f:
        for line in f:
            line = line.strip('\n')
            p1, p2 = line.split(' -> ')
            x1, y1 = p1.split(',')
            x2, y2 = p2.split(',')
            vents.append(Points(x1, y1, x2, y2))

    for vent in vents:
        if vent.isHorizontal():
            for i in range(vent.maxX() - vent.minX() + 1):
                grid2[vent.y1][vent.minX() + i] += 1
        elif vent.isVertical():
            for i in range(vent.maxY() - vent.minY() + 1):
                grid2[vent.minY() + i][vent.x1] += 1
        elif vent.isDiagonalIncreasing():
            for i in range(vent.maxY() - vent.minY() + 1):
                grid2[vent.maxY() - i][vent.minX() + i] += 1
        elif vent.isDiagonalDecreasing():
            for i in range(vent.maxY() - vent.minY() + 1):
                grid2[vent.minY() + i][vent.minX() + i] += 1

    
    for vent in vents:
        if vent.isHorizontal():
            for i in range(vent.maxX() - vent.minX() + 1):
                grid1[vent.y1][vent.minX() + i] += 1
        elif vent.isVertical():
            for i in range(vent.maxY() - vent.minY() + 1):
                grid1[vent.minY() + i][vent.x1] += 1

    for row in grid1:
        for value in row:
            if value > 1:
                part1 += 1

    for row in grid2:
        for value in row:
            if value > 1:
                part2 += 1

    return part1, part2

print(day5())