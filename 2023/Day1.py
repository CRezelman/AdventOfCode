def day1(): 
    part1 = 0
    part2 = 0
    with open('2023/inputs/day1.txt') as f:
        for line in f:
            digits = []
            part2Digits = []

            for i, char in enumerate(line):
                if char.isdigit():
                    digits.append(char)
                    part2Digits.append(char)

                for j, value in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                    if line[i:].startswith(value):
                        part2Digits.append(str(j + 1))
            part1 += int(digits[0] + digits[-1])
            part2 += int(part2Digits[0] + part2Digits[-1])

    return part1, part2

print(day1())