def day6():
    lights1 = [[0 for x in range(1000)] for y in range(1000)]
    lights2 = [[0 for x in range(1000)] for y in range(1000)]
    lightCount1 = 0
    lightCount2 = 0
    with open('2015/inputs/day6.txt') as f:
        for line in f:
            switch = line.split(' ')
            action = ''
            if 'toggle' in line:
                startX, startY = switch[1].split(',')
                endX, endY = switch[3].split(',')

                for i in range(int(endX)-int(startX) + 1):
                    for j in range(int(endY)-int(startY) + 1):
                        lights1[int(startX) + i][int(startY) +
                                                 j] = not lights1[int(startX) + i][int(startY) + j]
                        lights2[int(startX) + i][int(startY) +
                                                 j] = lights2[int(startX) + i][int(startY) + j] + 2

            if 'turn on' in line:
                startX, startY = switch[2].split(',')
                endX, endY = switch[4].split(',')

                for i in range(int(endX)-int(startX) + 1):
                    for j in range(int(endY)-int(startY) + 1):
                        lights1[int(startX) + i][int(startY) + j] = 1
                        lights2[int(startX) + i][int(startY) + j] += 1

            if 'turn off' in line:
                startX, startY = switch[2].split(',')
                endX, endY = switch[4].split(',')

                for i in range(int(endX)-int(startX) + 1):
                    for j in range(int(endY)-int(startY) + 1):
                        lights1[int(startX) + i][int(startY) + j] = 0
                        if lights2[int(startX) + i][int(startY) + j] > 0:
                            lights2[int(startX) + i][int(startY) + j] -= 1

    for i in range(len(lights1)):
        for j in range(len(lights1[i])):
            if lights1[i][j]:
                lightCount1 += 1
    for i in range(len(lights2)):
        for j in range(len(lights2[i])):
            lightCount2 += lights2[i][j]

    return lightCount1, lightCount2


print(day6())
