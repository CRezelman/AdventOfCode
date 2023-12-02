from enum import Enum

class Colours(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

class AllowedColours(Enum):
    RED = 12
    GREEN = 13
    BLUE = 14
class GameInfo:
    def __init__(self, colour: Colours, number: int):
        self.colour = colour
        self.number = number


class Game:
    def __init__(self, id: int) -> None:
        self.id = id
        self.info: list[GameInfo] = []
        self.maxRed = 0
        self.maxGreen = 0
        self.maxBlue = 0

    def addInfo(self, colour: Colours, number: int):
        info = GameInfo(colour, number)
        self.info.append(info)

def day1(): 
    part1 = 0
    part2 = 0
    games: list[Game] = []
    with open('2023/inputs/day2.txt') as f:
        for line in f:
            split = line.strip('\n').replace(';', ',').split(':')
            id = split[0].split(' ')[1]
            game = Game(id)

            infoSplit = split[1].strip().split(', ')

            for info in infoSplit:
                gameInfo = info.split(' ')
                game.addInfo(gameInfo[1], int(gameInfo[0]))
            
            games.append(game)

    
    for game in games:
        valid = True

        for info in game.info:
            if info.colour == Colours.RED.value:
                game.maxRed = max(info.number, game.maxRed)
                if info.number > AllowedColours.RED.value:
                    valid = False
            if info.colour == Colours.GREEN.value:
                game.maxGreen = max(info.number, game.maxGreen)
                if info.number > AllowedColours.GREEN.value:
                    valid = False
            if info.colour == Colours.BLUE.value:
                game.maxBlue = max(info.number, game.maxBlue)
                if info.number > AllowedColours.BLUE.value:
                    valid = False
        if valid:
            part1 += int(game.id)
        part2 += game.maxRed*game.maxGreen*game.maxBlue

    return part1, part2

print(day1())