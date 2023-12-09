from enum import Enum
from functools import cmp_to_key

class HandTypes(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1
    NONE = 0

class Hand:
    def __init__(self, hand: str, bid: int) -> None:
        self.hand = hand
        self.bid = bid
        self.rank = 0
        self.matches = {}
        self.type = HandTypes.NONE.value
        self.jokers = 0

    def addMatches(self, matches: dict):
        self.matches = matches
        # No matches | 1 Joker
        if len(matches) == 0:
            if self.jokers == 1:
                self.type = HandTypes.ONE_PAIR
            else:
                self.type = HandTypes.HIGH_CARD

        # 1 Match | 1, 2, 3, 4 or 5 Jokers
        elif len(matches) == 1:
            value = list(self.matches.values())[0]
            if self.jokers == 1:
                if value == 2:
                    self.type = HandTypes.THREE_OF_A_KIND
                elif value == 3:
                    self.type = HandTypes.FOUR_OF_A_KIND
                elif value == 4:
                    self.type = HandTypes.FIVE_OF_A_KIND
            elif self.jokers == 2:
                self.type = HandTypes.THREE_OF_A_KIND
            elif self.jokers == 3:
                self.type = HandTypes.FOUR_OF_A_KIND
            elif self.jokers == 4:
                self.type = HandTypes.FIVE_OF_A_KIND
            elif self.jokers == 5:
                self.type = HandTypes.FIVE_OF_A_KIND
            else:
                if value == 2:
                    self.type = HandTypes.ONE_PAIR
                elif value == 3:
                    self.type = HandTypes.THREE_OF_A_KIND
                elif value == 4:
                    self.type = HandTypes.FOUR_OF_A_KIND
                elif value == 5:
                    self.type = HandTypes.FIVE_OF_A_KIND

        # 2 Matches | 1, 2 or 3 Jokers
        elif len(matches) == 2:
            values = list(self.matches.values())
            if self.jokers == 1:
                if values[0] == 2 and values[1] == 2:
                    self.type = HandTypes.FULL_HOUSE
            elif self.jokers == 2:
                if values[0] == 2 and values[1] == 2:
                    self.type = HandTypes.FOUR_OF_A_KIND
                if (values[0] == 2 and values[1] == 3) or (values[1] == 2 and values[0] == 3):
                    self.type = HandTypes.FIVE_OF_A_KIND
            elif self.jokers == 3:
                self.type = HandTypes.FIVE_OF_A_KIND
            else:
                if values[0] == 2 and values[1] == 2:
                    self.type = HandTypes.TWO_PAIR
                if (values[0] == 2 and values[1] == 3) or (values[1] == 2 and values[0] == 3):
                    self.type = HandTypes.FULL_HOUSE

def countMatchingCharacters(string: str, includeJokers: bool):
    charCount = {}
    jokers = 0

    for char in string:
        if char == 'J' and includeJokers: 
            jokers += 1
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1

    matchingCharacters = {key: value for key, value in charCount.items() if value > 1}

    return matchingCharacters, jokers

def compare(a: Hand, b: Hand):
    cardValues = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    if a.type.value > b.type.value:
        return 1
    elif a.type.value == b.type.value:
        for char1, char2 in zip(a.hand, b.hand):
            value1 = cardValues.get(char1)
            value2 = cardValues.get(char2)
            if value1 > value2: return 1
            elif value1 < value2: return -1
    else: 
        return -1

def compareWithJokers(a: Hand, b: Hand):
    cardValues = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
    if a.type.value > b.type.value:
        return 1
    elif a.type.value == b.type.value:
        for char1, char2 in zip(a.hand, b.hand):
            value1 = cardValues.get(char1)
            value2 = cardValues.get(char2)
            if value1 > value2: return 1
            elif value1 < value2: return -1
    else: 
        return -1


def day7(includeJokers: bool): 
    result = 0
    hands: list[Hand] = []
    with open('2023/inputs/day7.txt', 'r') as f:
        for line in f:
            hand, bid = line.strip().split()
            current = Hand(hand, int(bid))
            matches, jokers = countMatchingCharacters(current.hand, includeJokers)
            current.jokers = jokers
            current.addMatches(matches)
            hands.append(current)

    hands = sorted(hands, key=cmp_to_key(compareWithJokers if includeJokers else compare))
    result = sum(hand.bid * (i + 1) for i, hand in enumerate(hands))


    return result

print((day7(False), day7(True)))

