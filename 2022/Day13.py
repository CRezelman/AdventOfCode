import ast

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def compare(first, second, index):

    if isinstance(first, int) and isinstance(second, int):
        if (first < second):
            print(index)
            return index
        elif (first > second):
            return False
        elif (first == second):
            return -1

    if isinstance(first, list) and isinstance(second, int):
        second = [second]

    if isinstance(first, int) and isinstance(second, list):
        first = [first]

    if isinstance(first, list) and isinstance(second, list):
        minLength = min(len(first), len(second))

        comp = -1
        for i in range(minLength):
            comp = compare(first[i], second[i], index)
            if comp != -1:
                return comp

        if (comp == -1):
            if len(first) > len(second):
                return False
            elif len(first) < len(second):
                print(index)
                return index
            elif len(first) == len(second):
                return -1


def day13():
    part1 = 0
    pairs = []
    with open('2022/inputs/day13.txt') as f:
        for i, line in enumerate(f):
            line = line.strip('\n')
            if i % 3 == 0:
                first = ast.literal_eval(line)
            elif i % 3 == 1:
                second = ast.literal_eval(line)
            elif i % 3 == 2:
                pairs.append(Pair(first, second))


    for j, pair in enumerate(pairs):
        part1 += compare(pair.first, pair.second, j+1)

    return part1

print(day13())