"""Day 13"""
import numpy as np

def day13():
    """Day 13"""
    part1 = 0
    part2 = 0

    prev_points = set()
    folds = []


    new_line_count = 0
    for line in open('2021/inputs/day13.txt', 'r').read().splitlines():
        if line == '':
            new_line_count += 1
            continue

        if new_line_count == 0:
            x, y = line.split(',')
            prev_points.add((int(x), int(y)))
        if new_line_count == 1:
            axis, l = line.split('=')
            folds.append((axis[-1], int(l)))

    for i, fold in enumerate(folds):
        new_points = set()
        axis, line = fold

        for x, y in prev_points:
            if axis == 'y':
                if y > line:
                    new_points.add((x, 2*line - y))
                else:
                    new_points.add((x, y))
            if axis == 'x':
                if x > line:
                    new_points.add((2*line - x, y))
                else:
                    new_points.add((x, y))
        prev_points = new_points
        if i == 0:
            part1 = len(new_points)


    rows = 6
    cols = 40 
    grid = np.full((rows, cols), '.')
    for x, y in new_points:
        grid[y][x] = '#'

    for row in grid:
        print(' '.join(row))

    return part1, part2

print(day13())
