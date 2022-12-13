import ast
from functools import cmp_to_key

def compare(first, second):

    if isinstance(first, int) and isinstance(second, int):
        return 0 if first == second else (-1 if first > second else 1)

    if isinstance(first, list) and isinstance(second, int):
        second = [second]

    if isinstance(first, int) and isinstance(second, list):
        first = [first]

    if isinstance(first, list) and isinstance(second, list):
        minLength = min(len(first), len(second))
        comp = 0

        for i in range(minLength):
            comp = compare(first[i], second[i])
            if comp != 0:
                return comp

        if (comp == 0):
            return 0 if len(first) == len(second) else (-1 if len(first) > len(second) else 1)


def day13():
    part1 = 0
    part2 = 1
    messages1 = []
    messages2 = [[[2]], [[6]]]

    with open('2022/inputs/day13.txt') as f:
        for i, line in enumerate(f):
            line = line.strip('\n')
            if i % 3 == 0:
                first = ast.literal_eval(line)
                messages2.append(ast.literal_eval(line))
            elif i % 3 == 1:
                second = ast.literal_eval(line)
                messages2.append(ast.literal_eval(line))
            elif i % 3 == 2:
                messages1.append([first, second])


    for j, msg in enumerate(messages1):
        if compare(msg[0], msg[1]) > -1:
            part1 += (j+1)
    
    messages2 = sorted(messages2, key=cmp_to_key(compare), reverse=1)

    for n, msg in enumerate(messages2):
        if msg == [[2]] or msg == [[6]]:
            part2 *= (n+1)

    return part1, part2

print(day13())