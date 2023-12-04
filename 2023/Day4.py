from functools import reduce

class Card:
    def __init__(self, winninerNumbers: list[int], cardNumbers: list[int]) -> None:
        self.winningNumbers = winninerNumbers
        self.cardNumbers = cardNumbers
        self.count = 1
        self.matches = 0

    def addCount(self, count):
        self.count += count


def day4(): 
    part1 = 0
    part2 = 0
    cards: list[Card] = []
    with open('2023/inputs/day4.txt') as f:
        for line in f:
            line = line.strip('\n')
            cardNo, values = line.split(':')
            winnners, card = values.split(' | ')
            winningNumbers = [int(x) for x in winnners.strip().replace('  ', ' ').split(' ')]
            cardNumbers = [int(x) for x in card.strip().replace('  ', ' ').split(' ')]
            cards.append(Card(winningNumbers, cardNumbers))

    for i, card in enumerate(cards):
        card.matches = reduce(lambda x, y: x+card.winningNumbers.count(y), set(card.cardNumbers), 0)
        if card.matches > 0: 
            part1 += 2**(card.matches - 1)
        for j in range(card.matches):
            cards[i + 1 + j].addCount(card.count)
        part2 += card.count

    return part1, part2

print(day4())