from collections import deque

score_part1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

score_part2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def day10():
    part1 = 0
    part2 = 0
    q = deque()
    lines = []
    scores = []

    with open('2021/inputs/day10.txt') as f:
        for line in f:
            corrupted = False
            for char in line.strip():
                if char in ['(', '[', '{', '<']:
                    q.append(char)
                elif char in [')', ']', '}', '>']:
                    open_char = q.pop()
                    if char != pairs[open_char]:
                        part1 += score_part1[char]
                        corrupted = True

            if not corrupted:
                lines.append(line.strip())

    for line in lines:
        q = deque()
        for char in line:
            if char in ['(', '[', '{', '<']:
                q.append(char)
            elif char in [')', ']', '}', '>']:
                q.pop()

        score = 0
        q.reverse()
        for char in q:
            score = score * 5 + score_part2[pairs[char]]

        scores.append(score)

    scores.sort()
    part2 = scores[int((len(scores) - 1)/2)]

    return part1, part2


print(day10())
