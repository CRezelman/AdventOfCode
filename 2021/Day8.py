

def day8():
    part1 = 0
    part2 = 0
    with open('2021/inputs/day8.txt') as f:
        for line in f:
            line = line.strip('\n')
            input, output = line.split(' | ')
            for digit in output.split(' '):
                if len(digit) in [2, 4, 3, 7]:
                    part1 += 1

    return part1, part2


print(day8())