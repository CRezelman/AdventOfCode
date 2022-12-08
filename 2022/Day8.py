def day8():
    gridSize = 99
    part1 = 0
    part2 = 0
    trees = [[0 for i in range(gridSize)] for j in range(gridSize)]
    scores = []

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
                    if trees[(i-1)-k][j] >= trees[i][j]:
                        colVisibleTop = False
                        treesUp += 1
                        break
                    else:
                        treesUp += 1

                for k in range(gridSize-(i+1)):
                    if trees[(i+1)+k][j] >= trees[i][j]:
                        colVisibleBottom = False
                        treesBottom += 1
                        break
                    else:
                        treesBottom += 1


                for n in range(j):
                    if trees[i][(j-1)-n] >= trees[i][j]:
                        rowVisibleLeft = False
                        treesLeft += 1
                        break
                    else:
                        treesLeft += 1

                for n in range(gridSize-(j+1)):
                    if trees[i][(n+1)+j] >= trees[i][j]:
                        rowVisibleRight = False
                        treesRight += 1
                        break
                    else:
                        treesRight += 1

                if rowVisibleLeft or rowVisibleRight or colVisibleTop or colVisibleBottom:
                    part1 += 1
                
                scores.append(treesRight*treesLeft*treesUp*treesBottom)

        part2 = max(scores)
    
    return part1, part2

print(day8())