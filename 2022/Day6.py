def day6():
    part1 = 0
    part2 = 0
    with open('2022/day6.txt') as f:
        for line in f:
            for i, char in enumerate(line):
                substring1 = line[i-3:i+1]
                substring2 = line[i-13:i+1]
                dups1 = []
                dups2 = []
                if i > 3:
                    for sub in substring1:
                        if substring1.count(sub) > 1 and sub not in dups1:
                            dups1.append(sub)
                    if (len(dups1) == 0 and part1 == 0):
                        part1 = i + 1

                if i > 13:
                    for sub in substring2:
                        if substring2.count(sub) > 1 and sub not in dups2:
                            dups2.append(sub)
                    if (len(dups2) == 0  and part2 == 0):
                        part2 = i + 1

    return part1, part2

print(day6())