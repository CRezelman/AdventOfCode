
def checkSymmetry(mirror):
    for y in range(len(mirror) - 1):
        dy = min(y, len(mirror) - y - 2)
        for j in range(dy + 1):
            if mirror[y - j] != mirror[y + j + 1]:
                break
        else:
            return y+1
    return False


def day13(): 
    part1 = 0
    part2 = 0
    mirrors = []
    with open('2023/inputs/day13.txt', 'r') as f:
        currentMirror = []
        for line in f:
                if line == '\n':
                    mirrors.append(currentMirror)
                    currentMirror = []
                else:
                    currentMirror.append(line.strip())
        mirrors.append(currentMirror)


    for mirror in mirrors:
        part1 += 100*(int(checkSymmetry(mirror)))
        transpose = list(zip(*mirror))
        part1 += int(checkSymmetry(transpose))

    return part1, part2

print(day13())
