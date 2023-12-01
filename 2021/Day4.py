class Board:
    def __init__(self) -> None:
        self.board = [[0 for i in range(5)] for j in range(5)]
        self.hasWon = False
        pass

    def populateRow(self, row: list[int], index: int):
        self.board[index] = row

    def markNumber(self, number: int) -> None:
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == number:
                    self.board[i][j] = '#'

    def checkWinner(self) -> bool:
        for row in self.board:
            if all(value == '#' for value in row):
                self.hasWon = True
                return True

        for col_index in range(len(self.board[0])):
            if all(row[col_index] == '#' for row in self.board):
                self.hasWon = True
                return True

        return False

def day1(): 
    part1 = 0
    part2 = 0
    boards: list[Board] = []
    with open('2021/inputs/day4.txt') as f:
        for i, line in enumerate(f):
            if i == 0:
                numbers = line.strip('\n').split(",")
            elif (i % 6 == 1):
                currentBoard = Board()
            else:
                row = [int(x) for x in line.strip('\n').strip(' ').replace('  ', ' ').split(' ')]
                currentBoard.populateRow(row, (i-2) % 6)
                if i % 6 == 0:
                    boards.append(currentBoard)

    winners: list[Board] = []
    winningNumbers: list[int] = []
    for number in numbers:
        for board in boards:
            if not board.hasWon:
                board.markNumber(int(number))
                if board.checkWinner():
                    winners.append(board)
                    winningNumbers.append(int(number))

    for row in winners[0].board:
        for value in row:
            if value != '#':
                part1 += value

    for row in winners[-1].board:
        for value in row:
            if value != '#':
                part2 += value

    return part1*winningNumbers[0], part2*winningNumbers[-1]

print(day1())
