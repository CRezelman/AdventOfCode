import itertools

def day11(): 
    part1 = 0
    part2 = 0
    with open('2023/inputs/day11.txt', 'r') as f:
       starMap = [list(line.strip()) for line in f]
    
    cols = []
    rows = []

    for y, row in enumerate(starMap):
        if all(value == '.' for value in row):
            rows.append(y)

    for col_index in range(len(starMap[0])):
        if all(row[col_index] == '.' for row in starMap):
            cols.append(col_index)

    galaxies = set()

    for i, row in enumerate(starMap):
        for j, value in enumerate(row):
            if starMap[i][j] == '#':
                galaxies.add((i, j))

    comb = itertools.combinations(galaxies, 2)

    for c in comb:
        minY = min(c[0][0], c[1][0])
        maxY = max(c[0][0], c[1][0])
        minX = min(c[0][1], c[1][1])
        maxX = max(c[0][1], c[1][1])
        extrasP1 = 0
        extrasP2 = 0

        for col in cols:
            if minX <= col <= maxX:
                extrasP1 += 1
                extrasP2 += 1000000 - 1

        for row in rows:
            if minY <= row <= maxY:
                extrasP1 += 1
                extrasP2 += 1000000 - 1

        part1 += maxX - minX + maxY - minY + extrasP1
        part2 += maxX - minX + maxY - minY + extrasP2

    

    return part1, part2

print(day11())