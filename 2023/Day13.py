
def checkSymmetry(mirror: list[str], allowedDiff: int):
    for y in range(len(mirror) - 1):
        dy = min(y, len(mirror) - y - 2)
        counts = [countDiff(mirror[y - j], mirror[y + j + 1]) for j in range(dy + 1)]

        if sum(counts) == allowedDiff:
            return y + 1
    return 0


def countDiff(mirror1: str, mirror2: str):
    if mirror1 == mirror2: return 0
    return sum(char1 != char2 for char1, char2 in zip(mirror1, mirror2))


def day13(): 
    part1 = 0
    part2 = 0

    for block in open('2023/inputs/day13.txt').read().split('\n\n'):
        mirror = block.splitlines()
        part1 += 100*(checkSymmetry(mirror, 0)) + checkSymmetry(list(zip(*mirror)), 0)
        part2 += 100*(checkSymmetry(mirror, 1)) + checkSymmetry(list(zip(*mirror)), 1)

    return part1, part2

print(day13())
