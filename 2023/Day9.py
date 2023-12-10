def day9(): 
    part1 = 0
    part2 = 0
    patterns: list[int] = []
    with open('2023/inputs/day9.txt', 'r') as f:
        for line in f:
            patterns.append([int(x) for x in line.strip().split(' ')])

    for pattern in patterns:
        diffs: list[list[int]] = [pattern]
        count = 0
        while True:
            nextDiff = [diffs[count][i + 1] - diffs[count][i] for i in range(len(diffs[count]) - 1)]
            diffs.append(nextDiff)

            if all(value == 0 for value in nextDiff):
                part1 += sum([x[-1] for x in diffs])
                part2 += sum((-1) ** i * num for i, num in enumerate([x[0] for x in diffs]))
                break

            count += 1

    return part1, part2

print(day9())