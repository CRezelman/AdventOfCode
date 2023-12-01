class ValidDigits:
    def __init__(self) -> None:
        self.part1 = dict({ '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9' })
        self.part2 = self.part1 | { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }
        pass
    def get(self, findStrings) -> dict:
        return self.part2 if findStrings else self.part1


def processLine(line: str, findStrings: bool) -> (str, str):
    validDigits = ValidDigits().get(findStrings)
    left = ''
    right = ''
    num1 = 0
    num2 = 0

    for i, char in enumerate(line):
        if num1 and num2:
            break
        left += char
        right += line[-1 - i]


        for numChar, value in validDigits.items():
            num1 = value if numChar in left and not num1 else num1
            num2 = value if numChar in right[::-1] and not num2 else num2
            if num1 and num2:
                break
    return int(num1 + num2)


def day1() -> int:
    part1 = 0
    part2 = 0
    with open('2023/inputs/day1.txt') as f:
        for line in f:
            part1 += processLine(line, False)
            part2 += processLine(line, True)

    return (part1, part2)

print(day1())
