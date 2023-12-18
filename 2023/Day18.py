def shoelace_area(x: list[int], y: list[int]):
    a1, a2 = 0, 0
    x.append(x[0])
    y.append(y[0])
    for j in range(len(x) - 1):
        a1 += x[j] * y[j + 1]
        a2 += y[j] * x[j + 1]
    l = abs(a1 - a2) / 2
    return l


def day18():
    dirMap = { 0: 'R', 1: 'D', 2: 'L', 3: 'U' }
    perimiter1 = 0
    perimiter2 = 0
    x1, y1 = [0], [0]
    x2, y2 = [0], [0]
    current1 = (0, 0)
    current2 = (0, 0)

    with open('2023/inputs/day18.txt', 'r') as file:
        for line in file:
            direction, count, hexValue = line.split()
            count = int(count)
            perimiter1 += count

            if direction == 'R':
                current1 = (current1[0], current1[1] + count)
            elif direction == 'L':
                current1 = (current1[0], current1[1] - count)
            elif direction == 'U':
                current1 = (current1[0] - count, current1[1])
            elif direction == 'D':
                current1 = (current1[0] + count, current1[1])

            x1.append(current1[1])
            y1.append(current1[0])

            hexValue = hexValue.strip('()#')
            hexDir = dirMap[int(hexValue[-1])]
            hexValue = int(hexValue[:-1], 16)
            perimiter2 += hexValue

            if hexDir == 'R':
                current2 = (current2[0], current2[1] + hexValue)
            elif hexDir == 'L':
                current2 = (current2[0], current2[1] - hexValue)
            elif hexDir == 'U':
                current2 = (current2[0] - hexValue, current2[1])
            elif hexDir == 'D':
                current2 = (current2[0] + hexValue, current2[1])

            x2.append(current2[1])
            y2.append(current2[0])

    part1 = int(shoelace_area(x1, y1)) + perimiter1 // 2 + 1
    part2 = int(shoelace_area(x2, y2)) + perimiter2 // 2 + 1
    return part1, part2

print(day18())