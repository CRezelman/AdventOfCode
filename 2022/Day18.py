
def day18():
    part1 = 0

    lava = [[[0 for i in range(25)] for j in range(25)] for k in range(25)]
    with open('C:/Git/AdventOfCode/2022/inputs/day18.txt') as f:
        for line in f:
            line = line.strip('\n')
            x, y, z = line.split(',')

            lava[int(x)][int(y)][int(z)] = 1

        for i, x in enumerate(lava):
            for j, y in enumerate(lava[i]):
                for k, z in enumerate(lava[j]):
                    if lava[i][j][k] == 1:
                        if lava[i+1][j][k] != 1:
                            part1 += 1
                        if lava[i-1][j][k] != 1:
                            part1 += 1
                        if lava[i][j+1][k] != 1:
                            part1 += 1
                        if lava[i][j-1][k] != 1:
                            part1 += 1
                        if lava[i][j][k+1] != 1:
                            part1 += 1
                        if lava[i][j][k-1] != 1:
                            part1 += 1

    return part1


print(day18())
