class Number:
    def __init__(self, startX: int, endX: int, y: int) -> None:
        self.startX = startX
        self.endX = endX
        self.y = y
        self.stars = set()
        pass

    def addStar(self, x: int, y: int):
        self.stars.add((x, y))

    def defineNumber(self, number: int):
        self.number = number


def day6(): 
    part1 = 0
    part2 = 0
    symbols = ['*', '+', '$', '%', '@', '=', '/', '#', '&', '-']

    schematic: list[list[str]] = []

    with open('2023/inputs/day3.txt') as f:
        for i, line in enumerate(f):
            schematic.append([])
            for j, char in enumerate(line):
                schematic[i].append(char)


    numbersFound: list[Number] = []
    for i, line in enumerate(schematic):   
        start = None
        end = None
        for j, char in enumerate(line):
            if char.isdigit():
                if start is None:
                    start = j
                if start is not None:
                    end = j
            elif start is not None and end is not None:
                numbersFound.append(Number(int(start), int(end), int(i)))
                start = None
                end = None

    validNumbers: set[Number] = set()

    for number in numbersFound:
        num = ''
        for i in range(number.endX - number.startX + 1):
            num += schematic[number.y][number.startX + i]
        number.defineNumber(int(num))

        if (number.startX -1) >= 0 and schematic[number.y][number.startX - 1] in symbols:
            validNumbers.add(number)
            if schematic[number.y][number.startX - 1] == '*':
                number.addStar(number.startX-1, number.y)
        if (number.endX +1) <= (len(schematic[0]) + 1) and schematic[number.y][number.endX + 1] in symbols:
            validNumbers.add(number)
            if schematic[number.y][number.endX + 1] == '*':
                number.addStar(number.endX+1, number.y)

        for i in range(number.endX - number.startX + 1 + 2):
            if (number.y - 1) >= 0 and (number.startX -1 + i) >= 0 and schematic[number.y - 1][number.startX -1 + i] in symbols:
                validNumbers.add(number)
                if schematic[number.y - 1][number.startX -1 + i] == '*':
                    number.addStar(number.startX -1 + i, number.y - 1)
            if (number.y - 1) >= 0 and (number.endX +1 + i) <= (len(schematic[0]) - 1) and schematic[number.y - 1][number.startX -1 + i] in symbols:
                validNumbers.add(number)
                if schematic[number.y - 1][number.startX -1 + i] == '*':
                    number.addStar(number.startX -1 + i, number.y - 1)
            if (number.y + 1) <= (len(schematic) - 1) and (number.startX -1 + i) >= 0 and schematic[number.y + 1][number.startX -1 + i] in symbols:
                validNumbers.add(number)
                if schematic[number.y + 1][number.startX -1 + i] == '*':
                    number.addStar(number.startX -1 + i, number.y + 1)
            if (number.y + 1) <= (len(schematic) - 1) and (number.endX +1 + i) <= (len(schematic[0]) - 1) and schematic[number.y + 1][number.startX -1 + i] in symbols:
                validNumbers.add(number)
                if schematic[number.y + 1][number.startX -1 + i] == '*':
                    number.addStar(number.startX -1 + i, number.y + 1)


    for validNumber in validNumbers:
        part1 += int(validNumber.number)

    starDict = dict()

    for number in numbersFound:
        for star in number.stars:
            if starDict.get(star):
                starDict[star] += [number]
            else: 
                starDict[star] = [number]

    for star in starDict.items():
        if len(star[1]) == 2:
            part2 += star[1][0].number*star[1][1].number


    return part1, part2


print(day6())