class Number:
    def __init__(self, startX: int, endX: int, y: int) -> None:
        self.startX = startX
        self.endX = endX
        self.y = y
        self.stars = set()
        self.number: int = 0
        pass

    def addStar(self, x: int, y: int):
        self.stars.add((x, y))

    def defineNumber(self, number: int):
        self.number = number


def day6(): 
    part1 = 0
    part2 = 0
    symbols = {'*', '+', '$', '%', '@', '=', '/', '#', '&', '-'}

    schematic: list[list[str]] = []

    with open('2023/inputs/day3.txt') as f:
        schematic = [list(line) for line in f]


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
        num = ''.join(schematic[number.y][number.startX:number.endX + 1])
        number.defineNumber(int(num))

        for i in range(number.startX - 1, number.endX + 2):
            for j in range(number.y - 1, number.y + 2):
                if 0 <= i < len(schematic[0]) and 0 <= j < len(schematic) and schematic[j][i] in symbols:
                    validNumbers.add(number)
                    if schematic[j][i] == '*':
                        number.addStar(i, j)


    for validNumber in validNumbers:
        part1 += int(validNumber.number)

    starDict: dict[tuple[int, int], list[Number]] = dict()

    for number in numbersFound:
        for star in number.stars:
            starDict.setdefault(star, []).append(number)

    for star in starDict.items():
        if len(star[1]) == 2:
            part2 += star[1][0].number*star[1][1].number


    return part1, part2


print(day6())