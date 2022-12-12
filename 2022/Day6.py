def day6():
    part1 = 0
    part2 = 0
    with open('2022/inputs/day6.txt') as f:
        for line in f:
            for i, char in enumerate(line):
                if (i - 3 >= 0 and part1 == 0) and len(set([line[i-j] for j in range(4)])) == 4:
                    part1 = i + 1
                if (i - 13 >= 0 and part2 == 0) and len(set([line[i-j] for j in range(14)])) == 14:
                    part2 = i + 1
    return part1, part2

print(day6())