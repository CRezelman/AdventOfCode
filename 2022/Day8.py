def day8():
    gridSize = 99
    part1 = 0
    part2 = 0
    trees = [[0 for i in range(gridSize)] for j in range(gridSize)]

    with open('2022/day8.txt') as f:
        for i, line in enumerate(f):
            line = line.strip('\n')
            for j, char in enumerate(line):
                trees[i][j] = int(char)
                    
        
        for i, rows in enumerate(trees):
            for j, tree in enumerate(trees[i]):

                rowVisibleLeft = True
                rowVisibleRight = True
                colVisibleTop = True
                colVisibleBottom = True

                treesLeft = 0
                treesRight = 0
                treesUp = 0
                treesBottom = 0

                for k in range(i):
                    treesUp += 1
                    if trees[(i-1)-k][j] >= trees[i][j]:
                        colVisibleTop = False
                        break

                for k in range(gridSize-(i+1)):
                    treesBottom += 1
                    if trees[(i+1)+k][j] >= trees[i][j]:
                        colVisibleBottom = False
                        break


                for n in range(j):
                    treesLeft += 1
                    if trees[i][(j-1)-n] >= trees[i][j]:
                        rowVisibleLeft = False
                        break

                for n in range(gridSize-(j+1)):
                    treesRight += 1
                    if trees[i][(n+1)+j] >= trees[i][j]:
                        rowVisibleRight = False
                        break

                if rowVisibleLeft or rowVisibleRight or colVisibleTop or colVisibleBottom:
                    part1 += 1

                part2 = max(part2, treesRight*treesLeft*treesUp*treesBottom)
    
    return part1, part2

print(day8())