def day8():
    gridSize = 99
    part1 = 0
    # trees[row][col]
    trees = [[0 for i in range(gridSize)] for j in range(gridSize)]

    with open('2022/day8.txt') as f:
        for i, line in enumerate(f):
            line = line.strip('\n')
            for j, char in enumerate(line):
                trees[i][j] = int(char)
                    
        
        for i, rows in enumerate(trees):
            for j, tree in enumerate(trees[i]):
                if (i == 0 or i == (gridSize-1)) or (j == 0 or j == (gridSize-1)):
                    part1 += 1
                    continue

                rowVisibleLeft = True
                rowVisibleRight = True
                colVisibleTop = True
                colVisibleBottom = True

                for k in range(i):
                    if trees[k][j] >= trees[i][j]:
                        colVisibleTop = False
                        break
                for k in range(gridSize-(i+1)):
                    if trees[(gridSize-1)-k][j] >= trees[i][j]:
                        colVisibleBottom = False
                        break

                for n in range(j):
                    if trees[i][n] >= trees[i][j]:
                        rowVisibleLeft = False
                        break
                for n in range(gridSize-(j+1)):
                    if trees[i][(gridSize-1)-n] >= trees[i][j]:
                        rowVisibleRight = False
                        break
                if rowVisibleLeft or rowVisibleRight or colVisibleTop or colVisibleBottom:
                    part1 += 1
    
    return part1

print(day8())