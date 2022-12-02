from enum import Enum

class ActionToTake(Enum):
    ROCK_OR_WIN = 'X'
    PAPER_OR_DRAW = 'Y'
    SCISSORS_OR_LOSE = 'Z'

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
        if (self.actionToTake == ActionToTake.ROCK_OR_WIN.value):
            score.part1 += score.Points.ROCK.value
            score.part2 += self.Outcome.LOSE.value

            if (self.opponent == Shape.ROCK.value):
                score.part1 += self.Outcome.DRAW.value
                score.part2 += score.Points.SCISSORS.value
            elif (self.opponent == Shape.PAPER.value):
                score.part1 += self.Outcome.LOSE.value
                score.part2 += score.Points.ROCK.value
            elif (self.opponent == Shape.SCISSORS.value):
                score.part1 += self.Outcome.WIN.value
                score.part2 += score.Points.PAPER.value

        elif (self.actionToTake == ActionToTake.PAPER_OR_DRAW.value):
            score.part1 += score.Points.PAPER.value
            score.part2 += self.Outcome.DRAW.value

            if (self.opponent == Shape.ROCK.value):
                score.part1 += self.Outcome.WIN.value
                score.part2 += score.Points.ROCK.value
            elif (self.opponent == Shape.PAPER.value):
                score.part1 += self.Outcome.DRAW.value
                score.part2 += score.Points.PAPER.value
            elif (self.opponent == Shape.SCISSORS.value):
                score.part1 += self.Outcome.LOSE.value
                score.part2 += score.Points.SCISSORS.value

        elif (self.actionToTake == ActionToTake.SCISSORS_OR_LOSE.value):
            score.part1 += score.Points.SCISSORS.value
            score.part2 += self.Outcome.WIN.value
            
            if (self.opponent == Shape.ROCK.value):
                score.part1 += self.Outcome.LOSE.value
                score.part2 += score.Points.PAPER.value
            elif (self.opponent == Shape.PAPER.value):
                score.part1 += self.Outcome.WIN.value
                score.part2 += score.Points.SCISSORS.value
            elif (self.opponent == Shape.SCISSORS.value):
                score.part1 += self.Outcome.DRAW.value
                score.part2 += score.Points.ROCK.value


def day2():
    score = Score()
    with open('2022/day2.txt') as f:
        for line in f:
            Round(line[0], line[2], score)

    return score

print(day2())