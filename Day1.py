
def day1():
    with open('day1.txt') as f:
        elves = []
        sum = 0
        for line in f:
            if (line == '\n'):
                elves.append(sum)
                sum = 0
            else:
                sum += int(line)
    elves.sort(reverse=1)

    return elves[0], elves[0]+elves[1]+elves[2]

print(day1())