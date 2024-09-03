from collections import deque
from functools import reduce


def floodfill(height_map, x, y):
    q = deque()

    cols = len(height_map)
    rows = len(height_map[0])

    size = 0
    height_map[y][x] = 9

    q.append((x, y))

    while q:
        x, y = q.popleft()
        size += 1

        if x + 1 < rows and height_map[y][x+1] != 9:
            height_map[y][x+1] = 9
            q.append((x+1, y))
        if x - 1 >= 0 and height_map[y][x-1] != 9:
            height_map[y][x-1] = 9
            q.append((x-1, y))
        if y + 1 < cols and height_map[y+1][x] != 9:
            height_map[y+1][x] = 9
            q.append((x, y+1))
        if y - 1 >= 0 and height_map[y-1][x] != 9:
            height_map[y-1][x] = 9
            q.append((x, y-1))

    return size

def day9():
    part1 = 0
    part2 = 0
    with open('2021/inputs/day9.txt') as f:
        height_map = [[int(char) for char in line.strip()] for line in f]

    offsets = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    lowpoints = []

    for i, row in enumerate(height_map):
        for j, value in enumerate(row):
            neighbors = [height_map[i + dy][j + dx] if 0 <= i + dy < len(height_map) and 0 <= j + dx < len(row) else 10 for dy, dx in offsets]
            if all(value < x for x in neighbors):
                lowpoints.append((j, i))
                part1 += value + 1

    sizes = []
    for point in lowpoints:
        size = floodfill(height_map, point[0], point[1])
        sizes.append(size)
 
    sizes.sort(reverse=True)
    part2 = reduce((lambda x, y: x*y), sizes[:3])

    return part1, part2


print(day9())
