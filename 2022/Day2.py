from enum import Enum

class ActionToTake(Enum):
    ROCK_OR_LOSE = 'X'
    PAPER_OR_DRAW = 'Y'
    SCISSORS_OR_WIN = 'Z'

class Shape(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'

class Score:
    part1 = 0
    part2 = 0

    def __str__(self) -> str:
        return str(self.__dict__)

    class Points(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

class Round():
    opponent: Shape
    actionToTake: ActionToTake
    class Outcome(Enum):
        WIN = 6
        DRAW = 3
        LOSE = 0

    def __init__(self, opponent: Shape, actionToTake: ActionToTake, score: Score):
        self.opponent = opponent
        self.actionToTake = actionToTake
        self.outcome(score)

    def outcome(self, score: Score):
        a = "ABC".index(self.opponent)
        b = "XYZ".index(self.actionToTake)

        score.part1 += b + 1

        res = (b - a) % 3

        if (res == 0):
            score.part1 += self.Outcome.DRAW.value
        elif (res == 1):
            score.part1 += self.Outcome.WIN.value
        elif (res == 2):
            score.part1 += self.Outcome.LOSE.value

        if (self.actionToTake == ActionToTake.ROCK_OR_LOSE.value):
            score.part2 += self.Outcome.LOSE.value + (a - 1) % 3 + 1
        elif (self.actionToTake == ActionToTake.PAPER_OR_DRAW.value):
            score.part2 += self.Outcome.DRAW.value + a + 1
        elif (self.actionToTake == ActionToTake.SCISSORS_OR_WIN.value):
            score.part2 += self.Outcome.WIN.value + (a + 1) % 3 + 1


def day2():
    score = Score()
    with open('2022/inputs/day2.txt') as f:
        for line in f:
            Round(line[0], line[2], score)
            
    return score

print(day2())