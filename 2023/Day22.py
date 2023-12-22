from matplotlib import pyplot as plt

class Point:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

class Brick:
    def __init__(self, start: Point, end: Point, id) -> None:
        self.start = start
        self.end = end
        self.id = id
    

def populateBricks(grid: list[list[list[int | None]]], bricks: list[Brick]):
    for brick in bricks:
        drawBrick(grid, brick, brick.id)


def drawBrick(grid: list[list[list[int | None]]], brick: Brick, value) -> None:
    for dx in range(brick.start.x, brick.end.x + 1):
        for dy in range(brick.start.y, brick.end.y + 1):
            for dz in range(brick.start.z, brick.end.z + 1):
                grid[dz][dy][dx] = value
    

def canBrickMoveDown(grid: list[list[list[int | None]]], brick: Brick) -> bool:
    for dx in range(brick.start.x, brick.end.x + 1):
        for dy in range(brick.start.y, brick.end.y + 1):
            if grid[brick.minZ - 1][dy][dx] is not None or brick.minZ - 1 == 0:
                return False
    return True

def moveBrickDown(grid: list[list[list[int | None]]], brick: Brick) -> bool:
    drawBrick(grid, brick, None)
    brick.start.z -= 1
    brick.end.z -= 1
    drawBrick(grid, brick, brick.id)


def collapseBricks(grid: list[list[list[int | None]]], bricks: list[Brick]) -> None:
    for brick in bricks:
        while canBrickMoveDown(grid, brick):
            moveBrickDown(grid, brick)

def day22():
    part1 = 0
    part2 = 0
    X, Y, Z = 10, 10, 363
    # grid[z][y][x]
    grid = [[[None for x in range(X)] for y in range(Y)] for z in range(Z)]
    bricks: list[Brick] = []
    for i, line in enumerate(open('2023/inputs/day22.txt', 'r').read().splitlines()):
        start, end = line.strip().split('~')
        start = Point(*list(map(int, start.split(','))))
        end = Point(*list(map(int, end.split(','))))
        bricks.append(Brick(start, end, i+1))

    bricks.sort(key=lambda x: x.start.z)

    populateBricks(grid, bricks)
    collapseBricks(grid, bricks)

    canRemove: set[int] = set()


    for brick in bricks:
        drawBrick(grid, brick, None)
        for br in bricks:
            if br.id == brick.id:
                continue
            if canBrickMoveDown(grid, br):
                break
        else:
            canRemove.add(brick.id)
        drawBrick(grid, brick, brick.id)

    part1 = len(canRemove)

    # plt.rcParams["figure.figsize"] = [7.00, 3.50]
    # plt.rcParams["figure.autolayout"] = True
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # data = numpy.array(grid)
    # z, y, x = data.nonzero()
    # ax.scatter(x, y, z, c=z, alpha=1)
    # plt.show()
            

    return part1, part2

print(day22())