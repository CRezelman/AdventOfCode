from enum import Enum

class ActionToTake(Enum):
    ROCK_OR_WIN = 'X'
    PAPER_OR_DRAW = 'Y'
    SCISSORS_OR_LOSE = 'Z'

class Opponent(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'

class Points(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Outcome(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0

def day2():
    score = [0, 0]
    with open('2022/day2.txt') as f:
        for line in f:
            round = line.strip('\n').split(' ')
            if (round[1] == ActionToTake.ROCK_OR_WIN.value):
                score[0] += Points.ROCK.value
                score[1] += Outcome.LOSE.value
                if (round[0] == Opponent.ROCK.value):
                    score[0] += Outcome.DRAW.value
                    score[1] += Points.SCISSORS.value
                elif (round[0] == Opponent.PAPER.value):
                    score[0] += Outcome.LOSE.value
                    score[1] += Points.ROCK.value
                elif (round[0] == Opponent.SCISSORS.value):
                    score[0] += Outcome.WIN.value
                    score[1] += Points.PAPER.value
            elif (round[1] == ActionToTake.PAPER_OR_DRAW.value):
                score[0] += Points.PAPER.value
                score[1] += Outcome.DRAW.value
                if (round[0] == Opponent.ROCK.value):
                    score[0] += Outcome.WIN.value
                    score[1] += Points.ROCK.value
                elif (round[0] == Opponent.PAPER.value):
                    score[0] += Outcome.DRAW.value
                    score[1] += Points.PAPER.value
                elif (round[0] == Opponent.SCISSORS.value):
                    score[0] += Outcome.LOSE.value
                    score[1] += Points.SCISSORS.value
            elif (round[1] == ActionToTake.SCISSORS_OR_LOSE.value):
                score[0] += Points.SCISSORS.value
                score[1] += Outcome.WIN.value
                if (round[0] == Opponent.ROCK.value):
                    score[0] += Outcome.LOSE.value
                    score[1] += Points.PAPER.value
                elif (round[0] == Opponent.PAPER.value):
                    score[0] += Outcome.WIN.value
                    score[1] += Points.SCISSORS.value
                elif (round[0] == Opponent.SCISSORS.value):
                    score[0] += Outcome.DRAW.value
                    score[1] += Points.ROCK.value

    return score

print(day2())