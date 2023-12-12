import itertools

def day11(): 
    part1 = 0
    part2 = 0
    with open('2023/inputs/day11.txt', 'r') as f:
       starMap = [list(line.strip()) for line in f]
    
    cols = [col_index for col_index in range(len(starMap[0])) if all(row[col_index] == '.' for row in starMap)]
    rows = [y for y, row in enumerate(starMap) if all(value == '.' for value in row)]
    galaxies = {(i, j) for i, row in enumerate(starMap) for j, value in enumerate(row) if value == '#'}


    for c in itertools.combinations(galaxies, 2):
        minY, maxY = sorted([c[0][0], c[1][0]])
        minX, maxX = sorted([c[0][1], c[1][1]])
        extrasP1 = sum(1 for col in cols if minX <= col <= maxX) + sum(1 for row in rows if minY <= row <= maxY)
        extrasP2 = extrasP1 * (1000000 - 1)

        part1 += maxX - minX + maxY - minY + extrasP1
        part2 += maxX - minX + maxY - minY + extrasP2

    return part1, part2

print(day11())