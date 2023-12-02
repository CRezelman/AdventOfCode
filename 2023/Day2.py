class GameInfo:
    def __init__(self, colour: str, number: int):
        self.colour = colour
        self.number = number


class Game:
    def __init__(self, id: int) -> None:
        self.id = id
        self.info: list[GameInfo] = []

    def addInfo(self, colour: str, number: int):
        info = GameInfo(colour, number)
        self.info.append(info)

def day1(): 
    part1 = 0
    part2 = 0
    allowedRed = 12
    allowedGreen = 13
    allowedBlue = 14
    games: list[Game] = []
    allowedGames: list[Game] = []
    with open('2023/inputs/day2.txt') as f:
        for line in f:
            line = line.strip('\n')
            line = line.replace(';', ',')
            split = line.split(':')
            id = split[0].split(' ')[1]
            game = Game(id)

            infoSplit = split[1].strip().split(', ')

            for info in infoSplit:
                gameInfo = info.split(' ')
                game.addInfo(gameInfo[1], int(gameInfo[0]))
            
            games.append(game)

    
    for game in games:
        for info in game.info:
            if info.colour == 'red' and info.number > allowedRed:
                break
            if info.colour == 'green' and info.number > allowedGreen:
                break
            if info.colour == 'blue' and info.number > allowedBlue:
                break
        else:
            allowedGames.append(game)

    for allowedGame in allowedGames:
        part1 += int(allowedGame.id)

    for game in games:
        maxRed = 0
        maxGreen = 0
        maxBlue = 0

        for info in game.info:
            if info.colour == 'red':
                maxRed = max(info.number, maxRed)
            if info.colour == 'green':
                maxGreen = max(info.number, maxGreen)
            if info.colour == 'blue':
                maxBlue = max(info.number, maxBlue)
        part2 += maxRed*maxGreen*maxBlue


    return part1, part2

print(day1())