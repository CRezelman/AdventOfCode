
def day1():
    elves = []
    sum = 0
    with open('2022/day1.txt') as f:
        for line in f:
            if (line == '\n'):
                elves.append(sum)
                sum = 0
            else:
                sum += int(line)
    elves.sort(reverse=1)

    return elves[0], elves[0]+elves[1]+elves[2]

print(day1())