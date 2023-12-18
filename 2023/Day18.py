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
    perimiter = 0
    x, y = [0], [0]
    current = (0, 0)

    with open('2023/inputs/day18.txt', 'r') as file:
        for line in file:
            direction, count, hex_value = line.split()
            count = int(count)
            perimiter += count

            if direction == 'R':
                current = (current[0], current[1] + count)
            elif direction == 'L':
                current = (current[0], current[1] - count)
            elif direction == 'U':
                current = (current[0] - count, current[1])
            elif direction == 'D':
                current = (current[0] + count, current[1])

            x.append(current[1])
            y.append(current[0])

    part1 = int(shoelace_area(x, y)) + perimiter // 2 + 1
    return part1, 0

print(day18())