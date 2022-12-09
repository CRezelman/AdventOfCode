
class Head():
    x = 0
    y = 0
    prevX = 0
    prevY = 0

    def __init__(self, x, y, prevX, prevY):
        self.x = x
        self.y = y
        self.prevX = prevX
        self.prevY = prevY


def checkDist(head: Head, tX, tY):
    return abs(head.x - tX) >= 2 or abs(head.y - tY) >= 2


def day9_2():
    part1 = 0
    part2 = 0

    head = Head(0,0,0,0)
    tX = 0
    tY = 0

    prevDir = 'h'

    tailPlaces = set()

    with open('2022/day9.txt') as f:
        for i, line in enumerate(f):
            line = line.strip('\n')
            dir, count = line.split(' ')

            for j in range(int(count)):
                head.prevX = head.x
                head.prevY = head.y

                if dir == 'R':
                    head.x +=1

                elif dir == 'L':
                    head.x -= 1

                elif dir == 'U':
                    head.y += 1

                elif dir == 'D':
                    head.y -= 1

                if checkDist(head, tX, tY):
                    tX = head.prevX
                    tY = head.prevY

                tailPlaces.add((tX, tY))

            
    print(tailPlaces)
    part1 = len(tailPlaces)

    return part1, part2

print(day9_2())